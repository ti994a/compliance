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

## False Positives and False Negatives

For this project:

 - False positive: the judged scenario is non-compliant, but the model incorrectly judged it as compliant.
 - False negative: the judged scenario is compliant, but the model incorrectly judged it as non-compliant.

---
![Confusion Matrix Analysis](/images/unweighted_confusion_matrix_analysis.png)


## Unweighted Model Performance: What the Data Reveals

When false positives and false negatives carry equal weight — a useful baseline before applying compliance-specific risk adjustments — the six models tested fall into two distinct tiers, with some intersting results.

### Unweighted Scoring Summary

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

### The Leaders

In considering unweighted model performance at each model's best performing tempurature:

**Claude 3.7 Sonnet** earns the top spot not by dominating any single metric, but by delivering the most stable performance profile across all four complexity levels. False Positive Rates (FPR) hold steady between 3.0-5.5%, and False Negative Rates (FNR) remain in the 4–10.2% range  as scenario complexity scales from 4 to 10 policies. It displays a gradual, predictable degradation curve that makes it the most operationally reliable choice for teams that need consistent behavior across a wide range of scenario types.

**Claude Opus 4.5** is a strong performer at lower complexity levels. However, it hits a notable cliff at C10: FNR jumps to 17.9%. For organizations whose compliance scenarios are not at the highest complexity levels, Opus 4.5 is a compelling option; for high-complexity assessments, the degradation warrants caution and possibly more investigation.

**Nova Premier** rounds out the top tier with a distinctive profile: the lowest FPR of any model tested (1.5% at C4) and the best FPR performance at both C4 and C6, meaning it is the least likely to pass a non-compliant, low to moderate complexity scenario. Its headline anomaly, however, is a meaningful performance dip at complexity 8 followed by a rebound at complexity 10 — a non-linear pattern not observed in the other models. This behavior is worth investigating further, given the solid performance it displayed overall.

### The Underperformers

**Nova 2 Lite** presents the most extreme failure mode in the dataset. Its maximum FNR is only 1.5% — it almost never flags a legitimate scenarios as a violation — but its FPR goes up to 27%, meaning it flags a large share of non-compliant scenarios as compliant. This represents a significant risk.

**Nova 2 Pro** struggles on both dimensions simultaneously. FPR climbs to 10.5% and its FNR maxes at 27.5%, the second worst and worst results of the group. In unweighted terms, it is the worst performer of the group.

**Claude 4 Sonnet** is perhaps the most counterintuitive result in the dataset. Despite being a newer model than Claude 3.7 Sonnet, it underperforms its predecessor at every complexity level, with FNR climbing steeply to 20.9% at C10. This finding is a direct challenge to the assumption that model recency is a reliable proxy for compliance reasoning capability — a reminder that specialized task performance requires targeted evaluation, not just benchmark comparisons.

### The Complexity Effect: C8 as the Performance Floor

One of the clearest cross-model findings is that scenarios referencing 8 policies (C8) represent the performance floor for most models tested. Accuracy is at or near its worst at this complexity level before either stabilizing or, in Nova Premier's case, good recovery at C10.

---
![Confusion Matrix Analysis](/images/weighted_confusion_matrix_analysis.png)


## Weighted Model Performance

The unweighted analysis treats all errors equally. But in a real compliance workflow, not all errors are created equal. Incorrectly clearing a non-compliant scenario — a false positive — carries meaningfully greater organizational risk than flagging a compliant one. A missed violation can go undetected, potentially exposing the organization to audit findings, regulatory penalties, or unmitigated security risk. An over-flagged compliant scenario, by contrast, generates unnecessary remediation work.

To reflect this asymmetry, the weighted scoring formula penalizes false positives at **2× the rate of false negatives**: `Weighted Score = 100 - ((2 × FP + FN) / Total × 100)`. The results under this scoring scheme reveal a somewhat different picture without affecting the overal unweighted leader and underperformer rankings.

### Weighted Scoring Summary

