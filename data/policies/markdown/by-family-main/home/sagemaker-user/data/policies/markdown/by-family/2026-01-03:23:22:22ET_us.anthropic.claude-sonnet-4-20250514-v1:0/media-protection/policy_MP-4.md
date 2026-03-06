# POLICY: MP-4: Media Storage

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-4 |
| NIST Control | MP-4: Media Storage |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media storage, physical control, digital media, non-digital media, controlled areas, media protection |

## 1. POLICY STATEMENT
All organizational digital and non-digital media containing sensitive information MUST be physically controlled and securely stored within designated controlled areas. Media protection controls SHALL remain in effect until media is properly destroyed or sanitized using approved methods.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Digital Media | YES | Flash drives, external drives, CDs, DVDs, magnetic tapes |
| Non-Digital Media | YES | Paper documents, microfilm, printed materials |
| All Employees | YES | Anyone handling organizational media |
| Contractors/Vendors | YES | When accessing organizational media |
| Public Domain Media | CONDITIONAL | Reduced controls for publicly releasable information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Media Custodian | • Maintain media inventory and checkout procedures<br>• Ensure secure storage implementation<br>• Monitor access to controlled storage areas |
| Information Owner | • Define media classification and storage requirements<br>• Approve media handling procedures<br>• Authorize media access exceptions |
| Security Officer | • Validate controlled area security measures<br>• Audit media storage compliance<br>• Approve sanitization procedures |

## 4. RULES

[RULE-01] Digital media containing confidential or restricted information MUST be stored in locked, controlled areas with documented access procedures.
[VALIDATION] IF media_type = "digital" AND classification IN ["confidential", "restricted"] AND storage_area_locked = FALSE THEN violation

[RULE-02] Non-digital media containing sensitive information MUST be stored in controlled areas with physical access controls commensurate with information classification.
[VALIDATION] IF media_type = "non-digital" AND contains_sensitive_info = TRUE AND controlled_area = FALSE THEN violation

[RULE-03] Media inventory records MUST be maintained with checkout/return procedures for all media stored in controlled areas.
[VALIDATION] IF media_in_controlled_storage = TRUE AND inventory_record_exists = FALSE THEN violation

[RULE-04] Media storage areas MUST implement physical controls appropriate to the highest classification of information stored within.
[VALIDATION] IF storage_area_controls < max_classification_level THEN violation

[RULE-05] Media protection controls MUST remain active until media is destroyed or sanitized using NIST-approved methods.
[VALIDATION] IF media_protection_removed = TRUE AND (destroyed = FALSE AND sanitized = FALSE) THEN critical_violation

[RULE-06] Public domain or publicly releasable media MAY use reduced physical controls but MUST still maintain basic inventory tracking.
[VALIDATION] IF classification = "public" AND inventory_tracking = FALSE THEN minor_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Classification and Handling - Procedures for determining appropriate storage requirements based on information classification
- [PROC-02] Controlled Area Access Management - Procedures for authorizing and monitoring access to media storage areas
- [PROC-03] Media Inventory and Tracking - Procedures for maintaining accurate inventory and checkout records
- [PROC-04] Media Sanitization and Destruction - Procedures for secure media disposal using approved methods

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Security incidents involving media, changes to classification schemes, new media types introduction

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unsecured Backup Media]
IF media_type = "backup_tape"
AND classification = "confidential"
AND stored_in_locked_cabinet = FALSE
AND controlled_area = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Inventory Records]
IF media_checkout_occurred = TRUE
AND checkout_date > 30_days_ago
AND return_documented = FALSE
AND inventory_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Inadequate Public Media Controls]
IF classification = "public"
AND basic_inventory = TRUE
AND physical_security_present = TRUE
THEN compliance = TRUE

[SCENARIO-04: Contractor Media Access]
IF user_type = "contractor"
AND media_access_authorized = TRUE
AND controlled_area_access = TRUE
AND checkout_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Unsanitized Media Reuse]
IF media_previous_use = TRUE
AND sanitization_completed = FALSE
AND new_data_written = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Digital media physically controlled | RULE-01 |
| Non-digital media physically controlled | RULE-02 |
| Media securely stored in controlled areas | RULE-01, RULE-02, RULE-04 |
| Media protected until destruction/sanitization | RULE-05 |
| Inventory and accountability procedures | RULE-03 |
| Classification-appropriate controls | RULE-04, RULE-06 |