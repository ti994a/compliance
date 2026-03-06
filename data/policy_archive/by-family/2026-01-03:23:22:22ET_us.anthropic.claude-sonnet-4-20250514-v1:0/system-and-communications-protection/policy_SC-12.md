# POLICY: SC-12: Cryptographic Key Establishment and Management

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12 |
| NIST Control | SC-12: Cryptographic Key Establishment and Management |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, key management, key generation, key distribution, key storage, key destruction, encryption, trust stores |

## 1. POLICY STATEMENT
The organization SHALL establish and manage cryptographic keys throughout their lifecycle when cryptography is employed within systems. All cryptographic key management activities MUST comply with defined requirements for key generation, distribution, storage, access, and destruction.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Systems using any form of cryptography |
| Cloud services | YES | Including hybrid and multi-cloud environments |
| Third-party integrations | YES | When cryptographic keys are shared or managed |
| Development environments | YES | Must follow same key management standards |
| Legacy systems | CONDITIONAL | Must comply within 180 days or obtain exception |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Cryptographic Officer | • Define key management requirements<br>• Approve cryptographic algorithms and modules<br>• Oversee trust store management |
| System Administrators | • Implement key management procedures<br>• Monitor key lifecycle events<br>• Maintain key management systems |
| Security Team | • Audit key management practices<br>• Validate compliance with requirements<br>• Investigate key-related incidents |

## 4. RULES

[RULE-01] All cryptographic keys MUST be generated using FIPS 140-2 Level 2 or higher validated cryptographic modules.
[VALIDATION] IF key_generation_module != "FIPS_140-2_L2+" THEN critical_violation

[RULE-02] Key generation MUST use approved random number generators with sufficient entropy as defined in NIST SP 800-90A.
[VALIDATION] IF entropy_source != "NIST_SP_800-90A_approved" THEN critical_violation

[RULE-03] Cryptographic keys MUST be distributed using secure channels with authentication and integrity protection.
[VALIDATION] IF key_distribution_channel != "secure_authenticated" THEN violation

[RULE-04] All cryptographic keys MUST be stored in hardware security modules (HSMs) or FIPS 140-2 Level 2+ validated storage.
[VALIDATION] IF key_storage_location != "HSM" AND key_storage_validation != "FIPS_140-2_L2+" THEN critical_violation

[RULE-05] Access to cryptographic keys MUST be restricted to authorized personnel with documented business justification.
[VALIDATION] IF key_access_granted = TRUE AND authorization_documented = FALSE THEN violation

[RULE-06] Cryptographic keys MUST be destroyed using NIST SP 800-88 approved methods when no longer needed.
[VALIDATION] IF key_destruction_method != "NIST_SP_800-88_approved" THEN violation

[RULE-07] Key rotation MUST occur according to defined schedules: encryption keys every 12 months, signing keys every 24 months.
[VALIDATION] IF key_type = "encryption" AND key_age > 12_months THEN violation
[VALIDATION] IF key_type = "signing" AND key_age > 24_months THEN violation

[RULE-08] Trust stores MUST contain only approved trust anchors and be reviewed quarterly.
[VALIDATION] IF trust_anchor_approved = FALSE THEN critical_violation
[VALIDATION] IF trust_store_review_date > 90_days THEN violation

[RULE-09] All key management activities MUST be logged with tamper-evident audit trails.
[VALIDATION] IF key_activity_logged = FALSE OR audit_trail_integrity != "protected" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Key Generation Procedure - Standardized process for generating cryptographic keys using approved methods
- [PROC-02] Key Distribution Procedure - Secure methods for distributing keys to authorized systems and personnel  
- [PROC-03] Key Storage and Access Control Procedure - Controls for storing and accessing cryptographic keys
- [PROC-04] Key Rotation and Renewal Procedure - Scheduled replacement of cryptographic keys
- [PROC-05] Key Destruction Procedure - Secure deletion and destruction of cryptographic keys
- [PROC-06] Trust Store Management Procedure - Management of certificate trust stores and trust anchors

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents involving keys, regulatory changes, technology updates, failed audits

## 7. SCENARIO PATTERNS

[SCENARIO-01: Expired Encryption Key Usage]
IF key_type = "encryption"
AND key_expiration_date < current_date
AND key_status = "active"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unauthorized Key Access]
IF key_access_granted = TRUE
AND user_authorization = FALSE
AND access_logged = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Non-FIPS Key Storage]
IF cryptographic_key_exists = TRUE
AND storage_location != "HSM"
AND storage_validation != "FIPS_140-2_L2+"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Improper Key Distribution]
IF key_distribution_occurred = TRUE
AND distribution_channel_encrypted = FALSE
AND distribution_authenticated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Unapproved Trust Anchor]
IF trust_anchor_in_store = TRUE
AND trust_anchor_approved = FALSE
AND discovery_date < 30_days_ago
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic keys are established in accordance with defined requirements | [RULE-01], [RULE-02] |
| Cryptographic keys are managed in accordance with defined requirements | [RULE-03], [RULE-04], [RULE-05] |
| Key generation requirements are defined and followed | [RULE-01], [RULE-02] |
| Key distribution requirements are defined and followed | [RULE-03] |
| Key storage requirements are defined and followed | [RULE-04] |
| Key access requirements are defined and followed | [RULE-05] |
| Key destruction requirements are defined and followed | [RULE-06] |