# POLICY: AU-6.6: Correlation with Physical Monitoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-6.6 |
| NIST Control | AU-6.6: Correlation with Physical Monitoring |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit correlation, physical monitoring, suspicious activity, access correlation, security investigation |

## 1. POLICY STATEMENT
The organization SHALL correlate information from system audit records with physical access monitoring data to enhance detection of suspicious, inappropriate, unusual, or malevolent activity. This correlation capability must be implemented to support security investigations and incident response activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Systems processing sensitive data |
| Physical access control systems | YES | Badge readers, surveillance systems |
| Audit log management systems | YES | SIEM and log aggregation platforms |
| Remote workers | CONDITIONAL | When accessing on-premises resources |
| Third-party facilities | CONDITIONAL | When housing organization systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Monitor correlated audit and physical access data<br>• Investigate suspicious activity patterns<br>• Escalate security incidents |
| Physical Security Team | • Maintain physical access monitoring systems<br>• Provide access to physical security logs<br>• Support correlation investigations |
| System Administrators | • Configure audit correlation capabilities<br>• Ensure system audit logs are available for correlation<br>• Maintain correlation system performance |

## 4. RULES

[RULE-01] Organizations MUST implement automated correlation capabilities between system audit records and physical access monitoring data for all facilities housing sensitive information systems.
[VALIDATION] IF facility_houses_sensitive_systems = TRUE AND correlation_capability = FALSE THEN violation

[RULE-02] Correlation analysis MUST be performed in real-time for critical systems and within 24 hours for standard systems to identify suspicious activity patterns.
[VALIDATION] IF system_criticality = "critical" AND correlation_delay > 0_minutes THEN violation
[VALIDATION] IF system_criticality = "standard" AND correlation_delay > 24_hours THEN violation

[RULE-03] Physical access records SHALL be retained and available for correlation for a minimum of 90 days for standard investigations and 1 year for compliance audits.
[VALIDATION] IF investigation_type = "standard" AND physical_records_retention < 90_days THEN violation
[VALIDATION] IF investigation_type = "compliance" AND physical_records_retention < 365_days THEN violation

[RULE-04] Correlation systems MUST flag discrepancies where logical access occurs without corresponding physical presence within a 30-minute window.
[VALIDATION] IF logical_access = TRUE AND physical_presence = FALSE AND time_window > 30_minutes THEN alert_required

[RULE-05] Personnel conducting correlation analysis MUST have appropriate security clearance and be trained on correlation procedures annually.
[VALIDATION] IF analyst_clearance_level < required_level OR training_date > 365_days_ago THEN access_denied

## 5. REQUIRED PROCEDURES
- [PROC-01] Audit-Physical Correlation Configuration - Establish automated correlation between audit and physical monitoring systems
- [PROC-02] Suspicious Activity Investigation - Define process for investigating correlated security alerts
- [PROC-03] Correlation System Maintenance - Regular testing and calibration of correlation capabilities
- [PROC-04] Incident Escalation - Procedures for escalating correlated security findings

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving physical/logical access, system upgrades, facility changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: After-Hours Logical Access]
IF logical_access_time = "after_hours"
AND physical_presence = FALSE
AND user_authorization_level = "standard"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Terminated Employee Access Attempt]
IF employee_status = "terminated"
AND logical_access_attempt = TRUE
AND physical_access_attempt = TRUE
AND correlation_alert_generated = TRUE
THEN compliance = TRUE

[SCENARIO-03: Contractor Remote Access During Facility Presence]
IF user_type = "contractor"
AND access_method = "remote"
AND physical_presence_at_facility = TRUE
AND correlation_review_conducted = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Multiple Failed Access Attempts]
IF failed_logical_attempts > 3
AND physical_presence = TRUE
AND correlation_investigation_initiated = TRUE
AND timeframe < 1_hour
THEN compliance = TRUE

[SCENARIO-05: VIP Access Without Correlation]
IF user_privilege_level = "administrative"
AND correlation_monitoring = FALSE
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information from audit records is correlated with physical access monitoring | RULE-01, RULE-04 |
| Correlation enhances ability to identify suspicious activity | RULE-02, RULE-04 |
| Supporting evidence for investigations is available | RULE-03 |
| Qualified personnel perform correlation analysis | RULE-05 |