Weighted scores are calculated as 100 - ((2*FP + FN) / total * 100), penalizing false positives twice as much as false negatives since incorrectly flagging compliant scenarios as violations is considered more costly than missing actual violations. This reflects real-world compliance scenarios where false alarms can waste resources and create unnecessary remediation work.

The full ranked results across all model and temperature combinations are:

## Weighted Scores
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

### The Leaders

**Claude 3.7 Sonnet** retains the top spot under weighted scoring, with its T=0.1 configuration edging out T=0.0 by a narrow margin. The key driver is its consistently low false positive rate across all complexity levels — a profile that holds up well under a scoring scheme that penalizes false positives twice as heavily.

**Claude Opus 4.5** finishes a close second, with its T=0.0 configuration performing best. Its low FPR at C4 and C8 is a genuine strength under weighted scoring. The model's cliff at C10 — where FNR jumps to 17.9% — is less damaging under this scheme than it would be if false negatives were weighted equally, because the penalty for missing a violation is relatively lower. That said, a 17.9% miss rate at high complexity remains a meaningful operational concern.

**Nova Premier** holds its third-place position from the unweighted analysis, with average weighted scores of 80.8 (T=0.0) and 80.2 (T=0.1). Its standout characteristic under weighted scoring is its exceptionally low FPR at C4 (1.5%) and C6 (3.5%) — the lowest of any model tested at those complexity levels. The C8 performance dip (FPR spikes to 10%) is more costly under weighted scoring than it appeared in the unweighted view, and it remains the most notable anomaly in the dataset.

### The Reordering: Nova 2 Lite Rises, Claude 4 Sonnet Falls

The most striking shift between unweighted and weighted results is the **rise of Nova 2 Lite**. Under equal weighting, Nova 2 Lite ranked near the bottom due to its extreme false positive bias (FPR of 24–54%). Under weighted scoring — where false positives are penalized twice as heavily — this bias should, in theory, hurt it even more. And yet Nova 2 Lite scores 82.4, *above* both Claude 4 Sonnet configurations.

The explanation lies in Nova 2 Lite's near-zero false negative rate (0–3%). Under the weighted formula, its FNs contribute almost nothing to the penalty, while its FPs — though high — are partially offset by the fact that it almost never misses a real violation. This creates a counterintuitive result: a model with a severe false positive bias can still score reasonably well under a formula that penalizes FPs more, if its FN rate is low enough to compensate.

This is an important nuance for practitioners: **weighted scoring does not simply punish false-positive-heavy models more**. It rebalances the tradeoff. Nova 2 Lite's profile — high FPR, near-zero FNR — produces a different weighted score than its unweighted score might suggest.

**Claude 4 Sonnet**, by contrast, falls further under weighted scoring. Its relatively high FNR at C10 (43–46%) is penalized at the standard 1× rate, but its FPR is low enough that it doesn't benefit from the weighting the way Nova 2 Lite does. The result is a model that performs poorly on both dimensions without the compensating advantage of near-zero false negatives.

**Nova 2 Pro** remains at the bottom of the rankings under both scoring schemes, with weighted averages of 70.9 and 70.6. Its combination of high FNR (30–53%) and moderate FPR produces the worst overall profile regardless of how errors are weighted.

### What This Means for System Design

The weighted results reinforce the top-line recommendation from the unweighted analysis — **Claude 3.7 Sonnet is the most reliable choice for production compliance workflows** — but they add important nuance:

- **If minimizing false positives is your primary constraint** (e.g., you have limited capacity for human review of flagged scenarios), Claude 3.7 Sonnet and Nova Premier at lower complexity levels offer the best FPR profiles.
- **If minimizing false negatives is your primary constraint** (e.g., you are operating in a high-stakes regulatory environment where missed violations are unacceptable), Claude Opus 4.5 at C4–C8 offers the lowest FNR of any model tested — but plan for human review at C10.
- **Nova 2 Lite's near-zero FNR** makes it a candidate for a first-pass screening layer in a multi-stage pipeline, where its high false positive rate can be filtered by a more precise model downstream. It should not be used as a standalone compliance judge.
- **Avoid Nova 2 Pro** in any compliance-critical workflow. Its combination of high FNR and moderate FPR produces the weakest risk profile under any scoring scheme.


