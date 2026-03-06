# POLICY: SA-15.3: Criticality Analysis

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-15.3 |
| NIST Control | SA-15.3: Criticality Analysis |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | criticality analysis, developer requirements, SDLC, supply chain, high value assets |

## 1. POLICY STATEMENT
The organization requires all system, component, and service developers to perform comprehensive criticality analysis at defined decision points throughout the system development lifecycle. This analysis must meet organization-defined rigor levels for breadth and depth to support organizational risk management and supply chain security decisions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All systems and components |
| Third-party Developers | YES | Contractual requirement |
| COTS Vendors | YES | When feasible through contracts |
| System Components | YES | Based on criticality classification |
| Cloud Services | YES | Provider-dependent analysis required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define criticality analysis requirements<br>• Approve analysis methodologies<br>• Oversee compliance verification |
| Procurement Manager | • Include criticality analysis in contracts<br>• Verify developer compliance<br>• Manage vendor relationships |
| System Owner | • Identify decision points for analysis<br>• Review and validate analysis results<br>• Integrate findings into risk assessments |
| Developer/Vendor | • Perform required criticality analysis<br>• Provide detailed documentation<br>• Update analysis at defined intervals |

## 4. RULES
[RULE-01] Developers MUST perform criticality analysis at all organization-defined SDLC decision points including requirements definition, design review, implementation milestones, and pre-deployment.
[VALIDATION] IF sdlc_decision_point = TRUE AND criticality_analysis_completed = FALSE THEN violation

[RULE-02] Criticality analysis MUST include both breadth (covering all system components, interfaces, and dependencies) and depth (detailed risk assessment of critical functions) as defined in organizational standards.
[VALIDATION] IF analysis_breadth_score < required_breadth_threshold OR analysis_depth_score < required_depth_threshold THEN violation

[RULE-03] High value asset systems MUST receive enhanced criticality analysis with additional rigor including threat modeling, failure mode analysis, and supply chain risk assessment.
[VALIDATION] IF system_classification = "high_value_asset" AND enhanced_analysis_completed = FALSE THEN critical_violation

[RULE-04] Developer criticality analysis documentation MUST be provided within 30 days of each SDLC decision point and include functional specifications, design documents, and risk assessments.
[VALIDATION] IF days_since_decision_point > 30 AND analysis_documentation_received = FALSE THEN violation

[RULE-05] COTS and third-party component criticality analysis MUST be obtained from vendors or performed independently when vendor analysis is unavailable.
[VALIDATION] IF component_type = "COTS" AND (vendor_analysis_received = FALSE AND independent_analysis_completed = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Criticality Analysis Standards - Define methodology, templates, and rigor levels
- [PROC-02] SDLC Decision Point Management - Establish checkpoints and analysis triggers
- [PROC-03] Vendor Analysis Verification - Process for validating third-party analysis
- [PROC-04] High Value Asset Enhanced Analysis - Additional requirements for critical systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon SDLC methodology changes
- Triggering events: New high value asset designation, supply chain incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing SDLC Analysis]
IF sdlc_phase = "design_review"
AND criticality_analysis_status = "not_completed"
AND system_impact_level >= "moderate"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate COTS Analysis]
IF component_type = "COTS"
AND vendor_analysis_provided = FALSE
AND independent_analysis_completed = FALSE
AND system_classification = "high_value_asset"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Late Documentation Delivery]
IF decision_point_date + 30_days < current_date
AND analysis_documentation_received = FALSE
AND developer_extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Insufficient Analysis Depth]
IF analysis_includes_threat_modeling = FALSE
AND system_classification = "high_value_asset"
AND impact_level = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Supply Chain Analysis Gap]
IF third_party_components > 0
AND supply_chain_criticality_analysis = "incomplete"
AND system_processes_sensitive_data = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer performs analysis at defined SDLC decision points | [RULE-01] |
| Analysis meets defined breadth requirements | [RULE-02] |
| Analysis meets defined depth requirements | [RULE-02] |
| Enhanced analysis for high value assets | [RULE-03] |
| Timely documentation delivery | [RULE-04] |
| COTS component analysis coverage | [RULE-05] |