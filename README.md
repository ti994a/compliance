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

# LLM Performance Results

## False Positives and False Negatives

For this project:

 - False positive: the judged scenario is non-compliant, but the model incorrectly judged it as compliant.
 - False negative: the judged scenario is compliant, but the model incorrectly judged it as non-compliant.

---
## Important Note - Tool Use

The Amazon Bedrock Converse API is a unified inference interface that provides a consistent way to interact with supported foundation models, and it includes built-in support for tool use (also called function calling), allowing models to request the execution of external functions or APIs during a conversation. Tool use is the ability for a model to recognize when it needs additional information or capabilities beyond its training data, declare a structured call to a predefined tool (such as a calculator, database lookup, or web search), and incorporate the tool's returned result into its final response.

Claude models were tested with tool use enabled - specifically a calculator tool to help the LLM with numerical and unit comparision (e.g. to indicate that 20 terabytes is smaller than 2 petabytes) and also a json tool to enforce that results were returned in a valid json format.  Claude tool use improved results significantly.  The calculator and json tools were also tried with the Nova and Nova 2 models.  However, performance degraded significantly with Nova Premier, degraded with Nova 2 Lite, and increased slightly with Nova 2 Pro.  (See the table below, which compares average weighted scores by model and temperature for tooluse versus no tool use enabled.) This was an unexpected result and is being investigated; Nova/Nova 2 results presented in this analysis are those where tool use was not enabled.


|Model/Temperature|No Tool Use| With Tool Use|
|--|--|--|
|Nova Premier, Temp 0.0 |80.8 |67.2|
|Nova Premier, Temp 0.1 |80.2 |68.9|
|Nova 2 Lite, Temp 0.0 | 65.4 |63.3|
|Nova 2 Lite, Temp 0.1 |65.6 | 62.7|
|Nova 2 Pro, Temp 0.0 |65.4 |66.1|
|Nova 2 Pro, Temp 0.1 |64.8 |65.7|

---

## Unweighted Model Performance

![Confusion Matrix Analysis](/images/unweighted_confusion_matrix_analysis.png)

Unweighted scores are calculated as 100 - ((FP + FN) / total * 100), treating false positives and false negatives equally. This provides a balanced view of overall accuracy where both types of errors have equal impact on the final score.

The full ranked results across all model and temperature combinations are:

| Model & Temp | C4 | C6 | C8 | C10 | Average |
|---|---|---|---|---|---|
| **claude 3 7 sonnet** (T=0.1) | 89.5% | 92.0% | 84.5% | 85.7% | 87.9% |
| **claude opus 4 5** (T=0.0) | 91.0% | 89.5% | 91.0% | 78.1% | 87.4% |
| **claude 3 7 sonnet** (T=0.0) | 88.5% | 91.5% | 83.0% | 85.7% | 87.2% |
| **claude opus 4 5** (T=0.1) | 90.0% | 88.5% | 88.5% | 80.6% | 86.9% |
| **nova premier** (T=0.0) | 88.5% | 87.5% | 80.0% | 84.7% | 85.2% |
| **nova premier** (T=0.1) | 87.0% | 87.0% | 81.0% | 83.7% | 84.7% |
| **nova 2 lite** (T=0.0) | 86.5% | 84.0% | 73.0% | 86.2% | 82.4% |
| **nova 2 lite** (T=0.1) | 87.0% | 83.5% | 73.0% | 86.2% | 82.4% |
| **claude 4 sonnet** (T=0.1) | 84.5% | 80.0% | 82.5% | 76.5% | 80.9% |
| **claude 4 sonnet** (T=0.0) | 87.0% | 79.0% | 79.0% | 75.0% | 80.0% |
| **nova 2 pro** (T=0.0) | 78.5% | 68.0% | 63.5% | 73.5% | 70.9% |
| **nova 2 pro** (T=0.1) | 78.0% | 70.0% | 62.5% | 71.9% | 70.6% |

---

## Weighted Model Performance

![Confusion Matrix Analysis](/images/weighted_confusion_matrix_analysis.png)

