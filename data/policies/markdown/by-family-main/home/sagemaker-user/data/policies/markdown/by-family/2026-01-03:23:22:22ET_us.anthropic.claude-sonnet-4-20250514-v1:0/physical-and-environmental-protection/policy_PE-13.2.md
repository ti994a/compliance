# POLICY: PE-13.2: Fire Suppression Systems — Automatic Activation and Notification

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-13.2 |
| NIST Control | PE-13.2: Fire Suppression Systems — Automatic Activation and Notification |
| Version | 1.0 |
| Owner | Facilities Security Manager |
| Keywords | fire suppression, automatic activation, notification, emergency response, facility protection |

## 1. POLICY STATEMENT
All facilities containing information systems SHALL employ automatic fire suppression systems that activate without human intervention and immediately notify designated personnel and emergency responders. Facilities operating without continuous staffing MUST have automatic fire suppression capabilities that function independently of human presence.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and backup facilities |
| Server Rooms | YES | Including closets with critical equipment |
| Network Operations Centers | YES | 24/7 and unstaffed facilities |
| Office Buildings | CONDITIONAL | Only areas housing critical IT infrastructure |
| Cloud Provider Facilities | YES | Must validate provider compliance |
| Temporary Facilities | CONDITIONAL | If housing systems >30 days |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Implement and maintain fire suppression systems<br>• Ensure automatic activation capabilities<br>• Maintain notification contact lists |
| IT Operations Manager | • Coordinate with facilities on system protection<br>• Validate suppression system compatibility<br>• Test notification procedures |
| Emergency Response Coordinator | • Maintain emergency responder contact information<br>• Coordinate response procedures<br>• Ensure 24/7 notification capability |

## 4. RULES
[RULE-01] All facilities containing information systems MUST employ fire suppression systems with automatic activation capability.
[VALIDATION] IF facility_contains_IT_systems = TRUE AND automatic_fire_suppression = FALSE THEN critical_violation

[RULE-02] Fire suppression systems MUST automatically notify designated personnel within 2 minutes of activation.
[VALIDATION] IF fire_suppression_activated = TRUE AND notification_time > 2_minutes THEN violation

[RULE-03] Fire suppression systems MUST automatically notify emergency responders within 1 minute of activation.
[VALIDATION] IF fire_suppression_activated = TRUE AND emergency_notification_time > 1_minute THEN critical_violation

[RULE-04] Facilities not staffed continuously (>8 hours unattended) MUST have automatic fire suppression that operates independently.
[VALIDATION] IF facility_staffing = "non_continuous" AND independent_suppression = FALSE THEN critical_violation

[RULE-05] Notification systems MUST have independent power sources separate from primary facility power.
[VALIDATION] IF notification_system_power = "facility_dependent" THEN violation

[RULE-06] Fire suppression systems MUST be tested quarterly for automatic activation and notification functions.
[VALIDATION] IF last_suppression_test > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Fire Suppression System Installation - Standards for automatic suppression system deployment
- [PROC-02] Emergency Notification Management - Maintaining current contact lists and notification methods
- [PROC-03] Suppression System Testing - Quarterly testing of activation and notification functions
- [PROC-04] Personnel Authorization Verification - Ensuring notified personnel have appropriate facility access

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Fire incidents, facility modifications, system failures, personnel changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Data Center Fire Event]
IF facility_type = "data_center"
AND fire_detected = TRUE
AND suppression_activation = "manual_only"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Unstaffed Facility Protection]
IF facility_staffing_hours < 16
AND automatic_suppression = FALSE
AND IT_systems_present = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Notification System Failure]
IF fire_suppression_activated = TRUE
AND personnel_notified = FALSE
AND notification_system_operational = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Emergency Responder Notification Delay]
IF fire_suppression_activated = TRUE
AND emergency_notification_time = 5_minutes
AND facility_classification = "restricted_access"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Power-Dependent Notification]
IF fire_event = TRUE
AND facility_power = "offline"
AND notification_sent = FALSE
AND independent_power_source = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Fire suppression systems that activate automatically are employed | [RULE-01] |
| Fire suppression systems notify personnel automatically | [RULE-02] |
| Fire suppression systems notify emergency responders automatically | [RULE-03] |
| Automatic fire suppression capability when facility not continuously staffed | [RULE-04] |
| Independent power sources for notification systems | [RULE-05] |
| Regular testing of suppression and notification systems | [RULE-06] |