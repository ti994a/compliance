# POLICY: SC-12.2: Symmetric Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12.2 |
| NIST Control | SC-12.2: Symmetric Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | symmetric keys, cryptographic keys, FIPS validation, key management, key distribution, key production |

## 1. POLICY STATEMENT
All symmetric cryptographic keys used within organizational systems MUST be produced, controlled, and distributed exclusively using NIST FIPS-validated key management technology and processes. Non-FIPS validated key management solutions are prohibited for symmetric key operations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, on-premises, and hybrid environments |
| Cryptographic Applications | YES | Any application performing symmetric encryption |
| Third-Party Services | YES | Must demonstrate FIPS validation for key operations |
| Development/Test Systems | CONDITIONAL | When processing regulated data or production keys |
| Network Infrastructure | YES | VPNs, network encryption devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Cryptographic Officer | • Validate FIPS compliance of key management systems<br>• Approve cryptographic key management procedures<br>• Maintain inventory of FIPS-validated products |
| System Administrators | • Implement FIPS-validated key management solutions<br>• Configure systems according to approved procedures<br>• Monitor key management operations |
| Security Engineers | • Design cryptographic architectures using FIPS-validated components<br>• Conduct security assessments of key management systems<br>• Document key management processes |

## 4. RULES
[RULE-01] Symmetric cryptographic key production MUST use only NIST FIPS 140-2 Level 2 or higher validated key generation modules.
[VALIDATION] IF key_generation_module_fips_level < 2 THEN critical_violation

[RULE-02] Key management systems SHALL maintain current FIPS 140-2 validation certificates and MUST NOT operate with expired validations.
[VALIDATION] IF fips_certificate_status = "expired" OR fips_certificate_status = "revoked" THEN critical_violation

[RULE-03] Symmetric key distribution MUST occur through FIPS-validated cryptographic protocols with authenticated key establishment.
[VALIDATION] IF key_distribution_protocol_fips_validated = FALSE THEN violation

[RULE-04] Key storage containers MUST be FIPS 140-2 Level 3 or higher validated hardware security modules for production environments.
[VALIDATION] IF environment = "production" AND key_storage_fips_level < 3 THEN violation

[RULE-05] All symmetric key operations SHALL be logged with tamper-evident audit trails including key lifecycle events.
[VALIDATION] IF key_operation_logged = FALSE OR audit_trail_integrity = "compromised" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] FIPS Validation Verification - Quarterly verification of FIPS certificate validity
- [PROC-02] Key Lifecycle Management - Standardized procedures for key generation, distribution, storage, and destruction
- [PROC-03] Cryptographic Module Assessment - Annual assessment of FIPS-validated components
- [PROC-04] Key Recovery Operations - Secure key recovery using FIPS-validated processes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: FIPS certificate expiration, security incidents involving keys, new cryptographic implementations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Non-FIPS Key Generation]
IF key_type = "symmetric"
AND key_generation_method = "software_random"
AND fips_validation_status = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Expired FIPS Certificate]
IF cryptographic_module_in_use = TRUE
AND fips_certificate_expiry_date < current_date
AND production_environment = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Cloud HSM Key Management]
IF deployment_type = "cloud"
AND key_management_service = "cloud_hsm"
AND fips_140_2_level >= 3
AND certificate_status = "valid"
THEN compliance = TRUE

[SCENARIO-04: Development Environment Exception]
IF environment = "development"
AND data_classification = "public"
AND production_key_access = FALSE
AND fips_validation = FALSE
THEN compliance = TRUE

[SCENARIO-05: Key Distribution Protocol]
IF key_distribution_in_progress = TRUE
AND transport_protocol = "TLS"
AND tls_fips_validated = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Symmetric cryptographic keys are produced using NIST FIPS-validated key management technology and processes | [RULE-01], [RULE-02] |
| Symmetric cryptographic keys are controlled using NIST FIPS-validated key management technology and processes | [RULE-02], [RULE-04], [RULE-05] |
| Symmetric cryptographic keys are distributed using NIST FIPS-validated key management technology and processes | [RULE-03], [RULE-05] |