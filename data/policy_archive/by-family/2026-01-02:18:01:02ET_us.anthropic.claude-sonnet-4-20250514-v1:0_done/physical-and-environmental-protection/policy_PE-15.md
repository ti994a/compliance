# POLICY: PE-15: Water Damage Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-15 |
| NIST Control | PE-15: Water Damage Protection |
| Version | 1.0 |
| Owner | Facilities Manager |
| Keywords | water damage, shutoff valves, isolation valves, data center, physical protection |

## 1. POLICY STATEMENT
The organization SHALL protect information systems from water damage by implementing accessible and functional master shutoff or isolation valves in facilities containing system resources. Key personnel MUST be trained on valve locations and activation procedures to ensure rapid response to water emergencies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary facilities with system concentrations |
| Server Rooms | YES | All rooms housing critical IT infrastructure |
| Network Equipment Rooms | YES | Including telecommunications closets |
| Office Areas | CONDITIONAL | Only if housing critical system components |
| Third-party Colocation | YES | Must verify provider compliance |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Install and maintain water shutoff systems<br>• Conduct quarterly valve inspections<br>• Maintain key personnel contact lists |
| IT Operations Manager | • Identify critical system locations requiring protection<br>• Coordinate with facilities on protection requirements<br>• Ensure 24/7 emergency response capability |
| Security Officer | • Verify compliance during security assessments<br>• Review incident response procedures<br>• Monitor physical security integration |

## 4. RULES
[RULE-01] All facilities containing critical IT systems MUST have accessible master shutoff or isolation valves installed within 50 feet of protected areas.
[VALIDATION] IF facility_contains_critical_systems = TRUE AND valve_distance > 50_feet THEN violation

[RULE-02] Water shutoff valves MUST be tested for proper operation quarterly and results documented.
[VALIDATION] IF last_valve_test > 90_days THEN violation

[RULE-03] At least three key personnel per facility MUST be trained on valve locations and activation procedures with annual recertification.
[VALIDATION] IF trained_personnel_count < 3 OR last_training > 365_days THEN violation

[RULE-04] Valve locations and activation procedures MUST be documented and accessible to emergency responders within 5 minutes.
[VALIDATION] IF documentation_access_time > 5_minutes THEN violation

[RULE-05] Emergency contact information for trained personnel MUST be available 24/7 with maximum 30-minute response time.
[VALIDATION] IF emergency_response_time > 30_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Water Valve Installation Standards - Specifications for valve placement and accessibility requirements
- [PROC-02] Quarterly Valve Testing Protocol - Systematic testing and documentation procedures
- [PROC-03] Personnel Training Program - Training curriculum and certification requirements
- [PROC-04] Emergency Response Procedures - Step-by-step water emergency response protocols
- [PROC-05] Documentation Management - Maintenance of valve maps and contact lists

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after any water incident
- Triggering events: Water damage incidents, facility modifications, personnel changes, failed valve tests

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Center Setup]
IF facility_type = "data_center"
AND critical_systems_present = TRUE
AND water_shutoff_valves = "not_installed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Quarterly Testing Missed]
IF last_valve_test > 90_days
AND facility_contains_systems = TRUE
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Insufficient Trained Personnel]
IF trained_personnel_count < 3
AND facility_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Emergency Response Delay]
IF water_emergency = TRUE
AND response_time > 30_minutes
AND no_documented_justification = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Third-party Facility]
IF facility_type = "colocation"
AND provider_compliance_verified = FALSE
AND systems_hosted = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Master shutoff or isolation valves provided | RULE-01 |
| Valves are accessible | RULE-01, RULE-04 |
| Valves are working properly | RULE-02 |
| Valves are known to key personnel | RULE-03, RULE-05 |