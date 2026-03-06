# POLICY: AC-10: Concurrent Session Control

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-10 |
| NIST Control | AC-10: Concurrent Session Control |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | concurrent sessions, access control, session limits, account management, system security |

## 1. POLICY STATEMENT
The organization SHALL limit the number of concurrent sessions for system accounts based on defined account types and security requirements. Session limits MUST be enforced automatically by system controls to prevent unauthorized resource consumption and potential security risks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All system accounts | YES | Including user, service, and administrative accounts |
| Interactive sessions | YES | GUI, CLI, API, and remote access sessions |
| Service accounts | YES | Automated processes and system integrations |
| Guest/temporary accounts | YES | Limited access accounts |
| Emergency accounts | CONDITIONAL | May have different limits during incidents |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure session limits in system settings<br>• Monitor concurrent session usage<br>• Implement technical controls for session enforcement |
| Security Team | • Define session limit requirements by account type<br>• Review session limit violations<br>• Audit compliance with session controls |
| Account Managers | • Assign appropriate account types with corresponding session limits<br>• Document business justification for session limit exceptions |

## 4. RULES
[RULE-01] Standard user accounts MUST be limited to a maximum of 3 concurrent sessions per account.
[VALIDATION] IF account_type = "standard_user" AND concurrent_sessions > 3 THEN violation

[RULE-02] Administrative accounts MUST be limited to a maximum of 2 concurrent sessions per account.
[VALIDATION] IF account_type = "administrator" AND concurrent_sessions > 2 THEN violation

[RULE-03] Service accounts MUST be limited to the minimum number of concurrent sessions required for business function, not to exceed 5 sessions.
[VALIDATION] IF account_type = "service" AND concurrent_sessions > documented_business_requirement AND concurrent_sessions > 5 THEN violation

[RULE-04] Privileged accounts (database admin, security admin) MUST be limited to 1 concurrent session per account.
[VALIDATION] IF account_type IN ["database_admin", "security_admin", "domain_admin"] AND concurrent_sessions > 1 THEN critical_violation

[RULE-05] Systems MUST automatically enforce session limits and deny new session requests when limits are exceeded.
[VALIDATION] IF session_limit_reached = TRUE AND new_session_allowed = TRUE THEN critical_violation

[RULE-06] Session limit exceptions MUST be documented with business justification and approved by the system owner and security team.
[VALIDATION] IF concurrent_sessions > defined_limit AND (business_justification = NULL OR security_approval = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Session Limit Configuration - Configure and maintain session limits in system authentication mechanisms
- [PROC-02] Session Monitoring - Monitor and alert on concurrent session usage and violations
- [PROC-03] Exception Management - Process for requesting, approving, and documenting session limit exceptions
- [PROC-04] Session Limit Review - Periodic review of session limits and usage patterns

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving session abuse, system architecture changes, new account types

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard User Exceeding Limit]
IF account_type = "standard_user"
AND concurrent_sessions = 4
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Admin Account Multiple Sessions]
IF account_type = "administrator"
AND concurrent_sessions = 3
AND session_enforcement = "active"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Service Account with Justification]
IF account_type = "service"
AND concurrent_sessions = 6
AND business_justification = "documented"
AND security_approval = TRUE
THEN compliance = TRUE

[SCENARIO-04: Privileged Account Violation]
IF account_type = "security_admin"
AND concurrent_sessions > 1
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: System Not Enforcing Limits]
IF session_limits_configured = TRUE
AND automatic_enforcement = FALSE
AND users_can_exceed_limits = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Number of concurrent sessions defined for account types | [RULE-01], [RULE-02], [RULE-03], [RULE-04] |
| Concurrent sessions limited to defined numbers | [RULE-05], [RULE-06] |
| Technical enforcement of session limits | [RULE-05] |
| Exception handling and documentation | [RULE-06] |