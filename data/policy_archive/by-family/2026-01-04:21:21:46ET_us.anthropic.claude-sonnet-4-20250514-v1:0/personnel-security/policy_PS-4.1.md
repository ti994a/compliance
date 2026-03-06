# POLICY: PS-4.1: Post-employment Requirements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-4.1 |
| NIST Control | PS-4.1: Post-employment Requirements |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | post-employment, termination, acknowledgment, legal requirements, information protection |

## 1. POLICY STATEMENT
All terminated employees and contractors must be notified of legally binding post-employment requirements for protecting organizational information and must sign acknowledgment forms during the termination process. Organizations must establish clear procedures for communicating and documenting these requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Full-time employees | YES | All employment types |
| Contractors | YES | Including temporary and consultant roles |
| Interns | YES | Paid and unpaid positions |
| Board members | YES | When terminating board service |
| Volunteers | CONDITIONAL | If they had access to sensitive information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Personnel | • Notify terminated individuals of post-employment requirements<br>• Obtain signed acknowledgment forms<br>• Maintain termination documentation |
| Legal Counsel | • Define legally binding post-employment requirements<br>• Review and approve acknowledgment forms<br>• Advise on enforcement matters |
| Security Officer | • Identify information protection requirements<br>• Validate termination security procedures<br>• Monitor compliance with post-employment obligations |

## 4. RULES
[RULE-01] All terminated individuals MUST be notified of applicable, legally binding post-employment requirements for protecting organizational information during the termination process.
[VALIDATION] IF termination_initiated = TRUE AND post_employment_notification = FALSE THEN violation

[RULE-02] Terminated individuals MUST sign an acknowledgment form confirming understanding of post-employment requirements before final separation.
[VALIDATION] IF termination_complete = TRUE AND signed_acknowledgment = FALSE THEN violation

[RULE-03] Post-employment requirements MUST be legally binding and reviewed by the Office of General Counsel annually or when changes occur.
[VALIDATION] IF legal_review_date < (current_date - 365_days) THEN violation

[RULE-04] Signed acknowledgment forms MUST be retained for the duration specified by legal requirements, minimum 7 years.
[VALIDATION] IF acknowledgment_retention_period < 7_years THEN violation

[RULE-05] Post-employment notification MUST occur before the individual's final work day and be documented in the termination checklist.
[VALIDATION] IF notification_date > final_work_date THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Termination Notification Process - Standardized communication of post-employment obligations
- [PROC-02] Acknowledgment Collection - Systematic collection and validation of signed forms
- [PROC-03] Legal Review Process - Annual review of post-employment requirements with counsel
- [PROC-04] Documentation Retention - Secure storage and lifecycle management of acknowledgment forms

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Legal requirement changes, regulatory updates, termination process changes, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Employee Termination]
IF employee_status = "terminated"
AND post_employment_notification = TRUE
AND signed_acknowledgment = TRUE
AND notification_date <= final_work_date
THEN compliance = TRUE

[SCENARIO-02: Missing Acknowledgment Form]
IF employee_status = "terminated"
AND post_employment_notification = TRUE
AND signed_acknowledgment = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Contractor Without Notification]
IF user_type = "contractor"
AND contract_status = "terminated"
AND post_employment_notification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Late Notification]
IF termination_initiated = TRUE
AND notification_date > final_work_date
AND signed_acknowledgment = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Outdated Legal Requirements]
IF legal_review_date < (current_date - 365_days)
AND post_employment_requirements_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Terminated individuals are notified of post-employment requirements | [RULE-01], [RULE-05] |
| Terminated individuals sign acknowledgment of requirements | [RULE-02] |
| Requirements are legally binding | [RULE-03] |
| Documentation is properly retained | [RULE-04] |