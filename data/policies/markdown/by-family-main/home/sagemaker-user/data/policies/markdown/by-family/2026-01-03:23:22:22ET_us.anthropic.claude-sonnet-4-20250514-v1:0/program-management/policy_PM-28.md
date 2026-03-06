# POLICY: PM-28: Risk Framing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-28 |
| NIST Control | PM-28: Risk Framing |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | risk framing, risk assessment, risk tolerance, assumptions, constraints, priorities, trade-offs |

## 1. POLICY STATEMENT
The organization must establish and maintain a comprehensive risk framing process that identifies and documents assumptions, constraints, priorities, trade-offs, and risk tolerance affecting risk management activities. Risk framing results must be distributed to relevant stakeholders and regularly reviewed to ensure alignment with organizational objectives.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including cloud, hybrid, and on-premises |
| Third-party systems | YES | When processing organizational data |
| Risk management activities | YES | Assessment, response, monitoring |
| All organizational personnel | YES | Distribution requirements vary by role |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee risk framing process<br>• Approve risk tolerance statements<br>• Ensure stakeholder consultation |
| Risk Management Team | • Document assumptions and constraints<br>• Facilitate risk framing reviews<br>• Distribute results to stakeholders |
| System Owners | • Provide system-specific risk context<br>• Review applicable risk framing results<br>• Implement risk framing guidance |

## 4. RULES
[RULE-01] Risk framing activities MUST identify and document assumptions affecting risk assessments, risk responses, and risk monitoring.
[VALIDATION] IF risk_framing_document EXISTS AND assumptions_documented = FALSE THEN violation

[RULE-02] Risk framing activities MUST identify and document constraints affecting risk assessments, risk responses, and risk monitoring.
[VALIDATION] IF risk_framing_document EXISTS AND constraints_documented = FALSE THEN violation

[RULE-03] Organizational priorities and trade-offs for managing risk MUST be identified and documented.
[VALIDATION] IF risk_management_strategy EXISTS AND (priorities_documented = FALSE OR tradeoffs_documented = FALSE) THEN violation

[RULE-04] Organizational risk tolerance MUST be clearly defined and documented with measurable criteria.
[VALIDATION] IF risk_tolerance_statement EXISTS AND measurable_criteria = FALSE THEN violation

[RULE-05] Risk framing results MUST be distributed to designated personnel within 30 days of completion or update.
[VALIDATION] IF risk_framing_completed = TRUE AND distribution_date > (completion_date + 30_days) THEN violation

[RULE-06] Risk framing considerations MUST be reviewed and updated at least annually or when significant organizational changes occur.
[VALIDATION] IF last_review_date > (current_date - 365_days) AND no_triggering_events = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Risk Framing Documentation - Systematic process for identifying and documenting risk framing elements
- [PROC-02] Stakeholder Consultation - Process for engaging organizational stakeholders in risk framing activities
- [PROC-03] Risk Framing Distribution - Procedure for distributing results to appropriate personnel
- [PROC-04] Risk Framing Review - Process for periodic review and update of risk framing considerations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major organizational changes, regulatory changes, significant security incidents, merger/acquisition activities

## 7. SCENARIO PATTERNS
[SCENARIO-01: Complete Risk Framing Documentation]
IF assumptions_documented = TRUE
AND constraints_documented = TRUE
AND priorities_documented = TRUE
AND risk_tolerance_defined = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Risk Tolerance Definition]
IF risk_framing_document EXISTS
AND risk_tolerance_defined = FALSE
AND measurable_criteria = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Distribution]
IF risk_framing_completed = TRUE
AND distribution_date > (completion_date + 30_days)
AND stakeholders_notified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Outdated Risk Framing]
IF last_review_date > (current_date - 365_days)
AND organizational_changes = TRUE
AND risk_framing_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Incomplete Stakeholder Engagement]
IF risk_framing_process = "active"
AND system_owners_consulted = FALSE
AND mission_owners_consulted = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Assumptions affecting risk assessments identified | RULE-01 |
| Assumptions affecting risk responses identified | RULE-01 |
| Assumptions affecting risk monitoring identified | RULE-01 |
| Constraints affecting risk assessments identified | RULE-02 |
| Constraints affecting risk responses identified | RULE-02 |
| Constraints affecting risk monitoring identified | RULE-02 |
| Priorities for managing risk identified | RULE-03 |
| Trade-offs for managing risk identified | RULE-03 |
| Organizational risk tolerance identified | RULE-04 |
| Risk framing results distributed to personnel | RULE-05 |
| Risk framing considerations reviewed and updated | RULE-06 |