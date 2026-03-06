# POLICY: SC-13: Cryptographic Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-13 |
| NIST Control | SC-13: Cryptographic Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptography, encryption, FIPS, NSA-approved, digital signatures, hash generation, classified information |

## 1. POLICY STATEMENT
The organization SHALL determine and document all cryptographic uses within information systems and implement appropriate types of cryptography for each specified use. All cryptographic implementations MUST comply with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines including FIPS-validated and NSA-approved cryptography where required.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| Third-party Applications | YES | Must meet cryptographic requirements |
| Mobile Devices | YES | Company-owned and BYOD with company data |
| Development Environments | YES | Must use approved cryptography |
| Legacy Systems | CONDITIONAL | Exemptions require documented risk acceptance |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve cryptographic standards and policies<br>• Review and approve cryptographic use cases<br>• Ensure compliance with regulatory requirements |
| Security Architecture Team | • Define approved cryptographic algorithms and implementations<br>• Review system designs for cryptographic compliance<br>• Maintain cryptographic standards documentation |
| System Owners | • Document cryptographic uses in their systems<br>• Implement required cryptographic controls<br>• Ensure ongoing compliance monitoring |
| Development Teams | • Implement FIPS-validated cryptography in applications<br>• Follow secure coding practices for cryptographic functions<br>• Conduct cryptographic testing and validation |

## 4. RULES

[RULE-01] All cryptographic uses within information systems MUST be documented and maintained in the system security plan.
[VALIDATION] IF system_has_crypto = TRUE AND crypto_uses_documented = FALSE THEN violation

[RULE-02] Systems processing classified information MUST use NSA-approved cryptographic algorithms and implementations.
[VALIDATION] IF data_classification = "classified" AND crypto_type != "NSA_approved" THEN critical_violation

[RULE-03] Digital signature implementations MUST use FIPS 140-2 validated cryptographic modules.
[VALIDATION] IF digital_signatures_used = TRUE AND fips_validated = FALSE THEN violation

[RULE-04] Cryptographic key generation MUST use FIPS-approved random number generators.
[VALIDATION] IF key_generation = TRUE AND rng_type != "FIPS_approved" THEN violation

[RULE-05] Hash functions MUST use SHA-2 or SHA-3 family algorithms; MD5 and SHA-1 are prohibited for security purposes.
[VALIDATION] IF hash_algorithm IN ["MD5", "SHA-1"] AND use_case = "security" THEN violation

[RULE-06] Symmetric encryption MUST use AES with minimum 128-bit key length for unclassified data and 256-bit for sensitive data.
[VALIDATION] IF encryption_type = "symmetric" AND key_length < 128 THEN violation
[VALIDATION] IF data_sensitivity = "high" AND encryption_type = "symmetric" AND key_length < 256 THEN violation

[RULE-07] All cryptographic implementations MUST be reviewed and approved by the Security Architecture Team before deployment.
[VALIDATION] IF crypto_implementation = TRUE AND security_approval = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cryptographic Use Case Documentation - Process for identifying and documenting all cryptographic uses
- [PROC-02] Cryptographic Algorithm Approval - Procedure for reviewing and approving cryptographic implementations
- [PROC-03] FIPS Validation Verification - Process for verifying FIPS 140-2 validation certificates
- [PROC-04] Cryptographic Compliance Assessment - Regular assessment of cryptographic implementations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New regulatory requirements, cryptographic vulnerabilities, algorithm deprecation, security incidents involving cryptography

## 7. SCENARIO PATTERNS

[SCENARIO-01: Legacy System with Weak Encryption]
IF system_age > 5_years
AND encryption_algorithm = "3DES"
AND data_sensitivity = "high"
AND migration_plan = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Development Team Using Custom Crypto]
IF development_phase = TRUE
AND crypto_implementation = "custom"
AND security_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Cloud Service with Compliant Encryption]
IF deployment_type = "cloud"
AND encryption_algorithm = "AES-256"
AND fips_validated = TRUE
AND crypto_uses_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Classified Data with Wrong Crypto Type]
IF data_classification = "classified"
AND crypto_type = "FIPS_validated"
AND crypto_type != "NSA_approved"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Hash Function for Digital Signatures]
IF use_case = "digital_signatures"
AND hash_algorithm = "SHA-256"
AND fips_validated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic uses are defined and identified | [RULE-01] |
| Types of cryptography for each use are defined | [RULE-02], [RULE-03], [RULE-05], [RULE-06] |
| Required cryptography is implemented for each use | [RULE-04], [RULE-07] |
| FIPS-validated cryptography for digital signatures | [RULE-03] |
| NSA-approved cryptography for classified information | [RULE-02] |
| Approved algorithms and key lengths | [RULE-05], [RULE-06] |