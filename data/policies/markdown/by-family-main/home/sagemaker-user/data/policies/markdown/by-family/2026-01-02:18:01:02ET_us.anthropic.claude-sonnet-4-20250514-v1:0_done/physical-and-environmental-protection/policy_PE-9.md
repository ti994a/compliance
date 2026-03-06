# POLICY: PE-9: Power Equipment and Cabling

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-9 |
| NIST Control | PE-9: Power Equipment and Cabling |
| Version | 1.0 |
| Owner | Facilities Manager |
| Keywords | power equipment, power cabling, physical protection, UPS, generators, data center |

## 1. POLICY STATEMENT
The organization SHALL protect all power equipment and power cabling supporting information systems from physical damage and destruction. Protection measures MUST address both internal and external power infrastructure across all organizational facilities and operational environments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary and backup facilities |
| Office Buildings | YES | All locations with IT equipment |
| External Power Infrastructure | YES | Generators, transformers, external cabling |
| Remote/Satellite Facilities | YES | Self-contained deployable systems |
| Third-party Colocation | CONDITIONAL | Where organization controls power equipment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Implement physical protection controls for power equipment<br>• Coordinate with utilities on external power protection<br>• Maintain power equipment protection documentation |
| Data Center Operations | • Monitor power equipment status and environmental conditions<br>• Execute emergency power procedures<br>• Report power equipment incidents |
| Security Operations | • Assess threats to power infrastructure<br>• Investigate power-related security incidents<br>• Coordinate with law enforcement on power sabotage |

## 4. RULES
[RULE-01] All power equipment supporting critical information systems MUST be housed in physically secured enclosures with restricted access controls.
[VALIDATION] IF power_equipment_criticality = "high" AND physical_enclosure = FALSE THEN violation

[RULE-02] Power cabling for information systems MUST be protected through conduits, cable trays, or underground installation to prevent accidental damage and unauthorized access.
[VALIDATION] IF power_cable_protection = "exposed" AND cable_criticality >= "moderate" THEN violation

[RULE-03] Backup power systems (UPS, generators) MUST be tested monthly and maintained according to manufacturer specifications with documented results.
[VALIDATION] IF backup_power_test_interval > 30_days OR maintenance_current = FALSE THEN violation

[RULE-04] External power equipment MUST be protected by physical barriers, surveillance, and environmental controls appropriate to the threat environment.
[VALIDATION] IF external_power_equipment = TRUE AND (physical_barriers = FALSE OR surveillance = FALSE) THEN violation

[RULE-05] Power equipment protection measures MUST be documented in facility security plans and reviewed annually.
[VALIDATION] IF power_protection_documentation = FALSE OR last_review > 365_days THEN violation

[RULE-06] Power-related incidents that could impact system availability MUST be reported to the Security Operations Center within 2 hours.
[VALIDATION] IF power_incident_impact >= "moderate" AND reporting_time > 2_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Power Equipment Physical Security Assessment - Annual evaluation of protection measures
- [PROC-02] Power Infrastructure Incident Response - Response procedures for power-related emergencies
- [PROC-03] Backup Power System Testing - Monthly testing and maintenance procedures
- [PROC-04] Power Cabling Installation Standards - Requirements for new power cable installations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Power incidents, facility changes, new threat intelligence, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Exposed Critical Power Cabling]
IF power_cable_criticality = "critical"
AND cable_protection_type = "exposed"
AND facility_location = "data_center"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Untested Backup Power System]
IF backup_power_system = TRUE
AND last_test_date > 30_days_ago
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unsecured External Generator]
IF power_equipment_type = "generator"
AND equipment_location = "external"
AND physical_barriers = FALSE
AND surveillance_coverage = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Delayed Power Incident Reporting]
IF incident_type = "power_outage"
AND system_impact = "moderate"
AND reporting_delay = "4_hours"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Protected Internal UPS System]
IF power_equipment_type = "UPS"
AND physical_enclosure = TRUE
AND access_controls = "restricted"
AND maintenance_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Power equipment protected from damage and destruction | [RULE-01], [RULE-03], [RULE-04] |
| Power cabling protected from damage and destruction | [RULE-02], [RULE-04] |