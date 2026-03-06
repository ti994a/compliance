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
Remote devices connecting to organizational systems SHALL NOT use split tunneling unless the split tunnel is securely provisioned using approved safeguards. All split tunneling must be explicitly authorized and continuously monitored to prevent unauthorized external connections and data exfiltration.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Remote employees | YES | All remote workers using company devices |
| Contractors | YES | Third-party personnel with system access |
| Company-owned devices | YES | Laptops, tablets, mobile devices |
| BYOD devices | YES | Personal devices accessing company systems |
| Guest networks | NO | Limited to internet-only access |
| Physical office connections | NO | Direct wired connections exempt |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure VPN clients to prevent unauthorized split tunneling<br>• Monitor network traffic for split tunnel violations<br>• Maintain approved split tunnel configurations |
| IT Operations | • Deploy compliant remote access solutions<br>• Validate device configurations before network access<br>• Implement technical controls to detect split tunneling |
| Remote Users | • Use only approved VPN configurations<br>• Report suspected network security issues<br>• Comply with remote access security requirements |

## 4. RULES
[RULE-01] Remote devices MUST NOT establish split tunnel connections unless explicitly authorized and securely provisioned through approved VPN solutions.
[VALIDATION] IF remote_device = TRUE AND split_tunnel_detected = TRUE AND authorized_split_tunnel = FALSE THEN critical_violation

[RULE-02] Approved split tunnels SHALL only connect to pre-approved, managed environments without user-configurable routing options.
[VALIDATION] IF split_tunnel_approved = TRUE AND (user_configurable_routing = TRUE OR destination_not_preapproved = TRUE) THEN violation

[RULE-03] VPN clients MUST be configured to prevent users from modifying tunnel settings or establishing unauthorized external connections.
[VALIDATION] IF vpn_client_deployed = TRUE AND user_modification_allowed = TRUE THEN violation

[RULE-04] Split tunnel detection mechanisms MUST automatically block connections when unauthorized split tunneling is identified.
[VALIDATION] IF unauthorized_split_tunnel_detected = TRUE AND connection_blocked = FALSE THEN critical_violation

[RULE-05] All remote access sessions SHALL be continuously monitored for split tunneling activity with real-time alerting capabilities.
[VALIDATION] IF remote_session_active = TRUE AND split_tunnel_monitoring = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Split Tunnel Authorization Process - Formal approval workflow for legitimate split tunnel requirements
- [PROC-02] VPN Configuration Management - Standardized deployment and maintenance of secure VPN clients
- [PROC-03] Split Tunnel Detection and Response - Automated monitoring and incident response procedures
- [PROC-04] Remote Device Compliance Validation - Pre-connection security posture assessment

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving split tunneling, new remote access technologies, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Split Tunnel Detection]
IF device_type = "remote_laptop"
AND vpn_connected = TRUE
AND external_connection_detected = TRUE
AND split_tunnel_authorized = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Contractor Using Personal VPN]
IF user_type = "contractor"
AND company_vpn_active = TRUE
AND personal_vpn_detected = TRUE
AND dual_tunnel_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Approved Split Tunnel to Managed Environment]
IF split_tunnel_active = TRUE
AND destination_environment = "managed_cloud_service"
AND pre_approved_destination = TRUE
AND user_routing_control = FALSE
THEN compliance = TRUE

[SCENARIO-04: User Modifying VPN Configuration]
IF vpn_client_installed = TRUE
AND configuration_modified = TRUE
AND modification_source = "end_user"
AND admin_approval = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Split Tunnel Without Monitoring]
IF remote_connection_active = TRUE
AND split_tunnel_enabled = TRUE
AND real_time_monitoring = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Split tunneling prevention for remote devices | [RULE-01] |
| Secure provisioning using defined safeguards | [RULE-02] |
| Prevention of user-configurable settings | [RULE-03] |
| Detection and blocking capabilities | [RULE-04] |
| Continuous monitoring requirements | [RULE-05] |