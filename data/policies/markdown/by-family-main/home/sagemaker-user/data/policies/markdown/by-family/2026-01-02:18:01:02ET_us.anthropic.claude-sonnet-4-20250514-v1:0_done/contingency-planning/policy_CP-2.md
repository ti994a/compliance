# POLICY: CP-2: Contingency Plan

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-2 |
| NIST Control | CP-2: Contingency Plan |
| Version | 1.0 |
| Owner | Chief Information Officer |
| Keywords | contingency planning, business continuity, disaster recovery, system restoration, incident response |

## 1. POLICY STATEMENT
All information systems must have comprehensive contingency plans that ensure continuity of essential mission and business functions during system disruptions, compromises, or failures. These plans must be regularly reviewed, updated, and coordinated with incident response activities to maintain organizational operations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| Mission-Critical Applications | YES | Require enhanced recovery objectives |
| Development/Test Systems | CONDITIONAL | Based on business impact assessment |
| Third-Party Systems | YES | When supporting essential functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Develop and maintain system contingency plans<br>• Define recovery objectives and priorities<br>• Approve plan updates and changes |
| IT Operations | • Implement contingency procedures<br>• Maintain backup and recovery capabilities<br>• Execute system restoration activities |
| Business Continuity Manager | • Coordinate contingency planning activities<br>• Review plans for completeness<br>• Facilitate testing and training |
| Information Security Officer | • Ensure plan protection from unauthorized access<br>• Validate security control restoration<br>• Coordinate with incident response team |

## 4. RULES

[RULE-01] Each information system MUST have a documented contingency plan that identifies essential mission and business functions with associated recovery requirements.
[VALIDATION] IF system_in_production = TRUE AND contingency_plan_exists = FALSE THEN critical_violation

[RULE-02] Contingency plans MUST define specific recovery time objectives (RTO) not exceeding 72 hours for critical systems and 168 hours for non-critical systems.
[VALIDATION] IF system_criticality = "critical" AND RTO > 72_hours THEN violation
[VALIDATION] IF system_criticality = "non-critical" AND RTO > 168_hours THEN violation

[RULE-03] Contingency plans MUST include assigned roles, responsibilities, and current contact information for all key personnel.
[VALIDATION] IF contingency_plan_contact_info_age > 90_days THEN violation

[RULE-04] Contingency plans MUST be reviewed and approved by designated organizational personnel at least annually or when significant changes occur.
[VALIDATION] IF days_since_last_review > 365 THEN violation
[VALIDATION] IF significant_system_change = TRUE AND plan_updated = FALSE THEN violation

[RULE-05] Copies of contingency plans MUST be distributed to all key contingency personnel and stored in secure, accessible locations.
[VALIDATION] IF key_personnel_has_current_plan = FALSE THEN violation

[RULE-06] Contingency planning activities MUST be coordinated with incident handling procedures and personnel.
[VALIDATION] IF contingency_incident_coordination_documented = FALSE THEN violation

[RULE-07] Contingency plans MUST address full system restoration without deterioration of originally implemented security controls.
[VALIDATION] IF restoration_security_validation_process = FALSE THEN violation

[RULE-08] Contingency plans MUST be protected from unauthorized disclosure and modification through appropriate access controls.
[VALIDATION] IF contingency_plan_access_controls = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Contingency Plan Development - Systematic approach for creating comprehensive contingency plans
- [PROC-02] Business Impact Assessment - Process for identifying essential functions and recovery requirements
- [PROC-03] Plan Review and Update - Regular review cycle and change management process
- [PROC-04] Personnel Notification - Procedures for communicating plan changes to key personnel
- [PROC-05] Plan Testing and Training - Regular validation of contingency procedures and personnel readiness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after significant organizational changes
- Triggering events: System modifications, organizational restructuring, lessons learned from incidents, failed tests

## 7. SCENARIO PATTERNS

[SCENARIO-01: Missing Contingency Plan]
IF system_in_production = TRUE
AND system_age > 30_days
AND contingency_plan_exists = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Outdated Recovery Objectives]
IF system_criticality = "critical"
AND defined_RTO > 72_hours
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Stale Contact Information]
IF contingency_plan_exists = TRUE
AND contact_info_last_verified > 90_days
AND key_personnel_changes = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unprotected Plan Storage]
IF contingency_plan_exists = TRUE
AND plan_access_controls = FALSE
AND plan_contains_sensitive_info = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Uncoordinated Incident Response]
IF contingency_plan_exists = TRUE
AND incident_response_plan_exists = TRUE
AND coordination_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Essential functions identification | [RULE-01] |
| Recovery objectives definition | [RULE-02] |
| Roles and contact information | [RULE-03] |
| Plan review and approval | [RULE-04] |
| Plan distribution | [RULE-05] |
| Incident handling coordination | [RULE-06] |
| Full system restoration | [RULE-07] |
| Plan protection | [RULE-08] |