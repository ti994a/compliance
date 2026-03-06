```markdown
# POLICY: AC-6.5: Privileged Accounts

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-6.5 |
| NIST Control | AC-6.5: Privileged Accounts |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | privileged accounts, system administrator, super user, role restriction, access control |

## 1. POLICY STATEMENT
Privileged accounts on all systems SHALL be restricted to specifically authorized personnel or roles based on business necessity and least privilege principles. Day-to-day users SHALL NOT have access to privileged accounts or privileged functions unless explicitly authorized through formal role assignment processes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid |
| Privileged accounts | YES | Super user, admin, service accounts |
| Standard user accounts | CONDITIONAL | Only when requesting privilege escalation |
| Third-party contractors | YES | When requiring privileged access |
| Emergency access accounts | YES | Break-glass and emergency admin accounts |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement privileged account restrictions<br>• Monitor privileged account usage<br>• Maintain account inventory |
| Identity Access Management Team | • Define privileged roles and permissions<br>• Review and approve privileged access requests<br>• Conduct periodic access reviews |
| Security Operations Center | • Monitor privileged account activities<br>• Investigate suspicious privileged access<br>• Report violations to management |

## 4. RULES
[RULE-01] Privileged accounts SHALL be assigned only to personnel whose job functions require administrative access to accomplish specific authorized tasks.
[VALIDATION] IF user_has_privileged_account = TRUE AND job_function_requires_admin = FALSE THEN violation

[RULE-02] Standard users MUST NOT be granted privileged account access for day-to-day operations or routine business functions.
[VALIDATION] IF user_type = "standard" AND has_permanent_privileged_access = TRUE AND justification = "routine_work" THEN violation

[RULE-03] Organizations SHALL maintain a current inventory of all privileged accounts with assigned personnel or roles documented and reviewed quarterly.
[VALIDATION] IF privileged_account_inventory_age > 90_days THEN violation

[RULE-04] Privileged account assignments SHALL be reviewed and reauthorized annually or when personnel change roles.
[VALIDATION] IF privileged_access_last_reviewed > 365_days OR (role_change_date < current_date AND access_not_reviewed = TRUE) THEN violation

[RULE-05] Local and domain privileged accounts MAY have different restriction levels provided the organization retains control over key system configuration parameters.
[VALIDATION] IF account_type = "domain" AND local_restrictions != domain_restrictions AND control_documentation = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privileged Account Request and Approval - Formal process for requesting, justifying, and approving privileged access
- [PROC-02] Quarterly Privileged Account Review - Regular review of all privileged accounts and their assignments
- [PROC-03] Role Change Access Adjustment - Process for modifying access when personnel change roles
- [PROC-04] Privileged Account Monitoring - Continuous monitoring and logging of privileged account activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving privileged accounts, organizational restructuring, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Developer with Admin Rights]
IF user_role = "developer"
AND has_production_admin_access = TRUE
AND business_justification = "code_deployment"
AND automated_deployment_available = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Temporary Privileged Access]
IF access_type = "temporary_privileged"
AND access_duration > 30_days
AND periodic_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Service Account Management]
IF account_type = "service_account"
AND privilege_level = "administrator"
AND assigned_personnel = "multiple_users"
AND individual_accountability = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Role-Based Privileged Access]
IF user_assigned_role = "system_administrator"
AND role_requires_privileged_access = TRUE
AND role_definition_documented = TRUE
AND access_matches_role_requirements = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Access Account]
IF account_type = "emergency_break_glass"
AND privilege_level = "super_user"
AND usage_monitoring = TRUE
AND post_use_review_required = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privileged accounts restricted to authorized personnel/roles | RULE-01, RULE-02 |
| Documentation of privileged account assignments | RULE-03 |
| Regular review and reauthorization of privileged access | RULE-04 |
| Control over system configuration parameters | RULE-05 |
```