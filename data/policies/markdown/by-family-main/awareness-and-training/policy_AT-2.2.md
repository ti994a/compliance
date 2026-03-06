```markdown
# POLICY: AT-2.2: Insider Threat

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-2.2 |
| NIST Control | AT-2.2: Insider Threat |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | insider threat, literacy training, awareness, behavioral indicators, reporting, recognition |

## 1. POLICY STATEMENT
All personnel MUST receive literacy training on recognizing and reporting potential indicators of insider threat. Training content SHALL be tailored to role-specific responsibilities and updated based on emerging threat patterns.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Employees | YES | Including full-time, part-time, temporary |
| Contractors | YES | Extended engagements >30 days |
| Third-party Personnel | CONDITIONAL | If accessing internal systems |
| Managers/Supervisors | YES | Enhanced training requirements |
| Security Personnel | YES | Advanced threat recognition training |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Security Officer | • Approve training curriculum and updates<br>• Define insider threat indicators<br>• Establish reporting channels |
| HR Director | • Coordinate training delivery<br>• Maintain training records<br>• Support incident response for personnel issues |
| Training Coordinator | • Develop role-specific training content<br>• Schedule and track completion<br>• Update materials based on threat intelligence |
| Managers/Supervisors | • Monitor team behavioral changes<br>• Report concerning behaviors<br>• Reinforce training concepts |

## 4. RULES
[RULE-01] All personnel MUST complete insider threat literacy training within 30 days of hire or role change.
[VALIDATION] IF employee_start_date + 30_days < current_date AND training_completed = FALSE THEN violation

[RULE-02] Insider threat training MUST be refreshed annually for all personnel.
[VALIDATION] IF last_training_date + 365_days < current_date THEN violation

[RULE-03] Training curriculum MUST include recognition of behavioral indicators including job dissatisfaction, unauthorized access attempts, unexplained financial access, workplace violence, and policy violations.
[VALIDATION] IF training_curriculum_missing_required_indicators = TRUE THEN violation

[RULE-04] Training MUST include established reporting channels and procedures for communicating insider threat concerns.
[VALIDATION] IF training_content_includes_reporting_procedures = FALSE THEN violation

[RULE-05] Manager-level training MUST include additional content on behavioral change detection and team monitoring techniques.
[VALIDATION] IF user_role = "manager" AND enhanced_training_completed = FALSE THEN violation

[RULE-06] Training materials MUST be updated within 90 days when new insider threat indicators are identified or reporting procedures change.
[VALIDATION] IF material_update_trigger_date + 90_days < current_date AND materials_updated = FALSE THEN violation

[RULE-07] Training completion rates MUST achieve 95% compliance across all personnel categories.
[VALIDATION] IF training_completion_rate < 95% THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Insider Threat Training Development - Role-specific curriculum creation and maintenance
- [PROC-02] Training Delivery and Tracking - Scheduling, delivery methods, and completion monitoring
- [PROC-03] Incident Reporting Procedures - Channels and processes for reporting potential threats
- [PROC-04] Training Effectiveness Assessment - Evaluation methods and improvement processes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving insider threats, significant organizational changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee Training Compliance]
IF employee_type = "new_hire"
AND days_since_start > 30
AND insider_threat_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Manager Enhanced Training]
IF user_role = "manager" OR user_role = "supervisor"
AND standard_training_completed = TRUE
AND enhanced_manager_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Annual Refresh Overdue]
IF last_training_completion_date + 365_days < current_date
AND active_employee = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Outdated Training Materials]
IF new_threat_indicators_identified = TRUE
AND material_last_updated + 90_days < current_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Contractor Extended Engagement]
IF user_type = "contractor"
AND engagement_duration > 30_days
AND insider_threat_training_completed = FALSE
AND system_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Literacy training on recognizing potential indicators provided | RULE-01, RULE-02, RULE-03 |
| Literacy training on reporting potential indicators provided | RULE-01, RULE-02, RULE-04 |
| Role-tailored training content | RULE-05 |
| Training currency and effectiveness | RULE-06, RULE-07 |
```