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
- Uses NIST Open Security Controls Assessment Language (OSCAL) JSON control file as source (https://pages.nist.gov/OSCAL-Reference/models/v1.1.0/complete/json-reference/)
- Developed by the National Institute of Standards and Technology (NIST), OSCAL is a standardized, machine-readable framework (using XML, JSON, or YAML) designed to streamline the documentation, implementation, and assessment of security controls. 
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
- Generates x scenarios (50% compliant, 50% non-compliant)
- Creates diverse, realistic business situations
- Balances scenario complexity and clarity

### 3. Judge Scenarios (`3-JudgeScenarios.ipynb`)
**Purpose**: Evaluate LLM performance on compliance assessment
- Tests multiple LLM models against generated scenarios
- Measures accuracy, consistency, and reasoning quality
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

# LLM Compliance Evaluation Analysis

## Understanding the Stakes

In compliance evaluation, the error types have asymmetric consequences:

| Error Type | What It Means | Risk Level |
|------------|---------------|------------|
| **False Positive (FP)** | Model says "Compliant" when actually **Non-Compliant** | 🔴 **Critical** - Violations slip through |
| **False Negative (FN)** | Model says "Non-Compliant" when actually **Compliant** | 🟡 **Moderate** - Extra review burden |

A **weighted error score**: `Weighted Score = (2 × FP%) + (1 × FN%)` was used to rank performance.

---

## Performance by Complexity Level

### Complexity 4 (Simplest - 4 Policies)

| Model | FP% | FN% | Weighted Score | Rank |
|-------|-----|-----|----------------|------|
| **nova_premier** | 1.5% | 11.5% | **14.5** | 🥇 1st |
| claude_4_sonnet | 2.5% | 10.5% | 15.5 | 🥈 2nd |
| claude_opus_4_5 | 2.5% | 6.5% | 11.5 | 🥇 **Best Overall** |
| claude_3_7_sonnet | 3.0% | 7.5% | 13.5 | 3rd |
| nova_2_lite | 11.0% | 0.5% | **22.5** | ❌ 5th |

**Key Insight:** At low complexity, all models except nova_2_lite perform well. Claude Opus 4.5 achieves the best balance, while Nova Premier has the lowest FP rate but higher FN.

---

### Complexity 6 (Moderate - 6 Policies)

| Model | FP% | FN% | Weighted Score | Rank |
|-------|-----|-----|----------------|------|
| **nova_premier** | 3.5% | 9.5% | **16.5** | 🥇 1st (FP-weighted) |
| claude_3_7_sonnet | 4.0% | 4.0% | 12.0 | 🥇 **Best Overall** |
| claude_4_sonnet | 5.5% | 15.5% | 26.5 | 4th |
| claude_opus_4_5 | 6.5% | 4.0% | 17.0 | 2nd |
| nova_2_lite | 15.0% | 1.0% | **31.0** | ❌ 5th |

**Key Insight:** Claude 3.7 Sonnet excels here with perfectly balanced 4%/4% error rates. Nova Premier maintains the lowest FP rate but trades off with higher FN.

---

### Complexity 8 (High - 8 Policies)

| Model | FP% | FN% | Weighted Score | Rank |
|-------|-----|-----|----------------|------|
| **claude_opus_4_5** | 5.0% | 4.0% | **14.0** | 🥇 **Best** |
| claude_3_7_sonnet | 5.5% | 10.0% | 21.0 | 2nd |
| claude_4_sonnet | 6.0% | 15.0% | 27.0 | 3rd |
| nova_premier | 10.0% | 9.0% | 29.0 | 4th |
| nova_2_lite | 27.0% | 0.0% | **54.0** | ❌ 5th |

**Key Insight:** Claude Opus 4.5 clearly separates from the pack at higher complexity. Nova Premier's FP rate jumps significantly (3.5% → 10%), indicating degradation under complexity.

---

### Complexity 10 (Highest - 10 Policies)

| Model | FP% | FN% | Weighted Score | Rank |
|-------|-----|-----|----------------|------|
| **nova_premier** | 3.1% | 13.3% | **19.5** | 🥇 1st (FP-weighted) |
| claude_3_7_sonnet | 4.1% | 10.2% | 18.4 | 🥇 **Best Overall** |
| claude_4_sonnet | 2.6% | 22.4% | 27.6 | 3rd |
| claude_opus_4_5 | 4.1% | 17.9% | 26.1 | 2nd |
| nova_2_lite | 14.3% | 0.0% | **28.6** | 4th |

**Key Insight:** Interesting reversal—all models show increased FN rates at max complexity, but FP rates actually improve for some (claude_4_sonnet achieves lowest FP at 2.6%). This suggests models become more conservative under complexity.

---

## Model-by-Model Analysis

### 🏆 Claude Opus 4.5 — **Recommended for Production**

| Complexity | FP% | FN% | Assessment |
|------------|-----|-----|------------|
| 4 | 2.5% | 6.5% | ✅ Excellent |
| 6 | 6.5% | 4.0% | ✅ Good |
| 8 | 5.0% | 4.0% | ✅ **Outstanding** |
| 10 | 4.1% | 17.9% | ⚠️ FN spike |

**Verdict:** Most consistent performer across complexity levels. The 5%/4% at Complexity 8 is exceptional. Degradation at Complexity 10 is primarily in FN (acceptable for compliance).

---

### 🥈 Claude 3.7 Sonnet — **Strong Runner-Up**

| Complexity | FP% | FN% | Assessment |
|------------|-----|-----|------------|
| 4 | 3.0% | 7.5% | ✅ Good |
| 6 | 4.0% | 4.0% | ✅ **Excellent** |
| 8 | 5.5% | 10.0% | ✅ Good |
| 10 | 4.1% | 10.2% | ✅ Good |

**Verdict:** Remarkably stable across all complexity levels. Never exceeds 5.5% FP. The balanced 4%/4% at Complexity 6 is noteworthy. **Best cost-performance ratio** if Opus pricing is a concern.

---

### 🥉 Nova Premier — **Conservative Choice**

| Complexity | FP% | FN% | Assessment |
|------------|-----|-----|------------|
| 4 | 1.5% | 11.5% | ✅ Lowest FP |
| 6 | 3.5% | 9.5% | ✅ Lowest FP |
| 8 | 10.0% | 9.0% | ⚠️ FP spike |
| 10 | 3.1% | 13.3% | ✅ Good FP |

**Verdict:** Achieves lowest FP rates at low/medium complexity but shows concerning instability at Complexity 8 (10% FP). The recovery at Complexity 10 is puzzling—may indicate evaluation variance.

---

### ⚠️ Claude 4 Sonnet — **Overly Conservative**

| Complexity | FP% | FN% | Assessment |
|------------|-----|-----|------------|
| 4 | 2.5% | 10.5% | ✅ Good FP |
| 6 | 5.5% | 15.5% | ⚠️ High FN |
| 8 | 6.0% | 15.0% | ⚠️ High FN |
| 10 | 2.6% | 22.4% | ⚠️ **Excessive FN** |

**Verdict:** This model exhibits a strong conservative bias—it flags too many scenarios as non-compliant. While this keeps FP rates reasonable, the 22.4% FN at Complexity 10 means nearly 1 in 4 compliant scenarios get incorrectly flagged, creating significant operational burden.

---

### ❌ Nova 2 Lite — **Not Recommended**

| Complexity | FP% | FN% | Assessment |
|------------|-----|-----|------------|
| 4 | 11.0% | 0.5% | ❌ High FP |
| 6 | 15.0% | 1.0% | ❌ High FP |
| 8 | 27.0% | 0.0% | ❌ **Critical FP** |
| 10 | 14.3% | 0.0% | ❌ High FP |

**Verdict:** This model has a fundamental flaw—it almost always predicts "Compliant." The 0% FN rates are a red flag, not a feature. At 27% FP (Complexity 8), over 1 in 4 non-compliant scenarios would be incorrectly approved. **Unsuitable for compliance use cases.**

---

## Complexity Scaling Trends

```
FP% Trend by Complexity
                    4       6       8       10
                    │       │       │       │
claude_opus_4_5     2.5 ──► 6.5 ──► 5.0 ──► 4.1   ← Most stable
claude_3_7_sonnet   3.0 ──► 4.0 ──► 5.5 ──► 4.1   ← Very stable  
claude_4_sonnet     2.5 ──► 5.5 ──► 6.0 ──► 2.6   ← Variable
nova_premier        1.5 ──► 3.5 ──► 10.0 ──► 3.1  ← Unstable at 8
nova_2_lite         11.0 ─► 15.0 ─► 27.0 ─► 14.3  ← Unacceptable
```

**Key Observations:**
1. **Complexity 8 appears to be a critical threshold** where several models show degradation
2. **Claude models show better stability** across complexity scaling
3. **Nova Premier's Complexity 8 spike** (10% FP) warrants investigation
4. **Complexity 10 results are counterintuitive**—models become more conservative, reducing FP but increasing FN

---

## Final Recommendations

### For Production Compliance Systems

| Priority | Recommendation |
|----------|----------------|
| **Primary** | **Claude Opus 4.5** — Best overall balance, exceptional at high complexity |
| **Budget-Conscious** | **Claude 3.7 Sonnet** — Nearly as good, more predictable behavior |
| **Lowest FP Priority** | **Nova Premier** — Use only for Complexity ≤6 scenarios |

### Configuration Recommendations

| Model | Optimal Use Case |
|-------|------------------|
| Claude Opus 4.5 | Complex multi-policy evaluations (6-10 policies) |
| Claude 3.7 Sonnet | General-purpose compliance, cost-sensitive deployments |
| Nova Premier | Simple policy checks (≤4 policies), with human review escalation |
| Claude 4 Sonnet | Not recommended—excessive false negatives |
| Nova 2 Lite | **Do not use** for compliance |

### Caveats

1. **Temperature settings varied** across models (0.0-0.2)—this may impact comparability
2. **Consider ensemble approaches**: Route complex scenarios to Opus, simple ones to 3.7 Sonnet
3. **Human-in-the-loop**: Even the best model (Opus at 5% FP) means 1 in 20 violations could slip through—implement sampling-based human review

---