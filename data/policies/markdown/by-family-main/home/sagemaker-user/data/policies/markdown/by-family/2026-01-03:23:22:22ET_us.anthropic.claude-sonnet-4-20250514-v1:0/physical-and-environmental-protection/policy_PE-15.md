# POLICY: PE-15: Water Damage Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-15 |
| NIST Control | PE-15: Water Damage Protection |
| Version | 1.0 |
| Owner | Facilities Manager |
| Keywords | water damage, shutoff valves, isolation valves, data centers, physical protection |

## 1. POLICY STATEMENT
The organization SHALL protect information systems from water damage by implementing accessible master shutoff or isolation valves that are properly maintained and known to designated personnel. This protection applies to all facilities containing critical system resources including data centers, server rooms, and mainframe computer rooms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary focus for water damage protection |
| Server Rooms | YES | Includes all rooms with critical IT infrastructure |
| Mainframe Computer Rooms | YES | Legacy and current mainframe facilities |
| Office Areas | CONDITIONAL | Only if containing critical system concentrations |
| Remote Facilities | YES | If housing production systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Ensure valve installation and maintenance<br>• Maintain personnel authorization lists<br>• Coordinate valve testing and documentation |
| Data Center Operations | • Know valve locations and procedures<br>• Execute emergency water shutoff procedures<br>• Report valve malfunctions immediately |
| Security Operations | • Integrate water protection into incident response<br>• Monitor environmental protection systems<br>• Maintain emergency contact procedures |

## 4. RULES
[RULE-01] All facilities containing critical information systems MUST have accessible master shutoff or isolation valves installed to prevent water damage.
[VALIDATION] IF facility_contains_critical_systems = TRUE AND (master_shutoff_valve = FALSE AND isolation_valve = FALSE) THEN critical_violation

[RULE-02] Master shutoff and isolation valves MUST be tested for proper operation at least quarterly.
[VALIDATION] IF valve_test_date + 90_days < current_date THEN violation

[RULE-03] Valve locations and activation procedures MUST be known to at least two designated key personnel per facility.
[VALIDATION] IF trained_personnel_count < 2 THEN violation

[RULE-04] Valve accessibility MUST be maintained with clear pathways and no obstructions within 3 feet of valve locations.
[VALIDATION] IF valve_accessibility = "obstructed" OR pathway_clear = FALSE THEN violation

[RULE-05] Documentation of valve locations, procedures, and key personnel MUST be updated within 30 days of any changes.
[VALIDATION] IF documentation_last_updated + 30_days < change_date THEN violation

[RULE-06] Key personnel MUST receive training on valve operation procedures within 30 days of designation and annually thereafter.
[VALIDATION] IF personnel_training_date + 365_days < current_date THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Valve Installation Standards - Specifications for master shutoff and isolation valve placement
- [PROC-02] Quarterly Valve Testing - Testing procedures and documentation requirements
- [PROC-03] Emergency Water Shutoff - Step-by-step activation procedures for different scenarios
- [PROC-04] Personnel Training Program - Training curriculum and certification requirements
- [PROC-05] Valve Maintenance Schedule - Preventive maintenance and inspection procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Water damage incidents, facility modifications, system relocations, personnel changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Center Setup]
IF facility_type = "data_center"
AND critical_systems_present = TRUE
AND water_shutoff_valve = "not_installed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Valve Obstruction]
IF valve_location = "obstructed"
AND obstruction_duration > 24_hours
AND facility_contains_critical_systems = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Untrained Personnel]
IF key_personnel_count >= 2
AND trained_personnel_count = 0
AND facility_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Valve Testing Overdue]
IF last_valve_test + 120_days < current_date
AND facility_type IN ["data_center", "server_room"]
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Response]
IF water_leak_detected = TRUE
AND valve_accessible = TRUE
AND trained_personnel_available = TRUE
AND response_time <= 15_minutes
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System protected from water damage by valves | RULE-01 |
| Master shutoff/isolation valves are accessible | RULE-04 |
| Valves are working properly | RULE-02 |
| Valves are known to key personnel | RULE-03, RULE-06 |
| Documentation maintenance | RULE-05 |