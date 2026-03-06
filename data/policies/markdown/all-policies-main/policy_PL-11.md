# POLICY: PL-11: Baseline Tailoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PL-11 |
| NIST Control | PL-11: Baseline Tailoring |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | baseline, tailoring, controls, customization, security plan, privacy plan, FISMA, risk assessment |

## 1. POLICY STATEMENT
Organizations MUST tailor selected control baselines by applying documented tailoring actions to reflect specific mission requirements, operational environments, and risk conditions. All baseline tailoring decisions MUST be documented with appropriate justification and approved through the established governance process.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems requiring security/privacy plans |
| Cloud Services | YES | Including hybrid and multi-cloud environments |
| Third-Party Systems | CONDITIONAL | When organization controls baseline selection |
| Development Projects | YES | During system design and implementation phases |
| Legacy Systems | YES | During reauthorization cycles |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Define mission-specific requirements<br>• Approve tailoring decisions<br>• Ensure operational feasibility |
| CISO/Privacy Officer | • Review tailoring rationale<br>• Approve baseline modifications<br>• Ensure compliance alignment |
| Risk Management Team | • Conduct risk assessments<br>• Validate compensating controls<br>• Document risk acceptance decisions |
| Security Architects | • Apply technical tailoring actions<br>• Select appropriate control parameters<br>• Design compensating controls |

## 4. RULES
[RULE-01] Organizations MUST apply tailoring actions from SP 800-53B or equivalent approved methodology when customizing control baselines.
[VALIDATION] IF baseline_tailoring_performed = TRUE AND methodology_source NOT IN [SP800-53B, approved_alternatives] THEN violation

[RULE-02] All tailoring actions MUST be documented with clear rationale linking to organizational mission, operational environment, threat landscape, or regulatory requirements.
[VALIDATION] IF tailoring_action_applied = TRUE AND rationale_documented = FALSE THEN violation

[RULE-03] Common controls MUST be identified and designated during baseline tailoring to avoid duplication and ensure consistent implementation across systems.
[VALIDATION] IF common_controls_identified = FALSE AND multiple_systems = TRUE THEN violation

[RULE-04] Compensating controls MUST be selected and implemented when baseline controls cannot be applied due to technical, operational, or cost constraints.
[VALIDATION] IF baseline_control_not_applicable = TRUE AND compensating_control_selected = FALSE AND risk_accepted = FALSE THEN critical_violation

[RULE-05] Control parameters MUST be assigned specific organizational values based on risk assessment results and operational requirements.
[VALIDATION] IF control_parameters_exist = TRUE AND parameter_values_assigned = FALSE THEN violation

[RULE-06] Tailored baselines MUST be reviewed and approved by designated authorities before system authorization.
[VALIDATION] IF baseline_tailored = TRUE AND approval_documented = FALSE THEN critical_violation

[RULE-07] Tailoring decisions MUST be reassessed during system reauthorization or when significant changes occur to mission, environment, or threat landscape.
[VALIDATION] IF (reauthorization_due = TRUE OR significant_change = TRUE) AND tailoring_reassessment_performed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Baseline Selection and Tailoring Process - Defines methodology for selecting and customizing control baselines
- [PROC-02] Common Control Identification - Establishes process for designating shared organizational controls
- [PROC-03] Compensating Control Selection - Provides framework for selecting alternative security measures
- [PROC-04] Parameter Assignment Methodology - Defines approach for setting organizational control parameter values
- [PROC-05] Tailoring Documentation Standards - Specifies required documentation and rationale formats

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: New NIST guidance release, significant regulatory changes, major organizational restructuring, post-incident reviews

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Migration Tailoring]
IF system_type = "cloud_migration"
AND baseline_selected = "NIST_moderate"
AND cloud_specific_controls_added = TRUE
AND tailoring_rationale_documented = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Compensating Controls]
IF baseline_control_not_applicable = TRUE
AND compensating_control_implemented = FALSE
AND risk_acceptance_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Inadequate Parameter Assignment]
IF control_parameters_exist = TRUE
AND parameter_values = "default_generic"
AND risk_assessment_completed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unapproved Tailoring Actions]
IF baseline_modified = TRUE
AND tailoring_methodology = "custom_undocumented"
AND formal_approval_obtained = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Common Controls Not Leveraged]
IF organizational_common_controls_available = TRUE
AND system_implements_duplicate_controls = TRUE
AND common_control_designation = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Selected control baseline is tailored using specified actions | RULE-01, RULE-02 |
| Tailoring actions are properly documented and justified | RULE-02, RULE-06 |
| Common controls are identified and designated | RULE-03 |
| Compensating controls address inapplicable baseline controls | RULE-04 |
| Control parameters are assigned organizational values | RULE-05 |
| Tailored baseline receives appropriate approval | RULE-06 |
| Tailoring decisions are periodically reassessed | RULE-07 |