```markdown
# POLICY: AT-3.3: Practical Exercises

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-3.3 |
| NIST Control | AT-3.3: Practical Exercises |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | practical exercises, security training, privacy training, simulated attacks, phishing simulation, hands-on learning |

## 1. POLICY STATEMENT
All security and privacy training programs MUST include practical exercises that reinforce training objectives through hands-on activities and simulations. These exercises SHALL provide realistic scenarios that allow personnel to apply knowledge and skills in controlled environments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Mandatory participation in role-appropriate exercises |
| Contractors | YES | Must complete exercises relevant to access level |
| Third-party vendors | CONDITIONAL | Required if accessing company systems/data |
| Software developers | YES | Must include secure coding practical exercises |
| Executives/Leadership | YES | Must include targeted phishing simulations |
| Privacy personnel | YES | Must include PII handling and PIA exercises |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve practical exercise curriculum<br>• Ensure adequate funding and resources<br>• Review exercise effectiveness metrics |
| Training Manager | • Design and implement practical exercises<br>• Track participation and completion rates<br>• Coordinate with subject matter experts |
| Department Managers | • Ensure team participation in exercises<br>• Provide feedback on exercise relevance<br>• Support remedial training for failures |

## 4. RULES
[RULE-01] Security training programs MUST include practical exercises that simulate real-world attack scenarios relevant to each role.
[VALIDATION] IF security_training_program EXISTS AND practical_exercises = FALSE THEN violation

[RULE-02] Privacy training programs MUST include hands-on exercises for identifying, processing, and protecting personally identifiable information.
[VALIDATION] IF privacy_training_program EXISTS AND practical_exercises = FALSE THEN violation

[RULE-03] Software developers MUST complete practical exercises addressing common vulnerability exploitation and secure coding practices at least annually.
[VALIDATION] IF role = "developer" AND secure_coding_exercises_completion < 365_days THEN violation

[RULE-04] Senior leaders and executives MUST participate in targeted phishing simulation exercises at least quarterly.
[VALIDATION] IF role IN ["executive", "senior_leader"] AND phishing_simulation_participation < 90_days THEN violation

[RULE-05] Privacy personnel MUST complete practical exercises on conducting privacy impact assessments and handling PII scenarios annually.
[VALIDATION] IF role CONTAINS "privacy" AND pia_exercises_completion < 365_days THEN violation

[RULE-06] All practical exercises MUST include performance metrics and pass/fail criteria with remedial training for failures.
[VALIDATION] IF practical_exercise EXISTS AND (performance_metrics = FALSE OR pass_fail_criteria = FALSE) THEN violation

[RULE-07] Exercise scenarios MUST be updated annually to reflect current threat landscape and regulatory changes.
[VALIDATION] IF exercise_last_updated > 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Exercise Development - Design role-specific practical exercises with measurable objectives
- [PROC-02] Simulation Management - Conduct phishing simulations and track response metrics
- [PROC-03] Performance Assessment - Evaluate exercise completion and identify remedial training needs
- [PROC-04] Scenario Updates - Annual review and update of exercise scenarios based on threat intelligence

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major security incidents, regulatory changes, significant threat landscape changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Developer Without Secure Coding Exercise]
IF role = "software_developer"
AND secure_coding_exercise_completion > 365_days
AND system_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Executive Phishing Simulation Overdue]
IF role IN ["C-level", "VP", "Director"]
AND last_phishing_simulation > 90_days
AND email_access = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Privacy Training Without PII Exercises]
IF privacy_training_required = TRUE
AND pii_handling_exercises = FALSE
AND data_access_level = "sensitive"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Contractor Exercise Exemption]
IF user_type = "contractor"
AND system_access_level = "privileged"
AND practical_exercises_completed = FALSE
AND documented_exemption = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Outdated Exercise Scenarios]
IF exercise_content_last_updated > 365_days
AND active_training_program = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Practical exercises in security training that reinforce training objectives are provided | [RULE-01], [RULE-03], [RULE-04] |
| Practical exercises in privacy training that reinforce training objectives are provided | [RULE-02], [RULE-05] |
| Exercise effectiveness and performance measurement | [RULE-06] |
| Current and relevant exercise content | [RULE-07] |
```