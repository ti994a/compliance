# POLICY: PE-6(1): Intrusion Alarms and Surveillance Equipment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-6-1 |
| NIST Control | PE-6(1): Intrusion Alarms and Surveillance Equipment |
| Version | 1.0 |
| Owner | Chief Physical Security Officer |
| Keywords | physical access, intrusion alarms, surveillance equipment, monitoring, facility security |

## 1. POLICY STATEMENT
The organization SHALL monitor physical access to facilities housing information systems using physical intrusion alarms and surveillance equipment. All monitoring systems MUST be operational, properly maintained, and integrated with incident response procedures to detect and respond to unauthorized physical access attempts.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary and backup facilities |
| Server Rooms | YES | All rooms containing production systems |
| Network Closets | YES | Containing critical network infrastructure |
| Executive Offices | CONDITIONAL | If housing classified systems |
| General Office Space | NO | Unless containing restricted systems |
| Remote Facilities | YES | If housing company IT systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Physical Security Officer | • Establish physical monitoring requirements<br>• Oversee alarm and surveillance system implementation<br>• Coordinate with incident response teams |
| Facilities Manager | • Maintain physical security equipment<br>• Ensure proper installation and coverage<br>• Coordinate equipment testing and repairs |
| Security Operations Center | • Monitor alarm systems 24/7<br>• Respond to physical security alerts<br>• Maintain monitoring logs and records |

## 4. RULES
[RULE-01] All facilities housing information systems MUST be equipped with physical intrusion alarm systems that detect unauthorized entry attempts.
[VALIDATION] IF facility_houses_systems = TRUE AND intrusion_alarms_installed = FALSE THEN violation

[RULE-02] Surveillance equipment MUST provide visual monitoring coverage of all physical access points to facilities containing information systems.
[VALIDATION] IF access_point_monitored = FALSE AND system_criticality >= "Moderate" THEN violation

[RULE-03] Intrusion alarms MUST be monitored continuously by security personnel or automated monitoring systems.
[VALIDATION] IF alarm_monitoring = "unmanned" AND monitoring_hours < 24 THEN violation

[RULE-04] Surveillance equipment MUST record and retain footage for a minimum of 90 days for compliance facilities and 30 days for standard facilities.
[VALIDATION] IF facility_type = "compliance" AND retention_days < 90 THEN violation
[VALIDATION] IF facility_type = "standard" AND retention_days < 30 THEN violation

[RULE-05] Physical intrusion alarms MUST be tested monthly and surveillance equipment MUST be tested quarterly to ensure proper operation.
[VALIDATION] IF last_alarm_test > 30_days THEN violation
[VALIDATION] IF last_surveillance_test > 90_days THEN violation

[RULE-06] All physical security alerts MUST trigger incident response procedures within 15 minutes of detection.
[VALIDATION] IF alert_response_time > 15_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Security Monitoring - Continuous monitoring of intrusion alarms and surveillance systems
- [PROC-02] Equipment Testing and Maintenance - Regular testing and maintenance of security equipment
- [PROC-03] Incident Response for Physical Breaches - Response procedures for physical security alerts
- [PROC-04] Access Log Review - Regular review of physical access monitoring records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Physical security incidents, facility changes, system criticality changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Center Without Alarms]
IF facility_type = "data_center"
AND systems_installed = TRUE
AND intrusion_alarms_installed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Surveillance Gap at Access Point]
IF access_point_exists = TRUE
AND system_criticality = "High"
AND surveillance_coverage = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Alert Response]
IF physical_alarm_triggered = TRUE
AND response_time = 20_minutes
AND facility_contains_systems = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Overdue Equipment Testing]
IF last_alarm_test = 45_days_ago
AND facility_operational = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Insufficient Video Retention]
IF facility_type = "compliance"
AND video_retention_period = 60_days
AND regulatory_requirement = "FedRAMP"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical access monitored using intrusion alarms | [RULE-01], [RULE-03] |
| Physical access monitored using surveillance equipment | [RULE-02], [RULE-04] |
| Continuous monitoring capability | [RULE-03], [RULE-06] |
| Equipment maintenance and testing | [RULE-05] |
| Incident response integration | [RULE-06] |