The unweighted analysis treats all errors equally. But in a real compliance workflow, not all errors are created equal. Incorrectly clearing a non-compliant scenario — a false positive — carries meaningfully greater organizational risk than flagging a compliant one. A missed violation can go undetected, potentially exposing the organization to audit findings, regulatory penalties, or unmitigated security risk. An over-flagged compliant scenario, by contrast, generates unnecessary remediation work.

To reflect this asymmetry, the weighted scoring formula penalizes false positives at **2× the rate of false negatives**: `Weighted Score = 100 - ((2 × FP + FN) / Total × 100)`; incorrectly flagging violations as compliant scenarios is considered risky and therefore costlier than incorrectly flagging compliant scenarios as non-compliant.

The results under this scoring scheme reveal a somewhat different picture without affecting the overall unweighted leader rankings.  Claude 4 Sonnet and Nova 2 Lite do switch places with weighting applied.  Additionally, the worst performers are penalized more due to having a proportionately higher number of false positives.

The full ranked results across all model and temperature combinations are:

| Model & Temp | C4 | C6 | C8 | C10 | Average |
|---|---|---|---|---|---|
| **claude 3 7 sonnet** (T=0.1) | 86.5% | 88.0% | 79.0% | 81.6% | 83.8% |
| **claude 3 7 sonnet** (T=0.0) | 85.0% | 87.5% | 78.0% | 82.1% | 83.2% |
| **claude opus 4 5** (T=0.0) | 88.5% | 83.0% | 86.0% | 74.0% | 82.9% |
| **claude opus 4 5** (T=0.1) | 87.0% | 82.0% | 83.0% | 77.0% | 82.3% |
| **nova premier** (T=0.0) | 87.0% | 84.0% | 70.0% | 82.1% | 80.8% |
| **nova premier** (T=0.1) | 85.5% | 83.5% | 71.0% | 80.6% | 80.2% |
| **claude 4 sonnet** (T=0.1) | 81.0% | 75.0% | 76.5% | 74.0% | 76.6% |
| **claude 4 sonnet** (T=0.0) | 84.5% | 73.5% | 73.0% | 72.4% | 75.9% |
| **nova 2 lite** (T=0.1) | 75.5% | 68.5% | 46.0% | 72.4% | 65.6% |
| **nova 2 lite** (T=0.0) | 74.0% | 69.0% | 46.0% | 72.4% | 65.4% |
| **nova 2 pro** (T=0.0) | 73.5% | 63.5% | 53.0% | 71.4% | 65.4% |
| **nova 2 pro** (T=0.1) | 72.0% | 66.5% | 51.0% | 69.9% | 64.8% |

---

## How Complexity Shapes Model Performance

![Confusion Matrix Analysis](/images/model_performance_by_complexity.png)

The question of *how* a model degrades as reasoning demands increase is just as important as where it ranks overall. This visualization makes this dynamic clear.

The figure presents two side-by-side line charts — one for best unweighted scores, one for best weighted scores — each plotting all six models across the four complexity levels: C4 (4 policies per scenario), C6, C8, and C10. Each model is represented as a labeled line with markers at each complexity point, using its best-performing temperature configuration.  Flat lines indicate robustness — a model that reasons about compliance with equal reliability whether a scenario references 4 policies or 10. Steep downward slopes indicate fragility — a model whose accuracy erodes meaningfully as the number of policies it must synthesize increases. And non-monotonic patterns — dips followed by recoveries — suggest something more complex is happening in how the model processes context at different scales.

## Price/Performance Scorecard

The five columns in the table each tell a different part of the story:

- **Weighted Score (Avg)** — The model's average risk-adjusted accuracy across all complexity levels, using its best temperature setting. *Think of this as the model's overall grade.* Higher is better.
- **Best Weighted Score (Single Complexity)** — The highest score the model achieved at any single complexity level. *This is the model's peak performance under ideal conditions* — useful for understanding what the model is capable of when scenarios align with its strengths.
- **Worst Weighted Score (Single Complexity)** — The lowest score the model achieved at any single complexity level. *This is the model's floor — its worst-case performance.* A low floor means the model can fail badly under certain conditions, even if its average looks acceptable.
- **Complexity Robustness (point drop)** — The difference between the best and worst single-complexity scores. *This measures how much the model degrades as scenarios get harder.* A small drop means the model performs consistently regardless of complexity; a large drop means it struggles when asked to reason across many policies at once.
- **Input / Output Price** — The cost per million tokens processed. *This is the direct cost lever* — the price you pay per unit of work, independent of accuracy.

