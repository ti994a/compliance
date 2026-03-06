# POLICY: IA-4.4: Identify User Status

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-4.4 |
| NIST Control | IA-4.4: Identify User Status |
| Version | 1.0 |
| Owner | Identity and Access Management Director |
| Keywords | user status, individual identifiers, contractors, foreign nationals, non-organizational users, identity management |

## 1. POLICY STATEMENT
The organization SHALL manage individual identifiers by uniquely identifying each individual and incorporating characteristics that define their organizational status. All user identifiers MUST include status indicators to distinguish between employees, contractors, foreign nationals, and external users for security and operational awareness.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All user accounts | YES | Includes all system access accounts |
| Service accounts | NO | Technical accounts without human association |
| Contractors | YES | Must be clearly identified as non-employee |
| Foreign nationals | YES | Requires special status designation |
| Temporary workers | YES | Must indicate temporary status |
| Vendors/Partners | YES | Must indicate external organization status |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity Management Team | • Define status classification standards<br>• Implement identifier management procedures<br>• Monitor compliance with status identification requirements |
| HR Department | • Provide authoritative status information<br>• Notify IAM of status changes<br>• Validate contractor and foreign national designations |
| System Administrators | • Configure systems to display user status<br>• Implement status-based access controls<br>• Report status identification violations |

## 4. RULES
[RULE-01] All user identifiers MUST include a status indicator that clearly identifies the individual as employee, contractor, foreign national, or external user.
[VALIDATION] IF user_account_created = TRUE AND status_indicator = NULL THEN violation

[RULE-02] User status characteristics MUST be updated within 5 business days of any status change notification from HR.
[VALIDATION] IF status_change_date < (current_date - 5_business_days) AND identifier_updated = FALSE THEN violation

[RULE-03] Contractor identifiers MUST include the contracting organization name and contract end date in the account metadata.
[VALIDATION] IF user_type = "contractor" AND (contracting_org = NULL OR contract_end_date = NULL) THEN violation

[RULE-04] Foreign national status MUST be clearly indicated in all user identifiers and maintained throughout the individual's association with the organization.
[VALIDATION] IF foreign_national = TRUE AND status_indicator != "foreign_national" THEN violation

[RULE-05] Email systems and collaboration tools MUST display user status information when showing user details or participant lists.
[VALIDATION] IF communication_system = TRUE AND status_display_enabled = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] User Status Classification - Process for determining and assigning appropriate status indicators
- [PROC-02] Status Change Management - Procedures for updating identifiers when user status changes
- [PROC-03] Status Verification - Regular validation of user status accuracy against authoritative sources
- [PROC-04] System Configuration - Technical implementation of status display in applications

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Organizational restructuring, new user types, system implementations, security incidents involving user misidentification

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Contractor Account]
IF user_type = "contractor"
AND account_creation_request = TRUE
AND status_indicator = "contractor"
AND contracting_org_specified = TRUE
THEN compliance = TRUE

[SCENARIO-02: Foreign National Without Status]
IF user_citizenship != "US"
AND foreign_national_flag = FALSE
AND account_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Status Change Not Updated]
IF user_status_changed = TRUE
AND change_notification_date < (current_date - 5_business_days)
AND identifier_status = "old_status"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Email Without Status Display]
IF email_system = TRUE
AND user_status_visible = FALSE
AND multi_user_communication = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Contractor Past End Date]
IF user_type = "contractor"
AND contract_end_date < current_date
AND account_active = TRUE
AND status_indicator_current = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Unique identification with status characteristics | RULE-01, RULE-03, RULE-04 |
| Management of individual identifiers | RULE-02, RULE-05 |
| Status-based identification for communication awareness | RULE-05 |
| Contractor identification requirements | RULE-03 |
| Foreign national identification requirements | RULE-04 |