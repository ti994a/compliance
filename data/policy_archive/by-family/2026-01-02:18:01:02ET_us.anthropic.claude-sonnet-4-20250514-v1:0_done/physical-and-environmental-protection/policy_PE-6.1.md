# POLICY: PE-6.1: Intrusion Alarms and Surveillance Equipment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-6.1 |
| NIST Control | PE-6.1: Intrusion Alarms and Surveillance Equipment |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | physical security, intrusion alarms, surveillance, monitoring, facility protection |

## 1. POLICY STATEMENT
All facilities housing information systems MUST be protected by physical intrusion alarms and surveillance equipment to monitor unauthorized access attempts. These systems SHALL work in conjunction with physical barriers and access controls to provide comprehensive facility security monitoring.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary and backup facilities |
| Server Rooms | YES | All locations with IT equipment |
| Network Closets | YES | If housing critical infrastructure |
| Office Buildings | CONDITIONAL | Only areas with sensitive systems |
| Remote Facilities | YES | If processing regulated data |
| Vendor Facilities | CONDITIONAL | If housing company systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Install and maintain intrusion alarm systems<br>• Configure surveillance equipment coverage<br>• Monitor alarm notifications 24/7 |
| Physical Security Team | • Respond to intrusion alarms within defined timeframes<br>• Review surveillance footage for incidents<br>• Maintain physical security equipment |
| IT Security Team | • Define security requirements for facilities<br>• Review physical security logs<br>• Coordinate incident response activities |

## 4. RULES
[RULE-01] All facilities housing information systems MUST be equipped with physical intrusion alarm systems that detect unauthorized access attempts.
[VALIDATION] IF facility_houses_systems = TRUE AND intrusion_alarms_installed = FALSE THEN violation

[RULE-02] Surveillance equipment MUST provide video monitoring coverage of all physical access points and critical areas within facilities.
[VALIDATION] IF access_point_monitored = FALSE OR critical_area_coverage < 100% THEN violation

[RULE-03] Intrusion alarms MUST trigger immediate notifications to security personnel and generate automated alerts within 30 seconds of activation.
[VALIDATION] IF alarm_triggered = TRUE AND notification_time > 30_seconds THEN violation

[RULE-04] Security personnel MUST respond to intrusion alarms within 15 minutes for critical facilities and 30 minutes for standard facilities.
[VALIDATION] IF facility_criticality = "critical" AND response_time > 15_minutes THEN critical_violation
[VALIDATION] IF facility_criticality = "standard" AND response_time > 30_minutes THEN violation

[RULE-05] Surveillance systems MUST retain video recordings for a minimum of 90 days and ensure 99% uptime availability.
[VALIDATION] IF video_retention_days < 90 OR system_uptime < 99% THEN violation

[RULE-06] All intrusion detection sensors MUST be tested monthly and surveillance equipment MUST undergo quarterly functionality testing.
[VALIDATION] IF sensor_test_interval > 30_days OR camera_test_interval > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Intrusion Alarm Installation and Configuration - Standardized deployment of alarm systems
- [PROC-02] Surveillance Equipment Monitoring and Maintenance - Regular inspection and testing protocols  
- [PROC-03] Alarm Response and Incident Investigation - Security team response procedures
- [PROC-04] Video Recording Management and Retention - Storage and disposal of surveillance data

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility changes, technology upgrades, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Facility Assessment]
IF new_facility = TRUE
AND houses_information_systems = TRUE
AND intrusion_alarms_installed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Surveillance Coverage Gap]
IF critical_access_point = TRUE
AND video_coverage = FALSE
AND risk_assessment_completed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Alarm Response]
IF intrusion_alarm_triggered = TRUE
AND facility_type = "data_center"
AND security_response_time > 15_minutes
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Equipment Maintenance Overdue]
IF surveillance_equipment_installed = TRUE
AND last_functionality_test > 90_days
AND no_maintenance_waiver = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Video Retention Compliance]
IF incident_investigation_required = TRUE
AND video_age > 90_days
AND video_available = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical access monitoring using intrusion alarms | [RULE-01], [RULE-03] |
| Physical access monitoring using surveillance equipment | [RULE-02], [RULE-05] |
| Alarm system functionality and response | [RULE-04], [RULE-06] |
| Equipment maintenance and testing | [RULE-06] |