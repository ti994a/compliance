# POLICY: SI-2.3: Time to Remediate Flaws and Benchmarks for Corrective Actions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-2.3 |
| NIST Control | SI-2.3: Time to Remediate Flaws and Benchmarks for Corrective Actions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | flaw remediation, vulnerability management, benchmarks, corrective actions, time measurement |

## 1. POLICY STATEMENT
The organization SHALL measure the time between flaw identification and remediation for all systems and establish benchmarks for taking corrective actions based on flaw severity and type. All remediation activities MUST be tracked with timestamps to enable measurement against established benchmarks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | Systems containing production-like data |
| Test Systems | CONDITIONAL | Only if containing sensitive data |
| Third-party Systems | YES | Where organization controls remediation |
| End-user Devices | YES | Managed corporate devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Vulnerability Management Team | • Track flaw identification timestamps<br>• Measure remediation timeframes<br>• Report benchmark compliance |
| System Administrators | • Execute remediation within benchmarks<br>• Document remediation completion<br>• Escalate benchmark violations |
| Security Operations Center | • Monitor benchmark adherence<br>• Alert on approaching deadlines<br>• Coordinate emergency patches |

## 4. RULES
[RULE-01] All identified flaws MUST have timestamps recorded for both identification and remediation completion dates.
[VALIDATION] IF flaw_identified = TRUE AND (identification_timestamp = NULL OR remediation_timestamp = NULL) THEN violation

[RULE-02] Critical severity flaws MUST be remediated within 72 hours of identification.
[VALIDATION] IF flaw_severity = "critical" AND remediation_time > 72_hours THEN critical_violation

[RULE-03] High severity flaws MUST be remediated within 7 days of identification.
[VALIDATION] IF flaw_severity = "high" AND remediation_time > 7_days THEN major_violation

[RULE-04] Medium severity flaws MUST be remediated within 30 days of identification.
[VALIDATION] IF flaw_severity = "medium" AND remediation_time > 30_days THEN moderate_violation

[RULE-05] Low severity flaws MUST be remediated within 90 days of identification.
[VALIDATION] IF flaw_severity = "low" AND remediation_time > 90_days THEN minor_violation

[RULE-06] Benchmark performance metrics MUST be calculated and reported monthly.
[VALIDATION] IF current_date - last_metrics_report > 30_days THEN violation

[RULE-07] Benchmark exceptions MUST be documented with risk acceptance and compensating controls.
[VALIDATION] IF remediation_time > benchmark AND exception_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Flaw Identification Logging - Automated timestamp capture upon vulnerability discovery
- [PROC-02] Remediation Tracking - Process for recording patch deployment and verification
- [PROC-03] Benchmark Reporting - Monthly measurement and analysis of remediation performance
- [PROC-04] Exception Management - Approval workflow for benchmark deviations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, benchmark performance degradation, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Vulnerability Exceeded]
IF flaw_severity = "critical"
AND remediation_time > 72_hours
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Acceptable Medium Severity Remediation]
IF flaw_severity = "medium"
AND remediation_time = 25_days
AND remediation_verified = TRUE
THEN compliance = TRUE

[SCENARIO-03: Missing Timestamp Documentation]
IF flaw_identified = TRUE
AND identification_timestamp = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Approved Exception with Compensating Controls]
IF flaw_severity = "high"
AND remediation_time > 7_days
AND exception_documented = TRUE
AND compensating_controls = TRUE
THEN compliance = TRUE

[SCENARIO-05: Late Benchmark Reporting]
IF current_date - last_metrics_report > 35_days
AND reporting_extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Minor"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Time between flaw identification and remediation is measured | RULE-01, RULE-06 |
| Benchmarks for corrective actions are defined | RULE-02, RULE-03, RULE-04, RULE-05 |
| Benchmarks for corrective actions have been established | RULE-02, RULE-03, RULE-04, RULE-05, RULE-07 |