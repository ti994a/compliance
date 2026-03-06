# POLICY: AC-2.5: Inactivity Logout

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-2.5 |
| NIST Control | AC-2.5: Inactivity Logout |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | inactivity, logout, session management, user behavior, access control |

## 1. POLICY STATEMENT
Users MUST manually log out of systems when expecting periods of inactivity that exceed defined thresholds or meet specific conditions. This policy establishes behavioral requirements for user-initiated logout actions to protect against unauthorized access during periods of user absence.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, temporary |
| Contractors | YES | All contracted personnel with system access |
| Third-party users | YES | External users with authorized access |
| Privileged accounts | YES | Enhanced requirements apply |
| Service accounts | NO | Covered under automated controls |
| Shared workstations | YES | Special requirements apply |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Users | • Log out when expecting inactivity periods<br>• Follow defined logout procedures<br>• Report logout policy violations |
| IT Security Team | • Define inactivity thresholds by system type<br>• Monitor compliance with logout requirements<br>• Investigate policy violations |
| System Administrators | • Implement logout notification mechanisms<br>• Configure system prompts and warnings<br>• Maintain logout audit trails |

## 4. RULES
[RULE-01] Users MUST log out when expecting to be away from their workstation for more than 15 minutes during business hours or any period outside business hours.
[VALIDATION] IF expected_absence > 15_minutes AND business_hours = TRUE AND manual_logout = FALSE THEN violation
[VALIDATION] IF expected_absence > 0_minutes AND business_hours = FALSE AND manual_logout = FALSE THEN violation

[RULE-02] Users with privileged access MUST log out when expecting to be away from their workstation for more than 5 minutes regardless of time of day.
[VALIDATION] IF user_privilege_level = "high" AND expected_absence > 5_minutes AND manual_logout = FALSE THEN critical_violation

[RULE-03] Users accessing systems containing sensitive data (PII, PHI, financial data) MUST log out immediately when stepping away from unattended workstations.
[VALIDATION] IF data_classification IN ["PII", "PHI", "financial"] AND workstation_unattended = TRUE AND manual_logout = FALSE THEN violation

[RULE-04] Users MUST log out from shared or public workstations immediately upon completion of their work session.
[VALIDATION] IF workstation_type = "shared" OR workstation_type = "public" AND session_complete = TRUE AND manual_logout = FALSE THEN violation

[RULE-05] Users SHALL receive logout reminders when systems detect potential inactivity periods approaching defined thresholds.
[VALIDATION] IF inactivity_approaching_threshold = TRUE AND logout_reminder_sent = FALSE THEN system_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] User Logout Training - Annual training on proper logout procedures and inactivity thresholds
- [PROC-02] Logout Compliance Monitoring - Quarterly review of logout behavior and policy adherence
- [PROC-03] Violation Investigation - Process for investigating and responding to logout policy violations
- [PROC-04] System Configuration - Procedures for implementing logout prompts and user notifications

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unattended sessions, changes to data classification, new system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard User Break]
IF user_privilege = "standard"
AND expected_absence = 20_minutes
AND business_hours = TRUE
AND manual_logout = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-02: Privileged User Brief Absence]
IF user_privilege = "high"
AND expected_absence = 8_minutes
AND manual_logout = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Sensitive Data Access]
IF data_classification = "PII"
AND workstation_unattended = TRUE
AND session_duration = 2_minutes
AND manual_logout = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Shared Workstation Compliance]
IF workstation_type = "shared"
AND work_session_complete = TRUE
AND manual_logout = TRUE
AND logout_time <= 1_minute
THEN compliance = TRUE

[SCENARIO-05: After Hours Access]
IF business_hours = FALSE
AND expected_absence = 5_minutes
AND manual_logout = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Users required to log out when inactivity period defined | RULE-01, RULE-02 |
| Behavioral logout enforcement for sensitive data | RULE-03 |
| Logout requirements for shared resources | RULE-04 |
| User notification and awareness | RULE-05 |