# POLICY: IA-11: Re-authentication

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-11 |
| NIST Control | IA-11: Re-authentication |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | re-authentication, privileged functions, role changes, authenticator changes, security categories |

## 1. POLICY STATEMENT
Users MUST re-authenticate when specific organizational circumstances or situations occur that increase security risk. Organizations SHALL define clear circumstances requiring re-authentication and implement mechanisms to enforce these requirements across all information systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All users (employees, contractors, vendors) | YES | Applies to all system access |
| Information systems | YES | All systems processing organizational data |
| Privileged accounts | YES | Enhanced re-authentication requirements |
| Guest/temporary accounts | YES | Subject to stricter re-authentication |
| Service accounts | CONDITIONAL | When interactive access is possible |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define re-authentication circumstances<br>• Approve re-authentication policies<br>• Monitor compliance across organization |
| System Administrators | • Implement re-authentication mechanisms<br>• Configure system settings<br>• Monitor re-authentication events |
| Security Operations | • Monitor re-authentication compliance<br>• Investigate re-authentication failures<br>• Report policy violations |
| Users | • Comply with re-authentication requirements<br>• Report re-authentication issues<br>• Maintain current authenticators |

## 4. RULES

[RULE-01] Users MUST re-authenticate when assuming elevated privileges or executing privileged functions.
[VALIDATION] IF privilege_elevation = TRUE AND re_authentication_completed = FALSE THEN violation

[RULE-02] Users MUST re-authenticate when their role or access permissions change within the same session.
[VALIDATION] IF role_change = TRUE AND session_active = TRUE AND re_authentication_completed = FALSE THEN violation

[RULE-03] Users MUST re-authenticate when authenticators or credentials are changed, reset, or updated.
[VALIDATION] IF authenticator_change = TRUE AND re_authentication_completed = FALSE THEN violation

[RULE-04] Users MUST re-authenticate when accessing systems with different security categories or classification levels.
[VALIDATION] IF security_category_change = TRUE AND re_authentication_completed = FALSE THEN violation

[RULE-05] Users MUST re-authenticate after a maximum session duration of 8 hours for standard users and 4 hours for privileged users.
[VALIDATION] IF user_type = "standard" AND session_duration > 8_hours AND re_authentication_completed = FALSE THEN violation
[VALIDATION] IF user_type = "privileged" AND session_duration > 4_hours AND re_authentication_completed = FALSE THEN violation

[RULE-06] Users MUST re-authenticate when accessing high-risk or sensitive data repositories after being idle for more than 15 minutes.
[VALIDATION] IF data_sensitivity = "high" AND idle_time > 15_minutes AND re_authentication_completed = FALSE THEN violation

[RULE-07] Re-authentication mechanisms MUST use the same or stronger authentication factors as the initial authentication.
[VALIDATION] IF re_auth_strength < initial_auth_strength THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Re-authentication Circumstances Definition - Document all situations requiring re-authentication
- [PROC-02] Re-authentication Mechanism Implementation - Deploy and configure re-authentication controls
- [PROC-03] Re-authentication Monitoring - Monitor and audit re-authentication events
- [PROC-04] Re-authentication Exception Handling - Process requests for re-authentication exceptions
- [PROC-05] Re-authentication Incident Response - Respond to re-authentication failures or bypasses

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, system changes, regulatory updates, authentication technology changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Privileged Function Access]
IF user_action = "privileged_function"
AND privilege_level > current_session_privilege
AND re_authentication_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Role Change During Session]
IF role_change_event = TRUE
AND session_active = TRUE
AND re_authentication_timestamp < role_change_timestamp
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Extended Session Duration]
IF user_type = "privileged"
AND session_duration > 4_hours
AND re_authentication_attempts = 0
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Cross-Security-Domain Access]
IF current_security_category != target_security_category
AND re_authentication_completed = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Authenticator Change Event]
IF authenticator_status = "recently_changed"
AND time_since_change < 24_hours
AND re_authentication_completed = TRUE
AND re_auth_method = "new_authenticator"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Users are required to re-authenticate when circumstances requiring re-authentication are defined | [RULE-01], [RULE-02], [RULE-03], [RULE-04], [RULE-05], [RULE-06] |
| Re-authentication mechanisms maintain security strength | [RULE-07] |
| Privileged function re-authentication | [RULE-01] |
| Role change re-authentication | [RULE-02] |
| Credential change re-authentication | [RULE-03] |
| Security category change re-authentication | [RULE-04] |
| Time-based re-authentication | [RULE-05], [RULE-06] |