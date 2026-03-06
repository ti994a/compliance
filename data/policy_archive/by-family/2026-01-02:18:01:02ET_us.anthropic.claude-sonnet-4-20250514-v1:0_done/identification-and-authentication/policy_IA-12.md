# POLICY: IA-12: Identity Proofing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-12 |
| NIST Control | IA-12: Identity Proofing |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | identity proofing, identity assurance, user verification, account registration, identity evidence |

## 1. POLICY STATEMENT
All users requiring accounts for logical access to organizational systems MUST undergo identity proofing based on appropriate identity assurance levels as specified in NIST SP 800-63A. User identities SHALL be resolved to a unique individual through collection, validation, and verification of identity evidence before account establishment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full identity proofing required |
| Contractors | YES | Same requirements as employees |
| External partners | YES | Risk-based identity assurance levels |
| Service accounts | NO | Technical accounts excluded |
| Guest accounts | CONDITIONAL | Based on access level and duration |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity Management Team | • Conduct identity proofing processes<br>• Validate identity evidence<br>• Maintain proofing documentation |
| System Owners | • Define identity assurance level requirements<br>• Approve access based on proofing results |
| Privacy Officer | • Ensure compliance with privacy requirements<br>• Review identity evidence collection practices |

## 4. RULES

[RULE-01] Identity proofing MUST be completed for all users before granting logical access to any organizational system.
[VALIDATION] IF user_account_created = TRUE AND identity_proofing_completed = FALSE THEN violation

[RULE-02] Identity assurance levels SHALL be determined based on NIST SP 800-63A guidelines and system risk categorization.
[VALIDATION] IF system_risk_level = "high" AND identity_assurance_level < "IAL2" THEN violation

[RULE-03] User identities MUST resolve to a unique individual with no ambiguity or duplication.
[VALIDATION] IF identity_resolution_status = "ambiguous" OR duplicate_identity_detected = TRUE THEN violation

[RULE-04] Identity evidence collection MUST include at least two forms of acceptable documentation as defined in organizational standards.
[VALIDATION] IF identity_evidence_count < 2 OR evidence_acceptable = FALSE THEN violation

[RULE-05] Identity evidence validation MUST verify authenticity and integrity of submitted documentation within 5 business days.
[VALIDATION] IF validation_completion_time > 5_business_days OR validation_status = "failed" THEN violation

[RULE-06] Identity verification MUST confirm that the applicant is the rightful owner of the claimed identity through approved methods.
[VALIDATION] IF verification_method NOT IN approved_methods OR verification_result = "failed" THEN violation

[RULE-07] Identity proofing documentation MUST be retained for the duration of account lifecycle plus 3 years.
[VALIDATION] IF account_closed = TRUE AND documentation_retention_period < 3_years THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Identity Assurance Level Determination - Risk-based assessment to determine appropriate IAL
- [PROC-02] Identity Evidence Collection - Standardized process for gathering required documentation
- [PROC-03] Identity Validation Process - Verification of document authenticity and integrity
- [PROC-04] Identity Verification Process - Confirmation of identity ownership
- [PROC-05] Documentation Retention - Secure storage and lifecycle management of proofing records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Regulatory changes, security incidents involving identity compromise, technology changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: High-Risk System Access]
IF system_classification = "high_risk"
AND user_access_requested = TRUE
AND identity_assurance_level < "IAL2"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Identity Evidence]
IF identity_proofing_initiated = TRUE
AND identity_evidence_count < 2
AND account_creation_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Expired Verification Timeline]
IF identity_evidence_submitted = TRUE
AND validation_start_date + 5_business_days < current_date
AND validation_status = "pending"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Duplicate Identity Detection]
IF identity_verification_completed = TRUE
AND duplicate_identity_flag = TRUE
AND account_provisioned = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Contractor Remote Access]
IF user_type = "contractor"
AND access_type = "remote"
AND identity_assurance_level >= "IAL2"
AND verification_method IN approved_methods
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Users identity proofed based on appropriate assurance levels | [RULE-01], [RULE-02] |
| User identities resolved to unique individual | [RULE-03] |
| Identity evidence collected | [RULE-04] |
| Identity evidence validated | [RULE-05] |
| Identity evidence verified | [RULE-06] |