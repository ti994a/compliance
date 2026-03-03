# NIST Compliance LLM Evaluation Framework

A comprehensive system for evaluating Large Language Model (LLM) performance on NIST SP 800-53 compliance scenarios to assess price/performance characteristics across different models.

## Overview

This project implements an end-to-end pipeline that transforms NIST cybersecurity controls into realistic compliance scenarios, then evaluates various LLMs' ability to correctly assess compliance. It provides data-driven insights into which models offer the best price/performance ratio for compliance automation tasks.

Goals:

 - Test LLM accuracy on complex regulatory compliance scenarios

 - Compare model performance across different LLMs (Claude variants, Nova Premier, Nova 2 Lite)

 - Support cost-effectiveness by tracking token usage for price/performance analysis

 - Evaluate reasoning quality through detailed explanations from each model

 - Assess scenario complexity impact by varying the number of policies referenced (4, 6, 8, 10 policies per scenario)


## Pipeline Flow

```
    ┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
    │   STEP 1     │      │   STEP 2     │      │   STEP 3     │      │   STEP 4     │
    │   Generate   │ ───▶ │   Generate   │ ───▶ │   Generate   │ ───▶ │    Judge     │
    │   Controls   │      │   Policies   │      │   Scenarios  │      │   Scenarios  │
    └──────────────┘      └──────────────┘      └──────────────┘      └──────────────┘
          │                     │                     │                     │
          ▼                     ▼                     ▼                     ▼
    ┌──────────────┐      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
    │ NIST Catalog │      │  Bedrock LLM │      │  Bedrock LLM │      │ Multi-Model  │
    │    (JSON)    │      │  (Claude/Nova)│      │  (Scenario   │      │  Evaluation  │
    │      ↓       │      │      ↓       │      │   Generator) │      │  + Metrics   │
    │ JSONL + MD   │      │ Policy MD    │      │      ↓       │      │      ↓       │
    │   Files      │      │   Files      │      │ 1,000 JSONL  │      │ Accuracy +   │
    └──────────────┘      └──────────────┘      │  Scenarios   │      │ Token Costs  │
                                               └──────────────┘      └──────────────┘
                                                                            │
                                                                            ▼
                                                                    ┌──────────────┐
                                                                    │   OUTPUTS    │
                                                                    │ • Accuracy % │
                                                                    │ • Cost/Query │
                                                                    │ • Latency    │
                                                                    │ • Error Types│
                                                                    └──────────────┘

```

## Processing Steps

### Step 1: Generate Controls

Purpose: Transform NIST SP 800-53 Rev 5 catalog into machine-readable formats
- Parses official NIST OSCAL JSON catalog from S3
- Substitutes organization-defined parameters with concrete values using regex replacement
- Filters withdrawn controls to exclude obsolete requirements
- Outputs JSONL (one control per line) and markdown files organized by control family
- Extracts statement, guidance, assessment objectives, and related controls for each control

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           STEP 1 EXECUTION FLOW                                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  main()                                                                              │
│    │                                                                                 │
│    ├─▶ 1. DOWNLOAD SOURCE CATALOG                                                   │
│    │       └─▶ download_file()                                                      │
│    │           └─▶ S3 → Local: NIST_SP-800-53_rev5_catalog.json                    │
│    │                                                                                 │
│    ├─▶ 2. PARSE JSON & EXTRACT METADATA                                             │
│    │       └─▶ Load JSON, extract catalog-level keywords                           │
│    │                                                                                 │
│    ├─▶ 3. COLLECT ALL CONTROLS                                                      │
│    │       └─▶ Iterate groups → controls → enhancements                            │
│    │       └─▶ Build (control, family) tuple list                                  │
│    │                                                                                 │
│    ├─▶ 4. PROCESS EACH CONTROL                                                      │
│    │       │                                                                         │
│    │       ├─▶ 4a. Filter withdrawn controls                                        │
│    │       │                                                                         │
│    │       ├─▶ 4b. extract_param_guidelines()                                       │
│    │       │       └─▶ Build parameter substitution map                            │
│    │       │                                                                         │
│    │       ├─▶ 4c. collect_text_from_parts() × 4                                   │
│    │       │       └─▶ Extract: statement, guidance, assessment-objective,         │
│    │       │           assessment-method                                            │
│    │       │                                                                         │
│    │       ├─▶ 4d. substitute_parameters() × 4                                      │
│    │       │       └─▶ Replace {{ insert: param, X }} placeholders                 │
│    │       │                                                                         │
│    │       └─▶ 4e. Write control object to JSONL                                   │
│    │                                                                                 │
│    ├─▶ 5. UPLOAD JSONL TO S3                                                        │
│    │       └─▶ upload_file()                                                        │
│    │                                                                                 │
│    ├─▶ 6. CREATE MARKDOWN FILES                                                     │
│    │       └─▶ create_markdown_files()                                             │
│    │           └─▶ Generate by-family/ and all-controls/ structures                │
│    │                                                                                 │
│    ├─▶ 7. DISPLAY DIRECTORY TREE                                                    │
│    │       └─▶ print_directory_tree()                                              │
│    │                                                                                 │
│    └─▶ 8. UPLOAD MARKDOWN TO S3                                                     │
│            └─▶ upload_directory_to_s3()                                            │
│                └─▶ Recursive upload maintaining structure                          │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘

