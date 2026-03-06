# POLICY: AC-12.2: Termination Message

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-12.2 |
| NIST Control | AC-12.2: Termination Message |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | logout, session termination, authentication, explicit message, user notification |

## 1. POLICY STATEMENT
All systems MUST display explicit logout messages to users when authenticated communication sessions are terminated. These messages confirm to users that their authenticated session has ended and they are no longer connected to the system.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Web Applications | YES | All authenticated web sessions |
| Database Systems | YES | All authenticated database connections |
| File Transfer Systems | YES | FTP, SFTP, and similar protocols |
| Remote Access Systems | YES | VPN, SSH, RDP connections |
| Mobile Applications | YES | Apps with authentication |
| Guest Networks | NO | No authentication required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure logout message display mechanisms<br>• Verify proper message delivery<br>• Monitor session termination logs |
| Application Developers | • Implement logout message functionality<br>• Test message display across different session types<br>• Document logout message behavior |
| Security Team | • Define logout message requirements<br>• Audit logout message compliance<br>• Review session termination logs |

## 4. RULES
[RULE-01] All systems with authenticated sessions MUST display an explicit logout message when sessions are terminated either by user action or system timeout.
[VALIDATION] IF session_terminated = TRUE AND logout_message_displayed = FALSE THEN violation

[RULE-02] Logout messages MUST clearly indicate that the authenticated session has ended and the user is no longer connected.
[VALIDATION] IF logout_message_content NOT CONTAINS ["session terminated", "logged out", "connection ended"] THEN violation

[RULE-03] For web-based systems, logout messages MUST be displayed after session termination is complete.
[VALIDATION] IF system_type = "web" AND message_timing = "before_termination" THEN violation

[RULE-04] For protocol-based sessions (FTP, SSH), logout messages MUST be sent as final messages prior to connection termination.
[VALIDATION] IF system_type IN ["FTP", "SSH", "SFTP"] AND message_timing = "after_termination" THEN violation

[RULE-05] Systems MUST log all session terminations and corresponding logout message delivery.
[VALIDATION] IF session_terminated = TRUE AND termination_logged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Logout Message Configuration - Standard procedure for implementing logout messages across different system types
- [PROC-02] Session Termination Monitoring - Process for reviewing session termination logs and message delivery
- [PROC-03] Logout Message Testing - Validation procedures for verifying proper logout message display

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployments, session management changes, security incidents involving session hijacking

## 7. SCENARIO PATTERNS
[SCENARIO-01: Web Application Timeout]
IF session_type = "web"
AND termination_cause = "timeout"
AND logout_message_displayed = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing FTP Logout Message]
IF system_type = "FTP"
AND session_terminated = TRUE
AND logout_message_sent = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Mobile App Manual Logout]
IF system_type = "mobile_app"
AND termination_cause = "user_logout"
AND logout_message_displayed = TRUE
AND message_content_appropriate = TRUE
THEN compliance = TRUE

[SCENARIO-04: Database Connection Termination]
IF system_type = "database"
AND session_terminated = TRUE
AND logout_message_logged = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Incomplete Message Content]
IF logout_message_displayed = TRUE
AND message_content NOT CONTAINS "session terminated"
AND message_clarity = "ambiguous"
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Explicit logout message displayed to users | RULE-01, RULE-02 |
| Message indicates termination of authenticated sessions | RULE-02 |
| Proper timing for different session types | RULE-03, RULE-04 |
| Session termination logging | RULE-05 |