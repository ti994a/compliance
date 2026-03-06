# POLICY: SI-4.1: System-wide Intrusion Detection System

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.1 |
| NIST Control | SI-4.1: System-wide Intrusion Detection System |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | intrusion detection, system-wide monitoring, IDS integration, threat detection, security monitoring |

## 1. POLICY STATEMENT
All individual intrusion detection tools deployed within the organization's infrastructure MUST be connected and configured into a centralized system-wide intrusion detection system. This integration enables comprehensive threat visibility, coordinated response capabilities, and enhanced detection through shared intelligence across all monitored systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network IDS/IPS devices | YES | All network-based detection tools |
| Host-based IDS agents | YES | All endpoint detection systems |
| Application security monitors | YES | Web application firewalls, database monitors |
| Cloud security tools | YES | AWS GuardDuty, Azure Sentinel, etc. |
| Third-party managed services | CONDITIONAL | Must provide integration capabilities |
| Development/test environments | YES | Critical systems only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) Manager | • Oversee system-wide IDS implementation and operations<br>• Ensure 24/7 monitoring capabilities<br>• Coordinate incident response activities |
| Network Security Engineers | • Configure and maintain IDS tool integrations<br>• Implement correlation rules and alerting<br>• Perform technical assessments of detection coverage |
| System Administrators | • Deploy and maintain individual IDS components<br>• Ensure proper network connectivity for integration<br>• Provide system access for monitoring tools |

## 4. RULES
[RULE-01] All individual intrusion detection tools MUST be connected to the centralized system-wide IDS platform within 30 days of deployment.
[VALIDATION] IF ids_tool_deployed = TRUE AND connection_to_central_system = FALSE AND days_since_deployment > 30 THEN violation

[RULE-02] Individual IDS tools MUST be configured to forward all security events and alerts to the system-wide platform in real-time with maximum delay of 5 minutes.
[VALIDATION] IF event_forwarding_enabled = FALSE OR event_delay > 5_minutes THEN violation

[RULE-03] The system-wide IDS MUST maintain bidirectional communication with individual tools to enable centralized configuration management and rule distribution.
[VALIDATION] IF bidirectional_communication = FALSE OR central_config_capability = FALSE THEN violation

[RULE-04] All IDS integrations MUST use encrypted communication channels and mutual authentication between individual tools and the central system.
[VALIDATION] IF communication_encrypted = FALSE OR mutual_auth = FALSE THEN violation

[RULE-05] The system-wide IDS MUST correlate events across all connected individual tools and generate consolidated alerts for coordinated threats.
[VALIDATION] IF cross_correlation_enabled = FALSE OR consolidated_alerting = FALSE THEN violation

[RULE-06] Individual IDS tools that cannot be integrated into the system-wide platform MUST be documented as exceptions with compensating controls approved by the CISO.
[VALIDATION] IF integration_capability = FALSE AND exception_documented = FALSE AND compensating_controls = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] IDS Integration Assessment - Evaluate new detection tools for system-wide integration capabilities
- [PROC-02] Central Platform Onboarding - Standard process for connecting individual IDS tools to central system
- [PROC-03] Event Correlation Configuration - Establish rules for cross-system threat correlation and alerting
- [PROC-04] Integration Health Monitoring - Continuous monitoring of connectivity and data flow between systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New IDS tool deployments, security incidents involving detection gaps, technology refresh cycles

## 7. SCENARIO PATTERNS
[SCENARIO-01: New IDS Tool Deployment]
IF new_ids_tool_deployed = TRUE
AND integration_assessment_completed = FALSE
AND days_since_deployment > 7
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Failed Integration Connectivity]
IF ids_tool_connection_status = "FAILED"
AND failure_duration > 4_hours
AND escalation_initiated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Legacy Tool Exception]
IF ids_tool_integration_capable = FALSE
AND ciso_exception_approved = TRUE
AND compensating_controls_implemented = TRUE
AND annual_review_current = TRUE
THEN compliance = TRUE

[SCENARIO-04: Event Forwarding Delay]
IF average_event_delay > 5_minutes
AND performance_issue_documented = FALSE
AND remediation_plan_exists = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unencrypted IDS Communication]
IF ids_communication_method = "plaintext"
AND sensitive_data_transmitted = TRUE
AND network_segment = "production"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individual intrusion detection tools are connected to a system-wide intrusion detection system | [RULE-01], [RULE-02] |
| Individual intrusion detection tools are configured into a system-wide intrusion detection system | [RULE-03], [RULE-05] |
| Secure integration implementation | [RULE-04], [RULE-06] |