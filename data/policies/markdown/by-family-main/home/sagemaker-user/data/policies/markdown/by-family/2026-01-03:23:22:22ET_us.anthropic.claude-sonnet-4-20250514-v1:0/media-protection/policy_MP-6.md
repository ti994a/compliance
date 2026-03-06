# POLICY: MP-6: Media Sanitization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-6 |
| NIST Control | MP-6: Media Sanitization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media sanitization, disposal, data destruction, clearing, purging, cryptographic erase |

## 1. POLICY STATEMENT
All organizational system media containing sensitive information MUST be sanitized using approved techniques prior to disposal, release from organizational control, or reuse. Sanitization mechanisms MUST have strength and integrity commensurate with the security category or classification of the information contained on the media.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Digital Media | YES | Hard drives, SSDs, USB drives, mobile devices, network components |
| Non-Digital Media | YES | Paper documents, microfilm, printed materials |
| Cloud Storage | YES | Virtual storage, backup systems, archived data |
| Third-Party Media | YES | Media processed by vendors or partners |
| Public Domain Media | CONDITIONAL | May use reduced sanitization based on data classification |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Classify media based on information sensitivity<br>• Approve sanitization methods<br>• Verify sanitization completion |
| IT Security Team | • Define sanitization procedures<br>• Validate sanitization techniques<br>• Maintain sanitization records |
| Asset Management | • Track media through disposal process<br>• Execute approved sanitization procedures<br>• Document sanitization activities |

## 4. RULES
[RULE-01] All system media MUST be sanitized using organization-approved techniques before disposal, release from organizational control, or reuse.
[VALIDATION] IF media_status = "disposal" OR "release" OR "reuse" AND sanitization_completed = FALSE THEN violation

[RULE-02] Sanitization methods MUST match or exceed the security classification level of the highest classified information ever stored on the media.
[VALIDATION] IF sanitization_strength < data_classification_level THEN violation

[RULE-03] Media containing TOP SECRET information MUST be destroyed through physical destruction methods only.
[VALIDATION] IF data_classification = "TOP_SECRET" AND sanitization_method != "physical_destruction" THEN critical_violation

[RULE-04] Media containing SECRET or CONFIDENTIAL information MUST use NSA-approved purging or destruction methods.
[VALIDATION] IF data_classification IN ["SECRET", "CONFIDENTIAL"] AND sanitization_method NOT IN approved_nsa_methods THEN violation

[RULE-05] Media containing PII or PHI MUST use cryptographic erase, secure overwrite (minimum 3 passes), or physical destruction.
[VALIDATION] IF data_type IN ["PII", "PHI"] AND sanitization_method NOT IN ["crypto_erase", "secure_overwrite_3pass", "physical_destruction"] THEN violation

[RULE-06] All sanitization activities MUST be documented with method used, date completed, personnel responsible, and verification results.
[VALIDATION] IF sanitization_completed = TRUE AND documentation_complete = FALSE THEN violation

[RULE-07] Third-party sanitization services MUST provide certificates of destruction or sanitization for all processed media.
[VALIDATION] IF sanitization_vendor = "third_party" AND certificate_received = FALSE THEN violation

[RULE-08] Media sanitization verification MUST be performed by personnel independent of those who performed the sanitization.
[VALIDATION] IF sanitization_performer = verification_performer THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Classification Procedure - Classify media based on highest sensitivity level of contained data
- [PROC-02] Sanitization Method Selection - Select appropriate sanitization technique based on classification and media type
- [PROC-03] Sanitization Execution - Perform sanitization using approved tools and techniques
- [PROC-04] Sanitization Verification - Verify complete data removal through independent testing
- [PROC-05] Documentation and Records Management - Maintain sanitization records per retention requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when sanitization standards change
- Triggering events: Data breach, new media types, regulatory changes, failed sanitization verification

## 7. SCENARIO PATTERNS
[SCENARIO-01: Laptop Disposal]
IF device_type = "laptop"
AND data_classification = "CONFIDENTIAL"
AND sanitization_method = "single_pass_overwrite"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: USB Drive Reuse]
IF media_type = "USB_drive"
AND previous_data = "PII"
AND sanitization_method = "crypto_erase"
AND verification_completed = TRUE
THEN compliance = TRUE

[SCENARIO-03: Third-Party Destruction]
IF disposal_method = "third_party"
AND certificate_destruction = "received"
AND vendor_approved = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-04: Paper Document Disposal]
IF media_type = "paper"
AND classification = "SECRET"
AND sanitization_method = "shredding"
AND shred_size > "2mm_strips"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Mobile Device Sanitization]
IF device_type = "mobile_device"
AND contains_corporate_data = TRUE
AND sanitization_method = "factory_reset_only"
AND crypto_erase = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Media sanitized prior to disposal | RULE-01, RULE-06 |
| Media sanitized prior to release from organizational control | RULE-01, RULE-07 |
| Media sanitized prior to reuse | RULE-01, RULE-08 |
| Sanitization strength commensurate with classification | RULE-02, RULE-03, RULE-04, RULE-05 |
| Sanitization techniques and procedures defined | RULE-01, RULE-02 |
| Documentation of sanitization activities | RULE-06, RULE-07 |