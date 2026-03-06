```markdown
# POLICY: PE-11.2: Alternate Power Supply — Self-contained

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-11.2 |
| NIST Control | PE-11.2: Alternate Power Supply — Self-contained |
| Version | 1.0 |
| Owner | Facilities Security Manager |
| Keywords | alternate power, backup power, generator, self-contained, manual activation, extended outage |

## 1. POLICY STATEMENT
All critical information systems SHALL have self-contained alternate power supplies that can be manually activated and maintain minimum operational capability during extended primary power outages. These alternate power supplies MUST NOT depend on external power generation sources and SHALL provide sufficient capacity for essential system functions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical Information Systems | YES | Systems supporting essential business functions |
| Data Centers | YES | Primary and backup facilities |
| Network Infrastructure | YES | Core networking equipment only |
| End User Workstations | NO | Unless classified as critical systems |
| Cloud Services | CONDITIONAL | Only customer-managed infrastructure |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Oversee alternate power supply implementation<br>• Ensure compliance with capacity requirements<br>• Coordinate testing and maintenance programs |
| System Owners | • Identify minimum operational capability requirements<br>• Validate power supply adequacy for their systems<br>• Participate in testing activities |
| Facilities Operations Team | • Perform manual activation procedures<br>• Conduct regular maintenance and testing<br>• Monitor fuel levels and supply logistics |

## 4. RULES
[RULE-01] All critical information systems MUST have self-contained alternate power supplies that do not rely on external power generation sources.
[VALIDATION] IF system_criticality = "critical" AND alternate_power_type != "self_contained" THEN violation

[RULE-02] Alternate power supplies MUST be activated manually, not automatically, to ensure controlled power transfer.
[VALIDATION] IF activation_method = "automatic" THEN violation

[RULE-03] Alternate power supplies SHALL maintain minimally required operational capability for a minimum of 72 hours during extended primary power loss.
[VALIDATION] IF runtime_capacity < 72_hours THEN violation

[RULE-04] Alternate power supply capacity MUST be sufficient to support all in-scope systems simultaneously at minimum operational levels.
[VALIDATION] IF total_system_load > alternate_power_capacity THEN violation

[RULE-05] Fuel supplies for generators MUST be maintained at levels sufficient for 72-hour continuous operation plus 25% reserve capacity.
[VALIDATION] IF fuel_level < (72_hour_consumption * 1.25) THEN violation

[RULE-06] Manual activation procedures MUST be documented and tested quarterly with designated personnel.
[VALIDATION] IF last_activation_test > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Manual Power Transfer Procedure - Step-by-step activation of alternate power supplies
- [PROC-02] Fuel Management Procedure - Monitoring, ordering, and maintaining fuel supplies
- [PROC-03] Load Prioritization Procedure - Determining minimum operational capability requirements
- [PROC-04] Testing and Maintenance Procedure - Regular validation of alternate power systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Power outage incidents, system criticality changes, facility modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Extended Power Outage]
IF primary_power_status = "lost"
AND outage_duration > 4_hours
AND alternate_power_activated = TRUE
AND system_operational_capability >= "minimum"
THEN compliance = TRUE

[SCENARIO-02: Insufficient Generator Capacity]
IF alternate_power_type = "generator"
AND generator_capacity < total_critical_system_load
AND minimum_operational_capability = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: External Power Dependency]
IF alternate_power_source = "grid_backup"
AND self_contained = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Automatic Activation System]
IF power_transfer_method = "automatic"
AND manual_override_capability = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Inadequate Fuel Reserves]
IF fuel_supply_hours < 72
AND refuel_capability_during_outage = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Alternate power supply activated manually | [RULE-02] |
| Alternate power supply is self-contained | [RULE-01] |
| Not reliant on external power generation | [RULE-01], [RULE-03] |
| Capable of maintaining minimum operational capability | [RULE-03], [RULE-04] |
```