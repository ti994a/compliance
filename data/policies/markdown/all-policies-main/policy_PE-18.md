# POLICY: PE-18: Location of System Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-18 |
| NIST Control | PE-18: Location of System Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system components, physical placement, environmental hazards, unauthorized access, facility security |

## 1. POLICY STATEMENT
System components SHALL be positioned within facilities to minimize potential damage from physical and environmental hazards and to minimize opportunities for unauthorized access. Organizations MUST consider both natural disasters and proximity-based security risks when determining component placement.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT system components | YES | Servers, network equipment, storage devices |
| Cloud infrastructure | CONDITIONAL | Hybrid and on-premises components only |
| Mobile devices | NO | Covered under separate mobile device policies |
| Contractor equipment | YES | When located in organizational facilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Assess environmental hazards and facility risks<br>• Implement physical placement requirements<br>• Coordinate with IT on component positioning |
| IT Operations Manager | • Evaluate technical requirements for component placement<br>• Ensure operational accessibility while maintaining security<br>• Document component locations and justifications |
| Information Security Officer | • Define security requirements for component positioning<br>• Assess unauthorized access risks<br>• Review and approve placement decisions |

## 4. RULES
[RULE-01] System components MUST be positioned at least 100 feet from external facility perimeters where feasible to minimize electromagnetic interception risks.
[VALIDATION] IF component_distance_from_perimeter < 100_feet AND justification_documented = FALSE THEN violation

[RULE-02] Critical system components SHALL NOT be located on ground floors or in basement areas prone to flooding unless flood protection measures are implemented.
[VALIDATION] IF component_criticality = "high" AND (floor_level = "ground" OR floor_level = "basement") AND flood_protection = FALSE THEN violation

[RULE-03] System components MUST be positioned away from windows, external walls, and public areas to minimize unauthorized visual or electronic access.
[VALIDATION] IF component_near_window = TRUE OR component_near_external_wall = TRUE THEN requires_additional_controls

[RULE-04] Environmental hazard assessments MUST be conducted annually and whenever system components are relocated.
[VALIDATION] IF last_hazard_assessment > 365_days OR component_relocated = TRUE AND new_assessment_completed = FALSE THEN violation

[RULE-05] System component locations SHALL be documented in facility diagrams with associated risk assessments updated within 30 days of any changes.
[VALIDATION] IF component_location_change_date > 30_days AND documentation_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Environmental Hazard Assessment - Annual evaluation of natural and man-made hazards affecting facility areas
- [PROC-02] Component Placement Review - Security and operational assessment before positioning system components
- [PROC-03] Location Documentation - Maintenance of current facility diagrams and component inventories
- [PROC-04] Risk Exception Process - Formal approval process when optimal placement is not feasible

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Facility changes, major system deployments, security incidents, natural disasters

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Server Placement]
IF component_type = "server"
AND criticality_level = "high"
AND proposed_location = "ground_floor"
AND flood_risk_assessment = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Network Equipment Near Perimeter]
IF component_type = "network_equipment"
AND distance_from_perimeter < 50_feet
AND electromagnetic_shielding = FALSE
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Emergency Relocation]
IF component_relocated = TRUE
AND relocation_reason = "emergency"
AND temporary_placement = TRUE
AND risk_assessment_pending = TRUE
AND days_since_relocation < 30
THEN compliance = TRUE

[SCENARIO-04: Basement Data Center]
IF component_location = "basement"
AND flood_protection_installed = TRUE
AND drainage_systems_functional = TRUE
AND environmental_monitoring = TRUE
THEN compliance = TRUE

[SCENARIO-05: Component Near Public Area]
IF component_visibility_from_public_area = TRUE
AND physical_access_controls = FALSE
AND visual_barriers = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Position components to minimize physical/environmental damage | [RULE-02], [RULE-04] |
| Position components to minimize unauthorized access opportunity | [RULE-01], [RULE-03] |
| Document component locations and risk assessments | [RULE-05] |
| Regular assessment of positioning effectiveness | [RULE-04] |