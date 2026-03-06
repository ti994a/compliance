# POLICY: PS-6.2: Classified Information Requiring Special Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-6.2 |
| NIST Control | PS-6.2: Classified Information Requiring Special Protection |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | classified information, access authorization, personnel security, nondisclosure agreement, SAP, SCI, collateral information |

## 1. POLICY STATEMENT
Access to classified information requiring special protection (collateral, SAP, and SCI) SHALL only be granted to individuals who possess valid access authorizations, satisfy personnel security criteria, and have executed required nondisclosure agreements. All access decisions MUST be documented and verified before granting access to special protection classified materials.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal employees | YES | All clearance levels |
| Contractors | YES | When requiring classified access |
| Consultants | YES | When requiring classified access |
| Visitors | YES | When requiring classified access |
| Systems processing classified data | YES | All classification levels |
| Cloud services | CONDITIONAL | Only FedRAMP High authorized |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Control Assessor | • Verify access authorizations match duties<br>• Validate personnel security criteria compliance<br>• Audit nondisclosure agreement execution |
| Personnel Security Manager | • Maintain personnel security criteria<br>• Process clearance verifications<br>• Manage nondisclosure agreement lifecycle |
| System Owner | • Define classified information access requirements<br>• Approve access based on official duties<br>• Monitor ongoing access appropriateness |

## 4. RULES
[RULE-01] Access to classified information requiring special protection MUST be granted only to individuals with valid access authorizations demonstrated by assigned official government duties.
[VALIDATION] IF access_requested = TRUE AND (valid_authorization = FALSE OR official_duties_documented = FALSE) THEN access_denied

[RULE-02] Personnel security criteria MUST be satisfied and verified before granting access to classified information requiring special protection.
[VALIDATION] IF personnel_security_criteria_met = FALSE OR verification_completed = FALSE THEN access_denied

[RULE-03] Individuals MUST read, understand, and sign a nondisclosure agreement before accessing classified information requiring special protection.
[VALIDATION] IF (nda_read = FALSE OR nda_understood = FALSE OR nda_signed = FALSE) THEN access_denied

[RULE-04] Access authorizations MUST be revalidated annually and whenever duties change significantly.
[VALIDATION] IF last_revalidation_date > 365_days OR duties_changed = TRUE AND revalidation_completed = FALSE THEN access_suspended

[RULE-05] All access grants and denials MUST be documented with justification and approval authority.
[VALIDATION] IF access_decision_documented = FALSE OR justification_provided = FALSE OR approver_identified = FALSE THEN compliance_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Access Authorization Verification - Validate clearance level and scope against duty requirements
- [PROC-02] Personnel Security Criteria Assessment - Evaluate background investigation currency and adjudication
- [PROC-03] Nondisclosure Agreement Management - Ensure proper execution and understanding documentation
- [PROC-04] Periodic Access Revalidation - Annual review of continued access need and authorization

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents, personnel changes, classification guide updates, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee Access Request]
IF employee_status = "new"
AND classified_access_requested = TRUE
AND clearance_level_verified = TRUE
AND personnel_criteria_met = TRUE
AND nda_signed = TRUE
AND official_duties_require_access = TRUE
THEN compliance = TRUE

[SCENARIO-02: Contractor Without NDA]
IF user_type = "contractor"
AND classified_access_granted = TRUE
AND nda_signed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Expired Clearance Access]
IF clearance_expiration_date < current_date
AND classified_access_active = TRUE
AND revalidation_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Duty Change Without Revalidation]
IF official_duties_changed = TRUE
AND duties_change_date > 30_days_ago
AND access_revalidation_completed = FALSE
AND classified_access_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Incomplete Personnel Security Criteria]
IF personnel_security_investigation_current = FALSE
OR adjudication_favorable = FALSE
AND classified_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Valid access authorization demonstrated by official duties | [RULE-01] |
| Associated personnel security criteria satisfied | [RULE-02] |
| Nondisclosure agreement read, understood, and signed | [RULE-03] |
| Ongoing authorization validation | [RULE-04] |
| Documentation and approval requirements | [RULE-05] |