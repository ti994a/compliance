# POLICY: IA-5: Authenticator Management

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5 |
| NIST Control | IA-5: Authenticator Management |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authenticator, password, certificate, biometric, identity verification, credential management |

## 1. POLICY STATEMENT
The organization SHALL manage system authenticators throughout their lifecycle by verifying recipient identity, establishing secure content, implementing administrative procedures, and protecting authenticators from unauthorized disclosure. All authenticators MUST have sufficient strength for their intended use and be changed according to defined schedules or triggering events.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full-time, part-time, contractors |
| System accounts | YES | Service accounts, shared accounts, role accounts |
| All authenticator types | YES | Passwords, certificates, biometrics, tokens, badges |
| Cloud and on-premise systems | YES | Hybrid infrastructure coverage |
| Third-party integrations | YES | When using organizational authenticators |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity Management Team | • Verify recipient identity during initial distribution<br>• Establish authenticator content and strength requirements<br>• Implement administrative procedures for lifecycle management |
| System Administrators | • Change default authenticators before first use<br>• Configure authenticator refresh schedules<br>• Protect stored authenticator content |
| End Users | • Safeguard personal authenticators<br>• Report lost/compromised authenticators immediately<br>• Follow organizational protection requirements |

## 4. RULES
[RULE-01] Identity verification MUST be completed for all individuals, groups, roles, services, or devices before initial authenticator distribution.
[VALIDATION] IF authenticator_distributed = TRUE AND identity_verified = FALSE THEN violation

[RULE-02] Default authenticators MUST be changed prior to first system use.
[VALIDATION] IF system_first_use = TRUE AND default_authenticator_changed = FALSE THEN critical_violation

[RULE-03] Authenticators MUST be changed or refreshed according to defined time periods: passwords every 90 days, certificates before expiration, and biometric templates every 2 years.
[VALIDATION] IF authenticator_age > defined_refresh_period AND no_valid_exception THEN violation

[RULE-04] Authenticators MUST be immediately revoked upon triggering events including termination, role changes, compromise incidents, or device loss.
[VALIDATION] IF triggering_event_occurred = TRUE AND revocation_time > 4_hours THEN violation

[RULE-05] Authenticator content MUST be protected from unauthorized disclosure through encryption at rest and secure transmission.
[VALIDATION] IF authenticator_storage = "plaintext" OR transmission_encrypted = FALSE THEN critical_violation

[RULE-06] Group and role account authenticators MUST be changed within 24 hours when membership changes occur.
[VALIDATION] IF membership_change_date < current_date AND authenticator_unchanged > 24_hours THEN violation

[RULE-07] Lost, stolen, or compromised authenticators MUST be reported within 1 hour and disabled within 4 hours of discovery.
[VALIDATION] IF incident_reported = TRUE AND disable_time > 4_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Identity Verification Process - Multi-factor verification for authenticator recipients
- [PROC-02] Authenticator Strength Assessment - Evaluation criteria for authenticator mechanisms
- [PROC-03] Incident Response for Compromised Authenticators - Immediate response and recovery procedures
- [PROC-04] Automated Refresh Management - System-driven authenticator lifecycle management

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, regulatory changes, technology updates, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Default Password Usage]
IF system_deployment = "new"
AND default_credentials = "unchanged"
AND production_access = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Expired Certificate Authentication]
IF authenticator_type = "certificate"
AND expiration_date < current_date
AND authentication_attempted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Shared Account Member Departure]
IF account_type = "shared_role"
AND member_departure_date < (current_date - 1_day)
AND authenticator_changed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unencrypted Password Storage]
IF password_storage_method = "plaintext"
AND system_classification >= "moderate"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Delayed Compromise Response]
IF authenticator_compromise_reported = TRUE
AND response_time > 4_hours
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Verify identity during initial distribution | [RULE-01] |
| Establish initial authenticator content | [RULE-01], [RULE-02] |
| Ensure sufficient strength of mechanism | [RULE-03] |
| Implement administrative procedures | [RULE-04], [RULE-07] |
| Change default authenticators before use | [RULE-02] |
| Change/refresh based on time periods or events | [RULE-03], [RULE-04] |
| Protect from unauthorized disclosure/modification | [RULE-05] |
| Require individual/device protection controls | [RULE-07] |
| Change group/role authenticators on membership changes | [RULE-06] |