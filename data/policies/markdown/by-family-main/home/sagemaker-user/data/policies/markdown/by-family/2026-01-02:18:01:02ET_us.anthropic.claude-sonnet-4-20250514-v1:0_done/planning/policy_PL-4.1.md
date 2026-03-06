# POLICY: PL-4.1: Social Media and External Site/Application Usage Restrictions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PL-4.1 |
| NIST Control | PL-4.1: Social Media and External Site/Application Usage Restrictions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | social media, external sites, rules of behavior, organizational identifiers, authentication secrets |

## 1. POLICY STATEMENT
All personnel must adhere to established rules of behavior that restrict social media and external site usage when conducting official business or handling organizational information. These restrictions protect organizational information from unauthorized disclosure and prevent misuse of organizational identifiers and authentication credentials on external platforms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, temporary |
| Contractors | YES | When accessing organizational systems |
| Third-party vendors | YES | When handling organizational information |
| Personal devices | CONDITIONAL | Only when used for organizational business |
| Organizational systems | YES | All company-owned IT resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish and maintain social media usage restrictions<br>• Review and approve rules of behavior<br>• Monitor compliance with external site restrictions |
| HR Department | • Ensure all personnel sign rules of behavior<br>• Conduct awareness training on social media restrictions<br>• Track compliance acknowledgments |
| IT Security Team | • Monitor for unauthorized use of organizational identifiers<br>• Implement technical controls for external site restrictions<br>• Investigate policy violations |
| All Personnel | • Comply with established rules of behavior<br>• Report suspected violations<br>• Complete required training |

## 4. RULES
[RULE-01] All personnel MUST sign and acknowledge rules of behavior that include restrictions on social media, social networking sites, and external site/application usage before system access is granted.
[VALIDATION] IF personnel_access_granted = TRUE AND rules_of_behavior_signed = FALSE THEN violation

[RULE-02] Personnel MUST NOT post organizational information, including non-public data, personally identifiable information, or system details, on public websites or social media platforms.
[VALIDATION] IF organizational_info_posted = TRUE AND platform_type = "public" THEN violation

[RULE-03] Personnel MUST NOT use organization-provided identifiers (email addresses, usernames) to create accounts on external sites/applications for personal use.
[VALIDATION] IF external_account_created = TRUE AND org_identifier_used = TRUE AND purpose = "personal" THEN violation

[RULE-04] Personnel MUST NOT use organizational authentication secrets (passwords, tokens) for creating or accessing accounts on external sites/applications.
[VALIDATION] IF external_account_access = TRUE AND org_credentials_used = TRUE THEN critical_violation

[RULE-05] Social media and external site usage for official business MUST be pre-approved through designated organizational channels and comply with information handling requirements.
[VALIDATION] IF official_business_usage = TRUE AND pre_approval_obtained = FALSE THEN violation

[RULE-06] Rules of behavior MUST be reviewed and re-acknowledged annually or when significant changes occur to social media policies.
[VALIDATION] IF last_acknowledgment_date > 365_days AND policy_changes = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Rules of Behavior Management - Establish, maintain, and distribute comprehensive rules of behavior
- [PROC-02] Social Media Monitoring - Monitor for unauthorized posting of organizational information
- [PROC-03] External Account Verification - Verify organizational identifiers are not used inappropriately
- [PROC-04] Violation Investigation - Investigate and respond to social media policy violations
- [PROC-05] Training and Awareness - Conduct regular training on social media restrictions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving social media, changes to organizational structure, new social media platforms, regulatory requirement changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Employee Personal Social Media Account]
IF employee_uses_work_email = TRUE
AND account_purpose = "personal"
AND platform_type = "social_media"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Contractor Posting Project Information]
IF user_type = "contractor"
AND organizational_info_posted = TRUE
AND platform_visibility = "public"
AND approval_obtained = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Approved Official Business Usage]
IF usage_purpose = "official_business"
AND pre_approval_obtained = TRUE
AND info_classification = "public"
AND designated_channel_used = TRUE
THEN compliance = TRUE

[SCENARIO-04: Password Reuse on External Site]
IF organizational_password_used = TRUE
AND external_site_account = TRUE
AND user_acknowledged_rules = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Unsigned Rules of Behavior]
IF system_access_granted = TRUE
AND rules_of_behavior_signed = FALSE
AND access_duration > 24_hours
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Rules of behavior include social media restrictions | RULE-01, RULE-05 |
| Rules of behavior include posting restrictions | RULE-02 |
| Rules of behavior include organizational identifier restrictions | RULE-03, RULE-04 |
| Annual acknowledgment process | RULE-06 |
| Monitoring and enforcement | RULE-02, RULE-03 |