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
The organization SHALL implement capabilities to dynamically isolate and segregate system components from other system components when security threats or questionable activities are detected. This capability reduces attack surface and limits damage from successful security incidents.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All production systems with sensitive data |
| Development Systems | YES | Systems containing production-like data |
| Test Systems | CONDITIONAL | Only if containing sensitive data |
| Network Infrastructure | YES | Routers, switches, firewalls |
| Cloud Workloads | YES | All cloud-based system components |
| IoT Devices | YES | Connected operational technology |
| Personal Devices | NO | Covered under separate BYOD policy |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center | • Monitor for isolation triggers<br>• Execute dynamic isolation procedures<br>• Coordinate incident response activities |
| Network Administrators | • Implement isolation mechanisms<br>• Maintain isolation capability infrastructure<br>• Test isolation procedures quarterly |
| System Owners | • Define components requiring isolation capability<br>• Approve isolation criteria and procedures<br>• Document business impact of isolation |

## 4. RULES
[RULE-01] All critical systems and high-value assets MUST have dynamic isolation capabilities implemented and tested quarterly.
[VALIDATION] IF system_criticality = "critical" OR asset_value = "high" AND isolation_capability = FALSE THEN violation

[RULE-02] Dynamic isolation MUST be triggered automatically when predefined security thresholds are exceeded or manually within 15 minutes of threat detection.
[VALIDATION] IF threat_detected = TRUE AND isolation_time > 15_minutes AND manual_trigger = TRUE THEN violation

[RULE-03] Isolated components MUST be segregated using network-level controls that prevent lateral movement while maintaining monitoring capabilities.
[VALIDATION] IF component_isolated = TRUE AND (network_segregation = FALSE OR monitoring_active = FALSE) THEN violation

[RULE-04] System components of questionable origin or trustworthiness MUST be isolated from high-trust components by default.
[VALIDATION] IF component_trust_level = "low" AND isolation_from_high_trust = FALSE THEN violation

[RULE-05] Isolation procedures MUST include predefined criteria for isolation, escalation paths, and restoration processes documented and approved by system owners.
[VALIDATION] IF isolation_procedure_exists = FALSE OR approval_status != "approved" THEN violation

[RULE-06] Dynamic isolation capabilities MUST be tested monthly and during incident response exercises to ensure functionality.
[VALIDATION] IF last_isolation_test > 30_days OR test_result = "failed" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Dynamic Isolation Implementation - Deploy and configure isolation mechanisms for in-scope systems
- [PROC-02] Threat Detection Integration - Configure automated triggers based on security monitoring alerts
- [PROC-03] Manual Isolation Process - Define procedures for security analyst-initiated isolation
- [PROC-04] Component Restoration - Establish criteria and process for returning isolated components to normal operation
- [PROC-05] Isolation Testing - Quarterly testing of isolation mechanisms and procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving lateral movement, new system deployments, architecture changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Malware Detection Isolation]
IF malware_detected = TRUE
AND affected_system = "production"
AND isolation_capability = TRUE
AND isolation_executed <= 15_minutes
THEN compliance = TRUE

[SCENARIO-02: Failed Automatic Isolation]
IF security_threshold_exceeded = TRUE
AND automatic_isolation = "configured"
AND isolation_executed = FALSE
AND manual_override_time > 15_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Untrusted Component Integration]
IF new_component_trust_level = "unknown"
AND integration_environment = "production"
AND isolation_from_critical_systems = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Isolation Testing Compliance]
IF system_criticality = "high"
AND last_isolation_test > 30_days
AND test_documentation = "missing"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Cloud Workload Isolation]
IF cloud_workload = "production"
AND lateral_movement_detected = TRUE
AND network_segmentation_active = TRUE
AND monitoring_maintained = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dynamic isolation capability provided for defined system components | [RULE-01], [RULE-03] |
| Isolation mechanisms reduce attack surface | [RULE-02], [RULE-04] |
| Questionable components isolated from trusted components | [RULE-04] |
| Isolation procedures documented and tested | [RULE-05], [RULE-06] |