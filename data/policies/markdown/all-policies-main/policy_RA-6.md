```markdown
# POLICY: RA-6: Technical Surveillance Countermeasures Survey

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-6 |
| NIST Control | RA-6: Technical Surveillance Countermeasures Survey |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | surveillance, countermeasures, TSCM, facility security, technical penetration, risk assessment |

## 1. POLICY STATEMENT
The organization MUST employ qualified technical surveillance countermeasures (TSCM) surveys at designated sensitive locations to detect technical surveillance devices, identify security weaknesses, and evaluate technical security posture. These surveys SHALL provide comprehensive visual, electronic, and physical examinations to protect against technical penetration and unauthorized surveillance activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Executive facilities | YES | CEO, C-suite offices and meeting rooms |
| Secure conference rooms | YES | Rooms used for sensitive discussions |
| Data centers | YES | Physical infrastructure hosting sensitive systems |
| R&D facilities | YES | Areas with proprietary technology development |
| Standard office spaces | CONDITIONAL | Only if processing classified/highly sensitive data |
| Remote work locations | NO | Individual employee homes excluded |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Security Officer | • Approve TSCM survey schedule and scope<br>• Ensure qualified personnel selection<br>• Review and act on survey findings |
| Facility Security Manager | • Coordinate survey logistics and access<br>• Maintain survey documentation<br>• Implement remediation recommendations |
| TSCM Survey Team | • Conduct comprehensive technical surveys<br>• Document findings and vulnerabilities<br>• Provide remediation recommendations |

## 4. RULES
[RULE-01] TSCM surveys MUST be conducted by certified professionals with appropriate security clearances and specialized detection equipment.
[VALIDATION] IF survey_conducted = TRUE AND surveyor_certified = FALSE THEN violation

[RULE-02] Executive facilities and secure conference rooms MUST undergo TSCM surveys at least annually or before high-sensitivity meetings.
[VALIDATION] IF facility_type = "executive" AND last_survey_date > 365_days THEN violation

[RULE-03] Data centers and R&D facilities MUST undergo TSCM surveys at least every 18 months or after any physical security incidents.
[VALIDATION] IF facility_type IN ["datacenter", "rnd"] AND last_survey_date > 545_days THEN violation

[RULE-04] TSCM surveys MUST include visual, electronic, and physical examinations of both internal and external facility areas.
[VALIDATION] IF survey_scope NOT INCLUDES ["visual", "electronic", "physical", "internal", "external"] THEN violation

[RULE-05] Survey findings MUST be documented in a formal report within 5 business days and remediation plans developed within 15 business days for high-risk findings.
[VALIDATION] IF survey_complete_date + 5_business_days < report_date THEN violation
[VALIDATION] IF finding_risk = "high" AND survey_complete_date + 15_business_days < remediation_plan_date THEN violation

[RULE-06] Access to TSCM survey reports MUST be restricted to personnel with legitimate business need and appropriate security clearance.
[VALIDATION] IF report_access_granted = TRUE AND (business_need = FALSE OR clearance_level < "secret") THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] TSCM Survey Planning - Define scope, schedule, and qualified personnel selection
- [PROC-02] Survey Execution - Standardized methodology for comprehensive facility examination
- [PROC-03] Findings Documentation - Formal reporting and risk categorization process
- [PROC-04] Remediation Management - Tracking and validation of security improvements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Security incidents, facility modifications, regulatory changes, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Annual Executive Survey]
IF facility_type = "executive"
AND last_survey_date > 365_days
AND no_scheduled_survey = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Pre-Meeting Survey]
IF meeting_classification = "highly_sensitive"
AND meeting_location_last_survey > 90_days
AND survey_requested = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unqualified Survey Personnel]
IF tscm_survey_conducted = TRUE
AND surveyor_certification = "none"
AND survey_results_used = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Survey Scope]
IF survey_completed = TRUE
AND survey_scope_missing = ["electronic_sweep"]
AND facility_risk_level = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Delayed Remediation Response]
IF survey_finding_risk = "high"
AND days_since_survey > 15
AND remediation_plan_status = "not_started"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Technical surveillance countermeasures survey employed at defined locations | [RULE-01], [RULE-02], [RULE-03] |
| Qualified personnel conduct surveys | [RULE-01] |
| Comprehensive examination methodology | [RULE-04] |
| Documented findings and response | [RULE-05] |
| Appropriate access controls for survey results | [RULE-06] |
```