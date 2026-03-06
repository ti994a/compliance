# POLICY: IA-12.4: In-person Validation and Verification

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-12.4 |
| NIST Control | IA-12.4: In-person Validation and Verification |
| Version | 1.0 |
| Owner | Identity and Access Management Team |
| Keywords | identity proofing, in-person validation, registration authority, identity evidence, physical presence |

## 1. POLICY STATEMENT
All validation and verification of identity evidence for privileged accounts and sensitive system access MUST be conducted through in-person verification before a designated registration authority. This requirement ensures the physical presence of individuals and presentation of physical identity documents to reduce fraudulent credential issuance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Privileged user accounts | YES | All administrative and elevated access accounts |
| Sensitive system access | YES | Systems handling regulated data (SOX, FedRAMP, PCI-DSS) |
| Standard business users | CONDITIONAL | Only for access to FISMA High systems |
| Contractors and vendors | YES | All external personnel requiring system access |
| Emergency accounts | CONDITIONAL | Subject to post-event validation within 72 hours |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Registration Authority | • Conduct in-person identity verification<br>• Validate physical identity documents<br>• Document verification process<br>• Approve or reject identity claims |
| Identity and Access Management Team | • Designate registration authorities<br>• Maintain verification procedures<br>• Monitor compliance<br>• Audit verification records |
| System Owners | • Identify systems requiring in-person verification<br>• Coordinate with registration authorities<br>• Enforce verification requirements |

## 4. RULES
[RULE-01] Identity validation and verification for privileged accounts MUST be conducted in-person before a designated registration authority prior to credential issuance.
[VALIDATION] IF account_type = "privileged" AND verification_method != "in_person" THEN critical_violation

[RULE-02] Physical identity documents MUST be presented and validated during in-person verification sessions.
[VALIDATION] IF verification_session = "in_person" AND physical_documents_validated = FALSE THEN violation

[RULE-03] Registration authorities MUST be formally designated and trained before conducting identity verification activities.
[VALIDATION] IF registration_authority_designation = FALSE OR training_completed = FALSE THEN violation

[RULE-04] In-person verification sessions MUST be documented with date, time, registration authority identity, and verification outcome.
[VALIDATION] IF verification_session_documented = FALSE OR required_fields_missing = TRUE THEN violation

[RULE-05] Remote or virtual identity verification SHALL NOT be accepted for initial privileged account establishment.
[VALIDATION] IF account_type = "privileged" AND initial_verification = TRUE AND verification_method = "remote" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Registration Authority Designation - Process for formally appointing and training registration authorities
- [PROC-02] In-Person Identity Verification - Step-by-step process for conducting face-to-face identity validation
- [PROC-03] Identity Document Validation - Procedures for authenticating physical identity documents
- [PROC-04] Verification Documentation - Requirements for recording verification sessions and outcomes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving identity fraud, changes to regulatory requirements, new system implementations requiring privileged access

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Privileged Account Setup]
IF account_type = "privileged"
AND verification_method = "in_person"
AND physical_documents_validated = TRUE
AND registration_authority_designated = TRUE
THEN compliance = TRUE

[SCENARIO-02: Remote Verification Attempt]
IF account_type = "privileged"
AND verification_method = "video_conference"
AND initial_verification = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Emergency Account Post-Validation]
IF account_type = "emergency"
AND emergency_activated = TRUE
AND post_verification_completed = TRUE
AND verification_timeframe <= 72_hours
THEN compliance = TRUE

[SCENARIO-04: Contractor Access Without In-Person Verification]
IF user_type = "contractor"
AND system_sensitivity = "high"
AND verification_method != "in_person"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Undocumented Verification Session]
IF verification_method = "in_person"
AND session_documented = FALSE
AND account_approved = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Validation and verification conducted in person before designated registration authority | [RULE-01], [RULE-03] |
| Physical presence requirement for identity proofing | [RULE-01], [RULE-05] |
| Designated registration authority involvement | [RULE-03] |
| Documentation of verification process | [RULE-04] |