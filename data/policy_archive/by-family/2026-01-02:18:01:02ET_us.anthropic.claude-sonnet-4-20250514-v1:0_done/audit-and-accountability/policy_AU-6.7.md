```markdown
# POLICY: AU-6.7: Permitted Actions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-6.7 |
| NIST Control | AU-6.7: Permitted Actions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit records, permitted actions, least privilege, system processes, audit analysis |

## 1. POLICY STATEMENT
The organization SHALL specify and enforce permitted actions for each system process, role, and user associated with the review, analysis, and reporting of audit record information. All access to audit records MUST follow the principle of least privilege with explicitly defined and documented permissions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Processes | YES | All automated processes handling audit records |
| User Accounts | YES | All accounts with audit record access |
| Service Accounts | YES | Automated systems accessing audit data |
| Third-party Tools | YES | External audit analysis tools |
| Backup Systems | YES | Systems storing audit record copies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve audit record access policies<br>• Review permitted action specifications<br>• Ensure compliance with least privilege |
| Security Operations Manager | • Define permitted actions for SOC processes<br>• Implement technical controls<br>• Monitor audit record access |
| System Administrators | • Configure system-level permissions<br>• Implement permitted action controls<br>• Maintain access control matrices |

## 4. RULES

[RULE-01] Organizations MUST specify permitted actions (read, write, execute, append, delete) for each system process that accesses audit record information.
[VALIDATION] IF system_process_defined = TRUE AND permitted_actions_specified = FALSE THEN violation

[RULE-02] All user roles with audit record access MUST have explicitly documented permitted actions based on job responsibilities and least privilege principles.
[VALIDATION] IF user_has_audit_access = TRUE AND documented_permissions = FALSE THEN violation

[RULE-03] System processes SHALL NOT be granted write, execute, or delete permissions to audit records unless specifically required and approved for their function.
[VALIDATION] IF process_type != "audit_management" AND (write_access = TRUE OR delete_access = TRUE) AND approval_documented = FALSE THEN critical_violation

[RULE-04] Permitted actions for audit record access MUST be technically enforced through system access controls and cannot rely solely on administrative controls.
[VALIDATION] IF technical_enforcement = FALSE AND administrative_only = TRUE THEN violation

[RULE-05] Any changes to permitted actions for audit record access MUST be documented, approved, and implemented within 5 business days.
[VALIDATION] IF permission_change_date > 5_business_days AND implementation_complete = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Audit Access Permission Definition - Document permitted actions for all processes and roles
- [PROC-02] Technical Control Implementation - Configure system-level access controls
- [PROC-03] Permission Change Management - Process for modifying audit record access
- [PROC-04] Access Review and Validation - Regular verification of implemented permissions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving audit records, system changes, role modifications

## 7. SCENARIO PATTERNS

[SCENARIO-01: Analyst Read-Only Access]
IF user_role = "security_analyst"
AND audit_record_access = TRUE
AND permitted_actions = ["read"]
AND write_access = FALSE
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Write Access]
IF system_process = "log_collector"
AND permitted_actions_include = "write"
AND process_function != "audit_management"
AND approval_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Service Account Permissions]
IF account_type = "service_account"
AND audit_access = TRUE
AND permitted_actions_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Management Override]
IF user_role = "system_admin"
AND delete_access = TRUE
AND business_justification = TRUE
AND approval_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Excessive Permissions]
IF user_role = "auditor"
AND permitted_actions = ["read", "write", "delete"]
AND job_requirements = ["read"]
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Permitted actions specified for each system process | RULE-01 |
| Role-based access documentation | RULE-02 |
| Least privilege enforcement | RULE-03 |
| Technical control implementation | RULE-04 |
| Change management for permissions | RULE-05 |
```