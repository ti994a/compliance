```markdown
# POLICY: PE-8: Visitor Access Records

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-8 |
| NIST Control | PE-8: Visitor Access Records |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | visitor access, physical security, access records, facility security, anomaly detection |

## 1. POLICY STATEMENT
The organization MUST maintain comprehensive visitor access records for facilities housing information systems, conduct regular reviews of these records, and report any identified anomalies to designated security personnel.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All facilities housing information systems | YES | Excludes publicly accessible areas |
| Data centers and server rooms | YES | Enhanced monitoring required |
| Office buildings with system access | YES | Standard monitoring applies |
| Remote work locations | NO | Individual workspace exemption |
| Publicly accessible lobbies/cafeterias | NO | No visitor logging required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Establish visitor access record procedures<br>• Define anomaly reporting processes<br>• Ensure compliance with retention requirements |
| Security Guards/Reception | • Collect required visitor information<br>• Maintain accurate access logs<br>• Verify visitor identification |
| Facility Security Officers | • Conduct periodic record reviews<br>• Investigate and report anomalies<br>• Coordinate with IT security teams |

## 4. RULES
[RULE-01] Visitor access records MUST include visitor name, organization, signature, identification form, access dates/times, visit purpose, and host information.
[VALIDATION] IF visitor_record_created = TRUE AND (name = NULL OR organization = NULL OR signature = NULL OR id_verification = NULL OR entry_time = NULL OR exit_time = NULL OR purpose = NULL OR host = NULL) THEN violation

[RULE-02] Visitor access records SHALL be maintained for a minimum of 3 years from the date of visit.
[VALIDATION] IF record_age > 3_years AND record_deleted = TRUE AND legal_hold = FALSE THEN compliant
[VALIDATION] IF record_age < 3_years AND record_deleted = TRUE THEN violation

[RULE-03] Visitor access records MUST be reviewed monthly for anomalies and unauthorized access patterns.
[VALIDATION] IF last_review_date > 30_days_ago THEN violation

[RULE-04] Anomalies in visitor access records MUST be reported to the Physical Security Manager and IT Security Team within 24 hours of discovery.
[VALIDATION] IF anomaly_detected = TRUE AND report_time > 24_hours THEN violation

[RULE-05] Visitors MUST NOT be granted unescorted access to facilities housing information systems without proper authorization.
[VALIDATION] IF visitor_type = "unescorted" AND authorization_level < "facility_access" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Visitor Registration Process - Standardized check-in/check-out procedures with required documentation
- [PROC-02] Access Record Review Process - Monthly systematic review of visitor logs for anomalies
- [PROC-03] Anomaly Investigation Process - Procedures for investigating and documenting suspicious visitor activities
- [PROC-04] Record Retention Process - Secure storage and disposal of visitor access records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving visitors, facility modifications, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Incomplete Visitor Record]
IF visitor_logged = TRUE
AND required_fields_complete < 100%
AND facility_type = "data_center"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Overdue Record Review]
IF last_review_date > 35_days_ago
AND facility_houses_systems = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-03: Unreported Access Anomaly]
IF anomaly_detected = TRUE
AND detection_date < current_date - 2_days
AND reported_to_security = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Premature Record Deletion]
IF visitor_record_age < 3_years
AND record_status = "deleted"
AND legal_hold_active = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unescorted Visitor in Restricted Area]
IF visitor_escort_status = "unescorted"
AND area_classification = "restricted"
AND visitor_clearance_level < "facility_access"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Maintain visitor access records for defined time period | [RULE-02] |
| Review visitor access records at defined frequency | [RULE-03] |
| Report anomalies in visitor access records | [RULE-04] |
| Collect comprehensive visitor information | [RULE-01] |
| Control unescorted visitor access | [RULE-05] |
```