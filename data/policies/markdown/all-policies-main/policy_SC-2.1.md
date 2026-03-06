```markdown
# POLICY: SC-2.1: Interfaces for Non-privileged Users

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-2.1 |
| NIST Control | SC-2.1: Interfaces for Non-privileged Users |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | interface_separation, privilege_management, user_interface, system_management, non-privileged_access |

## 1. POLICY STATEMENT
System management functionality MUST be prevented from being presented at interfaces accessible to non-privileged users. Non-privileged users SHALL NOT have visibility or access to administrative options, controls, or system management features through any user interface.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid systems |
| Web applications | YES | All user-facing applications with admin functions |
| Mobile applications | YES | Enterprise and customer-facing mobile apps |
| API interfaces | YES | REST, GraphQL, and other programmatic interfaces |
| Third-party systems | CONDITIONAL | When integrated with company systems |
| Development environments | CONDITIONAL | When containing production-like data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement interface separation controls<br>• Configure role-based access restrictions<br>• Monitor for privilege escalation attempts |
| Application Developers | • Design applications with proper privilege separation<br>• Implement secure UI/UX patterns<br>• Conduct privilege separation testing |
| Security Team | • Define interface separation requirements<br>• Audit system compliance<br>• Investigate privilege violations |

## 4. RULES
[RULE-01] System management functionality MUST NOT be visible or accessible through interfaces presented to non-privileged users.
[VALIDATION] IF user_privilege_level = "non-privileged" AND admin_functionality_visible = TRUE THEN critical_violation

[RULE-02] Administrative options MUST be withheld until users establish authenticated sessions with appropriate administrative privileges.
[VALIDATION] IF admin_session_established = FALSE AND admin_options_available = TRUE THEN violation

[RULE-03] Grey-out or disabled administrative controls MUST NOT be presented to non-privileged users as this still reveals system management capabilities.
[VALIDATION] IF user_privilege_level = "non-privileged" AND (admin_controls_greyed = TRUE OR admin_controls_disabled_visible = TRUE) THEN violation

[RULE-04] Interface designs MUST implement complete separation where non-privileged users cannot discover or enumerate administrative functionality.
[VALIDATION] IF privilege_enumeration_possible = TRUE AND user_privilege_level = "non-privileged" THEN violation

[RULE-05] All systems MUST implement role-based interface presentation that dynamically adjusts based on authenticated user privileges.
[VALIDATION] IF dynamic_interface_adjustment = FALSE OR role_based_presentation = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Interface Design Review - Security review of all user interfaces before deployment
- [PROC-02] Privilege Separation Testing - Automated and manual testing of privilege boundaries
- [PROC-03] Access Control Validation - Quarterly validation of interface access controls
- [PROC-04] Incident Response - Process for handling privilege separation violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, system architecture changes, new application deployments, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Web Application Admin Panel]
IF user_role = "standard_user"
AND admin_menu_items_visible = TRUE
AND system_type = "web_application"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: API Administrative Endpoints]
IF api_user_privilege = "read_only"
AND administrative_endpoints_discoverable = TRUE
AND authentication_level = "standard"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Mobile App Settings]
IF mobile_user_type = "end_user"
AND system_configuration_options_visible = TRUE
AND admin_privileges_granted = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Disabled Admin Controls Visible]
IF user_privilege_level = "non-privileged"
AND admin_buttons_greyed_out = TRUE
AND admin_functionality_hidden = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Privilege-Based Interface]
IF user_authenticated = TRUE
AND interface_content = dynamic_based_on_privileges
AND admin_functions_completely_hidden = TRUE
AND user_privilege_level = "non-privileged"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Presentation of system management functionality is prevented at interfaces to non-privileged users | RULE-01, RULE-02, RULE-03, RULE-04, RULE-05 |
| Administrative privileges not available to general user population | RULE-01, RULE-02 |
| Grey-out options eliminated for accessibility restrictions | RULE-03 |
| System administration options withheld until privileged sessions established | RULE-02, RULE-05 |
```