| Model (Best Temp) | Weighted Score (Avg) | Best Weighted Score (Single Complexity) | Worst Weighted Score (Single Complexity) | Complexity Robustness (point drop) | Input Price (per 1M tokens) | Output Price (per 1M tokens) |
|---|---|---|---|---|---|---|
| Claude 3.7 Sonnet (T=0.1) | 83.8 | 88.0 (C6) | 79.0 (C8) | 9.0 pts | $3.00 | $15.00 |
| Claude Opus 4.5 (T=0.0) | 82.9 | 88.5 (C4) | 74.0 (C10) | 14.5 pts | $5.50 | $27.50 |
| Nova Premier (T=0.0) | 80.8 | 87.0 (C4) | 70.0 (C8) | 17.0 pts* | $2.50 | $12.50 |
| Claude 4 Sonnet (T=0.1) | 76.6 | 81.0 (C4) | 74.0 (C10) | 7.0 pts | $3.00 | $15.00 |
| Nova 2 Lite (T=0.1) | 65.6 | 75.5 (C4) | 46.0 (C8) | 29.5 pts | $0.33 | $2.75 |
| Nova 2 Pro (T=0.0) | 65.4 | 73.5 (C4) | 53.0 (C8) | 20.5 pts | TBD | TBD |

*Nova Premier's complexity drop is non-monotonic: performance dips at C8 then partially recovers at C10, rather than declining steadily.*

*Pricing: US East (N. Virginia), Standard Tier/Non-Batch, Geo cross-region inference and in-region. Nova 2 Pro pricing pending general availability. Weighted score formula: 100 − ((2 × FP + FN) / Total × 100), where false positives are penalized at 2× the rate of false negatives.*

## Conclusion: Choosing the Right LLM for NIST Compliance Automation

**Note to reader:  this analysis is still in progress, and should be be considered draft.  More work is needed in this section.**

The results of this evaluation offer a nuanced picture of how six leading LLMs perform on NIST SP 800-53 compliance reasoning tasks. Across nearly 800 labeled compliance scenarios, four complexity levels, two temperature configurations, and three distinct scoring lenses — unweighted accuracy, weighted risk-adjusted scoring, and performance curves — meaningful differences emerge in accuracy, failure modes, cost, and robustness.

### Claude 3.7 Sonnet — Best Overall Performer

Claude 3.7 Sonnet achieves the most consistent and well-calibrated performance across all complexity levels, with FP rates ranging from 3.0% to 5.5% and FN rates from 4.0% to 12.0%. Its defining characteristic is stability: unlike most models in this evaluation, its FP rate does not exhibit dramatic degradation as scenario complexity increases from C4 to C10. This stability is attributable to two reinforcing factors. First, the model has access to the compliance_calculator tool, which provides grounded arithmetic for the numerical threshold comparisons that appear throughout NIST SP 800-53 controls — comparisons such as "95 days vs. a 90-day requirement" that cannot be reliably resolved through approximate text-based reasoning alone. Second, Claude 3.7 Sonnet was Anthropic's first model to incorporate extended thinking capabilities, a training approach specifically designed to improve performance on multi-step analytical tasks requiring exhaustive verification rather than rapid pattern matching.[1] This architectural orientation is well-matched to the compliance evaluation task, which rewards systematic rule-by-rule checking over confident brevity.

The question of why Claude 3.7 Sonnet outperforms the nominally newer Claude 4 Sonnet is a counterintuitive finding in this dataset and merits careful analysis. The answer lies in the distinction between general-purpose optimization and task-specific optimization. Research on large language model capability transfer has consistently demonstrated that newer models optimized for broad instruction-following efficiency can underperform older models that were specifically trained for deep multi-step reasoning on structured analytical tasks.[2] Claude 4 Sonnet was positioned as a general-purpose model emphasizing concise, efficient responses — a training objective that is misaligned with compliance evaluation, which requires exhaustive skepticism rather than confident brevity. Claude 3.7 Sonnet's extended thinking architecture, by contrast, is specifically designed to allocate additional reasoning budget to complex verification tasks, making it the better-suited model for this workload despite being an earlier release.

