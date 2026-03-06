```markdown
# POLICY: AC-7.3: Biometric Attempt Limiting

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-7.3 |
| NIST Control | AC-7.3: Biometric Attempt Limiting |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | biometric, authentication, logon attempts, access control, probabilistic authentication |

## 1. POLICY STATEMENT
Organizations must limit the number of unsuccessful biometric logon attempts to prevent unauthorized access while accounting for the probabilistic nature of biometric authentication. Biometric attempt limits shall be based on organizationally-defined factors including matching performance and presentation attack detection capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Biometric authentication systems | YES | All systems using fingerprint, facial, iris, or voice recognition |
| Multi-factor authentication with biometric component | YES | When biometrics are primary or secondary factor |
| Physical access control systems | YES | Biometric door locks, turnstiles, secure areas |
| Logical access control systems | YES | Workstation login, application access, privileged accounts |
| Third-party biometric services | YES | Cloud-based biometric authentication providers |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve biometric attempt limit policies<br>• Review biometric security incidents<br>• Ensure compliance with regulatory requirements |
| System Administrators | • Configure biometric attempt limits per policy<br>• Monitor biometric authentication logs<br>• Implement lockout and recovery procedures |
| Security Operations | • Monitor biometric authentication failures<br>• Investigate suspicious biometric activity<br>• Coordinate incident response for biometric bypasses |

## 4. RULES

[RULE-01] Biometric authentication systems MUST limit unsuccessful logon attempts to a maximum of 5 attempts within a 15-minute window for standard user accounts.
[VALIDATION] IF unsuccessful_biometric_attempts > 5 AND time_window <= 15_minutes THEN account_lockout_required

[RULE-02] Privileged accounts using biometric authentication MUST be limited to 3 unsuccessful attempts within a 10-minute window before account lockout.
[VALIDATION] IF account_type = "privileged" AND unsuccessful_biometric_attempts > 3 AND time_window <= 10_minutes THEN immediate_lockout_required

[RULE-03] Biometric attempt limits MUST account for false rejection rates and SHALL NOT be set below 3 attempts to ensure legitimate user access.
[VALIDATION] IF biometric_attempt_limit < 3 THEN policy_violation

[RULE-04] Account lockout duration after exceeding biometric attempt limits MUST be at least 30 minutes for standard accounts and 60 minutes for privileged accounts.
[VALIDATION] IF lockout_duration < 30_minutes AND account_type = "standard" THEN policy_violation
[VALIDATION] IF lockout_duration < 60_minutes AND account_type = "privileged" THEN policy_violation

[RULE-05] Biometric systems MUST log all authentication attempts including successful authentications, failed attempts, and lockout events with timestamp and user identification.
[VALIDATION] IF biometric_logging = FALSE OR log_details_incomplete = TRUE THEN audit_violation

[RULE-06] Alternative authentication methods MUST be available when biometric attempt limits are exceeded, requiring additional verification for privileged accounts.
[VALIDATION] IF biometric_locked = TRUE AND alternative_auth_available = FALSE THEN availability_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Biometric Attempt Limit Configuration - Establish and document appropriate attempt limits based on system risk level and user population
- [PROC-02] Biometric Account Recovery - Define process for unlocking accounts after biometric attempt limit exceeded
- [PROC-03] Biometric Performance Monitoring - Regular review of false acceptance/rejection rates to optimize attempt limits
- [PROC-04] Biometric Incident Response - Procedures for investigating potential biometric spoofing or bypass attempts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Biometric security incidents, technology changes, regulatory updates, significant false rejection rate changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard User Biometric Lockout]
IF user_type = "standard"
AND unsuccessful_biometric_attempts = 6
AND time_window = "10_minutes"
AND account_locked = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Privileged Account Protection]
IF account_type = "privileged"
AND unsuccessful_biometric_attempts = 3
AND time_window = "8_minutes"
AND account_locked = TRUE
AND lockout_duration = "60_minutes"
THEN compliance = TRUE

[SCENARIO-03: Insufficient Attempt Limit]
IF biometric_attempt_limit = 2
AND system_type = "any"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Alternative Authentication]
IF biometric_locked = TRUE
AND alternative_auth_method = "none"
AND user_access_required = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Incomplete Logging]
IF biometric_authentication_event = TRUE
AND event_logged = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Limit unsuccessful biometric logon attempts | RULE-01, RULE-02 |
| Account for biometric probabilistic nature | RULE-03 |
| Implement appropriate lockout duration | RULE-04 |
| Maintain audit trail of biometric events | RULE-05 |
| Ensure availability through alternative methods | RULE-06 |
```