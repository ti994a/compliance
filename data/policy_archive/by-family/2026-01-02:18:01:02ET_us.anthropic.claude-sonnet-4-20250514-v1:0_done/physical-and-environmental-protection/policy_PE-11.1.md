# POLICY: PE-11.1: Alternate Power Supply — Minimal Operational Capability

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-11.1 |
| NIST Control | PE-11.1: Alternate Power Supply — Minimal Operational Capability |
| Version | 1.0 |
| Owner | Facilities Security Manager |
| Keywords | alternate power, backup power, manual activation, operational capability, power outage, emergency power |

## 1. POLICY STATEMENT
The organization SHALL provide manually-activated alternate power supplies for all information systems to maintain minimal operational capability during extended primary power outages. These alternate power sources MUST be capable of sustaining critical system functions for the duration required by business continuity requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and secondary facilities |
| Server Rooms | YES | Supporting critical systems |
| Network Equipment Rooms | YES | Core infrastructure components |
| Desktop Systems | NO | Unless designated as critical |
| Cloud Infrastructure | CONDITIONAL | Customer-managed facilities only |
| Remote Offices | CONDITIONAL | Based on criticality assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Oversee alternate power supply implementation<br>• Ensure compliance with policy requirements<br>• Coordinate testing and maintenance activities |
| Data Center Operations | • Perform manual activation procedures<br>• Monitor power systems during outages<br>• Execute emergency power protocols |
| System Administrators | • Define minimal operational capability requirements<br>• Validate system functionality during power events<br>• Document critical system dependencies |

## 4. RULES
[RULE-01] All information systems classified as HIGH or MODERATE impact SHALL have manually-activated alternate power supplies installed and operational.
[VALIDATION] IF system_impact_level IN ["HIGH", "MODERATE"] AND alternate_power_supply = FALSE THEN violation

[RULE-02] Alternate power supplies MUST be capable of maintaining minimal operational capability for at least 4 hours for HIGH impact systems and 2 hours for MODERATE impact systems.
[VALIDATION] IF system_impact_level = "HIGH" AND power_duration < 4_hours THEN violation
[VALIDATION] IF system_impact_level = "MODERATE" AND power_duration < 2_hours THEN violation

[RULE-03] Manual activation procedures for alternate power supplies MUST be documented and accessible to authorized personnel within 15 minutes of power loss detection.
[VALIDATION] IF power_loss_detected = TRUE AND activation_time > 15_minutes THEN violation

[RULE-04] Alternate power supplies SHALL be tested monthly to verify manual activation capability and operational duration requirements.
[VALIDATION] IF last_test_date > 30_days AND test_status != "PASSED" THEN violation

[RULE-05] Minimal operational capability requirements MUST be defined and documented for each system with alternate power supply protection.
[VALIDATION] IF alternate_power_required = TRUE AND minimal_capability_defined = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Alternate Power Supply Installation - Standards for UPS, generator, and secondary power source deployment
- [PROC-02] Manual Activation Protocol - Step-by-step procedures for emergency power activation
- [PROC-03] Monthly Power Testing - Systematic testing of alternate power systems and duration validation
- [PROC-04] Minimal Capability Assessment - Process for defining and validating minimal operational requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Extended power outages, system criticality changes, facility modifications, failed power tests

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical System Without Alternate Power]
IF system_impact_level = "HIGH"
AND alternate_power_supply = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Insufficient Power Duration Capacity]
IF alternate_power_supply = TRUE
AND system_impact_level = "MODERATE"
AND power_duration_capacity = 1_hour
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Failed Monthly Power Test]
IF alternate_power_supply = TRUE
AND last_test_result = "FAILED"
AND days_since_test <= 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed Manual Activation]
IF power_outage_event = TRUE
AND manual_activation_time = 20_minutes
AND system_impact_level = "HIGH"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Alternate Power Implementation]
IF system_impact_level = "HIGH"
AND alternate_power_supply = TRUE
AND power_duration_capacity >= 4_hours
AND last_test_result = "PASSED"
AND minimal_capability_defined = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Alternate power supply provided for the system | [RULE-01] |
| Alternate power supply is activated manually | [RULE-03] |
| Can maintain minimally required operational capability | [RULE-02], [RULE-05] |
| Functions during extended loss of primary power source | [RULE-02], [RULE-04] |