# POLICY: IR-2: Incident Response Training

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IR-2 |
| NIST Control | IR-2: Incident Response Training |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | incident response, training, roles, responsibilities, cybersecurity awareness |

## 1. POLICY STATEMENT
All system users SHALL receive incident response training appropriate to their assigned roles and responsibilities within defined timeframes. Training content MUST be regularly reviewed and updated to maintain effectiveness and relevance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Role-based training requirements |
| Contractors | YES | Must complete training before system access |
| Temporary staff | YES | Abbreviated training within 5 days |
| Third-party vendors | CONDITIONAL | Only if accessing company systems |
| External partners | CONDITIONAL | Only if handling company data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve training curriculum and content<br>• Define role-based training requirements<br>• Ensure policy compliance |
| Security Training Team | • Develop and deliver training content<br>• Track completion rates<br>• Update materials based on lessons learned |
| HR Department | • Coordinate new hire training<br>• Maintain training records<br>• Notify Security team of role changes |
| Managers | • Ensure direct reports complete required training<br>• Identify training needs for their teams<br>• Support incident response activities |

## 4. RULES
[RULE-01] All personnel with system access MUST complete initial incident response training within 30 days of assuming incident response responsibilities or acquiring system access.
[VALIDATION] IF days_since_role_assignment > 30 AND training_completed = FALSE THEN violation

[RULE-02] Personnel in critical incident response roles MUST complete initial training within 15 days of role assignment.
[VALIDATION] IF role_type = "critical_incident_response" AND days_since_assignment > 15 AND training_completed = FALSE THEN critical_violation

[RULE-03] All personnel MUST complete refresher incident response training annually.
[VALIDATION] IF days_since_last_training > 365 THEN violation

[RULE-04] Additional training MUST be provided within 60 days when required by significant system changes.
[VALIDATION] IF system_change_occurred = TRUE AND days_since_change > 60 AND additional_training_completed = FALSE THEN violation

[RULE-05] Training content MUST be reviewed and updated at least annually and within 90 days following significant incidents or audit findings.
[VALIDATION] IF days_since_content_review > 365 THEN violation
[VALIDATION] IF significant_event_occurred = TRUE AND days_since_event > 90 AND content_updated = FALSE THEN violation

[RULE-06] Training MUST be role-appropriate with different content for general users, system administrators, and incident responders.
[VALIDATION] IF training_content ≠ role_requirements THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] New Hire IR Training Process - Standardized onboarding training delivery
- [PROC-02] Role-Based Training Matrix - Mapping of roles to training requirements  
- [PROC-03] Training Content Review Process - Annual and event-driven content updates
- [PROC-04] Training Completion Tracking - Monitoring and reporting mechanisms
- [PROC-05] Training Effectiveness Assessment - Measuring training outcomes and improvements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Major incidents, audit findings, regulatory changes, significant system modifications, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee Access]
IF employee_status = "new_hire"
AND system_access_granted = TRUE
AND days_since_hire > 30
AND ir_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Critical Role Assignment]
IF role_assignment = "incident_response_team"
AND days_since_assignment > 15
AND specialized_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Annual Refresher Overdue]
IF last_training_date < (current_date - 365_days)
AND employee_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Post-Incident Training Update]
IF major_incident_occurred = TRUE
AND days_since_incident > 90
AND training_content_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: System Change Training Gap]
IF significant_system_change = TRUE
AND days_since_change > 60
AND affected_users_retrained = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Training provided within defined timeframe upon role assignment | [RULE-01], [RULE-02] |
| Training provided when required by system changes | [RULE-04] |
| Periodic refresher training provided | [RULE-03] |
| Training content regularly reviewed and updated | [RULE-05] |
| Training appropriate to assigned roles and responsibilities | [RULE-06] |