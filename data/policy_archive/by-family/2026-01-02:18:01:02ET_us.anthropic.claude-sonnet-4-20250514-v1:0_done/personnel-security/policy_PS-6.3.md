# POLICY: PS-6.3: Post-employment Requirements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-6.3 |
| NIST Control | PS-6.3: Post-employment Requirements |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | post-employment, acknowledgment, legal requirements, information protection, access agreements |

## 1. POLICY STATEMENT
All individuals granted access to organizational information must be notified of applicable, legally binding post-employment requirements for information protection. Individuals must sign acknowledgment of these requirements as part of initial access provisioning to covered information systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Full-time employees | YES | All positions with system access |
| Part-time employees | YES | All positions with system access |
| Contractors | YES | Access to covered information |
| Temporary workers | YES | Access to covered information |
| Interns | YES | Access to covered information |
| Vendors | CONDITIONAL | Only if accessing covered information |
| Visitors | NO | No system access granted |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Security Team | • Develop post-employment requirement notifications<br>• Maintain signed acknowledgment records<br>• Coordinate with Legal on requirement updates |
| Legal Counsel | • Define legally binding post-employment requirements<br>• Review and approve notification language<br>• Advise on enforcement mechanisms |
| Access Administrators | • Verify acknowledgment completion before access provisioning<br>• Maintain access to acknowledgment status |
| Line Managers | • Ensure team members complete acknowledgments<br>• Escalate non-compliance issues |

## 4. RULES
[RULE-01] All individuals MUST be notified of applicable, legally binding post-employment requirements before being granted initial access to covered information.
[VALIDATION] IF initial_access_granted = TRUE AND post_employment_notification = FALSE THEN violation

[RULE-02] Individuals MUST sign written acknowledgment of post-employment requirements as part of initial access provisioning to covered information systems.
[VALIDATION] IF covered_information_access = TRUE AND signed_acknowledgment = FALSE THEN violation

[RULE-03] Post-employment requirement notifications MUST be reviewed and approved by Legal Counsel before implementation.
[VALIDATION] IF notification_document_updated = TRUE AND legal_approval = FALSE THEN violation

[RULE-04] Signed acknowledgment forms MUST be retained for the duration of employment plus seven years after termination.
[VALIDATION] IF acknowledgment_form_exists = TRUE AND retention_period < (employment_end + 7_years) THEN violation

[RULE-05] Access to covered information systems MUST be contingent upon completed and signed post-employment acknowledgments.
[VALIDATION] IF covered_system_access = TRUE AND acknowledgment_status != "completed_signed" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Post-Employment Notification Process - Standardized delivery of legal requirements to new personnel
- [PROC-02] Acknowledgment Collection and Verification - Systematic collection and validation of signed forms
- [PROC-03] Legal Review and Update Process - Periodic review of requirements with counsel
- [PROC-04] Access Provisioning Controls - Integration of acknowledgment verification into access workflows

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Legal requirement changes, regulatory updates, significant security incidents, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee Access Without Acknowledgment]
IF user_type = "new_employee"
AND system_access_requested = TRUE
AND post_employment_acknowledgment = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Accessing Covered Information]
IF user_type = "contractor"
AND covered_information_access = TRUE
AND signed_acknowledgment = TRUE
AND legal_approval_current = TRUE
THEN compliance = TRUE

[SCENARIO-03: Expired Legal Review]
IF notification_document_age > 365_days
AND legal_review_completed = FALSE
AND active_users_count > 0
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Emergency Access Bypass]
IF access_type = "emergency"
AND covered_information_access = TRUE
AND acknowledgment_status = "pending"
AND emergency_justification = TRUE
THEN compliance = CONDITIONAL
required_action = "Complete acknowledgment within 48 hours"

[SCENARIO-05: Acknowledgment Record Retention]
IF employee_termination_date < (current_date - 7_years)
AND acknowledgment_records_retained = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individuals are notified of applicable, legally binding post-employment requirements | [RULE-01] |
| Individuals sign acknowledgment as part of initial access to covered information | [RULE-02], [RULE-05] |
| Legal counsel involvement in post-employment matters | [RULE-03] |
| Documentation and record retention | [RULE-04] |