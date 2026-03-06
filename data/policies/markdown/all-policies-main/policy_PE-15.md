# POLICY: PE-15: Water Damage Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-15 |
| NIST Control | PE-15: Water Damage Protection |
| Version | 1.0 |
| Owner | Facilities Security Manager |
| Keywords | water damage, shutoff valves, isolation valves, data centers, physical protection |

## 1. POLICY STATEMENT
The organization SHALL protect information systems from water damage by implementing accessible master shutoff or isolation valves in facilities containing system resources. Key personnel MUST be trained on valve locations and activation procedures to ensure rapid response to water emergencies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary focus areas |
| Server Rooms | YES | Including distributed locations |
| Mainframe Computer Rooms | YES | Legacy and modern systems |
| Network Equipment Rooms | YES | Critical infrastructure components |
| Office Areas | CONDITIONAL | Only if containing critical systems |
| Remote Facilities | YES | If housing organizational IT assets |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Oversee water damage protection program<br>• Ensure valve maintenance and testing<br>• Maintain key personnel training records |
| Site Facility Managers | • Implement local water protection measures<br>• Conduct regular valve inspections<br>• Coordinate emergency response procedures |
| Key Personnel (Designated) | • Know valve locations and procedures<br>• Respond to water emergencies<br>• Report valve malfunctions immediately |

## 4. RULES
[RULE-01] Master shutoff or isolation valves MUST be installed in all facilities containing concentrations of information system resources.
[VALIDATION] IF facility_contains_systems = TRUE AND valve_installed = FALSE THEN critical_violation

[RULE-02] All water shutoff valves MUST be accessible to authorized personnel within 60 seconds during emergency conditions.
[VALIDATION] IF valve_access_time > 60_seconds OR access_blocked = TRUE THEN violation

[RULE-03] Water shutoff valves MUST be tested for proper operation quarterly and maintenance records SHALL be maintained.
[VALIDATION] IF last_test_date > 90_days OR test_failed = TRUE THEN violation

[RULE-04] At least two key personnel per facility MUST be trained on valve locations and activation procedures.
[VALIDATION] IF trained_personnel_count < 2 OR training_current = FALSE THEN violation

[RULE-05] Valve location documentation MUST be updated within 30 days of any facility modifications affecting water systems.
[VALIDATION] IF facility_modified = TRUE AND documentation_updated = FALSE AND days_since_modification > 30 THEN violation

[RULE-06] Emergency contact information for key personnel MUST be posted near valve locations and updated within 10 days of personnel changes.
[VALIDATION] IF contact_info_current = FALSE OR days_since_update > 10 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Water Valve Installation Standards - Specifications for valve placement and accessibility requirements
- [PROC-02] Quarterly Valve Testing Protocol - Systematic testing and documentation procedures
- [PROC-03] Key Personnel Training Program - Training curriculum and certification requirements
- [PROC-04] Emergency Water Response Plan - Step-by-step activation and notification procedures
- [PROC-05] Valve Maintenance Schedule - Preventive maintenance and replacement protocols

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Water incidents, facility modifications, personnel changes, failed valve tests

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Center Setup]
IF facility_type = "data_center"
AND systems_deployed = TRUE
AND valve_installation = "pending"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Valve Accessibility During Emergency]
IF emergency_declared = TRUE
AND valve_access_time > 60_seconds
AND water_threat_present = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Quarterly Testing Overdue]
IF current_date - last_valve_test > 90_days
AND facility_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Insufficient Trained Personnel]
IF facility_active = TRUE
AND trained_personnel_count < 2
AND key_systems_present = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Outdated Emergency Contacts]
IF personnel_change_date < contact_update_date + 10_days
AND valve_signage_current = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System protected from water damage by valves | RULE-01 |
| Master shutoff/isolation valves are accessible | RULE-02 |
| Valves are working properly | RULE-03 |
| Valves are known to key personnel | RULE-04, RULE-06 |