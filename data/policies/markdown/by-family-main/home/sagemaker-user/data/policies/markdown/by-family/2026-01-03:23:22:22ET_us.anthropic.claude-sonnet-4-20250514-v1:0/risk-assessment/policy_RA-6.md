# POLICY: RA-6: Technical Surveillance Countermeasures Survey

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-6 |
| NIST Control | RA-6: Technical Surveillance Countermeasures Survey |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | surveillance, countermeasures, TSCM, facility security, technical penetration, risk assessment |

## 1. POLICY STATEMENT
The organization SHALL conduct technical surveillance countermeasures (TSCM) surveys at designated facilities to detect unauthorized surveillance devices and identify technical security vulnerabilities. These surveys provide critical input for risk assessments and evaluate organizational exposure to adversarial surveillance activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Executive facilities | YES | CEO, C-suite offices and meeting rooms |
| Classified processing areas | YES | All areas handling classified information |
| R&D facilities | YES | Intellectual property development areas |
| Data centers | YES | Primary and backup facilities |
| Conference rooms | CONDITIONAL | High-sensitivity meeting spaces only |
| Remote offices | CONDITIONAL | If processing sensitive data |
| Vendor facilities | CONDITIONAL | If hosting company data/systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve TSCM survey schedule and scope<br>• Review survey findings and remediation plans<br>• Authorize qualified TSCM service providers |
| Facility Security Manager | • Coordinate TSCM survey scheduling<br>• Ensure facility access for survey teams<br>• Track remediation of identified vulnerabilities |
| Risk Management Office | • Incorporate TSCM findings into risk assessments<br>• Evaluate organizational exposure levels<br>• Update threat models based on survey results |

## 4. RULES
[RULE-01] TSCM surveys MUST be conducted by qualified personnel with appropriate security clearances and technical certifications.
[VALIDATION] IF survey_conducted = TRUE AND (personnel_certified = FALSE OR clearance_verified = FALSE) THEN violation

[RULE-02] Executive facilities and classified processing areas MUST undergo TSCM surveys at least annually.
[VALIDATION] IF facility_classification IN ["executive", "classified"] AND days_since_last_survey > 365 THEN violation

[RULE-03] R&D facilities and sensitive data centers MUST undergo TSCM surveys at least every 18 months.
[VALIDATION] IF facility_type IN ["research", "datacenter"] AND days_since_last_survey > 548 THEN violation

[RULE-04] TSCM surveys MUST include visual, electronic, and physical examinations of both internal and external facility areas.
[VALIDATION] IF survey_scope NOT INCLUDES ["visual", "electronic", "physical"] THEN violation

[RULE-05] Survey findings MUST be documented and provided to facility management within 5 business days of survey completion.
[VALIDATION] IF survey_complete = TRUE AND report_delivery_days > 5 THEN violation

[RULE-06] High-risk vulnerabilities identified during TSCM surveys MUST be remediated within 30 days.
[VALIDATION] IF vulnerability_risk = "high" AND remediation_days > 30 THEN violation

[RULE-07] TSCM survey results MUST be incorporated into organizational risk assessments within 60 days.
[VALIDATION] IF survey_complete = TRUE AND risk_assessment_updated = FALSE AND days_elapsed > 60 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] TSCM Survey Scheduling - Establish survey frequency and coordinate with facility operations
- [PROC-02] Vendor Qualification - Verify TSCM service provider credentials and clearances
- [PROC-03] Survey Scope Definition - Define examination areas and technical requirements
- [PROC-04] Finding Remediation - Process for addressing identified vulnerabilities and weaknesses
- [PROC-05] Risk Assessment Integration - Incorporate survey results into organizational risk models

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Security incidents involving surveillance, facility modifications, threat landscape changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Overdue Executive Survey]
IF facility_type = "executive"
AND days_since_last_survey > 365
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unqualified Survey Personnel]
IF survey_scheduled = TRUE
AND personnel_tscm_certified = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Incomplete Survey Scope]
IF survey_conducted = TRUE
AND survey_includes_external_examination = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed Vulnerability Remediation]
IF vulnerability_identified = TRUE
AND vulnerability_risk_level = "high"
AND remediation_days > 30
AND approved_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Risk Assessment Update]
IF survey_completed = TRUE
AND days_since_completion > 60
AND risk_assessment_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| TSCM surveys employed at designated locations | [RULE-02], [RULE-03] |
| Qualified personnel conduct surveys | [RULE-01] |
| Comprehensive examination scope | [RULE-04] |
| Timely reporting and remediation | [RULE-05], [RULE-06] |
| Risk assessment integration | [RULE-07] |