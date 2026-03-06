# POLICY: PM-28: Risk Framing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-28 |
| NIST Control | PM-28: Risk Framing |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | risk framing, risk tolerance, assumptions, constraints, priorities, trade-offs, risk assessment, stakeholders |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain a comprehensive risk framing process that identifies assumptions, constraints, priorities, trade-offs, and risk tolerance to inform all risk management activities. Risk framing results MUST be documented, distributed to appropriate stakeholders, and regularly reviewed to ensure alignment with organizational objectives and changing threat landscapes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including cloud, hybrid, and on-premises |
| Third-party services | YES | Where organization has risk management responsibility |
| Business processes | YES | Mission-critical and support functions |
| All personnel levels | YES | From executives to system operators |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee risk framing process<br>• Approve organizational risk tolerance<br>• Ensure stakeholder engagement |
| Risk Management Team | • Conduct risk framing activities<br>• Document assumptions and constraints<br>• Distribute risk framing results |
| System Owners | • Provide system-specific risk context<br>• Implement risk framing guidance<br>• Report constraint changes |
| Senior Leadership | • Define organizational priorities<br>• Approve trade-off decisions<br>• Set risk tolerance levels |

## 4. RULES

[RULE-01] The organization MUST identify and document assumptions affecting risk assessments, risk responses, and risk monitoring activities.
[VALIDATION] IF risk_framing_document EXISTS AND assumptions_documented = FALSE THEN violation

[RULE-02] The organization MUST identify and document constraints affecting risk assessments, risk responses, and risk monitoring activities.
[VALIDATION] IF risk_activity_conducted = TRUE AND constraints_documented = FALSE THEN violation

[RULE-03] Organizational priorities and trade-offs for managing risk MUST be identified, documented, and approved by senior leadership.
[VALIDATION] IF priorities_documented = FALSE OR senior_leadership_approval = FALSE THEN violation

[RULE-04] Organizational risk tolerance MUST be formally defined, documented, and approved by the Chief Risk Officer or designated authority.
[VALIDATION] IF risk_tolerance_defined = FALSE OR cro_approval = FALSE THEN violation

[RULE-05] Risk framing results MUST be distributed to all personnel identified as recipients within 30 days of completion or update.
[VALIDATION] IF risk_framing_completed = TRUE AND distribution_time > 30_days THEN violation

[RULE-06] Risk framing considerations MUST be reviewed and updated at least annually or when significant organizational changes occur.
[VALIDATION] IF last_review_date > 365_days AND no_triggering_events = TRUE THEN violation

[RULE-07] Risk framing activities MUST involve consultation with stakeholders including mission owners, business owners, system owners, and authorizing officials.
[VALIDATION] IF stakeholder_consultation_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Risk Framing Documentation - Standard templates and processes for documenting assumptions, constraints, priorities, and risk tolerance
- [PROC-02] Stakeholder Engagement - Process for identifying and consulting with relevant organizational stakeholders
- [PROC-03] Risk Framing Distribution - Procedures for distributing risk framing results to appropriate personnel
- [PROC-04] Risk Framing Review - Process for periodic review and update of risk framing considerations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major organizational changes, significant security incidents, regulatory changes, merger/acquisition activities

## 7. SCENARIO PATTERNS

[SCENARIO-01: New System Risk Assessment]
IF new_system_deployment = TRUE
AND risk_assessment_initiated = TRUE
AND current_risk_framing_applied = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Outdated Risk Tolerance]
IF risk_tolerance_last_updated > 365_days
AND no_formal_review_conducted = TRUE
AND organizational_changes_occurred = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Incomplete Stakeholder Consultation]
IF risk_framing_activity = "in_progress"
AND system_owners_consulted = FALSE
AND mission_owners_consulted = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Distribution]
IF risk_framing_updated = TRUE
AND update_date < 45_days_ago
AND stakeholder_notification = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Undocumented Assumptions]
IF risk_assessment_conducted = TRUE
AND assumptions_identified = TRUE
AND assumptions_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Assumptions affecting risk assessments are identified and documented | RULE-01 |
| Assumptions affecting risk responses are identified and documented | RULE-01 |
| Assumptions affecting risk monitoring are identified and documented | RULE-01 |
| Constraints affecting risk assessments are identified and documented | RULE-02 |
| Constraints affecting risk responses are identified and documented | RULE-02 |
| Constraints affecting risk monitoring are identified and documented | RULE-02 |
| Priorities considered for managing risk are identified and documented | RULE-03 |
| Trade-offs considered for managing risk are identified and documented | RULE-03 |
| Organizational risk tolerance is identified and documented | RULE-04 |
| Results of risk framing activities are distributed to appropriate personnel | RULE-05 |
| Risk framing considerations are reviewed and updated per defined frequency | RULE-06 |