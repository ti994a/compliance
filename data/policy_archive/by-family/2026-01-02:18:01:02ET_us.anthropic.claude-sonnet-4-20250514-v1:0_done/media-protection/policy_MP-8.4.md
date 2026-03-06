```markdown
# POLICY: MP-8.4: Media Downgrading - Classified Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-8.4 |
| NIST Control | MP-8.4: Media Downgrading - Classified Information |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | classified information, media downgrading, sanitization, access authorization, media protection |

## 1. POLICY STATEMENT
System media containing classified information MUST be properly downgraded using approved sanitization procedures before release to individuals lacking required security clearances. All downgrading activities MUST be documented and verified to ensure complete removal of classified content.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All system media | YES | Physical and electronic storage devices |
| Classified information systems | YES | All classification levels |
| Cleared personnel | YES | Those performing downgrading operations |
| Uncleared personnel | YES | Those receiving downgraded media |
| Third-party contractors | CONDITIONAL | Only if handling classified media |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Information System Security Manager | • Oversee media downgrading program<br>• Approve downgrading procedures<br>• Ensure compliance with classification policies |
| Authorized Downgrading Personnel | • Execute approved sanitization procedures<br>• Document all downgrading activities<br>• Verify complete removal of classified information |
| Security Control Assessor | • Validate downgrading effectiveness<br>• Review downgrading documentation<br>• Test sanitization procedures |

## 4. RULES
[RULE-01] System media containing classified information MUST be identified and inventoried before any downgrading process begins.
[VALIDATION] IF media_contains_classified = TRUE AND inventory_status = "not_documented" THEN violation

[RULE-02] Media downgrading MUST use only NSA-approved sanitization tools, techniques, and procedures appropriate for the classification level and media type.
[VALIDATION] IF sanitization_tool_approved = FALSE OR procedure_nsa_approved = FALSE THEN critical_violation

[RULE-03] Downgrading activities MUST be performed only by personnel with appropriate security clearances and authorized downgrading responsibilities.
[VALIDATION] IF operator_clearance_level < media_classification_level OR downgrading_authorization = FALSE THEN critical_violation

[RULE-04] All media downgrading activities MUST be documented with timestamps, personnel involved, procedures used, and verification results.
[VALIDATION] IF downgrading_documentation = "incomplete" OR verification_results = "missing" THEN violation

[RULE-05] Downgraded media MUST be verified as containing only unclassified information before release to individuals without required access authorizations.
[VALIDATION] IF verification_complete = FALSE AND media_released = TRUE THEN critical_violation

[RULE-06] Media downgrading records MUST be retained for minimum 7 years and made available for compliance audits.
[VALIDATION] IF record_retention_period < 7_years OR audit_availability = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Classification Assessment - Identify and categorize classified content on media
- [PROC-02] Sanitization Tool Validation - Verify NSA approval status of downgrading tools
- [PROC-03] Downgrading Operation Execution - Step-by-step media sanitization process
- [PROC-04] Content Verification Testing - Confirm complete removal of classified information
- [PROC-05] Documentation and Record Keeping - Maintain comprehensive downgrading logs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving classified media, changes to NSA guidance, new media types introduction

## 7. SCENARIO PATTERNS
[SCENARIO-01: Proper Downgrading Process]
IF media_classification = "SECRET"
AND operator_clearance = "SECRET_or_higher"
AND sanitization_tool = "NSA_approved"
AND verification_complete = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Personnel Access]
IF media_classification = "CONFIDENTIAL"
AND operator_clearance = "uncleared"
AND downgrading_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Incomplete Verification]
IF downgrading_completed = TRUE
AND verification_status = "incomplete"
AND media_released = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Unapproved Sanitization Tool]
IF sanitization_tool = "commercial_software"
AND nsa_approval_status = FALSE
AND classified_media_processed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Missing Documentation]
IF downgrading_completed = TRUE
AND documentation_status = "incomplete"
AND retention_period > 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System media containing classified information is identified | [RULE-01] |
| System media containing classified information is downgraded prior to release to individuals without required access authorizations | [RULE-02], [RULE-03], [RULE-05] |
| Approved sanitization procedures are used | [RULE-02] |
| Downgrading activities are properly documented | [RULE-04], [RULE-06] |
| Personnel authorization requirements are enforced | [RULE-03] |
```