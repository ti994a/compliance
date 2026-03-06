# POLICY: PM-6: Measures of Performance

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-6 |
| NIST Control | PM-6: Measures of Performance |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | performance metrics, security effectiveness, privacy monitoring, risk tolerance, outcome measurement |

## 1. POLICY STATEMENT
The organization SHALL develop, monitor, and report on outcome-based measures of performance for information security and privacy programs. These measures SHALL align with organizational risk tolerance and demonstrate the effectiveness of security and privacy controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Security Program | YES | All security controls and functions |
| Privacy Program | YES | All privacy controls and functions |
| Third-party Services | YES | When processing organizational data |
| Development/Test Systems | YES | Must contribute to overall metrics |
| Legacy Systems | YES | Performance measured within constraints |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve performance measures framework<br>• Review quarterly performance reports<br>• Ensure alignment with risk tolerance |
| Privacy Officer | • Develop privacy-specific performance measures<br>• Monitor privacy program effectiveness<br>• Report privacy metrics to leadership |
| Security Program Manager | • Implement performance measurement processes<br>• Collect and analyze security metrics<br>• Coordinate with business units for data collection |
| Risk Management Team | • Align measures with risk tolerance<br>• Validate metric effectiveness<br>• Support risk-based performance analysis |

## 4. RULES
[RULE-01] Information security measures of performance MUST be developed and documented within 90 days of program establishment or major changes.
[VALIDATION] IF security_program_established = TRUE AND measures_documented = FALSE AND days_elapsed > 90 THEN violation

[RULE-02] Privacy measures of performance MUST be developed and documented within 90 days of privacy program establishment or major changes.
[VALIDATION] IF privacy_program_established = TRUE AND privacy_measures_documented = FALSE AND days_elapsed > 90 THEN violation

[RULE-03] Performance measures MUST be monitored continuously with formal assessment conducted at least quarterly.
[VALIDATION] IF last_formal_assessment > 90_days THEN violation

[RULE-04] Performance measurement results MUST be reported to executive leadership quarterly and to the board annually.
[VALIDATION] IF executive_report_overdue > 90_days OR board_report_overdue > 365_days THEN violation

[RULE-05] Performance measures MUST align with organizational risk tolerance as defined in the risk management strategy.
[VALIDATION] IF measures_risk_alignment_documented = FALSE OR last_alignment_review > 365_days THEN violation

[RULE-06] Each performance measure MUST include defined baselines, targets, and thresholds for acceptable performance.
[VALIDATION] IF measure_baseline = NULL OR measure_target = NULL OR measure_threshold = NULL THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Performance Measure Development - Establish metrics aligned with program objectives and risk tolerance
- [PROC-02] Data Collection and Analysis - Systematic gathering and evaluation of performance data
- [PROC-03] Performance Reporting - Regular communication of results to stakeholders
- [PROC-04] Measure Effectiveness Review - Annual assessment of metric relevance and accuracy

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, regulatory updates, significant security incidents, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Security Metrics]
IF security_program_active = TRUE
AND security_measures_documented = FALSE
AND program_age > 90_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Performance Reports]
IF last_executive_report_date < (current_date - 95_days)
AND reporting_exemption = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unaligned Risk Metrics]
IF performance_measures_exist = TRUE
AND risk_alignment_documented = FALSE
AND risk_strategy_updated = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Continuous Monitoring Gap]
IF automated_monitoring = FALSE
AND manual_assessment_frequency > 90_days
AND high_risk_environment = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Incomplete Privacy Metrics]
IF privacy_program_active = TRUE
AND privacy_measures_count = 0
AND pii_processing = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information security measures of performance are developed | [RULE-01] |
| Information security measures of performance are monitored | [RULE-03] |
| Results of information security measures are reported | [RULE-04] |
| Privacy measures of performance are developed | [RULE-02] |
| Privacy measures of performance are monitored | [RULE-03] |
| Results of privacy measures are reported | [RULE-04] |