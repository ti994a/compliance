# POLICY: MP-6: Media Sanitization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-6 |
| NIST Control | MP-6: Media Sanitization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media sanitization, data destruction, disposal, reuse, clearing, purging, cryptographic erase |

## 1. POLICY STATEMENT
All organizational system media containing sensitive information MUST be sanitized using approved techniques prior to disposal, release from organizational control, or reuse. Sanitization mechanisms MUST have strength and integrity commensurate with the security category or classification of the information contained on the media.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Digital storage media | YES | Hard drives, SSDs, USB drives, mobile devices, network components |
| Non-digital media | YES | Paper documents, microfilm, printed materials |
| Cloud storage | YES | Virtual storage requiring cryptographic sanitization |
| Public domain information | CONDITIONAL | May use reduced sanitization based on risk assessment |
| Classified information | YES | Must follow NSA standards and policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Asset Manager | • Maintain inventory of media requiring sanitization<br>• Coordinate sanitization activities<br>• Verify completion of sanitization procedures |
| Security Officer | • Define sanitization requirements by data classification<br>• Approve sanitization techniques and procedures<br>• Conduct compliance audits |
| Data Custodians | • Execute approved sanitization procedures<br>• Document sanitization activities<br>• Report sanitization completion |

## 4. RULES
[RULE-01] All system media MUST be sanitized using organization-approved techniques before disposal, release from organizational control, or reuse.
[VALIDATION] IF media_status = "pending_disposal" OR media_status = "pending_release" OR media_status = "pending_reuse" AND sanitization_completed = FALSE THEN violation

[RULE-02] Sanitization techniques MUST be selected based on data classification level with clearing for CUI, purging for sensitive data, and destruction for classified information.
[VALIDATION] IF data_classification = "classified" AND sanitization_method ≠ "destruction" AND nsa_exception = FALSE THEN critical_violation

[RULE-03] Digital media sanitization MUST use NIST SP 800-88 approved methods including overwriting, cryptographic erase, or physical destruction.
[VALIDATION] IF media_type = "digital" AND sanitization_method NOT IN ["nist_approved_overwrite", "cryptographic_erase", "physical_destruction"] THEN violation

[RULE-04] All sanitization activities MUST be documented with media identifier, sanitization method used, date completed, and responsible personnel.
[VALIDATION] IF sanitization_completed = TRUE AND (documentation_complete = FALSE OR required_fields_missing > 0) THEN violation

[RULE-05] Media containing classified information MUST follow NSA sanitization standards and policies exclusively.
[VALIDATION] IF data_classification = "classified" AND sanitization_standard ≠ "nsa_approved" THEN critical_violation

[RULE-06] Sanitization verification MUST be performed and documented for all media containing sensitive or classified information.
[VALIDATION] IF data_classification IN ["sensitive", "classified"] AND verification_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Sanitization Standard Operating Procedure - Detailed steps for each approved sanitization method
- [PROC-02] Media Classification and Handling Procedure - Guidelines for determining appropriate sanitization level
- [PROC-03] Sanitization Verification Procedure - Steps to verify successful sanitization completion
- [PROC-04] Documentation and Record Keeping Procedure - Requirements for maintaining sanitization records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when technology changes
- Triggering events: New media types, classification changes, regulatory updates, security incidents involving media

## 7. SCENARIO PATTERNS
[SCENARIO-01: Laptop Disposal]
IF device_type = "laptop"
AND contains_sensitive_data = TRUE
AND sanitization_method = "simple_delete"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Classified Media Destruction]
IF data_classification = "classified"
AND sanitization_method = "nsa_approved_destruction"
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-03: USB Drive Reuse]
IF media_type = "usb_drive"
AND previous_use = "sensitive_data"
AND sanitization_method = "cryptographic_erase"
AND verification_completed = TRUE
THEN compliance = TRUE

[SCENARIO-04: Paper Document Disposal]
IF media_type = "paper"
AND classification = "confidential"
AND sanitization_method = "cross_cut_shredding"
AND particle_size > "nist_requirement"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Cloud Storage Termination]
IF storage_type = "cloud"
AND data_classification = "sensitive"
AND sanitization_method = "cryptographic_erase"
AND key_destruction_verified = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System media sanitized prior to disposal | [RULE-01] |
| System media sanitized prior to release from organizational control | [RULE-01] |
| System media sanitized prior to release for reuse | [RULE-01] |
| Sanitization techniques and procedures defined for disposal | [RULE-02], [RULE-03] |
| Sanitization techniques and procedures defined for release | [RULE-02], [RULE-03] |
| Sanitization techniques and procedures defined for reuse | [RULE-02], [RULE-03] |
| Sanitization mechanisms commensurate with security category employed | [RULE-02], [RULE-05] |