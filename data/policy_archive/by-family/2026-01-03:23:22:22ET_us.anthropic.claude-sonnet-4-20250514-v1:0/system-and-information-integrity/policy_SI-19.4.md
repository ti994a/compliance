# POLICY: SI-19.4: Removal, Masking, Encryption, Hashing, or Replacement of Direct Identifiers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-19.4 |
| NIST Control | SI-19.4: Removal, Masking, Encryption, Hashing, or Replacement of Direct Identifiers |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | direct identifiers, masking, encryption, hashing, PII, de-identification, dataset |

## 1. POLICY STATEMENT
The organization SHALL remove, mask, encrypt, hash, or replace direct identifiers in datasets containing personally identifiable information (PII) to protect individual privacy. All direct identifier processing MUST use approved methods and maintain data utility requirements while ensuring adequate privacy protection.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All datasets containing PII | YES | Internal and external datasets |
| Production systems | YES | Systems processing PII |
| Development/test environments | YES | When using production PII |
| Third-party data processors | YES | Via contractual requirements |
| Public datasets | CONDITIONAL | If originally contained PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Approve de-identification methods<br>• Review risk assessments<br>• Validate compliance with privacy requirements |
| Data Stewards | • Implement approved de-identification techniques<br>• Document processing methods<br>• Maintain key management procedures |
| Security Team | • Provide cryptographic standards<br>• Validate encryption implementations<br>• Monitor de-identification tool security |

## 4. RULES
[RULE-01] Direct identifiers MUST be processed using one of five approved methods: removal, masking, encryption, hashing, or replacement before dataset use in non-production environments.
[VALIDATION] IF dataset_contains_direct_identifiers = TRUE AND environment != "production" AND de_identification_method NOT IN ["removal", "masking", "encryption", "hashing", "replacement"] THEN violation

[RULE-02] Encryption or hashing of direct identifiers MUST use FIPS 140-2 Level 2 validated algorithms with unique keys per identifier when maximum security is required.
[VALIDATION] IF de_identification_method IN ["encryption", "hashing"] AND security_level = "maximum" AND (algorithm_fips_validated = FALSE OR unique_keys_per_identifier = FALSE) THEN violation

[RULE-03] Masking implementations MUST replace all characters of direct identifiers with repeating characters and SHALL NOT preserve partial identifier information.
[VALIDATION] IF de_identification_method = "masking" AND (partial_identifier_preserved = TRUE OR masking_character_consistent = FALSE) THEN violation

[RULE-04] All de-identification processes MUST be documented with method selection justification, risk assessment, and data utility impact analysis.
[VALIDATION] IF de_identification_performed = TRUE AND (method_documented = FALSE OR risk_assessment_completed = FALSE OR utility_analysis_completed = FALSE) THEN violation

[RULE-05] Cryptographic keys used for identifier encryption or hashing MUST be managed according to SC-12 and SC-13 key management requirements.
[VALIDATION] IF de_identification_method IN ["encryption", "hashing"] AND key_management_compliant = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Direct Identifier Assessment - Systematic identification of direct identifiers in datasets
- [PROC-02] De-identification Method Selection - Risk-based selection of appropriate processing method
- [PROC-03] Cryptographic Key Management - Secure generation, storage, and rotation of de-identification keys
- [PROC-04] Data Utility Validation - Testing to ensure de-identified data meets business requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy incidents, new PII processing, regulatory changes, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Development Environment PII]
IF dataset_contains_direct_identifiers = TRUE
AND environment = "development"
AND de_identification_method = "none"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Proper Masking Implementation]
IF de_identification_method = "masking"
AND all_identifier_chars_replaced = TRUE
AND masking_character_consistent = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-03: Encryption with Weak Algorithm]
IF de_identification_method = "encryption"
AND algorithm_fips_validated = FALSE
AND dataset_sensitivity = "high"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Documentation]
IF de_identification_performed = TRUE
AND method_documented = TRUE
AND risk_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Key Reuse Across Identifiers]
IF de_identification_method = "encryption"
AND security_level = "maximum"
AND unique_keys_per_identifier = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Direct identifiers are removed, masked, encrypted, hashed, or replaced | RULE-01, RULE-02, RULE-03 |
| Approved cryptographic methods are used | RULE-02, RULE-05 |
| De-identification processes are documented | RULE-04 |
| Key management requirements are followed | RULE-05 |