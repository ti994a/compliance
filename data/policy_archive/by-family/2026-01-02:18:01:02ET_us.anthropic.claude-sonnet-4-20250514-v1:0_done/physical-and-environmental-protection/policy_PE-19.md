# POLICY: PE-19: Information Leakage

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-19 |
| NIST Control | PE-19: Information Leakage |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | electromagnetic, emanations, TEMPEST, information leakage, signal protection, SCIF, classified systems |

## 1. POLICY STATEMENT
The organization SHALL protect information systems from unintentional information disclosure through electromagnetic signal emanations. Systems processing classified, sensitive, or high-value data MUST implement appropriate electromagnetic shielding and containment measures based on system classification and risk assessment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified Systems | YES | All systems processing classified data |
| High-Value Assets | YES | Systems identified as critical business assets |
| Development Systems | CONDITIONAL | Only if processing sensitive production data |
| Standard Business Systems | CONDITIONAL | Based on data classification and risk assessment |
| SCIF Facilities | YES | All Sensitive Compartmented Information Facilities |
| Data Centers | YES | Primary and backup facilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve electromagnetic protection requirements<br>• Oversee compliance assessments<br>• Define risk tolerance for emanation protection |
| Facilities Security Manager | • Implement physical shielding measures<br>• Coordinate TEMPEST assessments<br>• Maintain emanation protection documentation |
| System Owners | • Identify systems requiring emanation protection<br>• Ensure compliance with protection requirements<br>• Report potential emanation vulnerabilities |

## 4. RULES
[RULE-01] Systems processing classified information MUST implement TEMPEST-certified protection measures or operate within approved SCIF facilities.
[VALIDATION] IF system_classification IN ["SECRET", "TOP_SECRET"] AND (tempest_certified = FALSE AND scif_location = FALSE) THEN critical_violation

[RULE-02] High-value business systems MUST undergo electromagnetic emanation risk assessment within 90 days of deployment.
[VALIDATION] IF system_value = "HIGH" AND days_since_deployment > 90 AND emanation_assessment_completed = FALSE THEN violation

[RULE-03] Systems requiring emanation protection MUST maintain minimum 3-meter separation from untrusted areas unless additional shielding is implemented.
[VALIDATION] IF emanation_protection_required = TRUE AND separation_distance < 3_meters AND additional_shielding = FALSE THEN violation

[RULE-04] Electromagnetic emanation assessments MUST be performed by certified TEMPEST professionals or approved third-party assessors.
[VALIDATION] IF emanation_assessment_required = TRUE AND assessor_certification NOT IN ["TEMPEST_CERTIFIED", "APPROVED_THIRD_PARTY"] THEN violation

[RULE-05] Facilities housing protected systems MUST conduct emanation testing every 24 months or after significant infrastructure changes.
[VALIDATION] IF protected_systems_present = TRUE AND (months_since_last_test > 24 OR significant_infrastructure_change = TRUE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Electromagnetic Emanation Risk Assessment - Systematic evaluation of information leakage risks
- [PROC-02] TEMPEST Compliance Verification - Validation of electromagnetic protection measures
- [PROC-03] Facility Shielding Implementation - Installation and maintenance of electromagnetic barriers
- [PROC-04] Emanation Incident Response - Response procedures for suspected information leakage

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: Security incidents involving emanations, facility modifications, new classified system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Classified System Without Protection]
IF system_classification = "SECRET"
AND tempest_protection = FALSE
AND scif_location = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: High-Value System Assessment Overdue]
IF system_value = "HIGH"
AND emanation_assessment_date < (current_date - 90_days)
AND assessment_waiver = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Insufficient Physical Separation]
IF emanation_protection_required = TRUE
AND separation_from_public_area = 2_meters
AND electromagnetic_shielding = "NONE"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Expired Emanation Testing]
IF facility_houses_classified_systems = TRUE
AND last_emanation_test_date < (current_date - 24_months)
AND test_extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Proper SCIF Implementation]
IF system_classification = "TOP_SECRET"
AND facility_type = "SCIF"
AND scif_certification = "CURRENT"
AND emanation_testing = "PASSED"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System protection from electromagnetic signal emanations | RULE-01, RULE-03 |
| Risk-based protection implementation | RULE-02, RULE-04 |
| Regular assessment and testing | RULE-05 |
| Certified protection measures | RULE-01, RULE-04 |