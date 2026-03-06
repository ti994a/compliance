# POLICY: MP-3: Media Marking

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-3 |
| NIST Control | MP-3: Media Marking |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media marking, distribution limitations, handling caveats, security markings, controlled areas |

## 1. POLICY STATEMENT
All system media containing organizational information MUST be marked with appropriate distribution limitations, handling caveats, and security markings to indicate proper safeguarding requirements. Media exempt from marking requirements MUST remain within designated controlled areas at all times.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Digital Media | YES | Includes drives, disks, tapes, flash media |
| Physical Media | YES | Includes paper documents, microfilm |
| Public Domain Information | CONDITIONAL | Only if organization requires public marking |
| Backup Media | YES | Subject to same marking as source data |
| Controlled Areas | YES | Designated areas for exempt media storage |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owners | • Determine appropriate security markings for their data<br>• Define distribution limitations and handling requirements<br>• Approve media marking exemptions |
| IT Security Team | • Maintain list of controlled areas for exempt media<br>• Validate proper media marking implementation<br>• Monitor compliance with marking requirements |
| Media Custodians | • Apply required markings before media distribution<br>• Ensure exempt media remains in controlled areas<br>• Report marking violations or incidents |

## 4. RULES
[RULE-01] All system media containing non-public organizational information MUST be marked with distribution limitations, handling caveats, and applicable security markings before leaving controlled areas.
[VALIDATION] IF media_contains_org_data = TRUE AND public_domain = FALSE AND markings_applied = FALSE AND location != "controlled_area" THEN violation

[RULE-02] Organizations MUST define and maintain a documented list of system media types exempt from marking requirements.
[VALIDATION] IF exempt_media_list = NULL OR exempt_media_list_documented = FALSE THEN violation

[RULE-03] Media exempt from marking MUST remain within designated controlled areas at all times.
[VALIDATION] IF media_type IN exempt_list AND current_location NOT IN controlled_areas THEN critical_violation

[RULE-04] Security markings MUST reflect applicable laws, executive orders, directives, policies, regulations, and standards including 32 CFR 2002 for CUI.
[VALIDATION] IF marking_standard_compliance = FALSE OR cui_marking_invalid = TRUE THEN violation

[RULE-05] Controlled areas for exempt media MUST be formally designated and documented with appropriate physical and access controls.
[VALIDATION] IF controlled_area_designation = NULL OR access_controls_missing = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Classification and Marking - Process for determining and applying appropriate markings
- [PROC-02] Controlled Area Management - Procedures for designating and maintaining controlled areas
- [PROC-03] Exempt Media Tracking - Process for monitoring exempt media location and access
- [PROC-04] Marking Compliance Audit - Regular verification of marking implementation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Regulatory changes, security incidents involving media, changes to controlled areas

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unmarked Sensitive Media Distribution]
IF media_classification = "confidential"
AND security_markings = NULL
AND distribution_outside_org = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Exempt Media in Uncontrolled Area]
IF media_type = "internal_backup_tape"
AND exempt_status = TRUE
AND current_location = "employee_desk"
AND controlled_area_status = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Public Information Marking]
IF information_classification = "public_domain"
AND organization_requires_public_marking = TRUE
AND public_release_marking = NULL
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: CUI Marking Compliance]
IF information_type = "CUI"
AND cfr_2002_marking_applied = TRUE
AND marking_format_valid = TRUE
THEN compliance = TRUE

[SCENARIO-05: Controlled Area Exempt Media]
IF media_type IN exempt_media_list
AND current_location IN controlled_areas
AND access_controls_active = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System media marked with distribution limitations | [RULE-01] |
| System media marked with handling caveats | [RULE-01] |
| System media marked with applicable security markings | [RULE-01], [RULE-04] |
| Types of exempt system media defined | [RULE-02] |
| Exempt media remains in controlled areas | [RULE-03] |
| Controlled areas properly designated | [RULE-05] |