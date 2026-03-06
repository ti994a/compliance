# POLICY: PM-28: Risk Framing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-28 |
| NIST Control | PM-28: Risk Framing |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | risk framing, risk tolerance, assumptions, constraints, priorities, trade-offs, risk assessment |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain a comprehensive risk framing process that identifies assumptions, constraints, priorities, trade-offs, and risk tolerance affecting all risk management activities. Risk framing results MUST be documented, distributed to appropriate stakeholders, and regularly reviewed to ensure organizational risk management alignment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including cloud, hybrid, and on-premises |
| Third-party services | YES | Where organization has risk management responsibility |
| Business processes | YES | All mission-critical and supporting processes |
| Contractor operations | CONDITIONAL | When handling organizational data or systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee risk framing process<br>• Approve organizational risk tolerance<br>• Ensure stakeholder engagement |
| Risk Management Team | • Document assumptions and constraints<br>• Facilitate risk framing workshops<br>• Maintain risk framing documentation |
| Business/Mission Owners | • Provide business context and priorities<br>• Review risk tolerance alignment<br>• Validate trade-off decisions |
| CISO/Privacy Officer | • Ensure security/privacy considerations<br>• Review technical constraints<br>• Validate control implementations |

## 4. RULES
[RULE-01] Risk assessments, risk responses, and risk monitoring assumptions MUST be identified and documented in the organizational risk register.
[VALIDATION] IF risk_activity_exists = TRUE AND documented_assumptions = FALSE THEN violation

[RULE-02] Constraints affecting risk assessments, risk responses, and risk monitoring MUST be identified and documented with impact analysis.
[VALIDATION] IF risk_management_activity = TRUE AND documented_constraints = FALSE THEN violation

[RULE-03] Organizational priorities and trade-offs for managing risk MUST be documented and approved by senior leadership.
[VALIDATION] IF risk_decisions_made = TRUE AND (documented_priorities = FALSE OR senior_approval = FALSE) THEN violation

[RULE-04] Organizational risk tolerance MUST be defined with quantitative and qualitative thresholds and approved by the Board or equivalent authority.
[VALIDATION] IF risk_tolerance_defined = FALSE OR board_approval = FALSE THEN critical_violation

[RULE-05] Risk framing results MUST be distributed to all identified stakeholders within 30 days of completion or update.
[VALIDATION] IF risk_framing_completed = TRUE AND distribution_days > 30 THEN violation

[RULE-06] Risk framing considerations MUST be reviewed and updated at least annually or when significant organizational changes occur.
[VALIDATION] IF last_review_date > 365_days OR (significant_change = TRUE AND updated = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Risk Framing Workshop Process - Structured approach for engaging stakeholders in risk framing activities
- [PROC-02] Assumption and Constraint Documentation - Standardized format for capturing and maintaining risk framing elements
- [PROC-03] Risk Tolerance Setting Methodology - Process for establishing and approving organizational risk thresholds
- [PROC-04] Stakeholder Distribution Process - Procedures for identifying recipients and distributing risk framing results

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Significant organizational changes, major incidents, regulatory changes, leadership changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Risk Assessment]
IF new_system_deployment = TRUE
AND risk_assessment_initiated = TRUE
AND documented_assumptions = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Outdated Risk Tolerance]
IF risk_tolerance_last_updated > 365_days
AND board_approval_current = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Undocumented Trade-offs]
IF risk_response_selected = TRUE
AND alternative_options_existed = TRUE
AND trade_off_rationale_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Stakeholder Distribution]
IF risk_framing_updated = TRUE
AND stakeholder_notification_sent = FALSE
AND days_since_update > 30
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Constraint Impact Not Assessed]
IF regulatory_constraint_identified = TRUE
AND impact_on_risk_activities_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Assumptions affecting risk assessments identified and documented | RULE-01 |
| Assumptions affecting risk responses identified and documented | RULE-01 |
| Assumptions affecting risk monitoring identified and documented | RULE-01 |
| Constraints affecting risk assessments identified and documented | RULE-02 |
| Constraints affecting risk responses identified and documented | RULE-02 |
| Constraints affecting risk monitoring identified and documented | RULE-02 |
| Priorities considered for managing risk identified and documented | RULE-03 |
| Trade-offs considered for managing risk identified and documented | RULE-03 |
| Organizational risk tolerance identified and documented | RULE-04 |
| Risk framing results distributed to appropriate personnel | RULE-05 |
| Risk framing considerations reviewed and updated per defined frequency | RULE-06 |