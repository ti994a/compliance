# POLICY: PS-6.3: Post-employment Requirements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-6.3 |
| NIST Control | PS-6.3: Post-employment Requirements |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | post-employment, acknowledgment, notification, legal requirements, information protection |

## 1. POLICY STATEMENT
All individuals granted access to covered organizational information must be notified of applicable, legally binding post-employment requirements for information protection. Individuals must sign an acknowledgment of these requirements as part of initial access provisioning.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Full-time employees | YES | All employees with access to covered information |
| Part-time employees | YES | All employees with access to covered information |
| Contractors | YES | When granted access to covered information |
| Temporary workers | YES | When granted access to covered information |
| Interns | YES | When granted access to covered information |
| Volunteers | CONDITIONAL | Only if accessing covered information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Human Resources | • Develop post-employment requirement notifications<br>• Obtain signed acknowledgments during onboarding<br>• Maintain acknowledgment records<br>• Coordinate with Legal on requirement updates |
| Legal Counsel | • Define legally binding post-employment requirements<br>• Review and approve notification language<br>• Advise on enforceability matters |
| Information Security | • Identify covered information categories<br>• Define information protection requirements<br>• Validate acknowledgment completeness |

## 4. RULES
[RULE-01] All individuals MUST be notified of applicable, legally binding post-employment requirements before being granted initial access to covered information.
[VALIDATION] IF individual_granted_access = TRUE AND notification_provided = FALSE THEN violation

[RULE-02] Individuals MUST sign an acknowledgment of post-employment requirements as part of initial access provisioning to covered information.
[VALIDATION] IF access_to_covered_info = TRUE AND signed_acknowledgment = FALSE THEN violation

[RULE-03] Post-employment requirement notifications MUST be reviewed and approved by Legal Counsel before implementation.
[VALIDATION] IF notification_deployed = TRUE AND legal_approval = FALSE THEN violation

[RULE-04] Signed acknowledgment forms MUST be retained for the duration of employment plus 7 years after termination.
[VALIDATION] IF acknowledgment_retention_period < (employment_duration + 7_years) THEN violation

[RULE-05] Post-employment requirements MUST be reviewed annually and updated when legal or regulatory changes occur.
[VALIDATION] IF last_review_date > 365_days AND no_triggering_events = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Post-employment Notification Process - Standardized notification delivery during onboarding
- [PROC-02] Acknowledgment Collection and Storage - Secure collection and retention of signed forms
- [PROC-03] Legal Review Process - Annual review and approval of requirement language
- [PROC-04] Record Retention Management - Systematic retention and disposal of acknowledgment records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Legal/regulatory changes, data breach incidents, merger/acquisition activities

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee Access]
IF employee_type = "new_hire"
AND access_request = "covered_information"
AND notification_provided = TRUE
AND acknowledgment_signed = TRUE
THEN compliance = TRUE

[SCENARIO-02: Contractor Without Acknowledgment]
IF user_type = "contractor"
AND access_granted = TRUE
AND covered_information_access = TRUE
AND signed_acknowledgment = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Legal Requirements]
IF notification_language = "current"
AND legal_review_date > 365_days
AND regulatory_changes = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Notification]
IF initial_access_granted = TRUE
AND covered_information_access = TRUE
AND post_employment_notification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Incomplete Record Retention]
IF employee_terminated = TRUE
AND termination_date > 7_years
AND acknowledgment_records_retained = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individuals notified of post-employment requirements | [RULE-01] |
| Signed acknowledgment required for initial access | [RULE-02] |
| Legal approval of notification content | [RULE-03] |
| Proper record retention | [RULE-04] |
| Regular requirement review | [RULE-05] |