# POLICY: SI-7.16: Time Limit on Process Execution Without Supervision

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.16 |
| NIST Control | SI-7.16: Time Limit on Process Execution Without Supervision |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | process execution, supervision, time limits, system monitoring, automated responses, process anomalies |

## 1. POLICY STATEMENT
All system processes MUST operate under defined supervision mechanisms with maximum execution time limits to prevent unauthorized or runaway processes. Organizations SHALL implement automated monitoring and response capabilities to detect and terminate processes that exceed established time thresholds without proper supervision.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All critical business systems |
| Development Systems | YES | Systems processing sensitive data |
| Test/Staging Systems | CONDITIONAL | If connected to production networks |
| Contractor Systems | YES | If processing company data |
| Cloud Infrastructure | YES | All hybrid cloud components |
| IoT/Embedded Devices | CONDITIONAL | If network-connected |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure process monitoring tools<br>• Set appropriate time limits for system processes<br>• Monitor supervision alerts and respond to violations |
| Security Operations Center | • Monitor process execution alerts<br>• Investigate supervision violations<br>• Escalate critical process anomalies |
| Application Owners | • Define normal execution parameters for applications<br>• Document legitimate long-running processes<br>• Maintain process supervision configurations |

## 4. RULES
[RULE-01] All system processes MUST have defined maximum execution time limits based on normal operational parameters.
[VALIDATION] IF process_time_limit = "undefined" OR process_time_limit = NULL THEN violation

[RULE-02] Processes SHALL NOT execute without supervision for longer than their defined maximum time period.
[VALIDATION] IF process_execution_time > defined_max_time AND supervision_active = FALSE THEN violation

[RULE-03] Automated supervision mechanisms MUST be implemented including timers, automated responses, or manual oversight procedures.
[VALIDATION] IF supervision_mechanism = "none" OR supervision_mechanism = NULL THEN critical_violation

[RULE-04] Process supervision violations MUST trigger automated alerts within 5 minutes of detection.
[VALIDATION] IF violation_detected = TRUE AND alert_time > 5_minutes THEN violation

[RULE-05] Long-running processes that legitimately exceed normal time limits MUST have documented exceptions with approved supervision procedures.
[VALIDATION] IF process_execution_time > normal_limit AND exception_documented = FALSE THEN violation

[RULE-06] Process supervision configurations MUST be reviewed and updated quarterly or when system changes occur.
[VALIDATION] IF last_review_date > 90_days AND system_changes = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Process Time Limit Definition - Establish maximum execution times for all system processes
- [PROC-02] Supervision Mechanism Configuration - Implement and maintain automated monitoring tools
- [PROC-03] Exception Management - Document and approve legitimate long-running processes
- [PROC-04] Incident Response - Respond to process supervision violations and anomalies
- [PROC-05] Quarterly Review - Regular assessment of time limits and supervision effectiveness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Quarterly
- Triggering events: Security incidents involving runaway processes, system architecture changes, new application deployments, supervision tool updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Runaway Batch Process]
IF process_type = "batch_job"
AND execution_time > 4_hours
AND normal_execution_time < 2_hours
AND supervision_alert = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Legitimate Long-Running Process]
IF process_execution_time > defined_limit
AND exception_documented = TRUE
AND exception_approved = TRUE
AND supervision_active = TRUE
THEN compliance = TRUE

[SCENARIO-03: Missing Process Supervision]
IF system_has_processes = TRUE
AND supervision_mechanism = "none"
AND process_monitoring = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Delayed Alert Response]
IF process_violation_detected = TRUE
AND alert_generated = TRUE
AND alert_delay > 5_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Outdated Time Limits]
IF process_time_limits_defined = TRUE
AND last_review_date > 90_days
AND no_system_changes = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Processes prohibited from executing without supervision beyond maximum time | RULE-01, RULE-02 |
| Maximum time period defined for unsupervised process execution | RULE-01, RULE-05 |
| Supervision mechanisms implemented (timers, automated responses, manual oversight) | RULE-03, RULE-04 |
| Process anomaly detection and response capabilities | RULE-04, PROC-04 |