# POLICY: SC-28: Protection of Information at Rest

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-28 |
| NIST Control | SC-28: Protection of Information at Rest |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | data encryption, data at rest, confidentiality, integrity, cryptographic protection |

## 1. POLICY STATEMENT
The organization SHALL protect the confidentiality and integrity of information at rest through appropriate security controls including cryptographic mechanisms, access controls, and monitoring. All information requiring protection MUST be identified, classified, and protected using approved methods based on its sensitivity level.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All data storage systems | YES | Internal and external storage devices |
| Databases | YES | Production, development, and test databases |
| File shares and repositories | YES | Network attached storage, cloud storage |
| Backup systems | YES | Online and offline backup storage |
| Mobile devices | YES | Company-owned and BYOD devices |
| Cloud storage services | YES | Must meet organizational security requirements |
| Temporary files | YES | Cache, swap, and temporary storage |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Classify information sensitivity levels<br>• Define protection requirements<br>• Approve access controls |
| System Administrator | • Implement encryption mechanisms<br>• Configure storage security settings<br>• Monitor compliance status |
| Security Team | • Define cryptographic standards<br>• Conduct security assessments<br>• Validate protection mechanisms |

## 4. RULES
[RULE-01] All information at rest classified as Confidential or higher MUST be encrypted using FIPS 140-2 Level 2 or higher approved cryptographic modules.
[VALIDATION] IF data_classification IN ["Confidential", "Secret", "Top Secret"] AND encryption_status = FALSE THEN critical_violation

[RULE-02] Encryption keys for data at rest MUST be managed through an approved key management system and rotated at least annually.
[VALIDATION] IF key_age > 365_days OR key_management_system NOT IN approved_systems THEN violation

[RULE-03] Database encryption MUST use Transparent Data Encryption (TDE) or equivalent technology for production databases containing sensitive information.
[VALIDATION] IF database_type = "production" AND sensitive_data = TRUE AND tde_enabled = FALSE THEN violation

[RULE-04] File-level encryption MUST be implemented for removable media and mobile devices containing organizational data.
[VALIDATION] IF device_type IN ["removable_media", "mobile_device"] AND org_data = TRUE AND file_encryption = FALSE THEN violation

[RULE-05] Cloud storage services MUST implement server-side encryption with customer-managed keys for all organizational data.
[VALIDATION] IF storage_location = "cloud" AND server_side_encryption = FALSE OR key_management != "customer_managed" THEN violation

[RULE-06] Backup data MUST be encrypted both in transit and at rest using the same protection level as the original data.
[VALIDATION] IF data_type = "backup" AND (encryption_at_rest = FALSE OR encryption_in_transit = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Classification Procedure - Systematic process for identifying and classifying information requiring protection
- [PROC-02] Encryption Implementation Procedure - Step-by-step process for implementing approved encryption mechanisms
- [PROC-03] Key Management Procedure - Processes for key generation, distribution, rotation, and revocation
- [PROC-04] Storage Security Assessment Procedure - Regular evaluation of data at rest protection mechanisms

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New storage technologies, security incidents, regulatory changes, failed assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unencrypted Sensitive Database]
IF database_contains_pii = TRUE
AND database_classification = "Confidential"
AND encryption_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Expired Encryption Keys]
IF encryption_enabled = TRUE
AND key_last_rotated > 365_days_ago
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Cloud Storage Without Customer-Managed Keys]
IF storage_type = "cloud"
AND data_classification = "Confidential"
AND key_management = "provider_managed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Compliant Encrypted Backup]
IF data_type = "backup"
AND source_data_classification = "Confidential"
AND backup_encrypted = TRUE
AND encryption_standard = "FIPS_140-2_Level_2"
THEN compliance = TRUE

[SCENARIO-05: Mobile Device with Unencrypted Files]
IF device_type = "mobile"
AND contains_org_data = TRUE
AND file_level_encryption = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Confidentiality of information at rest requiring protection is defined | RULE-01, RULE-03 |
| Information at rest requiring protection is protected | RULE-01, RULE-02, RULE-04, RULE-05, RULE-06 |
| Cryptographic mechanisms are properly implemented | RULE-01, RULE-02 |
| Database protection mechanisms are in place | RULE-03 |
| Mobile and removable media protection is implemented | RULE-04 |
| Cloud storage protection requirements are met | RULE-05 |