```

* NIST Open Security Controls Assessment Language (OSCAL) JSON control file as source (https://pages.nist.gov/OSCAL-Reference/models/v1.1.0/complete/json-reference/)

---

### Step 2: Generate Policies

Purpose: Convert technical NIST controls into organizational policy documents
- Reads control markdown files from Step 1 output
- Invokes Bedrock LLM (Claude or Nova) with structured prompt template
- Generates RAG-optimized policies with validation logic, scenario patterns, and compliance mapping
- Creates versioned output folders with timestamp and model ID for experiment tracking
- Supports resume capability via start_with_control parameter for interrupted runs
  

```
┌─────────────────────────────────────────────────────────────────┐
│                    STEP 2 PROCESSING FLOW                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. INITIALIZE OUTPUT DIRECTORIES                               │
│     └─▶ Create versioned subfolders with timestamp and model ID│
│         • Format: {YYYY-MM-DD:HH:MM:SSET}_{model_id}           │
│         • Creates both all-controls/ and by-family/ versions   │
│                                                                 │
│  2. TRAVERSE CONTROL FILES                                      │
│     └─▶ Walk through control markdown directory tree           │
│     └─▶ Process each .md file in by-family/ structure          │
│                                                                 │
│  3. FILTER CONTROLS (Optional Resume)                           │
│     └─▶ If start_with_control specified:                       │
│         • Parse control IDs using control_key() function       │
│         • Skip controls that sort before the start control     │
│         • Enables resuming interrupted processing              │
│                                                                 │
│  4. GENERATE POLICIES                                           │
│     └─▶ For each control file:                                 │
│         a. Read control markdown content                       │
│         b. Format prompt using PROMPT_TEMPLATE                 │
│         c. Call invoke_bedrock_model() with configured model   │
│         d. Extract policy markdown from response               │
│                                                                 │
│  5. WRITE POLICY FILES                                          │
│     └─▶ Save to BOTH output locations:                         │
│         • all-controls/{family}/policy_{control_name}.md       │
│         • by-family/{family}/policy_{control_name}.md          │
│     └─▶ Maintain original directory structure                  │
│     └─▶ Prefix output files with "policy_"                     │
│                                                                 │
│  6. UPLOAD TO S3                                                │
│     └─▶ Call upload_directory_to_s3() separately               │
│     └─▶ Recursively upload maintaining directory structure     │
│     └─▶ Target: s3://{bucket}/policies/markdown/               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

