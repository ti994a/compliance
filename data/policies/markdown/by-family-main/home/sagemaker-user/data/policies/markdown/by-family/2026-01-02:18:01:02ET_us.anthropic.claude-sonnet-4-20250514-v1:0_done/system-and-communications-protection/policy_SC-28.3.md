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
All cryptographic keys used by organizational systems MUST be stored in hardware-protected storage mechanisms that provide tamper-resistant protection. Software-based key storage is prohibited for production systems handling sensitive data.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing sensitive data |
| Development Systems | CONDITIONAL | Required if handling production data |
| Test Systems | CONDITIONAL | Required if using production keys |
| Third-party Services | YES | Must meet equivalent protection standards |
| Mobile Devices | YES | Corporate devices accessing encrypted data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement hardware-protected key storage<br>• Configure TPM/HSM modules<br>• Monitor key storage integrity |
| Security Engineers | • Design key protection architecture<br>• Validate hardware protection mechanisms<br>• Conduct security assessments |
| Cryptographic Officers | • Approve key storage solutions<br>• Oversee key lifecycle management<br>• Ensure compliance with protection requirements |

## 4. RULES
[RULE-01] All cryptographic keys MUST be stored using hardware-protected storage mechanisms such as TPM, HSM, or equivalent tamper-resistant hardware.
[VALIDATION] IF key_storage_type = "software" AND system_classification >= "sensitive" THEN critical_violation

[RULE-02] Software-based key storage SHALL NOT be used for production systems processing sensitive or classified information.
[VALIDATION] IF key_storage_type = "software" AND environment = "production" AND data_sensitivity >= "sensitive" THEN critical_violation

[RULE-03] Hardware protection mechanisms MUST provide tamper detection and resistance capabilities verified through FIPS 140-2 Level 2 or higher certification.
[VALIDATION] IF hardware_certification_level < "FIPS_140-2_Level_2" THEN major_violation

[RULE-04] Key storage solutions MUST maintain audit logs of all key access and usage activities.
[VALIDATION] IF key_access_logging = FALSE THEN major_violation

[RULE-05] Backup cryptographic keys MUST be stored using equivalent or stronger hardware protection than primary keys.
[VALIDATION] IF backup_key_protection < primary_key_protection THEN major_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Hardware Key Storage Implementation - Deploy and configure TPM/HSM solutions
- [PROC-02] Key Storage Validation - Verify hardware protection mechanisms are functioning
- [PROC-03] Key Migration - Securely transfer keys between hardware protection devices
- [PROC-04] Hardware Failure Recovery - Restore keys from protected backup storage

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Hardware security incidents, new cryptographic requirements, technology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production Database Encryption]
IF system_type = "database"
AND environment = "production"
AND encryption_keys_present = TRUE
AND key_storage_type = "software"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Development Environment with Production Data]
IF environment = "development"
AND contains_production_data = TRUE
AND key_storage_mechanism = "TPM"
AND fips_certification = "Level_2"
THEN compliance = TRUE

[SCENARIO-03: Third-party Cloud Service]
IF service_type = "third_party_cloud"
AND handles_encrypted_data = TRUE
AND vendor_key_protection = "software_only"
AND no_equivalent_hardware_protection = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Mobile Device Key Storage]
IF device_type = "mobile"
AND accesses_corporate_encrypted_data = TRUE
AND secure_enclave_enabled = TRUE
AND hardware_backed_keystore = TRUE
THEN compliance = TRUE

[SCENARIO-05: Legacy System Exception]
IF system_age > 5_years
AND hardware_protection_unavailable = TRUE
AND compensating_controls_documented = FALSE
AND risk_acceptance_signed = FALSE
THEN compliance = FALSE
violation_severity = "Major"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Protected storage for cryptographic keys is provided using hardware mechanisms | RULE-01, RULE-03 |
| Keys are protected from unauthorized access and tampering | RULE-01, RULE-02 |
| Hardware protection mechanisms meet security standards | RULE-03 |
| Key storage activities are auditable | RULE-04 |
| Backup keys receive equivalent protection | RULE-05 |