# POLICY: PM-10: Authorization Process

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-10 |
| NIST Control | PM-10: Authorization Process |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authorization, risk management, authorizing official, continuous monitoring, security state, privacy state |

## 1. POLICY STATEMENT
The organization SHALL manage the security and privacy state of all organizational systems through formal authorization processes integrated with enterprise risk management. Designated individuals MUST fulfill specific roles within the risk management process to ensure ongoing understanding and acceptance of security and privacy risks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including cloud, on-premises, and hybrid |
| Common control providers | YES | Shared services and infrastructure |
| Third-party hosted systems | YES | Where organization maintains data ownership |
| Development/test environments | CONDITIONAL | If processing production data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Risk Executive | • Oversee organization-wide risk management program<br>• Approve risk tolerance levels<br>• Ensure integration with business processes |
| Authorizing Official (AO) | • Make authorization decisions for assigned systems<br>• Accept residual risks<br>• Monitor ongoing security and privacy posture |
| System Owner | • Implement required controls<br>• Maintain system documentation<br>• Report security/privacy incidents |

## 4. RULES
[RULE-01] Each organizational system MUST have a designated Authorizing Official with documented authority to accept security and privacy risks.
[VALIDATION] IF system_in_production = TRUE AND authorizing_official = NULL THEN critical_violation

[RULE-02] Authorization processes MUST be integrated with the organization-wide risk management program and updated within 30 days of program changes.
[VALIDATION] IF risk_program_updated = TRUE AND authorization_process_update > 30_days THEN violation

[RULE-03] Security and privacy states MUST be continuously monitored with formal assessment at least annually or when significant changes occur.
[VALIDATION] IF last_assessment_date > 365_days AND significant_changes = FALSE THEN violation
[VALIDATION] IF significant_changes = TRUE AND reassessment_initiated = FALSE THEN critical_violation

[RULE-04] All individuals in risk management roles MUST have documented responsibilities and receive role-specific training within 60 days of assignment.
[VALIDATION] IF role_assigned = TRUE AND training_completed = FALSE AND days_since_assignment > 60 THEN violation

[RULE-05] Authorization decisions MUST be documented with explicit risk acceptance statements and approved mitigation timelines for identified deficiencies.
[VALIDATION] IF authorization_granted = TRUE AND risk_acceptance_documented = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Authorization Process - Define steps for initial and reauthorization activities
- [PROC-02] Risk Executive Function - Establish governance structure and decision-making authority  
- [PROC-03] Continuous Monitoring Integration - Link authorization with ongoing risk assessment
- [PROC-04] Role Assignment and Training - Define qualification requirements and training programs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Regulatory changes, significant security incidents, organizational restructuring, new system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Deployment]
IF system_status = "production_ready"
AND authorizing_official_assigned = FALSE
AND deployment_date <= 30_days
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Expired Authorization]
IF authorization_date < current_date - 3_years
AND reauthorization_initiated = FALSE
AND system_status = "operational"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Significant Change Without Reassessment]
IF system_changes = "major_architectural_modification"
AND change_date < current_date - 90_days
AND impact_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Unqualified Authorizing Official]
IF authorizing_official_training = "incomplete"
AND authorization_decision_made = TRUE
AND days_in_role > 60
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Missing Risk Integration]
IF organization_risk_program_updated = TRUE
AND authorization_process_aligned = FALSE
AND days_since_update > 30
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Assessment Objective | Rule Reference |
|---------------------|---------------|
| Security state managed through authorization processes | [RULE-01], [RULE-03] |
| Privacy state managed through authorization processes | [RULE-01], [RULE-03] |
| Individuals designated for risk management roles | [RULE-04] |
| Authorization processes integrated with risk management | [RULE-02], [RULE-05] |