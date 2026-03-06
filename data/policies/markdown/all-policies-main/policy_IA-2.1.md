```markdown
POLICY: IA-2.1: Multi-factor Authentication to Privileged Accounts

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-2.1 |
| NIST Control | IA-2.1: Multi-factor Authentication to Privileged Accounts |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | multi-factor authentication, MFA, privileged accounts, authentication factors, PIV, CAC, biometric |

1. POLICY STATEMENT
All privileged accounts MUST implement multi-factor authentication using at least two different authentication factors (something you know, something you have, or something you are). This requirement applies to all access types including local, network, and remote access to privileged accounts.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Privileged user accounts | YES | All accounts with elevated system privileges |
| Administrative accounts | YES | Including domain admins, system admins, database admins |
| Service accounts with privileges | YES | When interactive logon is possible |
| Standard user accounts | NO | Covered under base IA-2 control |
| Emergency/break-glass accounts | CONDITIONAL | Must have compensating controls if MFA unavailable |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure MFA for all privileged accounts<br>• Monitor MFA compliance and failures<br>• Maintain approved authenticator inventory |
| Account Managers | • Provision MFA tokens during account creation<br>• Revoke MFA access during account termination<br>• Document MFA exemptions with justification |
| Security Team | • Define approved MFA technologies and factors<br>• Audit MFA implementation compliance<br>• Investigate MFA bypass attempts |

4. RULES
[RULE-01] Privileged accounts MUST implement multi-factor authentication using at least two different authentication factors from: something you know (PIN/password), something you have (hardware token/smart card), or something you are (biometric).
[VALIDATION] IF account_type = "privileged" AND mfa_factors_count < 2 THEN violation

[RULE-02] Hardware authenticators SHALL be preferred for privileged access and MUST include time-based tokens, challenge-response devices, PIV cards, or CAC cards.
[VALIDATION] IF account_type = "privileged" AND authenticator_type = "software_only" AND hardware_exemption = FALSE THEN violation

[RULE-03] Multi-factor authentication MUST be enforced for ALL access types to privileged accounts including local logon, network access, and remote access.
[VALIDATION] IF account_type = "privileged" AND access_type IN ["local", "network", "remote"] AND mfa_enforced = FALSE THEN critical_violation

[RULE-04] MFA bypass or exemptions for privileged accounts MUST be documented with business justification and approved by the CISO or designated authority.
[VALIDATION] IF account_type = "privileged" AND mfa_bypass = TRUE AND documented_exemption = FALSE THEN violation

[RULE-05] Failed MFA attempts for privileged accounts MUST be logged and monitored with alerts generated after 3 consecutive failures within 15 minutes.
[VALIDATION] IF account_type = "privileged" AND failed_mfa_attempts >= 3 AND time_window <= 15_minutes AND alert_generated = FALSE THEN violation

5. REQUIRED PROCEDURES
- [PROC-01] Privileged Account MFA Enrollment - Process for provisioning and configuring MFA for new privileged accounts
- [PROC-02] MFA Token Management - Procedures for issuing, replacing, and revoking hardware authentication tokens
- [PROC-03] MFA Failure Response - Incident response procedures for MFA bypass attempts or systematic failures
- [PROC-04] Emergency Access Protocol - Documented process for emergency access when MFA is unavailable

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving privileged accounts, new authentication technologies, regulatory changes

7. SCENARIO PATTERNS
[SCENARIO-01: Domain Administrator Login]
IF account_type = "domain_administrator"
AND authentication_factors = 1
AND access_type = "remote"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Service Account with Interactive Logon]
IF account_type = "service_account"
AND interactive_logon_enabled = TRUE
AND privileged_access = TRUE
AND mfa_configured = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Emergency Access with Documentation]
IF account_type = "privileged"
AND mfa_bypass = TRUE
AND emergency_access = TRUE
AND ciso_approval = TRUE
AND incident_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: PIV Card Authentication]
IF account_type = "privileged"
AND authenticator_type = "PIV_card"
AND pin_required = TRUE
AND certificate_valid = TRUE
THEN compliance = TRUE

[SCENARIO-05: Repeated MFA Failures]
IF account_type = "privileged"
AND failed_mfa_attempts = 5
AND time_window = "10_minutes"
AND security_alert = FALSE
THEN compliance = FALSE
violation_severity = "High"

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Multi-factor authentication implemented for privileged accounts | [RULE-01], [RULE-03] |
| Hardware authenticators for high-risk access | [RULE-02] |
| Comprehensive access coverage (local/network/remote) | [RULE-03] |
| Documented exemption process | [RULE-04] |
| Security monitoring and alerting | [RULE-05] |
```