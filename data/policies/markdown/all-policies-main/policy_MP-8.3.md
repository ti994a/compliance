# POLICY: MP-8.3: Controlled Unclassified Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-8-3 |
| NIST Control | MP-8.3: Controlled Unclassified Information |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media protection, controlled unclassified information, CUI, downgrading, sanitization, public release |

## 1. POLICY STATEMENT
All system media containing Controlled Unclassified Information (CUI) MUST be properly downgraded using approved sanitization methods before any public release. Organizations SHALL maintain documented procedures and records for all media downgrading activities to ensure CUI protection requirements are met.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All system media | YES | Physical and digital media containing CUI |
| Cloud storage | YES | When containing CUI data |
| Backup media | YES | All backup systems with CUI |
| Development/test systems | YES | When using production CUI data |
| Public-facing systems | YES | Before any public data release |
| Third-party vendors | CONDITIONAL | When handling CUI on our behalf |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Classification Officer | • Identify CUI on system media<br>• Approve downgrading procedures<br>• Validate sanitization completeness |
| IT Security Team | • Execute approved sanitization tools and techniques<br>• Maintain downgrading records<br>• Verify media sanitization before release |
| System Administrators | • Identify media requiring downgrading<br>• Follow established downgrading procedures<br>• Document all downgrading activities |

## 4. RULES
[RULE-01] All system media containing CUI MUST be identified and classified before any processing or release activities.
[VALIDATION] IF media_contains_CUI = TRUE AND classification_status = "unidentified" THEN violation

[RULE-02] System media containing CUI MUST be downgraded using only approved sanitization tools and techniques prior to public release.
[VALIDATION] IF media_contains_CUI = TRUE AND public_release = TRUE AND approved_sanitization = FALSE THEN critical_violation

[RULE-03] Media downgrading activities MUST be documented with records including date, method used, personnel involved, and verification of completion.
[VALIDATION] IF downgrading_performed = TRUE AND documentation_complete = FALSE THEN violation

[RULE-04] Downgrading procedures MUST be reviewed and approved by the Data Classification Officer before implementation.
[VALIDATION] IF downgrading_procedure = "new" AND DCO_approval = FALSE THEN violation

[RULE-05] Media downgrading records MUST be retained for minimum 7 years or per applicable regulatory requirements.
[VALIDATION] IF record_age > retention_period AND record_destroyed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] CUI Media Identification - Systematic process to identify and tag media containing CUI
- [PROC-02] Approved Sanitization Methods - Documented list of approved tools and techniques for CUI downgrading
- [PROC-03] Downgrading Verification - Process to verify complete removal or downgrading of CUI before release
- [PROC-04] Record Keeping - Documentation requirements for all media downgrading activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New CUI regulations, sanitization tool updates, security incidents involving CUI, regulatory audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Public Website Data Release]
IF media_contains_CUI = TRUE
AND release_destination = "public_website"
AND sanitization_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Approved Sanitization Process]
IF media_contains_CUI = TRUE
AND sanitization_method IN approved_methods
AND verification_completed = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-03: Vendor Media Handling]
IF vendor_handling_CUI = TRUE
AND contract_includes_CUI_requirements = FALSE
AND media_downgrading_specified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Backup Media Disposal]
IF backup_media_contains_CUI = TRUE
AND disposal_planned = TRUE
AND sanitization_performed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Incomplete Documentation]
IF downgrading_performed = TRUE
AND sanitization_method_documented = TRUE
AND personnel_verification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System media containing CUI is identified | [RULE-01] |
| System media containing CUI is downgraded prior to public release | [RULE-02] |
| Approved sanitization tools and techniques are used | [RULE-02], [RULE-04] |
| Media downgrading activities are documented | [RULE-03] |
| Records retention requirements are met | [RULE-05] |