---
![Confusion Matrix Analysis](/images/model_performance_by_complexity.png)


## How Complexity Shapes Model Performance: A Visual Analysis

The unweighted and weighted scoring analyses in the previous sections aggregate performance across all complexity levels into a single ranked score. But compliance scenarios are not uniform — and the question of *how* a model degrades as reasoning demands increase is just as important as where it ranks overall. The `model_performance_by_complexity.png` visualization makes this dynamic visible.

### Reading the Chart

The figure presents two side-by-side line charts — one for best unweighted scores, one for best weighted scores — each plotting all six models across the four complexity levels: C4 (4 policies per scenario), C6, C8, and C10. Each model is represented as a labeled line with markers at each complexity point, using its best-performing temperature configuration. The shape of each line tells a story that aggregate scores alone cannot.

Flat lines indicate robustness — a model that reasons about compliance with equal reliability whether a scenario references 4 policies or 10. Steep downward slopes indicate fragility — a model whose accuracy erodes meaningfully as the number of policies it must synthesize increases. And non-monotonic patterns — dips followed by recoveries — suggest something more complex is happening in how the model processes context at different scales.

### The Stable Performers: Claude 3.7 Sonnet and Claude Opus 4.5

The two models that topped both the unweighted and weighted rankings hold their positions here, and the chart reveals *why*: their lines are the flattest in the visualization.

**Claude 3.7 Sonnet** traces the most consistent path across all four complexity levels in both panels. Its line descends gradually from C4 to C10 without dramatic inflection points, confirming what the aggregate scores suggested: this model's accuracy degrades predictably and proportionally as complexity increases. For teams designing compliance workflows that must handle a wide range of scenario types, this predictability is operationally valuable — you can reason about expected performance at any complexity level without worrying about sudden capability cliffs.

**Claude Opus 4.5** tracks closely with Claude 3.7 Sonnet through C4–C8, with lines that are nearly parallel in the mid-complexity range. The divergence becomes visible at C10, where Claude Opus 4.5's line drops more steeply — the cliff effect identified in the previous sections is clearly visible here as a sharper downward slope in the final segment. In the weighted panel, this drop is somewhat less pronounced, consistent with the earlier finding that the weighted formula partially offsets high FNR by penalizing FP more heavily.

### The Anomaly: Nova Premier's C8 Dip

The most visually distinctive pattern in the chart belongs to **Nova Premier**. Rather than a smooth descent, its line shows a clear V-shape: strong performance at C4 and C6, a meaningful dip at C8, and a partial recovery at C10. This non-monotonic pattern is unique among the six models tested and stands out immediately in both panels.

As noted in the weighted analysis, Nova Premier's FPR spikes at C8 — the point at which its performance is most costly under the weighted scoring formula. The recovery at C10 is genuine but incomplete: Nova Premier does not return to its C6 performance level. The practical implication is that workflows generating a high proportion of C8-equivalent scenarios — those requiring synthesis across 8 policies — should treat Nova Premier's performance estimates with additional caution and consider supplementary human review at that complexity tier.

### The Declining Models: Claude 4 Sonnet and Nova 2 Pro

**Claude 4 Sonnet** shows a steeper and more consistent downward slope than either of the top-tier Claude models, with the most pronounced drop occurring between C6 and C10. The chart makes visually explicit what the aggregate scores implied: this model's performance gap relative to Claude 3.7 Sonnet widens as complexity increases. At C4, the two models are relatively close; by C10, the separation is substantial. This pattern reinforces the earlier finding that model recency is not a reliable predictor of compliance reasoning capability — and the chart makes that divergence impossible to miss.

