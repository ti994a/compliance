# POLICY: PE-19: Information Leakage

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-19 |
| NIST Control | PE-19: Information Leakage |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | electromagnetic, emanations, TEMPEST, information leakage, signal protection, SCIF |

## 1. POLICY STATEMENT
All information systems SHALL be protected from unintentional information disclosure through electromagnetic signal emanations based on system classification and risk assessment. Protection mechanisms MUST be implemented proportional to the confidentiality requirements and threat environment of the system.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| High confidentiality systems | YES | Mandatory TEMPEST compliance |
| Moderate confidentiality systems | CONDITIONAL | Based on risk assessment |
| Low confidentiality systems | CONDITIONAL | Based on threat environment |
| SCIF facilities | YES | Full electromagnetic protection required |
| Cloud infrastructure | YES | For systems processing confidential data |
| Mobile devices | CONDITIONAL | When processing classified information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve electromagnetic protection standards<br>• Define system classification requirements<br>• Oversee compliance assessments |
| Facilities Manager | • Implement physical electromagnetic shielding<br>• Coordinate TEMPEST facility certifications<br>• Maintain protection equipment |
| System Owners | • Conduct electromagnetic risk assessments<br>• Implement appropriate protection controls<br>• Document protection measures |

## 4. RULES
[RULE-01] Systems processing classified or high confidentiality data MUST implement TEMPEST-compliant electromagnetic protection measures.
[VALIDATION] IF system_classification IN ["classified", "high_confidentiality"] AND tempest_compliant = FALSE THEN critical_violation

[RULE-02] Electromagnetic emanation risk assessments MUST be conducted for all moderate and high confidentiality systems within 90 days of deployment.
[VALIDATION] IF system_confidentiality IN ["moderate", "high"] AND risk_assessment_age > 90_days THEN violation

[RULE-03] Systems in high-threat environments MUST implement electromagnetic shielding regardless of data classification.
[VALIDATION] IF threat_environment = "high" AND electromagnetic_shielding = FALSE THEN violation

[RULE-04] TEMPEST testing MUST be performed annually for classified systems and every two years for high confidentiality systems.
[VALIDATION] IF system_classification = "classified" AND tempest_test_age > 365_days THEN violation
[VALIDATION] IF system_classification = "high_confidentiality" AND tempest_test_age > 730_days THEN violation

[RULE-05] Electromagnetic protection equipment MUST be maintained and tested quarterly to ensure effectiveness.
[VALIDATION] IF protection_equipment_test_age > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Electromagnetic Risk Assessment - Evaluate emanation risks for new systems
- [PROC-02] TEMPEST Testing Protocol - Conduct electromagnetic emanation testing
- [PROC-03] Shielding Installation - Install and validate electromagnetic shielding
- [PROC-04] Equipment Maintenance - Maintain electromagnetic protection systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Security incidents, facility changes, new technology deployment, classification changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Classified System Without TEMPEST]
IF system_classification = "classified"
AND tempest_compliant = FALSE
AND deployment_status = "active"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Overdue Risk Assessment]
IF system_confidentiality = "moderate"
AND risk_assessment_completed = FALSE
AND days_since_deployment > 90
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: High Threat Environment]
IF facility_threat_level = "high"
AND electromagnetic_shielding = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Expired TEMPEST Testing]
IF system_classification = "classified"
AND last_tempest_test_date < (current_date - 365_days)
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Maintenance Compliance]
IF protection_equipment_installed = TRUE
AND last_maintenance_date < (current_date - 90_days)
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System protection from electromagnetic signal emanations | RULE-01, RULE-03 |
| Risk-based protection implementation | RULE-02 |
| Regular testing and validation | RULE-04 |
| Equipment maintenance and effectiveness | RULE-05 |