```

---

### Step 3: Generate Scenarios

Purpose: Create labeled test corpus for LLM evaluation
- Randomly selects 10 policies per scenario from S3 policy repository
- Generates 1,000 scenarios (500 compliant, 500 non-compliant) using alternating batch approach
- Enforces JSON schema via Bedrock tool use to ensure consistent output structure
- Includes compliance_calculator tool for accurate numerical threshold comparisons
- Saves batch checkpoints after each generation for crash recovery


```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           STEP 3 EXECUTION FLOW                                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  main()                                                                              │
│    │                                                                                 │
│    ├─▶ 1. CREATE OUTPUT DIRECTORY                                                   │
│    │       └─▶ FOLDER_SCENARIOS.mkdir(parents=True, exist_ok=True)                 │
│    │                                                                                 │
│    ├─▶ 2. START KEEP-ALIVE THREAD                                                   │
│    │       └─▶ threading.Thread(target=keep_alive, daemon=True)                    │
│    │       └─▶ Prevents SageMaker session timeout during long runs                 │
│    │                                                                                 │
│    ├─▶ 3. GENERATE ALL SCENARIOS                                                    │
│    │       └─▶ generate_compliance_scenarios()                                      │
│    │           │                                                                     │
│    │           └─▶ FOR EACH BATCH (0 to NUM_BATCHES-1):                            │
│    │               │                                                                 │
│    │               ├─▶ 3a. retrieve_s3_policies()                                  │
│    │               │       └─▶ List S3 bucket for policy files                     │
│    │               │       └─▶ Random sample POLICIES_PER_SCENARIO files           │
│    │               │       └─▶ Read content + extract policy IDs                   │
│    │               │                                                                 │
│    │               ├─▶ 3b. generate_scenario_batch()                               │
│    │               │       └─▶ Construct prompt with policies                      │
│    │               │       └─▶ bedrock_call_with_retry()                           │
│    │               │           └─▶ bedrock_runtime.converse()                      │
│    │               │       └─▶ Handle tool_use responses (loop)                    │
│    │               │       └─▶ Extract scenarios from JSON tool                    │
│    │               │       └─▶ Append policy IDs to each scenario                  │
│    │               │                                                                 │
│    │               ├─▶ 3c. SAVE BATCH CHECKPOINT                                   │
│    │               │       └─▶ Write batch_{n}.json locally                        │
│    │               │                                                                 │
│    │               └─▶ 3d. RATE LIMIT PAUSE                                        │
│    │                       └─▶ time.sleep(2)                                       │
│    │                                                                                 │
│    ├─▶ 4. SAVE FINAL OUTPUT (LOCAL)                                                │
│    │       └─▶ save_scenarios_to_file()                                            │
│    │           └─▶ Write scenarios.json with metadata                              │
│    │                                                                                 │
│    └─▶ 5. SAVE FINAL OUTPUT (S3)                                                   │
│            └─▶ save_scenarios_to_s3()                                              │
│                └─▶ Upload scenarios.json to S3                                     │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘

