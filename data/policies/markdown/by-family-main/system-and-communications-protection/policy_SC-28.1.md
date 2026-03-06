# POLICY: SC-28.1: Cryptographic Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-28.1 |
| NIST Control | SC-28.1: Cryptographic Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptography, encryption, data at rest, confidentiality, integrity, unauthorized disclosure |

## 1. POLICY STATEMENT
The organization SHALL implement cryptographic mechanisms to prevent unauthorized disclosure and modification of sensitive information at rest on system components and media. Cryptographic protection MUST be applied to all data classified as confidential, restricted, or requiring regulatory compliance protection when stored on any organizational system or removable media.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing sensitive data |
| Development Systems | YES | When containing production data copies |
| Database Servers | YES | All databases with sensitive information |
| File Servers | YES | All shared storage systems |
| Backup Media | YES | All backup tapes, disks, and cloud storage |
| Mobile Devices | YES | Laptops, tablets accessing corporate data |
| Removable Media | YES | USB drives, external drives, optical media |
| Test Systems | CONDITIONAL | Only if containing sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Define data classification levels<br>• Approve cryptographic requirements<br>• Review access controls quarterly |
| System Administrator | • Implement encryption solutions<br>• Maintain cryptographic configurations<br>• Monitor encryption status |
| Security Team | • Define encryption standards<br>• Validate implementation<br>• Conduct compliance assessments |

## 4. RULES
[RULE-01] All data classified as Confidential or Restricted MUST be encrypted at rest using FIPS 140-2 Level 2 validated cryptographic modules with AES-256 or approved equivalent algorithms.
[VALIDATION] IF data_classification IN ["confidential", "restricted"] AND encryption_status = FALSE THEN critical_violation

[RULE-02] Database encryption MUST use Transparent Data Encryption (TDE) or equivalent database-native encryption for all production databases containing sensitive information.
[VALIDATION] IF system_type = "database" AND contains_sensitive_data = TRUE AND tde_enabled = FALSE THEN violation

[RULE-03] Full disk encryption MUST be enabled on all laptops, mobile devices, and removable media using approved encryption solutions before deployment.
[VALIDATION] IF device_type IN ["laptop", "mobile", "removable_media"] AND full_disk_encryption = FALSE THEN critical_violation

[RULE-04] Encryption key management MUST follow organizational key management procedures with keys stored separately from encrypted data and rotated according to established schedules.
[VALIDATION] IF encryption_enabled = TRUE AND (key_separation = FALSE OR key_rotation_overdue = TRUE) THEN violation

[RULE-05] Cloud storage containing organizational data MUST use server-side encryption with customer-managed keys (SSE-C) or equivalent customer-controlled encryption.
[VALIDATION] IF storage_location = "cloud" AND (server_side_encryption = FALSE OR customer_managed_keys = FALSE) THEN violation

[RULE-06] Backup media encryption MUST be verified before offsite storage and tested during quarterly restore procedures.
[VALIDATION] IF media_type = "backup" AND (encryption_verified = FALSE OR quarterly_test_passed = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Classification Procedure - Systematic process for identifying and labeling sensitive data
- [PROC-02] Encryption Implementation Procedure - Standard process for deploying cryptographic controls
- [PROC-03] Key Management Procedure - Comprehensive key lifecycle management process
- [PROC-04] Encryption Monitoring Procedure - Continuous monitoring of encryption status and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, regulatory changes, technology updates, failed compliance assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unencrypted Production Database]
IF system_type = "database"
AND environment = "production"
AND contains_pii = TRUE
AND encryption_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Mobile Device Without Encryption]
IF device_type = "laptop"
AND corporate_access = TRUE
AND full_disk_encryption = FALSE
AND device_deployed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Cloud Storage with Provider Keys]
IF storage_type = "cloud"
AND data_classification = "confidential"
AND encryption_enabled = TRUE
AND key_management = "provider_managed"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Backup Media Encryption Compliance]
IF media_type = "backup"
AND contains_sensitive_data = TRUE
AND encryption_enabled = TRUE
AND encryption_verified = TRUE
AND offsite_storage = TRUE
THEN compliance = TRUE

[SCENARIO-05: Development System with Production Data]
IF environment = "development"
AND contains_production_data = TRUE
AND data_classification = "restricted"
AND encryption_enabled = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic mechanisms prevent unauthorized disclosure of defined information at rest | [RULE-01], [RULE-03] |
| Cryptographic mechanisms prevent unauthorized modification of defined information at rest | [RULE-01], [RULE-02] |
| Information requiring protection is properly defined and classified | [RULE-01] |
| Appropriate cryptographic strength is implemented | [RULE-01], [RULE-04] |
| Protection extends to system components and media | [RULE-02], [RULE-03], [RULE-05], [RULE-06] |