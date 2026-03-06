# POLICY: IR-3: Incident Response Testing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IR-3 |
| NIST Control | IR-3: Incident Response Testing |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | incident response, testing, tabletop exercises, simulations, effectiveness, capability assessment |

## 1. POLICY STATEMENT
The organization MUST test the effectiveness of incident response capabilities at defined frequencies using approved testing methods. Testing SHALL identify weaknesses, validate procedures, and measure organizational readiness to respond to cybersecurity incidents.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and hybrid environments |
| Incident response teams | YES | All designated IR personnel |
| Business continuity teams | YES | Supporting IR operations |
| Third-party service providers | CONDITIONAL | When providing IR services |
| Development/test systems | CONDITIONAL | If containing production data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve IR testing strategy and frequency<br>• Review test results and remediation plans<br>• Ensure adequate resources for testing |
| IR Team Lead | • Develop and execute IR testing plans<br>• Coordinate testing activities across teams<br>• Document findings and track remediation |
| System Owners | • Participate in IR testing for their systems<br>• Implement remediation actions<br>• Provide system-specific expertise |

## 4. RULES
[RULE-01] Incident response testing MUST be conducted at least annually for all in-scope systems, with high-impact systems tested semi-annually.
[VALIDATION] IF system_impact_level = "high" AND last_test_date > 6_months THEN violation
[VALIDATION] IF system_impact_level IN ["moderate", "low"] AND last_test_date > 12_months THEN violation

[RULE-02] IR testing SHALL include at minimum one tabletop exercise and one technical simulation per testing cycle.
[VALIDATION] IF testing_cycle_complete = TRUE AND (tabletop_conducted = FALSE OR simulation_conducted = FALSE) THEN violation

[RULE-03] All IR team members MUST participate in at least 75% of scheduled IR tests within a 12-month period.
[VALIDATION] IF ir_member_participation_rate < 0.75 AND review_period = 12_months THEN violation

[RULE-04] IR test results MUST be documented within 5 business days of test completion and include identified gaps and remediation timelines.
[VALIDATION] IF test_completion_date + 5_business_days < current_date AND documentation_complete = FALSE THEN violation

[RULE-05] Critical findings from IR testing MUST be remediated within 30 days, and moderate findings within 90 days.
[VALIDATION] IF finding_severity = "critical" AND days_since_finding > 30 AND status != "remediated" THEN critical_violation
[VALIDATION] IF finding_severity = "moderate" AND days_since_finding > 90 AND status != "remediated" THEN violation

[RULE-06] IR testing scenarios MUST be updated annually to reflect current threat landscape and organizational changes.
[VALIDATION] IF scenario_last_updated > 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] IR Testing Planning - Define test objectives, scenarios, and success criteria
- [PROC-02] Tabletop Exercise Execution - Conduct discussion-based IR scenario walkthroughs
- [PROC-03] Technical Simulation Testing - Execute hands-on IR capability validation
- [PROC-04] Test Results Analysis - Document findings, gaps, and improvement recommendations
- [PROC-05] Remediation Tracking - Monitor and verify correction of identified deficiencies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after major incidents
- Triggering events: Major security incidents, organizational restructuring, significant technology changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Overdue High-Impact System Testing]
IF system_impact_level = "high"
AND last_ir_test_date > 6_months_ago
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Testing Methods]
IF annual_testing_cycle = "complete"
AND tabletop_exercise_conducted = TRUE
AND technical_simulation_conducted = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Critical Remediation]
IF ir_test_finding_severity = "critical"
AND finding_age_days = 45
AND remediation_status = "in_progress"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Low Team Participation]
IF ir_team_member_participation = 60%
AND evaluation_period = "12_months"
AND valid_exemptions = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Outdated Test Scenarios]
IF ir_test_scenarios_last_updated = "18_months_ago"
AND threat_landscape_changes = "significant"
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Test IR effectiveness at defined frequency | [RULE-01] |
| Use appropriate testing methods | [RULE-02] |
| Ensure adequate team participation | [RULE-03] |
| Document test results timely | [RULE-04] |
| Remediate identified gaps | [RULE-05] |
| Maintain current test scenarios | [RULE-06] |