**Nova 2 Pro** occupies the bottom of both panels across nearly every complexity level, with a line that descends steeply and does not recover. Its combination of high FNR and moderate FPR — neither accurate nor conservative — produces the weakest complexity-adjusted profile in the dataset. The chart confirms that Nova 2 Pro's underperformance is not a complexity-specific phenomenon: it is consistently the weakest model at every level tested.

### The Outlier: Nova 2 Lite's Reordering Under Weighted Scoring

One of the most instructive comparisons between the two panels involves **Nova 2 Lite**. In the unweighted panel, its line sits near the bottom of the chart — a reflection of its extreme false positive bias (FPR of 24–54%) dragging down its equal-weight score. In the weighted panel, its line rises noticeably relative to the other models, crossing above Claude 4 Sonnet and approaching Nova Premier at several complexity levels.

This visual reordering makes concrete the statistical argument from the weighted analysis: Nova 2 Lite's near-zero FNR (0–3%) partially compensates for its high FPR under a formula that penalizes false positives more heavily. The chart allows you to see this tradeoff play out across complexity levels simultaneously — Nova 2 Lite's weighted line is relatively flat, because its FNR advantage is consistent regardless of complexity, even as its FPR disadvantage fluctuates.

### The Takeaway: Complexity Is a First-Class Design Variable

Taken together, the two panels make a clear case that **complexity is not a secondary consideration in model selection — it is a first-class design variable**. The models that perform best in aggregate are not always the models that perform best at the specific complexity level your workflow will encounter most frequently. Nova Premier's C8 anomaly, Claude Opus 4.5's C10 cliff, and Claude 4 Sonnet's widening gap at high complexity are all patterns that aggregate scores obscure but the complexity chart makes visible.

For practitioners, the practical guidance is straightforward: before selecting a model for a compliance workflow, characterize the typical complexity distribution of your scenarios — how many policies does a representative scenario reference? — and use the complexity-adjusted performance curves, not just the aggregate rankings, to inform your decision.






## Conclusion: Choosing the Right LLM for NIST Compliance Automation

The results of this evaluation offer a nuanced picture of how six leading LLMs perform on NIST SP 800-53 compliance reasoning tasks. Across 1,000 labeled compliance scenarios, four complexity levels, two temperature configurations, and three distinct scoring lenses — unweighted accuracy, weighted risk-adjusted scoring, and complexity-adjusted performance curves — meaningful differences emerge in accuracy, failure modes, cost, and robustness. The right model for any given deployment will depend on the specific risk posture, complexity distribution, and budget constraints of the organization.

### Understanding the Scorecard

Before diving into results, it helps to understand what each metric in the table below is measuring — and why it matters.

**Weighted scoring** is the primary lens for this evaluation. In a compliance context, not all errors carry equal weight. Incorrectly clearing a non-compliant scenario — a *false positive* — is more dangerous than flagging a compliant one, because a missed violation can go undetected and expose the organization to real risk. The weighted score formula penalizes false positives at twice the rate of false negatives: `100 − ((2 × FP + FN) / Total × 100)`. A score of 100 would mean zero errors; a score of 0 would mean every judgment was wrong.

**Scenario complexity** refers to how many organizational policies a model must read and reason across simultaneously to reach a compliance judgment. Scenarios in this evaluation reference 4, 6, 8, or 10 policies (labeled C4 through C10). More policies mean more context to synthesize — and more opportunity for a model to make mistakes.

The five columns in the table each tell a different part of the story:

- **Weighted Score (Avg)** — The model's average risk-adjusted accuracy across all complexity levels, using its best temperature setting. *Think of this as the model's overall grade.* Higher is better.
- **Best Weighted Score (Single Complexity)** — The highest score the model achieved at any single complexity level. *This is the model's peak performance under ideal conditions* — useful for understanding what the model is capable of when scenarios align with its strengths.
- **Worst Weighted Score (Single Complexity)** — The lowest score the model achieved at any single complexity level. *This is the model's floor — its worst-case performance.* A low floor means the model can fail badly under certain conditions, even if its average looks acceptable.
- **Complexity Robustness (point drop)** — The difference between the best and worst single-complexity scores. *This measures how much the model degrades as scenarios get harder.* A small drop means the model performs consistently regardless of complexity; a large drop means it struggles when asked to reason across many policies at once.
- **Input / Output Price** — The cost per million tokens processed. *This is the direct cost lever* — the price you pay per unit of work, independent of accuracy.

