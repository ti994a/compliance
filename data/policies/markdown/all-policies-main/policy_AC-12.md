# POLICY: AC-12: Session Termination

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-12 |
| NIST Control | AC-12: Session Termination |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | session termination, user sessions, automatic logout, inactivity timeout, session disconnect |

## 1. POLICY STATEMENT
All user sessions on organizational systems MUST be automatically terminated when predefined conditions or trigger events occur. Session termination requirements apply to all logical user sessions including local, network, and remote access sessions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid systems |
| User workstations | YES | Local and remote access sessions |
| Web applications | YES | Browser-based and API sessions |
| Database systems | YES | Direct and application-mediated access |
| Mobile applications | YES | Corporate and BYOD devices |
| Service accounts | CONDITIONAL | Only interactive service account sessions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure session timeout settings<br>• Monitor session termination logs<br>• Implement automated termination mechanisms |
| Application Owners | • Define application-specific timeout requirements<br>• Ensure session termination in custom applications<br>• Document session handling procedures |
| Security Team | • Define organization-wide timeout standards<br>• Review and approve timeout configurations<br>• Monitor compliance with session termination requirements |

## 4. RULES
[RULE-01] All systems MUST automatically terminate user sessions after 30 minutes of inactivity for standard users and 15 minutes for privileged users.
[VALIDATION] IF user_type = "standard" AND inactivity_time > 30_minutes AND session_active = TRUE THEN violation
[VALIDATION] IF user_type = "privileged" AND inactivity_time > 15_minutes AND session_active = TRUE THEN violation

[RULE-02] Systems MUST terminate all user sessions during defined maintenance windows and security incidents as specified by the Security Operations Center.
[VALIDATION] IF maintenance_window = TRUE AND active_sessions > 0 THEN violation
[VALIDATION] IF security_incident_level >= "HIGH" AND session_termination_executed = FALSE THEN critical_violation

[RULE-03] Web applications MUST implement both client-side and server-side session timeout mechanisms with server-side enforcement taking precedence.
[VALIDATION] IF application_type = "web" AND server_side_timeout = FALSE THEN violation

[RULE-04] Session termination events MUST be logged with timestamp, user identifier, session duration, and termination reason.
[VALIDATION] IF session_terminated = TRUE AND log_entry_created = FALSE THEN violation

[RULE-05] Systems MUST provide users with a warning notification at least 5 minutes before automatic session termination due to inactivity.
[VALIDATION] IF session_timeout_approaching = TRUE AND warning_displayed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Session Timeout Configuration - Standard procedures for configuring timeout values across different system types
- [PROC-02] Emergency Session Termination - Process for immediate termination of all sessions during security incidents
- [PROC-03] Session Monitoring and Reporting - Regular review of session termination logs and compliance metrics
- [PROC-04] Exception Management - Process for requesting and approving extended session timeouts for business requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving session hijacking, changes to regulatory requirements, major system implementations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard User Inactivity]
IF user_type = "standard"
AND last_activity_time > 30_minutes_ago
AND session_status = "active"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-02: Privileged User Extended Session]
IF user_privileges = "administrative"
AND session_duration > 15_minutes
AND user_activity = "inactive"
AND session_terminated = FALSE
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-03: Security Incident Response]
IF incident_severity = "HIGH"
AND incident_type = "security_breach"
AND active_user_sessions > 0
AND mass_termination_executed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Web Application Session Management]
IF system_type = "web_application"
AND server_side_timeout = "disabled"
AND client_side_timeout = "enabled"
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-05: Missing Session Termination Logs]
IF session_termination_event = TRUE
AND audit_log_entry = "missing"
AND system_type = "in_scope"
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Automatic session termination after defined conditions | RULE-01, RULE-02 |
| Session termination mechanism implementation | RULE-03 |
| Session termination logging and monitoring | RULE-04 |
| User notification before termination | RULE-05 |