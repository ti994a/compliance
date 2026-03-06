```markdown
# POLICY: AT-6: Training Feedback

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-6 |
| NIST Control | AT-6: Training Feedback |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | training feedback, awareness training, role-based training, training results, senior management |

## 1. POLICY STATEMENT
The organization SHALL provide systematic feedback on training results to designated personnel at defined frequencies. Training feedback MUST include both general awareness training results and specialized role-based training results to support continuous improvement of training programs.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Subject to training feedback reporting |
| Contractors | YES | When receiving organizational training |
| Training administrators | YES | Responsible for generating feedback |
| Senior management | YES | Recipients of training feedback |
| Third-party training providers | CONDITIONAL | When providing organizational training |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Training Manager | • Generate training feedback reports<br>• Analyze training completion and performance data<br>• Distribute feedback to designated personnel |
| Senior Management | • Review training feedback reports<br>• Take corrective actions for training deficiencies<br>• Approve training program modifications |
| HR Business Partners | • Coordinate feedback delivery to business units<br>• Support remedial training efforts<br>• Maintain training feedback documentation |

## 4. RULES
[RULE-01] Training feedback reports MUST be generated and distributed quarterly to designated senior management personnel.
[VALIDATION] IF current_date - last_feedback_date > 90_days AND feedback_generated = FALSE THEN violation

[RULE-02] Training feedback MUST include both awareness training results and role-based training completion rates, failure rates, and performance metrics.
[VALIDATION] IF feedback_report_contains_awareness_training = FALSE OR feedback_report_contains_role_based_training = FALSE THEN violation

[RULE-03] Personnel in critical security roles with training failures MUST be reported to senior management within 5 business days of failure identification.
[VALIDATION] IF critical_role_training_failure = TRUE AND days_since_failure > 5 AND senior_mgmt_notified = FALSE THEN critical_violation

[RULE-04] Training feedback reports MUST identify trends, deficiencies, and recommended improvements to training programs.
[VALIDATION] IF feedback_report_contains_trends = FALSE OR feedback_report_contains_recommendations = FALSE THEN violation

[RULE-05] Remedial training plans MUST be developed within 15 business days for personnel or groups with training completion rates below 85%.
[VALIDATION] IF training_completion_rate < 85% AND remedial_plan_created = FALSE AND days_since_identification > 15 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Training Results Analysis - Systematic collection and analysis of training completion and performance data
- [PROC-02] Feedback Report Generation - Creation of standardized training feedback reports with metrics and trends
- [PROC-03] Senior Management Briefing - Regular presentation of training feedback to executive leadership
- [PROC-04] Remedial Training Planning - Development of corrective training plans for deficient areas

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Significant training failures, regulatory changes, major organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: Quarterly Feedback Overdue]
IF current_date - last_feedback_date > 95_days
AND feedback_report_generated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Critical Role Training Failure]
IF employee_role = "critical_security"
AND training_status = "failed"
AND days_since_failure = 7
AND senior_management_notified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Low Completion Rate Without Remediation]
IF department_training_completion_rate = 78%
AND days_since_identification = 20
AND remedial_plan_exists = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete Feedback Report]
IF feedback_report_generated = TRUE
AND awareness_training_data_included = FALSE
AND role_based_training_data_included = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Timely Comprehensive Feedback]
IF feedback_report_generated = TRUE
AND report_includes_trends = TRUE
AND report_includes_recommendations = TRUE
AND delivered_to_senior_mgmt = TRUE
AND delivery_within_schedule = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Provide feedback at defined frequency | [RULE-01] |
| Include awareness and role-based training results | [RULE-02] |
| Report critical role training failures | [RULE-03] |
| Identify trends and improvements | [RULE-04] |
| Develop remedial training plans | [RULE-05] |
```