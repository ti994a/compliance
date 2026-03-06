# POLICY: AC-12.3: Timeout Warning Message

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-12.3 |
| NIST Control | AC-12.3: Timeout Warning Message |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | session timeout, warning message, user notification, session termination, access control |

## 1. POLICY STATEMENT
All information systems MUST display explicit warning messages to users indicating pending session termination before automatic logout occurs. Warning messages MUST provide sufficient advance notice to allow users to save work and extend sessions when appropriate.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including web applications, desktop systems, mobile apps |
| Interactive user sessions | YES | Human-to-system interactive sessions only |
| Service accounts | NO | Automated system-to-system connections excluded |
| Public-facing systems | YES | Customer and partner-facing applications included |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure timeout warning mechanisms<br>• Test warning message functionality<br>• Document timeout parameters |
| Application Developers | • Implement warning message displays<br>• Ensure user-friendly notification design<br>• Integrate with session management controls |
| Information Security Team | • Define warning time requirements<br>• Review timeout configurations<br>• Validate compliance implementation |

## 4. RULES
[RULE-01] All interactive systems MUST display an explicit warning message when a user session will terminate due to inactivity timeout.
[VALIDATION] IF system_has_timeout = TRUE AND warning_message_configured = FALSE THEN violation

[RULE-02] Warning messages MUST be displayed at least 2 minutes before session termination for sessions longer than 15 minutes, and at least 30 seconds before termination for shorter sessions.
[VALIDATION] IF session_duration > 15_minutes AND warning_time < 2_minutes THEN violation
[VALIDATION] IF session_duration <= 15_minutes AND warning_time < 30_seconds THEN violation

[RULE-03] Warning messages MUST clearly indicate the remaining time until session termination and provide an option to extend the session.
[VALIDATION] IF warning_message_shows_time = FALSE OR extend_option_available = FALSE THEN violation

[RULE-04] Systems MUST allow users to acknowledge the warning and continue their session without data loss.
[VALIDATION] IF user_acknowledgment_option = FALSE THEN violation

[RULE-05] Warning message timing parameters MUST align with the base timeout values defined in AC-12 policy.
[VALIDATION] IF warning_parameters != AC12_base_parameters THEN configuration_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Session Timeout Configuration - Standardized process for setting timeout and warning parameters
- [PROC-02] Warning Message Testing - Regular validation of warning functionality across all systems
- [PROC-03] User Experience Review - Periodic assessment of warning message usability and effectiveness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployments, user complaints about session timeouts, security incidents related to unattended sessions

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Web Application]
IF system_type = "web_application"
AND user_session_active = TRUE
AND inactivity_detected = TRUE
AND warning_displayed = TRUE
AND warning_time >= 2_minutes
THEN compliance = TRUE

[SCENARIO-02: Mobile Application Short Session]
IF system_type = "mobile_app"
AND session_duration <= 15_minutes
AND warning_time >= 30_seconds
AND extend_option_available = TRUE
THEN compliance = TRUE

[SCENARIO-03: Missing Warning Message]
IF timeout_configured = TRUE
AND warning_message_configured = FALSE
AND session_terminated_automatically = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Insufficient Warning Time]
IF session_duration = 30_minutes
AND warning_time < 2_minutes
AND user_work_lost = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Warning Without Extension Option]
IF warning_message_displayed = TRUE
AND remaining_time_shown = TRUE
AND extend_session_option = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Explicit message display to users indicating session will end | RULE-01, RULE-03 |
| Time until end of session display | RULE-02, RULE-03 |
| User notification and continuation capability | RULE-04 |
| Integration with base AC-12 controls | RULE-05 |