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
The organization SHALL remove, mask, encrypt, hash, or replace direct identifiers in datasets containing personally identifiable information (PII) to protect individual privacy. All direct identifier processing MUST use approved cryptographic algorithms and key management practices consistent with organizational security standards.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All datasets containing PII | YES | Production, test, development environments |
| Third-party data processors | YES | When processing organizational data |
| Archived datasets | YES | Historical data retention requirements apply |
| Public datasets | CONDITIONAL | Only if containing direct identifiers |
| Encrypted data at rest | CONDITIONAL | If identifiers remain accessible |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Approve de-identification methods<br>• Oversee compliance monitoring<br>• Review dataset processing procedures |
| Data Stewards | • Implement approved de-identification techniques<br>• Maintain key management procedures<br>• Document processing activities |
| Security Team | • Validate cryptographic implementations<br>• Monitor automated de-identification tools<br>• Conduct technical compliance assessments |

## 4. RULES
[RULE-01] Direct identifiers in datasets MUST be processed using one of five approved methods: removal, masking, encryption, hashing, or replacement before use in non-production environments or sharing.
[VALIDATION] IF dataset_contains_direct_identifiers = TRUE AND processing_method NOT IN [removal, masking, encryption, hashing, replacement] THEN violation

[RULE-02] Encryption and hashing of direct identifiers MUST use FIPS 140-2 Level 2 validated algorithms with organizationally-approved key lengths (AES-256 minimum, SHA-256 minimum).
[VALIDATION] IF processing_method IN [encryption, hashing] AND (algorithm_fips_validated = FALSE OR key_length < minimum_required) THEN violation

[RULE-03] Each direct identifier type SHOULD use a unique encryption key to provide enhanced security and privacy protection.
[VALIDATION] IF processing_method = "encryption" AND unique_keys_per_identifier = FALSE THEN advisory_finding

[RULE-04] Masking implementations MUST completely obscure original identifier values and SHALL NOT use predictable patterns that enable reverse engineering.
[VALIDATION] IF processing_method = "masking" AND (original_data_recoverable = TRUE OR pattern_predictable = TRUE) THEN violation

[RULE-05] All de-identification processing activities MUST be documented including method used, algorithms employed, key management procedures, and retention periods.
[VALIDATION] IF de_identification_performed = TRUE AND documentation_complete = FALSE THEN violation

[RULE-06] Automated de-identification tools MUST be validated for accuracy and MUST NOT introduce data integrity issues during processing.
[VALIDATION] IF automated_tool_used = TRUE AND (validation_completed = FALSE OR integrity_issues_detected = TRUE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Direct Identifier Assessment - Systematic identification of direct identifiers in datasets
- [PROC-02] De-identification Method Selection - Risk-based selection of appropriate processing method
- [PROC-03] Cryptographic Key Management - Secure generation, storage, and rotation of encryption keys
- [PROC-04] Processing Validation - Verification of successful de-identification implementation
- [PROC-05] Documentation and Audit Trail - Comprehensive logging of all processing activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy incidents, regulatory changes, new data types, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Development Environment Data]
IF environment_type = "development"
AND dataset_contains_pii = TRUE
AND direct_identifiers_processed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Third-Party Data Sharing]
IF data_shared_externally = TRUE
AND direct_identifiers_present = TRUE
AND approved_processing_method_applied = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-03: Weak Cryptographic Implementation]
IF processing_method = "encryption"
AND algorithm_approved = FALSE
AND key_length < 256
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Masking with Recoverable Data]
IF processing_method = "masking"
AND original_values_determinable = TRUE
AND reverse_engineering_possible = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Undocumented Processing]
IF de_identification_performed = TRUE
AND processing_documentation = FALSE
AND audit_trail_missing = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Direct identifiers are removed, masked, encrypted, hashed, or replaced | RULE-01 |
| Cryptographic methods use approved algorithms | RULE-02 |
| Processing maintains data integrity | RULE-06 |
| Activities are properly documented | RULE-05 |
| Masking prevents data recovery | RULE-04 |