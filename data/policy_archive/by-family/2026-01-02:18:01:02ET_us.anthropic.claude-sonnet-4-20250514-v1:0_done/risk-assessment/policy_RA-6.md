```markdown
# POLICY: RA-6: Technical Surveillance Countermeasures Survey

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-6 |
| NIST Control | RA-6: Technical Surveillance Countermeasures Survey |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | technical surveillance, countermeasures, facility security, penetration testing, risk assessment |

## 1. POLICY STATEMENT
The organization SHALL conduct technical surveillance countermeasures (TSCM) surveys at designated facilities to detect surveillance devices, identify technical security weaknesses, and evaluate the technical security posture. These surveys provide critical input for risk assessments and organizational exposure evaluation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified facilities | YES | All facilities processing classified information |
| Executive offices | YES | C-suite and senior leadership areas |
| Secure meeting rooms | YES | Boardrooms and confidential meeting spaces |
| Data centers | YES | Primary and backup data processing facilities |
| R&D facilities | YES | Areas with sensitive intellectual property |
| Standard office space | CONDITIONAL | Only if processing sensitive customer data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Security Officer | • Approve TSCM survey schedule and scope<br>• Ensure qualified personnel conduct surveys<br>• Review and act on survey findings |
| Facility Security Manager | • Coordinate survey logistics and access<br>• Maintain survey documentation<br>• Implement remediation measures |
| Risk Management Team | • Integrate TSCM findings into risk assessments<br>• Track remediation of identified vulnerabilities<br>• Report on organizational exposure levels |

## 4. RULES
[RULE-01] TSCM surveys MUST be conducted by qualified personnel with appropriate certifications and security clearances.
[VALIDATION] IF survey_conducted = TRUE AND personnel_qualified = FALSE THEN violation

[RULE-02] High-risk facilities SHALL undergo TSCM surveys at least annually, with medium-risk facilities surveyed every 24 months.
[VALIDATION] IF facility_risk = "high" AND last_survey_date > 365_days THEN violation
[VALIDATION] IF facility_risk = "medium" AND last_survey_date > 730_days THEN violation

[RULE-03] TSCM surveys MUST include visual, electronic, and physical examinations of both internal and external facility areas.
[VALIDATION] IF survey_type NOT IN ["visual", "electronic", "physical"] OR coverage NOT IN ["internal", "external"] THEN violation

[RULE-04] Survey findings MUST be documented and remediated within 30 days for critical findings and 90 days for non-critical findings.
[VALIDATION] IF finding_severity = "critical" AND remediation_time > 30_days THEN violation
[VALIDATION] IF finding_severity = "non-critical" AND remediation_time > 90_days THEN violation

[RULE-05] TSCM survey results MUST be integrated into organizational risk assessments within 15 days of survey completion.
[VALIDATION] IF survey_complete_date + 15_days < current_date AND risk_assessment_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] TSCM Survey Planning - Define scope, schedule, and qualified personnel requirements
- [PROC-02] Survey Execution - Conduct visual, electronic, and physical examinations
- [PROC-03] Findings Documentation - Record and classify identified vulnerabilities and exposures
- [PROC-04] Remediation Tracking - Monitor and verify correction of identified issues
- [PROC-05] Risk Assessment Integration - Incorporate findings into organizational risk posture

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: Security incidents, facility modifications, threat level changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Overdue High-Risk Facility Survey]
IF facility_classification = "high_risk"
AND last_tscm_survey > 365_days_ago
AND no_approved_extension = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unqualified Survey Personnel]
IF tscm_survey_conducted = TRUE
AND surveyor_certification = "invalid"
AND security_clearance_level < required_level
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Incomplete Survey Scope]
IF survey_areas NOT INCLUDES "internal_examination"
OR survey_areas NOT INCLUDES "external_examination"
OR survey_methods NOT INCLUDES ["visual", "electronic", "physical"]
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed Critical Finding Remediation]
IF finding_severity = "critical"
AND discovery_date + 30_days < current_date
AND remediation_status = "open"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Risk Assessment Integration]
IF tscm_survey_completed = TRUE
AND survey_completion_date + 15_days < current_date
AND risk_assessment_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Technical surveillance countermeasures survey employed at defined locations | RULE-01, RULE-02 |
| Qualified personnel conduct surveys | RULE-01 |
| Comprehensive examination methodology | RULE-03 |
| Timely remediation of findings | RULE-04 |
| Risk assessment integration | RULE-05 |
```