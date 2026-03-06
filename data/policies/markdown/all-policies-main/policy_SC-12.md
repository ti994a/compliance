# POLICY: SC-12: Cryptographic Key Establishment and Management

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12 |
| NIST Control | SC-12: Cryptographic Key Establishment and Management |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, key management, key generation, key distribution, key storage, key destruction, trust stores, FIPS 140-2 |

## 1. POLICY STATEMENT
The organization SHALL establish and manage cryptographic keys used within information systems according to defined key management requirements covering the complete key lifecycle. All cryptographic key operations MUST comply with approved standards and organizational security requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems using any form of cryptography |
| Cloud Services | YES | Including hybrid and multi-cloud environments |
| Third-party Applications | YES | When integrated with organizational systems |
| Development/Test Systems | YES | Must follow same key management standards |
| Legacy Systems | CONDITIONAL | Must comply within 12 months or obtain exception |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve key management policies and procedures<br>• Oversee cryptographic key governance<br>• Ensure compliance with regulatory requirements |
| System Administrators | • Implement key management procedures<br>• Monitor key lifecycle events<br>• Maintain key management system configurations |
| Security Engineers | • Design key management architectures<br>• Validate cryptographic implementations<br>• Conduct key management assessments |

## 4. RULES

[RULE-01] All cryptographic keys MUST be generated using FIPS 140-2 Level 2 or higher validated cryptographic modules.
[VALIDATION] IF key_generation_method != "FIPS_140-2_L2_or_higher" THEN critical_violation

[RULE-02] Key distribution MUST occur through secure, authenticated channels with end-to-end encryption and integrity protection.
[VALIDATION] IF key_distribution_channel = "unencrypted" OR authentication = FALSE THEN critical_violation

[RULE-03] Cryptographic keys MUST be stored in hardware security modules (HSMs) or FIPS 140-2 Level 2+ validated key storage systems.
[VALIDATION] IF key_storage_location != "HSM" AND key_storage_validation < "FIPS_140-2_L2" THEN critical_violation

[RULE-04] Access to cryptographic keys MUST be restricted based on least privilege and role-based access controls with multi-factor authentication required.
[VALIDATION] IF key_access_control != "RBAC" OR mfa_required = FALSE THEN violation

[RULE-05] Cryptographic keys MUST be destroyed securely when no longer needed, with destruction verified and documented within 24 hours of expiration or revocation.
[VALIDATION] IF key_destruction_time > 24_hours OR destruction_verification = FALSE THEN violation

[RULE-06] Key management procedures MUST define specific requirements for key generation, distribution, storage, access, and destruction for each cryptographic use case.
[VALIDATION] IF key_mgmt_procedures_defined = FALSE OR use_case_requirements = "undefined" THEN violation

[RULE-07] Trust stores MUST contain only approved trust anchors and be reviewed quarterly for unauthorized certificates.
[VALIDATION] IF trust_store_review_frequency > 90_days OR unapproved_certificates > 0 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Key Generation Procedure - Defines approved algorithms, key lengths, and generation methods
- [PROC-02] Key Distribution Procedure - Specifies secure channels and authentication requirements
- [PROC-03] Key Storage Procedure - Details storage requirements and access controls
- [PROC-04] Key Destruction Procedure - Outlines secure deletion and verification processes
- [PROC-05] Trust Store Management Procedure - Governs certificate authority and trust anchor management

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving keys, regulatory changes, technology updates, failed audits

## 7. SCENARIO PATTERNS

[SCENARIO-01: Development Key in Production]
IF environment = "production"
AND key_type = "development" OR key_classification = "test"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Expired Key Still Active]
IF key_expiration_date < current_date
AND key_status = "active"
AND destruction_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unauthorized Key Access]
IF key_access_attempt = TRUE
AND user_authorization = FALSE
AND mfa_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Non-FIPS Key Generation]
IF key_generated = TRUE
AND generation_module_validation != "FIPS_140-2"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Unencrypted Key Distribution]
IF key_distribution = TRUE
AND channel_encryption = FALSE
AND internal_network = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic keys are established in accordance with defined requirements | RULE-01, RULE-06 |
| Cryptographic keys are managed in accordance with defined requirements | RULE-02, RULE-03, RULE-04, RULE-05 |
| Key generation requirements are defined and followed | RULE-01, RULE-06 |
| Key distribution requirements are defined and followed | RULE-02, RULE-06 |
| Key storage requirements are defined and followed | RULE-03, RULE-06 |
| Key access requirements are defined and followed | RULE-04, RULE-06 |
| Key destruction requirements are defined and followed | RULE-05, RULE-06 |
| Trust stores contain only approved trust anchors | RULE-07 |