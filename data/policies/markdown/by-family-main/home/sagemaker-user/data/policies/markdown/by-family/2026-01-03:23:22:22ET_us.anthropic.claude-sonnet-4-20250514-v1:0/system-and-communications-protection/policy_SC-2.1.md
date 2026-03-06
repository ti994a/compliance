# POLICY: SC-2.1: Interfaces for Non-privileged Users

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-2.1 |
| NIST Control | SC-2.1: Interfaces for Non-privileged Users |
| Version | 1.0 |
| Owner | CISO |
| Keywords | interface separation, privilege separation, system management, non-privileged users, administrative functions |

## 1. POLICY STATEMENT
System management functionality SHALL NOT be presented at interfaces accessible to non-privileged users. Administrative options and system management capabilities MUST be restricted to users with appropriate administrative privileges through role-based access controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid |
| Web applications | YES | All user-facing applications |
| Database interfaces | YES | Administrative and user interfaces |
| Network devices | YES | Management interfaces and user portals |
| Third-party systems | YES | When integrated with company systems |
| Development environments | CONDITIONAL | Only production-like environments |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure interface separation controls<br>• Implement privilege-based interface restrictions<br>• Monitor for unauthorized management function exposure |
| Application Developers | • Design applications with separated user/admin interfaces<br>• Implement role-based UI rendering<br>• Ensure administrative functions require elevated privileges |
| Security Team | • Review interface designs for privilege separation<br>• Conduct testing for management function exposure<br>• Define interface separation requirements |

## 4. RULES
[RULE-01] System management functions MUST NOT be visible or accessible through non-privileged user interfaces, including grayed-out or disabled options.
[VALIDATION] IF user_privilege_level = "standard" AND management_functions_visible = TRUE THEN violation

[RULE-02] Administrative interface access MUST require explicit privilege elevation or separate administrative session establishment.
[VALIDATION] IF admin_function_accessed = TRUE AND privilege_elevation_performed = FALSE THEN violation

[RULE-03] User interface rendering MUST be dynamically filtered based on authenticated user privilege levels to prevent exposure of management functionality.
[VALIDATION] IF interface_filtering = "static" OR privilege_based_rendering = FALSE THEN violation

[RULE-04] System management options MUST be withheld from display until users establish sessions with appropriate administrator privileges.
[VALIDATION] IF admin_session_active = FALSE AND management_options_displayed = TRUE THEN violation

[RULE-05] Interface separation controls MUST be tested during system deployment and after configuration changes to verify non-privileged users cannot access management functions.
[VALIDATION] IF interface_testing_completed = FALSE OR testing_date > 30_days_old THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Interface Privilege Review - Quarterly assessment of user interfaces for management function exposure
- [PROC-02] Privilege Elevation Process - Standard procedure for administrative session establishment
- [PROC-03] Interface Testing Protocol - Testing methodology for verifying privilege separation
- [PROC-04] Application Security Review - Security review process for new applications and interface changes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving privilege escalation, new system deployments, major application updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Grayed-Out Admin Options]
IF user_type = "standard_user"
AND admin_functions_visible = TRUE
AND function_state = "grayed_out"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Proper Admin Session]
IF user_type = "administrator"
AND admin_session_established = TRUE
AND management_functions_visible = TRUE
THEN compliance = TRUE

[SCENARIO-03: Contractor Access to Management Interface]
IF user_type = "contractor"
AND privilege_level = "standard"
AND system_management_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Dynamic Interface Filtering]
IF privilege_based_rendering = TRUE
AND user_privilege_level = "standard"
AND management_functions_visible = FALSE
THEN compliance = TRUE

[SCENARIO-05: Privilege Escalation Required]
IF admin_function_requested = TRUE
AND current_session_privilege = "standard"
AND privilege_elevation_prompt = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prevention of system management functionality presentation to non-privileged users | RULE-01, RULE-04 |
| Interface separation implementation | RULE-02, RULE-03 |
| Privilege-based access controls | RULE-02, RULE-04 |
| Testing and verification of controls | RULE-05 |