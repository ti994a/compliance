# POLICY: SA-9.6: Organization-controlled Cryptographic Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9.6 |
| NIST Control | SA-9.6: Organization-controlled Cryptographic Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, external systems, encryption, key management, third-party services |

## 1. POLICY STATEMENT
The organization SHALL maintain exclusive control of all cryptographic keys used for encrypting data stored or transmitted through external systems. External system providers SHALL NOT have access to organizational cryptographic keys or the ability to decrypt organizational data.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud Service Providers | YES | All SaaS, PaaS, IaaS providers |
| Third-party Data Centers | YES | Colocation and hosting facilities |
| Managed Service Providers | YES | IT services handling encrypted data |
| Business Partners | YES | When processing encrypted organizational data |
| Internal Systems | NO | Covered by separate key management policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve cryptographic key control strategies<br>• Oversee compliance with external system requirements<br>• Authorize exceptions to key control requirements |
| Cryptographic Officer | • Design key management architectures for external systems<br>• Validate key control implementations<br>• Monitor key access and usage |
| Vendor Management | • Include key control requirements in contracts<br>• Verify vendor compliance with key control obligations<br>• Manage key control-related SLAs |

## 4. RULES
[RULE-01] Organizations MUST maintain exclusive control of cryptographic keys for all data encrypted and stored or transmitted through external systems.
[VALIDATION] IF external_system = TRUE AND organizational_data_encrypted = TRUE AND key_control != "exclusive_organizational" THEN violation

[RULE-02] External system providers SHALL NOT have access to organizational cryptographic keys or plaintext versions of encrypted organizational data.
[VALIDATION] IF external_provider_key_access = TRUE OR external_provider_plaintext_access = TRUE THEN critical_violation

[RULE-03] Encryption and decryption operations MUST occur within organizational boundaries or through organizationally-controlled hardware security modules deployed in external environments.
[VALIDATION] IF crypto_operations_location != "organizational_control" AND hsm_organizational_control != TRUE THEN violation

[RULE-04] Key escrow or key recovery mechanisms provided by external systems SHALL NOT be used unless organizationally controlled and documented through formal risk acceptance.
[VALIDATION] IF external_key_escrow = TRUE AND organizational_control = FALSE AND risk_acceptance_documented = FALSE THEN violation

[RULE-05] Contracts with external system providers MUST explicitly prohibit provider access to organizational cryptographic keys and specify key control requirements.
[VALIDATION] IF external_contract_exists = TRUE AND key_control_clause = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External System Key Control Assessment - Evaluate key control mechanisms before external system adoption
- [PROC-02] Cryptographic Architecture Review - Design and approve key management for external system integrations
- [PROC-03] Vendor Key Control Verification - Validate and monitor external provider compliance with key control requirements
- [PROC-04] Key Control Incident Response - Address compromises or violations of key control in external systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New external system adoption, vendor security incidents, key compromise events, contract renewals

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Storage with Provider-Managed Keys]
IF external_system_type = "cloud_storage"
AND encryption_enabled = TRUE
AND key_management = "provider_managed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Organizationally-Controlled HSM in External Environment]
IF external_system = TRUE
AND hsm_deployed = TRUE
AND hsm_organizational_control = TRUE
AND provider_key_access = FALSE
THEN compliance = TRUE

[SCENARIO-03: Third-Party Backup Service with Escrow]
IF service_type = "backup"
AND external_provider = TRUE
AND key_escrow_enabled = TRUE
AND organizational_key_control = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Hybrid Cloud with Client-Side Encryption]
IF deployment_model = "hybrid_cloud"
AND encryption_location = "client_side"
AND key_storage = "organizational"
AND provider_plaintext_access = FALSE
THEN compliance = TRUE

[SCENARIO-05: Managed Service with Bring-Your-Own-Key]
IF service_type = "managed_service"
AND key_model = "bring_your_own_key"
AND organizational_key_control = TRUE
AND contract_prohibits_provider_access = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Exclusive control of cryptographic keys maintained for external systems | RULE-01, RULE-03 |
| External providers prohibited from key access | RULE-02 |
| Organizational control of encryption/decryption operations | RULE-03 |
| Key escrow restrictions | RULE-04 |
| Contractual key control requirements | RULE-05 |