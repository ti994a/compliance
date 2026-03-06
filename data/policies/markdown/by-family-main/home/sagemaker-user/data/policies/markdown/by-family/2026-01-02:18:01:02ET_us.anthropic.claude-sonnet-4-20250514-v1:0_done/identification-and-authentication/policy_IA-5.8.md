# POLICY: IA-5.8: Multiple System Accounts

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5.8 |
| NIST Control | IA-5.8: Multiple System Accounts |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | multiple accounts, authenticators, passwords, single sign-on, federation, compromise risk |

## 1. POLICY STATEMENT
The organization SHALL implement security controls to manage the risk of compromise when individuals maintain accounts on multiple systems. These controls prevent credential reuse vulnerabilities and limit the impact of account compromises across systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, contractors |
| Service accounts | YES | When used across multiple systems |
| Privileged accounts | YES | Enhanced controls required |
| Guest/temporary accounts | YES | Limited duration controls |
| External federated users | CONDITIONAL | When accessing internal systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity and Access Management Team | • Implement and maintain authentication controls<br>• Monitor cross-system account usage<br>• Enforce password differentiation policies |
| System Administrators | • Configure system-specific authentication requirements<br>• Implement SSO/federation where approved<br>• Report authentication anomalies |
| Security Operations Center | • Monitor for credential compromise indicators<br>• Investigate suspicious cross-system access<br>• Coordinate incident response for account compromises |

## 4. RULES

[RULE-01] Users with accounts on multiple systems MUST NOT use identical passwords across different systems unless using approved single sign-on or federation mechanisms.
[VALIDATION] IF user_has_multiple_accounts = TRUE AND password_reuse_detected = TRUE AND sso_enabled = FALSE THEN violation

[RULE-02] Organizations MUST implement at least one of the following controls for users with multiple system accounts: unique passwords per system, approved SSO/federation, or multi-factor authentication on all systems.
[VALIDATION] IF multiple_accounts = TRUE AND (unique_passwords = FALSE AND sso_federation = FALSE AND mfa_all_systems = FALSE) THEN violation

[RULE-03] Users with privileged accounts on multiple systems MUST use unique authenticators and enable multi-factor authentication on all privileged accounts.
[VALIDATION] IF account_type = "privileged" AND multiple_systems = TRUE AND (unique_auth = FALSE OR mfa_enabled = FALSE) THEN critical_violation

[RULE-04] Single sign-on and federation mechanisms MUST be approved by the security team and meet organizational security standards before deployment.
[VALIDATION] IF sso_federation_deployed = TRUE AND security_approval = FALSE THEN violation

[RULE-05] Account compromise incidents involving users with multiple system accounts MUST trigger immediate review and potential credential reset across all associated systems within 4 hours.
[VALIDATION] IF compromise_detected = TRUE AND multiple_accounts = TRUE AND response_time > 4_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Multi-System Account Risk Assessment - Annual review of users with multiple accounts and associated risks
- [PROC-02] Password Differentiation Enforcement - Technical controls to prevent password reuse across systems
- [PROC-03] SSO/Federation Security Review - Security assessment process for authentication federation solutions
- [PROC-04] Cross-System Compromise Response - Incident response procedures for multi-account compromises

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving multiple accounts, new authentication technologies, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Password Reuse Detection]
IF user_has_accounts_on_systems > 1
AND password_hash_match = TRUE
AND sso_enabled = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Privileged Account Without MFA]
IF account_type = "privileged"
AND system_count > 1
AND mfa_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Approved SSO Implementation]
IF sso_solution_deployed = TRUE
AND security_team_approval = TRUE
AND meets_security_standards = TRUE
THEN compliance = TRUE

[SCENARIO-04: Delayed Compromise Response]
IF account_compromise_detected = TRUE
AND affected_systems > 1
AND response_initiated_hours > 4
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Contractor Multiple Account Access]
IF user_type = "contractor"
AND active_systems > 2
AND unique_passwords = TRUE
AND business_justification = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security controls for multiple system accounts are defined | RULE-02 |
| Controls implemented to manage compromise risk | RULE-01, RULE-03 |
| Authenticator management for multiple accounts | RULE-01, RULE-04 |
| Risk mitigation for cross-system access | RULE-05 |