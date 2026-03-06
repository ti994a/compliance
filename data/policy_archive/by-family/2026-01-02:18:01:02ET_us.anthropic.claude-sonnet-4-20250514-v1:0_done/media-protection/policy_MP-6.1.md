```markdown
# POLICY: MP-6.1: Review, Approve, Track, Document, and Verify

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-6.1 |
| NIST Control | MP-6.1: Review, Approve, Track, Document, and Verify |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media sanitization, disposal, tracking, documentation, verification, records retention |

## 1. POLICY STATEMENT
All media sanitization and disposal actions must be reviewed, approved, tracked, documented, and verified to ensure compliance with records retention policies and effective data destruction. Organizations must maintain comprehensive records of all sanitization activities and verify effectiveness before final disposal.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All storage media | YES | Physical and digital media containing organizational data |
| Third-party sanitization vendors | YES | When outsourced sanitization services are used |
| Emergency disposal situations | YES | Expedited process but all steps still required |
| Personal devices with org data | YES | BYOD and contractor devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Custodian | • Review media for sanitization eligibility<br>• Verify records retention compliance<br>• Document media contents and classification |
| Security Officer | • Approve sanitization methods<br>• Verify sanitization effectiveness<br>• Maintain sanitization records |
| IT Operations | • Execute approved sanitization procedures<br>• Track media through disposal process<br>• Perform technical verification |

## 4. RULES
[RULE-01] All media sanitization requests MUST be reviewed and approved by designated security personnel before sanitization begins.
[VALIDATION] IF sanitization_started = TRUE AND approval_status ≠ "approved" THEN violation

[RULE-02] Media sanitization actions MUST be tracked with unique identifiers from initiation through final disposal verification.
[VALIDATION] IF sanitization_record EXISTS AND tracking_id = NULL THEN violation

[RULE-03] Documentation MUST include personnel names, media types, file inventories, sanitization methods, timestamps, and verification results.
[VALIDATION] IF required_documentation_fields < 7 THEN violation

[RULE-04] Sanitization effectiveness MUST be verified through technical testing before media disposal or reuse.
[VALIDATION] IF disposal_authorized = TRUE AND verification_status ≠ "passed" THEN critical_violation

[RULE-05] All sanitization records MUST be retained for minimum 7 years or per applicable regulatory requirements, whichever is longer.
[VALIDATION] IF record_retention_period < 7_years AND regulatory_requirement_period < record_retention_period THEN violation

[RULE-06] Emergency sanitization procedures MUST complete all review, approval, tracking, documentation, and verification steps within 72 hours of action.
[VALIDATION] IF emergency_sanitization = TRUE AND documentation_complete_time > 72_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Sanitization Request and Approval - Formal process for requesting and approving media sanitization
- [PROC-02] Sanitization Tracking and Documentation - Standardized forms and tracking systems for all sanitization activities  
- [PROC-03] Technical Verification Testing - Methods for verifying complete data destruction
- [PROC-04] Records Management and Retention - Long-term storage and retrieval of sanitization records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Security incidents, regulatory changes, failed verifications, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Hard Drive Sanitization]
IF media_type = "hard_drive"
AND approval_status = "approved"
AND sanitization_method = "DoD_5220.22-M"
AND verification_passed = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Approval Documentation]
IF sanitization_completed = TRUE
AND approval_documentation = FALSE
AND emergency_justification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Failed Verification Before Disposal]
IF sanitization_completed = TRUE
AND verification_status = "failed"
AND disposal_authorized = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Tracking Records]
IF sanitization_record EXISTS
AND (tracking_id = NULL OR personnel_names = NULL OR timestamps = NULL)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Third-Party Vendor Sanitization]
IF vendor_sanitization = TRUE
AND vendor_certification_provided = TRUE
AND internal_verification_completed = TRUE
AND chain_of_custody_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Media sanitization actions are reviewed | [RULE-01] |
| Media sanitization actions are approved | [RULE-01] |
| Media sanitization actions are tracked | [RULE-02] |
| Media sanitization actions are documented | [RULE-03] |
| Media sanitization actions are verified | [RULE-04] |
```