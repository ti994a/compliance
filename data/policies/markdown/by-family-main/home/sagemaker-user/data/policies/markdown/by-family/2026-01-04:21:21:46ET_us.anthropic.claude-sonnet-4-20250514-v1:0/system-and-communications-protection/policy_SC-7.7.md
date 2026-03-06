```markdown
# POLICY: SC-7.7: Split Tunneling for Remote Devices

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.7 |
| NIST Control | SC-7.7: Split Tunneling for Remote Devices |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | split tunneling, remote access, VPN, boundary protection, network security |

## 1. POLICY STATEMENT
Split tunneling for remote devices connecting to organizational systems is prohibited unless securely provisioned using approved safeguards. All remote connections must be controlled to prevent unauthorized external network access that could compromise organizational information or systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Remote employees | YES | All employees accessing systems remotely |
| Contractors/vendors | YES | Third-party personnel with remote access |
| Mobile devices | YES | Company-owned and BYOD devices |
| VPN connections | YES | All VPN client configurations |
| Guest networks | NO | Separate policy governs guest access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure and maintain VPN infrastructure<br>• Monitor for split tunneling violations<br>• Implement technical controls |
| IT Operations | • Deploy compliant remote access configurations<br>• Provide user support and training<br>• Maintain device compliance monitoring |
| Security Operations Center | • Monitor remote access logs<br>• Investigate split tunneling incidents<br>• Enforce policy violations |

## 4. RULES
[RULE-01] Remote devices MUST NOT be configured to allow split tunneling unless explicitly approved through the secure provisioning process.
[VALIDATION] IF remote_device_connected = TRUE AND split_tunneling_enabled = TRUE AND secure_provisioning_approved = FALSE THEN violation

[RULE-02] VPN clients MUST be configured to disable user-controllable split tunneling settings by default.
[VALIDATION] IF vpn_client_deployed = TRUE AND user_configurable_split_tunnel = TRUE THEN violation

[RULE-03] Securely provisioned split tunnels SHALL only allow connectivity to pre-approved, named environments or specific IP address ranges.
[VALIDATION] IF split_tunnel_approved = TRUE AND (destination_addresses NOT IN approved_list OR user_controllable = TRUE) THEN violation

[RULE-04] Remote access monitoring systems MUST detect and alert on unauthorized split tunneling within 15 minutes of occurrence.
[VALIDATION] IF split_tunneling_detected = TRUE AND alert_time > 15_minutes THEN violation

[RULE-05] Remote devices found using unauthorized split tunneling SHALL be immediately disconnected from organizational systems.
[VALIDATION] IF unauthorized_split_tunnel = TRUE AND connection_active = TRUE AND disconnect_time > 5_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Split Tunnel Risk Assessment - Evaluate business justification and security risks
- [PROC-02] Secure VPN Provisioning - Configure locked-down split tunnel environments
- [PROC-03] Remote Device Monitoring - Continuous monitoring for split tunneling violations
- [PROC-04] Incident Response - Handle split tunneling security incidents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, technology changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Employee Split Tunneling]
IF remote_employee_connected = TRUE
AND split_tunneling_detected = TRUE
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved Contractor Split Tunnel]
IF contractor_connection = TRUE
AND split_tunnel_active = TRUE
AND secure_provisioning_approved = TRUE
AND destination_in_approved_list = TRUE
THEN compliance = TRUE

[SCENARIO-03: User-Configurable VPN Client]
IF vpn_client_installed = TRUE
AND split_tunnel_user_configurable = TRUE
AND user_modified_settings = TRUE
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-04: Delayed Incident Response]
IF split_tunnel_violation_detected = TRUE
AND alert_generated = TRUE
AND response_time > 15_minutes
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-05: Mobile Device Split Tunneling]
IF mobile_device_connected = TRUE
AND personal_app_traffic = TRUE
AND corporate_vpn_active = TRUE
AND split_tunnel_unauthorized = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prevent unauthorized split tunneling | [RULE-01], [RULE-02] |
| Secure provisioning of approved split tunnels | [RULE-03] |
| Detection and monitoring capabilities | [RULE-04] |
| Incident response and remediation | [RULE-05] |
```