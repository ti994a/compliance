# POLICY: SC-28.3: Cryptographic Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-28.3 |
| NIST Control | SC-28.3: Cryptographic Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, protected storage, TPM, hardware security module, key management |

## 1. POLICY STATEMENT
All cryptographic keys used by organizational systems MUST be stored in protected storage mechanisms that provide hardware-based security protections. Protected storage mechanisms SHALL prevent unauthorized access to cryptographic material and maintain key integrity throughout the key lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All cryptographic keys | YES | Including encryption, signing, and authentication keys |
| Hardware Security Modules | YES | Primary protected storage mechanism |
| Trusted Platform Modules | YES | Acceptable for endpoint key storage |
| Software-only key storage | NO | Does not meet protected storage requirement |
| Cloud-based HSMs | YES | When properly configured and validated |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve protected storage mechanisms<br>• Define key protection requirements<br>• Oversee compliance monitoring |
| System Administrators | • Configure protected storage systems<br>• Implement key storage procedures<br>• Monitor key storage integrity |
| Security Engineers | • Validate protected storage implementations<br>• Assess key protection mechanisms<br>• Conduct security reviews |

## 4. RULES
[RULE-01] All cryptographic keys MUST be stored in hardware-protected storage mechanisms such as Hardware Security Modules (HSMs) or Trusted Platform Modules (TPMs).
[VALIDATION] IF key_storage_type != "hardware_protected" THEN critical_violation

[RULE-02] Protected storage mechanisms MUST be FIPS 140-2 Level 2 or higher certified for organizational cryptographic keys.
[VALIDATION] IF storage_certification_level < "FIPS_140-2_Level_2" THEN violation

[RULE-03] Software-only key storage SHALL NOT be used for production cryptographic keys except during initial key generation and immediate transfer to protected storage.
[VALIDATION] IF key_storage_type = "software_only" AND storage_duration > 24_hours THEN critical_violation

[RULE-04] Key extraction from protected storage MUST require multi-factor authentication and be logged with tamper-evident audit trails.
[VALIDATION] IF key_extraction_mfa = FALSE OR audit_logging = FALSE THEN violation

[RULE-05] Protected storage systems MUST implement tamper detection and automatic key zeroization upon physical intrusion attempts.
[VALIDATION] IF tamper_detection = FALSE OR auto_zeroization = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Key Storage Assessment - Validate protected storage mechanisms meet security requirements
- [PROC-02] HSM/TPM Configuration - Establish secure configuration baselines for protected storage
- [PROC-03] Key Migration - Secure transfer of keys from generation to protected storage
- [PROC-04] Storage Monitoring - Continuous monitoring of protected storage integrity and access

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving keys, new cryptographic implementations, technology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Development Key Storage]
IF environment_type = "development"
AND key_storage_type = "software_only"
AND key_type = "production_equivalent"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Cloud HSM Usage]
IF key_storage_mechanism = "cloud_HSM"
AND fips_certification = "Level_3"
AND access_controls = "implemented"
THEN compliance = TRUE

[SCENARIO-03: TPM for Endpoint Keys]
IF system_type = "endpoint"
AND key_storage_mechanism = "TPM"
AND tpm_version >= "2.0"
AND fips_certification >= "Level_2"
THEN compliance = TRUE

[SCENARIO-04: Temporary Software Storage]
IF key_generation_location = "software"
AND transfer_to_hsm_time <= 1_hour
AND software_storage_encrypted = TRUE
THEN compliance = TRUE

[SCENARIO-05: Legacy System Keys]
IF system_age > 5_years
AND key_storage_type = "software_only"
AND migration_plan = "not_documented"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Protected storage for cryptographic keys is provided using hardware-protected mechanisms | RULE-01, RULE-02 |
| Key storage mechanisms prevent unauthorized access | RULE-04, RULE-05 |
| Storage mechanisms maintain key integrity | RULE-02, RULE-05 |