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
All system components including servers, workstations, notebooks, and mobile devices MUST implement host-based boundary protection mechanisms. These mechanisms SHALL be properly configured, maintained, and monitored to provide effective protection at the individual system level.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Servers (physical/virtual) | YES | All production and non-production servers |
| Workstations | YES | All corporate-managed workstations |
| Notebook computers | YES | All corporate-issued laptops |
| Mobile devices | YES | All devices accessing corporate resources |
| Personal devices (BYOD) | CONDITIONAL | Only if accessing corporate network/data |
| Network appliances | NO | Covered under network-level controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Define host-based protection requirements<br>• Monitor compliance and effectiveness<br>• Investigate security incidents |
| System Administrators | • Deploy and configure host-based protections<br>• Maintain current signatures and rules<br>• Report protection failures |
| Endpoint Management Team | • Centrally manage host-based solutions<br>• Ensure consistent policy deployment<br>• Monitor agent health and connectivity |

## 4. RULES
[RULE-01] All in-scope system components MUST have host-based firewall or equivalent boundary protection mechanism installed and actively running.
[VALIDATION] IF system_component IN scope AND host_protection_active = FALSE THEN critical_violation

[RULE-02] Host-based protection mechanisms MUST be configured according to approved baseline configurations and organizational security policies.
[VALIDATION] IF configuration_compliant = FALSE OR baseline_deviation = TRUE THEN violation

[RULE-03] Host-based protection rules MUST be reviewed and updated at least quarterly or within 30 days of identified threats.
[VALIDATION] IF last_rule_review > 90_days OR threat_identified AND rule_update > 30_days THEN violation

[RULE-04] Host-based protection mechanisms MUST generate and forward security logs to centralized logging systems within 15 minutes.
[VALIDATION] IF log_forwarding_enabled = FALSE OR log_delay > 15_minutes THEN violation

[RULE-05] Users SHALL NOT disable, bypass, or tamper with host-based protection mechanisms without documented IT Security approval.
[VALIDATION] IF protection_disabled = TRUE AND approval_documented = FALSE THEN critical_violation

[RULE-06] Host-based protection agents MUST maintain connectivity to management servers and update signatures within 24 hours of release.
[VALIDATION] IF management_connectivity = FALSE OR signature_age > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Host Protection Deployment - Standardized installation and configuration of host-based protection mechanisms
- [PROC-02] Baseline Configuration Management - Maintenance of approved security configurations for different system types
- [PROC-03] Exception Request Process - Formal approval process for protection mechanism modifications or exemptions
- [PROC-04] Incident Response Integration - Procedures for responding to host-based protection alerts and violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, new threat intelligence, technology changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unprotected Corporate Laptop]
IF device_type = "laptop"
AND corporate_managed = TRUE
AND host_firewall_active = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: BYOD Device Access]
IF device_type = "mobile"
AND ownership = "personal"
AND corporate_data_access = TRUE
AND host_protection_verified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Server with Outdated Protection]
IF system_type = "server"
AND host_protection_active = TRUE
AND signature_last_update > 48_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Approved Protection Bypass]
IF host_protection_disabled = TRUE
AND security_approval_documented = TRUE
AND approval_date < 90_days_ago
AND business_justification_valid = TRUE
THEN compliance = TRUE

[SCENARIO-05: Contractor Workstation]
IF user_type = "contractor"
AND device_corporate_managed = TRUE
AND host_firewall_configured = TRUE
AND baseline_compliance = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Host-based boundary protection mechanisms are implemented | RULE-01, RULE-02 |
| Protection mechanisms are properly configured | RULE-02, RULE-03 |
| System components coverage verification | RULE-01, RULE-06 |
| Monitoring and logging capabilities | RULE-04 |
| Administrative controls and user restrictions | RULE-05 |