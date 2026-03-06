# POLICY: SI-4.21: Probationary Periods

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.21 |
| NIST Control | SI-4.21: Probationary Periods |
| Version | 1.0 |
| Owner | CISO |
| Keywords | probationary monitoring, employee surveillance, insider threat, system monitoring, access oversight |

## 1. POLICY STATEMENT
All individuals during their probationary employment period SHALL be subject to additional monitoring of their system activities and data access beyond standard monitoring applied to permanent employees. Enhanced monitoring measures MUST be implemented to detect potentially malicious activity or inappropriate behavior during the probationary period.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Probationary employees | YES | All new hires during probationary period |
| Contract employees | YES | First 90 days or contract duration if shorter |
| Temporary workers | YES | Entire duration of temporary assignment |
| Permanent employees | NO | Standard monitoring applies |
| Consultants | CONDITIONAL | If accessing sensitive systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center | • Monitor probationary user activities • Generate daily activity reports • Escalate suspicious behavior • Maintain monitoring logs |
| HR Department | • Notify IT Security of probationary status • Provide probationary period timelines • Coordinate status changes • Document employment transitions |
| Direct Supervisors | • Review daily activity reports • Validate business justification for access • Report concerning behaviors • Approve access requests |

## 4. RULES

[RULE-01] All probationary employees MUST have enhanced monitoring enabled within 24 hours of their start date.
[VALIDATION] IF employee_status = "probationary" AND monitoring_enabled = FALSE AND days_since_start > 1 THEN violation

[RULE-02] Probationary employees SHALL NOT access sensitive data systems without explicit supervisor approval and additional monitoring controls.
[VALIDATION] IF employee_status = "probationary" AND sensitive_system_access = TRUE AND supervisor_approval = FALSE THEN critical_violation

[RULE-03] All file transfers, email communications, and system access by probationary employees MUST be logged and reviewed daily.
[VALIDATION] IF employee_status = "probationary" AND daily_review_completed = FALSE THEN violation

[RULE-04] Probationary monitoring controls MUST be removed within 48 hours of permanent employment confirmation.
[VALIDATION] IF employee_status = "permanent" AND enhanced_monitoring = TRUE AND hours_since_confirmation > 48 THEN violation

[RULE-05] Suspicious activities by probationary employees MUST be escalated to HR and management within 4 hours of detection.
[VALIDATION] IF employee_status = "probationary" AND suspicious_activity = TRUE AND escalation_time > 4_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Probationary Employee Onboarding - Configure enhanced monitoring during account provisioning
- [PROC-02] Daily Activity Review - Review and document probationary employee activities
- [PROC-03] Incident Escalation - Process for reporting suspicious probationary employee behavior
- [PROC-04] Monitoring Removal - Disable enhanced monitoring upon permanent status confirmation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving probationary employees, changes to employment policies, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Probationary Employee Accessing Sensitive Data]
IF employee_status = "probationary"
AND system_classification = "sensitive" 
AND supervisor_approval = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Missing Daily Review]
IF employee_status = "probationary"
AND current_date > hire_date
AND daily_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Enhanced Monitoring Not Enabled]
IF employee_status = "probationary"
AND days_since_start >= 1
AND enhanced_monitoring = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Monitoring Not Removed After Permanent Status]
IF employee_status = "permanent"
AND enhanced_monitoring = TRUE
AND hours_since_status_change > 48
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Delayed Incident Escalation]
IF employee_status = "probationary"
AND incident_detected = TRUE
AND escalation_completed = FALSE
AND hours_since_detection > 4
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Additional monitoring implemented during probationary periods | [RULE-01], [RULE-03] |
| Probationary period monitoring controls defined | [RULE-02], [RULE-05] |
| Monitoring process documentation | [PROC-01], [PROC-02] |
| Incident response for probationary employees | [RULE-05], [PROC-03] |