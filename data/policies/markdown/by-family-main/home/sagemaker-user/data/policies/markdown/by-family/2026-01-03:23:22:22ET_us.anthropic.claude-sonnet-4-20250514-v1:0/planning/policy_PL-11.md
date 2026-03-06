# POLICY: PL-11: Baseline Tailoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PL-11 |
| NIST Control | PL-11: Baseline Tailoring |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | baseline, tailoring, control customization, security planning, risk assessment, FISMA, compensating controls |

## 1. POLICY STATEMENT
All information systems MUST have their selected control baselines tailored through documented tailoring actions that reflect organizational mission, business functions, operating environment, and risk profile. Tailoring decisions MUST be documented with clear rationale and approved by authorized personnel before system implementation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Information Systems | YES | FISMA compliance required |
| Cloud Infrastructure | YES | Including hybrid and multi-cloud |
| Third-party Systems | YES | When processing organizational data |
| Development Systems | YES | Based on data classification |
| Legacy Systems | YES | Tailoring during modernization |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Approve tailoring decisions<br>• Ensure business alignment<br>• Accept residual risks |
| Information System Security Officer | • Execute tailoring process<br>• Document tailoring rationale<br>• Validate control implementation |
| Risk Management Team | • Provide risk assessment input<br>• Review tailoring decisions<br>• Assess compensating controls |

## 4. RULES

[RULE-01] Control baseline tailoring MUST follow SP 800-53B guidance and include all six tailoring actions: common control identification, scoping considerations, compensating controls, parameter assignment, control supplementation, and implementation guidance.
[VALIDATION] IF tailoring_actions_count < 6 OR sp800_53b_compliance = FALSE THEN violation

[RULE-02] Tailoring decisions MUST be documented with clear rationale linking to system categorization, risk assessment findings, and organizational requirements.
[VALIDATION] IF tailoring_rationale = NULL OR risk_assessment_reference = NULL THEN violation

[RULE-03] Compensating controls MUST provide equivalent or greater security protection than the original control and SHALL be validated through risk assessment.
[VALIDATION] IF compensating_control_used = TRUE AND (equivalent_protection = FALSE OR risk_validation = NULL) THEN violation

[RULE-04] Control parameter assignments MUST reflect organizational values and be consistent with risk tolerance and operational requirements.
[VALIDATION] IF parameter_assignment = NULL OR organizational_alignment = FALSE THEN violation

[RULE-05] Tailored baselines MUST be reviewed and approved by the System Owner and ISSO before system authorization.
[VALIDATION] IF system_owner_approval = NULL OR isso_approval = NULL AND system_status = "authorized" THEN critical_violation

[RULE-06] Tailoring documentation MUST be updated within 30 days when system changes affect control applicability or effectiveness.
[VALIDATION] IF system_change_date > (tailoring_update_date + 30_days) AND control_impact = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Baseline Selection and Tailoring Process - Systematic approach for applying tailoring actions
- [PROC-02] Compensating Control Evaluation - Assessment methodology for alternative controls
- [PROC-03] Tailoring Documentation Review - Quality assurance for tailoring rationale
- [PROC-04] Stakeholder Approval Workflow - Process for obtaining required approvals

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: System categorization changes, major system modifications, regulatory updates, significant risk environment changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Cloud Migration Tailoring]
IF system_type = "cloud_migration"
AND baseline_selected = TRUE
AND cloud_specific_tailoring = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Compensating Control Implementation]
IF original_control_applicable = FALSE
AND compensating_control_implemented = TRUE
AND risk_assessment_validates_equivalence = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-03: Inadequate Tailoring Documentation]
IF tailoring_actions_applied = TRUE
AND tailoring_rationale = "generic_template"
AND system_specific_justification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Parameter Assignment Missing]
IF control_requires_parameters = TRUE
AND parameter_values_assigned = FALSE
AND system_authorization_date > current_date
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Post-Implementation Changes]
IF system_modification_date < (current_date - 45_days)
AND control_applicability_changed = TRUE
AND tailoring_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Selected control baseline is tailored by applying specified tailoring actions | RULE-01, RULE-02 |
| Tailoring reflects organizational mission and environment | RULE-04, RULE-02 |
| Compensating controls provide equivalent protection | RULE-03 |
| Tailoring decisions are documented and approved | RULE-05, RULE-02 |
| Tailoring documentation remains current | RULE-06 |