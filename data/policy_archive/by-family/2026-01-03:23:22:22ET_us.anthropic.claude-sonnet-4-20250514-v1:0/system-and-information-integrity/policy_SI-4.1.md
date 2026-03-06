# POLICY: SI-4.1: System-wide Intrusion Detection System

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.1 |
| NIST Control | SI-4.1: System-wide Intrusion Detection System |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | intrusion detection, system-wide monitoring, IDS integration, security tools, network monitoring |

## 1. POLICY STATEMENT
All individual intrusion detection tools deployed across the organization MUST be connected and configured into a unified system-wide intrusion detection system. This integration SHALL enable comprehensive threat detection coverage and facilitate information sharing across organizational security infrastructure.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network IDS/IPS devices | YES | All network-based detection tools |
| Host-based IDS agents | YES | All endpoint detection systems |
| Application security monitoring | YES | Web application firewalls, API gateways |
| Cloud security tools | YES | Cloud-native and hybrid monitoring tools |
| Standalone security appliances | YES | Must integrate or be replaced |
| Legacy systems without integration capability | CONDITIONAL | Requires documented exception and compensating controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) Manager | • Oversee system-wide IDS implementation and operation<br>• Ensure 24/7 monitoring coverage<br>• Manage alert correlation and response procedures |
| Network Security Engineers | • Configure IDS tool integration and data flows<br>• Maintain system-wide detection rule consistency<br>• Troubleshoot connectivity and performance issues |
| System Administrators | • Deploy and maintain individual IDS components<br>• Ensure proper configuration and log forwarding<br>• Coordinate with security team on system changes |

## 4. RULES
[RULE-01] All individual intrusion detection tools MUST be connected to the centralized system-wide intrusion detection system within 30 days of deployment.
[VALIDATION] IF ids_tool_deployed = TRUE AND connection_to_central_system = FALSE AND days_since_deployment > 30 THEN violation

[RULE-02] Individual IDS tools SHALL be configured to forward all security events and alerts to the system-wide platform in real-time with maximum delay of 5 minutes.
[VALIDATION] IF event_forwarding_delay > 5_minutes AND system_operational = TRUE THEN violation

[RULE-03] The system-wide IDS MUST maintain centralized logging and correlation capabilities for all connected individual detection tools.
[VALIDATION] IF central_logging_enabled = FALSE OR correlation_engine_active = FALSE THEN critical_violation

[RULE-04] Configuration changes to individual IDS tools MUST be synchronized with the system-wide detection system within 24 hours.
[VALIDATION] IF config_change_timestamp > 24_hours_ago AND system_wide_sync = FALSE THEN violation

[RULE-05] System-wide IDS coverage MUST include all network segments, critical systems, and data flows identified in the system security plan.
[VALIDATION] IF coverage_percentage < 100% AND documented_exception = FALSE THEN violation

[RULE-06] Individual IDS tools that cannot integrate with the system-wide platform MUST have documented compensating controls approved by the CISO.
[VALIDATION] IF integration_capable = FALSE AND compensating_controls_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] IDS Integration Process - Standard procedure for connecting new detection tools to system-wide platform
- [PROC-02] Alert Correlation and Response - Process for handling system-wide security events and coordinated response
- [PROC-03] Configuration Management - Procedure for maintaining consistent detection rules across integrated tools
- [PROC-04] Performance Monitoring - Process for monitoring system-wide IDS performance and availability

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major infrastructure changes, new IDS tool deployments, security incidents involving detection gaps

## 7. SCENARIO PATTERNS
[SCENARIO-01: New IDS Tool Deployment]
IF new_ids_tool_deployed = TRUE
AND connection_to_system_wide_ids = FALSE
AND days_since_deployment > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Legacy System Exception]
IF ids_tool_integration_capable = FALSE
AND compensating_controls_documented = TRUE
AND ciso_approval = TRUE
THEN compliance = TRUE

[SCENARIO-03: Event Forwarding Delay]
IF event_forwarding_enabled = TRUE
AND average_delay > 5_minutes
AND no_documented_outage = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete Coverage]
IF system_wide_coverage < 100%
AND all_critical_systems_covered = FALSE
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Configuration Drift]
IF individual_ids_config_changed = TRUE
AND system_wide_sync_completed = FALSE
AND hours_since_change > 24
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individual intrusion detection tools are connected to a system-wide intrusion detection system | [RULE-01], [RULE-03] |
| Individual intrusion detection tools are configured into a system-wide intrusion detection system | [RULE-02], [RULE-04], [RULE-05] |