# POLICY: SC-2.1: Interfaces for Non-privileged Users

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-2.1 |
| NIST Control | SC-2.1: Interfaces for Non-privileged Users |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | interface separation, non-privileged users, system management, administrative functions, user interface |

## 1. POLICY STATEMENT
System interfaces presented to non-privileged users MUST NOT display or provide access to system management functionality. Administrative options and system management capabilities SHALL be completely hidden from non-privileged user interfaces until appropriate administrative privileges are established.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All system interfaces | YES | Web, desktop, mobile, API interfaces |
| Non-privileged user accounts | YES | Standard users, contractors, guests |
| Privileged user accounts | CONDITIONAL | When accessing via non-privileged sessions |
| System management functions | YES | Admin panels, configuration options, system controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure interfaces to hide management functions from non-privileged users<br>• Implement proper session-based privilege escalation<br>• Monitor for unauthorized access attempts |
| Security Team | • Review interface designs for privilege separation<br>• Conduct regular assessments of user interface compliance<br>• Define management functionality classification |
| Development Teams | • Design applications with proper interface separation<br>• Implement role-based UI rendering<br>• Test privilege separation in user interfaces |

## 4. RULES
[RULE-01] System interfaces MUST NOT display management functionality to users without administrative privileges.
[VALIDATION] IF user_privilege_level = "non-privileged" AND management_functions_visible = TRUE THEN violation

[RULE-02] Administrative options SHALL be withheld until users establish sessions with appropriate administrative privileges.
[VALIDATION] IF admin_session_established = FALSE AND admin_options_available = TRUE THEN violation

[RULE-03] Grey-out or disabled administrative options MUST NOT be presented to non-privileged users.
[VALIDATION] IF user_privilege_level = "non-privileged" AND (admin_options_greyed = TRUE OR admin_options_disabled_visible = TRUE) THEN violation

[RULE-04] Interface rendering MUST be based on authenticated user privilege levels and active session permissions.
[VALIDATION] IF interface_rendered = TRUE AND privilege_check_performed = FALSE THEN violation

[RULE-05] System management functionality MUST be accessible only through dedicated administrative interfaces or privilege escalation mechanisms.
[VALIDATION] IF management_function_accessed = TRUE AND (admin_interface = FALSE AND privilege_escalation = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Interface Design Review - Review all user interfaces for proper privilege separation before deployment
- [PROC-02] Privilege Escalation Implementation - Implement secure methods for administrative privilege establishment
- [PROC-03] User Interface Testing - Test interfaces with various privilege levels to ensure proper functionality hiding
- [PROC-04] Management Function Classification - Maintain inventory of system management functions requiring privilege separation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployments, interface modifications, privilege model changes, security incidents involving privilege escalation

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard User Web Interface]
IF user_type = "standard_user"
AND web_interface_loaded = TRUE
AND admin_menu_visible = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Mobile Access]
IF user_type = "contractor"
AND mobile_app_interface = TRUE
AND system_configuration_options_present = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Privileged User Non-Admin Session]
IF user_has_admin_rights = TRUE
AND current_session_privilege = "standard"
AND management_functions_accessible = TRUE
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-04: API Interface Management Endpoints]
IF api_user_privilege = "non-privileged"
AND management_endpoints_discoverable = TRUE
AND access_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Proper Administrative Access]
IF user_privilege_level = "administrator"
AND admin_session_established = TRUE
AND management_functions_visible = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prevention of system management functionality presentation to non-privileged users | [RULE-01], [RULE-02], [RULE-03] |
| Proper interface separation based on user privileges | [RULE-04], [RULE-05] |
| Administrative session establishment before management access | [RULE-02], [RULE-05] |