### The Price/Performance Summary

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

### The Top Tier: Accuracy and Consistency

**Claude 3.7 Sonnet (T=0.1)** achieves the highest average weighted score (83.8) and the tightest performance range of the top three models — a floor of 79.0 and a ceiling of 88.0, with only a 9.0-point spread across all complexity levels. For executives, this translates to predictability: the model behaves consistently whether scenarios are simple or complex. 

**Claude Opus 4.5 (T=0.0)** achieves the highest single-complexity peak of any model tested (88.5 at C4) and excels through mid-complexity scenarios, reaching 86.0 at C8 — the highest C8 score in the evaluation. However, it hits a notable cliff at C10, where its score drops to 74.0, producing a 14.5-point robustness gap. At $5.50 per million input tokens — 83% more than Claude 3.7 Sonnet — the premium is difficult to justify unless minimizing missed violations at lower complexity levels is the overriding priority.

**Nova Premier (T=0.0)** rounds out the top tier with an average weighted score of 80.8 and the lowest input price of the top three at $2.50 per million tokens. Its peak score of 87.0 at C4 is competitive with the top Claude models. The headline concern is its C8 floor of 70.0 — the lowest worst-case score in the top tier — driven by a spike in false positives at that complexity level before partially recovering at C10. For executives: Nova Premier is a strong value option for workflows where most scenarios reference fewer than 8 policies, but teams should plan for additional human review at the 8-policy complexity tier. As a fully Amazon-native model, it also benefits from the tightest integration with the broader AWS ecosystem.

### A Note on Claude 4 Sonnet

**Claude 4 Sonnet (T=0.1)** scores 76.6 on the weighted scale — meaningfully below both Claude 3.7 Sonnet and Claude Opus 4.5, despite carrying the same price tag as Claude 3.7 Sonnet ($3.00 per million input tokens). Its peak of 81.0 and floor of 74.0 reflect a model that underperforms its predecessor at every complexity level. Its 7.0-point robustness gap is the smallest of any model tested, but this reflects a consistently moderate performance profile rather than genuine resilience: its floor of 74.0 is lower than Claude 3.7 Sonnet's floor of 79.0, despite the smaller spread. For executives: at the same price as Claude 3.7 Sonnet, Claude 4 Sonnet delivers less accuracy. This finding is a direct challenge to the assumption that a newer model generation automatically means better performance on specialized tasks.

### The Specialized Cases: Nova 2 Lite and Nova 2 Pro

**Nova 2 Lite (T=0.1)** presents the most extreme tradeoff in the dataset. Its average weighted score of 65.6 and worst-case floor of 46.0 at C8 reflect a model with a severe false positive bias — it flags a large share of compliant scenarios as violations. The 29.5-point robustness gap is the largest in the evaluation. For executives: this model almost never misses a real violation, but it generates a high volume of false alarms — meaning compliance teams would spend significant time investigating issues that turn out to be non-problems. At $0.33 per million input tokens — roughly 9× cheaper than Claude 3.7 Sonnet — Nova 2 Lite is best suited as a **first-pass screening layer** in a multi-stage pipeline, where its high recall can be leveraged and its false positive rate filtered by a more precise model downstream. It should not be used as a standalone compliance judge.

**Nova 2 Pro (T=0.0)** finishes last in average weighted score (65.4), with a floor of 53.0 at C8 and a 20.5-point robustness gap. For executives: this model misses a significant share of real violations while also generating false alarms — the worst of both failure modes simultaneously. Pricing is pending general availability, but performance results alone make it difficult to recommend for compliance-critical workflows in its current form.

### Design Principles for Production Compliance Workflows

