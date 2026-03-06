# POLICY: MP-2: Media Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-2 |
| NIST Control | MP-2: Media Access |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media access, digital media, non-digital media, access control, authorization, storage |

## 1. POLICY STATEMENT
The organization SHALL restrict access to all digital and non-digital media to only authorized personnel or roles based on business need and security classification. All media access MUST be controlled through formal authorization processes and documented access controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Digital Media | YES | Flash drives, external drives, CDs, DVDs, tapes, removable storage |
| Non-Digital Media | YES | Paper documents, microfilm, printed materials |
| Cloud Storage Media | YES | When containing organizational data |
| Personal Devices | CONDITIONAL | Only when accessing organizational media |
| Contractors/Vendors | YES | When requiring media access for business purposes |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Define media classification and access requirements<br>• Approve access authorization requests<br>• Review access permissions quarterly |
| IT Security Team | • Implement technical access controls<br>• Monitor media access activities<br>• Maintain access control systems |
| Media Custodian | • Enforce physical access controls<br>• Maintain media inventory and access logs<br>• Report access violations |

## 4. RULES
[RULE-01] Access to digital media MUST be restricted to personnel or roles explicitly authorized by the data owner based on documented business justification.
[VALIDATION] IF user_accesses_digital_media = TRUE AND user_authorized_for_media = FALSE THEN violation

[RULE-02] Access to non-digital media MUST be restricted to personnel or roles explicitly authorized by the data owner with physical access controls implemented.
[VALIDATION] IF user_accesses_nondigital_media = TRUE AND user_authorized_for_media = FALSE THEN violation

[RULE-03] All media types requiring access restrictions MUST be clearly defined and documented in the media classification policy.
[VALIDATION] IF media_type_defined = FALSE AND access_restricted = TRUE THEN violation

[RULE-04] Personnel authorized for media access MUST be formally documented with role-based access assignments reviewed at least quarterly.
[VALIDATION] IF authorized_personnel_documented = FALSE OR last_review_date > 90_days THEN violation

[RULE-05] Media access authorization MUST be removed within 24 hours of personnel role change or termination.
[VALIDATION] IF personnel_status_changed = TRUE AND access_revocation_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Classification - Categorize all digital and non-digital media types requiring access restrictions
- [PROC-02] Access Authorization - Process for requesting and approving media access permissions
- [PROC-03] Access Control Implementation - Technical and physical controls for enforcing media access restrictions
- [PROC-04] Access Review - Quarterly review of media access permissions and authorization

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, organizational changes, new media types, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Digital Media Access]
IF user_role = "standard_employee"
AND media_type = "classified_external_drive"
AND authorization_documented = FALSE
AND access_attempted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Media Access]
IF user_type = "contractor"
AND media_contains_sensitive_data = TRUE
AND business_justification_documented = TRUE
AND data_owner_approval = TRUE
THEN compliance = TRUE

[SCENARIO-03: Terminated Employee Media Access]
IF employee_status = "terminated"
AND termination_date < current_date
AND media_access_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Healthcare Records Access]
IF media_type = "patient_medical_records"
AND user_role = "healthcare_provider"
AND patient_care_relationship = TRUE
AND access_logged = TRUE
THEN compliance = TRUE

[SCENARIO-05: Undefined Media Type Access]
IF media_classification = "undefined"
AND access_restrictions_applied = FALSE
AND sensitive_data_present = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Digital media access restrictions defined | [RULE-01], [RULE-03] |
| Digital media access restricted to authorized personnel | [RULE-01], [RULE-04] |
| Non-digital media access restrictions defined | [RULE-02], [RULE-03] |
| Non-digital media access restricted to authorized personnel | [RULE-02], [RULE-04] |