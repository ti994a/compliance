# POLICY: PE-13.2: Suppression Systems — Automatic Activation and Notification

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-13.2 |
| NIST Control | PE-13.2: Suppression Systems — Automatic Activation and Notification |
| Version | 1.0 |
| Owner | Facilities Security Manager |
| Keywords | fire suppression, automatic activation, notification, emergency response, facility protection |

## 1. POLICY STATEMENT
All facilities housing information systems MUST employ automatic fire suppression systems that activate without human intervention and immediately notify designated personnel and emergency responders. Facilities operating without continuous staffing MUST have enhanced automatic fire suppression capabilities to compensate for the absence of on-site personnel.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and secondary facilities |
| Server Rooms | YES | Including distributed server closets |
| Network Equipment Rooms | YES | MDF/IDF locations with critical infrastructure |
| Office Spaces | CONDITIONAL | Only if housing critical systems |
| Third-party Colocation | YES | Must verify compliance through contracts |
| Temporary Facilities | CONDITIONAL | If housing systems >30 days |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Define notification personnel and emergency responders<br>• Ensure system compliance and testing<br>• Maintain independent power sources for notifications |
| IT Operations Manager | • Coordinate with facilities for system protection<br>• Validate notification receipt procedures<br>• Document staffing schedules for facilities |
| Emergency Response Coordinator | • Maintain current emergency responder contact lists<br>• Ensure proper clearances for facility access<br>• Test notification mechanisms quarterly |

## 4. RULES
[RULE-01] All facilities housing information systems MUST employ fire suppression systems that activate automatically without human intervention.
[VALIDATION] IF facility_houses_info_systems = TRUE AND suppression_system_automatic = FALSE THEN critical_violation

[RULE-02] Fire suppression systems MUST automatically notify designated personnel within 5 minutes of activation.
[VALIDATION] IF suppression_activated = TRUE AND personnel_notification_time > 5_minutes THEN violation

[RULE-03] Fire suppression systems MUST automatically notify emergency responders within 2 minutes of activation.
[VALIDATION] IF suppression_activated = TRUE AND emergency_notification_time > 2_minutes THEN critical_violation

[RULE-04] Facilities not staffed continuously (>8 hours unattended) MUST have enhanced automatic fire suppression capabilities.
[VALIDATION] IF facility_staffing = "non_continuous" AND enhanced_suppression = FALSE THEN violation

[RULE-05] Notification mechanisms MUST have independent energy sources separate from primary facility power.
[VALIDATION] IF notification_system_independent_power = FALSE THEN violation

[RULE-06] Personnel and emergency responders on notification lists MUST have appropriate facility access authorizations.
[VALIDATION] IF notification_recipient_clearance = FALSE AND facility_restricted = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Fire Suppression System Testing - Monthly activation tests and quarterly full system tests
- [PROC-02] Notification List Management - Quarterly review and update of personnel and emergency contacts
- [PROC-03] Emergency Response Coordination - Annual drills with local emergency services
- [PROC-04] Independent Power Source Testing - Monthly backup power tests for notification systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Fire incidents, facility changes, staffing model changes, emergency response failures

## 7. SCENARIO PATTERNS
[SCENARIO-01: Data Center Fire Suppression]
IF facility_type = "data_center"
AND suppression_system_automatic = TRUE
AND personnel_notification_time <= 5_minutes
AND emergency_notification_time <= 2_minutes
THEN compliance = TRUE

[SCENARIO-02: Unstaffed Facility Fire Event]
IF facility_staffing = "non_continuous"
AND suppression_activated = TRUE
AND enhanced_suppression = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Notification System Power Failure]
IF suppression_activated = TRUE
AND primary_power = FALSE
AND notification_system_independent_power = TRUE
AND notifications_sent = TRUE
THEN compliance = TRUE

[SCENARIO-04: Unauthorized Emergency Responder]
IF emergency_responder_notified = TRUE
AND facility_classification = "restricted"
AND responder_clearance = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Delayed Personnel Notification]
IF suppression_activated = TRUE
AND personnel_notification_time = 8_minutes
AND system_malfunction = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Fire suppression systems that activate automatically are employed | RULE-01 |
| Fire suppression systems notify personnel automatically | RULE-02 |
| Fire suppression systems notify emergency responders automatically | RULE-03 |
| Automatic fire suppression capability for unstaffed facilities | RULE-04 |
| Independent energy sources for notifications | RULE-05 |
| Appropriate access authorizations for notification recipients | RULE-06 |