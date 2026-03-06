# POLICY: IA-4.1: Prohibit Account Identifiers as Public Identifiers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-4.1 |
| NIST Control | IA-4.1: Prohibit Account Identifiers as Public Identifiers |
| Version | 1.0 |
| Owner | Identity and Access Management Team |
| Keywords | account identifiers, public identifiers, email addresses, usernames, privacy protection |

## 1. POLICY STATEMENT
The organization prohibits the use of system account identifiers that are identical to publicly disclosed identifiers for individual user accounts. This requirement protects against account enumeration attacks and reduces the risk of targeted credential attacks by making user identifiers less predictable.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All system user accounts | YES | Individual user accounts across all systems |
| Service accounts | NO | Technical accounts for system-to-system communication |
| Shared accounts | YES | When used by individuals |
| External contractor accounts | YES | Same requirements as employee accounts |
| Guest/temporary accounts | YES | All individual access accounts |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity and Access Management Team | • Enforce account identifier standards<br>• Review and approve identifier formats<br>• Monitor compliance with identifier policies |
| System Administrators | • Configure systems to enforce identifier requirements<br>• Validate account creation processes<br>• Report identifier policy violations |
| Security Team | • Audit account identifier compliance<br>• Investigate potential identifier-based attacks<br>• Update identifier security requirements |

## 4. RULES
[RULE-01] System account identifiers MUST NOT be identical to publicly disclosed identifiers such as email addresses, social media handles, or other public communication identifiers.
[VALIDATION] IF account_identifier = public_identifier THEN violation

[RULE-02] Account creation processes MUST validate that proposed identifiers do not match known public identifiers for the same individual.
[VALIDATION] IF new_account_request AND identifier_matches_public = TRUE THEN creation_blocked

[RULE-03] Existing accounts with identifiers matching public identifiers MUST be remediated within 30 days of policy implementation or discovery.
[VALIDATION] IF account_age > policy_effective_date AND identifier_matches_public = TRUE AND remediation_time > 30_days THEN violation

[RULE-04] Automated account provisioning systems MUST include controls to prevent creation of accounts with public identifier formats.
[VALIDATION] IF provisioning_system AND public_identifier_check = FALSE THEN configuration_violation

[RULE-05] Account identifier compliance MUST be reviewed quarterly through automated scanning and manual verification processes.
[VALIDATION] IF last_compliance_review > 90_days THEN review_required

## 5. REQUIRED PROCEDURES
- [PROC-01] Account Identifier Validation - Process for validating new account identifiers against public identifier databases
- [PROC-02] Public Identifier Discovery - Procedure for identifying employee public identifiers through OSINT and HR data
- [PROC-03] Account Remediation - Process for updating non-compliant account identifiers with minimal business disruption
- [PROC-04] Compliance Monitoring - Automated and manual processes for ongoing identifier compliance verification

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving account enumeration, new system implementations, significant organizational changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Email-Based Account Creation]
IF account_identifier = "john.smith"
AND employee_email = "john.smith@company.com"
AND email_publicly_disclosed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Social Media Handle Matching]
IF account_identifier = "jsmith_tech"
AND employee_social_media_handle = "jsmith_tech"
AND social_media_profile_public = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Compliant Unique Identifier]
IF account_identifier = "js47291"
AND identifier_format = "randomized"
AND public_identifier_match = FALSE
THEN compliance = TRUE

[SCENARIO-04: Service Account Exception]
IF account_type = "service_account"
AND account_purpose = "system_integration"
AND individual_user = FALSE
THEN policy_applicable = FALSE

[SCENARIO-05: Legacy Account Remediation]
IF account_created_date < policy_effective_date
AND identifier_matches_public = TRUE
AND remediation_completed = FALSE
AND days_since_discovery > 30
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibition of matching public identifiers | [RULE-01] |
| Account creation validation controls | [RULE-02] |
| Remediation of non-compliant accounts | [RULE-03] |
| Automated provisioning controls | [RULE-04] |
| Regular compliance verification | [RULE-05] |