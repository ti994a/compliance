```markdown
# POLICY: PS-5: Personnel Transfer

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-5 |
| NIST Control | PS-5: Personnel Transfer |
| Version | 1.0 |
| Owner | CISO |
| Keywords | personnel transfer, access review, reassignment, logical access, physical access |

## 1. POLICY STATEMENT
When personnel are reassigned or transferred to other positions within the organization, the company MUST review current access authorizations, modify access as needed, and notify appropriate stakeholders. All transfer actions MUST be completed within defined timeframes to maintain security posture.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Full-time employees | YES | All permanent reassignments/transfers |
| Contractors | YES | Extended duration transfers (>90 days) |
| Temporary staff | CONDITIONAL | Only if transfer duration >30 days |
| Interns | YES | All reassignments |
| Executive staff | YES | No exceptions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Manager | • Initiate transfer notifications<br>• Coordinate with IT Security<br>• Maintain transfer documentation |
| IT Security Team | • Review access authorizations<br>• Modify logical access permissions<br>• Validate access changes |
| Facility Security | • Review physical access needs<br>• Issue/revoke badges and keys<br>• Update facility access systems |
| Direct Managers | • Confirm operational access needs<br>• Approve access modifications<br>• Validate business justification |

## 4. RULES
[RULE-01] HR MUST initiate personnel transfer review process within 24 hours of official transfer notification.
[VALIDATION] IF transfer_notification_received = TRUE AND review_initiated_time > 24_hours THEN violation

[RULE-02] Current logical and physical access authorizations MUST be reviewed and confirmed for ongoing operational need within 3 business days of transfer initiation.
[VALIDATION] IF transfer_initiated = TRUE AND access_review_completed_time > 3_business_days THEN violation

[RULE-03] Access authorizations MUST be modified to correspond with new role requirements within 5 business days of transfer approval.
[VALIDATION] IF transfer_approved = TRUE AND access_modified_time > 5_business_days THEN violation

[RULE-04] Unnecessary access from previous role MUST be revoked within 24 hours of access modification completion.
[VALIDATION] IF access_modified = TRUE AND unnecessary_access_revoked_time > 24_hours THEN critical_violation

[RULE-05] IT Security, Facility Security, and new direct manager MUST be notified within 2 business days of transfer initiation.
[VALIDATION] IF transfer_initiated = TRUE AND (it_security_notified = FALSE OR facility_security_notified = FALSE OR new_manager_notified = FALSE) AND notification_time > 2_business_days THEN violation

[RULE-06] Physical access credentials (badges, keys) MUST be collected from old location and reissued for new location within 3 business days.
[VALIDATION] IF physical_transfer = TRUE AND credential_reissuance_time > 3_business_days THEN violation

[RULE-07] Transfer actions and access modifications MUST be documented with business justification and approval signatures.
[VALIDATION] IF transfer_completed = TRUE AND (documentation_complete = FALSE OR business_justification = FALSE OR approvals_complete = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Personnel Transfer Initiation - HR-initiated process for transfer notifications
- [PROC-02] Access Authorization Review - Systematic review of current logical/physical access
- [PROC-03] Access Modification Workflow - Process for modifying access based on new role
- [PROC-04] Physical Credential Management - Badge/key collection and reissuance process
- [PROC-05] Transfer Documentation - Record-keeping requirements for transfer actions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents related to transferred personnel, audit findings, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Internal Transfer]
IF employee_type = "full-time"
AND transfer_type = "internal_reassignment"
AND transfer_duration = "permanent"
AND access_review_completed_within_3_days = TRUE
AND unnecessary_access_revoked = TRUE
THEN compliance = TRUE

[SCENARIO-02: Delayed Access Review]
IF transfer_initiated = TRUE
AND access_review_completed_time > 3_business_days
AND business_justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Retained Excessive Access]
IF transfer_completed = TRUE
AND previous_role_access_active = TRUE
AND operational_need_justified = FALSE
AND time_since_transfer > 30_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Stakeholder Notification]
IF transfer_type = "cross_department"
AND new_manager_notified = FALSE
AND it_security_notified = TRUE
AND notification_time > 2_business_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Extended Contractor Transfer]
IF user_type = "contractor"
AND transfer_duration > 90_days
AND access_review_completed = TRUE
AND physical_credentials_updated = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Review ongoing operational need for access authorizations | [RULE-02] |
| Initiate transfer actions within defined timeframe | [RULE-01], [RULE-03] |
| Modify access authorization based on operational need changes | [RULE-03], [RULE-04] |
| Notify personnel/roles within defined timeframe | [RULE-05] |
| Document transfer actions and justifications | [RULE-07] |
| Manage physical access credentials during transfer | [RULE-06] |
```