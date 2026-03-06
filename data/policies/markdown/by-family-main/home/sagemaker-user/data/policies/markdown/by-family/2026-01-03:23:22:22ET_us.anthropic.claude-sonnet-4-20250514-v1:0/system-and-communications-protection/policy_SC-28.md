# POLICY: SC-28: Protection of Information at Rest

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-28 |
| NIST Control | SC-28: Protection of Information at Rest |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | data at rest, encryption, confidentiality, integrity, storage protection, cryptographic controls |

## 1. POLICY STATEMENT
The organization SHALL protect the confidentiality and integrity of sensitive information when stored on system components including databases, hard drives, and storage devices. All information at rest requiring protection MUST be identified, classified, and secured using appropriate cryptographic or alternative protection mechanisms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All data storage systems | YES | Internal/external drives, databases, SAN devices |
| Cloud storage services | YES | Including hybrid and multi-cloud environments |
| Backup and archive systems | YES | Both online and offline storage |
| Mobile devices | YES | Laptops, tablets, removable media |
| Development/test systems | YES | When containing production data |
| Public/non-sensitive data | NO | Unless specifically classified as requiring protection |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Classify information requiring protection<br>• Define protection requirements<br>• Approve protection mechanisms |
| System Administrator | • Implement encryption controls<br>• Configure storage security settings<br>• Monitor protection mechanisms |
| CISO | • Define protection standards<br>• Approve cryptographic mechanisms<br>• Oversee compliance monitoring |

## 4. RULES
[RULE-01] All information classified as Confidential or higher MUST be encrypted at rest using FIPS 140-2 Level 2 or higher validated cryptographic modules.
[VALIDATION] IF data_classification IN ["Confidential", "Secret", "Top Secret"] AND encryption_status = FALSE THEN critical_violation

[RULE-02] Database systems containing PII, PHI, or financial data MUST implement Transparent Data Encryption (TDE) or equivalent database-level encryption.
[VALIDATION] IF database_contains_sensitive_data = TRUE AND database_encryption = FALSE THEN critical_violation

[RULE-03] Encryption keys for data at rest MUST be managed through approved key management systems and rotated at least annually.
[VALIDATION] IF key_age > 365_days OR key_management_system NOT IN approved_systems THEN major_violation

[RULE-04] System configuration files, authentication databases, and security rule sets MUST be protected with integrity controls including digital signatures or checksums.
[VALIDATION] IF system_config_file = TRUE AND integrity_protection = FALSE THEN major_violation

[RULE-05] When encryption is not feasible, alternative protection mechanisms MUST include WORM technology, secure offline storage, or continuous malware scanning.
[VALIDATION] IF encryption_feasible = FALSE AND alternative_protection = FALSE THEN major_violation

[RULE-06] All storage devices containing sensitive data MUST be inventoried and tracked with documented protection status.
[VALIDATION] IF device_contains_sensitive_data = TRUE AND (inventory_status = FALSE OR protection_documented = FALSE) THEN moderate_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Classification Procedure - Systematic identification and labeling of information requiring protection
- [PROC-02] Encryption Implementation Procedure - Standardized deployment of cryptographic controls for data at rest
- [PROC-03] Key Management Procedure - Lifecycle management of encryption keys including generation, rotation, and destruction
- [PROC-04] Storage Device Inventory Procedure - Regular discovery and cataloging of all storage devices and their protection status

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving data at rest, new storage technologies, regulatory changes, failed compliance audits

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unencrypted Database with PII]
IF database_type = "production"
AND contains_PII = TRUE
AND encryption_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Expired Encryption Keys]
IF data_encrypted = TRUE
AND key_age > 365_days
AND key_rotation_exception = FALSE
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-03: Cloud Storage Without Encryption]
IF storage_location = "cloud"
AND data_classification = "Confidential"
AND encryption_at_rest = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Backup System with Alternative Protection]
IF system_type = "backup"
AND encryption_feasible = FALSE
AND WORM_technology = TRUE
AND offline_storage = TRUE
THEN compliance = TRUE

[SCENARIO-05: Development System with Production Data]
IF environment = "development"
AND contains_production_data = TRUE
AND encryption_status = FALSE
AND data_classification IN ["Confidential", "Restricted"]
THEN compliance = FALSE
violation_severity = "Major"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information at rest requiring protection is defined | [RULE-06] |
| Confidentiality of defined information at rest is protected | [RULE-01], [RULE-02] |
| Integrity protections are implemented | [RULE-04] |
| Alternative protection mechanisms when encryption not feasible | [RULE-05] |
| Cryptographic key management controls | [RULE-03] |