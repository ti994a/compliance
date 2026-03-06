```markdown
# POLICY: AC-6.7: Review of User Privileges

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-6.7 |
| NIST Control | AC-6.7: Review of User Privileges |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | privilege review, access control, role validation, least privilege, periodic review |

## 1. POLICY STATEMENT
The organization must establish and maintain a systematic process for regularly reviewing user privileges assigned to roles and classes of users to validate continued need and business justification. Privileges must be reassigned or removed when no longer required to support organizational mission and business needs.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All user accounts | YES | Including employees, contractors, service accounts |
| Privileged roles | YES | Administrative, security, and elevated access roles |
| System accounts | YES | Automated processes and service accounts |
| Guest/temporary accounts | YES | Short-term and visitor access accounts |
| External partner accounts | CONDITIONAL | When accessing internal systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish privilege review policy and frequency<br>• Approve privilege review procedures<br>• Oversee compliance monitoring |
| System Administrators | • Conduct privilege reviews per schedule<br>• Document review findings<br>• Implement privilege changes |
| Business Unit Managers | • Validate business need for user privileges<br>• Approve privilege assignments for their teams<br>• Report organizational changes affecting access needs |
| Identity and Access Management Team | • Maintain privilege inventory<br>• Generate privilege review reports<br>• Track remediation activities |

## 4. RULES
[RULE-01] Privilege reviews for standard user roles MUST be conducted at least annually, and privileged roles MUST be reviewed at least quarterly.
[VALIDATION] IF last_review_date + review_frequency < current_date THEN violation

[RULE-02] All privilege assignments MUST have documented business justification that is validated during each review cycle.
[VALIDATION] IF business_justification = NULL OR justification_validated = FALSE THEN violation

[RULE-03] Privileges identified as no longer needed MUST be removed within 5 business days of review completion.
[VALIDATION] IF privilege_status = "remove_required" AND days_since_review > 5 THEN violation

[RULE-04] Privilege reviews MUST include validation from the user's direct manager and system owner.
[VALIDATION] IF manager_approval = FALSE OR system_owner_approval = FALSE THEN violation

[RULE-05] Emergency or temporary privilege assignments MUST be reviewed within 30 days of assignment.
[VALIDATION] IF privilege_type = "emergency" AND days_since_assignment > 30 AND review_completed = FALSE THEN critical_violation

[RULE-06] Privilege review results MUST be documented with reviewer identity, review date, and disposition for each privilege.
[VALIDATION] IF review_documentation = INCOMPLETE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privilege Inventory Management - Maintain current inventory of all user privileges and role assignments
- [PROC-02] Periodic Privilege Review - Systematic review process for validating privilege assignments
- [PROC-03] Privilege Modification - Process for reassigning or removing privileges based on review findings
- [PROC-04] Exception Handling - Process for managing temporary privilege assignments and emergency access

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Organizational restructuring, system changes, security incidents, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Overdue Standard Review]
IF user_role = "standard"
AND last_privilege_review > 365_days
AND review_status = "pending"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Privileged Account Review Overdue]
IF privilege_level = "administrative"
AND last_privilege_review > 90_days
AND review_status = "not_started"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Privilege Removal Not Executed]
IF review_disposition = "remove_privilege"
AND days_since_review_completion > 5
AND privilege_status = "active"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Business Justification]
IF privilege_assignment_exists = TRUE
AND business_justification = NULL
AND review_completed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Access Extended]
IF privilege_type = "emergency"
AND days_since_assignment > 30
AND privilege_status = "active"
AND extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privileges assigned to roles are defined and reviewed at defined frequency | RULE-01, RULE-06 |
| Reviews validate the need for assigned privileges | RULE-02, RULE-04 |
| Privileges are reassigned or removed when necessary | RULE-03, RULE-05 |
| Review process reflects organizational mission and business needs | RULE-02, RULE-04 |
```