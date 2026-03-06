# POLICY: SA-9.6: Organization-controlled Cryptographic Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9.6 |
| NIST Control | SA-9.6: Organization-controlled Cryptographic Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, external systems, encryption, key management, exclusive control |

## 1. POLICY STATEMENT
The organization SHALL maintain exclusive control of all cryptographic keys used for encrypting data stored or transmitted through external systems. External system providers SHALL NOT have access to organizational cryptographic keys or the ability to decrypt organizational data.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud service providers | YES | All external cloud storage and processing |
| SaaS applications | YES | When storing encrypted organizational data |
| Third-party data processors | YES | All contracted data processing services |
| Internal systems | NO | Covered by other key management policies |
| Public key infrastructure | CONDITIONAL | Only for organizationally-controlled private keys |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve cryptographic key management strategies for external systems<br>• Ensure compliance with exclusive key control requirements<br>• Review key management incidents and violations |
| Cryptographic Officer | • Implement and maintain exclusive key control mechanisms<br>• Validate encryption/decryption processes for external systems<br>• Monitor key access and usage across external services |
| IT Security Team | • Configure encryption solutions for external system integration<br>• Audit external system key management implementations<br>• Respond to key compromise incidents |

## 4. RULES
[RULE-01] Organizations MUST maintain exclusive control of cryptographic keys for all data encrypted and stored in external systems.
[VALIDATION] IF data_location = "external_system" AND key_control = "external_provider" THEN critical_violation

[RULE-02] External system providers SHALL NOT have access to organizational cryptographic keys or decryption capabilities.
[VALIDATION] IF external_provider_access = "cryptographic_keys" OR external_provider_access = "decryption_capability" THEN critical_violation

[RULE-03] Encryption and decryption operations MUST occur within organizational boundaries or through organizationally-controlled components.
[VALIDATION] IF encryption_location = "external_system" AND organizational_control = FALSE THEN violation

[RULE-04] Key escrow or key recovery mechanisms for external systems MUST be under exclusive organizational control.
[VALIDATION] IF key_escrow_exists = TRUE AND escrow_control ≠ "organization" THEN violation

[RULE-05] Contractual agreements with external providers MUST explicitly prohibit provider access to organizational cryptographic keys.
[VALIDATION] IF contract_exists = TRUE AND key_access_prohibition = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External System Key Management - Establish exclusive key control for external integrations
- [PROC-02] Key Control Validation - Verify organizational control before external system deployment
- [PROC-03] External Provider Assessment - Evaluate provider key management capabilities and restrictions
- [PROC-04] Key Compromise Response - Respond to potential key exposure in external systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New external system integrations, key compromise incidents, contract renewals, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Storage with Provider-Managed Keys]
IF data_storage = "external_cloud"
AND encryption_keys = "provider_managed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: SaaS Application with Client-Side Encryption]
IF application_type = "external_saas"
AND encryption_location = "client_side"
AND key_control = "organization"
THEN compliance = TRUE

[SCENARIO-03: Third-Party Processing with Shared Keys]
IF data_processing = "third_party"
AND key_access = "shared_with_provider"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: External System with Organizational HSM]
IF external_system = TRUE
AND encryption_component = "organizational_hsm"
AND key_access = "organization_exclusive"
THEN compliance = TRUE

[SCENARIO-05: Contract Without Key Access Restrictions]
IF external_provider_contract = TRUE
AND key_access_clause = "not_specified"
AND encrypted_data_transfer = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Exclusive control of cryptographic keys is maintained for encrypted material stored or transmitted through an external system | [RULE-01], [RULE-02], [RULE-03] |