This evaluation surfaces several principles that should inform how teams architect AI-assisted compliance systems on AWS:

**Match model selection to your complexity distribution.** The number of policies a scenario must reference is a first-class predictor of model accuracy. Before selecting a model, characterize the typical complexity of your scenarios and use the Best and Worst Weighted Score columns — not just the average — to understand each model's performance range at the complexity levels your workflow will encounter most frequently.

**Treat false positives and false negatives as asymmetric risks.** The weighted scoring results diverge meaningfully from equal-weight accuracy, and the right balance depends on your organization's specific risk posture. A team with limited capacity for human review should optimize for low false positive rates; a team operating under strict regulatory scrutiny should optimize for low false negative rates. The weighted score formula used here — penalizing false positives at 2× — reflects one reasonable calibration, but organizations should validate this weighting against their own compliance risk model.

**Consider multi-stage architectures for cost-sensitive deployments.** Nova 2 Lite's near-zero false negative rate at a fraction of the cost of frontier models makes it a viable first-pass filter. A pipeline that uses Nova 2 Lite to flag potential violations and Claude 3.7 Sonnet or Nova Premier to adjudicate flagged cases could achieve near-top-tier accuracy at significantly lower per-scenario cost.

**Don't assume newer means better for specialized tasks.** Claude 4 Sonnet's underperformance relative to Claude 3.7 Sonnet at the same price point is a finding that generalizes beyond this specific evaluation: compliance reasoning is a specialized capability that requires targeted benchmarking. General-purpose model benchmarks are not a substitute for task-specific evaluation.

### Looking Ahead

This framework is designed to evolve alongside the models it evaluates. As Amazon Bedrock continues to expand its model catalog — and as Amazon Nova 2 Pro reaches general availability with published pricing — the pipeline can be extended to incorporate new entrants without modification to the core evaluation architecture. Future work will explore fine-tuning approaches for models that show systematic failure modes at high complexity, expanded scenario coverage across additional NIST control families, and cost modeling that accounts for full token consumption across multi-turn compliance workflows.

The core finding, however, is durable: **rigorous, task-specific evaluation is the only reliable basis for model selection in compliance-critical AI applications.** The differences between models in this evaluation — in accuracy, in failure modes, in cost, and in how performance degrades with complexity — are large enough to have real operational and financial consequences. The framework described in this post provides a reproducible, extensible methodology for making those differences visible.

---

