# POLICY: AC-3.7: Role-based Access Control

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-3.7 |
| NIST Control | AC-3.7: Role-based Access Control |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | RBAC, role-based access, access control, authorization, privileges, job functions |

## 1. POLICY STATEMENT
The organization SHALL enforce a role-based access control (RBAC) policy that controls access to system resources based on defined organizational roles and explicitly authorized role assignments. Access permissions SHALL be granted through role inheritance rather than direct user assignments, with roles aligned to specific job functions and business requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid systems |
| All users (employees, contractors, partners) | YES | Subject to role-based access assignments |
| Service accounts | YES | Must be assigned to functional roles |
| Emergency/break-glass accounts | CONDITIONAL | Must have documented exception process |
| Public-facing systems | YES | Internal access components only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity and Access Management Team | • Define and maintain organizational roles<br>• Implement RBAC technical controls<br>• Monitor role assignments and usage |
| System Owners | • Define system-specific roles and permissions<br>• Approve role assignments for their systems<br>• Conduct periodic access reviews |
| HR/People Operations | • Notify IAM team of role changes<br>• Validate job function alignments<br>• Support access reviews |
| Security Team | • Audit RBAC implementation<br>• Monitor for privilege escalation<br>• Validate role separation |

## 4. RULES
[RULE-01] All system access MUST be granted through predefined organizational roles that align with specific job functions and business requirements.
[VALIDATION] IF user_access_method ≠ "role_based" AND exception_approved = FALSE THEN violation

[RULE-02] Direct privilege assignments to individual users SHALL NOT be permitted except for documented emergency access scenarios lasting no more than 72 hours.
[VALIDATION] IF direct_privilege_assignment = TRUE AND emergency_documented = FALSE THEN critical_violation
[VALIDATION] IF direct_privilege_assignment = TRUE AND duration > 72_hours THEN violation

[RULE-03] Role definitions MUST include explicit permission sets, business justification, and approval authority documentation.
[VALIDATION] IF role_definition_complete = FALSE OR business_justification = NULL THEN violation

[RULE-04] Users SHALL only be assigned roles necessary for their current job functions, following least privilege principles.
[VALIDATION] IF user_roles > job_function_requirements AND justification_documented = FALSE THEN violation

[RULE-05] Role assignments MUST be reviewed and revalidated at least quarterly by system owners and annually by role owners.
[VALIDATION] IF last_role_review > 90_days AND system_criticality = "high" THEN violation
[VALIDATION] IF last_role_review > 365_days THEN critical_violation

[RULE-06] Conflicting roles that create segregation of duties violations SHALL NOT be assigned to the same user without documented compensating controls.
[VALIDATION] IF conflicting_roles_assigned = TRUE AND compensating_controls = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Role Definition and Management - Standardized process for creating, modifying, and retiring organizational roles
- [PROC-02] Role Assignment and Approval - Workflow for requesting, approving, and implementing role assignments
- [PROC-03] Periodic Access Review - Quarterly and annual review processes for validating role assignments
- [PROC-04] Emergency Access Management - Break-glass procedures for temporary direct privilege assignments
- [PROC-05] Role Conflict Detection - Automated and manual processes for identifying segregation of duties violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system changes, organizational restructuring, security incidents involving privilege abuse, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Role Assignment]
IF user_type = "employee"
AND job_function_defined = TRUE
AND role_matches_job_function = TRUE
AND approval_documented = TRUE
THEN compliance = TRUE

[SCENARIO-02: Excessive Role Assignment]
IF user_assigned_roles > 3
AND business_justification = FALSE
AND compensating_controls = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Direct Privilege Assignment]
IF access_method = "direct_privilege"
AND emergency_scenario = FALSE
AND duration > 0_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Conflicting Role Assignment]
IF roles_assigned CONTAINS "financial_approver"
AND roles_assigned CONTAINS "financial_preparer"
AND compensating_controls = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Outdated Role Review]
IF last_access_review > 90_days
AND system_classification = "high"
AND user_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Role-based access control policy enforced over defined subjects | [RULE-01], [RULE-04] |
| Role-based access control policy enforced over defined objects | [RULE-01], [RULE-03] |
| Access controlled based on defined organizational roles | [RULE-01], [RULE-02] |
| Users authorized to assume specific roles are defined | [RULE-04], [RULE-05] |
| Role definitions include appropriate authorization scope | [RULE-03], [RULE-06] |