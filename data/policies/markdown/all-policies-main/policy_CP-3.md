# POLICY: CP-3: Contingency Training

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-3 |
| NIST Control | CP-3: Contingency Training |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | contingency, training, business continuity, disaster recovery, roles, responsibilities, emergency response |

## 1. POLICY STATEMENT
All system users with assigned contingency roles and responsibilities must receive role-appropriate contingency training within defined timeframes. Training content must be regularly reviewed, updated, and delivered to ensure personnel can effectively execute contingency plans during disruptions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | CONDITIONAL | Only those with contingency roles |
| Contractors | CONDITIONAL | Only those with contingency responsibilities |
| Third-party vendors | CONDITIONAL | Only those supporting critical systems |
| All information systems | YES | Systems covered by contingency plans |
| Cloud services | YES | Including hybrid cloud infrastructure |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve contingency training program<br>• Define training requirements and frequencies<br>• Ensure compliance with regulatory requirements |
| Business Continuity Manager | • Develop role-specific training content<br>• Schedule and deliver training sessions<br>• Maintain training records and track completion |
| System Administrators | • Receive specialized technical recovery training<br>• Participate in system restoration exercises<br>• Maintain current knowledge of backup procedures |
| Department Managers | • Identify personnel with contingency roles<br>• Ensure team members complete required training<br>• Support training schedule compliance |

## 4. RULES
[RULE-01] Personnel assuming contingency roles MUST complete initial contingency training within 30 days of role assignment.
[VALIDATION] IF role_assignment_date + 30_days < current_date AND initial_training_completed = FALSE THEN violation

[RULE-02] System administrators with contingency responsibilities MUST complete technical recovery training within 15 days of role assignment.
[VALIDATION] IF user_role = "system_administrator" AND contingency_role = TRUE AND technical_training_completed = FALSE AND assignment_date + 15_days < current_date THEN violation

[RULE-03] All personnel with contingency roles MUST complete refresher training annually.
[VALIDATION] IF contingency_role = TRUE AND last_training_date + 365_days < current_date THEN violation

[RULE-04] Contingency training content MUST be reviewed and updated annually and within 90 days of significant system changes.
[VALIDATION] IF last_content_review + 365_days < current_date OR (significant_change_date + 90_days < current_date AND content_updated = FALSE) THEN violation

[RULE-05] Personnel MUST complete updated training within 60 days when system changes affect their contingency responsibilities.
[VALIDATION] IF system_change_affects_role = TRUE AND updated_training_completed = FALSE AND change_date + 60_days < current_date THEN violation

[RULE-06] Training completion records MUST be maintained for a minimum of 3 years.
[VALIDATION] IF training_record_retention < 3_years THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Contingency Role Assignment - Process for identifying and assigning contingency responsibilities
- [PROC-02] Training Content Development - Creating role-specific training materials and curricula
- [PROC-03] Training Delivery and Tracking - Scheduling, conducting, and documenting training completion
- [PROC-04] Training Content Review - Regular assessment and updating of training materials
- [PROC-05] Training Records Management - Maintaining and archiving training documentation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Contingency plan activation, failed contingency tests, regulatory changes, significant system modifications, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Administrator]
IF user_role = "system_administrator"
AND contingency_responsibilities_assigned = TRUE
AND days_since_assignment > 15
AND technical_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Annual Training Overdue]
IF contingency_role = TRUE
AND last_training_completion_date + 365_days < current_date
AND no_valid_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: System Change Impact]
IF major_system_change = TRUE
AND change_affects_contingency_procedures = TRUE
AND personnel_retrained = FALSE
AND days_since_change > 60
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Training Content Outdated]
IF contingency_plan_updated = TRUE
AND training_content_updated = FALSE
AND days_since_plan_update > 90
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Contractor with Contingency Role]
IF user_type = "contractor"
AND contingency_role_assigned = TRUE
AND initial_training_completed = TRUE
AND training_completion_date + 365_days < current_date
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Training provided within defined timeframe after role assignment | RULE-01, RULE-02 |
| Training provided when required by system changes | RULE-05 |
| Periodic refresher training provided | RULE-03 |
| Training content reviewed and updated regularly | RULE-04 |
| Training content updated following triggering events | RULE-04 |
| Training records maintained | RULE-06 |