# POLICY: PE-11.2: Alternate Power Supply — Self-contained

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-11.2 |
| NIST Control | PE-11.2: Alternate Power Supply — Self-contained |
| Version | 1.0 |
| Owner | Facilities Manager |
| Keywords | alternate power, self-contained, generator, extended outage, manual activation |

## 1. POLICY STATEMENT
The organization SHALL provide self-contained alternate power supplies for critical information systems that can be manually activated and maintain minimum operational capability during extended primary power loss. These alternate power supplies MUST be independent of external power generation and capable of supporting essential system functions without reliance on utility power or third-party power sources.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All facilities housing critical systems |
| Server Rooms | YES | Supporting business-critical applications |
| Network Operations Centers | YES | Required for continuous operations |
| Office Buildings | CONDITIONAL | Only if housing critical infrastructure |
| Remote Facilities | CONDITIONAL | Based on criticality assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Procure and maintain alternate power supplies<br>• Ensure adequate fuel supplies<br>• Coordinate testing and maintenance schedules |
| System Administrator | • Identify minimum operational requirements<br>• Configure systems for graceful power transitions<br>• Validate system functionality during power events |
| Security Officer | • Assess criticality of systems requiring alternate power<br>• Review and approve alternate power configurations<br>• Monitor compliance with power supply requirements |

## 4. RULES
[RULE-01] Critical information systems MUST have self-contained alternate power supplies that do not rely on external power generation sources.
[VALIDATION] IF system_criticality = "high" AND alternate_power_source = "external_grid" THEN violation

[RULE-02] Alternate power supplies MUST be activated manually and SHALL NOT depend on automatic utility power restoration.
[VALIDATION] IF activation_method = "automatic_utility_dependent" THEN violation

[RULE-03] Self-contained power supplies MUST maintain minimally required operational capability for at least 72 hours during extended primary power loss.
[VALIDATION] IF power_duration_capability < 72_hours AND system_criticality = "high" THEN violation

[RULE-04] Alternate power supply fuel reserves MUST be maintained at minimum 80% capacity at all times.
[VALIDATION] IF fuel_level < 80_percent THEN violation

[RULE-05] Alternate power supplies MUST be tested monthly under load conditions to verify operational capability.
[VALIDATION] IF last_load_test > 30_days THEN violation

[RULE-06] Generator capacity MUST meet or exceed 110% of the calculated minimum operational power requirements for supported systems.
[VALIDATION] IF generator_capacity < (minimum_power_requirements * 1.10) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Alternate Power Activation - Manual procedures for activating backup power during outages
- [PROC-02] Monthly Load Testing - Comprehensive testing of generators under operational conditions
- [PROC-03] Fuel Management - Monitoring, ordering, and maintaining adequate fuel supplies
- [PROC-04] Power Requirements Assessment - Annual review of minimum operational power needs
- [PROC-05] Emergency Power Transition - Procedures for switching systems to alternate power

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Extended power outages, system additions, facility changes, generator failures

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical System Without Self-Contained Power]
IF system_criticality = "high"
AND alternate_power_type = "utility_backup"
AND self_contained = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Insufficient Generator Runtime]
IF alternate_power_source = "generator"
AND fuel_capacity_hours < 72
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Automatic Utility-Dependent Activation]
IF activation_method = "automatic"
AND utility_dependency = TRUE
AND manual_override = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Overdue Load Testing]
IF last_load_test_date > 30_days
AND alternate_power_installed = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Adequate Self-Contained System]
IF alternate_power_type = "self_contained_generator"
AND fuel_capacity_hours >= 72
AND activation_method = "manual"
AND last_load_test_date <= 30_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Alternate power supply activated manually | [RULE-02] |
| Alternate power supply is self-contained | [RULE-01] |
| Not reliant on external power generation | [RULE-01] |
| Capable of maintaining minimum operational capability during extended loss | [RULE-03], [RULE-06] |