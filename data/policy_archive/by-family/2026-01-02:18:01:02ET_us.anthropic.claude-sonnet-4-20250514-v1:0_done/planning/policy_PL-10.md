# POLICY: PL-10: Baseline Selection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PL-10 |
| NIST Control | PL-10: Baseline Selection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | baseline, control selection, FISMA, categorization, risk assessment, stakeholder requirements |

## 1. POLICY STATEMENT
All information systems MUST have an appropriate NIST SP 800-53 control baseline selected based on system categorization, stakeholder needs, and regulatory requirements. Baseline selection MUST occur during system planning phase and be documented in the system security plan.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Information Systems | YES | Subject to FISMA requirements |
| Cloud Services | YES | Including FedRAMP authorized services |
| Development Systems | YES | Based on data classification |
| Third-party Systems | CONDITIONAL | When processing organizational data |
| Personal Devices | NO | Covered under separate BYOD policy |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Approve baseline selection<br>• Ensure stakeholder needs assessment<br>• Validate regulatory compliance |
| ISSO/Privacy Officer | • Conduct system categorization<br>• Recommend appropriate baseline<br>• Document baseline rationale |
| Risk Management Team | • Review risk assessments<br>• Validate baseline adequacy<br>• Approve risk-based adjustments |

## 4. RULES

[RULE-01] System owners MUST select a control baseline from NIST SP 800-53B that corresponds to the system's FIPS 199 categorization.
[VALIDATION] IF system_categorization_complete = TRUE AND baseline_selected NOT IN [low, moderate, high] THEN violation

[RULE-02] Baseline selection MUST be completed within 30 days of system categorization approval and before system authorization activities begin.
[VALIDATION] IF categorization_date + 30_days < current_date AND baseline_selection_date = NULL THEN violation

[RULE-03] The selected baseline MUST address all applicable regulatory requirements including FISMA, FedRAMP, SOX, and PCI-DSS based on system function.
[VALIDATION] IF regulatory_requirements_identified = TRUE AND baseline_covers_requirements = FALSE THEN violation

[RULE-04] Baseline selection MUST be supported by documented stakeholder needs analysis and business impact assessment.
[VALIDATION] IF baseline_selected = TRUE AND (stakeholder_analysis = NULL OR business_impact_analysis = NULL) THEN violation

[RULE-05] Systems processing PII MUST select baselines that include privacy control families or approved privacy overlays.
[VALIDATION] IF processes_pii = TRUE AND (privacy_controls_included = FALSE AND privacy_overlay = NULL) THEN violation

[RULE-06] National security systems MUST follow CNSSI 1253 guidance for baseline selection in addition to NIST requirements.
[VALIDATION] IF system_type = "national_security" AND cnssi_1253_compliance = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Categorization Process - Systematic approach to determine FIPS 199 impact levels
- [PROC-02] Stakeholder Needs Assessment - Process to identify mission, business, and regulatory requirements
- [PROC-03] Baseline Selection Documentation - Standard format for recording baseline selection rationale
- [PROC-04] Baseline Review and Approval - Workflow for reviewing and approving baseline selections

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon NIST SP 800-53 updates
- Triggering events: New regulatory requirements, significant system changes, security incidents affecting baseline adequacy

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Moderate System]
IF system_categorization = "moderate"
AND baseline_selected = "NIST_800_53_moderate"
AND stakeholder_analysis_complete = TRUE
AND selection_documented = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Privacy Controls]
IF processes_pii = TRUE
AND baseline_selected = "low"
AND privacy_overlay = NULL
AND privacy_controls_included = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Baseline Selection]
IF system_categorization_date = "2024-01-01"
AND current_date = "2024-02-15"
AND baseline_selection_date = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: FedRAMP Cloud Service]
IF system_type = "cloud_service"
AND fedramp_required = TRUE
AND baseline_selected IN ["fedramp_low", "fedramp_moderate", "fedramp_high"]
AND fedramp_baseline_matches_categorization = TRUE
THEN compliance = TRUE

[SCENARIO-05: Inadequate Baseline for Regulatory Requirements]
IF sox_applicable = TRUE
AND pci_dss_applicable = TRUE
AND baseline_selected = "low"
AND regulatory_gap_analysis = "gaps_identified"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Control baseline selected for system | RULE-01, RULE-02 |
| Baseline addresses stakeholder needs | RULE-03, RULE-04 |
| Selection properly documented | RULE-04, RULE-06 |
| Regulatory compliance ensured | RULE-03, RULE-05 |