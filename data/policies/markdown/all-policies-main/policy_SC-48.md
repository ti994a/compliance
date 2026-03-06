# POLICY: SC-48: Sensor Relocation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-48 |
| NIST Control | SC-48: Sensor Relocation |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | sensors, monitoring, relocation, lateral movement, threat response, detection |

## 1. POLICY STATEMENT
The organization SHALL maintain the capability to relocate security sensors and monitoring capabilities to alternate locations to counter adversary lateral movement and evasion tactics. Sensor relocation MUST be performed based on threat intelligence, security incidents, or predetermined schedules to maintain detection coverage effectiveness.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network security sensors | YES | IDS/IPS, network monitoring tools |
| Host-based monitoring agents | YES | EDR, HIDS, log collectors |
| Cloud monitoring services | YES | CASB, cloud security tools |
| Physical security sensors | CONDITIONAL | Only if integrated with cyber monitoring |
| Third-party monitoring tools | YES | Managed security services |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) Manager | • Define sensor relocation criteria and procedures<br>• Approve relocation decisions<br>• Maintain sensor inventory and coverage maps |
| Network Security Engineers | • Execute sensor relocations<br>• Validate post-relocation functionality<br>• Document configuration changes |
| Threat Intelligence Team | • Provide threat-based relocation recommendations<br>• Analyze adversary tactics for coverage gaps<br>• Monitor effectiveness of relocated sensors |

## 4. RULES
[RULE-01] The organization MUST maintain an inventory of all relocatable sensors and monitoring capabilities with their current locations and coverage areas.
[VALIDATION] IF sensor_inventory_exists = FALSE OR last_updated > 30_days THEN violation

[RULE-02] Sensor relocation criteria MUST be defined and include threat intelligence indicators, incident response triggers, and scheduled rotation requirements.
[VALIDATION] IF relocation_criteria_documented = FALSE OR criteria_count < 3 THEN violation

[RULE-03] Critical sensors MUST be relocated within 4 hours of identifying adversary evasion attempts or lateral movement indicators.
[VALIDATION] IF threat_detected = TRUE AND sensor_relocation_time > 4_hours THEN critical_violation

[RULE-04] Relocated sensors MUST maintain equivalent or improved detection coverage compared to previous locations.
[VALIDATION] IF post_relocation_coverage < pre_relocation_coverage THEN violation

[RULE-05] Sensor relocations MUST be documented with justification, timeline, and validation of functionality within 24 hours of completion.
[VALIDATION] IF relocation_completed = TRUE AND documentation_time > 24_hours THEN violation

[RULE-06] At least 20% of monitoring capabilities MUST be relocated quarterly as part of proactive defense measures.
[VALIDATION] IF quarterly_relocations < (total_sensors * 0.20) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Sensor Inventory Management - Maintain current inventory of all relocatable monitoring capabilities
- [PROC-02] Threat-Based Relocation - Execute relocations based on threat intelligence and incident indicators
- [PROC-03] Scheduled Sensor Rotation - Perform proactive relocations to prevent adversary adaptation
- [PROC-04] Coverage Gap Analysis - Assess and validate monitoring coverage before and after relocations
- [PROC-05] Relocation Documentation - Record all sensor movements with justification and validation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving sensor evasion, threat landscape changes, infrastructure modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Threat-Triggered Relocation]
IF lateral_movement_detected = TRUE
AND current_sensors_bypassed = TRUE
AND relocation_time > 4_hours
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Scheduled Rotation Compliance]
IF quarter_end = TRUE
AND sensors_relocated < (total_sensors * 0.20)
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Coverage Degradation]
IF sensor_relocated = TRUE
AND new_coverage_area < original_coverage_area
AND coverage_gap_not_mitigated = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Documentation Failure]
IF sensor_relocation_completed = TRUE
AND days_since_completion > 1
AND relocation_documented = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Inventory Management]
IF sensor_inventory_last_updated > 30_days
OR relocatable_sensors_not_identified = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Sensors and monitoring capabilities to be relocated are defined | [RULE-01] |
| Locations for sensor relocation are defined | [RULE-02], [RULE-04] |
| Conditions for relocating sensors are defined | [RULE-02], [RULE-03] |
| Relocation procedures are implemented | [RULE-03], [RULE-05], [RULE-06] |