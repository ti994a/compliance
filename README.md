# NIST Compliance LLM Evaluation Framework

A comprehensive system for evaluating Large Language Model (LLM) performance on NIST SP 800-53 compliance scenarios to assess price/performance characteristics across different models.

## Overview

This project implements an end-to-end pipeline that transforms NIST cybersecurity controls into realistic compliance scenarios, then evaluates various LLMs' ability to correctly assess compliance. The goal is to provide data-driven insights into which models offer the best price/performance ratio for compliance automation tasks.

## System Architecture

```
NIST SP 800-53 Controls → Organizational Policies → Test Scenarios → LLM Evaluation
       ↓                        ↓                    ↓               ↓
  [Notebook 0]            [Notebook 1]         [Notebook 2]    [Notebook 3]
```

## Workflow Components

### 0. Generate Controls (`0-GenerateControls.ipynb`)
**Purpose**: Extract and process NIST SP 800-53 security controls
- Downloads NIST controls from S3 storage
- Extracts control families and individual controls
- Substitutes organization-specific parameters
- Outputs structured JSONL and markdown formats

### 1. Generate Policies (`1-GeneratePolicies.ipynb`)
**Purpose**: Convert NIST controls into organizational policies using LLM
- Transforms technical controls into business-readable policies
- Uses AWS Bedrock for policy generation
- Creates RAG-optimized policy documents
- Implements validation and quality checks

### 2. Generate Scenarios (`2-GenerateScenarios.ipynb`)
**Purpose**: Create realistic compliance test scenarios
- Generates 1,000 scenarios (500 compliant, 500 non-compliant)
- Uses RAG with AWS Knowledge Base for context-aware generation
- Creates diverse, realistic business situations
- Balances scenario complexity and clarity

### 3. Judge Scenarios (`3-JudgeScenarios.ipynb`)
**Purpose**: Evaluate LLM performance on compliance assessment
- Tests multiple LLM models against generated scenarios
- Measures accuracy, consistency, and reasoning quality
- Calculates price/performance metrics
- Provides comparative analysis across models

## Key Features

- **Multi-Model Evaluation**: Compare performance across different LLM providers and models
- **Realistic Scenarios**: Generate contextually relevant compliance situations
- **Cost Analysis**: Track API costs and processing time for price/performance optimization
- **Validation Pipeline**: Independent judgment system to verify scenario quality
- **Scalable Architecture**: AWS-native implementation for enterprise-scale evaluation

## AWS Services Used

- **AWS Bedrock**: LLM inference and model access
- **Amazon S3**: Data storage and retrieval
- **AWS Knowledge Base**: RAG functionality for context-aware generation
- **SageMaker**: Notebook execution environment

## Getting Started

1. **Setup**: Ensure AWS credentials and Bedrock model access
2. **Run Notebooks**: Execute in sequence (0 → 1 → 2 → 3)
3. **Configure Models**: Update model configurations in notebook 3 for your evaluation targets
4. **Analyze Results**: Review generated metrics and cost analysis

## Output Artifacts

- **Controls**: Processed NIST controls in JSONL/markdown
- **Policies**: Organization-specific policy documents
- **Scenarios**: Labeled compliance test cases
- **Evaluations**: Model performance metrics and cost analysis
- **Reports**: Comparative analysis across LLM models

## Performance Considerations

- **API Throttling**: Implements 1-2 second delays between Bedrock calls
- **Batch Processing**: Optimized for large-scale scenario generation
- **Cost Monitoring**: Tracks token usage and API costs per model
- **Error Handling**: Robust retry logic with exponential backoff

## Use Cases

- **Model Selection**: Choose optimal LLM for compliance automation
- **Cost Optimization**: Identify best price/performance ratios
- **Compliance Automation**: Automate policy adherence checking
- **Risk Assessment**: Evaluate model reliability for regulatory tasks

---

## SageMaker Studio Workspace

### File Organization
- **compliance/**: Main project notebooks and data
- **shared/**: Collaborative files visible to all project members
- **local/**: Private development files

### Collaboration Notes
- Copy files to `shared/` folder when ready to collaborate
- Avoid simultaneous editing of shared files
- Use local folder for frequent development iterations