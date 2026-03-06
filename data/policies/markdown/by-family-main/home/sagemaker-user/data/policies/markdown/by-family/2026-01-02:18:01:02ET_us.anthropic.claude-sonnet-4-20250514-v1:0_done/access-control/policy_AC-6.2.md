# POLICY: AC-6.2: Non-privileged Access for Nonsecurity Functions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-6.2 |
| NIST Control | AC-6.2: Non-privileged Access for Nonsecurity Functions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | privileged access, non-privileged accounts, security functions, role separation, least privilege |

## 1. POLICY STATEMENT
Users with privileged system accounts or roles that provide access to security functions or security-relevant information must use separate non-privileged accounts when accessing non-security functions. This separation limits exposure and enforces the principle of least privilege across all system operations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System administrators | YES | All privileged administrative accounts |
| Security personnel | YES | Users with access to security functions |
| Database administrators | YES | Users with elevated database privileges |
| Network administrators | YES | Users with network security access |
| Application administrators | YES | Users with application security controls |
| End users | CONDITIONAL | Only if granted privileged access |
| Service accounts | YES | Automated accounts with security functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Maintain separate privileged and non-privileged accounts<br>• Use non-privileged accounts for email, web browsing, document editing<br>• Document account separation requirements |
| Security Team | • Define security functions requiring privileged access<br>• Monitor compliance with account separation<br>• Review privileged account usage patterns |
| IT Management | • Enforce account separation policies<br>• Provision appropriate account types<br>• Conduct regular access reviews |

## 4. RULES
[RULE-01] Users with privileged accounts or roles SHALL maintain separate non-privileged accounts for accessing non-security functions including email, web browsing, and document management.
[VALIDATION] IF user_has_privileged_account = TRUE AND non_privileged_account_exists = FALSE THEN violation

[RULE-02] Non-security functions MUST NOT be performed using privileged accounts or roles that have access to security functions or security-relevant information.
[VALIDATION] IF account_type = "privileged" AND function_type = "non-security" AND access_granted = TRUE THEN violation

[RULE-03] Organizations MUST define and document which users require non-privileged account separation based on their access to security functions.
[VALIDATION] IF user_has_security_access = TRUE AND separation_requirement_documented = FALSE THEN violation

[RULE-04] Privileged accounts SHALL only be used for security functions, security administration, and security-relevant information access.
[VALIDATION] IF account_type = "privileged" AND activity_type NOT IN ["security_function", "security_admin", "security_info"] THEN violation

[RULE-05] Role-based access implementations MUST provide equivalent assurance when changing between privileged and non-privileged roles as changing between different account types.
[VALIDATION] IF access_control_type = "role_based" AND role_change_assurance < account_change_assurance THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privileged Account Provisioning - Define process for creating separated privileged and non-privileged accounts
- [PROC-02] Security Function Classification - Document which functions require privileged access
- [PROC-03] Account Usage Monitoring - Monitor and audit privileged account activities
- [PROC-04] Role Transition Controls - Implement secure role changing mechanisms for RBAC systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving privileged accounts, organizational changes, new security functions

## 7. SCENARIO PATTERNS
[SCENARIO-01: Administrator Email Access]
IF user_role = "system_administrator"
AND account_type = "privileged"
AND activity = "email_access"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Proper Account Separation]
IF user_has_privileged_account = TRUE
AND non_privileged_account_exists = TRUE
AND current_activity = "document_editing"
AND current_account_type = "non_privileged"
THEN compliance = TRUE

[SCENARIO-03: Security Function Access]
IF user_role = "security_analyst"
AND activity = "firewall_configuration"
AND account_type = "privileged"
THEN compliance = TRUE

[SCENARIO-04: Undocumented Privileged User]
IF user_has_security_function_access = TRUE
AND separation_requirement_documented = FALSE
AND privileged_account_exists = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Role-Based Access Control]
IF access_control_method = "RBAC"
AND current_role = "privileged_security_role"
AND activity = "web_browsing"
AND role_separation_enforced = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Users requiring non-privileged account separation are defined | [RULE-03] |
| Non-privileged accounts used for non-security functions | [RULE-01], [RULE-02] |
| Privileged accounts limited to security functions | [RULE-04] |
| Role-based access provides equivalent assurance | [RULE-05] |