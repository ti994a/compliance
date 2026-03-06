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
All personnel must comply with established rules of behavior that restrict the use of social media, social networking sites, and external applications when conducting official business or handling organizational information. These restrictions include prohibitions on posting organizational information publicly and using company-provided credentials for personal external accounts.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, temporary |
| Contractors | YES | When accessing organizational systems |
| Third-party vendors | YES | When handling organizational data |
| Personal devices | CONDITIONAL | Only when accessing company resources |
| Company-owned devices | YES | All usage scenarios |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish social media usage restrictions<br>• Review and approve rules of behavior<br>• Monitor compliance violations |
| HR Manager | • Ensure all personnel acknowledge rules of behavior<br>• Conduct awareness training<br>• Document policy violations |
| IT Security Team | • Monitor for unauthorized credential usage<br>• Implement technical controls<br>• Investigate security incidents |

## 4. RULES

[RULE-01] All personnel MUST acknowledge and comply with rules of behavior that explicitly restrict social media and external site usage for official business.
[VALIDATION] IF personnel_status = "active" AND rules_of_behavior_acknowledged = FALSE THEN violation

[RULE-02] Personnel MUST NOT post organizational information, including non-public data and personally identifiable information, on public websites or social media platforms.
[VALIDATION] IF organizational_info_posted = TRUE AND platform_type = "public" THEN critical_violation

[RULE-03] Personnel MUST NOT use organization-provided email addresses to create accounts on external sites or applications for personal use.
[VALIDATION] IF account_creation = TRUE AND email_domain = "company_domain" AND purpose = "personal" THEN violation

[RULE-04] Personnel MUST NOT use organization-provided authentication secrets (passwords, tokens) for external site accounts under any circumstances.
[VALIDATION] IF external_account = TRUE AND auth_secret_source = "organizational" THEN critical_violation

[RULE-05] Personnel MUST report any inadvertent disclosure of organizational information on social media or external sites within 24 hours of discovery.
[VALIDATION] IF incident_discovered = TRUE AND report_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Social Media Incident Response - Process for handling unauthorized information disclosure
- [PROC-02] Rules of Behavior Acknowledgment - Annual certification and training requirements
- [PROC-03] External Account Monitoring - Automated scanning for organizational credential misuse
- [PROC-04] Public Information Review - Pre-publication approval for official social media posts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, regulatory changes, new social media platforms

## 7. SCENARIO PATTERNS

[SCENARIO-01: Employee Personal Social Media]
IF employee_posts_content = TRUE
AND content_contains_org_info = TRUE
AND platform_type = "public_social_media"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Using Company Email]
IF user_type = "contractor"
AND external_account_created = TRUE
AND email_used = "company_domain"
AND account_purpose = "personal"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Password Reuse on External Site]
IF organizational_password = TRUE
AND external_site_account = TRUE
AND password_reused = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Approved Official Social Media]
IF post_type = "official_business"
AND pre_approval_obtained = TRUE
AND content_reviewed = TRUE
AND platform_approved = TRUE
THEN compliance = TRUE

[SCENARIO-05: Delayed Incident Reporting]
IF org_info_disclosed = TRUE
AND discovery_date = "known"
AND report_submitted = TRUE
AND reporting_delay > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Rules of behavior include social media restrictions | [RULE-01] |
| Restrictions on posting organizational information | [RULE-02] |
| Restrictions on using organizational identifiers | [RULE-03] |
| Restrictions on using authentication secrets | [RULE-04] |
| Incident reporting requirements | [RULE-05] |