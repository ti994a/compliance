# POLICY: MP-8.3: Controlled Unclassified Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-8.3 |
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
| Public-facing systems | YES | Systems that may release information publicly |
| Third-party vendors | YES | When handling CUI on behalf of organization |
| Personal devices | CONDITIONAL | Only if approved for CUI processing |
| Development/test systems | YES | If containing production CUI data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Custodian | • Identify CUI on system media<br>• Execute approved downgrading procedures<br>• Maintain downgrading records |
| Information Security Officer | • Approve sanitization tools and techniques<br>• Review downgrading procedures<br>• Validate compliance with CUI requirements |
| Media Manager | • Oversee media handling processes<br>• Ensure proper chain of custody<br>• Coordinate with data custodians |

## 4. RULES
[RULE-01] All system media containing CUI MUST be identified and classified before any processing or release activities.
[VALIDATION] IF media_contains_CUI = TRUE AND classification_status = "unidentified" THEN violation

[RULE-02] CUI downgrading SHALL only be performed using organization-approved sanitization tools, techniques, and procedures.
[VALIDATION] IF downgrading_method NOT IN approved_methods_list THEN violation

[RULE-03] System media containing CUI MUST be completely downgraded prior to any public release or declassification.
[VALIDATION] IF public_release = TRUE AND CUI_present = TRUE AND downgrade_complete = FALSE THEN critical_violation

[RULE-04] All media downgrading activities MUST be documented with timestamps, methods used, and personnel responsible.
[VALIDATION] IF downgrading_performed = TRUE AND documentation_complete = FALSE THEN violation

[RULE-05] Downgrading procedures MUST be validated through testing before implementation on media containing actual CUI.
[VALIDATION] IF procedure_status = "new" AND validation_testing = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] CUI Media Identification - Systematic process for identifying and marking media containing CUI
- [PROC-02] Sanitization Tool Approval - Evaluation and approval process for downgrading tools and techniques
- [PROC-03] Media Downgrading Execution - Step-by-step procedures for performing CUI downgrading
- [PROC-04] Downgrading Verification - Process to verify complete removal of CUI from media
- [PROC-05] Documentation and Record Keeping - Requirements for maintaining downgrading records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: CUI regulation changes, security incidents involving CUI, new media types, sanitization tool updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Sanitization Method]
IF media_contains_CUI = TRUE
AND sanitization_method = "custom_script"
AND method_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Documentation]
IF downgrading_completed = TRUE
AND documentation_timestamp = NULL
AND personnel_recorded = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Public Release Without Downgrading]
IF release_type = "public"
AND CUI_identified = TRUE
AND downgrade_status = "pending"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Proper CUI Downgrading Process]
IF media_contains_CUI = TRUE
AND approved_method_used = TRUE
AND verification_complete = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-05: Third-Party Vendor Handling]
IF vendor_handling_CUI = TRUE
AND contractual_requirements = FALSE
AND downgrading_oversight = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System media containing CUI is identified | [RULE-01] |
| System media containing CUI is downgraded prior to public release | [RULE-03] |
| Approved sanitization tools and techniques are used | [RULE-02] |
| Downgrading activities are properly documented | [RULE-04] |
| Procedures are validated before implementation | [RULE-05] |