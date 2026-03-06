# POLICY: PL-11: Baseline Tailoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PL-11 |
| NIST Control | PL-11: Baseline Tailoring |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | baseline, tailoring, control customization, security plan, privacy plan, FISMA, risk assessment |

## 1. POLICY STATEMENT
Organizations MUST tailor selected control baselines by applying documented tailoring actions that reflect specific mission requirements, operational environments, and risk profiles. All baseline tailoring activities MUST be documented with clear rationale and approved through established governance processes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems requiring security/privacy plans |
| Cloud Services | YES | Including hybrid and multi-cloud deployments |
| Third-party Systems | YES | When organization controls baseline selection |
| Development Environments | CONDITIONAL | Only if processing regulated data |
| Legacy Systems | YES | Must document tailoring constraints |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Identify mission-specific requirements<br>• Approve tailoring decisions<br>• Ensure business alignment |
| Security Architect | • Execute tailoring methodology<br>• Document tailoring rationale<br>• Validate control adequacy |
| Compliance Manager | • Verify regulatory alignment<br>• Review tailoring documentation<br>• Coordinate assessor reviews |

## 4. RULES

[RULE-01] Organizations MUST apply tailoring actions using NIST SP 800-53B methodology or equivalent approved framework.
[VALIDATION] IF tailoring_methodology != "NIST_SP_800-53B" AND approved_equivalent = FALSE THEN violation

[RULE-02] All tailoring decisions MUST be documented with specific rationale linking to mission requirements, operational constraints, or risk assessments.
[VALIDATION] IF tailoring_action_documented = TRUE AND rationale_provided = FALSE THEN violation

[RULE-03] Compensating controls MUST provide equivalent security/privacy protection when baseline controls are modified or removed.
[VALIDATION] IF baseline_control_modified = TRUE AND compensating_control_equivalent = FALSE THEN critical_violation

[RULE-04] Control parameter assignments MUST align with organizational risk tolerance and regulatory requirements.
[VALIDATION] IF parameter_assignment != organizational_standard AND exception_approved = FALSE THEN violation

[RULE-05] Tailored baselines MUST be reviewed and approved by designated security and privacy officials before implementation.
[VALIDATION] IF tailored_baseline_approved = FALSE AND implementation_started = TRUE THEN critical_violation

[RULE-06] Supplemental controls added beyond baseline MUST address identified gaps from risk assessments or regulatory analysis.
[VALIDATION] IF supplemental_controls_added = TRUE AND gap_analysis_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Baseline Selection and Categorization - Select appropriate baseline using system categorization
- [PROC-02] Tailoring Action Documentation - Document all tailoring decisions with rationale
- [PROC-03] Compensating Control Analysis - Evaluate equivalent protection for modified controls
- [PROC-04] Stakeholder Review and Approval - Obtain required approvals before implementation
- [PROC-05] Tailoring Rationale Maintenance - Update documentation when conditions change

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Major system changes, new regulatory requirements, significant risk assessment findings, baseline updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Control Removal]
IF baseline_control_status = "removed"
AND compensating_control_implemented = FALSE
AND risk_acceptance_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Undocumented Parameter Changes]
IF control_parameter_modified = TRUE
AND modification_rationale = "not_documented"
AND system_categorization = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Supplemental Controls Without Justification]
IF additional_controls_added = TRUE
AND gap_analysis_exists = FALSE
AND regulatory_requirement_identified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Approved Tailoring with Documentation]
IF tailoring_methodology = "NIST_SP_800-53B"
AND all_decisions_documented = TRUE
AND security_officer_approval = TRUE
THEN compliance = TRUE

[SCENARIO-05: Cloud Service Baseline Mismatch]
IF deployment_model = "cloud"
AND baseline_selection != "cloud_appropriate"
AND tailoring_addresses_cloud_risks = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Selected control baseline is tailored using specified actions | RULE-01, RULE-02 |
| Tailoring decisions are documented and justified | RULE-02, RULE-06 |
| Modified controls maintain equivalent protection | RULE-03 |
| Parameter assignments reflect organizational needs | RULE-04 |
| Tailored baseline receives proper approval | RULE-05 |