# POLICY: SC-48: Sensor Relocation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-48 |
| NIST Control | SC-48: Sensor Relocation |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | sensors, monitoring, relocation, threat response, lateral movement, detection |

## 1. POLICY STATEMENT
The organization SHALL relocate security sensors and monitoring capabilities to alternate positions to counter adversarial lateral movement and maintain effective detection coverage. Sensor relocation SHALL be performed based on threat intelligence, security incidents, or predetermined schedules to prevent adversaries from evading detection systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network monitoring sensors | YES | All IDS/IPS, network taps, flow collectors |
| Host-based monitoring agents | YES | EDR, log collectors, integrity monitors |
| Physical security sensors | YES | Cameras, motion detectors, access sensors |
| Cloud monitoring services | YES | CASB, cloud security posture tools |
| Third-party managed sensors | CONDITIONAL | If organization controls placement |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Manager | • Define sensor relocation criteria and procedures<br>• Approve relocation plans and schedules<br>• Monitor effectiveness of relocated sensors |
| Network Security Engineer | • Execute sensor relocations<br>• Maintain monitoring coverage during transitions<br>• Document new sensor configurations |
| Threat Intelligence Analyst | • Identify relocation triggers based on threat data<br>• Assess adversary tactics requiring sensor adjustments<br>• Recommend optimal sensor placement |

## 4. RULES

[RULE-01] The organization MUST define specific sensors and monitoring capabilities subject to relocation requirements.
[VALIDATION] IF sensor_inventory_defined = FALSE THEN violation

[RULE-02] Target relocation positions MUST be predetermined and documented for each relocatable sensor type.
[VALIDATION] IF sensor_type IN relocatable_sensors AND target_locations_defined = FALSE THEN violation

[RULE-03] Sensor relocation MUST occur within 72 hours when triggered by confirmed lateral movement indicators.
[VALIDATION] IF lateral_movement_detected = TRUE AND relocation_time > 72_hours THEN violation

[RULE-04] Preventive sensor relocation MUST be performed at least quarterly for critical network segments.
[VALIDATION] IF segment_criticality = "high" AND last_relocation > 90_days THEN violation

[RULE-05] Monitoring coverage MUST be maintained during sensor relocation with backup detection capabilities.
[VALIDATION] IF relocation_in_progress = TRUE AND backup_monitoring = FALSE THEN critical_violation

[RULE-06] All sensor relocations MUST be documented with justification, timing, and effectiveness assessment.
[VALIDATION] IF relocation_completed = TRUE AND documentation_complete = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Sensor Inventory and Classification - Catalog all relocatable monitoring capabilities
- [PROC-02] Threat-Based Relocation Triggers - Define conditions requiring immediate sensor movement
- [PROC-03] Relocation Execution Process - Step-by-step sensor movement with coverage continuity
- [PROC-04] Effectiveness Assessment - Post-relocation monitoring and detection validation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, infrastructure changes, threat landscape shifts

## 7. SCENARIO PATTERNS

[SCENARIO-01: Threat-Triggered Relocation]
IF lateral_movement_indicators = TRUE
AND threat_intelligence_confidence = "high"
AND sensor_relocation_completed = TRUE
AND relocation_time <= 72_hours
THEN compliance = TRUE

[SCENARIO-02: Quarterly Preventive Relocation]
IF network_segment = "critical"
AND last_relocation_date > 90_days
AND scheduled_relocation = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Coverage Gap During Relocation]
IF sensor_relocation_in_progress = TRUE
AND backup_monitoring_active = FALSE
AND coverage_gap_duration > 4_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Undocumented Sensor Movement]
IF sensor_location_changed = TRUE
AND relocation_documentation = FALSE
AND change_justification = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Random Relocation Schedule]
IF relocation_trigger = "random"
AND relocation_schedule_defined = TRUE
AND execution_within_window = TRUE
AND monitoring_continuity = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Sensors and monitoring capabilities to be relocated are defined | [RULE-01] |
| Target relocation locations are defined | [RULE-02] |
| Relocation conditions and circumstances are defined | [RULE-03], [RULE-04] |
| Relocation execution maintains security posture | [RULE-05], [RULE-06] |