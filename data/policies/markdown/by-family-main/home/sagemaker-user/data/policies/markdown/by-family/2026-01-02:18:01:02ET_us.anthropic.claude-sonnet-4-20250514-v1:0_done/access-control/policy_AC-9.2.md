# POLICY: AC-9.2: Successful and Unsuccessful Logons

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-9.2 |
| NIST Control | AC-9.2: Successful and Unsuccessful Logons |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | logon notification, authentication, access control, user awareness, security monitoring |

## 1. POLICY STATEMENT
All systems SHALL notify users upon successful logon of the number of successful and unsuccessful logon attempts during a defined time period. This notification enables users to detect unauthorized access attempts and verify the legitimacy of their account activity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid systems |
| Interactive user accounts | YES | Human users requiring logon notification |
| Service accounts | NO | Automated accounts without human interaction |
| Guest accounts | YES | When guest access is permitted |
| Administrative accounts | YES | Enhanced monitoring requirements apply |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure logon notification mechanisms<br>• Define notification time periods<br>• Maintain notification system functionality |
| Security Operations | • Monitor notification system effectiveness<br>• Investigate anomalous logon patterns<br>• Validate notification accuracy |
| End Users | • Review logon notifications upon login<br>• Report suspicious logon activity<br>• Acknowledge notification information |

## 4. RULES

[RULE-01] Systems MUST display logon notification information immediately upon successful user authentication and before granting system access.
[VALIDATION] IF successful_authentication = TRUE AND notification_displayed = FALSE THEN violation

[RULE-02] Logon notifications MUST include the number of successful logons during the preceding 30 days unless a different time period is organizationally defined and documented.
[VALIDATION] IF notification_time_period > 30_days AND custom_period_documented = FALSE THEN violation

[RULE-03] Logon notifications MUST include the number of unsuccessful logon attempts during the same time period as successful logon reporting.
[VALIDATION] IF successful_logons_displayed = TRUE AND unsuccessful_attempts_displayed = FALSE THEN violation

[RULE-04] The logon notification time period MUST be consistently applied across all systems within the same security boundary.
[VALIDATION] IF system_boundary = SAME AND notification_periods != CONSISTENT THEN violation

[RULE-05] Logon notification functionality MUST remain active and cannot be disabled by end users.
[VALIDATION] IF user_can_disable_notification = TRUE THEN critical_violation

[RULE-06] Systems MUST maintain accurate logon attempt records for the defined notification time period plus 90 days for audit purposes.
[VALIDATION] IF logon_records_retention < (notification_period + 90_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Logon Notification Configuration - Standard process for implementing and configuring logon notifications across system types
- [PROC-02] Time Period Definition - Procedure for establishing and documenting notification time periods based on system risk level
- [PROC-03] Notification Testing - Regular validation of logon notification accuracy and functionality
- [PROC-04] User Training - Education program for users on interpreting and responding to logon notifications

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized access, system architecture changes, regulatory requirement updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard User Login]
IF user_type = "standard"
AND authentication_successful = TRUE
AND notification_displayed = TRUE
AND notification_includes_successful_count = TRUE
AND notification_includes_unsuccessful_count = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Unsuccessful Attempts]
IF authentication_successful = TRUE
AND notification_displayed = TRUE
AND notification_includes_successful_count = TRUE
AND notification_includes_unsuccessful_count = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: User-Disabled Notifications]
IF notification_functionality = "disabled"
AND disabled_by = "end_user"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Inconsistent Time Periods]
IF system_A_notification_period = "30_days"
AND system_B_notification_period = "60_days"
AND security_boundary = "same"
AND variance_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Service Account Login]
IF user_type = "service_account"
AND human_interactive = FALSE
AND notification_required = FALSE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| User notification upon successful logon | [RULE-01] |
| Number of successful logons displayed | [RULE-02] |
| Number of unsuccessful attempts displayed | [RULE-03] |
| Consistent time period application | [RULE-04] |
| Non-bypassable notification mechanism | [RULE-05] |
| Adequate record retention for notifications | [RULE-06] |