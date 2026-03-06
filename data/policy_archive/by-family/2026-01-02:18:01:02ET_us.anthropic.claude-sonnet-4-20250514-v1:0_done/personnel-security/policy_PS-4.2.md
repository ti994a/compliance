# POLICY: PS-4.2: Automated Actions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-4.2 |
| NIST Control | PS-4.2: Automated Actions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | automated termination, access revocation, personnel security, notifications, system access |

## 1. POLICY STATEMENT
The organization SHALL implement automated mechanisms to notify designated personnel and roles of individual termination actions and to disable access to system resources. These automated processes ensure timely and comprehensive response to personnel terminations across all organizational systems and resources.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full-time, part-time, temporary |
| Contractors | YES | All contracted personnel with system access |
| Vendors | YES | Third-party personnel with privileged access |
| Interns | YES | All personnel with any system access |
| Cloud systems | YES | All hybrid cloud infrastructure |
| On-premises systems | YES | All internal systems and applications |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Oversee automated termination policy compliance<br>• Approve automated mechanism configurations<br>• Review termination process effectiveness |
| IT Security Team | • Configure and maintain automated notification systems<br>• Monitor automated access revocation processes<br>• Validate termination automation effectiveness |
| HR Department | • Initiate termination workflows in HRIS<br>• Ensure accurate termination data entry<br>• Coordinate with IT for access requirements |
| System Administrators | • Implement automated access revocation tools<br>• Monitor system access removal completion<br>• Maintain termination automation logs |

## 4. RULES
[RULE-01] Automated mechanisms MUST notify designated security personnel within 15 minutes of termination initiation in the HRIS system.
[VALIDATION] IF termination_initiated = TRUE AND notification_time > 15_minutes THEN violation

[RULE-02] Automated systems MUST disable standard user access within 2 hours of termination notification for voluntary terminations.
[VALIDATION] IF termination_type = "voluntary" AND access_disabled_time > 2_hours THEN violation

[RULE-03] Automated systems MUST disable all access within 30 minutes of termination notification for involuntary or security-related terminations.
[VALIDATION] IF termination_type IN ["involuntary", "security"] AND access_disabled_time > 30_minutes THEN critical_violation

[RULE-04] Automated notification mechanisms MUST alert IT security, direct managers, and facility security simultaneously upon termination initiation.
[VALIDATION] IF termination_initiated = TRUE AND (security_notified = FALSE OR manager_notified = FALSE OR facility_notified = FALSE) THEN violation

[RULE-05] Automated access revocation MUST cover all systems including Active Directory, cloud platforms, VPN, and physical access controls.
[VALIDATION] IF termination_processed = TRUE AND (AD_disabled = FALSE OR cloud_disabled = FALSE OR vpn_disabled = FALSE OR badge_disabled = FALSE) THEN violation

[RULE-06] Automated mechanisms MUST generate audit logs of all termination actions and notifications with timestamps and system responses.
[VALIDATION] IF termination_processed = TRUE AND audit_log_created = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Automated Termination Workflow Configuration - Define HRIS integration and notification triggers
- [PROC-02] Multi-System Access Revocation Automation - Configure automated disabling across all platforms
- [PROC-03] Termination Notification Distribution - Establish automated alert routing and escalation
- [PROC-04] Audit Log Collection and Review - Implement logging and monitoring of automated actions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: System changes, security incidents, failed automations, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Employee Voluntary Termination]
IF employee_type = "full_time"
AND termination_type = "voluntary"
AND automated_notification_sent = TRUE
AND access_disabled_time <= 2_hours
THEN compliance = TRUE

[SCENARIO-02: Contractor Involuntary Termination]
IF user_type = "contractor"
AND termination_type = "involuntary"
AND access_disabled_time > 30_minutes
AND automated_notification_sent = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Failed Automation with Manual Override]
IF termination_initiated = TRUE
AND automated_mechanism_failed = TRUE
AND manual_override_time > 1_hour
AND security_team_notified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Privileged User Security Termination]
IF user_privileges = "administrative"
AND termination_reason = "security_incident"
AND access_disabled_time <= 15_minutes
AND all_systems_revoked = TRUE
THEN compliance = TRUE

[SCENARIO-05: Incomplete Automated Revocation]
IF termination_processed = TRUE
AND AD_access = "disabled"
AND cloud_access = "enabled"
AND automated_audit_log = "generated"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Automated mechanisms notify personnel of termination actions | [RULE-01], [RULE-04] |
| Automated mechanisms disable access to system resources | [RULE-02], [RULE-03], [RULE-05] |
| Comprehensive coverage of all system types | [RULE-05] |
| Audit trail of automated actions | [RULE-06] |
| Timely response to termination events | [RULE-01], [RULE-02], [RULE-03] |