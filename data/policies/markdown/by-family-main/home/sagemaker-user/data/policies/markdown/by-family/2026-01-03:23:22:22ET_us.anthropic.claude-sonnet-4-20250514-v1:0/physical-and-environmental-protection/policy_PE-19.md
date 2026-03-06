# POLICY: PE-19: Information Leakage

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-19 |
| NIST Control | PE-19: Information Leakage |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | electromagnetic, emanations, TEMPEST, information leakage, signal protection |

## 1. POLICY STATEMENT
All systems processing classified or sensitive information MUST be protected from information leakage due to electromagnetic signal emanations. Protection measures SHALL be implemented based on system security categorization and organizational risk tolerance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| High confidentiality systems | YES | Mandatory TEMPEST protection |
| Moderate confidentiality systems | CONDITIONAL | Risk-based assessment required |
| Low confidentiality systems | CONDITIONAL | Basic shielding may be sufficient |
| Processing facilities | YES | All facilities housing in-scope systems |
| Mobile devices | CONDITIONAL | When processing classified data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Oversee emanations protection program<br>• Approve protection measures<br>• Coordinate with facilities management |
| ISSO/System Owner | • Assess system emanations risk<br>• Implement required protections<br>• Maintain protection documentation |
| Facilities Manager | • Install physical shielding<br>• Maintain environmental controls<br>• Coordinate construction activities |

## 4. RULES
[RULE-01] Systems processing HIGH confidentiality data MUST implement TEMPEST-certified protection measures or equivalent electromagnetic shielding.
[VALIDATION] IF system_confidentiality = "HIGH" AND tempest_certified = FALSE AND equivalent_shielding = FALSE THEN critical_violation

[RULE-02] Electromagnetic emanations testing MUST be conducted within 12 months of system deployment and every 3 years thereafter for high confidentiality systems.
[VALIDATION] IF system_confidentiality = "HIGH" AND last_emanations_test > 36_months THEN violation

[RULE-03] Processing facilities MUST maintain minimum 6-foot separation between HIGH confidentiality systems and external walls, windows, or untrusted areas.
[VALIDATION] IF system_confidentiality = "HIGH" AND distance_to_external < 6_feet AND shielding_installed = FALSE THEN violation

[RULE-04] Emanations risk assessments MUST be completed for all MODERATE confidentiality systems within 90 days of deployment.
[VALIDATION] IF system_confidentiality = "MODERATE" AND emanations_assessment = NULL AND days_since_deployment > 90 THEN violation

[RULE-05] Mobile devices processing classified information MUST use approved emanations-protected cases or operate only in controlled environments.
[VALIDATION] IF device_type = "mobile" AND classification_level > "UNCLASSIFIED" AND protected_case = FALSE AND controlled_environment = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Emanations Risk Assessment - Evaluate electromagnetic leakage risks for new systems
- [PROC-02] TEMPEST Testing - Conduct electromagnetic emanations testing and validation
- [PROC-03] Shielding Installation - Install and maintain electromagnetic shielding measures
- [PROC-04] Facility Design Review - Review facility designs for emanations protection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: New facility construction, system classification changes, security incidents involving emanations

## 7. SCENARIO PATTERNS
[SCENARIO-01: High Confidentiality System Deployment]
IF system_confidentiality = "HIGH"
AND tempest_protection = FALSE
AND equivalent_shielding = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Overdue Emanations Testing]
IF system_confidentiality = "HIGH"
AND last_emanations_test > 36_months
AND system_status = "operational"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Inadequate Physical Separation]
IF system_confidentiality = "HIGH"
AND distance_to_external_wall < 6_feet
AND electromagnetic_shielding = "none"
AND risk_assessment_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Mobile Device Classification Processing]
IF device_type = "mobile"
AND data_classification = "SECRET"
AND emanations_protection = FALSE
AND location = "uncontrolled_environment"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Moderate System Risk Assessment]
IF system_confidentiality = "MODERATE"
AND emanations_risk_assessment = "completed"
AND assessment_conclusion = "low_risk"
AND basic_controls_implemented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System protection from electromagnetic signal emanations | RULE-01, RULE-03 |
| Risk-based protection measures | RULE-04 |
| Testing and validation | RULE-02 |
| Mobile device protection | RULE-05 |