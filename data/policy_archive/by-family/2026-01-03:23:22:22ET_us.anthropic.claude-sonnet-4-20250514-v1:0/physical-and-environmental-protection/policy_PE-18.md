# POLICY: PE-18: Location of System Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-18 |
| NIST Control | PE-18: Location of System Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system components, physical hazards, environmental hazards, unauthorized access, facility positioning |

## 1. POLICY STATEMENT
System components must be positioned within facilities to minimize potential damage from physical and environmental hazards and reduce opportunities for unauthorized access. Organizations shall maintain documented positioning requirements and conduct regular assessments of component placement effectiveness.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and backup facilities |
| Server Rooms | YES | Including wiring closets and network rooms |
| Critical System Components | YES | Servers, network equipment, storage systems |
| Workstations | CONDITIONAL | Only those processing sensitive data |
| Mobile Computing Devices | NO | Covered under separate mobile device policy |
| Cloud Infrastructure | CONDITIONAL | Only hybrid/private cloud components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Assess physical and environmental hazards<br>• Coordinate system component positioning<br>• Maintain facility security measures |
| IT Operations Manager | • Define system component placement requirements<br>• Coordinate with facilities on optimal positioning<br>• Monitor component security and accessibility |
| Information Security Officer | • Review positioning for security implications<br>• Assess unauthorized access risks<br>• Validate compliance with positioning requirements |

## 4. RULES
[RULE-01] System components MUST be positioned at least 3 feet away from exterior walls and windows to minimize exposure to environmental hazards and unauthorized access attempts.
[VALIDATION] IF component_distance_from_exterior < 3_feet THEN violation

[RULE-02] Critical system components SHALL NOT be located on ground floors or basement levels in areas with flood risk ratings above moderate.
[VALIDATION] IF component_criticality = "high" AND floor_level <= 1 AND flood_risk > "moderate" THEN violation

[RULE-03] System components MUST be positioned away from known electromagnetic interference sources by a minimum distance of 10 feet.
[VALIDATION] IF distance_from_EMI_source < 10_feet THEN violation

[RULE-04] Organizations MUST maintain documented hazard assessments for each facility housing system components, updated annually or when significant changes occur.
[VALIDATION] IF hazard_assessment_age > 365_days OR facility_changes = "significant" AND assessment_updated = FALSE THEN violation

[RULE-05] System components SHALL be positioned to prevent direct line-of-sight access from public areas, parking lots, or unsecured building areas.
[VALIDATION] IF line_of_sight_from_public_area = TRUE THEN violation

[RULE-06] Environmental monitoring equipment MUST be positioned within 15 feet of critical system components to ensure adequate hazard detection.
[VALIDATION] IF distance_to_environmental_monitor > 15_feet AND component_criticality = "high" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Facility Hazard Assessment - Annual evaluation of physical and environmental risks
- [PROC-02] Component Positioning Review - Quarterly assessment of system component placement
- [PROC-03] New Installation Approval - Security review process for new component installations
- [PROC-04] Environmental Monitoring - Continuous monitoring and alerting for environmental hazards

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Facility modifications, new system installations, environmental incidents, security breaches

## 7. SCENARIO PATTERNS
[SCENARIO-01: Server Room Near Loading Dock]
IF system_components = "critical_servers"
AND proximity_to_loading_dock < 50_feet
AND physical_barriers = "insufficient"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Ground Floor Data Center in Flood Zone]
IF facility_floor = "ground"
AND flood_risk_rating = "high"
AND critical_systems_present = TRUE
AND flood_mitigation_controls = "none"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Network Equipment Visible from Parking]
IF component_type = "network_equipment"
AND window_visibility_from_parking = TRUE
AND visual_barriers = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Proper Component Positioning]
IF distance_from_exterior >= 3_feet
AND flood_risk_mitigation = "adequate"
AND EMI_distance >= 10_feet
AND line_of_sight_blocked = TRUE
THEN compliance = TRUE

[SCENARIO-05: Missing Environmental Monitoring]
IF component_criticality = "high"
AND environmental_monitoring = FALSE
AND hazard_detection_capability = "inadequate"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Minimize damage from physical and environmental hazards | [RULE-01], [RULE-02], [RULE-03], [RULE-06] |
| Minimize opportunity for unauthorized access | [RULE-01], [RULE-05] |
| Document hazard assessments | [RULE-04] |
| Position components appropriately within facility | [RULE-01], [RULE-02], [RULE-03], [RULE-05] |