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
The organization SHALL implement a comprehensive process to develop, maintain, and report Plans of Action and Milestones (POA&M) for information security, privacy, and supply chain risk management programs. All POA&Ms MUST document remedial actions to address identified risks and be reviewed for consistency with organizational risk management strategy.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All organizational systems |
| Security Programs | YES | Information security, privacy, supply chain |
| Third-party Systems | YES | When organizationally managed |
| Contractor Systems | CONDITIONAL | When processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee POA&M process implementation<br>• Ensure alignment with risk management strategy<br>• Approve organization-wide POA&M priorities |
| System Owners | • Develop and maintain system-level POA&Ms<br>• Implement remediation actions<br>• Report POA&M status updates |
| Risk Management Team | • Review POA&M consistency with strategy<br>• Consolidate reporting requirements<br>• Monitor remediation progress |

## 4. RULES
[RULE-01] POA&Ms MUST be developed for all information security, privacy, and supply chain risk management programs and associated organizational systems.
[VALIDATION] IF risk_assessment_completed = TRUE AND poam_exists = FALSE THEN violation

[RULE-02] POA&Ms SHALL document specific remedial actions with defined milestones, responsible parties, and target completion dates.
[VALIDATION] IF poam_entry EXISTS AND (milestone_date = NULL OR responsible_party = NULL OR remedial_action = NULL) THEN violation

[RULE-03] POA&Ms MUST be maintained and updated based on control assessment findings and continuous monitoring activities at least quarterly.
[VALIDATION] IF last_poam_update > 90_days AND assessment_findings_exist = TRUE THEN violation

[RULE-04] All POA&Ms SHALL be reported in accordance with established organizational and regulatory reporting requirements including OMB FISMA requirements.
[VALIDATION] IF reporting_deadline_passed = TRUE AND poam_submitted = FALSE THEN critical_violation

[RULE-05] POA&Ms MUST be reviewed for consistency with organizational risk management strategy and organization-wide priorities for risk response actions annually.
[VALIDATION] IF last_strategy_review > 365_days THEN violation

[RULE-06] High-risk findings MUST have POA&M entries created within 30 days of identification, medium-risk within 60 days, and low-risk within 90 days.
[VALIDATION] IF risk_level = "HIGH" AND poam_creation_time > 30_days THEN critical_violation
[VALIDATION] IF risk_level = "MEDIUM" AND poam_creation_time > 60_days THEN violation
[VALIDATION] IF risk_level = "LOW" AND poam_creation_time > 90_days THEN minor_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] POA&M Development - Standardized process for creating POA&M entries from assessment findings
- [PROC-02] POA&M Maintenance - Regular update and status tracking procedures
- [PROC-03] POA&M Reporting - Automated reporting to internal stakeholders and external agencies
- [PROC-04] Risk Prioritization - Process for aligning POA&Ms with organizational risk tolerance
- [PROC-05] POA&M Closure - Validation and approval process for completed remediation actions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, regulatory changes, organizational restructuring, failed compliance audits

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing POA&M Entry]
IF control_assessment_finding = "FAILED"
AND risk_rating >= "MEDIUM"
AND poam_entry_exists = FALSE
AND finding_age > 30_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Overdue Remediation]
IF poam_milestone_date < current_date
AND remediation_status != "COMPLETED"
AND extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incomplete POA&M Documentation]
IF poam_entry_exists = TRUE
AND (responsible_party = NULL OR target_date = NULL OR resources_identified = FALSE)
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Missing Regulatory Reporting]
IF reporting_period = "QUARTERLY"
AND poam_report_submitted = FALSE
AND days_past_deadline > 5
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Strategy Alignment Review]
IF last_strategy_alignment_review > 365_days
AND organizational_risk_strategy_updated = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| POA&M development for security programs | [RULE-01] |
| POA&M development for privacy programs | [RULE-01] |
| POA&M development for supply chain programs | [RULE-01] |
| POA&M maintenance processes | [RULE-03] |
| Remedial action documentation | [RULE-02] |
| Reporting requirement compliance | [RULE-04] |
| Strategy consistency review | [RULE-05] |
| Timely POA&M creation | [RULE-06] |