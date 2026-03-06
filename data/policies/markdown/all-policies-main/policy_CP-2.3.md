# POLICY: CP-2.3: Resume Mission and Business Functions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-2.3 |
| NIST Control | CP-2.3: Resume Mission and Business Functions |
| Version | 1.0 |
| Owner | Business Continuity Manager |
| Keywords | contingency planning, business continuity, mission functions, recovery time, business impact |

## 1. POLICY STATEMENT
The organization must plan for the resumption of all mission and business functions within defined time periods following contingency plan activation. All critical business operations and mission-essential functions must have documented recovery procedures with specific timeframes based on business impact analysis and organizational priorities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| Mission-Critical Functions | YES | As defined in BIA |
| Business Operations | YES | All revenue-generating activities |
| Support Functions | YES | HR, Finance, IT operations |
| Third-Party Services | YES | Critical vendor dependencies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Business Continuity Manager | • Develop and maintain resumption plans<br>• Define recovery time objectives<br>• Coordinate cross-functional recovery efforts |
| Business Unit Owners | • Identify critical functions and dependencies<br>• Validate recovery procedures<br>• Execute function-specific recovery plans |
| IT Operations Team | • Restore technical infrastructure<br>• Support business function recovery<br>• Monitor system performance during recovery |

## 4. RULES
[RULE-01] All mission and business functions MUST have documented resumption procedures within the contingency plan with specific recovery time objectives (RTOs).
[VALIDATION] IF function_type IN ["mission_critical", "business_essential"] AND resumption_procedure = NULL THEN violation

[RULE-02] Recovery time objectives MUST be defined based on business impact analysis and SHALL NOT exceed maximum tolerable downtime (MTD) for each function.
[VALIDATION] IF RTO > MTD THEN critical_violation

[RULE-03] Resumption procedures MUST prioritize functions based on criticality levels defined in the business impact assessment.
[VALIDATION] IF recovery_priority NOT IN business_impact_assessment.criticality_levels THEN violation

[RULE-04] All resumption plans MUST include dependencies, resource requirements, and success criteria for each business function.
[VALIDATION] IF resumption_plan.dependencies = NULL OR resumption_plan.resources = NULL OR resumption_plan.success_criteria = NULL THEN violation

[RULE-05] Resumption procedures MUST be tested annually and updated within 30 days of any significant business process changes.
[VALIDATION] IF last_test_date > 365_days OR (business_change_date > resumption_plan.last_update + 30_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Business Impact Analysis - Annual assessment of function criticality and recovery requirements
- [PROC-02] Resumption Plan Development - Creation and maintenance of function-specific recovery procedures
- [PROC-03] Recovery Testing - Annual validation of resumption procedures and timeframes
- [PROC-04] Plan Activation - Formal process for initiating business function recovery

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major business changes, failed recovery tests, actual contingency activations, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Function Missing Recovery Plan]
IF function_criticality = "mission_critical"
AND resumption_procedure = NULL
AND contingency_plan_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: RTO Exceeds Business Tolerance]
IF defined_RTO > business_impact_assessment.MTD
AND function_type = "revenue_generating"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Resumption Procedures]
IF business_process_change_date > resumption_plan.last_update
AND days_since_change > 30
AND function_criticality IN ["critical", "high"]
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Untested Recovery Procedures]
IF resumption_plan.last_test_date > 365_days
AND function_type = "mission_essential"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Successful Prioritized Recovery]
IF contingency_activated = TRUE
AND recovery_sequence = business_impact_assessment.priority_order
AND all_critical_functions_recovered_within_RTO = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Resumption of all mission and business functions are planned | [RULE-01] |
| Recovery within defined time periods | [RULE-02] |
| Prioritization based on business impact | [RULE-03] |
| Complete resumption procedures documented | [RULE-04] |
| Regular testing and maintenance | [RULE-05] |