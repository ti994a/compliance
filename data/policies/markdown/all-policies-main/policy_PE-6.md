# POLICY: PE-6: Monitoring Physical Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-6 |
| NIST Control | PE-6: Monitoring Physical Access |
| Version | 1.0 |
| Owner | Chief Physical Security Officer |
| Keywords | physical access, monitoring, surveillance, access logs, incident response, facility security |

## 1. POLICY STATEMENT
The organization SHALL continuously monitor physical access to facilities housing information systems through automated and manual mechanisms. Physical access logs MUST be regularly reviewed to detect anomalous activities and coordinate security incidents with organizational incident response capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary and secondary facilities |
| Server Rooms | YES | All locations with IT infrastructure |
| Network Closets | YES | Including remote/branch locations |
| Office Areas | CONDITIONAL | Areas with sensitive systems only |
| Public Areas | YES | Lobbies, reception areas within facilities |
| Remote Facilities | YES | All company-controlled locations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Deploy and maintain monitoring systems<br>• Conduct regular log reviews<br>• Coordinate with incident response team |
| Facility Operations | • Monitor real-time access events<br>• Respond to physical security alerts<br>• Maintain access control systems |
| Incident Response Team | • Investigate physical security incidents<br>• Document and track incident resolution<br>• Coordinate with law enforcement if required |

## 4. RULES
[RULE-01] Physical access monitoring systems MUST be deployed at all entry points to facilities housing information systems, including cameras, sensors, and automated logging mechanisms.
[VALIDATION] IF facility_houses_IT_systems = TRUE AND monitoring_system_deployed = FALSE THEN violation

[RULE-02] Physical access logs MUST be reviewed at least weekly for routine analysis and within 24 hours of triggered security events.
[VALIDATION] IF routine_review_frequency > 7_days THEN violation
[VALIDATION] IF security_event_triggered = TRUE AND review_time > 24_hours THEN violation

[RULE-03] Monitoring systems SHALL detect and log all physical access attempts including successful entries, failed attempts, tailgating, and forced entry events.
[VALIDATION] IF access_attempt_logged = FALSE THEN violation

[RULE-04] Physical access anomalies MUST be investigated within 4 hours of detection and coordinated with incident response capabilities within 8 hours for confirmed incidents.
[VALIDATION] IF anomaly_detected = TRUE AND investigation_start_time > 4_hours THEN violation
[VALIDATION] IF incident_confirmed = TRUE AND IR_coordination_time > 8_hours THEN violation

[RULE-05] Video surveillance systems MUST provide continuous recording with minimum 90-day retention for critical areas and 30-day retention for general areas.
[VALIDATION] IF area_classification = "critical" AND retention_period < 90_days THEN violation
[VALIDATION] IF area_classification = "general" AND retention_period < 30_days THEN violation

[RULE-06] Physical access monitoring SHALL include detection of suspicious activities such as after-hours access, repeated failed attempts, unusual duration access, and access to unauthorized areas.
[VALIDATION] IF suspicious_activity_detection_enabled = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Access Monitoring Deployment - Installation and configuration of monitoring systems
- [PROC-02] Access Log Review and Analysis - Systematic review process for identifying anomalies
- [PROC-03] Physical Security Incident Response - Investigation and coordination procedures
- [PROC-04] Monitoring System Maintenance - Regular testing and maintenance of surveillance equipment

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Physical security incidents, facility changes, technology updates, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: After-Hours Data Center Access]
IF access_time = "outside_business_hours"
AND facility_type = "data_center"
AND user_authorization_verified = FALSE
AND supervisor_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Failed Tailgating Detection]
IF multiple_persons_detected = TRUE
AND single_badge_used = TRUE
AND tailgating_alert_generated = FALSE
AND monitoring_system_functional = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Incident Coordination]
IF physical_security_incident = TRUE
AND incident_confirmed_time = 2_hours
AND IR_team_notification_time = 10_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Insufficient Log Retention]
IF area_classification = "critical"
AND video_retention_period = 60_days
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Unmonitored Server Room]
IF location_contains_servers = TRUE
AND physical_monitoring_deployed = FALSE
AND facility_access_controlled = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitor physical access to detect incidents | [RULE-01], [RULE-03] |
| Review physical access logs at defined frequency | [RULE-02] |
| Review logs upon occurrence of defined events | [RULE-02], [RULE-04] |
| Coordinate review results with incident response | [RULE-04] |
| Coordinate investigation results with incident response | [RULE-04] |