# POLICY: PS-4.2: Personnel Security - Automated Actions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-4.2 |
| NIST Control | PS-4.2: Personnel Security - Automated Actions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | personnel termination, automated notifications, access revocation, HR systems, identity management |

## 1. POLICY STATEMENT
The organization SHALL implement automated mechanisms to notify designated personnel and roles of individual termination actions and to disable access to system resources. Automated notifications MUST be sent immediately upon termination processing to ensure timely access revocation and security response.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full-time, part-time, temporary |
| Contractors | YES | When granted system access |
| Vendors | YES | When granted system access |
| Interns | YES | All categories |
| Board members | CONDITIONAL | Only if granted direct system access |
| Guest accounts | NO | Covered under separate procedures |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Operations | • Configure automated termination workflows<br>• Initiate termination process in HRIS<br>• Verify notification delivery |
| Identity Management Team | • Maintain automated access revocation systems<br>• Monitor termination processing<br>• Escalate failed automations |
| Security Operations Center | • Receive and act on termination notifications<br>• Verify access revocation completion<br>• Investigate anomalous termination patterns |
| IT Service Desk | • Execute manual fallback procedures<br>• Provide termination status updates<br>• Document automation failures |

## 4. RULES
[RULE-01] Automated mechanisms MUST notify designated personnel within 15 minutes of termination processing initiation in the HRIS system.
[VALIDATION] IF termination_initiated = TRUE AND notification_sent_time > (termination_time + 15_minutes) THEN violation

[RULE-02] Automated notifications MUST be sent to the employee's direct manager, IT security team, facilities management, and system administrators for any systems the individual had privileged access to.
[VALIDATION] IF termination_processed = TRUE AND (manager_notified = FALSE OR security_notified = FALSE OR facilities_notified = FALSE) THEN violation

[RULE-03] Automated access revocation MUST disable at minimum: network accounts, email access, VPN access, and physical access cards within 1 hour of termination for standard terminations.
[VALIDATION] IF termination_type = "standard" AND (network_disabled = FALSE OR email_disabled = FALSE OR vpn_disabled = FALSE OR badge_disabled = FALSE) AND time_elapsed > 1_hour THEN violation

[RULE-04] For involuntary terminations or security-related terminations, automated access revocation MUST occur within 15 minutes.
[VALIDATION] IF (termination_type = "involuntary" OR termination_reason = "security") AND access_revoked_time > (termination_time + 15_minutes) THEN critical_violation

[RULE-05] Automated mechanisms MUST generate audit logs of all notification attempts and access revocation actions with timestamps and success/failure status.
[VALIDATION] IF termination_processed = TRUE AND (notification_logs = NULL OR revocation_logs = NULL) THEN violation

[RULE-06] Failed automated notifications or access revocations MUST trigger immediate manual backup procedures and alert the Security Operations Center.
[VALIDATION] IF (notification_failed = TRUE OR revocation_failed = TRUE) AND soc_alerted = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Automated Termination Workflow Configuration - Define and maintain HRIS integration with identity management systems
- [PROC-02] Notification Distribution Lists Management - Maintain current lists of personnel requiring termination notifications
- [PROC-03] Manual Fallback Procedures - Execute manual termination steps when automation fails
- [PROC-04] Termination Audit and Verification - Verify completion of automated termination actions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Automation system changes, HRIS upgrades, security incidents involving terminated employees, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Employee Termination]
IF employee_type = "full_time"
AND termination_type = "voluntary"
AND automated_notifications_sent = TRUE
AND access_revoked_within_1_hour = TRUE
THEN compliance = TRUE

[SCENARIO-02: Failed Automation with Manual Override]
IF automated_notification = FAILED
AND manual_notification_completed = TRUE
AND notification_time < (termination_time + 30_minutes)
AND soc_alerted = TRUE
THEN compliance = TRUE

[SCENARIO-03: Security Termination Delay]
IF termination_reason = "security_violation"
AND access_revoked_time > (termination_time + 15_minutes)
AND no_manual_override = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Contractor Access After Project End]
IF user_type = "contractor"
AND project_end_date < current_date
AND automated_termination_triggered = FALSE
AND active_system_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Incomplete Notification Distribution]
IF termination_processed = TRUE
AND manager_notified = TRUE
AND security_team_notified = FALSE
AND privileged_access = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Automated mechanisms to notify personnel of termination actions are defined | [RULE-02] |
| Automated mechanisms are used to notify designated personnel | [RULE-01], [RULE-06] |
| Automated mechanisms disable access to system resources | [RULE-03], [RULE-04] |
| Notifications occur in timely manner | [RULE-01], [RULE-04] |
| Termination actions are properly documented | [RULE-05] |