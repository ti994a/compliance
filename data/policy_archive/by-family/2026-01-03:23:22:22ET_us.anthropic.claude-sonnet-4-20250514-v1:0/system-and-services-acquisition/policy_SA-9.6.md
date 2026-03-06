# POLICY: SA-9.6: Organization-controlled Cryptographic Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9.6 |
| NIST Control | SA-9.6: Organization-controlled Cryptographic Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, external systems, encryption, key management, data protection |

## 1. POLICY STATEMENT
The organization SHALL maintain exclusive control of all cryptographic keys used for encrypting material stored or transmitted through external systems. External system providers MUST NOT have access to organizational cryptographic keys or the ability to decrypt organizational data.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud Service Providers | YES | All CSPs storing/transmitting encrypted org data |
| SaaS Applications | YES | Applications handling encrypted organizational data |
| Third-party Data Centers | YES | Facilities storing encrypted organizational systems |
| Backup Service Providers | YES | Services storing encrypted organizational backups |
| Internal Systems | NO | Covered under separate key management policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve cryptographic key control requirements<br>• Oversee external system key management compliance<br>• Review key control violations |
| Security Architecture Team | • Design key management solutions for external systems<br>• Validate cryptographic implementations<br>• Assess external system key control mechanisms |
| Vendor Management | • Include key control requirements in contracts<br>• Monitor vendor compliance with key control terms<br>• Escalate key control violations |

## 4. RULES
[RULE-01] Organizations MUST maintain exclusive control of cryptographic keys for all data encrypted and stored or transmitted through external systems.
[VALIDATION] IF external_system = TRUE AND organizational_data_encrypted = TRUE AND key_control = "external" THEN violation

[RULE-02] External system providers MUST NOT have access to organizational cryptographic keys or decryption capabilities for organizational data.
[VALIDATION] IF external_provider_key_access = TRUE OR external_provider_decrypt_capability = TRUE THEN critical_violation

[RULE-03] Cryptographic operations SHALL be performed within organizational control boundaries or through organization-controlled hardware security modules deployed in external systems.
[VALIDATION] IF crypto_operations_location = "external_uncontrolled" AND hsm_organizational_control = FALSE THEN violation

[RULE-04] All contracts with external system providers MUST include explicit requirements for organizational control of cryptographic keys.
[VALIDATION] IF external_system_contract = TRUE AND key_control_clause = FALSE THEN violation

[RULE-05] Key escrow or key recovery mechanisms provided by external systems MUST NOT be used unless organizationally controlled.
[VALIDATION] IF key_escrow_used = TRUE AND escrow_organizational_control = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External System Key Control Assessment - Evaluate key management capabilities before system adoption
- [PROC-02] Cryptographic Architecture Review - Design review for external system integration
- [PROC-03] Key Control Monitoring - Ongoing verification of key control maintenance
- [PROC-04] Contract Key Requirements - Standard clauses for external system agreements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New external system adoption, contract renewals, key control incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Storage with Provider-Managed Keys]
IF system_type = "cloud_storage"
AND encryption_enabled = TRUE
AND key_management = "provider_managed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: SaaS with Customer-Managed Encryption]
IF system_type = "saas_application"
AND organizational_data = TRUE
AND encryption_location = "organizational_premises"
AND key_control = "organizational"
THEN compliance = TRUE

[SCENARIO-03: Hybrid Cloud with HSM]
IF system_type = "hybrid_cloud"
AND hsm_deployed = TRUE
AND hsm_control = "organizational"
AND external_provider_key_access = FALSE
THEN compliance = TRUE

[SCENARIO-04: Backup Service with Shared Keys]
IF system_type = "backup_service"
AND encryption_enabled = TRUE
AND key_sharing = "provider_access"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: External System with Key Escrow]
IF external_system = TRUE
AND key_escrow_enabled = TRUE
AND escrow_control = "third_party"
AND organizational_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Exclusive control of cryptographic keys maintained for external systems | [RULE-01] |
| External providers lack access to organizational keys | [RULE-02] |
| Cryptographic operations under organizational control | [RULE-03] |
| Contractual key control requirements established | [RULE-04] |