```

---

### Step 4: Judge Scenarios

Purpose: Measure LLM accuracy against ground truth labels
- Extracts policy IDs from scenario text and retrieves full policy content from S3
- Supports Claude (Converse API with tool use) and Nova/Mistral/DeepSeek (invoke_model with JSON parsing)
- Records per-scenario token counts (input, output, total) for cost analysis
- Streams results to file incrementally to prevent data loss during long evaluations
- Outputs judged-compliant boolean, reasoning, model metadata, and timestamp per scenario

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           STEP 4 EXECUTION FLOW                                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  main(model_configs, scenarios, num_scenarios, start_index)                         │
│    │                                                                                 │
│    ├─▶ 1. START KEEP-ALIVE THREAD                                                   │
│    │       └─▶ threading.Thread(target=keep_alive, daemon=True)                    │
│    │       └─▶ Prevents SageMaker session timeout during long runs                 │
│    │                                                                                 │
│    ├─▶ 2. VALIDATE & NORMALIZE INPUTS                                               │
│    │       ├─▶ model_configs: "all" → expand to all MODELS with temp=0.0           │
│    │       ├─▶ model_configs: dict → wrap in list                                  │
│    │       ├─▶ scenarios: "all" → SCENARIOS array                                  │
│    │       └─▶ scenarios: str → wrap in list                                       │
│    │                                                                                 │
│    ├─▶ 3. PRINT PROCESSING SUMMARY                                                  │
│    │       └─▶ Display models, scenarios, counts, start_index                      │
│    │       └─▶ Wait for user confirmation (input())                                │
│    │                                                                                 │
│    ├─▶ 4. NESTED LOOP: FOR EACH MODEL × SCENARIO FILE                              │
│    │       │                                                                         │
│    │       ├─▶ 4a. LOAD BASE MODEL CONFIG                                          │
│    │       │       └─▶ Find model ARN from MODELS array by name                    │
│    │       │                                                                         │
│    │       ├─▶ 4b. LOAD SCENARIOS FROM S3                                          │
│    │       │       └─▶ load_scenarios_from_s3(BUCKET, prefix, filename)            │
│    │       │                                                                         │
│    │       ├─▶ 4c. CONSTRUCT OUTPUT PATHS                                          │
│    │       │       └─▶ Local: FOLDER_JUDGED_SCENARIOS / {batch_name}.json          │
│    │       │       └─▶ S3: scenarios-judged/{batch_name}.json                      │
│    │       │                                                                         │
│    │       ├─▶ 4d. JUDGE ALL SCENARIOS (STREAMING)                                 │
│    │       │       └─▶ judge_scenarios_streaming(                                  │
│    │       │               source_scenarios, model_arn, temperature,               │
│    │       │               num_scenarios, start_index, output_file                 │
│    │       │           )                                                            │
│    │       │                                                                         │
│    │       ├─▶ 4e. UPLOAD RESULTS TO S3                                            │
│    │       │       └─▶ save_file_to_s3(local_path, BUCKET, s3_key)                 │
│    │       │                                                                         │
│    │       └─▶ 4f. PRINT BATCH COMPLETION STATUS                                   │
│    │                                                                                 │
│    └─▶ 5. ERROR HANDLING                                                            │
│            └─▶ Try/except per batch with traceback printing                        │
│            └─▶ Continue to next batch on error                                     │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘

```

---

## Key Features

Multi-Model Evaluation
- Supports Claude (3.7 Sonnet, 4 Sonnet, Opus 4.5), Nova (Premier, 2 Lite), Mistral Large 3, and DeepSeek v3
- Claude models use Converse API with tool use for structured JSON output
- Nova and other models use invoke_model API with JSON parsing
- Configurable temperature settings (0.0, 0.1) per model

Scenario Generation
- 1,000 scenarios (500 compliant, 500 non-compliant) generated from 10 randomly selected policies per scenario
- Alternating batch generation ensures balanced distribution
- Each scenario contains 350+ words with specific business details

Token and Cost Tracking
- Per-scenario token counts (input, output, total) recorded for each evaluation
- Enables price/performance analysis across models
- Timestamps recorded for processing time analysis

Streaming Output
- Results written incrementally to prevent data loss during long-running evaluations
- Batch checkpoint files saved after each generation batch
- Supports resume from any point using start_index parameter

## AWS Services Used

Amazon Bedrock
- Model inference via Converse API (Claude) and invoke_model API (Nova, Mistral, DeepSeek)
- Tool use configuration forces structured JSON output from Claude models
- Inference profiles for cross-region model access

Amazon S3
- Source storage for NIST SP 800-53 Rev 5 catalog (OSCAL JSON format)
- Policy documents stored as markdown files
- Scenario files stored as JSON with ground truth labels
- Evaluation results stored with model-specific naming

Amazon SageMaker Studio
- Jupyter notebook execution environment (Python 3.11)
- Background keep-alive thread prevents session timeout during long runs

