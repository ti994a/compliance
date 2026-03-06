# POLICY: CA-7.4: Risk Monitoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CA-7.4 |
| NIST Control | CA-7.4: Risk Monitoring |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | risk monitoring, continuous monitoring, effectiveness monitoring, compliance monitoring, change monitoring |

## 1. POLICY STATEMENT
Risk monitoring must be an integral component of the organization's continuous monitoring strategy. The risk monitoring program shall include effectiveness monitoring, compliance monitoring, and change monitoring to ensure ongoing security and privacy risk management aligned with organizational risk tolerance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| Third-party Services | YES | Where organization maintains risk responsibility |
| Development Environments | YES | Must align with production risk monitoring |
| Legacy Systems | YES | May require compensating controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Establish organizational risk tolerance<br>• Oversee risk monitoring strategy<br>• Review risk monitoring effectiveness |
| Security Operations Center | • Execute continuous monitoring activities<br>• Generate risk monitoring reports<br>• Escalate risk threshold breaches |
| System Owners | • Implement system-level risk monitoring<br>• Report changes affecting risk posture<br>• Maintain risk monitoring documentation |

## 4. RULES
[RULE-01] Risk monitoring MUST be documented as an integral part of the continuous monitoring strategy for all information systems.
[VALIDATION] IF system_has_continuous_monitoring_strategy = TRUE AND risk_monitoring_documented = FALSE THEN violation

[RULE-02] Effectiveness monitoring MUST be implemented to determine ongoing effectiveness of risk response measures at least monthly.
[VALIDATION] IF effectiveness_monitoring_frequency > 30_days THEN violation

[RULE-03] Compliance monitoring MUST verify implementation of required risk response measures and satisfaction of security/privacy requirements quarterly.
[VALIDATION] IF compliance_monitoring_frequency > 90_days THEN violation

[RULE-04] Change monitoring MUST identify and assess changes to systems and environments that may affect security and privacy risk within 72 hours of change implementation.
[VALIDATION] IF change_detected = TRUE AND risk_assessment_time > 72_hours THEN violation

[RULE-05] Risk monitoring activities MUST be aligned with established organizational risk tolerance thresholds.
[VALIDATION] IF risk_tolerance_defined = FALSE OR risk_monitoring_alignment_documented = FALSE THEN violation

[RULE-06] Risk monitoring results MUST be documented and reported to appropriate stakeholders according to the continuous monitoring strategy.
[VALIDATION] IF monitoring_results_documented = FALSE OR reporting_schedule_missed = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Risk Monitoring Strategy Development - Establish comprehensive approach integrating all monitoring types
- [PROC-02] Effectiveness Assessment - Evaluate ongoing effectiveness of risk response measures
- [PROC-03] Compliance Verification - Verify implementation and effectiveness of required controls
- [PROC-04] Change Impact Analysis - Assess security and privacy risk impact of system changes
- [PROC-05] Risk Reporting and Escalation - Document and communicate risk monitoring findings

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system changes, risk tolerance updates, regulatory changes, significant security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Risk Monitoring Integration]
IF continuous_monitoring_strategy_exists = TRUE
AND risk_monitoring_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delayed Change Risk Assessment]
IF system_change_implemented = TRUE
AND change_risk_assessment_completed = FALSE
AND hours_since_change > 72
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Ineffective Monitoring Frequency]
IF effectiveness_monitoring_required = TRUE
AND last_effectiveness_review > 30_days
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Compliance Monitoring Gap]
IF required_controls_implemented = TRUE
AND compliance_verification_overdue = TRUE
AND days_overdue > 90
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Risk Tolerance Misalignment]
IF risk_monitoring_active = TRUE
AND organizational_risk_tolerance_defined = TRUE
AND monitoring_alignment_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Risk monitoring integral to continuous monitoring strategy | RULE-01 |
| Effectiveness monitoring included in risk monitoring | RULE-02 |
| Compliance monitoring included in risk monitoring | RULE-03 |
| Change monitoring included in risk monitoring | RULE-04 |