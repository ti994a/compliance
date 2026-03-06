```markdown
# POLICY: CA-6: Authorization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CA-6 |
| NIST Control | CA-6: Authorization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authorization, authorizing official, common controls, system authorization, continuous monitoring, reauthorization |

## 1. POLICY STATEMENT
Senior officials must be designated as authorizing officials for systems and common controls, with explicit responsibility for authorizing system operations and accepting associated risks. All systems require formal authorization before commencing operations, and authorizations must be maintained through continuous monitoring and periodic updates.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| Common Control Providers | YES | Controls available for inheritance |
| Federal Employees in Senior Roles | YES | Eligible for authorizing official designation |
| Contractor Systems | CONDITIONAL | Must have federal authorizing official |
| Development/Test Systems | CONDITIONAL | Based on data sensitivity and connectivity |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Authorizing Official (AO) | • Issue system authorization decisions<br>• Accept organizational risk<br>• Provide budgetary oversight<br>• Review continuous monitoring results |
| Common Control Provider | • Implement and maintain common controls<br>• Provide inheritance documentation<br>• Support authorization activities |
| System Owner | • Prepare authorization packages<br>• Implement continuous monitoring<br>• Maintain system documentation |

## 4. RULES

[RULE-01] Each information system MUST have a designated senior federal employee as the authorizing official before commencing operations.
[VALIDATION] IF system_status = "operational" AND authorizing_official_designated = FALSE THEN critical_violation

[RULE-02] Each common control provider MUST have a designated senior federal employee as the authorizing official for controls available for inheritance.
[VALIDATION] IF common_controls_available = TRUE AND common_control_ao_designated = FALSE THEN critical_violation

[RULE-03] The system authorizing official MUST formally accept the use of inherited common controls before system authorization.
[VALIDATION] IF inherited_controls_count > 0 AND common_controls_acceptance = FALSE THEN violation

[RULE-04] The authorizing official MUST issue written authorization for the system to operate before production deployment.
[VALIDATION] IF system_status = "production" AND written_authorization_issued = FALSE THEN critical_violation

[RULE-05] The common control authorizing official MUST authorize controls for inheritance by organizational systems.
[VALIDATION] IF controls_offered_for_inheritance = TRUE AND inheritance_authorization = FALSE THEN violation

[RULE-06] System authorizations MUST be updated at least every 3 years or when significant changes occur.
[VALIDATION] IF current_date > (authorization_date + 3_years) AND reauthorization_completed = FALSE THEN violation

[RULE-07] Authorizing officials MUST be federal employees with appropriate seniority and budgetary authority.
[VALIDATION] IF authorizing_official_type != "federal_employee" OR seniority_level < "senior_official" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Authorization Decision Process - Formal process for AO review and decision-making
- [PROC-02] Common Control Inheritance - Process for accepting and documenting inherited controls
- [PROC-03] Continuous Authorization - Ongoing monitoring and authorization maintenance
- [PROC-04] Reauthorization Process - Periodic review and renewal of system authorizations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Significant system changes, security incidents, regulatory changes, AO changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: System Launch Without Authorization]
IF system_status = "production"
AND written_authorization_issued = FALSE
AND operations_commenced = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Expired Authorization]
IF authorization_date < (current_date - 3_years)
AND reauthorization_completed = FALSE
AND continuous_monitoring_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Contractor as Authorizing Official]
IF authorizing_official_employee_type = "contractor"
AND system_type = "federal_information_system"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Inherited Controls Not Accepted]
IF inherited_common_controls > 0
AND common_controls_formally_accepted = FALSE
AND system_authorization_issued = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Continuous Monitoring Reauthorization]
IF authorization_date < (current_date - 3_years)
AND continuous_monitoring_program = "robust"
AND security_posture = "acceptable"
AND ao_review_completed = TRUE
THEN compliance = TRUE
violation_severity = "None"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Senior official assigned as system AO | RULE-01, RULE-07 |
| Senior official assigned as common control AO | RULE-02, RULE-07 |
| AO accepts inherited common controls | RULE-03 |
| AO authorizes system operation | RULE-04 |
| Common control AO authorizes inheritance | RULE-05 |
| Authorizations updated at defined frequency | RULE-06 |
```