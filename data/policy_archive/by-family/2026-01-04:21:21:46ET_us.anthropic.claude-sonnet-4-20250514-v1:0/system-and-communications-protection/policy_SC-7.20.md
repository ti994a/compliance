```markdown
# POLICY: SC-7.20: Dynamic Isolation and Segregation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.20 |
| NIST Control | SC-7.20: Dynamic Isolation and Segregation |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | dynamic isolation, network segregation, component isolation, threat containment, attack surface reduction |

## 1. POLICY STATEMENT
The organization SHALL implement capabilities to dynamically isolate system components from other system components when threats are detected or components are deemed untrustworthy. This capability reduces attack surfaces and limits damage from successful security incidents.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All critical and high-value systems |
| Development Systems | YES | When processing production data |
| Network Infrastructure | YES | Routers, switches, security appliances |
| Cloud Workloads | YES | Virtual machines, containers, serverless |
| IoT/OT Devices | CONDITIONAL | If connected to corporate networks |
| Guest Networks | NO | Already isolated by design |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center | • Monitor for isolation triggers<br>• Execute dynamic isolation procedures<br>• Document isolation events |
| Network Engineering | • Implement isolation capabilities<br>• Maintain isolation infrastructure<br>• Test isolation mechanisms |
| System Administrators | • Configure component isolation settings<br>• Validate isolation effectiveness<br>• Coordinate with SOC during events |

## 4. RULES
[RULE-01] All production systems MUST have dynamic isolation capabilities implemented and tested within 90 days of deployment.
[VALIDATION] IF system_type = "production" AND isolation_capability = FALSE AND deployment_date < (current_date - 90_days) THEN violation

[RULE-02] Dynamic isolation MUST be triggered automatically within 5 minutes when malicious activity is detected by security monitoring tools.
[VALIDATION] IF threat_detected = TRUE AND isolation_trigger_time > 5_minutes THEN violation

[RULE-03] Isolated components MUST remain segregated until security analysis confirms the threat is remediated and formal approval is granted for reconnection.
[VALIDATION] IF component_status = "isolated" AND reconnection_approval = FALSE AND reconnection_attempted = TRUE THEN critical_violation

[RULE-04] The organization MUST maintain an inventory of all components with dynamic isolation capabilities, updated monthly.
[VALIDATION] IF isolation_inventory_last_updated > 30_days THEN violation

[RULE-05] Dynamic isolation mechanisms MUST be tested quarterly to ensure functionality and effectiveness.
[VALIDATION] IF last_isolation_test > 90_days THEN violation

[RULE-06] All dynamic isolation events MUST be logged with timestamp, trigger reason, affected components, and duration.
[VALIDATION] IF isolation_event_occurred = TRUE AND (log_timestamp = NULL OR trigger_reason = NULL) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Dynamic Isolation Implementation - Deploy and configure isolation capabilities for new systems
- [PROC-02] Threat-Based Isolation Response - Execute isolation when threats are detected
- [PROC-03] Component Reconnection Process - Validate and approve return of isolated components
- [PROC-04] Isolation Testing Protocol - Quarterly validation of isolation mechanisms

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, infrastructure changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Malware Detection Isolation]
IF malware_detected = TRUE
AND affected_system = "production"
AND isolation_time > 5_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Untested Isolation Capability]
IF system_deployment_date < (current_date - 90_days)
AND isolation_capability_tested = FALSE
AND system_classification = "critical"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unauthorized Reconnection]
IF component_isolation_status = "active"
AND reconnection_approval = "pending"
AND component_network_access = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Isolation Logs]
IF isolation_event_count > 0
AND isolation_logs_complete = FALSE
AND audit_period = "current_quarter"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Quarterly Test Compliance]
IF last_isolation_test_date < (current_date - 90_days)
AND system_type = "production"
AND isolation_capability = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dynamic isolation capability provided | [RULE-01] |
| Isolation mechanisms functional | [RULE-05] |
| Isolation events documented | [RULE-06] |
| Components properly segregated | [RULE-03] |
| Automated threat response | [RULE-02] |
| Isolation inventory maintained | [RULE-04] |
```