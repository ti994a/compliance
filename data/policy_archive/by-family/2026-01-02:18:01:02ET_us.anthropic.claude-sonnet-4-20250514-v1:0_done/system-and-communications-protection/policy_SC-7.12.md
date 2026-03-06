```markdown
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
All system components including servers, workstations, notebooks, and mobile devices MUST implement host-based boundary protection mechanisms. These mechanisms SHALL be properly configured, maintained, and monitored to provide defense-in-depth protection at the endpoint level.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Servers | YES | All production and non-production servers |
| Workstations | YES | Corporate-managed desktop and laptop systems |
| Mobile Devices | YES | Company-owned smartphones, tablets accessing corporate resources |
| Virtual Machines | YES | All VMs regardless of hosting location |
| Containers | CONDITIONAL | When processing sensitive data or in production |
| IoT Devices | CONDITIONAL | When connected to corporate network |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Deploy and configure host-based protection mechanisms<br>• Monitor protection status and alerts<br>• Maintain current protection signatures and rules |
| Security Operations Team | • Define protection policies and rules<br>• Investigate security incidents<br>• Perform compliance monitoring and reporting |
| Asset Owners | • Ensure systems under their control have required protections<br>• Report protection failures or anomalies<br>• Coordinate maintenance windows for updates |

## 4. RULES

[RULE-01] All in-scope system components MUST have an approved host-based boundary protection mechanism installed and actively running.
[VALIDATION] IF system_component IN scope AND host_protection_installed = FALSE THEN critical_violation

[RULE-02] Host-based protection mechanisms MUST be configured according to organization-approved baseline configurations and security policies.
[VALIDATION] IF host_protection_config != approved_baseline THEN violation

[RULE-03] Host-based protection mechanisms MUST maintain current signatures, rules, and threat intelligence updates within 24 hours of availability.
[VALIDATION] IF signature_age > 24_hours AND update_available = TRUE THEN violation

[RULE-04] Host-based protection mechanisms MUST log security events and forward logs to the centralized security monitoring system within 15 minutes.
[VALIDATION] IF log_forwarding_delay > 15_minutes THEN violation

[RULE-05] Users SHALL NOT disable, bypass, or modify host-based protection mechanisms without documented security approval.
[VALIDATION] IF protection_disabled = TRUE AND security_approval = FALSE THEN critical_violation

[RULE-06] Host-based protection status MUST be monitored continuously with alerts generated for protection failures within 5 minutes.
[VALIDATION] IF protection_failure_detected = TRUE AND alert_delay > 5_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Host Protection Deployment - Standardized installation and configuration process
- [PROC-02] Baseline Configuration Management - Maintenance of approved security configurations  
- [PROC-03] Exception Request Process - Formal approval workflow for protection modifications
- [PROC-04] Incident Response - Response procedures for protection failures or bypasses
- [PROC-05] Compliance Monitoring - Regular assessment of protection deployment and effectiveness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents involving unprotected endpoints, new technology deployments, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unprotected Production Server]
IF system_type = "production_server"
AND host_firewall_enabled = FALSE
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Outdated Protection Signatures]
IF signature_last_updated > 48_hours
AND internet_connectivity = TRUE
AND maintenance_window = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Mobile Device Without Protection]
IF device_type = "mobile"
AND corporate_data_access = TRUE
AND host_protection_installed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Approved Temporary Bypass]
IF host_protection_disabled = TRUE
AND security_approval_valid = TRUE
AND bypass_duration < approved_timeframe
AND compensating_controls = TRUE
THEN compliance = TRUE

[SCENARIO-05: Container in Production Environment]
IF system_type = "container"
AND environment = "production"
AND host_protection_enabled = FALSE
AND container_security_controls = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Host-based boundary protection mechanisms are defined | [RULE-01], [RULE-02] |
| Protection mechanisms are implemented at system components | [RULE-01], [RULE-06] |
| Mechanisms are properly configured and maintained | [RULE-02], [RULE-03] |
| Protection status is monitored and managed | [RULE-04], [RULE-06] |
| Unauthorized modifications are prevented | [RULE-05] |
```