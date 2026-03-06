# POLICY: PS-5: Personnel Transfer

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-5 |
| NIST Control | PS-5: Personnel Transfer |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | personnel transfer, access review, reassignment, access modification, notification |

## 1. POLICY STATEMENT
When personnel are reassigned or transferred to other positions within the organization, the company must review current access authorizations, modify access as operationally needed, and notify appropriate stakeholders. All transfer actions must be completed within defined timeframes to maintain security posture during organizational changes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Full-time employees | YES | All permanent transfers and reassignments |
| Contractors | YES | Transfers lasting >30 days |
| Temporary staff | CONDITIONAL | Only if transfer >90 days |
| Interns | YES | All transfers between departments |
| Executive leadership | YES | No exceptions for senior roles |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Business Partners | • Initiate transfer workflow within 24 hours<br>• Coordinate with managers on operational needs<br>• Maintain transfer documentation |
| IT Security Team | • Review current access authorizations<br>• Modify system access based on new role<br>• Validate access changes within 72 hours |
| Hiring Managers | • Confirm operational access requirements<br>• Approve access modifications<br>• Document business justification |
| Physical Security | • Update facility access permissions<br>• Issue new badges/keys as needed<br>• Collect old access credentials |

## 4. RULES

[RULE-01] HR MUST initiate personnel transfer review process within 24 hours of transfer notification for permanent reassignments and within 48 hours for extended temporary assignments (>30 days).
[VALIDATION] IF transfer_type = "permanent" AND review_initiated_hours > 24 THEN violation
[VALIDATION] IF transfer_type = "extended_temporary" AND assignment_duration > 30_days AND review_initiated_hours > 48 THEN violation

[RULE-02] All current logical and physical access authorizations MUST be reviewed and confirmed for ongoing operational need within 72 hours of transfer initiation.
[VALIDATION] IF access_review_completed = FALSE AND hours_since_transfer > 72 THEN violation

[RULE-03] Access authorizations MUST be modified within 5 business days to correspond with operational needs of the new position, with critical system access changes completed within 24 hours.
[VALIDATION] IF critical_system_access = TRUE AND modification_hours > 24 THEN critical_violation
[VALIDATION] IF access_modification_days > 5 THEN violation

[RULE-04] Notification MUST be sent to the employee's new manager, IT security team, and facilities management within 24 hours of transfer confirmation.
[VALIDATION] IF required_notifications_sent = FALSE AND notification_hours > 24 THEN violation

[RULE-05] Physical access credentials (badges, keys, parking passes) MUST be updated within 3 business days of transfer, with old credentials deactivated immediately upon new credential issuance.
[VALIDATION] IF physical_credential_update_days > 3 THEN violation
[VALIDATION] IF old_credentials_active = TRUE AND new_credentials_issued = TRUE THEN violation

[RULE-06] Transfer actions and access modifications MUST be documented with business justification and maintained for audit purposes for minimum 3 years.
[VALIDATION] IF transfer_documentation_complete = FALSE OR business_justification = NULL THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Personnel Transfer Workflow - Standardized process for initiating and tracking transfers
- [PROC-02] Access Review and Modification - Systematic review of current permissions against new role requirements  
- [PROC-03] Stakeholder Notification - Automated notification system for transfer communications
- [PROC-04] Physical Credential Management - Process for updating facility access during transfers
- [PROC-05] Transfer Documentation - Requirements for maintaining transfer records and audit trails

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Organizational restructuring, security incidents involving transferred personnel, regulatory changes, failed compliance audits

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Department Transfer]
IF transfer_type = "permanent"
AND departments_different = TRUE
AND access_review_completed = TRUE
AND modifications_within_timeline = TRUE
AND notifications_sent = TRUE
THEN compliance = TRUE

[SCENARIO-02: Delayed Access Review]
IF transfer_initiated = TRUE
AND hours_since_transfer = 96
AND access_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Critical System Access Delay]
IF new_role_requires_critical_access = TRUE
AND critical_access_granted_hours > 24
AND business_justification_documented = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Incomplete Physical Access Update]
IF transfer_completed = TRUE
AND old_badge_active = TRUE
AND new_badge_issued = TRUE
AND days_since_transfer = 2
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Missing Transfer Documentation]
IF transfer_completed = TRUE
AND access_modified = TRUE
AND business_justification = NULL
AND documentation_complete = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Review ongoing operational need for access authorizations | [RULE-02] |
| Initiate transfer actions within defined timeframes | [RULE-01] |
| Modify access authorization based on operational need | [RULE-03] |
| Notify appropriate personnel within defined timeframes | [RULE-04] |
| Manage physical access credentials during transfers | [RULE-05] |
| Document transfer actions and decisions | [RULE-06] |