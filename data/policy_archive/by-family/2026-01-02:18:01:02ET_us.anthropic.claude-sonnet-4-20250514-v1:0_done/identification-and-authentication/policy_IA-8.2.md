```markdown
# POLICY: IA-8.2: Acceptance of External Authenticators

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-8.2 |
| NIST Control | IA-8.2: Acceptance of External Authenticators |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external authenticators, NIST compliance, SP 800-63B, public systems, third-party credentials |

## 1. POLICY STATEMENT
The organization SHALL accept only NIST-compliant external authenticators for public-facing systems and maintain a documented list of approved external authenticators. All external authenticators must meet or exceed SP 800-63B requirements and Federal Government technical, security, privacy, and organizational maturity standards.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Public-facing systems | YES | Internet-accessible organizational systems |
| Internal systems | CONDITIONAL | Only if configured to accept external authenticators |
| Third-party authenticators | YES | All external authentication providers |
| Federal authenticators | NO | Covered under separate federal identity policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve external authenticator policy<br>• Review and approve external authenticator list<br>• Ensure compliance monitoring |
| Identity and Access Management Team | • Maintain approved external authenticator list<br>• Conduct NIST compliance assessments<br>• Configure system authentication settings |
| System Owners | • Implement approved external authenticators only<br>• Request additions to approved authenticator list<br>• Monitor authentication logs |

## 4. RULES
[RULE-01] Public-facing systems MUST accept only external authenticators that are documented on the approved external authenticator list.
[VALIDATION] IF system_type = "public-facing" AND external_authenticator NOT IN approved_list THEN violation

[RULE-02] All external authenticators MUST be verified as NIST SP 800-63B compliant before addition to the approved list.
[VALIDATION] IF external_authenticator.sp800_63b_compliant = FALSE THEN critical_violation

[RULE-03] The approved external authenticator list MUST be documented and maintained in the central identity management system.
[VALIDATION] IF approved_authenticator_list.last_updated > 90_days THEN violation

[RULE-04] External authenticators MUST meet or exceed Federal Government technical, security, privacy, and organizational maturity requirements.
[VALIDATION] IF external_authenticator.federal_requirements_met = FALSE THEN critical_violation

[RULE-05] Systems MUST NOT accept external authenticators that are not on the approved list, even if technically compatible.
[VALIDATION] IF system_accepts_unapproved_authenticator = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Authenticator Assessment - Evaluate NIST compliance and Federal requirements
- [PROC-02] Approved Authenticator List Management - Document, update, and distribute approved authenticators
- [PROC-03] System Configuration Validation - Verify systems only accept approved external authenticators
- [PROC-04] Authentication Monitoring - Monitor and audit external authentication events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New external authenticator requests, NIST guideline updates, security incidents involving external authentication

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved External Authenticator]
IF system_type = "public-facing"
AND external_authenticator_used = TRUE
AND authenticator NOT IN approved_list
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Non-NIST Compliant Authenticator]
IF external_authenticator.nist_compliant = FALSE
AND authenticator IN approved_list
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Outdated Authenticator List]
IF approved_authenticator_list.last_reviewed > 90_days
AND public_facing_systems_exist = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Internal System External Auth]
IF system_type = "internal"
AND external_authenticator_configured = TRUE
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper External Authentication]
IF system_type = "public-facing"
AND external_authenticator IN approved_list
AND authenticator.sp800_63b_compliant = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Only NIST-compliant external authenticators are accepted | [RULE-02], [RULE-04] |
| List of accepted external authenticators is documented | [RULE-03] |
| List of accepted external authenticators is maintained | [RULE-03] |
```