The C8 FN spike (12.0% at T=0.0) is the primary anomaly for this model. At eight policies, the scenario context becomes sufficiently dense that the model occasionally misidentifies a compliant near-threshold value as a violation — the opposite of the dangerous error type, but operationally costly. Research on long-context attention in transformer architectures has shown that models exhibit degraded recall for information positioned in the middle of long input sequences, a phenomenon sometimes called the "lost in the middle" effect.[3] At C8, the compliance-relevant threshold value may be positioned in a context region where attention is less concentrated, leading to occasional misclassification of compliant values as violations. The partial recovery at C10 (FN drops to 10.7%) is consistent with the hypothesis that C10 violations are more prominent and unambiguous — they must be significant enough to stand out among ten policies — making them easier to detect correctly.

### Claude Opus 4.5 — Strong at C4–C8, Significant C10 Cliff

Claude Opus 4.5 is Anthropic's highest-capability model in this evaluation by parameter count and training investment, and its performance at C4 through C8 reflects this: it achieves the lowest FN rates of any model at these complexity levels (4.0–8.0%), demonstrating superior ability to correctly confirm compliant scenarios without generating false alarms. Its thorough reasoning outputs are notably longer and more systematic than those of other models, reflecting a training approach that prioritizes comprehensive verification over efficient summarization.[4]

The C10 FN cliff — where FN rates rise from 4.0% at C8 to 17.9% at T=0.0 — is the most striking finding for this model and represents a well-documented failure mode in long-context LLM reasoning. The most plausible mechanism is a form of over-thoroughness under output token constraint: Opus 4.5's tendency to exhaustively verify each policy means it allocates more output tokens per policy than other models. With ten policies and a 4,096 maximum token budget, the model may exhaust its output budget before completing verification of all policies, causing it to render a verdict based on incomplete analysis. Alternatively, the model may exhibit what has been described in the RLHF literature as a form of majority-signal anchoring: having verified nine policies as compliant, it develops increasing confidence in a compliant verdict and becomes less sensitive to the single non-compliant policy remaining.[5] Either mechanism produces the same observable outcome — a dramatic increase in false alarms at maximum complexity — and both are consistent with the known behavior of models trained to be thorough under resource constraints.

The practical implication is significant: for C10 workloads, Claude 3.7 Sonnet is the better choice despite being a smaller model. Opus 4.5 is optimal for most lower complexity workloads where its superior FN performance reduces operational overhead from false alarms.

### Nova Premier — Best Amazon Model, Competitive with Anthropic

Nova Premier achieves FP rates of 1.5% at C4 and 3.5% at C6 — the best FP performance of any model tested at these complexity levels. This is a remarkable result for a model operating without tool use access. The explanation could lie in Nova Premier's architectural positioning: it is Amazon's most capable model in the Nova family, designed for complex tasks requiring deep understanding of context, multistep planning, and precise execution across multiple data sources, with a one-million-token context window and benchmark scores of 87.4% on MMLU and 82.0% on Math500.[10] Its base reasoning capability is sufficiently strong to perform many numerical threshold comparisons inline without requiring the calculator tool, and its systematic policy-by-policy evaluation approach — evident in the judged output data — produces reliable violation detection at lower complexity levels.

The C8 anomaly is the most analytically interesting finding in the dataset. Nova Premier's FP rate jumps from 3.5% at C6 to 10.0% at C8 — nearly tripling — before recovering to 2.6% at C10. This non-monotonic degradation pattern is observed across multiple models and is unlikely to be a coincidence. The most parsimonious explanation involves the interaction between scenario complexity and the absence of tool use. Research on attention mechanisms in transformer architectures has demonstrated that models exhibit non-linear degradation in recall accuracy as input length increases, with particular difficulty maintaining equal attention across all positions in long contexts.[3]

