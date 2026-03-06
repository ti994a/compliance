# POLICY: SI-19.4: Removal, Masking, Encryption, Hashing, or Replacement of Direct Identifiers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-19.4 |
| NIST Control | SI-19.4: Removal, Masking, Encryption, Hashing, or Replacement of Direct Identifiers |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | direct identifiers, masking, encryption, hashing, de-identification, PII, dataset protection |

## 1. POLICY STATEMENT
All datasets containing direct identifiers MUST undergo removal, masking, encryption, hashing, or replacement processes before use in non-production environments or sharing with third parties. Direct identifier protection methods SHALL be implemented using approved cryptographic standards and documented procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production datasets with PII | YES | All datasets containing direct identifiers |
| Non-production environments | YES | Must use de-identified data only |
| Third-party data sharing | YES | Requires de-identification before transfer |
| Internal analytics datasets | YES | Unless explicit authorization exists |
| Backup and archive systems | YES | Historical data must be protected |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Approve de-identification methods<br>• Review and validate de-identification procedures<br>• Monitor compliance with identifier protection requirements |
| Data Engineers | • Implement de-identification processes<br>• Maintain cryptographic keys and algorithms<br>• Document de-identification activities |
| Security Team | • Validate cryptographic implementations<br>• Review de-identification tools and methods<br>• Assess security of key management |

## 4. RULES
[RULE-01] Direct identifiers in datasets MUST be removed, masked, encrypted, hashed, or replaced before use in non-production environments or external sharing.
[VALIDATION] IF dataset_contains_direct_identifiers = TRUE AND environment != "production" AND de_identification_applied = FALSE THEN violation

[RULE-02] Cryptographic methods for identifier protection SHALL use FIPS 140-2 approved algorithms including AES for encryption and HMAC for hashing.
[VALIDATION] IF de_identification_method IN ["encryption", "hashing"] AND algorithm_fips_approved = FALSE THEN violation

[RULE-03] Each direct identifier type SHOULD use a unique cryptographic key to provide enhanced security and privacy protection.
[VALIDATION] IF de_identification_method IN ["encryption", "hashing"] AND unique_keys_per_identifier = FALSE THEN advisory_finding

[RULE-04] De-identification procedures MUST be documented and include the specific method used, tools employed, and validation steps performed.
[VALIDATION] IF de_identification_performed = TRUE AND documentation_complete = FALSE THEN violation

[RULE-05] Masking implementations MUST ensure complete replacement of identifier values with approved character patterns or surrogate values.
[VALIDATION] IF de_identification_method = "masking" AND original_data_recoverable = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Direct Identifier Classification - Systematic identification and cataloging of direct identifiers in datasets
- [PROC-02] De-identification Method Selection - Process for choosing appropriate protection method based on data sensitivity and use case
- [PROC-03] Cryptographic Key Management - Secure generation, storage, and lifecycle management of de-identification keys
- [PROC-04] De-identification Validation - Testing and verification that direct identifiers are properly protected

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Data breach incidents, new PII processing activities, regulatory changes, cryptographic standard updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Non-Production Database Copy]
IF dataset_contains_pii = TRUE
AND environment = "development"
AND direct_identifiers_protected = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Third-Party Analytics Sharing]
IF data_sharing_external = TRUE
AND de_identification_method IN ["encryption", "hashing", "masking", "replacement"]
AND fips_approved_algorithm = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-03: Inadequate Masking Implementation]
IF de_identification_method = "masking"
AND masked_pattern = "XXX"
AND original_length_preserved = TRUE
AND pattern_allows_inference = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Key Reuse Across Identifiers]
IF de_identification_method = "encryption"
AND same_key_multiple_identifiers = TRUE
AND data_sensitivity = "high"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Undocumented De-identification]
IF de_identification_performed = TRUE
AND method_documented = FALSE
AND validation_recorded = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Direct identifiers are removed, masked, encrypted, hashed, or replaced | RULE-01, RULE-05 |
| Approved cryptographic methods are used | RULE-02 |
| De-identification processes are documented | RULE-04 |
| Enhanced security through unique keys | RULE-03 |