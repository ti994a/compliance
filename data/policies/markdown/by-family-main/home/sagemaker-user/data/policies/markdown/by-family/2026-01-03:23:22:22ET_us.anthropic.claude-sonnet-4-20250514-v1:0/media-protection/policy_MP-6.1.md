```markdown
# POLICY: MP-6.1: Review, Approve, Track, Document, and Verify

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-6.1 |
| NIST Control | MP-6.1: Review, Approve, Track, Document, and Verify |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media sanitization, disposal actions, verification, tracking, documentation, approval |

## 1. POLICY STATEMENT
All media sanitization and disposal actions MUST be reviewed, approved, tracked, documented, and verified to ensure compliance with records retention policies and effective data destruction. Organizations SHALL maintain comprehensive records of all sanitization activities and verify effectiveness prior to disposal.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All storage media | YES | Physical and digital media containing organizational data |
| Contractor-owned media | YES | When processing organizational data |
| Personal devices | CONDITIONAL | Only when used for business purposes |
| Cloud storage | YES | Virtual media and storage allocations |
| Backup media | YES | All backup tapes, drives, and storage systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Custodian | • Review media for sanitization eligibility<br>• Ensure compliance with retention policies<br>• Coordinate with Records Management |
| Security Administrator | • Approve sanitization methods<br>• Verify sanitization effectiveness<br>• Maintain sanitization records |
| IT Operations | • Execute approved sanitization procedures<br>• Document sanitization activities<br>• Perform disposal actions |

## 4. RULES
[RULE-01] All media containing sensitive data MUST be reviewed and approved by designated personnel before sanitization or disposal actions.
[VALIDATION] IF media_contains_sensitive_data = TRUE AND review_approval_documented = FALSE THEN violation

[RULE-02] Media sanitization actions MUST be tracked with unique identifiers and maintained in a centralized tracking system.
[VALIDATION] IF sanitization_performed = TRUE AND tracking_record_exists = FALSE THEN violation

[RULE-03] Documentation MUST include personnel names, media types, files stored, sanitization methods, timestamps, and verification results.
[VALIDATION] IF required_documentation_fields < 6 THEN violation

[RULE-04] Sanitization effectiveness MUST be verified through testing or certification before media disposal.
[VALIDATION] IF sanitization_completed = TRUE AND verification_performed = FALSE THEN critical_violation

[RULE-05] All sanitization and disposal records MUST be retained for minimum 7 years or per applicable regulatory requirements.
[VALIDATION] IF record_age > retention_period AND record_destroyed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Review and Approval - Systematic review process for media eligibility
- [PROC-02] Sanitization Tracking - Centralized tracking system maintenance
- [PROC-03] Documentation Standards - Required fields and formats for sanitization records
- [PROC-04] Verification Testing - Methods for confirming sanitization effectiveness
- [PROC-05] Records Retention - Long-term storage and retrieval of sanitization records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Regulatory changes, sanitization failures, audit findings, technology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unverified Hard Drive Disposal]
IF media_type = "hard_drive"
AND sanitization_method = "applied"
AND verification_performed = FALSE
AND disposal_completed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Missing Approval Documentation]
IF media_contains_pii = TRUE
AND sanitization_requested = TRUE
AND approval_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Incomplete Tracking Records]
IF sanitization_performed = TRUE
AND tracking_id = "assigned"
AND personnel_names = "missing"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Compliant Sanitization Process]
IF review_completed = TRUE
AND approval_documented = TRUE
AND tracking_active = TRUE
AND verification_passed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Expired Records Retention]
IF sanitization_date > 7_years_ago
AND regulatory_requirement = "none"
AND records_retained = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Media sanitization and disposal actions are reviewed | [RULE-01] |
| Media sanitization and disposal actions are approved | [RULE-01] |
| Media sanitization and disposal actions are tracked | [RULE-02] |
| Media sanitization and disposal actions are documented | [RULE-03] |
| Media sanitization and disposal actions are verified | [RULE-04] |
```