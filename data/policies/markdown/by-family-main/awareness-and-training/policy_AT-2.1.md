# POLICY: AT-2.1: Practical Exercises

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-2.1 |
| NIST Control | AT-2.1: Practical Exercises |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | practical exercises, literacy training, simulation, social engineering, phishing, incident simulation |

## 1. POLICY STATEMENT
The organization SHALL conduct practical exercises as part of security awareness and literacy training programs that simulate real-world cybersecurity events and incidents. These exercises MUST include simulated social engineering attacks, phishing campaigns, and other threat scenarios to test and improve employee security awareness and response capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Including full-time, part-time, and contractors |
| Third-party users | YES | When accessing company systems |
| Executive leadership | YES | Subject to tailored exercises |
| Temporary workers | YES | Based on system access level |
| Vendors with system access | YES | Per contractual requirements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve practical exercise program<br>• Define exercise scope and frequency<br>• Review exercise results and metrics |
| Security Awareness Team | • Design and execute practical exercises<br>• Develop simulation scenarios<br>• Track participation and results<br>• Provide remedial training |
| IT Security Operations | • Support technical implementation of exercises<br>• Monitor exercise execution<br>• Coordinate with SOC during exercises |
| Human Resources | • Facilitate employee participation<br>• Support disciplinary actions for repeated failures<br>• Coordinate new hire exercise requirements |

## 4. RULES
[RULE-01] The organization MUST conduct practical exercises simulating cybersecurity events and incidents at least quarterly for all personnel with system access.
[VALIDATION] IF last_exercise_date > 90_days AND user_has_system_access = TRUE THEN violation

[RULE-02] Practical exercises MUST include simulated social engineering attempts designed to collect information or gain unauthorized access.
[VALIDATION] IF exercise_type NOT IN ["social_engineering", "phishing", "pretexting"] THEN violation

[RULE-03] No-notice phishing simulation exercises MUST be conducted monthly with randomized targeting of at least 20% of the user population.
[VALIDATION] IF phishing_simulation_frequency > 30_days OR target_percentage < 20% THEN violation

[RULE-04] Personnel who fail practical exercises MUST complete remedial training within 5 business days of notification.
[VALIDATION] IF exercise_result = "failed" AND remedial_training_completion > 5_business_days THEN violation

[RULE-05] Exercise scenarios MUST simulate current threat intelligence and attack vectors relevant to the organization's threat landscape.
[VALIDATION] IF scenario_age > 6_months AND threat_intelligence_updated = FALSE THEN violation

[RULE-06] All practical exercise results MUST be documented and reported to management within 30 days of exercise completion.
[VALIDATION] IF exercise_completion_date + 30_days < current_date AND report_submitted = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Practical Exercise Planning - Define scenarios, targets, and success criteria
- [PROC-02] Phishing Simulation Execution - Deploy and monitor simulated phishing campaigns
- [PROC-03] Social Engineering Testing - Conduct phone and physical social engineering tests
- [PROC-04] Exercise Result Analysis - Evaluate performance and identify training gaps
- [PROC-05] Remedial Training Delivery - Provide additional training for exercise failures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, significant organizational changes, new threat intelligence, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Quarterly Exercise]
IF current_date - last_exercise_date > 90_days
AND user_system_access = TRUE
AND approved_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Failed Phishing Test Without Remediation]
IF phishing_test_result = "clicked_link"
AND remedial_training_completed = FALSE
AND notification_date + 5_business_days < current_date
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Exercise Scenarios]
IF exercise_scenarios_last_updated > 6_months
AND threat_landscape_assessment = "not_current"
AND exercise_conducted = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete Exercise Documentation]
IF exercise_completed = TRUE
AND exercise_completion_date + 30_days < current_date
AND management_report_submitted = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Adequate Exercise Program]
IF quarterly_exercises_conducted = TRUE
AND phishing_simulations_monthly = TRUE
AND remedial_training_timely = TRUE
AND current_threat_scenarios = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Practical exercises in literacy training provided | [RULE-01], [RULE-02] |
| Exercises simulate events and incidents | [RULE-02], [RULE-05] |
| Social engineering simulations included | [RULE-02], [RULE-03] |
| Regular exercise execution | [RULE-01], [RULE-03] |
| Performance tracking and remediation | [RULE-04], [RULE-06] |