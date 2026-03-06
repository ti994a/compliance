# POLICY: SC-28.1: Cryptographic Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-28.1 |
| NIST Control | SC-28.1: Cryptographic Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptography, encryption, data at rest, confidentiality, integrity, unauthorized disclosure, unauthorized modification |

## 1. POLICY STATEMENT
The organization MUST implement cryptographic mechanisms to prevent unauthorized disclosure and modification of information at rest on system components and media. Cryptographic strength MUST be commensurate with the security category and classification of the protected information.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid environments |
| Storage media | YES | Physical and virtual storage containing sensitive data |
| Database systems | YES | All databases storing regulated or sensitive information |
| Backup systems | YES | All backup and archive storage |
| Mobile devices | YES | Laptops, tablets, smartphones with organizational data |
| Removable media | YES | USB drives, external drives, optical media |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define cryptographic protection requirements<br>• Approve cryptographic standards and algorithms<br>• Oversee compliance monitoring |
| System Administrators | • Implement encryption on assigned systems<br>• Maintain cryptographic configurations<br>• Monitor encryption status and alerts |
| Data Owners | • Classify data requiring cryptographic protection<br>• Define access requirements for encrypted data<br>• Validate encryption coverage for their data |

## 4. RULES
[RULE-01] All data classified as Confidential or above MUST be encrypted at rest using FIPS 140-2 Level 2 validated cryptographic modules.
[VALIDATION] IF data_classification IN ["Confidential", "Secret", "Top Secret"] AND encryption_status = FALSE THEN critical_violation

[RULE-02] Database systems containing PII, PHI, or payment card data MUST implement transparent data encryption (TDE) or equivalent database-level encryption.
[VALIDATION] IF database_contains_regulated_data = TRUE AND database_encryption = FALSE THEN critical_violation

[RULE-03] Encryption algorithms MUST use AES-256 or approved equivalent with key lengths meeting current NIST recommendations.
[VALIDATION] IF encryption_algorithm NOT IN approved_algorithms OR key_length < minimum_required_length THEN violation

[RULE-04] Cryptographic keys MUST be managed through approved key management systems and rotated according to established schedules.
[VALIDATION] IF key_age > rotation_schedule AND exception_approved = FALSE THEN violation

[RULE-05] Mobile devices and removable media containing organizational data MUST use full-disk encryption or equivalent protection.
[VALIDATION] IF device_type IN ["mobile", "removable_media"] AND full_disk_encryption = FALSE THEN violation

[RULE-06] Backup and archive systems MUST encrypt data using the same or stronger cryptographic protection as the source systems.
[VALIDATION] IF backup_encryption_strength < source_encryption_strength THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Classification Procedure - Systematic process for identifying data requiring cryptographic protection
- [PROC-02] Cryptographic Implementation Procedure - Step-by-step process for deploying encryption solutions
- [PROC-03] Key Management Procedure - Processes for key generation, distribution, rotation, and destruction
- [PROC-04] Encryption Monitoring Procedure - Continuous monitoring of encryption status and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when cryptographic standards change
- Triggering events: Security incidents involving encrypted data, regulatory changes, technology refresh cycles

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unencrypted Confidential Database]
IF data_classification = "Confidential"
AND system_type = "database"
AND encryption_at_rest = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Weak Encryption Algorithm]
IF encryption_enabled = TRUE
AND algorithm = "AES-128"
AND data_classification = "Secret"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Mobile Device Without Encryption]
IF device_type = "laptop"
AND contains_organizational_data = TRUE
AND full_disk_encryption = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Compliant Encrypted System]
IF data_classification = "Confidential"
AND encryption_algorithm = "AES-256"
AND fips_140_2_validated = TRUE
AND key_management_compliant = TRUE
THEN compliance = TRUE

[SCENARIO-05: Backup Encryption Gap]
IF system_type = "backup"
AND source_encrypted = TRUE
AND backup_encrypted = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic mechanisms prevent unauthorized disclosure of defined information at rest | [RULE-01], [RULE-02], [RULE-05] |
| Cryptographic mechanisms prevent unauthorized modification of defined information at rest | [RULE-01], [RULE-02], [RULE-06] |
| Appropriate cryptographic strength based on information classification | [RULE-03], [RULE-04] |
| Comprehensive coverage of system components and media | [RULE-05], [RULE-06] |