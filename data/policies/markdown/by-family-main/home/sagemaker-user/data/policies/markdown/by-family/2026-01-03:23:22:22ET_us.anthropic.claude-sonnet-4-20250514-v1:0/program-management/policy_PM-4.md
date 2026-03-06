# POLICY: PM-4: Plan of Action and Milestones Process

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-4 |
| NIST Control | PM-4: Plan of Action and Milestones Process |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | POA&M, remediation, risk management, reporting, milestones |

## 1. POLICY STATEMENT
The organization SHALL implement a comprehensive process to develop, maintain, and report Plans of Action and Milestones (POA&M) for information security, privacy, and supply chain risk management programs. All POA&Ms MUST document remedial actions to address identified risks and be reviewed for consistency with organizational risk management strategy and priorities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud and hybrid infrastructure |
| Security Programs | YES | Information security, privacy, supply chain |
| Business Processes | YES | Mission-critical and supporting processes |
| Third-party Services | YES | When under organizational control |
| Contractors | CONDITIONAL | When managing organizational systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee organization-wide POA&M process<br>• Ensure consistency with risk management strategy<br>• Approve POA&M reporting procedures |
| System Owners | • Develop and maintain system-level POA&Ms<br>• Coordinate remediation activities<br>• Report POA&M status according to schedule |
| Security Team | • Provide technical guidance for remediation<br>• Validate POA&M entries and milestones<br>• Monitor continuous assessment findings |

## 4. RULES
[RULE-01] Organizations MUST develop and maintain POA&Ms for information security, privacy, and supply chain risk management programs at system, process, and organizational levels.
[VALIDATION] IF program_type IN ["security", "privacy", "supply_chain"] AND poam_exists = FALSE THEN violation

[RULE-02] POA&Ms MUST document remedial actions that adequately respond to risks to organizational operations, assets, individuals, other organizations, and the Nation.
[VALIDATION] IF risk_identified = TRUE AND remedial_action_documented = FALSE THEN violation

[RULE-03] POA&Ms SHALL be reported according to established organizational and regulatory reporting requirements, including OMB FISMA requirements where applicable.
[VALIDATION] IF reporting_due_date < current_date AND poam_submitted = FALSE THEN violation

[RULE-04] POA&Ms MUST be reviewed for consistency with organizational risk management strategy and organization-wide priorities for risk response actions.
[VALIDATION] IF poam_review_date + 90_days < current_date THEN violation

[RULE-05] POA&M updates MUST be based on findings from control assessments and continuous monitoring activities.
[VALIDATION] IF assessment_finding_date > poam_update_date + 30_days THEN violation

[RULE-06] Each POA&M entry MUST include specific milestones, responsible parties, target completion dates, and resource requirements.
[VALIDATION] IF poam_entry_complete = FALSE AND required_fields_missing > 0 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] POA&M Development Process - Standardized methodology for creating POA&M entries
- [PROC-02] POA&M Maintenance and Updates - Regular review and update procedures
- [PROC-03] Risk Prioritization Matrix - Framework for prioritizing remediation activities
- [PROC-04] POA&M Reporting Process - Internal and external reporting procedures
- [PROC-05] Consistency Review Process - Alignment with risk management strategy

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system changes, significant security incidents, regulatory updates, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing POA&M for New Vulnerability]
IF vulnerability_severity = "HIGH"
AND discovery_date + 30_days < current_date
AND poam_entry_exists = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Overdue POA&M Reporting]
IF reporting_requirement = "FISMA"
AND quarterly_report_due = TRUE
AND submission_date > due_date
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Inconsistent Risk Prioritization]
IF poam_priority = "LOW"
AND organizational_risk_rating = "HIGH"
AND justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Outdated POA&M Entry]
IF poam_last_updated + 90_days < current_date
AND remediation_status = "IN_PROGRESS"
AND milestone_passed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Complete POA&M Process]
IF poam_developed = TRUE
AND remediation_documented = TRUE
AND consistency_reviewed = TRUE
AND reporting_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| POA&M development for security programs | RULE-01 |
| POA&M development for privacy programs | RULE-01 |
| POA&M development for supply chain programs | RULE-01 |
| POA&M maintenance processes | RULE-05, RULE-06 |
| Remedial action documentation | RULE-02 |
| Reporting requirements compliance | RULE-03 |
| Consistency with risk management strategy | RULE-04 |
| Organization-wide priority alignment | RULE-04 |