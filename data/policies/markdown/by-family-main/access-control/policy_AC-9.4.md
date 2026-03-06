# POLICY: AC-9.4: Additional Logon Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-9.4 |
| NIST Control | AC-9.4: Additional Logon Information |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | logon notification, user notification, access control, authentication, session management |

## 1. POLICY STATEMENT
Upon successful user authentication, systems MUST notify users of additional security-relevant information as defined by organizational requirements. This policy ensures users are informed of relevant access details to support security awareness and anomaly detection.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid systems |
| Interactive user sessions | YES | Human users requiring authentication |
| Service accounts | NO | Automated system accounts excluded |
| Emergency access accounts | YES | Must comply during emergency use |
| Third-party applications | YES | When integrated with enterprise authentication |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define additional logon information requirements<br>• Approve exceptions to notification requirements<br>• Oversee policy compliance monitoring |
| System Administrators | • Configure logon notification mechanisms<br>• Maintain notification system functionality<br>• Document system-specific implementations |
| Security Operations | • Monitor logon notification compliance<br>• Investigate notification system failures<br>• Report compliance violations |

## 4. RULES
[RULE-01] Systems MUST display additional logon information immediately upon successful user authentication and before granting system access.
[VALIDATION] IF successful_logon = TRUE AND additional_info_displayed = FALSE THEN violation

[RULE-02] Additional logon information MUST include at minimum: last successful logon timestamp, last logon source location (IP address or device identifier), and number of unsuccessful logon attempts since last successful logon.
[VALIDATION] IF logon_notification_missing_required_elements = TRUE THEN violation

[RULE-03] Logon notifications MUST be displayed for a minimum of 5 seconds or until user acknowledgment, whichever occurs first.
[VALIDATION] IF notification_display_time < 5_seconds AND user_acknowledgment = FALSE THEN violation

[RULE-04] Systems MUST log all instances where additional logon information cannot be displayed due to technical failures.
[VALIDATION] IF notification_failure = TRUE AND failure_logged = FALSE THEN violation

[RULE-05] Additional logon information MUST be accurate and reflect data from the past 90 days maximum.
[VALIDATION] IF logon_info_age > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Logon Notification Configuration - Standard procedures for implementing additional logon information displays across system types
- [PROC-02] Notification Content Management - Process for defining and updating required additional information elements
- [PROC-03] Compliance Monitoring - Regular verification that logon notifications are functioning correctly
- [PROC-04] Exception Handling - Process for managing systems unable to display additional logon information

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving compromised accounts, system architecture changes, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Web Application Logon]
IF user_authentication = "successful"
AND system_type = "web_application"
AND last_logon_info_displayed = TRUE
AND unsuccessful_attempts_shown = TRUE
THEN compliance = TRUE

[SCENARIO-02: Mobile Application Missing Location Info]
IF user_authentication = "successful"
AND system_type = "mobile_app"
AND last_logon_timestamp_shown = TRUE
AND logon_location_shown = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: System with Technical Notification Failure]
IF user_authentication = "successful"
AND notification_system_failure = TRUE
AND failure_logged = TRUE
AND user_granted_access = TRUE
THEN compliance = TRUE
note = "Acceptable if failure is logged and remediated"

[SCENARIO-04: Legacy System Exception]
IF system_type = "legacy"
AND technical_capability = "limited"
AND documented_exception = TRUE
AND compensating_controls = TRUE
THEN compliance = TRUE

[SCENARIO-05: Insufficient Display Time]
IF additional_info_displayed = TRUE
AND display_duration = 2_seconds
AND user_acknowledgment = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| User notification upon successful logon of additional information | RULE-01, RULE-02 |
| Additional information content requirements | RULE-02, RULE-05 |
| Notification display and acknowledgment | RULE-03 |
| Failure logging and monitoring | RULE-04 |