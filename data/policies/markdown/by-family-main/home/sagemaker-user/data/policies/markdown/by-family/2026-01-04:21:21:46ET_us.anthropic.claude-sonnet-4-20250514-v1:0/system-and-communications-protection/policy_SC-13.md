# POLICY: SC-13: Cryptographic Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-13 |
| NIST Control | SC-13: Cryptographic Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptography, FIPS, NSA-approved, encryption, digital signatures, key management |

## 1. POLICY STATEMENT
The organization SHALL define all cryptographic uses within information systems and implement appropriate types of cryptography for each specified use case. All cryptographic implementations MUST comply with FIPS-validated or NSA-approved cryptographic standards as applicable to the data classification and regulatory requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, on-premises, and hybrid |
| Third-party Applications | YES | When processing organizational data |
| Mobile Devices | YES | When accessing corporate resources |
| Development Environments | YES | When handling production-like data |
| Test Systems | CONDITIONAL | Only when using production data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve cryptographic standards and use cases<br>• Oversee compliance with regulatory requirements<br>• Review and approve exceptions |
| Security Architecture Team | • Define approved cryptographic algorithms and implementations<br>• Validate cryptographic use case definitions<br>• Assess cryptographic module compliance |
| System Owners | • Implement required cryptography for their systems<br>• Document cryptographic use cases<br>• Maintain cryptographic module inventories |
| Development Teams | • Integrate approved cryptographic libraries<br>• Follow secure coding practices for cryptographic implementations<br>• Obtain security review for cryptographic implementations |

## 4. RULES
[RULE-01] All cryptographic use cases within organizational systems MUST be formally defined and documented in the system security plan.
[VALIDATION] IF system_has_cryptography = TRUE AND cryptographic_uses_documented = FALSE THEN violation

[RULE-02] Cryptographic modules used for FISMA systems MUST be FIPS 140-2 Level 1 or higher validated.
[VALIDATION] IF system_type = "FISMA" AND cryptographic_module_fips_validated = FALSE THEN critical_violation

[RULE-03] Classified information processing systems MUST use NSA-approved cryptographic algorithms and implementations.
[VALIDATION] IF data_classification = "classified" AND cryptography_nsa_approved = FALSE THEN critical_violation

[RULE-04] Digital signature implementations MUST use FIPS-validated cryptographic modules.
[VALIDATION] IF cryptographic_use = "digital_signatures" AND fips_validated = FALSE THEN violation

[RULE-05] Cryptographic implementations MUST NOT use deprecated or weak algorithms including DES, MD5, SHA-1 for new implementations.
[VALIDATION] IF cryptographic_algorithm IN ["DES", "MD5", "SHA-1"] AND implementation_date > "2023-01-01" THEN violation

[RULE-06] Random number generation for cryptographic purposes MUST use cryptographically secure pseudorandom number generators (CSPRNG).
[VALIDATION] IF cryptographic_use = "random_generation" AND csprng_used = FALSE THEN violation

[RULE-07] All cryptographic modules MUST be inventoried and tracked with validation certificates maintained.
[VALIDATION] IF cryptographic_module_deployed = TRUE AND validation_certificate_maintained = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cryptographic Use Case Definition - Process for identifying and documenting cryptographic requirements
- [PROC-02] Cryptographic Module Validation - Verification of FIPS/NSA approval status
- [PROC-03] Cryptographic Implementation Review - Security assessment of cryptographic implementations
- [PROC-04] Cryptographic Inventory Management - Tracking and maintenance of cryptographic modules

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New regulatory requirements, cryptographic standard updates, security incidents involving cryptography

## 7. SCENARIO PATTERNS
[SCENARIO-01: FIPS Validation Required]
IF system_type = "FedRAMP" OR system_type = "FISMA"
AND cryptographic_modules_present = TRUE
AND fips_140_2_validated = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Deprecated Algorithm Usage]
IF cryptographic_algorithm = "SHA-1"
AND implementation_date > "2023-01-01"
AND use_case != "legacy_verification_only"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Undocumented Cryptographic Use]
IF application_uses_encryption = TRUE
AND cryptographic_use_cases_documented = FALSE
AND system_security_plan_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: NSA Approval for Classified Data]
IF data_classification = "SECRET" OR data_classification = "TOP_SECRET"
AND cryptographic_protection_enabled = TRUE
AND nsa_approved_cryptography = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Third-party Cryptographic Module]
IF cryptographic_module_source = "third_party"
AND validation_certificate_verified = TRUE
AND approved_cryptographic_standards_met = TRUE
AND inventory_updated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic uses are defined | RULE-01 |
| Types of cryptography for each use are defined | RULE-01, RULE-02, RULE-03 |
| Required cryptography is implemented | RULE-02, RULE-03, RULE-04, RULE-05 |
| FIPS-validated cryptography compliance | RULE-02, RULE-04 |
| NSA-approved cryptography for classified systems | RULE-03 |
| Cryptographic module inventory maintenance | RULE-07 |