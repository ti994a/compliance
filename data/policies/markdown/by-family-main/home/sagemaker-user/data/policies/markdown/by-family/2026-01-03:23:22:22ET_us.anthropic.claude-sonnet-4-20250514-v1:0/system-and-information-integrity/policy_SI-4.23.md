# POLICY: SI-4.23: Host-based Devices

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.23 |
| NIST Control | SI-4.23: Host-based Devices |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | host-based monitoring, endpoint detection, system monitoring, security monitoring, endpoint security |

## 1. POLICY STATEMENT
The organization SHALL implement host-based monitoring mechanisms on defined system components to detect and respond to security events. All system components requiring host-based monitoring must be clearly identified and configured with appropriate monitoring capabilities from approved vendors.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Servers (physical/virtual) | YES | All production and development servers |
| Workstations/Laptops | YES | All corporate-managed endpoints |
| Mobile devices | YES | Organization-owned and BYOD with corporate access |
| Network infrastructure | NO | Covered under network-based monitoring controls |
| IoT devices | CONDITIONAL | Only if processing corporate data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define host-based monitoring requirements<br>• Approve monitoring tools and vendors<br>• Oversee compliance with monitoring policies |
| IT Security Team | • Implement and configure host-based monitoring<br>• Monitor alerts and respond to incidents<br>• Maintain monitoring tool configurations |
| System Administrators | • Deploy monitoring agents on assigned systems<br>• Ensure monitoring tools remain operational<br>• Report monitoring failures immediately |

## 4. RULES
[RULE-01] All system components identified as requiring host-based monitoring MUST have approved monitoring mechanisms deployed and operational within 7 days of system deployment.
[VALIDATION] IF system_component IN monitoring_required_list AND monitoring_agent_status != "active" AND days_since_deployment > 7 THEN violation

[RULE-02] Host-based monitoring mechanisms MUST be sourced from approved vendors and SHALL NOT be disabled without documented security approval.
[VALIDATION] IF monitoring_tool NOT IN approved_vendor_list THEN violation
[VALIDATION] IF monitoring_agent_status = "disabled" AND security_approval = FALSE THEN critical_violation

[RULE-03] Organizations SHOULD employ host-based monitoring mechanisms from multiple product developers to enhance detection capabilities.
[VALIDATION] IF unique_vendor_count < 2 AND total_monitored_systems > 100 THEN advisory_finding

[RULE-04] Host-based monitoring systems MUST generate alerts for defined security events and forward logs to the central SIEM within 15 minutes.
[VALIDATION] IF alert_generation = FALSE OR log_forwarding_delay > 15_minutes THEN violation

[RULE-05] All host-based monitoring configurations MUST be documented and reviewed quarterly for effectiveness.
[VALIDATION] IF configuration_documentation = FALSE OR last_review_date > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Host-based Monitoring Deployment - Standardized process for deploying monitoring agents
- [PROC-02] Monitoring Tool Evaluation - Assessment criteria for approving new monitoring vendors
- [PROC-03] Alert Response Procedures - Escalation and response workflows for monitoring alerts
- [PROC-04] Monitoring Configuration Management - Change control for monitoring configurations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving monitored systems, new technology deployments, vendor changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Server Deployment]
IF system_type = "server"
AND deployment_date < (current_date - 7_days)
AND host_monitoring_status = "not_deployed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Monitoring Agent Disabled]
IF monitoring_agent_status = "disabled"
AND security_approval_documented = FALSE
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Single Vendor Dependency]
IF total_monitored_endpoints > 100
AND unique_monitoring_vendors = 1
AND risk_assessment_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Mobile Device Monitoring]
IF device_type = "mobile"
AND corporate_data_access = TRUE
AND host_monitoring_deployed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Log Forwarding Delay]
IF monitoring_logs_generated = TRUE
AND siem_delivery_time > 15_minutes
AND network_issues_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Host-based monitoring mechanisms defined and implemented | [RULE-01], [RULE-05] |
| Monitoring deployed on identified system components | [RULE-01], [RULE-04] |
| Multiple vendor consideration for enhanced coverage | [RULE-03] |
| Approved monitoring tools and configurations | [RULE-02], [RULE-05] |