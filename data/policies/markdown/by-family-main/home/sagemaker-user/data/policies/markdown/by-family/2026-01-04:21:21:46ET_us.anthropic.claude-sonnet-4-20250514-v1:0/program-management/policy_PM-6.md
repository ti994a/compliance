# POLICY: PM-6: Measures of Performance

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-6 |
| NIST Control | PM-6: Measures of Performance |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | performance metrics, security effectiveness, privacy metrics, outcome measurement, program assessment, risk tolerance |

## 1. POLICY STATEMENT
The organization SHALL develop, monitor, and report on outcome-based measures of performance for information security and privacy programs to evaluate effectiveness and efficiency. Performance measures MUST align with organizational risk tolerance and support continuous improvement of security and privacy controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Security Program | YES | All security controls and functions |
| Privacy Program | YES | All privacy controls and functions |
| Third-party Services | YES | When processing organizational data |
| Development/Test Systems | YES | Must contribute to overall metrics |
| Legacy Systems | YES | Performance measurement required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve performance measurement framework<br>• Review quarterly performance reports<br>• Ensure alignment with risk tolerance |
| Privacy Officer | • Develop privacy-specific performance measures<br>• Monitor privacy program effectiveness<br>• Report privacy metrics to leadership |
| Security Program Manager | • Implement performance measurement processes<br>• Collect and analyze security metrics<br>• Coordinate cross-functional reporting |
| System Owners | • Provide system-level performance data<br>• Implement measurement tools<br>• Report anomalies and trends |

## 4. RULES
[RULE-01] Information security measures of performance MUST be developed within 90 days of program establishment and reviewed annually.
[VALIDATION] IF security_program_established = TRUE AND measures_developed_days > 90 THEN violation

[RULE-02] Privacy measures of performance MUST be developed within 90 days of privacy program establishment and reviewed annually.
[VALIDATION] IF privacy_program_established = TRUE AND measures_developed_days > 90 THEN violation

[RULE-03] Performance measures MUST be monitored continuously with formal assessment conducted at least quarterly.
[VALIDATION] IF last_formal_assessment_days > 90 THEN violation

[RULE-04] Performance measurement results MUST be reported to executive leadership within 30 days of quarterly assessment completion.
[VALIDATION] IF assessment_complete = TRUE AND report_delivery_days > 30 THEN violation

[RULE-05] Performance measures MUST align with organizational risk tolerance as defined in the risk management strategy.
[VALIDATION] IF measures_risk_aligned = FALSE THEN violation

[RULE-06] Outcome-based metrics MUST comprise at least 70% of all performance measures, with remaining 30% allowed for process metrics.
[VALIDATION] IF outcome_metrics_percentage < 70 THEN violation

[RULE-07] Performance measures MUST include both effectiveness metrics (security/privacy outcomes) and efficiency metrics (resource utilization).
[VALIDATION] IF effectiveness_metrics = FALSE OR efficiency_metrics = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Performance Measure Development - Establish methodology for creating outcome-based metrics
- [PROC-02] Continuous Monitoring Process - Define automated and manual monitoring activities
- [PROC-03] Quarterly Assessment Protocol - Standardize formal performance evaluation process
- [PROC-04] Executive Reporting Framework - Template and process for leadership communication
- [PROC-05] Metrics Validation and Calibration - Ensure accuracy and relevance of measurements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Major security incidents, regulatory changes, risk tolerance updates, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Security Program]
IF security_program_age_days = 120
AND performance_measures_developed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Quarterly Reporting Delay]
IF quarterly_assessment_complete = TRUE
AND report_submitted_days = 45
AND executive_leadership_notified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Process-Heavy Metrics]
IF total_metrics = 20
AND outcome_based_metrics = 12
AND process_metrics = 8
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Risk Misalignment]
IF risk_tolerance = "low"
AND performance_thresholds = "moderate"
AND alignment_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Monitoring Gap]
IF last_continuous_monitoring_days = 180
AND formal_assessment_overdue = TRUE
AND justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information security measures developed | [RULE-01] |
| Information security measures monitored | [RULE-03] |
| Information security results reported | [RULE-04] |
| Privacy measures developed | [RULE-02] |
| Privacy measures monitored | [RULE-03] |
| Privacy results reported | [RULE-04] |
| Risk tolerance alignment | [RULE-05] |
| Outcome-based methodology | [RULE-06] |