Why RAG Was Abandoned

The pipeline initially used AWS Bedrock Knowledge Base for policy retrieval. This approach was abandoned for two reasons:

1. Retrieval accuracy: Knowledge Base RAG returned incomplete policy chunks, missing relevant sections needed for accurate scenario generation and evaluation.

2. Evaluation integrity: For ground truth labeling, the pipeline requires 100% certainty about which policies inform each scenario. RAG retrieval introduces non-deterministic policy selection, making it impossible to establish reliable ground truth labels.

The current implementation uses direct S3 policy retrieval, which guarantees complete policy content and deterministic selection.

## Getting Started

Prerequisites
- AWS account with Bedrock model access enabled for target models
- SageMaker Studio domain with appropriate execution role
- S3 bucket with read/write permissions
- NIST SP 800-53 Rev 5 catalog file (OSCAL JSON format)

Execution Sequence
1. Run 1-GenerateControls.ipynb: Parses NIST catalog, outputs JSONL and markdown controls
2. Run 2-GeneratePolicies.ipynb: Generates organizational policies using Bedrock LLM
3. Run 3-GenerateScenarios.ipynb: Creates labeled compliance scenarios
4. Run 4-JudgeScenarios.ipynb: Evaluates LLM accuracy against ground truth

Configuration
- Model selection: Update MODELS dictionary in each notebook
- Scenario parameters: Adjust SCENARIOS_PER_BATCH, NUM_BATCHES, POLICIES_PER_SCENARIO
- Temperature: Set per-model temperature in model_configs parameter

## Output Artifacts

Step 1 Outputs
- NIST_SP-800-53_rev5_catalog.jsonl: One control per line, machine-readable
- controls/markdown/by-family/: Controls organized by family (AC, AU, CA, etc.)
- controls/markdown/all-controls/: All controls in single directory

Step 2 Outputs
- policies/markdown/by-family/{timestamp}_{model}/: Policies organized by family
- policies/markdown/all-controls/{timestamp}_{model}/: All policies in single directory

Step 3 Outputs
- scenarios/scenarios.json: Complete scenario set with ground truth labels
- scenarios/batch_{n}.json: Individual batch checkpoints for crash recovery

Step 4 Outputs
- scenarios-judged/judged_scenarios_batch-{scenario_file}-{model}-temp{temp}.json
- Contains original scenario fields plus: judged-compliant, judged-compliant-reason, token counts, timestamp

## Performance Considerations

API Throttling
- Exponential backoff retry logic: delay = base_delay × 2^attempt (max 5 retries)
- 2-second pause between batches in scenario generation
- ThrottlingException handling with automatic retry

Memory and I/O
- Streaming output prevents memory accumulation during long runs
- Batch checkpoints enable crash recovery without full restart
- Background keep-alive thread prevents SageMaker session timeout

## Use Cases

Model Selection for Compliance Automation
- Compare accuracy (true positive rate, false negative rate) across models
- Identify models with lowest false negative rate for regulatory-critical applications
- Evaluate consistency across multiple temperature settings

Price/Performance Optimization
- Calculate cost per correct judgment using token counts and model pricing
- Identify optimal model for given accuracy threshold and budget constraint
- Compare Claude vs Nova vs Mistral (coming) and Deepseek (coming) for cost-sensitive deployments

Compliance Workflow Development
- Use generated policies as templates for organizational policy documents
- Adapt scenario patterns for domain-specific compliance testing
- Extend evaluation framework to other compliance standards (FedRAMP, HIPAA, PCI-DSS)

Risk Quantification
- Weighted false positve rate to quantify missed violation (i.e. indicating a scenario is compliant when it is not)
- Confusion matrix analysis for error pattern identification

# LLM Performance

---
![Confusion Matrix Analysis](/images/unweighted_confusion_matrix_analysis.png)

