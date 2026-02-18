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

## Step 1: Generate Controls

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

# LLM Compliance Evaluation Analysis

---
![Confusion Matrix Analysis](/images/confusion_matrix_analysis.png)

---

### Summary Table

| Model | Temp | Policies | Total | TP | TN | FP | FN | FP Rate | FN Rate |
|-------|------|----------|-------|----|----|----|----|---------|---------|
| Claude Opus 4.5 | 0.0 | 4 | 200 | 90 | 92 | 5 | 13 | 2.5% | 6.5% |
| Claude Opus 4.5 | 0.1 | 4 | 200 | 89 | 91 | 6 | 14 | 3.0% | 7.0% |
| Claude Opus 4.5 | 0.0 | 6 | 200 | 87 | 92 | 13 | 8 | 6.5% | 4.0% |
| Claude Opus 4.5 | 0.1 | 6 | 200 | 87 | 90 | 13 | 10 | 6.5% | 5.0% |
| Claude Opus 4.5 | 0.0 | 8 | 200 | 90 | 92 | 10 | 8 | 5.0% | 4.0% |
| Claude Opus 4.5 | 0.1 | 8 | 200 | 89 | 88 | 11 | 12 | 5.5% | 6.0% |
| Claude Opus 4.5 | 0.0 | 10 | 196 | 92 | 61 | 8 | 35 | 4.1% | 17.9% |
| Claude Opus 4.5 | 0.1 | 10 | 196 | 93 | 65 | 7 | 31 | 3.6% | 15.8% |
| Claude 4 Sonnet | 0.0 | 4 | 200 | 90 | 84 | 5 | 21 | 2.5% | 10.5% |
| Claude 4 Sonnet | 0.1 | 4 | 200 | 88 | 81 | 7 | 24 | 3.5% | 12.0% |
| Claude 4 Sonnet | 0.0 | 6 | 200 | 89 | 69 | 11 | 31 | 5.5% | 15.5% |
| Claude 4 Sonnet | 0.1 | 6 | 200 | 90 | 70 | 10 | 30 | 5.0% | 15.0% |
| Claude 4 Sonnet | 0.0 | 8 | 200 | 88 | 70 | 12 | 30 | 6.0% | 15.0% |
| Claude 4 Sonnet | 0.1 | 8 | 200 | 88 | 77 | 12 | 23 | 6.0% | 11.5% |
| Claude 4 Sonnet | 0.0 | 10 | 196 | 95 | 52 | 5 | 44 | 2.6% | 22.4% |
| Claude 4 Sonnet | 0.1 | 10 | 196 | 95 | 55 | 5 | 41 | 2.6% | 20.9% |
| Claude 3.7 Sonnet | 0.0 | 4 | 200 | 88 | 89 | 7 | 16 | 3.5% | 8.0% |
| Claude 3.7 Sonnet | 0.1 | 4 | 200 | 89 | 90 | 6 | 15 | 3.0% | 7.5% |
| Claude 3.7 Sonnet | 0.0 | 6 | 200 | 92 | 91 | 8 | 9 | 4.0% | 4.5% |
| Claude 3.7 Sonnet | 0.1 | 6 | 200 | 92 | 92 | 8 | 8 | 4.0% | 4.0% |
| Claude 3.7 Sonnet | 0.0 | 8 | 200 | 90 | 76 | 10 | 24 | 5.0% | 12.0% |
| Claude 3.7 Sonnet | 0.1 | 8 | 200 | 89 | 80 | 11 | 20 | 5.5% | 10.0% |
| Claude 3.7 Sonnet | 0.0 | 10 | 196 | 93 | 75 | 7 | 21 | 3.6% | 10.7% |
| Claude 3.7 Sonnet | 0.1 | 10 | 196 | 92 | 76 | 8 | 20 | 4.1% | 10.2% |
| Nova Premier | 0.0 | 4 | 200 | 92 | 85 | 3 | 20 | 1.5% | 10.0% |
| Nova Premier | 0.1 | 4 | 200 | 92 | 82 | 3 | 23 | 1.5% | 11.5% |
| Nova Premier | 0.0 | 6 | 200 | 93 | 82 | 7 | 18 | 3.5% | 9.0% |
| Nova Premier | 0.1 | 6 | 200 | 93 | 81 | 7 | 19 | 3.5% | 9.5% |
| Nova Premier | 0.0 | 8 | 200 | 80 | 80 | 20 | 20 | 10.0% | 10.0% |
| Nova Premier | 0.1 | 8 | 200 | 80 | 82 | 20 | 18 | 10.0% | 9.0% |
| Nova Premier | 0.0 | 10 | 196 | 95 | 71 | 5 | 25 | 2.6% | 12.8% |
| Nova Premier | 0.1 | 10 | 196 | 94 | 70 | 6 | 26 | 3.1% | 13.3% |
| Nova 2 Lite | 0.0 | 4 | 200 | 70 | 103 | 25 | 2 | 12.5% | 1.0% |
| Nova 2 Lite | 0.0 | 6 | 200 | 70 | 98 | 30 | 2 | 15.0% | 1.0% |
| Nova 2 Lite | 0.0 | 8 | 200 | 46 | 100 | 54 | 0 | 27.0% | 0.0% |
| Nova 2 Lite | 0.0 | 10 | 196 | 73 | 96 | 27 | 0 | 13.8% | 0.0% |

Column definitions:
- Model: LLM tested
- Temp: Model temperature used
- Policies: Number of policies referenced per scenario (complexity measure)
- Total: Number of scenarios tested
- TP: True Positives (correctly identified compliant scenarios)
- TN: True Negatives (correctly identified non-compliant scenarios)
- FP: False Positives (non-compliant scenarios incorrectly marked as compliant)
- FN: False Negatives (compliant scenarios incorrectly flagged as violations)
- FP Rate: FP / (FP + TN) — false alarm rate
- FN Rate: FN / (FN + TP) — missed violation rate

### Key Observations

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

