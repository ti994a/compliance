```markdown
# POLICY: SC-28.1: Cryptographic Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-28.1 |
| NIST Control | SC-28.1: Cryptographic Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | encryption, cryptography, data-at-rest, confidentiality, integrity, unauthorized-disclosure, unauthorized-modification |

## 1. POLICY STATEMENT
All information requiring cryptographic protection must be encrypted at rest using approved cryptographic mechanisms to prevent unauthorized disclosure and modification. The strength of cryptographic mechanisms must be commensurate with the security category or classification of the protected information.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Components | YES | All servers, workstations, mobile devices storing protected data |
| Storage Media | YES | Hard drives, SSDs, removable media, backup tapes |
| Cloud Storage | YES | All cloud-based storage containing organizational data |
| Database Systems | YES | Production, development, and test databases with protected data |
| File Shares | YES | Network attached storage and shared drives |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Classify data requiring cryptographic protection<br>• Define encryption requirements for their data<br>• Approve encryption implementation methods |
| System Administrator | • Implement approved cryptographic mechanisms<br>• Configure encryption on system components and media<br>• Monitor encryption status and compliance |
| CISO | • Approve cryptographic standards and mechanisms<br>• Define organizational encryption policy<br>• Oversee compliance monitoring and reporting |

## 4. RULES
[RULE-01] All data classified as Confidential, Restricted, or higher MUST be encrypted at rest using FIPS 140-2 Level 2 or higher validated cryptographic modules.
[VALIDATION] IF data_classification IN ["Confidential", "Restricted", "Secret"] AND encryption_at_rest = FALSE THEN critical_violation

[RULE-02] Database systems containing PII, PHI, financial data, or intellectual property MUST implement transparent data encryption (TDE) or equivalent database-level encryption.
[VALIDATION] IF database_contains_sensitive_data = TRUE AND database_encryption = FALSE THEN critical_violation

[RULE-03] All laptops, mobile devices, and removable media capable of storing organizational data MUST use full-disk encryption with AES-256 or equivalent approved algorithm.
[VALIDATION] IF device_type IN ["laptop", "mobile", "removable_media"] AND full_disk_encryption = FALSE THEN critical_violation

[RULE-04] Encryption keys MUST be managed through an approved key management system and SHALL NOT be stored on the same system or media as the encrypted data.
[VALIDATION] IF encryption_keys_location = encrypted_data_location THEN critical_violation

[RULE-05] Cloud storage containing organizational data MUST use customer-managed encryption keys (CMEK) or customer-supplied encryption keys (CSEK) where available.
[VALIDATION] IF cloud_storage = TRUE AND key_management = "provider_managed" AND cmek_available = TRUE THEN violation

[RULE-06] Backup media and archived data MUST be encrypted using the same or stronger cryptographic protection as the original data.
[VALIDATION] IF backup_encryption_strength < original_data_encryption_strength THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Classification and Encryption Requirements Assessment - Systematic review to identify data requiring cryptographic protection
- [PROC-02] Cryptographic Implementation Standards - Technical specifications for approved encryption algorithms and key lengths
- [PROC-03] Key Management Lifecycle - Procedures for key generation, distribution, rotation, and destruction
- [PROC-04] Encryption Compliance Monitoring - Regular verification of encryption status across all systems and media

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New regulatory requirements, cryptographic vulnerabilities, technology changes, data breach incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unencrypted Sensitive Database]
IF database_contains_pii = TRUE
AND database_encryption = FALSE
AND data_classification = "Confidential"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Weak Encryption Algorithm]
IF encryption_algorithm = "DES"
AND data_classification = "Restricted"
AND fips_140_2_validated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Co-located Keys and Data]
IF encryption_enabled = TRUE
AND key_storage_location = data_storage_location
AND separation_implemented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Unencrypted Cloud Backup]
IF storage_type = "cloud_backup"
AND contains_organizational_data = TRUE
AND encryption_at_rest = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Mobile Device Without Full Disk Encryption]
IF device_type = "laptop"
AND contains_confidential_data = TRUE
AND full_disk_encryption = FALSE
AND approved_exception = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic mechanisms prevent unauthorized disclosure of defined information at rest | [RULE-01], [RULE-02], [RULE-03] |
| Cryptographic mechanisms prevent unauthorized modification of defined information at rest | [RULE-01], [RULE-02], [RULE-06] |
| Information requiring cryptographic protection is properly defined and classified | [RULE-01], [RULE-02] |
| Appropriate cryptographic strength based on information classification | [RULE-01], [RULE-05] |
```