The significance of Nova Premier's performance for Telos is that it achieves competitive results with Claude 3.7 Sonnet at C4–C6 without tool use access, at a lower cost. 

### Claude 4 Sonnet — Underperformer Relative to Generation

Claude 4 Sonnet exhibits the worst FN performance of any Anthropic model, with rates rising from 10.5% at C4 to 22.4% at C10. This pattern — consistently high false alarm rates that worsen with complexity — is the signature of a model that has developed a compliance-skeptical bias: when uncertain, it defaults to "non-compliant" rather than investing in deeper verification. While this posture keeps FP rates low (2.5–6.0%), it creates substantial operational overhead through excessive false alarms.

The behavioral explanation is grounded in the known tradeoffs of RLHF-based training. Models trained with human feedback that rewards concise, confident responses tend to develop a preference for decisive verdicts over extended deliberation.[6] For compliance evaluation — a task that rewards exhaustive skepticism and systematic rule-checking — this optimization target is misaligned. Claude 4 Sonnet's judged outputs are notably shorter than those of Claude 3.7 Sonnet, suggesting the model is rendering verdicts after less thorough policy analysis. The C6 FN spike (15.5%) is particularly notable: the model's performance degrades substantially at just six policies, suggesting its effective context utilization for structured rule-checking tasks might be lower than that of its predecessor.

The C10 FP recovery (2.6%) could be a consequence of the over-conservative posture: at maximum complexity, the model is so reluctant to call anything compliant that it almost never does, which incidentally keeps FP low while driving FN to its worst level. This is not a genuine improvement in violation detection — it is a degenerate strategy of near-universal non-compliance verdicts.

### Nova 2 Lite — Poor Performance

Nova 2 Lite exhibits a near-perfect "always compliant" bias that constitutes a systematic model failure mode rather than a performance characteristic. At C8, the model misses 27% of all non-compliant scenarios — more than one in four real violations go undetected. The 0.0% FNR at C8 and C10 confirms the model is not performing genuine policy analysis at these complexity levels; it is essentially biased toward outputting "compliant".

The root cause is a combination of model capacity and inference architecture. Nova 2 Lite is Amazon's smallest, fastest, and least expensive Nova model designed for high-throughput, low-latency tasks rather than deep multi-document reasoning.[7] Research on the relationship between model scale and multi-step reasoning has consistently demonstrated that smaller models exhibit greater difficulty with tasks requiring the simultaneous tracking of multiple constraints across long input contexts.[8] With 4–10 dense policy documents in the input, Nova 2 Lite lacks the reasoning depth to identify subtle violations, particularly those involving numerical threshold comparisons.

The apparent C8→C10 FP reduction (27% → 13.8%) is misleading. At C10, scenarios are sufficiently long and violations sufficiently prominent that the model occasionally identifies a violation by chance. This is noise, not signal — the near-zero FNR persists, confirming the model is not performing reliable violation detection.

### Nova 2 Pro — Worst Overall Performer

Nova 2 Pro's performance is paradoxically worse than both Nova 2 Lite and Nova Premier, exhibiting the worst overall error profile in the evaluation. Understanding why requires examining the specific engineering decision that shaped its inference path.

The bidirectional error pattern at C6–C8 — simultaneously elevated FP and catastrophic FN — is the worst possible outcome for a compliance workload. The model neither reliably detects violations nor reliably confirms compliance. The C10 FP recovery (2.0%) mirrors Claude 4 Sonnet's degenerate strategy: at maximum complexity, the model becomes so conservative that it almost never calls anything compliant, which incidentally reduces missed violations while driving false alarms to approximately 25%.

### Design Principles for Production Compliance Workflows

This evaluation surfaces principles that should inform how teams architect AI-assisted compliance systems on AWS:

**Treat false positives and false negatives as asymmetric risks.** The weighted scoring results diverge meaningfully from equal-weight accuracy, and the right balance depends on your organization's specific risk posture. A team with limited capacity for human review should optimize for low false positive rates; a team operating under strict regulatory scrutiny should optimize for low false negative rates. The weighted score formula used here — penalizing false positives at 2× — reflects one reasonable calibration, but organizations should validate this weighting against their own compliance risk model.

