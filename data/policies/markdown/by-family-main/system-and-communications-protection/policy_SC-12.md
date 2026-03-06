# POLICY: SC-12: Cryptographic Key Establishment and Management

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12 |
| NIST Control | SC-12: Cryptographic Key Establishment and Management |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, key management, encryption, key generation, key distribution, key storage, key destruction, FIPS 140-2, trust stores |

## 1. POLICY STATEMENT
The organization SHALL establish and manage cryptographic keys throughout their lifecycle when cryptography is employed within systems. All cryptographic key operations including generation, distribution, storage, access, and destruction MUST comply with defined security requirements and approved standards.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems using cryptographic functions |
| Cloud Services | YES | Including hybrid and multi-cloud environments |
| Third-party Applications | YES | When integrated with organizational systems |
| Mobile Devices | YES | Corporate and BYOD with access to systems |
| IoT Devices | YES | Connected devices using encryption |
| Development/Test Systems | YES | Must follow same key management standards |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve cryptographic key management policies<br>• Oversee compliance with regulatory requirements<br>• Authorize key management system implementations |
| Security Operations | • Implement key lifecycle procedures<br>• Monitor key usage and compliance<br>• Manage trust stores and certificate authorities |
| System Administrators | • Configure key management systems<br>• Execute key rotation procedures<br>• Maintain key backup and recovery capabilities |
| Application Owners | • Define application-specific key requirements<br>• Ensure proper key integration in applications<br>• Coordinate key updates with security teams |

## 4. RULES
[RULE-01] Cryptographic keys MUST be generated using FIPS 140-2 Level 2 or higher validated cryptographic modules.
[VALIDATION] IF key_generation_module_fips_level < 2 THEN critical_violation

[RULE-02] Key generation MUST use approved random number generators with sufficient entropy as specified in NIST SP 800-90A.
[VALIDATION] IF rng_type NOT IN approved_rng_list OR entropy_level < required_minimum THEN violation

[RULE-03] Symmetric encryption keys MUST be a minimum of 128 bits for new implementations and 256 bits for highly sensitive data.
[VALIDATION] IF symmetric_key_length < 128 OR (data_classification = "highly_sensitive" AND key_length < 256) THEN violation

[RULE-04] Asymmetric encryption keys MUST be a minimum of 2048 bits for RSA or equivalent strength for other algorithms.
[VALIDATION] IF (algorithm = "RSA" AND key_length < 2048) OR equivalent_strength < 2048_bit_rsa THEN violation

[RULE-05] Cryptographic keys MUST be rotated according to defined schedules: annually for long-term keys, quarterly for medium-term keys, and monthly for high-risk environments.
[VALIDATION] IF (key_type = "long_term" AND days_since_rotation > 365) OR (key_type = "medium_term" AND days_since_rotation > 90) OR (environment_risk = "high" AND days_since_rotation > 30) THEN violation

[RULE-06] Key distribution MUST occur through secure, authenticated channels with integrity protection.
[VALIDATION] IF key_distribution_channel_encrypted = FALSE OR authentication_verified = FALSE OR integrity_protected = FALSE THEN critical_violation

[RULE-07] Cryptographic keys MUST be stored in FIPS 140-2 Level 2 or higher hardware security modules or equivalent protected storage.
[VALIDATION] IF key_storage_protection_level < "FIPS_140-2_Level_2" THEN critical_violation

[RULE-08] Access to cryptographic keys MUST be restricted to authorized personnel with documented business justification and approval.
[VALIDATION] IF key_access_granted = TRUE AND (authorization_documented = FALSE OR business_justification = FALSE OR approval_obtained = FALSE) THEN violation

[RULE-09] Key destruction MUST render keys unrecoverable using approved sanitization methods within 24 hours of destruction authorization.
[VALIDATION] IF destruction_authorized = TRUE AND (destruction_completed = FALSE OR hours_since_authorization > 24 OR sanitization_method NOT IN approved_methods) THEN violation

[RULE-10] Trust stores MUST contain only approved trust anchors and certificates, with quarterly reviews of all entries.
[VALIDATION] IF trust_store_entry NOT IN approved_certificates OR days_since_review > 90 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Key Generation Procedure - Standardized process for generating cryptographic keys using approved methods
- [PROC-02] Key Distribution Procedure - Secure methods for distributing keys to authorized systems and personnel
- [PROC-03] Key Rotation Procedure - Scheduled replacement of cryptographic keys based on risk and usage
- [PROC-04] Key Backup and Recovery Procedure - Secure backup and emergency recovery of critical cryptographic keys
- [PROC-05] Key Destruction Procedure - Secure deletion and sanitization of cryptographic keys at end of lifecycle
- [PROC-06] Trust Store Management Procedure - Management and validation of certificate authorities and trust anchors

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving keys, regulatory changes, technology updates, failed audits

## 7. SCENARIO PATTERNS
[SCENARIO-01: Weak Key Generation]
IF key_generation_method = "software_only"
AND fips_validation = FALSE
AND system_classification = "sensitive"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Overdue Key Rotation]
IF key_age > rotation_schedule
AND environment_classification = "production"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unauthorized Key Access]
IF key_access_requested = TRUE
AND requester_authorization_level = "insufficient"
AND override_applied = FALSE
THEN compliance = TRUE

[SCENARIO-04: Insecure Key Storage]
IF key_storage_location = "unencrypted_database"
AND data_classification IN ["confidential", "restricted"]
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Incomplete Key Destruction]
IF key_destruction_requested = TRUE
AND destruction_method = "standard_delete"
AND secure_sanitization = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Keys established in accordance with requirements | RULE-01, RULE-02, RULE-03, RULE-04 |
| Key generation requirements defined | RULE-01, RULE-02 |
| Key distribution requirements defined | RULE-06 |
| Key storage requirements defined | RULE-07 |
| Key access requirements defined | RULE-08 |
| Key destruction requirements defined | RULE-09 |
| Trust store management | RULE-10 |