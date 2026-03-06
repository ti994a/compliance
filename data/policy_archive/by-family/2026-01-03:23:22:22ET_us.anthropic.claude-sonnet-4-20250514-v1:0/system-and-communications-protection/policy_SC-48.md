```markdown
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
The organization shall maintain the capability to dynamically relocate security sensors and monitoring capabilities to alternate locations based on threat intelligence, security incidents, or predetermined circumstances. Sensor relocation shall be implemented to disrupt adversary lateral movement and enhance detection coverage across critical system paths.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network security sensors | YES | IDS/IPS, network monitors |
| Host-based monitoring | YES | EDR agents, file integrity monitors |
| Cloud monitoring services | YES | SIEM collectors, API monitors |
| Physical security sensors | CONDITIONAL | Only IT-related physical monitoring |
| Third-party monitoring tools | YES | When under organizational control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Execute sensor relocation procedures<br>• Monitor relocation effectiveness<br>• Document relocation activities |
| Network Security Team | • Maintain sensor relocation capabilities<br>• Define relocation trigger conditions<br>• Test relocation mechanisms |
| Threat Intelligence Team | • Provide threat-based relocation recommendations<br>• Analyze adversary movement patterns<br>• Update relocation criteria |

## 4. RULES
[RULE-01] The organization MUST maintain a documented inventory of relocatable sensors and monitoring capabilities with defined alternate deployment locations.
[VALIDATION] IF sensor_inventory_exists = FALSE OR alternate_locations_defined = FALSE THEN violation

[RULE-02] Sensor relocation capabilities MUST be tested quarterly to ensure operational readiness.
[VALIDATION] IF last_relocation_test > 90_days THEN violation

[RULE-03] Threat-based sensor relocation MUST be initiated within 4 hours of receiving credible threat intelligence indicating compromised monitoring coverage.
[VALIDATION] IF threat_intelligence_received = TRUE AND relocation_time > 4_hours THEN violation

[RULE-04] Random sensor relocation MUST occur at intervals not exceeding 30 days for critical system monitoring points.
[VALIDATION] IF sensor_criticality = "high" AND last_random_relocation > 30_days THEN violation

[RULE-05] All sensor relocations MUST be logged with timestamp, trigger condition, source location, and destination location.
[VALIDATION] IF relocation_occurred = TRUE AND (timestamp = NULL OR trigger = NULL OR source = NULL OR destination = NULL) THEN violation

[RULE-06] Relocated sensors MUST achieve operational status within 2 hours of relocation initiation.
[VALIDATION] IF relocation_initiated = TRUE AND operational_time > 2_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Sensor Relocation Planning - Define relocation triggers, locations, and procedures
- [PROC-02] Threat-Based Relocation - Execute relocations based on threat intelligence
- [PROC-03] Random Relocation Schedule - Implement unpredictable relocation patterns
- [PROC-04] Relocation Testing - Quarterly validation of relocation capabilities
- [PROC-05] Impact Assessment - Evaluate relocation effectiveness and coverage gaps

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, infrastructure changes, new threat intelligence, failed relocation tests

## 7. SCENARIO PATTERNS
[SCENARIO-01: Threat-Driven Relocation]
IF threat_intelligence = "lateral_movement_detected"
AND current_sensor_coverage = "compromised_path"
AND relocation_capability = "available"
THEN compliance = TRUE (if relocated within 4 hours)
violation_severity = "High" (if not relocated)

[SCENARIO-02: Quarterly Testing Failure]
IF last_relocation_test > 90_days
AND test_scheduled = TRUE
AND test_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Critical Sensor Static Deployment]
IF sensor_criticality = "high"
AND last_random_relocation > 30_days
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete Relocation Logging]
IF sensor_relocated = TRUE
AND (log_timestamp = NULL OR trigger_reason = NULL)
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Extended Relocation Downtime]
IF relocation_initiated = TRUE
AND sensor_operational_time > 2_hours
AND no_technical_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Sensors and monitoring capabilities relocated are defined | RULE-01 |
| Relocation locations are defined | RULE-01 |
| Relocation conditions and circumstances are defined | RULE-03, RULE-04 |
| Relocation capability is maintained | RULE-02, RULE-06 |
| Relocation activities are documented | RULE-05 |
```