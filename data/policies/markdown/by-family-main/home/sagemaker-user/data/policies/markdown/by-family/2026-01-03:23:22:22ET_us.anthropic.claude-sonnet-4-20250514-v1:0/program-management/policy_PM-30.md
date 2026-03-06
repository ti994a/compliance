```markdown
# POLICY: PM-30: Supply Chain Risk Management Strategy

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-30 |
| NIST Control | PM-30: Supply Chain Risk Management Strategy |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | supply chain, risk management, acquisition, vendor management, third-party risk |

## 1. POLICY STATEMENT
The organization SHALL develop, implement, and maintain an organization-wide supply chain risk management strategy that addresses risks across the entire system lifecycle. This strategy MUST be consistently applied across all organizational units and regularly reviewed to ensure continued effectiveness and alignment with organizational changes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational units | YES | Strategy applies organization-wide |
| System development | YES | Internal and contracted development |
| System acquisition | YES | All procurement activities |
| System maintenance | YES | Ongoing support and updates |
| System disposal | YES | End-of-life activities |
| Third-party vendors | YES | All supply chain partners |
| Cloud service providers | YES | Including SaaS, PaaS, IaaS |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Develop and maintain organization-wide supply chain risk strategy<br>• Ensure consistent implementation across organization<br>• Report supply chain risk posture to executive leadership |
| Procurement Officer | • Implement supply chain risk requirements in acquisition processes<br>• Conduct vendor risk assessments<br>• Maintain approved vendor lists |
| System Owners | • Develop system-level supply chain risk management plans<br>• Implement strategy requirements for assigned systems<br>• Monitor and report supply chain risks |

## 4. RULES
[RULE-01] The organization MUST develop a comprehensive supply chain risk management strategy that addresses development, acquisition, maintenance, and disposal phases.
[VALIDATION] IF strategy_exists = FALSE OR lifecycle_phases_covered < 4 THEN violation

[RULE-02] The supply chain risk management strategy MUST include explicit risk appetite and tolerance statements for supply chain risks.
[VALIDATION] IF risk_appetite_defined = FALSE OR risk_tolerance_defined = FALSE THEN violation

[RULE-03] The strategy MUST define acceptable supply chain risk mitigation strategies and controls for each lifecycle phase.
[VALIDATION] IF mitigation_strategies_defined = FALSE OR controls_per_phase < 1 THEN violation

[RULE-04] The organization MUST implement the supply chain risk management strategy consistently across all organizational units.
[VALIDATION] IF implementation_coverage < 100% OR variance_between_units = TRUE THEN violation

[RULE-05] The supply chain risk management strategy MUST be reviewed and updated at least annually or when significant organizational changes occur.
[VALIDATION] IF last_review_date > 365_days OR organizational_change = TRUE AND strategy_updated = FALSE THEN violation

[RULE-06] The strategy MUST establish clear roles and responsibilities for supply chain risk management activities.
[VALIDATION] IF roles_defined = FALSE OR responsibilities_assigned = FALSE THEN violation

[RULE-07] The organization MUST establish processes for consistently evaluating and monitoring supply chain risks.
[VALIDATION] IF evaluation_process_exists = FALSE OR monitoring_process_exists = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment - Standard methodology for evaluating supplier risks
- [PROC-02] Vendor Onboarding - Risk-based approval process for new suppliers
- [PROC-03] Continuous Monitoring - Ongoing assessment of supplier risk posture
- [PROC-04] Incident Response - Procedures for supply chain security incidents
- [PROC-05] Contract Management - Integration of security requirements in supplier contracts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Organizational restructuring, major acquisitions, significant supply chain incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Strategy Component]
IF strategy_exists = TRUE
AND disposal_risks_addressed = FALSE
AND acquisition_risks_addressed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inconsistent Implementation]
IF strategy_approved = TRUE
AND business_unit_A_implementation = "complete"
AND business_unit_B_implementation = "partial"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated Strategy]
IF strategy_last_updated = "2022-01-01"
AND current_date = "2024-01-15"
AND major_org_change = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Complete Compliance]
IF strategy_exists = TRUE
AND all_lifecycle_phases_covered = TRUE
AND consistent_implementation = TRUE
AND annual_review_completed = TRUE
THEN compliance = TRUE

[SCENARIO-05: New Vendor Without Assessment]
IF vendor_status = "new"
AND contract_signed = TRUE
AND supply_chain_risk_assessment = "not_completed"
AND strategy_requires_assessment = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Organization-wide strategy developed | RULE-01 |
| Strategy addresses development risks | RULE-01 |
| Strategy addresses acquisition risks | RULE-01 |
| Strategy addresses maintenance risks | RULE-01 |
| Strategy addresses disposal risks | RULE-01 |
| Strategy implemented consistently | RULE-04 |
| Strategy reviewed and updated regularly | RULE-05 |
| Risk appetite and tolerance defined | RULE-02 |
| Mitigation strategies established | RULE-03 |
| Roles and responsibilities assigned | RULE-06 |
| Evaluation and monitoring processes | RULE-07 |
```