# POLICY: PE-6: Monitoring Physical Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-6 |
| NIST Control | PE-6: Monitoring Physical Access |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | physical access, monitoring, surveillance, logs, incident response, facility security |

## 1. POLICY STATEMENT
The organization SHALL monitor physical access to facilities housing information systems through continuous surveillance and systematic log review. All physical access events MUST be logged, regularly reviewed, and coordinated with incident response capabilities to detect and respond to physical security incidents.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All facilities housing production systems |
| Office Buildings | YES | Areas with system components or sensitive data |
| Remote Facilities | YES | Branch offices with IT infrastructure |
| Third-party Colocation | YES | Contracted facility spaces |
| Public Areas | CONDITIONAL | Only publicly accessible areas within organizational facilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facility Security Manager | • Implement physical monitoring systems<br>• Conduct regular log reviews<br>• Coordinate with incident response team |
| Security Operations Center | • Monitor real-time access alerts<br>• Investigate anomalous access patterns<br>• Escalate security incidents |
| Incident Response Team | • Respond to physical security incidents<br>• Conduct investigations<br>• Document incident outcomes |

## 4. RULES

[RULE-01] All facilities housing information systems MUST implement continuous physical access monitoring through guards, video surveillance, or sensor devices.
[VALIDATION] IF facility_houses_systems = TRUE AND monitoring_system = NULL THEN violation

[RULE-02] Physical access logs MUST be reviewed at least weekly and within 24 hours of triggering events.
[VALIDATION] IF last_log_review > 7_days OR (triggering_event_occurred = TRUE AND review_time > 24_hours) THEN violation

[RULE-03] Triggering events requiring immediate log review include after-hours access, repeated failed access attempts, access to restricted areas, and unusual access duration exceeding 4 hours.
[VALIDATION] IF (access_time = "after_hours" OR failed_attempts >= 3 OR area_type = "restricted" OR access_duration > 4_hours) AND immediate_review = FALSE THEN violation

[RULE-04] All physical access monitoring results and investigations MUST be coordinated with the organizational incident response capability within 2 hours of detection.
[VALIDATION] IF security_incident_detected = TRUE AND incident_response_notification_time > 2_hours THEN violation

[RULE-05] Physical access logs MUST be retained for minimum 90 days and protected against unauthorized modification.
[VALIDATION] IF log_retention_period < 90_days OR log_integrity_protection = FALSE THEN violation

[RULE-06] Suspicious physical access activities MUST trigger immediate investigation and incident response procedures.
[VALIDATION] IF suspicious_activity_detected = TRUE AND investigation_initiated = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Access Monitoring Implementation - Deploy and maintain surveillance systems
- [PROC-02] Access Log Review Process - Systematic review of physical access records  
- [PROC-03] Incident Response Coordination - Interface between physical security and cyber incident response
- [PROC-04] Anomaly Detection and Investigation - Identify and investigate suspicious access patterns

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Physical security incidents, facility changes, regulatory updates, technology upgrades

## 7. SCENARIO PATTERNS

[SCENARIO-01: After-Hours Data Center Access]
IF access_time = "after_hours"
AND facility_type = "data_center"
AND log_review_completed = FALSE
AND time_since_access > 24_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Repeated Failed Access Attempts]
IF failed_access_attempts >= 3
AND investigation_initiated = TRUE
AND incident_response_notified = TRUE
AND notification_time <= 2_hours
THEN compliance = TRUE

[SCENARIO-03: Missing Surveillance System]
IF facility_houses_production_systems = TRUE
AND surveillance_system_active = FALSE
AND alternative_monitoring = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Log Review Compliance]
IF last_weekly_review <= 7_days
AND triggering_events_reviewed = TRUE
AND review_documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-05: Incident Response Coordination Gap]
IF physical_security_incident = TRUE
AND incident_response_team_notified = FALSE
AND detection_time > 2_hours_ago
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitor physical access to detect incidents | [RULE-01] |
| Review physical access logs at defined frequency | [RULE-02] |
| Review logs upon occurrence of triggering events | [RULE-03] |
| Coordinate review results with incident response | [RULE-04] |
| Coordinate investigation results with incident response | [RULE-04] |