# POLICY: MA-4.6: Cryptographic Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MA-4.6 |
| NIST Control | MA-4.6: Cryptographic Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic protection, nonlocal maintenance, diagnostic communications, integrity, confidentiality |

## 1. POLICY STATEMENT
All nonlocal maintenance and diagnostic communications MUST be protected using approved cryptographic mechanisms to ensure both integrity and confidentiality. Organizations SHALL define and implement specific cryptographic controls for remote maintenance sessions to prevent unauthorized access and protect against malicious activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Remote maintenance sessions | YES | All vendor and internal remote access |
| Diagnostic communications | YES | System health monitoring and troubleshooting |
| Local maintenance activities | NO | Physical access maintenance excluded |
| Emergency maintenance | YES | Must follow expedited crypto approval process |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define approved cryptographic mechanisms<br>• Approve cryptographic standards<br>• Review policy compliance |
| System Administrators | • Implement cryptographic protections<br>• Configure secure maintenance channels<br>• Monitor maintenance session security |
| Network Engineers | • Establish secure communication channels<br>• Maintain cryptographic infrastructure<br>• Validate encryption implementations |

## 4. RULES
[RULE-01] All nonlocal maintenance and diagnostic communications MUST use FIPS 140-2 Level 2 or higher validated cryptographic modules.
[VALIDATION] IF maintenance_type = "nonlocal" AND crypto_validation < "FIPS_140-2_Level_2" THEN violation

[RULE-02] Cryptographic mechanisms SHALL provide both integrity protection using HMAC-SHA-256 or stronger and confidentiality protection using AES-256 or approved equivalent.
[VALIDATION] IF integrity_protection NOT IN ["HMAC-SHA-256", "HMAC-SHA-384", "HMAC-SHA-512"] OR confidentiality_protection NOT IN ["AES-256", "ChaCha20-Poly1305"] THEN violation

[RULE-03] All cryptographic keys used for maintenance communications MUST be rotated at least every 90 days or after each maintenance session, whichever is more frequent.
[VALIDATION] IF key_age > 90_days OR sessions_since_rotation > 0 THEN violation

[RULE-04] Nonlocal maintenance sessions SHALL establish end-to-end encryption before any diagnostic data transmission begins.
[VALIDATION] IF maintenance_session = "active" AND encryption_established = FALSE AND data_transmitted = TRUE THEN critical_violation

[RULE-05] Organizations MUST maintain an approved list of cryptographic mechanisms and review it annually or when cryptographic standards change.
[VALIDATION] IF approved_crypto_list_age > 365_days OR standards_updated = TRUE AND list_reviewed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cryptographic Mechanism Selection - Define process for selecting and approving cryptographic controls
- [PROC-02] Secure Channel Establishment - Establish encrypted communication channels before maintenance
- [PROC-03] Key Management for Maintenance - Generate, distribute, and rotate cryptographic keys
- [PROC-04] Maintenance Session Monitoring - Monitor and log all cryptographic maintenance activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Cryptographic standard updates, security incidents involving maintenance, new maintenance tools deployment

## 7. SCENARIO PATTERNS
[SCENARIO-01: Vendor Remote Maintenance]
IF maintenance_type = "vendor_remote"
AND crypto_mechanism = "approved"
AND encryption_active = TRUE
AND integrity_protection = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unencrypted Diagnostic Session]
IF session_type = "diagnostic"
AND location = "remote"
AND encryption_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Weak Cryptographic Protection]
IF maintenance_session = "active"
AND crypto_standard = "AES-128"
AND approved_minimum = "AES-256"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Emergency Maintenance Override]
IF maintenance_urgency = "emergency"
AND crypto_bypass_approved = TRUE
AND compensating_controls = "implemented"
AND duration < 4_hours
THEN compliance = TRUE

[SCENARIO-05: Expired Cryptographic Keys]
IF key_rotation_date < (current_date - 90_days)
AND maintenance_session = "scheduled"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Define cryptographic mechanisms for integrity and confidentiality | [RULE-02], [RULE-05] |
| Implement cryptographic mechanisms for integrity protection | [RULE-01], [RULE-04] |
| Implement cryptographic mechanisms for confidentiality protection | [RULE-01], [RULE-04] |
| Maintain cryptographic key management | [RULE-03] |