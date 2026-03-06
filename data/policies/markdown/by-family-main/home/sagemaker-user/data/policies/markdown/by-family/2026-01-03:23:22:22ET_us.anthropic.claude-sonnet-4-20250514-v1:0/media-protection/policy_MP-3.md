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
All system media containing organizational information MUST be marked to indicate distribution limitations, handling caveats, and applicable security markings. Organizations SHALL define specific types of media exempt from marking requirements when such media remain within designated controlled areas.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Digital Media | YES | Includes drives, disks, tapes, flash drives, CDs, DVDs |
| Non-Digital Media | YES | Includes paper documents, microfilm |
| Public Domain Information | CONDITIONAL | Only if organization requires public release markings |
| Media in Controlled Areas | CONDITIONAL | Subject to defined exemptions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Custodians | • Apply appropriate markings to media based on information classification<br>• Verify marking compliance before media distribution<br>• Maintain marking standards documentation |
| Security Officers | • Define controlled areas and exemption criteria<br>• Establish marking requirements and procedures<br>• Monitor compliance with marking requirements |
| IT Personnel | • Implement technical controls for automated marking<br>• Ensure marking integrity during media handling<br>• Report unmarked or improperly marked media |

## 4. RULES
[RULE-01] System media containing non-public organizational information MUST be marked with distribution limitations, handling caveats, and security markings appropriate to the information classification level.
[VALIDATION] IF media_contains_org_info = TRUE AND marking_present = FALSE AND exemption_applies = FALSE THEN violation

[RULE-02] Organizations MUST define and document specific types of system media exempt from marking requirements when remaining in controlled areas.
[VALIDATION] IF controlled_area_exemptions = undefined OR exemption_documentation = missing THEN violation

[RULE-03] Media exempt from marking MUST NOT leave designated controlled areas unless properly marked according to information classification requirements.
[VALIDATION] IF exempt_media = TRUE AND location = outside_controlled_area AND proper_marking = FALSE THEN critical_violation

[RULE-04] Security markings MUST reflect applicable laws, executive orders, directives, policies, regulations, standards, and guidelines including CUI requirements per 32 CFR 2002.
[VALIDATION] IF marking_standards = non_compliant OR cui_requirements = not_met THEN violation

[RULE-05] Media marking procedures MUST be reviewed and updated annually or when regulatory requirements change.
[VALIDATION] IF last_review_date > 365_days OR regulatory_change = TRUE AND procedure_update = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Classification and Marking - Process for determining appropriate markings based on information sensitivity
- [PROC-02] Controlled Area Management - Procedures for defining, maintaining, and monitoring controlled areas
- [PROC-03] Exemption Documentation - Process for documenting and approving media marking exemptions
- [PROC-04] Marking Verification - Procedures for validating marking accuracy and completeness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Regulatory changes, security incidents involving unmarked media, changes to controlled areas

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unmarked Media Distribution]
IF media_classification = "confidential"
AND marking_present = FALSE
AND distribution_outside_org = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Exempt Media in Controlled Area]
IF media_type = "working_papers"
AND location = "controlled_area"
AND exemption_documented = TRUE
AND marking_present = FALSE
THEN compliance = TRUE

[SCENARIO-03: CUI Media Without Proper Marking]
IF information_type = "CUI"
AND cui_marking = FALSE
AND media_distributed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Public Information Media]
IF information_classification = "public"
AND organization_requires_public_marking = FALSE
AND marking_present = FALSE
THEN compliance = TRUE

[SCENARIO-05: Exempt Media Leaving Controlled Area]
IF media_exemption = TRUE
AND current_location = "outside_controlled_area"
AND transit_marking_applied = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Media marked with distribution limitations and handling caveats | [RULE-01] |
| Types of exempt media in controlled areas defined | [RULE-02] |
| Exempt media remains in controlled areas | [RULE-03] |
| Markings reflect applicable legal requirements | [RULE-04] |