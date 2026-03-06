# POLICY: AC-9.1: Unsuccessful Logons

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-9.1 |
| NIST Control | AC-9.1: Unsuccessful Logons |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | logon notification, unsuccessful attempts, user notification, authentication, access control |

## 1. POLICY STATEMENT
All information systems MUST notify users upon successful logon of the number of unsuccessful logon attempts since their last successful logon. This notification enables users to detect potential unauthorized access attempts to their accounts.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid systems |
| Service accounts | NO | Automated accounts without interactive logon |
| Emergency access accounts | YES | Must comply during emergency use |
| Contractor systems | YES | When accessing company resources |
| Mobile applications | YES | When providing authentication services |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure logon notification mechanisms<br>• Maintain audit logs for unsuccessful attempts<br>• Test notification functionality |
| Security Team | • Define notification requirements<br>• Monitor compliance across systems<br>• Review unsuccessful logon patterns |
| Application Owners | • Implement notification in custom applications<br>• Ensure notification display standards<br>• Coordinate with security for requirements |

## 4. RULES
[RULE-01] All systems with interactive user logon capabilities MUST display the count of unsuccessful logon attempts since the user's last successful logon immediately upon successful authentication.
[VALIDATION] IF system_type = "interactive" AND successful_logon = TRUE AND notification_displayed = FALSE THEN violation

[RULE-02] The unsuccessful logon count notification MUST be displayed before granting access to system resources and MUST remain visible for a minimum of 5 seconds or until user acknowledgment.
[VALIDATION] IF notification_duration < 5_seconds AND user_acknowledgment = FALSE THEN violation

[RULE-03] Systems MUST maintain accurate records of unsuccessful logon attempts per user account to enable proper notification calculation.
[VALIDATION] IF unsuccessful_attempt_logging = FALSE OR log_accuracy = FALSE THEN violation

[RULE-04] The notification MUST include only the numerical count of unsuccessful attempts and SHALL NOT display specific details about the failed attempts (timestamps, source IPs, etc.).
[VALIDATION] IF notification_includes_details = TRUE THEN violation

[RULE-05] Systems MUST reset the unsuccessful logon counter to zero after displaying the notification and completing successful authentication.
[VALIDATION] IF counter_reset = FALSE AND successful_logon = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Logon Notification Configuration - Standard configuration process for implementing unsuccessful logon notifications across system types
- [PROC-02] Notification Testing Protocol - Regular testing procedures to verify notification functionality and accuracy
- [PROC-03] Audit Log Management - Procedures for maintaining and protecting unsuccessful logon attempt records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: System upgrades, security incidents involving authentication, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard User Logon]
IF user_type = "standard"
AND logon_success = TRUE
AND unsuccessful_attempts_since_last = 3
AND notification_displayed = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Notification Display]
IF successful_logon = TRUE
AND unsuccessful_attempts_since_last > 0
AND notification_displayed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Service Account Authentication]
IF account_type = "service_account"
AND interactive_logon = FALSE
AND notification_not_displayed = TRUE
THEN compliance = TRUE

[SCENARIO-04: Detailed Information Exposure]
IF notification_displayed = TRUE
AND notification_content_includes = "timestamps"
OR notification_content_includes = "source_ip"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Counter Not Reset]
IF successful_logon = TRUE
AND notification_displayed = TRUE
AND unsuccessful_counter_reset = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| User notification upon successful logon of unsuccessful attempts | RULE-01, RULE-02 |
| Accurate tracking of unsuccessful logon attempts | RULE-03 |
| Proper information disclosure in notifications | RULE-04 |
| Counter management after successful authentication | RULE-05 |