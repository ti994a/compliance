# POLICY: AC-5: Separation of Duties

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-5 |
| NIST Control | AC-5: Separation of Duties |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | separation of duties, access control, privilege abuse, role segregation, authorization |

## 1. POLICY STATEMENT
The organization SHALL identify, document, and enforce separation of duties to prevent abuse of authorized privileges and reduce risk of malevolent activity without collusion. System access authorizations MUST be defined and implemented to support proper separation of critical functions across different individuals and roles.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Including full-time, part-time, contractors |
| System administrators | YES | Special focus on privileged access |
| Security personnel | YES | Cannot administer both access control and audit functions |
| Business applications | YES | All systems processing sensitive data |
| Cloud infrastructure | YES | Including hybrid and multi-cloud environments |
| Third-party vendors | YES | When accessing company systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define separation of duties policy<br>• Approve high-risk role combinations<br>• Oversee policy compliance |
| System Owners | • Identify critical functions requiring separation<br>• Document role-based access requirements<br>• Monitor for violations |
| IAM Team | • Implement technical controls for separation<br>• Configure role-based access controls<br>• Maintain access authorization matrix |
| Audit Team | • Monitor compliance with separation requirements<br>• Report violations and conflicts<br>• Validate control effectiveness |

## 4. RULES

[RULE-01] Critical business functions MUST be divided among different individuals with no single person having complete control over an entire critical process.
[VALIDATION] IF user_roles CONTAINS conflicting_critical_functions AND exception_approved = FALSE THEN violation

[RULE-02] Security personnel who administer access control functions MUST NOT also administer audit functions on the same systems.
[VALIDATION] IF user_role = "security_admin" AND (access_control_admin = TRUE AND audit_admin = TRUE) THEN critical_violation

[RULE-03] Financial transaction processes MUST require approval from at least two authorized individuals with segregated roles.
[VALIDATION] IF transaction_type = "financial" AND approver_count < 2 THEN violation

[RULE-04] System administrators MUST NOT have the ability to modify or delete their own audit logs.
[VALIDATION] IF user_type = "system_admin" AND audit_log_modify_permission = TRUE AND target_logs = "own_activities" THEN critical_violation

[RULE-05] Database administrators MUST NOT have direct access to production application data without business user approval and logging.
[VALIDATION] IF user_role = "dba" AND data_access = "direct_production" AND (business_approval = FALSE OR logging_enabled = FALSE) THEN violation

[RULE-06] Code deployment to production MUST require separation between code developers and deployment personnel.
[VALIDATION] IF environment = "production" AND developer_id = deployer_id THEN violation

[RULE-07] Incompatible role combinations MUST be documented, reviewed quarterly, and approved by CISO for any exceptions.
[VALIDATION] IF role_combination IN incompatible_roles_list AND (exception_approved = FALSE OR exception_age > 90_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Role Compatibility Assessment - Evaluate new roles for separation conflicts
- [PROC-02] Access Authorization Matrix - Maintain current mapping of roles to system access
- [PROC-03] Separation Violation Monitoring - Automated detection and alerting for conflicts
- [PROC-04] Exception Management - Process for documenting and approving necessary exceptions
- [PROC-05] Quarterly Access Review - Regular validation of role assignments and separations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, organizational changes, new system implementations, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Developer with Production Access]
IF user_role = "developer"
AND production_access = TRUE
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Security Admin Managing Own Audit Logs]
IF user_role = "security_administrator"
AND audit_admin_rights = TRUE
AND access_control_admin_rights = TRUE
AND same_system = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Financial Process Single Approver]
IF process_type = "financial_transaction"
AND transaction_amount > approval_threshold
AND approver_count = 1
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Approved Exception with Documentation]
IF role_combination IN incompatible_roles
AND exception_documented = TRUE
AND ciso_approval = TRUE
AND exception_age <= 90_days
THEN compliance = TRUE

[SCENARIO-05: Emergency Access Without Monitoring]
IF access_type = "emergency_override"
AND separation_bypassed = TRUE
AND (monitoring_enabled = FALSE OR post_review_completed = FALSE)
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Duties requiring separation are identified and documented | [RULE-01], [RULE-07] |
| System access authorizations support separation of duties | [RULE-02], [RULE-05], [RULE-06] |
| Security personnel access controls are segregated | [RULE-02], [RULE-04] |
| Financial controls enforce separation | [RULE-03] |
| Technical controls prevent privilege abuse | [RULE-04], [RULE-05], [RULE-06] |