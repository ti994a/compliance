# POLICY: AC-18.1: Authentication and Encryption

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-18.1 |
| NIST Control | AC-18.1: Authentication and Encryption |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | wireless, authentication, encryption, access control, network security |

## 1. POLICY STATEMENT
All wireless access to organizational systems MUST be protected through strong authentication of users and devices combined with encryption. Wireless networking capabilities represent a significant security vulnerability and SHALL be secured against adversarial threats through mandatory cryptographic protections.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All wireless access points | YES | Corporate and guest networks |
| Employee devices | YES | BYOD and corporate-owned |
| Contractor devices | YES | Must meet same standards |
| IoT devices | YES | Including sensors and smart devices |
| Temporary wireless deployments | YES | Events, meetings, projects |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure wireless authentication mechanisms<br>• Implement encryption protocols<br>• Monitor wireless access attempts |
| IT Operations | • Deploy compliant wireless infrastructure<br>• Maintain wireless device inventory<br>• Execute access provisioning procedures |
| Security Operations Center | • Monitor wireless security events<br>• Investigate authentication failures<br>• Respond to wireless security incidents |

## 4. RULES
[RULE-01] All wireless access points MUST implement WPA3-Enterprise or equivalent authentication protocol with minimum AES-256 encryption.
[VALIDATION] IF wireless_protocol != "WPA3-Enterprise" AND encryption_strength < "AES-256" THEN critical_violation

[RULE-02] User authentication for wireless access MUST use multi-factor authentication (MFA) integrated with organizational identity management systems.
[VALIDATION] IF wireless_access = TRUE AND mfa_enabled = FALSE THEN violation

[RULE-03] Device authentication MUST use digital certificates issued by organizational Certificate Authority with certificate validation against revocation lists.
[VALIDATION] IF device_certificate = "invalid" OR certificate_revoked = TRUE THEN access_denied

[RULE-04] Wireless encryption keys MUST be rotated automatically every 24 hours for session keys and every 90 days for master keys.
[VALIDATION] IF session_key_age > 24_hours OR master_key_age > 90_days THEN violation

[RULE-05] Guest wireless networks MUST be isolated from internal networks with separate authentication and encryption requirements.
[VALIDATION] IF network_type = "guest" AND network_isolation = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Wireless Access Point Configuration - Standard configuration templates for enterprise wireless infrastructure
- [PROC-02] Device Certificate Management - Issuance, renewal, and revocation of device authentication certificates  
- [PROC-03] Wireless Security Monitoring - Continuous monitoring of wireless authentication and encryption status
- [PROC-04] Guest Network Management - Provisioning and management of isolated guest wireless access

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving wireless access, technology changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Corporate Device Connection]
IF device_type = "corporate"
AND wireless_protocol = "WPA3-Enterprise" 
AND mfa_enabled = TRUE
AND certificate_valid = TRUE
THEN compliance = TRUE

[SCENARIO-02: BYOD Weak Authentication]
IF device_type = "BYOD"
AND wireless_protocol = "WPA2-Personal"
AND mfa_enabled = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Expired Certificate Access]
IF certificate_status = "expired"
AND access_granted = TRUE
AND override_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Guest Network Isolation Failure]
IF network_type = "guest"
AND internal_network_access = TRUE
AND isolation_bypass = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Key Rotation Overdue]
IF session_key_age > 24_hours
AND automatic_rotation = "disabled"
AND manual_rotation_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Wireless access protected using authentication of users | [RULE-02], [RULE-03] |
| Wireless access protected using encryption | [RULE-01], [RULE-04] |
| Strong authentication implementation | [RULE-02] |
| Strong encryption implementation | [RULE-01], [RULE-04] |
| Network isolation for guest access | [RULE-05] |