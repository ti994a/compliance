# POLICY: CM-9.1: Assignment of Responsibility

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-9.1 |
| NIST Control | CM-9.1: Assignment of Responsibility |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | configuration management, separation of duties, system development, independence, oversight |

## 1. POLICY STATEMENT
The organization SHALL assign responsibility for developing configuration management processes to personnel who are not directly involved in system development activities. This separation ensures independence and effective oversight of configuration management activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including development, test, and production environments |
| System developers | YES | Subject to separation requirements |
| Configuration management personnel | YES | Must be independent from development |
| Contractors and vendors | YES | When performing development or CM functions |
| Cloud service providers | CONDITIONAL | When organization retains CM responsibility |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Ensure separation of duties policy compliance<br>• Approve CM process assignments<br>• Monitor independence requirements |
| IT Director | • Assign CM responsibilities to appropriate personnel<br>• Maintain organizational separation<br>• Document role assignments |
| Configuration Management Lead | • Develop CM processes independently<br>• Ensure no conflicts of interest<br>• Report separation violations |
| System Development Manager | • Identify personnel involved in development<br>• Support separation requirements<br>• Coordinate with CM teams |

## 4. RULES
[RULE-01] Configuration management process development responsibilities MUST be assigned to personnel who are not directly involved in system development activities.
[VALIDATION] IF cm_personnel_role INTERSECTS development_personnel_role THEN violation

[RULE-02] Organizations MUST maintain documented role assignments that demonstrate separation between CM and development functions.
[VALIDATION] IF role_documentation_exists = FALSE OR separation_documented = FALSE THEN violation

[RULE-03] Personnel assigned to CM process development MUST NOT have direct reporting relationships to system development managers.
[VALIDATION] IF cm_personnel_reports_to = development_manager THEN violation

[RULE-04] Any conflicts of interest or dual roles MUST be documented, approved by CISO, and reviewed quarterly.
[VALIDATION] IF dual_role_exists = TRUE AND (ciso_approval = FALSE OR quarterly_review_current = FALSE) THEN violation

[RULE-05] CM process assignments MUST be reviewed and revalidated annually or when organizational changes occur.
[VALIDATION] IF last_assignment_review > 365_days OR organizational_change_occurred = TRUE AND review_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] CM Role Assignment Process - Define criteria and approval workflow for CM assignments
- [PROC-02] Separation of Duties Validation - Quarterly review of role independence
- [PROC-03] Conflict of Interest Management - Document and manage unavoidable dual roles
- [PROC-04] Organizational Change Assessment - Evaluate CM assignments during restructuring

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Organizational restructuring, new system development projects, CM personnel changes, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Developer Assigned to CM]
IF personnel_role = "system_developer"
AND assigned_to = "configuration_management_process_development"
AND separation_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Reporting Relationship Conflict]
IF cm_lead_manager = development_manager
AND organizational_separation = FALSE
AND ciso_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Small Team Exception]
IF organization_size = "small"
AND dual_role_documented = TRUE
AND ciso_approved = TRUE
AND quarterly_review_current = TRUE
THEN compliance = TRUE

[SCENARIO-04: Contractor Independence]
IF contractor_performs = "development"
AND contractor_performs = "configuration_management"
AND different_contractor_entities = FALSE
AND separation_controls_implemented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Undocumented Role Assignment]
IF cm_process_responsibility_assigned = TRUE
AND role_assignment_documented = FALSE
AND separation_validated = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Responsibility assigned to non-development personnel | RULE-01 |
| Documented role assignments demonstrating separation | RULE-02 |
| Independent reporting relationships | RULE-03 |
| Conflict management and oversight | RULE-04 |
| Regular validation of assignments | RULE-05 |