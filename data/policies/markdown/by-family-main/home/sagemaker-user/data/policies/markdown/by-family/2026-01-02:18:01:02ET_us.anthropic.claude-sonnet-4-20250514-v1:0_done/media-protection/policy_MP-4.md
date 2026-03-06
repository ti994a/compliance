# POLICY: MP-4: Media Storage

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-4 |
| NIST Control | MP-4: Media Storage |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media storage, physical control, digital media, non-digital media, controlled areas, sanitization |

## 1. POLICY STATEMENT
The organization SHALL physically control and securely store all defined types of digital and non-digital media within designated controlled areas. All system media MUST be protected until proper destruction or sanitization using approved equipment, techniques, and procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Digital Media | YES | Flash drives, external drives, CDs, DVDs, magnetic tapes |
| Non-Digital Media | YES | Paper documents, microfilm, printed materials |
| Cloud Storage | CONDITIONAL | Only physical backup media and local caches |
| Personal Devices | YES | When containing organizational data |
| Vendor Media | YES | When under organizational control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Media Custodian | • Maintain media inventory and check-out procedures<br>• Ensure secure storage in controlled areas<br>• Verify media sanitization before disposal |
| Security Officer | • Define controlled area requirements<br>• Approve sanitization procedures<br>• Conduct periodic compliance audits |
| IT Asset Manager | • Track media lifecycle from procurement to disposal<br>• Maintain approved equipment lists<br>• Coordinate with facilities for secure storage areas |

## 4. RULES
[RULE-01] All digital media containing organizational data MUST be stored in locked, access-controlled facilities with environmental protections.
[VALIDATION] IF media_type = "digital" AND storage_location != "controlled_area" THEN violation

[RULE-02] Non-digital media containing sensitive information MUST be stored in fire-resistant containers within controlled areas.
[VALIDATION] IF media_type = "non-digital" AND sensitivity_level >= "sensitive" AND container_type != "fire_resistant" THEN violation

[RULE-03] Media check-out procedures MUST maintain accountability records including user identity, media identifier, and return date.
[VALIDATION] IF media_checkout = TRUE AND (user_id = NULL OR media_id = NULL OR return_date = NULL) THEN violation

[RULE-04] Media inventory MUST be conducted quarterly with discrepancies reported within 24 hours.
[VALIDATION] IF last_inventory_date > 90_days AND current_date > last_inventory_date THEN violation

[RULE-05] All media MUST be protected using approved sanitization methods before disposal or reuse outside the organization.
[VALIDATION] IF media_disposal = TRUE AND sanitization_method NOT IN approved_methods THEN critical_violation

[RULE-06] Controlled areas for media storage MUST implement physical access controls commensurate with the highest classification of stored media.
[VALIDATION] IF max_classification_level > area_security_level THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Inventory Management - Quarterly physical inventory with reconciliation
- [PROC-02] Media Check-out/Check-in - Standardized accountability procedures
- [PROC-03] Secure Storage Area Management - Access control and environmental monitoring
- [PROC-04] Media Sanitization - Approved destruction and sanitization methods
- [PROC-05] Incident Response - Procedures for lost or compromised media

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving media, changes in data classification, new media types

## 7. SCENARIO PATTERNS
[SCENARIO-01: Uncontrolled Digital Media Storage]
IF media_type = "digital"
AND contains_org_data = TRUE
AND storage_location = "unsecured_area"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Checkout Documentation]
IF media_status = "checked_out"
AND checkout_record_complete = FALSE
AND days_outstanding > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Overdue Inventory]
IF last_inventory_date > 90_days
AND inventory_status = "overdue"
AND discrepancy_count > 0
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Improper Media Disposal]
IF media_disposal_pending = TRUE
AND sanitization_completed = FALSE
AND approved_method_used = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Classification Mismatch]
IF media_classification = "SECRET"
AND storage_area_level = "UNCLASSIFIED"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Digital media physically controlled | RULE-01, RULE-03 |
| Non-digital media physically controlled | RULE-02, RULE-03 |
| Digital media securely stored in controlled areas | RULE-01, RULE-06 |
| Non-digital media securely stored in controlled areas | RULE-02, RULE-06 |
| System media protected until destruction/sanitization | RULE-05 |
| Inventory and accountability maintained | RULE-03, RULE-04 |