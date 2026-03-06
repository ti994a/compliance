# POLICY: AC-9: Previous Logon Notification

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-9 |
| NIST Control | AC-9: Previous Logon Notification |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | logon, notification, authentication, access control, user interface |

## 1. POLICY STATEMENT
All systems MUST notify users of their previous successful logon date and time immediately upon successful authentication. This notification enables users to detect unauthorized access attempts and maintain awareness of their account activity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems requiring user authentication |
| Human User Interfaces | YES | Interactive logon sessions |
| Service Accounts | NO | Automated system-to-system authentication |
| Emergency Access | YES | Including break-glass scenarios |
| Third-party Applications | YES | When integrated with corporate authentication |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure logon notification mechanisms<br>• Maintain accurate timestamp logging<br>• Test notification functionality |
| Security Team | • Define notification requirements<br>• Monitor compliance<br>• Validate notification accuracy |
| Application Owners | • Implement notification in custom applications<br>• Ensure integration with authentication systems |

## 4. RULES
[RULE-01] All systems with human user interfaces MUST display the date and time of the user's last successful logon immediately upon successful authentication.
[VALIDATION] IF system_has_user_interface = TRUE AND successful_logon = TRUE AND previous_logon_displayed = FALSE THEN violation

[RULE-02] Previous logon notifications MUST be displayed before the user gains access to system resources or functionality.
[VALIDATION] IF logon_successful = TRUE AND system_access_granted = TRUE AND notification_displayed = FALSE THEN violation

[RULE-03] The previous logon timestamp MUST be accurate and reflect the actual last successful authentication event for that user account.
[VALIDATION] IF displayed_timestamp != actual_last_logon_timestamp THEN violation

[RULE-04] Systems MUST maintain logon history records to support previous logon notification functionality.
[VALIDATION] IF logon_history_retention < 2_previous_logons THEN violation

[RULE-05] Previous logon notification functionality MUST be tested during system deployment and after authentication system changes.
[VALIDATION] IF system_deployment = TRUE AND notification_testing_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Configuration - Configure authentication systems to capture and display previous logon information
- [PROC-02] Testing Protocol - Validate previous logon notification accuracy during system testing
- [PROC-03] User Training - Educate users on reviewing and reporting suspicious logon notifications
- [PROC-04] Incident Response - Process for handling reports of suspicious previous logon timestamps

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Authentication system changes, security incidents involving unauthorized access, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Web Application Logon]
IF user_authentication = "successful"
AND interface_type = "web_browser"
AND previous_logon_notification = "displayed"
THEN compliance = TRUE

[SCENARIO-02: Missing Previous Logon Display]
IF user_authentication = "successful"
AND system_access = "granted"
AND previous_logon_notification = "not_displayed"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Service Account Authentication]
IF account_type = "service_account"
AND authentication_method = "automated"
AND user_interface = FALSE
THEN compliance = TRUE
exemption_reason = "No human user interface"

[SCENARIO-04: Inaccurate Timestamp Display]
IF previous_logon_displayed = TRUE
AND displayed_timestamp != actual_last_logon
AND timestamp_variance > 5_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: First-time User Logon]
IF user_account = "new"
AND previous_successful_logons = 0
AND notification_message = "first_time_logon"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| User notification upon successful logon of previous logon date and time | RULE-01, RULE-02 |
| Accurate previous logon information display | RULE-03 |
| System capability to maintain logon history | RULE-04 |
| Verification of notification functionality | RULE-05 |