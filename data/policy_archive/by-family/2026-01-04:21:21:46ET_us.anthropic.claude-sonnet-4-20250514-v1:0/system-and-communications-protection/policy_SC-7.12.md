# POLICY: SC-7.12: Host-based Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.12 |
| NIST Control | SC-7.12: Host-based Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | host-based firewall, endpoint protection, boundary protection, workstation security, mobile device security |

## 1. POLICY STATEMENT
All system components including servers, workstations, notebooks, and mobile devices MUST implement host-based boundary protection mechanisms. Host-based firewalls and equivalent protection mechanisms SHALL be deployed, configured, and maintained according to organizational security requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Servers (Physical/Virtual) | YES | All production and non-production servers |
| Workstations | YES | All company-owned and managed devices |
| Notebook Computers | YES | Including remote work devices |
| Mobile Devices | YES | Company-owned smartphones and tablets |
| IoT Devices | CONDITIONAL | Only if capable of host-based protection |
| Network Equipment | NO | Covered under network boundary controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Deploy and configure host-based firewalls<br>• Monitor firewall logs and alerts<br>• Maintain firewall rule documentation |
| Security Team | • Define firewall baseline configurations<br>• Review and approve firewall rule changes<br>• Conduct compliance assessments |
| Device Owners | • Report security incidents<br>• Comply with device usage policies<br>• Request firewall exceptions through proper channels |

## 4. RULES
[RULE-01] All in-scope system components MUST have host-based boundary protection mechanisms installed and actively running.
[VALIDATION] IF system_component IN scope AND host_firewall_status != "active" THEN critical_violation

[RULE-02] Host-based firewalls MUST be configured according to approved baseline configurations within 24 hours of system deployment.
[VALIDATION] IF system_age > 24_hours AND firewall_config != "baseline_compliant" THEN violation

[RULE-03] Host-based firewall rules MUST follow least privilege principle, denying all traffic except explicitly approved connections.
[VALIDATION] IF default_rule != "deny_all" OR unapproved_allow_rules > 0 THEN violation

[RULE-04] Firewall rule changes MUST be approved by security team before implementation and documented within 48 hours.
[VALIDATION] IF rule_change_date > current_date AND (security_approval = FALSE OR documentation_complete = FALSE) THEN violation

[RULE-05] Host-based firewall logs MUST be collected and forwarded to centralized logging system within 15 minutes.
[VALIDATION] IF log_forwarding_delay > 15_minutes THEN violation

[RULE-06] Firewall bypass or disabling MUST NOT occur without documented security exception approval.
[VALIDATION] IF firewall_status = "disabled" AND security_exception = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Host Firewall Deployment - Standard process for installing and configuring firewalls on new systems
- [PROC-02] Firewall Rule Management - Change control process for firewall rule modifications
- [PROC-03] Exception Request Process - Procedure for requesting temporary firewall exceptions
- [PROC-04] Compliance Monitoring - Regular assessment of firewall configuration and status

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, technology changes, regulatory updates, control failures

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Server Deployment]
IF system_type = "server"
AND deployment_date <= 24_hours_ago
AND host_firewall_installed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Approved Firewall Exception]
IF firewall_status = "modified"
AND security_exception_approved = TRUE
AND exception_expiry_date > current_date
THEN compliance = TRUE

[SCENARIO-03: Mobile Device Without Protection]
IF device_type = "mobile"
AND company_owned = TRUE
AND host_protection_enabled = FALSE
AND capability_supported = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Firewall Log Collection Failure]
IF firewall_logs_collected = FALSE
AND last_log_timestamp > 15_minutes_ago
AND system_status = "online"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unauthorized Rule Modification]
IF firewall_rules_modified = TRUE
AND security_approval_date = NULL
AND modification_date < 48_hours_ago
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Host-based boundary protection mechanisms are defined | [RULE-01], [RULE-03] |
| Mechanisms implemented at defined system components | [RULE-01], [RULE-02] |
| Proper configuration and maintenance | [RULE-02], [RULE-04] |
| Monitoring and logging capabilities | [RULE-05] |
| Exception handling and approval | [RULE-06] |