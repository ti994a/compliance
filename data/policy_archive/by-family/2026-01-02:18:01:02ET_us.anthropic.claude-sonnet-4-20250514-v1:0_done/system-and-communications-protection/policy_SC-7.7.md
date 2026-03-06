# POLICY: SC-7.7: Split Tunneling for Remote Devices

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.7 |
| NIST Control | SC-7.7: Split Tunneling for Remote Devices |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | split tunneling, remote access, VPN, network security, boundary protection |

## 1. POLICY STATEMENT
Split tunneling for remote devices connecting to organizational systems is prohibited unless securely provisioned using approved safeguards. All remote connections must be configured to prevent unauthorized external network access while connected to organizational systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Remote employees | YES | All staff accessing systems remotely |
| Contractors | YES | External personnel with system access |
| Third-party vendors | YES | When accessing organizational systems |
| Mobile devices | YES | Company and BYOD devices |
| VPN connections | YES | All remote access methods |
| Guest networks | NO | No organizational system access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure VPN clients to prevent split tunneling<br>• Monitor for unauthorized split tunnel configurations<br>• Maintain approved split tunnel safeguards |
| IT Operations | • Deploy compliant remote access clients<br>• Validate device configurations before connection<br>• Implement technical controls to detect violations |
| Remote Users | • Use only approved remote access methods<br>• Report suspected configuration issues<br>• Comply with device configuration requirements |

## 4. RULES
[RULE-01] Remote devices MUST NOT use split tunneling when connecting to organizational systems unless explicitly authorized and securely provisioned.
[VALIDATION] IF remote_connection = TRUE AND split_tunnel_detected = TRUE AND authorized_exception = FALSE THEN violation

[RULE-02] VPN clients MUST be configured to disable user-configurable split tunneling options by default.
[VALIDATION] IF vpn_client_deployed = TRUE AND user_configurable_split_tunnel = TRUE THEN violation

[RULE-03] Securely provisioned split tunnels SHALL only connect to pre-approved, named network environments without user control.
[VALIDATION] IF split_tunnel_authorized = TRUE AND (destination_networks NOT IN approved_list OR user_controllable = TRUE) THEN violation

[RULE-04] Network monitoring systems MUST detect and block connections from devices using unauthorized split tunneling.
[VALIDATION] IF split_tunnel_detected = TRUE AND connection_blocked = FALSE AND detection_time > 5_minutes THEN violation

[RULE-05] Remote access clients SHALL prevent modification of tunnel configuration settings by end users.
[VALIDATION] IF remote_client_installed = TRUE AND user_can_modify_tunnel_config = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Split Tunnel Exception Process - Formal approval workflow for authorized split tunnel configurations
- [PROC-02] Remote Device Configuration Validation - Technical verification of compliant device settings
- [PROC-03] Split Tunnel Detection and Response - Automated monitoring and incident response procedures
- [PROC-04] VPN Client Deployment - Standardized installation and configuration management

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving split tunneling, new remote access technologies, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Split Tunnel Detection]
IF remote_device_connected = TRUE
AND split_tunnel_active = TRUE
AND formal_authorization = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: User-Modified VPN Configuration]
IF vpn_client_installed = TRUE
AND user_modified_tunnel_settings = TRUE
AND administrative_approval = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Approved Split Tunnel Implementation]
IF split_tunnel_requested = TRUE
AND security_review_completed = TRUE
AND pre_approved_destinations_only = TRUE
AND user_control_disabled = TRUE
THEN compliance = TRUE

[SCENARIO-04: Mobile Device Personal Use]
IF mobile_device_type = "BYOD"
AND organizational_system_connected = TRUE
AND personal_apps_accessible = TRUE
AND split_tunnel_prevention = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Contractor Remote Access]
IF user_type = "contractor"
AND remote_connection_active = TRUE
AND split_tunnel_detected = TRUE
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prevent split tunneling for remote devices | RULE-01, RULE-04 |
| Secure provisioning of authorized split tunnels | RULE-03 |
| Prevention of user configuration modifications | RULE-02, RULE-05 |
| Detection and blocking capabilities | RULE-04 |