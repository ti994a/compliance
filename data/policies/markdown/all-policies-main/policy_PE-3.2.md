# POLICY: PE-3.2: Facility and Systems

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3.2 |
| NIST Control | PE-3.2: Facility and Systems |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | physical security, exfiltration, perimeter checks, facility security, system components |

## 1. POLICY STATEMENT
The organization SHALL perform security checks at defined frequencies at the physical perimeter of facilities and systems to prevent unauthorized exfiltration of information or removal of system components. Security checks MUST be designed to adequately mitigate risks associated with data exfiltration and asset theft.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All company-owned and leased facilities |
| Office Buildings | YES | Buildings containing sensitive systems |
| Cloud Provider Facilities | CONDITIONAL | Where physical access agreements exist |
| Remote Work Locations | NO | Covered under separate telework policy |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Define security check frequencies and procedures<br>• Oversee implementation of perimeter security checks<br>• Review and approve security check schedules |
| Security Operations Center | • Monitor security check completion<br>• Investigate security check anomalies<br>• Coordinate incident response for failed checks |
| Facility Security Officers | • Perform scheduled and random security checks<br>• Document security check results<br>• Report security violations immediately |

## 4. RULES
[RULE-01] Security checks at physical perimeters MUST be performed at minimum daily for high-risk facilities and weekly for standard facilities.
[VALIDATION] IF facility_risk_level = "high" AND last_security_check > 24_hours THEN violation
[VALIDATION] IF facility_risk_level = "standard" AND last_security_check > 168_hours THEN violation

[RULE-02] Random security checks MUST comprise at least 20% of total security checks performed monthly.
[VALIDATION] IF random_checks_percentage < 20% AND month_complete = TRUE THEN violation

[RULE-03] Security checks MUST include inspection for unauthorized devices, media, or materials that could facilitate information exfiltration.
[VALIDATION] IF security_check_scope NOT INCLUDES "exfiltration_devices" THEN violation

[RULE-04] Failed or missed security checks MUST be reported to the Security Operations Center within 2 hours of discovery.
[VALIDATION] IF security_check_status = "failed" AND report_time > 2_hours THEN violation

[RULE-05] All security check activities MUST be documented with timestamp, personnel involved, findings, and corrective actions taken.
[VALIDATION] IF security_check_documentation = "incomplete" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Perimeter Security Check Procedures - Detailed steps for conducting systematic security inspections
- [PROC-02] Exfiltration Risk Assessment - Process for identifying and evaluating information exfiltration risks
- [PROC-03] Security Check Incident Response - Procedures for responding to security check failures or violations
- [PROC-04] Random Security Check Scheduling - Process for implementing unpredictable security check timing

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility changes, regulatory updates, technology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: High-Risk Facility Check Overdue]
IF facility_risk_level = "high"
AND last_security_check > 24_hours
AND business_hours = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Insufficient Random Checks]
IF month_complete = TRUE
AND total_security_checks > 0
AND (random_checks / total_checks) < 0.20
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Undocumented Security Check]
IF security_check_performed = TRUE
AND documentation_complete = FALSE
AND check_date < current_date - 24_hours
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Failed Check Unreported]
IF security_check_status = "failed"
AND incident_reported = FALSE
AND discovery_time > 2_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compliant Standard Facility]
IF facility_risk_level = "standard"
AND last_security_check < 168_hours
AND documentation_complete = TRUE
AND random_check_quota_met = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security checks performed at defined frequency | [RULE-01] |
| Adequate risk mitigation through check frequency | [RULE-01], [RULE-02] |
| Exfiltration prevention focus | [RULE-03] |
| Security check documentation | [RULE-05] |
| Incident reporting for failed checks | [RULE-04] |