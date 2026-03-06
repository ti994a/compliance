```markdown
# POLICY: MP-8.4: Classified Information Downgrading

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-8.4 |
| NIST Control | MP-8.4: Classified Information Downgrading |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | classified information, media downgrading, sanitization, access authorization, media protection |

## 1. POLICY STATEMENT
System media containing classified information MUST be properly downgraded using approved sanitization tools and procedures prior to release to individuals without required access authorizations. All downgrading activities MUST be documented and verified to ensure complete removal of classified content.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified system media | YES | All storage devices containing classified information |
| Unclassified system media | NO | Does not contain classified information |
| Contractor personnel | YES | When handling classified media downgrading |
| Federal employees | YES | With classified media responsibilities |
| Cloud storage systems | YES | If containing classified information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Information System Security Officer | • Oversee media downgrading procedures<br>• Validate sanitization tool approvals<br>• Maintain downgrading documentation |
| Media Custodian | • Execute approved downgrading procedures<br>• Verify complete sanitization<br>• Document all downgrading activities |
| Security Control Assessor | • Validate downgrading effectiveness<br>• Review sanitization procedures<br>• Audit downgrading records |

## 4. RULES

[RULE-01] System media containing classified information MUST be identified and marked before any downgrading process begins.
[VALIDATION] IF media_contains_classified = TRUE AND media_identified = FALSE THEN violation

[RULE-02] Media downgrading MUST only be performed using NSA-approved sanitization tools and techniques.
[VALIDATION] IF downgrading_tool_approved = FALSE AND downgrading_attempted = TRUE THEN critical_violation

[RULE-03] Classified information MUST be confirmed as completely removed before media release to unauthorized individuals.
[VALIDATION] IF classified_content_verified_removed = FALSE AND media_released = TRUE THEN critical_violation

[RULE-04] All media downgrading activities MUST be documented with timestamps, personnel involved, and verification results.
[VALIDATION] IF downgrading_performed = TRUE AND documentation_complete = FALSE THEN violation

[RULE-05] Personnel performing media downgrading MUST possess appropriate security clearance and training certifications.
[VALIDATION] IF personnel_clearance_level < required_clearance_level AND downgrading_authorized = TRUE THEN critical_violation

[RULE-06] Downgraded media MUST undergo independent verification before release to ensure no classified residue remains.
[VALIDATION] IF independent_verification_completed = FALSE AND media_release_approved = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Classification Identification - Systematic process to identify and catalog classified content on media
- [PROC-02] Approved Sanitization Tool Management - Maintenance and validation of NSA-approved downgrading tools
- [PROC-03] Downgrading Verification Process - Independent confirmation of complete classified information removal
- [PROC-04] Documentation and Record Keeping - Comprehensive logging of all downgrading activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving classified media, changes to NSA sanitization standards, failed downgrading verification

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Tool Usage]
IF media_contains_classified = TRUE
AND sanitization_tool_nsa_approved = FALSE
AND downgrading_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Incomplete Verification]
IF downgrading_completed = TRUE
AND independent_verification = FALSE
AND media_released_to_uncleared_personnel = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Documentation]
IF media_downgrading_performed = TRUE
AND activity_documented = FALSE
AND verification_records_exist = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Clearance Level Mismatch]
IF personnel_clearance_level = "Secret"
AND media_classification_level = "Top Secret"
AND downgrading_authorized = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Proper Downgrading Process]
IF media_properly_identified = TRUE
AND nsa_approved_tools_used = TRUE
AND independent_verification_passed = TRUE
AND complete_documentation_exists = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System media containing classified information is identified | [RULE-01] |
| System media containing classified information is downgraded prior to release to individuals without required access authorizations | [RULE-02], [RULE-03], [RULE-05] |
| Approved sanitization tools and techniques are used | [RULE-02] |
| Downgrading activities are properly documented | [RULE-04] |
| Independent verification of sanitization effectiveness | [RULE-06] |
```