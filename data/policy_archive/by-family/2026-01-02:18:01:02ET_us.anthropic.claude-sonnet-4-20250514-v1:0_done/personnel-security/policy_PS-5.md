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
When employees are reassigned or transferred to other positions within the organization, all logical and physical access authorizations must be reviewed for ongoing operational need and modified appropriately. Transfer actions and stakeholder notifications must be completed within defined timeframes to maintain security posture.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Permanent and extended duration transfers |
| Contractors | YES | When reassigned between projects/roles |
| Temporary assignments | CONDITIONAL | Only if duration >90 days |
| External users | NO | Covered under different controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Human Resources | • Initiate transfer notifications<br>• Coordinate with security teams<br>• Maintain transfer documentation |
| IT Security Team | • Review access authorizations<br>• Modify system permissions<br>• Validate access changes |
| Direct Managers | • Confirm operational access needs<br>• Approve new role requirements<br>• Document business justification |

## 4. RULES

[RULE-01] HR MUST initiate personnel transfer security review process within 24 hours of approved transfer or reassignment notification.
[VALIDATION] IF transfer_approved = TRUE AND security_review_initiated = FALSE AND elapsed_time > 24_hours THEN violation

[RULE-02] All current logical and physical access authorizations MUST be reviewed and confirmed for ongoing operational need within 5 business days of transfer notification.
[VALIDATION] IF transfer_notification_date + 5_business_days < current_date AND access_review_status != "completed" THEN violation

[RULE-03] Access authorizations MUST be modified within 10 business days to correspond with changes in operational need due to reassignment or transfer.
[VALIDATION] IF access_modification_required = TRUE AND modification_completion_date > transfer_date + 10_business_days THEN violation

[RULE-04] Stakeholders including IT Security, Facilities, and new/old managers MUST be notified of personnel transfers within 48 hours of HR approval.
[VALIDATION] IF transfer_approved = TRUE AND stakeholder_notification_time > 48_hours THEN violation

[RULE-05] Physical access credentials (badges, keys, tokens) MUST be updated or replaced within 5 business days of transfer effective date.
[VALIDATION] IF physical_access_update_required = TRUE AND update_completion_date > transfer_effective_date + 5_business_days THEN violation

[RULE-06] System accounts MUST be reviewed and privileges adjusted to match new role requirements within 3 business days of transfer.
[VALIDATION] IF account_privilege_review_date > transfer_effective_date + 3_business_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Personnel Transfer Security Review - Systematic review of all access rights and operational needs
- [PROC-02] Access Authorization Modification - Process for updating system and facility access permissions  
- [PROC-03] Stakeholder Notification Protocol - Communication workflow for transfer-related security actions
- [PROC-04] Physical Credential Management - Procedures for updating badges, keys, and physical tokens

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Organizational restructuring, security incidents related to transfers, audit findings

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Internal Transfer]
IF employee_transfer = "internal"
AND transfer_type = "permanent"
AND access_review_completed = TRUE
AND modifications_completed_within_timeframe = TRUE
THEN compliance = TRUE

[SCENARIO-02: Delayed Access Review]
IF transfer_notification_date = "2024-01-15"
AND access_review_completion_date = "2024-01-25"
AND required_completion_date = "2024-01-22"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Cross-Department Transfer with Elevated Access]
IF transfer_type = "cross_department"
AND previous_access_level = "elevated"
AND new_role_access_level = "standard"
AND access_downgrade_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Temporary Assignment Extension]
IF assignment_type = "temporary"
AND assignment_duration > 90_days
AND transfer_security_review = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Transfer Notification]
IF transfer_urgency = "emergency"
AND stakeholder_notification_time <= 24_hours
AND access_review_initiated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Review ongoing operational need for access authorizations | RULE-02 |
| Initiate transfer actions within defined timeframe | RULE-01, RULE-03 |
| Modify access authorization based on operational changes | RULE-05, RULE-06 |
| Notify personnel/roles within defined timeframe | RULE-04 |