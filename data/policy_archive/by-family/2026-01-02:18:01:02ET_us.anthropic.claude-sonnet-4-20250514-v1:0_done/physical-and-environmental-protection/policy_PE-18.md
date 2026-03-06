# POLICY: PE-18: Location of System Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-18 |
| NIST Control | PE-18: Location of System Components |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | system components, physical hazards, environmental hazards, unauthorized access, facility positioning |

## 1. POLICY STATEMENT
System components must be positioned within facilities to minimize potential damage from physical and environmental hazards and reduce opportunities for unauthorized access. Organizations shall maintain documented positioning requirements and conduct regular assessments of component placement.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and secondary facilities |
| Server Rooms | YES | Including closets and distributed locations |
| Network Equipment | YES | Switches, routers, wireless access points |
| Critical Workstations | YES | Admin stations, privileged access workstations |
| Mobile Devices | CONDITIONAL | When used for critical operations |
| Cloud Infrastructure | CONDITIONAL | When organization controls physical placement |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Assess physical and environmental hazards<br>• Implement component positioning requirements<br>• Coordinate with security team on placement decisions |
| IT Security Manager | • Define security positioning requirements<br>• Assess unauthorized access risks<br>• Review and approve component placement plans |
| Data Center Operations | • Execute positioning procedures<br>• Monitor environmental conditions<br>• Report positioning violations |

## 4. RULES
[RULE-01] System components MUST be positioned at least 100 feet from external walls in high-risk facilities and 50 feet in standard facilities.
[VALIDATION] IF facility_risk_level = "high" AND distance_to_external_wall < 100_feet THEN violation
[VALIDATION] IF facility_risk_level = "standard" AND distance_to_external_wall < 50_feet THEN violation

[RULE-02] Critical system components SHALL NOT be placed in basement levels or ground floors of facilities in flood-prone areas.
[VALIDATION] IF flood_risk = "high" AND component_criticality = "critical" AND floor_level <= 1 THEN violation

[RULE-03] System components MUST be positioned away from public areas, with minimum 25-foot separation from lobbies, cafeterias, and visitor areas.
[VALIDATION] IF distance_to_public_area < 25_feet THEN violation

[RULE-04] Network equipment SHALL be positioned to minimize electromagnetic interference, maintaining 6-foot minimum separation from power distribution units and electrical panels.
[VALIDATION] IF component_type = "network_equipment" AND distance_to_electrical_source < 6_feet THEN violation

[RULE-05] Component positioning assessments MUST be conducted annually and within 30 days of any facility modifications.
[VALIDATION] IF last_assessment_date > 365_days OR (facility_modification = TRUE AND assessment_delay > 30_days) THEN violation

[RULE-06] Positioning documentation MUST be maintained for all critical and high-value system components, updated within 48 hours of any relocation.
[VALIDATION] IF component_criticality >= "high" AND positioning_documentation = "missing" THEN violation
[VALIDATION] IF component_moved = TRUE AND documentation_update_delay > 48_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Positioning Assessment - Annual evaluation of physical placement against hazard and security criteria
- [PROC-02] Hazard Impact Analysis - Assessment of potential damage from identified physical and environmental threats
- [PROC-03] Positioning Documentation Management - Maintenance of current component location and justification records
- [PROC-04] Emergency Relocation - Procedures for rapid component movement during threat events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Facility changes, new threat identification, security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Data Center Near External Wall]
IF component_type = "server"
AND component_criticality = "critical"
AND distance_to_external_wall < 50_feet
AND facility_risk_level = "standard"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Network Equipment EMI Exposure]
IF component_type = "network_switch"
AND distance_to_electrical_panel = 4_feet
AND electromagnetic_shielding = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-03: Flood Risk Basement Placement]
IF component_criticality = "critical"
AND floor_level = 0
AND flood_risk_zone = "high"
AND flood_mitigation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Public Area Proximity]
IF distance_to_visitor_area = 15_feet
AND component_contains_sensitive_data = TRUE
AND physical_barriers = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Positioning]
IF distance_to_external_wall >= 50_feet
AND distance_to_public_area >= 25_feet
AND electromagnetic_interference_risk = "low"
AND positioning_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Position components to minimize physical/environmental damage | [RULE-01], [RULE-02], [RULE-04] |
| Minimize unauthorized access opportunities | [RULE-03] |
| Maintain positioning documentation | [RULE-06] |
| Regular positioning assessments | [RULE-05] |