In this analysis, false positives and false negatives are treated equally when evaluating model performance.  Our top 3 performers overall are Claude 3.7 Sonnet, Claude Opus 4.5, and Nova Premier.
Among those models, we see a notable dip in Nova Premier's performance at complexity 8 (8 policies per scenario).  Interestingly, at the even higher complexity of 10, Nova Premier's performance rebounds.



---
![Confusion Matrix Analysis](/images/weighted_confusion_matrix_analysis.png)

---
![Confusion Matrix Analysis](/images/model_performance_by_complexity.png)

---

## Confusion Matrix Summary
| Model & Temp | Complexity 4 | Complexity 6 | Complexity 8 | Complexity 10 |
|---|---|---|---|---|
| **claude 3 7 sonnet** (T=0.0) | TP:89 FP:7<br>FN:16 TN:88<br>FPR:7.4% FNR:15.2%  | TP:91 FP:8<br>FN:9 TN:92<br>FPR:8.0% FNR:9.0%  | TP:76 FP:10<br>FN:24 TN:90<br>FPR:10.0% FNR:24.0%  | TP:75 FP:7<br>FN:21 TN:93<br>FPR:7.0% FNR:21.9%  |
| **claude 3 7 sonnet** (T=0.1) | TP:90 FP:6<br>FN:15 TN:89<br>FPR:6.3% FNR:14.3%  | TP:92 FP:8<br>FN:8 TN:92<br>FPR:8.0% FNR:8.0%  | TP:80 FP:11<br>FN:20 TN:89<br>FPR:11.0% FNR:20.0%  | TP:76 FP:8<br>FN:20 TN:92<br>FPR:8.0% FNR:20.8%  |
| **claude 4 sonnet** (T=0.0) | TP:84 FP:5<br>FN:21 TN:90<br>FPR:5.3% FNR:20.0%  | TP:69 FP:11<br>FN:31 TN:89<br>FPR:11.0% FNR:31.0%  | TP:70 FP:12<br>FN:30 TN:88<br>FPR:12.0% FNR:30.0%  | TP:52 FP:5<br>FN:44 TN:95<br>FPR:5.0% FNR:45.8%  |
| **claude 4 sonnet** (T=0.1) | TP:81 FP:7<br>FN:24 TN:88<br>FPR:7.4% FNR:22.9%  | TP:70 FP:10<br>FN:30 TN:90<br>FPR:10.0% FNR:30.0%  | TP:77 FP:12<br>FN:23 TN:88<br>FPR:12.0% FNR:23.0%  | TP:55 FP:5<br>FN:41 TN:95<br>FPR:5.0% FNR:42.7%  |
| **claude opus 4 5** (T=0.0) | TP:92 FP:5<br>FN:13 TN:90<br>FPR:5.3% FNR:12.4%  | TP:92 FP:13<br>FN:8 TN:87<br>FPR:13.0% FNR:8.0%  | TP:92 FP:10<br>FN:8 TN:90<br>FPR:10.0% FNR:8.0%  | TP:61 FP:8<br>FN:35 TN:92<br>FPR:8.0% FNR:36.5%  |
| **claude opus 4 5** (T=0.1) | TP:91 FP:6<br>FN:14 TN:89<br>FPR:6.3% FNR:13.3%  | TP:90 FP:13<br>FN:10 TN:87<br>FPR:13.0% FNR:10.0%  | TP:88 FP:11<br>FN:12 TN:89<br>FPR:11.0% FNR:12.0%  | TP:65 FP:7<br>FN:31 TN:93<br>FPR:7.0% FNR:32.3%  |
| **nova 2 lite** (T=0.0) | TP:103 FP:25<br>FN:2 TN:70<br>FPR:26.3% FNR:1.9%  | TP:98 FP:30<br>FN:2 TN:70<br>FPR:30.0% FNR:2.0%  | TP:100 FP:54<br>FN:0 TN:46<br>FPR:54.0% FNR:0.0%  | TP:96 FP:27<br>FN:0 TN:73<br>FPR:27.0% FNR:0.0%  |
| **nova 2 lite** (T=0.1) | TP:102 FP:23<br>FN:3 TN:72<br>FPR:24.2% FNR:2.9%  | TP:97 FP:30<br>FN:3 TN:70<br>FPR:30.0% FNR:3.0%  | TP:100 FP:54<br>FN:0 TN:46<br>FPR:54.0% FNR:0.0%  | TP:96 FP:27<br>FN:0 TN:73<br>FPR:27.0% FNR:0.0%  |
| **nova 2 pro** (T=0.0) | TP:72 FP:10<br>FN:33 TN:85<br>FPR:10.5% FNR:31.4%  | TP:45 FP:9<br>FN:55 TN:91<br>FPR:9.0% FNR:55.0%  | TP:48 FP:21<br>FN:52 TN:79<br>FPR:21.0% FNR:52.0%  | TP:48 FP:4<br>FN:48 TN:96<br>FPR:4.0% FNR:50.0%  |
| **nova 2 pro** (T=0.1) | TP:73 FP:12<br>FN:32 TN:83<br>FPR:12.6% FNR:30.5%  | TP:47 FP:7<br>FN:53 TN:93<br>FPR:7.0% FNR:53.0%  | TP:48 FP:23<br>FN:52 TN:77<br>FPR:23.0% FNR:52.0%  | TP:45 FP:4<br>FN:51 TN:96<br>FPR:4.0% FNR:53.1%  |
| **nova premier** (T=0.0) | TP:85 FP:3<br>FN:20 TN:92<br>FPR:3.2% FNR:19.0%  | TP:82 FP:7<br>FN:18 TN:93<br>FPR:7.0% FNR:18.0%  | TP:80 FP:20<br>FN:20 TN:80<br>FPR:20.0% FNR:20.0%  | TP:71 FP:5<br>FN:25 TN:95<br>FPR:5.0% FNR:26.0%  |
| **nova premier** (T=0.1) | TP:82 FP:3<br>FN:23 TN:92<br>FPR:3.2% FNR:21.9%  | TP:81 FP:7<br>FN:19 TN:93<br>FPR:7.0% FNR:19.0%  | TP:82 FP:20<br>FN:18 TN:80<br>FPR:20.0% FNR:18.0%  | TP:70 FP:6<br>FN:26 TN:94<br>FPR:6.0% FNR:27.1%  |