*To explore the models evaluated in this post, visit [Amazon Bedrock](https://aws.amazon.com/bedrock/). To build and run evaluation pipelines like this one, see [Amazon SageMaker Unified Studio](https://aws.amazon.com/sagemaker/). For guidance on NIST SP 800-53 compliance on AWS, visit the [AWS Compliance Center](https://aws.amazon.com/compliance/programs/).*








---

## Confusion Matrix Summary
| Model & Temp | C4-TP | C4-FP | C4-FN | C4-TN | C4-FPR | C4-FNR | C6-TP | C6-FP | C6-FN | C6-TN | C6-FPR | C6-FNR | C8-TP | C8-FP | C8-FN | C8-TN | C8-FPR | C8-FNR | C10-TP | C10-FP | C10-FN | C10-TN | C10-FPR | C10-FNR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **claude 3 7 sonnet** (T=0.0) | 89 | 7 | 16 | 88 | 7.4% | 15.2% | 91 | 8 | 9 | 92 | 8.0% | 9.0% | 76 | 10 | 24 | 90 | 10.0% | 24.0% | 75 | 7 | 21 | 93 | 7.0% | 21.9% |
| **claude 3 7 sonnet** (T=0.1) | 90 | 6 | 15 | 89 | 6.3% | 14.3% | 92 | 8 | 8 | 92 | 8.0% | 8.0% | 80 | 11 | 20 | 89 | 11.0% | 20.0% | 76 | 8 | 20 | 92 | 8.0% | 20.8% |
| **claude 4 sonnet** (T=0.0) | 84 | 5 | 21 | 90 | 5.3% | 20.0% | 69 | 11 | 31 | 89 | 11.0% | 31.0% | 70 | 12 | 30 | 88 | 12.0% | 30.0% | 52 | 5 | 44 | 95 | 5.0% | 45.8% |
| **claude 4 sonnet** (T=0.1) | 81 | 7 | 24 | 88 | 7.4% | 22.9% | 70 | 10 | 30 | 90 | 10.0% | 30.0% | 77 | 12 | 23 | 88 | 12.0% | 23.0% | 55 | 5 | 41 | 95 | 5.0% | 42.7% |
| **claude opus 4 5** (T=0.0) | 92 | 5 | 13 | 90 | 5.3% | 12.4% | 92 | 13 | 8 | 87 | 13.0% | 8.0% | 92 | 10 | 8 | 90 | 10.0% | 8.0% | 61 | 8 | 35 | 92 | 8.0% | 36.5% |
| **claude opus 4 5** (T=0.1) | 91 | 6 | 14 | 89 | 6.3% | 13.3% | 90 | 13 | 10 | 87 | 13.0% | 10.0% | 88 | 11 | 12 | 89 | 11.0% | 12.0% | 65 | 7 | 31 | 93 | 7.0% | 32.3% |
| **nova 2 lite** (T=0.0) | 103 | 25 | 2 | 70 | 26.3% | 1.9% | 98 | 30 | 2 | 70 | 30.0% | 2.0% | 100 | 54 | 0 | 46 | 54.0% | 0.0% | 96 | 27 | 0 | 73 | 27.0% | 0.0% |
| **nova 2 lite** (T=0.1) | 102 | 23 | 3 | 72 | 24.2% | 2.9% | 97 | 30 | 3 | 70 | 30.0% | 3.0% | 100 | 54 | 0 | 46 | 54.0% | 0.0% | 96 | 27 | 0 | 73 | 27.0% | 0.0% |
| **nova 2 pro** (T=0.0) | 72 | 10 | 33 | 85 | 10.5% | 31.4% | 45 | 9 | 55 | 91 | 9.0% | 55.0% | 48 | 21 | 52 | 79 | 21.0% | 52.0% | 48 | 4 | 48 | 96 | 4.0% | 50.0% |
| **nova 2 pro** (T=0.1) | 73 | 12 | 32 | 83 | 12.6% | 30.5% | 47 | 7 | 53 | 93 | 7.0% | 53.0% | 48 | 23 | 52 | 77 | 23.0% | 52.0% | 45 | 4 | 51 | 96 | 4.0% | 53.1% |
| **nova premier** (T=0.0) | 85 | 3 | 20 | 92 | 3.2% | 19.0% | 82 | 7 | 18 | 93 | 7.0% | 18.0% | 80 | 20 | 20 | 80 | 20.0% | 20.0% | 71 | 5 | 25 | 95 | 5.0% | 26.0% |
| **nova premier** (T=0.1) | 82 | 3 | 23 | 92 | 3.2% | 21.9% | 81 | 7 | 19 | 93 | 7.0% | 19.0% | 82 | 20 | 18 | 80 | 20.0% | 18.0% | 70 | 6 | 26 | 94 | 6.0% | 27.1% |

**Legend:** C=Complexity, TP=True Positive, FP=False Positive, FN=False Negative, TN=True Negative
FPR = False Positive Rate (FP/(FP+TN)), FNR = False Negative Rate (FN/(FN+TP))


## Pricing Comparison

| Model | Price per 1M Input Tokens | Price per 1M Output Tokens |
|---|---|---|
| Amazon Nova 2 Lite | $0.33 | $2.75 |
| Amazon Nova Premier | $2.50 | $12.50 |
| Claude 3.7 Sonnet | $3.00 | $15.00 |
| Claude Sonnet 4 | $3.00 | $15.00 |
| Claude Opus 4.5 | $5.50 | $27.50 |

Pricing for Amazon Nova 2 Pro is pending general availability.

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

