# POLICY: PS-4.2: Automated Actions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-4.2 |
| NIST Control | PS-4.2: Automated Actions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | automated termination, access revocation, personnel notifications, system disabling, termination alerts |

## 1. POLICY STATEMENT
The organization SHALL implement automated mechanisms to notify designated personnel and roles of individual termination actions and automatically disable access to system resources. These automated processes ensure timely and comprehensive response to personnel terminations across all organizational systems and stakeholders.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full-time, part-time, temporary |
| Contractors | YES | All contracted personnel with system access |
| Privileged users | YES | Enhanced monitoring and faster response |
| Service accounts | CONDITIONAL | When tied to individual personnel |
| Shared accounts | NO | Covered under separate access controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define automated notification requirements<br>• Approve termination workflow automation<br>• Oversee policy compliance monitoring |
| HR Department | • Initiate termination process in HRIS<br>• Provide termination classification<br>• Validate automated notification delivery |
| IT Security Team | • Configure automated access revocation<br>• Monitor termination alert systems<br>• Validate complete access removal |
| System Administrators | • Respond to termination notifications<br>• Execute manual remediation when needed<br>• Document termination completion |

## 4. RULES
[RULE-01] Automated mechanisms MUST notify designated personnel within 15 minutes of termination record creation in the authoritative HR system.
[VALIDATION] IF termination_initiated = TRUE AND notification_time > 15_minutes THEN violation

[RULE-02] Automated systems MUST disable logical access to all organizational information systems within 1 hour for standard terminations and within 15 minutes for involuntary terminations.
[VALIDATION] IF termination_type = "standard" AND access_disabled_time > 1_hour THEN violation
[VALIDATION] IF termination_type = "involuntary" AND access_disabled_time > 15_minutes THEN critical_violation

[RULE-03] Notification recipients MUST include the employee's direct supervisor, IT security team, facility security, and system administrators for any systems where the individual held privileged access.
[VALIDATION] IF privileged_access = TRUE AND (supervisor_notified = FALSE OR security_notified = FALSE OR sysadmin_notified = FALSE) THEN violation

[RULE-04] Automated termination processes MUST generate audit logs documenting all notification deliveries and access revocation actions with timestamps.
[VALIDATION] IF termination_processed = TRUE AND audit_log_generated = FALSE THEN violation

[RULE-05] Failed automated termination actions MUST trigger immediate alerts to IT security personnel and initiate manual backup procedures within 30 minutes.
[VALIDATION] IF automation_failed = TRUE AND manual_process_initiated = FALSE AND time_elapsed > 30_minutes THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Automated Termination Workflow Configuration - Define system integrations and notification routing
- [PROC-02] Termination Alert Response - Standard operating procedures for notification recipients
- [PROC-03] Manual Backup Procedures - Process when automated systems fail
- [PROC-04] Audit Log Review - Regular verification of automated termination completeness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: System changes, failed automations, audit findings, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Employee Termination]
IF termination_type = "standard"
AND hr_system_updated = TRUE
AND notification_sent_within_15min = TRUE
AND access_disabled_within_1hour = TRUE
THEN compliance = TRUE

[SCENARIO-02: Failed Automation Backup]
IF automated_termination = "failed"
AND manual_process_initiated = TRUE
AND security_team_alerted = TRUE
AND backup_completed_within_30min = TRUE
THEN compliance = TRUE

[SCENARIO-03: Privileged User Involuntary Termination]
IF user_privilege_level = "high"
AND termination_type = "involuntary"
AND access_disabled_within_15min = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Notification Recipients]
IF termination_processed = TRUE
AND supervisor_notified = FALSE
AND privileged_access = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Audit Trail Gap]
IF termination_completed = TRUE
AND audit_log_generated = FALSE
AND compliance_review = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Automated mechanisms notify personnel of termination actions | [RULE-01], [RULE-03] |
| Automated mechanisms disable access to system resources | [RULE-02] |
| Comprehensive notification to appropriate roles | [RULE-03] |
| Audit trail of automated actions | [RULE-04] |
| Backup procedures for automation failures | [RULE-05] |