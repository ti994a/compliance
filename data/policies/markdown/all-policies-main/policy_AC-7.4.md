# POLICY: AC-7.4: Use of Alternate Authentication Factor

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-7.4 |
| NIST Control | AC-7.4: Use of Alternate Authentication Factor |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authentication, alternate factors, lockout, availability, invalid logons |

## 1. POLICY STATEMENT
The organization SHALL allow users to utilize alternate authentication factors different from primary authentication factors after exceeding defined consecutive invalid logon attempts. Limits MUST be enforced on consecutive invalid attempts for both primary and alternate authentication factors to maintain security while supporting availability.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Systems requiring user authentication |
| External users | YES | Including contractors and partners |
| Service accounts | NO | Automated accounts excluded |
| Emergency access accounts | CONDITIONAL | If configured with alternate factors |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define alternate authentication factor policies<br>• Approve lockout thresholds<br>• Oversee compliance monitoring |
| System Administrators | • Configure alternate authentication mechanisms<br>• Monitor lockout events<br>• Maintain authentication logs |
| Identity Management Team | • Implement alternate factor enrollment<br>• Manage factor lifecycle<br>• Support lockout recovery |

## 4. RULES

[RULE-01] Organizations MUST define alternate authentication factors that are different from primary authentication factors for user account recovery.
[VALIDATION] IF alternate_factors_defined = FALSE THEN violation

[RULE-02] Systems SHALL allow use of alternate authentication factors after 5 consecutive invalid logon attempts using primary factors within a 15-minute period.
[VALIDATION] IF primary_invalid_attempts >= 5 AND time_window <= 15_minutes AND alternate_factors_enabled = FALSE THEN violation

[RULE-03] Organizations MUST enforce a limit of 3 consecutive invalid logon attempts for alternate authentication factors within a 30-minute period.
[VALIDATION] IF alternate_invalid_attempts > 3 AND time_window <= 30_minutes THEN lockout_required

[RULE-04] After exceeding alternate factor limits, accounts MUST be locked for a minimum of 30 minutes or require administrator intervention.
[VALIDATION] IF alternate_lockout_triggered = TRUE AND (lockout_duration < 30_minutes AND admin_unlock = FALSE) THEN violation

[RULE-05] All authentication attempts using primary and alternate factors MUST be logged with timestamps, user identity, factor type, and success/failure status.
[VALIDATION] IF authentication_event_logged = FALSE OR log_missing_required_fields = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Alternate Factor Enrollment - Process for users to register backup authentication methods
- [PROC-02] Account Lockout Recovery - Standardized process for unlocking accounts after alternate factor exhaustion
- [PROC-03] Authentication Monitoring - Continuous monitoring of authentication patterns and anomalies
- [PROC-04] Factor Lifecycle Management - Regular review and rotation of alternate authentication factors

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving authentication bypass, technology changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Lockout Recovery]
IF primary_invalid_attempts = 5
AND time_window <= 15_minutes
AND alternate_factors_available = TRUE
AND user_attempts_alternate = TRUE
THEN compliance = TRUE

[SCENARIO-02: Alternate Factor Abuse]
IF alternate_invalid_attempts > 3
AND time_window <= 30_minutes
AND account_locked = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Alternate Factors]
IF system_requires_authentication = TRUE
AND primary_lockout_threshold_defined = TRUE
AND alternate_factors_configured = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Insufficient Logging]
IF authentication_attempt_made = TRUE
AND (timestamp_logged = FALSE OR factor_type_logged = FALSE)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Excessive Lockout Duration]
IF alternate_lockout_triggered = TRUE
AND lockout_duration > 24_hours
AND admin_intervention_available = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Alternate authentication factors defined and different from primary | [RULE-01] |
| Alternate factors allowed after primary lockout threshold | [RULE-02] |
| Limits enforced on alternate factor attempts | [RULE-03] |
| Appropriate lockout duration after alternate factor exhaustion | [RULE-04] |
| Comprehensive logging of authentication events | [RULE-05] |