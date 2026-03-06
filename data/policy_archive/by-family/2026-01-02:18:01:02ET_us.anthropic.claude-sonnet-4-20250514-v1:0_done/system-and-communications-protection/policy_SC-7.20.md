# POLICY: SC-7.20: Dynamic Isolation and Segregation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.20 |
| NIST Control | SC-7.20: Dynamic Isolation and Segregation |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | dynamic isolation, system segregation, component isolation, attack surface reduction, boundary protection |

## 1. POLICY STATEMENT
The organization SHALL implement capabilities to dynamically isolate system components from other system components when security concerns arise. This capability reduces attack surfaces and limits damage from successful attacks by partitioning components of questionable origin from more trustworthy components.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production systems | YES | All systems handling sensitive data |
| Development systems | YES | When connected to production networks |
| Cloud workloads | YES | Including containers and virtual machines |
| Network segments | YES | Critical infrastructure components |
| IoT devices | CONDITIONAL | When integrated with corporate systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center | • Monitor for isolation triggers<br>• Execute dynamic isolation procedures<br>• Maintain isolation capability documentation |
| Network Administrators | • Implement network-level isolation mechanisms<br>• Configure automated isolation tools<br>• Test isolation capabilities quarterly |
| System Administrators | • Deploy host-based isolation controls<br>• Maintain component inventory for isolation<br>• Execute emergency isolation procedures |

## 4. RULES
[RULE-01] Organizations MUST implement automated dynamic isolation capabilities that can segregate system components within 5 minutes of threat detection.
[VALIDATION] IF threat_detected = TRUE AND isolation_time > 5_minutes THEN violation

[RULE-02] All systems handling sensitive data MUST have pre-defined isolation profiles identifying which components can be dynamically isolated.
[VALIDATION] IF system_classification >= "sensitive" AND isolation_profile_exists = FALSE THEN violation

[RULE-03] Dynamic isolation capabilities MUST be tested monthly to ensure proper functionality and response times.
[VALIDATION] IF last_isolation_test > 30_days THEN violation

[RULE-04] Isolated components SHALL NOT communicate with other system components except through approved security gateways or proxies.
[VALIDATION] IF component_isolated = TRUE AND direct_communication = TRUE AND approved_gateway = FALSE THEN critical_violation

[RULE-05] Organizations MUST maintain an inventory of system components capable of dynamic isolation, updated within 72 hours of changes.
[VALIDATION] IF component_change_date > (current_date - 72_hours) AND inventory_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Dynamic Isolation Response - Automated and manual procedures for isolating compromised components
- [PROC-02] Isolation Testing Protocol - Monthly testing of isolation mechanisms and response times
- [PROC-03] Component Classification - Process for identifying and categorizing isolatable system components
- [PROC-04] Isolation Recovery - Procedures for safely reintegrating isolated components

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents requiring isolation, technology architecture changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Malware Detection Isolation]
IF malware_detected = TRUE
AND affected_component_identified = TRUE
AND isolation_capability_available = TRUE
THEN isolation_required = TRUE
violation_severity = "Critical" if not executed within 5 minutes

[SCENARIO-02: Suspicious Network Activity]
IF anomalous_network_traffic = TRUE
AND traffic_source_identified = TRUE
AND isolation_profile_exists = TRUE
THEN dynamic_isolation = REQUIRED
violation_severity = "High" if manual intervention required

[SCENARIO-03: Untrusted Component Integration]
IF new_component_deployed = TRUE
AND trust_level = "questionable"
AND isolation_capability = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Cloud Workload Compromise]
IF cloud_workload_compromised = TRUE
AND lateral_movement_detected = TRUE
AND isolation_executed > 5_minutes
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: IoT Device Anomaly]
IF iot_device_behavior = "anomalous"
AND corporate_network_connected = TRUE
AND isolation_not_available = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dynamic isolation capability provided | RULE-01, RULE-02 |
| System components defined for isolation | RULE-02, RULE-05 |
| Isolation mechanisms tested and functional | RULE-03 |
| Isolated components properly segregated | RULE-04 |