# POLICY: AC-7: Unsuccessful Logon Attempts

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-7 |
| NIST Control | AC-7: Unsuccessful Logon Attempts |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | logon, authentication, account lockout, brute force, failed attempts |

## 1. POLICY STATEMENT
The organization SHALL enforce limits on consecutive invalid logon attempts and automatically lock accounts when thresholds are exceeded to prevent brute force attacks. Account lockouts MUST be temporary with defined unlock procedures to balance security and availability.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including local and network connections |
| User accounts | YES | All privileged and non-privileged accounts |
| Service accounts | CONDITIONAL | Exempt only with documented risk assessment |
| Emergency accounts | CONDITIONAL | May have modified thresholds with approval |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure lockout thresholds per system classification<br>• Monitor lockout events<br>• Implement unlock procedures |
| Security Operations Center | • Monitor failed authentication patterns<br>• Investigate suspicious lockout events<br>• Escalate potential attacks |
| Identity and Access Management Team | • Define threshold standards<br>• Approve exceptions<br>• Review lockout policies quarterly |

## 4. RULES
[RULE-01] Systems MUST enforce a maximum of 5 consecutive invalid logon attempts within a 15-minute period for standard user accounts.
[VALIDATION] IF failed_attempts >= 5 AND time_window <= 15_minutes THEN account_lockout_required

[RULE-02] Privileged accounts MUST be locked after 3 consecutive invalid logon attempts within a 15-minute period.
[VALIDATION] IF account_type = "privileged" AND failed_attempts >= 3 AND time_window <= 15_minutes THEN account_lockout_required

[RULE-03] Account lockouts MUST be temporary with automatic unlock after 30 minutes for standard accounts and 60 minutes for privileged accounts.
[VALIDATION] IF account_type = "standard" AND lockout_duration > 30_minutes THEN violation
[VALIDATION] IF account_type = "privileged" AND lockout_duration > 60_minutes THEN violation

[RULE-04] Systems MUST log all failed authentication attempts including username, timestamp, source IP, and lockout actions.
[VALIDATION] IF failed_attempt_logged = FALSE OR required_fields_missing = TRUE THEN violation

[RULE-05] Manual account unlocks MUST require approval from the user's manager or security team for privileged accounts.
[VALIDATION] IF account_type = "privileged" AND manual_unlock = TRUE AND approval_documented = FALSE THEN violation

[RULE-06] Systems MUST implement progressive delays between authentication attempts after the second failed attempt.
[VALIDATION] IF failed_attempts >= 2 AND delay_implemented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Account Lockout Configuration - Standard configurations for different system types and account classifications
- [PROC-02] Manual Account Unlock - Process for emergency unlocks with proper authorization
- [PROC-03] Lockout Monitoring - Procedures for detecting and responding to suspicious lockout patterns
- [PROC-04] Exception Management - Process for approving alternative lockout thresholds

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving authentication, system updates, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard User Lockout]
IF account_type = "standard"
AND failed_attempts = 5
AND time_window <= 15_minutes
THEN compliance = TRUE (lockout required)

[SCENARIO-02: Privileged Account Violation]
IF account_type = "privileged"
AND failed_attempts = 5
AND lockout_triggered = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Extended Lockout Duration]
IF account_locked = TRUE
AND lockout_duration > 60_minutes
AND manual_unlock_unavailable = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Audit Trail]
IF failed_attempt_occurred = TRUE
AND (username_logged = FALSE OR timestamp_logged = FALSE OR source_ip_logged = FALSE)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Service Account Exception]
IF account_type = "service"
AND lockout_disabled = TRUE
AND risk_assessment_documented = TRUE
AND annual_review_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Enforce limit of consecutive invalid logon attempts | [RULE-01], [RULE-02] |
| Define time period for attempt counting | [RULE-01], [RULE-02] |
| Automatically lock account when threshold exceeded | [RULE-01], [RULE-02] |
| Log unsuccessful authentication events | [RULE-04] |
| Implement appropriate lockout duration | [RULE-03] |