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
All system processes MUST operate within defined maximum execution time limits and SHALL NOT execute without supervision beyond established thresholds. The organization SHALL implement automated supervision mechanisms and manual oversight procedures to detect and respond to processes exceeding normal execution periods.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All critical and high-impact systems |
| Development Systems | YES | Systems processing sensitive data |
| Test Systems | CONDITIONAL | Only if containing production data |
| Batch Processing Jobs | YES | All automated batch operations |
| User Interactive Processes | CONDITIONAL | Only long-running operations |
| Third-party Applications | YES | All applications on organization systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Define maximum execution time limits for system processes<br>• Configure automated supervision mechanisms<br>• Monitor process execution alerts |
| Security Operations Center | • Monitor process execution violations<br>• Investigate process anomalies<br>• Escalate critical supervision failures |
| Application Owners | • Define normal execution periods for applications<br>• Document process supervision requirements<br>• Respond to application-specific violations |

## 4. RULES
[RULE-01] All system processes MUST have defined maximum execution time limits based on normal operational requirements plus a reasonable buffer period.
[VALIDATION] IF process_max_time = undefined OR process_max_time = null THEN violation

[RULE-02] Processes SHALL NOT execute without supervision for more than their defined maximum time limit.
[VALIDATION] IF process_execution_time > defined_max_time AND supervision_active = FALSE THEN violation

[RULE-03] Automated supervision mechanisms MUST be implemented for all processes with execution times exceeding 30 minutes.
[VALIDATION] IF normal_execution_time > 30_minutes AND automated_supervision = FALSE THEN violation

[RULE-04] Manual oversight procedures MUST be established for critical processes that cannot be automatically supervised.
[VALIDATION] IF automated_supervision = FALSE AND manual_oversight_documented = FALSE THEN violation

[RULE-05] Process supervision violations MUST generate alerts within 5 minutes of detection.
[VALIDATION] IF violation_detected = TRUE AND alert_time > 5_minutes THEN critical_violation

[RULE-06] Processes exceeding maximum time limits MUST be terminated or escalated for manual review within 15 minutes.
[VALIDATION] IF process_execution_time > defined_max_time AND response_time > 15_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Process Time Limit Definition - Establish maximum execution times for all system processes
- [PROC-02] Automated Supervision Configuration - Implement and maintain process monitoring systems
- [PROC-03] Process Anomaly Response - Define response procedures for supervision violations
- [PROC-04] Manual Oversight Implementation - Establish procedures for processes requiring human supervision

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Process supervision failures, new system deployments, significant process changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Batch Job Exceeding Time Limit]
IF process_type = "batch_job"
AND execution_time > defined_max_time
AND automated_termination = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Critical Process Without Supervision]
IF process_criticality = "high"
AND supervision_mechanism = "none"
AND execution_time > 30_minutes
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Automated Response Within Limits]
IF process_execution_time > defined_max_time
AND alert_generated = TRUE
AND response_time <= 15_minutes
THEN compliance = TRUE

[SCENARIO-04: Manual Oversight Process]
IF automated_supervision = FALSE
AND manual_oversight_documented = TRUE
AND oversight_performed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Process Without Defined Limits]
IF process_active = TRUE
AND defined_max_time = undefined
AND process_type != "interactive"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Processes prohibited from executing without supervision beyond maximum time | RULE-02, RULE-06 |
| Maximum time period defined for process execution | RULE-01 |
| Supervision mechanisms implemented | RULE-03, RULE-04 |
| Process anomaly detection and response | RULE-05, RULE-06 |