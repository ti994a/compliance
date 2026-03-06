# POLICY: PE-12: Emergency Lighting

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-12 |
| NIST Control | PE-12: Emergency Lighting |
| Version | 1.0 |
| Owner | Facilities Security Manager |
| Keywords | emergency lighting, power outage, evacuation routes, emergency exits, data centers, contingency |

## 1. POLICY STATEMENT
The organization SHALL employ and maintain automatic emergency lighting systems that activate during power outages or disruptions to ensure safe evacuation from facilities containing critical information systems. Emergency lighting MUST cover all emergency exits and evacuation routes within facilities housing data centers, server rooms, and mainframe computer rooms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary facilities with system concentrations |
| Server Rooms | YES | Facilities containing critical systems |
| Mainframe Computer Rooms | YES | High-value system locations |
| Office Buildings | CONDITIONAL | Only areas with critical system resources |
| Remote Facilities | CONDITIONAL | If housing production systems |
| Temporary Facilities | YES | When used for system operations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Oversee emergency lighting implementation and maintenance<br>• Ensure compliance with evacuation route coverage<br>• Coordinate with contingency planning teams |
| Site Operations Manager | • Conduct regular testing and maintenance<br>• Report lighting failures immediately<br>• Maintain emergency lighting documentation |
| Contingency Planning Team | • Include emergency lighting in contingency plans<br>• Identify alternate processing sites for lighting failures<br>• Coordinate emergency response procedures |

## 4. RULES
[RULE-01] All facilities containing critical information systems MUST have automatic emergency lighting that activates within 10 seconds of power outage or disruption.
[VALIDATION] IF facility_has_critical_systems = TRUE AND emergency_lighting_activation_time > 10_seconds THEN violation

[RULE-02] Emergency lighting MUST provide illumination coverage for 100% of designated emergency exits and evacuation routes within scope facilities.
[VALIDATION] IF emergency_exit_coverage < 100% OR evacuation_route_coverage < 100% THEN critical_violation

[RULE-03] Emergency lighting systems MUST be tested monthly and maintained according to manufacturer specifications and local fire codes.
[VALIDATION] IF last_test_date > 30_days_ago OR maintenance_status = "overdue" THEN violation

[RULE-04] Emergency lighting MUST provide minimum 90 minutes of continuous illumination during power outages.
[VALIDATION] IF battery_duration < 90_minutes OR illumination_test_duration < 90_minutes THEN violation

[RULE-05] Emergency lighting failures MUST be reported within 2 hours of discovery and repaired within 24 hours for critical facilities.
[VALIDATION] IF failure_report_time > 2_hours OR repair_time > 24_hours THEN violation

[RULE-06] Contingency plans MUST document emergency lighting provisions and alternate processing sites for lighting system failures.
[VALIDATION] IF contingency_plan_includes_lighting = FALSE OR alternate_sites_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Emergency Lighting Testing - Monthly functional testing of all emergency lighting systems
- [PROC-02] Emergency Lighting Maintenance - Preventive maintenance and battery replacement procedures
- [PROC-03] Failure Response - Immediate response and repair procedures for lighting failures
- [PROC-04] Coverage Assessment - Annual verification of exit and evacuation route coverage

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Facility modifications, evacuation route changes, lighting system failures, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Data Center Power Outage]
IF facility_type = "data_center"
AND power_status = "outage"
AND emergency_lighting_activated = TRUE
AND activation_time <= 10_seconds
AND coverage_percentage = 100%
THEN compliance = TRUE

[SCENARIO-02: Server Room Lighting Failure]
IF facility_type = "server_room"
AND emergency_lighting_status = "failed"
AND failure_reported = TRUE
AND report_time > 2_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Inadequate Evacuation Route Coverage]
IF emergency_lighting_installed = TRUE
AND evacuation_route_coverage < 100%
AND emergency_exit_coverage < 100%
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Testing Overdue]
IF last_emergency_lighting_test > 30_days_ago
AND facility_has_critical_systems = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Battery Duration Insufficient]
IF emergency_lighting_test_conducted = TRUE
AND battery_duration_test < 90_minutes
AND facility_type IN ["data_center", "server_room", "mainframe_room"]
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Automatic emergency lighting employed for the system | [RULE-01] |
| Automatic emergency lighting maintained for the system | [RULE-03] |
| Emergency lighting covers emergency exits within facility | [RULE-02] |
| Emergency lighting covers evacuation routes within facility | [RULE-02] |