**Don't assume newer means better for specialized tasks.** Claude 4 Sonnet's underperformance relative to Claude 3.7 Sonnet at the same price point is a finding that generalizes beyond this specific evaluation: compliance reasoning is a specialized capability that requires targeted benchmarking. General-purpose model benchmarks are not a substitute for task-specific evaluation.

**Model performance does not decline steadily as scenario complexity increases.**  Four of the six models tested saw their worst performance at complexity level 8, with an increase at complexity level 10.

### Looking Ahead

This framework is designed to be evolve alongside the models it evaluates, and the pipeline can be extended to incorporate additional entrants without modification to the core evaluation architecture.  The core finding, however, is that rigorous, task-specific evaluation is the only reliable basis for model selection in compliance-critical AI applications.  The differences between models in this evaluation — in accuracy, in failure modes, in cost, and in how performance degrades with complexity — are large enough to have real operational and financial consequences. The framework described in this post provides a reproducible, extensible methodology for making those differences visible.  As discussed above, understanding tool use with Nova/Nova 2 models is a takeaway item.

---

## Appendix: Confusion Matrix Summary

| Model & Temp | C4-FP% | C4-FN% | C6-FP% | C6-FN% | C8-FP% | C8-FN% | C10-FP% | C10-FN% |
|---|---|---|---|---|---|---|---|---|
| **claude 3 7 sonnet** (T=0.0) | 3.5% | 8.0% | 4.0% | 4.5% | 5.0% | 12.0% | 3.6% | 10.7% |
| **claude 3 7 sonnet** (T=0.1) | 3.0% | 7.5% | 4.0% | 4.0% | 5.5% | 10.0% | 4.1% | 10.2% |
| **claude 4 sonnet** (T=0.0) | 2.5% | 10.5% | 5.5% | 15.5% | 6.0% | 15.0% | 2.6% | 22.4% |
| **claude 4 sonnet** (T=0.1) | 3.5% | 12.0% | 5.0% | 15.0% | 6.0% | 11.5% | 2.6% | 20.9% |
| **claude opus 4 5** (T=0.0) | 2.5% | 6.5% | 6.5% | 4.0% | 5.0% | 4.0% | 4.1% | 17.9% |
| **claude opus 4 5** (T=0.1) | 3.0% | 7.0% | 6.5% | 5.0% | 5.5% | 6.0% | 3.6% | 15.8% |
| **nova 2 lite** (T=0.0) | **12.5%** | 1.0% | **15.0%** | 1.0% | **27.0%** | 0.0% | **13.8%** | 0.0% |
| **nova 2 lite** (T=0.1) | **11.5%** | 1.5% | **15.0%** | 1.5% | **27.0%** | 0.0% | **13.8%** | 0.0% |
| **nova 2 pro** (T=0.0) | 5.0% | 16.5% | 4.5% | 27.5% | **10.5%** | 26.0% | 2.0% | 24.5% |
| **nova 2 pro** (T=0.1) | 6.0% | 16.0% | 3.5% | 26.5% | **11.5%** | 26.0% | 2.0% | 26.0% |
| **nova premier** (T=0.0) | 1.5% | 10.0% | 3.5% | 9.0% | **10.0%** | 10.0% | 2.6% | 12.8% |
| **nova premier** (T=0.1) | 1.5% | 11.5% | 3.5% | 9.5% | **10.0%** | 9.0% | 3.1% | 13.3% |

**Legend:** C=Complexity, FP%=False Positive %, FN%=False Negative %
Worst 25% in False Postives are **bolded**

---

## Appendix: Model Pricing

| Model | Price per 1M Input Tokens | Price per 1M Output Tokens |
|---|---|---|
| Amazon Nova 2 Lite | $0.33 | $2.75 |
| Amazon Nova Premier | $2.50 | $12.50 |
| Claude 3.7 Sonnet | $3.00 | $15.00 |
| Claude Sonnet 4 | $3.00 | $15.00 |
| Claude Opus 4.5 | $5.50 | $27.50 |

Pricing for Amazon Nova 2 Pro is pending general availability.

*US East (N. Virginia), Standard Tier/Non-Batch, Geo cross-region inference and in-region*


