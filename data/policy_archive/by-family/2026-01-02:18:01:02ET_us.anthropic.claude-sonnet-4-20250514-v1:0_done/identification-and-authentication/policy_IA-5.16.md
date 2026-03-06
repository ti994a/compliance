# POLICY: IA-5.16: In-person or Trusted External Party Authenticator Issuance

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5.16 |
| NIST Control | IA-5.16: In-person or Trusted External Party Authenticator Issuance |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authenticator, issuance, in-person, registration authority, identity proofing, trusted party |

## 1. POLICY STATEMENT
All defined high-assurance authenticators MUST be issued through in-person verification before an authorized registration authority or through a verified trusted external party. This policy ensures the integrity of identity proofing processes for critical system access credentials.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Privileged access authenticators | YES | Administrative and elevated privilege credentials |
| PIV/CAC cards | YES | Government and contractor identity credentials |
| Hardware security keys (FIDO2) | YES | Multi-factor authentication tokens |
| Digital certificates (high assurance) | YES | PKI certificates for system authentication |
| Standard employee badges | CONDITIONAL | Only if used for system access |
| Temporary/guest credentials | NO | Lower assurance acceptable |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Registration Authority | • Conduct in-person identity verification<br>• Validate supporting documentation<br>• Issue authenticators per established procedures |
| Identity Management Office | • Define authenticator types requiring in-person issuance<br>• Maintain approved trusted external party list<br>• Oversee registration authority operations |
| Security Operations | • Monitor authenticator issuance compliance<br>• Investigate irregular issuance patterns<br>• Maintain audit logs of issuance activities |

## 4. RULES
[RULE-01] High-assurance authenticators as defined in the organization's authenticator classification matrix MUST be issued only through in-person verification before an authorized registration authority.
[VALIDATION] IF authenticator_type IN high_assurance_list AND issuance_method != "in_person_RA" THEN violation

[RULE-02] Trusted external parties used for authenticator issuance MUST be pre-approved, contractually bound to organization security requirements, and subject to annual security assessments.
[VALIDATION] IF issuance_party = "external" AND (approval_status != "current" OR security_assessment_age > 365_days) THEN violation

[RULE-03] Registration authorities MUST verify a minimum of two forms of government-issued identification and perform identity proofing consistent with NIST SP 800-63A Identity Assurance Level 3 requirements.
[VALIDATION] IF id_documents_verified < 2 OR identity_assurance_level < "IAL3" THEN violation

[RULE-04] All authenticator issuance activities MUST be logged with requestor identity, authorizing personnel, registration authority, and issuance timestamp within the identity management system.
[VALIDATION] IF authenticator_issued = TRUE AND (audit_log_entry = FALSE OR required_fields_missing = TRUE) THEN violation

[RULE-05] Personnel authorized to approve high-assurance authenticator issuance MUST hold minimum Secret clearance or equivalent background investigation and complete annual identity management training.
[VALIDATION] IF approver_clearance_level < "Secret" OR training_completion_date > 365_days_ago THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Identity Proofing and Verification - Standardized process for in-person identity validation
- [PROC-02] Trusted External Party Vetting - Assessment and approval process for third-party issuers
- [PROC-03] Registration Authority Certification - Training and authorization for RA personnel
- [PROC-04] Authenticator Lifecycle Management - Issuance through revocation tracking

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Security incidents involving authenticator compromise, changes to NIST guidance, new authenticator technologies

## 7. SCENARIO PATTERNS
[SCENARIO-01: Remote PIV Card Issuance]
IF authenticator_type = "PIV_card"
AND issuance_method = "remote"
AND emergency_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Using Approved External Party]
IF user_type = "contractor"
AND issuance_party = "external_trusted"
AND party_approval_status = "current"
AND security_assessment_date < 365_days_ago
THEN compliance = TRUE

[SCENARIO-03: Unauthorized Registration Authority]
IF registration_authority_id NOT IN approved_RA_list
AND authenticator_type IN high_assurance_list
AND authenticator_issued = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Insufficient Identity Proofing]
IF identity_documents_count = 1
AND authenticator_type = "hardware_security_key"
AND system_classification = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Missing Audit Trail]
IF authenticator_issued = TRUE
AND audit_log_complete = FALSE
AND issuance_date > 24_hours_ago
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Defined authenticator types require in-person issuance | [RULE-01] |
| Issuance conducted before authorized registration authority | [RULE-01], [RULE-03] |
| Authorization by defined personnel/roles | [RULE-05] |
| Trusted external party requirements | [RULE-02] |
| Identity proofing standards | [RULE-03] |
| Audit and accountability | [RULE-04] |