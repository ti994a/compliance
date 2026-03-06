# POLICY: SI-4.1: System-wide Intrusion Detection System

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.1 |
| NIST Control | SI-4.1: System-wide Intrusion Detection System |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | intrusion detection, IDS, system monitoring, security tools, threat detection |

## 1. POLICY STATEMENT
All individual intrusion detection tools deployed across the organization MUST be connected and configured into a unified system-wide intrusion detection system. This integration enables comprehensive threat visibility, centralized monitoring, and enhanced detection capabilities across all organizational systems and networks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network IDS/IPS devices | YES | All network-based detection tools |
| Host-based IDS agents | YES | All endpoint detection systems |
| Application security monitoring | YES | WAF, RASP, and app-specific tools |
| Cloud security tools | YES | Cloud-native and hybrid monitoring |
| Legacy standalone tools | YES | Must integrate or be replaced |
| Third-party managed services | CONDITIONAL | If organizationally controlled |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Monitor system-wide IDS dashboard<br>• Investigate alerts and incidents<br>• Maintain detection rule correlation |
| Network Security Team | • Configure IDS tool integration<br>• Ensure data flow between systems<br>• Validate detection coverage |
| System Administrators | • Deploy and maintain IDS agents<br>• Configure local detection tools<br>• Report integration issues |

## 4. RULES
[RULE-01] All intrusion detection tools MUST be connected to the centralized SIEM platform within 30 days of deployment.
[VALIDATION] IF ids_tool_deployed = TRUE AND siem_integration_days > 30 THEN violation

[RULE-02] Individual IDS tools MUST forward alerts and logs to the system-wide platform in real-time with maximum 5-minute delay.
[VALIDATION] IF log_forwarding_delay > 5_minutes THEN violation

[RULE-03] System-wide IDS MUST maintain visibility into at least 95% of network segments and critical systems.
[VALIDATION] IF coverage_percentage < 95 THEN violation

[RULE-04] Cross-correlation rules MUST be configured to share threat intelligence between individual IDS tools.
[VALIDATION] IF correlation_rules_configured = FALSE THEN violation

[RULE-05] Standalone IDS tools operating independently SHALL NOT be permitted beyond 90-day exception period.
[VALIDATION] IF standalone_operation = TRUE AND exception_days > 90 THEN critical_violation

[RULE-06] System-wide IDS configuration changes MUST be documented and approved through change management process.
[VALIDATION] IF config_change = TRUE AND change_approval = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] IDS Integration Procedure - Steps for connecting new detection tools to system-wide platform
- [PROC-02] Alert Correlation Configuration - Process for establishing cross-system detection rules
- [PROC-03] Coverage Assessment - Quarterly validation of detection coverage across all systems
- [PROC-04] Integration Testing - Verification procedures for IDS tool connectivity and data flow

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New IDS deployment, major infrastructure changes, security incidents involving detection gaps

## 7. SCENARIO PATTERNS
[SCENARIO-01: New IDS Tool Deployment]
IF new_ids_tool_deployed = TRUE
AND integration_completed = FALSE
AND deployment_days > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Standalone IDS Operation]
IF ids_tool_status = "standalone"
AND system_wide_connection = FALSE
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Alert Forwarding Failure]
IF ids_generating_alerts = TRUE
AND siem_receiving_alerts = FALSE
AND outage_duration > 1_hour
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Insufficient Coverage]
IF critical_systems_monitored < 100%
AND network_coverage < 95%
AND remediation_plan = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Proper Integration]
IF all_ids_tools_connected = TRUE
AND real_time_forwarding = TRUE
AND correlation_rules_active = TRUE
AND coverage_percentage >= 95%
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individual intrusion detection tools are connected to system-wide IDS | RULE-01, RULE-05 |
| Individual intrusion detection tools are configured into system-wide IDS | RULE-02, RULE-04, RULE-06 |
| System-wide detection coverage is maintained | RULE-03 |
| Integration processes are documented | RULE-06 |