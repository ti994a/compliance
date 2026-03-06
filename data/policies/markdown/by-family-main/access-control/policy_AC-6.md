# POLICY: AC-6: Least Privilege

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-6 |
| NIST Control | AC-6: Least Privilege |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | least privilege, access control, authorization, user privileges, system processes |

## 1. POLICY STATEMENT
All users and system processes SHALL be granted only the minimum access privileges necessary to accomplish their assigned organizational tasks. Access privileges MUST be regularly reviewed and adjusted to maintain least privilege principles across all systems and applications.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Including full-time, part-time, contractors |
| Service accounts | YES | All automated processes and system accounts |
| Administrative accounts | YES | Elevated privileges require additional controls |
| Cloud resources | YES | IaaS, PaaS, SaaS platforms and services |
| Legacy systems | YES | Subject to compensating controls if needed |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Define minimum required privileges for system functions<br>• Approve privilege escalation requests<br>• Conduct quarterly privilege reviews |
| Identity & Access Management Team | • Implement technical controls for least privilege<br>• Monitor privilege usage and violations<br>• Maintain privilege inventory and documentation |
| Security Team | • Audit privilege compliance<br>• Investigate privilege violations<br>• Define privilege standards and baselines |

## 4. RULES

[RULE-01] Users MUST be granted only the minimum privileges necessary to perform their specific job functions and assigned tasks.
[VALIDATION] IF user_privileges > minimum_required_privileges THEN violation

[RULE-02] Administrative privileges MUST be separated from standard user accounts and granted through dedicated administrative accounts.
[VALIDATION] IF standard_account = TRUE AND admin_privileges = TRUE THEN critical_violation

[RULE-03] Privilege reviews MUST be conducted quarterly for all accounts with elevated access and annually for standard user accounts.
[VALIDATION] IF last_privilege_review > 90_days AND elevated_access = TRUE THEN violation
[VALIDATION] IF last_privilege_review > 365_days AND elevated_access = FALSE THEN violation

[RULE-04] System processes and service accounts MUST operate with the minimum privileges required for their intended function.
[VALIDATION] IF process_privileges > functional_requirements THEN violation

[RULE-05] Temporary privilege escalations MUST be documented, approved, time-limited, and automatically revoked upon expiration.
[VALIDATION] IF temp_privilege = TRUE AND (approval = FALSE OR expiration_date < current_date) THEN violation

[RULE-06] Users SHALL NOT share accounts or credentials that would circumvent least privilege controls.
[VALIDATION] IF shared_account_usage = TRUE AND least_privilege_bypass = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privilege Assignment Process - Standardized workflow for requesting and approving access privileges
- [PROC-02] Privilege Review Process - Quarterly and annual review procedures for validating continued need
- [PROC-03] Emergency Access Process - Controlled break-glass procedures for emergency privilege escalation
- [PROC-04] Privilege Monitoring Process - Automated monitoring and alerting for privilege violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving privilege abuse, regulatory changes, significant system changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Developer with Production Admin Access]
IF user_role = "developer"
AND production_admin_access = TRUE
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Service Account with Excessive Privileges]
IF account_type = "service"
AND granted_privileges > minimum_functional_requirements
AND privilege_review_date > 90_days_ago
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Shared Administrative Account Usage]
IF account_type = "administrative"
AND multiple_users_access = TRUE
AND individual_accountability = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Expired Temporary Privilege Escalation]
IF privilege_type = "temporary"
AND current_date > expiration_date
AND auto_revocation = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Standard User with Database Admin Rights]
IF user_classification = "standard"
AND database_admin_privileges = TRUE
AND role_separation = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Employ principle of least privilege for users | [RULE-01], [RULE-02] |
| Apply least privilege to system processes | [RULE-04] |
| Ensure authorized accesses only for assigned tasks | [RULE-01], [RULE-05] |
| Maintain least privilege during development and operation | [RULE-03], [RULE-06] |