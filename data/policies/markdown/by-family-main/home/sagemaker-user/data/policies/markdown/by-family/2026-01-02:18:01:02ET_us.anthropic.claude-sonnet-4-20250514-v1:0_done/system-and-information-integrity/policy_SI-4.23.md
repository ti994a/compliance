# POLICY: SI-4.23: Host-based Devices

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.23 |
| NIST Control | SI-4.23: Host-based Devices |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | host-based monitoring, endpoint monitoring, system components, servers, workstations, mobile devices |

## 1. POLICY STATEMENT
The organization SHALL implement host-based monitoring mechanisms on designated system components to detect security events and collect security-relevant information. Host-based monitoring SHALL be deployed across servers, workstations, and mobile devices based on risk assessment and system categorization.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Servers (Physical/Virtual) | YES | All production and development servers |
| Workstations/Laptops | YES | All corporate-managed endpoints |
| Mobile Devices | YES | Corporate-owned and BYOD devices with corporate access |
| Network Infrastructure | NO | Covered under network-based monitoring controls |
| IoT Devices | CONDITIONAL | Only devices processing sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve host-based monitoring strategy<br>• Define monitoring requirements<br>• Ensure compliance oversight |
| IT Security Team | • Deploy and configure monitoring agents<br>• Monitor security events and alerts<br>• Maintain monitoring infrastructure |
| System Administrators | • Install monitoring agents on managed systems<br>• Ensure agent health and connectivity<br>• Coordinate with security team on incidents |

## 4. RULES

[RULE-01] Host-based monitoring agents MUST be deployed on all servers processing sensitive data within 30 days of system deployment.
[VALIDATION] IF system_type = "server" AND data_classification IN ["confidential", "restricted"] AND monitoring_agent = FALSE AND deployment_date > 30_days THEN violation

[RULE-02] Host-based monitoring SHALL collect security events including process execution, network connections, file modifications, and user authentication activities.
[VALIDATION] IF monitoring_agent = TRUE AND (process_monitoring = FALSE OR network_monitoring = FALSE OR file_monitoring = FALSE OR auth_monitoring = FALSE) THEN violation

[RULE-03] Monitoring agents MUST NOT be disabled or tampered with by end users or unauthorized personnel.
[VALIDATION] IF agent_status = "disabled" AND authorized_by = FALSE THEN critical_violation

[RULE-04] Host-based monitoring data MUST be retained for a minimum of 90 days for compliance systems and 30 days for standard systems.
[VALIDATION] IF system_compliance_scope = TRUE AND log_retention < 90_days THEN violation
[VALIDATION] IF system_compliance_scope = FALSE AND log_retention < 30_days THEN violation

[RULE-05] Organizations SHALL employ host-based monitoring mechanisms from multiple vendors where feasible to reduce single points of failure.
[VALIDATION] IF critical_systems_count > 100 AND unique_monitoring_vendors < 2 THEN recommendation_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Host-based Monitoring Deployment - Standard process for agent installation and configuration
- [PROC-02] Monitoring Data Analysis - Procedures for reviewing and analyzing collected security data
- [PROC-03] Agent Health Monitoring - Process for ensuring monitoring agents remain operational
- [PROC-04] Incident Response Integration - Procedures for escalating host-based monitoring alerts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving monitored hosts, technology changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unmonitored Production Server]
IF system_type = "server"
AND environment = "production"
AND data_classification = "confidential"
AND host_monitoring_agent = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Monitoring Agent Disabled by User]
IF host_monitoring_agent = "installed"
AND agent_status = "disabled"
AND disabled_by = "end_user"
AND authorization_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Insufficient Log Retention]
IF system_compliance_scope = TRUE
AND log_retention_days = 60
AND retention_policy_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Mobile Device with Corporate Access]
IF device_type = "mobile"
AND corporate_data_access = TRUE
AND host_monitoring_agent = FALSE
AND risk_acceptance_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Multi-Vendor Deployment]
IF critical_systems_count = 150
AND monitoring_vendor_count = 2
AND coverage_percentage >= 95
AND agent_health_status = "operational"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Host-based monitoring mechanisms implemented on designated system components | RULE-01, RULE-02 |
| Monitoring mechanisms collect appropriate security information | RULE-02 |
| Protection of monitoring infrastructure integrity | RULE-03 |
| Adequate retention of monitoring data | RULE-04 |
| Vendor diversity considerations | RULE-05 |