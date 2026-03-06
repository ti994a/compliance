# POLICY: IA-13.1: Protection of Cryptographic Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-13.1 |
| NIST Control | IA-13.1: Protection of Cryptographic Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, access tokens, key management, digital signatures, key protection, disclosure prevention |

## 1. POLICY STATEMENT
All cryptographic keys used to protect access tokens MUST be generated using approved methods, managed throughout their lifecycle, and protected from unauthorized disclosure and misuse. Key protection measures SHALL be commensurate with the impact level of systems and information resources accessible through the protected tokens.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Identity Management Systems | YES | All systems generating/managing access tokens |
| Authentication Services | YES | Including SSO, SAML, OAuth providers |
| API Gateway Services | YES | Systems validating signed tokens |
| Development Teams | YES | Applications using cryptographic keys for tokens |
| Third-party Identity Providers | YES | When integrated with company systems |
| Test/Development Keys | CONDITIONAL | Only if used with production-like data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve cryptographic key policies<br>• Oversee key management program<br>• Ensure compliance with regulatory requirements |
| Security Architecture Team | • Define approved key generation methods<br>• Establish key protection requirements<br>• Review cryptographic implementations |
| Identity Management Team | • Implement secure key generation processes<br>• Manage key lifecycle operations<br>• Monitor key usage and access |
| Development Teams | • Follow secure coding practices for key handling<br>• Implement approved cryptographic libraries<br>• Report key-related security incidents |

## 4. RULES
[RULE-01] Cryptographic keys protecting access tokens MUST be generated using FIPS 140-2 Level 2 or higher validated cryptographic modules.
[VALIDATION] IF key_generation_module_fips_level < 2 THEN critical_violation

[RULE-02] Private keys used for signing access tokens SHALL be stored in hardware security modules (HSMs) or equivalent secure key storage for HIGH impact systems.
[VALIDATION] IF system_impact = "HIGH" AND private_key_storage != "HSM" AND private_key_storage != "equivalent_secure_storage" THEN violation

[RULE-03] Key rotation for access token signing keys MUST occur at least annually for MODERATE impact systems and every 6 months for HIGH impact systems.
[VALIDATION] IF system_impact = "MODERATE" AND key_age > 365_days THEN violation
[VALIDATION] IF system_impact = "HIGH" AND key_age > 180_days THEN violation

[RULE-04] Access to cryptographic keys protecting access tokens SHALL be restricted to authorized personnel with documented business justification.
[VALIDATION] IF key_access_granted = TRUE AND (authorization_documented = FALSE OR business_justification = FALSE) THEN violation

[RULE-05] All cryptographic key operations for access token protection MUST be logged with tamper-evident audit trails.
[VALIDATION] IF key_operation_logged = FALSE OR audit_trail_tamper_evident = FALSE THEN violation

[RULE-06] Backup copies of cryptographic keys MUST be encrypted and stored separately from primary keys with equivalent protection controls.
[VALIDATION] IF backup_key_encrypted = FALSE OR backup_colocation = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cryptographic Key Generation - Standardized process for generating keys using approved algorithms and entropy sources
- [PROC-02] Key Lifecycle Management - Procedures for key activation, rotation, revocation, and destruction
- [PROC-03] Key Access Control - Process for granting, reviewing, and revoking access to cryptographic keys
- [PROC-04] Key Backup and Recovery - Secure procedures for backing up and recovering cryptographic keys
- [PROC-05] Incident Response for Key Compromise - Steps to take when key compromise is suspected or confirmed

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving keys, regulatory changes, technology updates, system impact level changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Expired Signing Key]
IF access_token_signing_key_expired = TRUE
AND token_validation_failing = TRUE
AND key_rotation_overdue = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unauthorized Key Access]
IF personnel_access_to_keys = TRUE
AND authorization_documented = FALSE
AND access_logged = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Non-FIPS Key Generation]
IF key_generation_method = "software_random"
AND fips_validated = FALSE
AND system_impact = "HIGH"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Proper Key Backup]
IF backup_keys_exist = TRUE
AND backup_encrypted = TRUE
AND backup_location != primary_location
AND access_controls_equivalent = TRUE
THEN compliance = TRUE

[SCENARIO-05: Key Compromise Response]
IF key_compromise_detected = TRUE
AND incident_response_initiated = TRUE
AND key_revocation_completed < 4_hours
AND affected_tokens_invalidated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic keys are generated using approved methods | RULE-01 |
| Cryptographic keys are properly managed throughout lifecycle | RULE-02, RULE-03, RULE-06 |
| Cryptographic keys are protected from disclosure | RULE-04, RULE-06 |
| Cryptographic keys are protected from misuse | RULE-04, RULE-05 |