**Legend:** TP=True Positive, FP=False Positive, FN=False Negative, TN=True Negative
FPR = False Positive Rate (FP/(FP+TN)) - False Alarm Rate
FNR = False Negative Rate (FN/(FN+TP)) - Missed Violation Rate

## Pricing Comparison

| Model | Price per 1M Input Tokens | Price per 1M Output Tokens |
|---|---|---|
| Amazon Nova 2 Lite | $0.33 | $2.75 |
| Amazon Nova Premier | $2.50 | $12.50 |
| Claude 3.7 Sonnet | $3.00 | $15.00 |
| Claude Sonnet 4 | $3.00 | $15.00 |
| Claude Opus 4.5 | $5.50 | $27.50 |

*US East (N. Virginia), Standard Tier/Non-Batch, Geo cross-region inference and in-region*

## Key Observations

Impact of Scenario Complexity:
- All models show degraded performance as policy count increases from 4 to 10
- False negative rates increase significantly at 10 policies per scenario
- Claude 4 Sonnet shows largest degradation (10.5% FN at 4 policies vs 22.4% at 10 policies)

Temperature Effect:
- Minimal impact on error rates for most models
- Claude 4 Sonnet shows slight improvement at temp=0.1 for higher complexity scenarios

Nova 2 Lite Behavior:
- Exhibits strong bias toward predicting "compliant" (near-zero false negatives)
- High false positive rates (12.5% - 27.0%) indicate poor violation detection
- Not recommended for compliance workloads requiring violation identification
- Temperature of 0.1 was not pursed due to poor performance at 0.0

