# POLICY: SI-4.5: System-generated Alerts

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.5 |
| NIST Control | SI-4.5: System-generated Alerts |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | alerts, compromise indicators, incident response, monitoring, notifications |

## 1. POLICY STATEMENT
The organization SHALL establish automated alert mechanisms to notify designated personnel when system-generated indicators of compromise or potential compromise occur. All compromise indicators must be clearly defined and alert notifications must reach appropriate personnel within specified timeframes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All production and development systems |
| Security Monitoring Tools | YES | SIEM, IDS/IPS, firewalls, endpoint protection |
| Cloud Infrastructure | YES | Hybrid cloud environments including AWS, Azure |
| Network Devices | YES | Routers, switches, gateways, boundary protection |
| Mobile Devices | CONDITIONAL | If accessing corporate resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center | • Monitor alert systems 24/7<br>• Validate and triage system-generated alerts<br>• Escalate confirmed incidents per procedures |
| System Administrators | • Configure alert thresholds and rules<br>• Maintain alert notification lists<br>• Test alert delivery mechanisms monthly |
| Incident Response Team | • Respond to compromise alerts within SLA<br>• Document alert response actions<br>• Update compromise indicators based on threats |

## 4. RULES
[RULE-01] All information systems MUST generate automated alerts when predefined compromise indicators are detected.
[VALIDATION] IF system_has_monitoring = TRUE AND compromise_indicator_detected = TRUE AND alert_generated = FALSE THEN violation

[RULE-02] Compromise indicators MUST be formally defined, documented, and reviewed quarterly.
[VALIDATION] IF compromise_indicators_defined = FALSE OR last_review_date > 90_days THEN violation

[RULE-03] Alert notification lists MUST include designated personnel from security operations, system administration, and incident response teams.
[VALIDATION] IF alert_list_includes_security = FALSE OR alert_list_includes_sysadmin = FALSE THEN violation

[RULE-04] System-generated alerts for critical compromise indicators MUST reach designated personnel within 15 minutes of detection.
[VALIDATION] IF alert_severity = "critical" AND notification_time > 15_minutes THEN violation

[RULE-05] Alert delivery mechanisms MUST support multiple communication methods including email, SMS, and console notifications.
[VALIDATION] IF delivery_methods < 2 THEN violation

[RULE-06] Alert notification lists MUST be updated within 5 business days of personnel changes.
[VALIDATION] IF personnel_change_date < current_date AND notification_list_updated = FALSE AND days_elapsed > 5 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Compromise Indicator Definition - Process for identifying and documenting system compromise indicators
- [PROC-02] Alert Configuration Management - Procedures for configuring and maintaining alert rules and thresholds
- [PROC-03] Alert Notification Management - Process for maintaining and updating alert recipient lists
- [PROC-04] Alert Response - Standardized response procedures for different alert types and severities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, infrastructure changes, personnel changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Alert Configuration]
IF system_in_production = TRUE
AND monitoring_enabled = FALSE
AND system_processes_sensitive_data = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delayed Critical Alert]
IF compromise_indicator_severity = "critical"
AND detection_time = "14:30:00"
AND first_notification_time = "14:50:00"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated Notification List]
IF employee_terminated = TRUE
AND termination_date = "2024-01-15"
AND alert_list_removal_date = NULL
AND current_date = "2024-01-25"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Proper Alert Response]
IF compromise_indicator_detected = TRUE
AND alert_generated = TRUE
AND notification_time <= 15_minutes
AND designated_personnel_notified = TRUE
THEN compliance = TRUE

[SCENARIO-05: Undefined Compromise Indicators]
IF system_has_monitoring = TRUE
AND compromise_indicators_documented = FALSE
AND system_operational_days > 30
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel alerted when compromise indicators occur | [RULE-01], [RULE-04] |
| System-generated compromise indicators defined | [RULE-02] |
| Alert notification mechanisms established | [RULE-03], [RULE-05] |
| Alert delivery timeframes met | [RULE-04] |
| Notification list maintenance | [RULE-06] |