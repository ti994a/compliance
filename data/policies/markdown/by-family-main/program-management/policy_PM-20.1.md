# POLICY: PM-20.1: Privacy Policies on Websites, Applications, and Digital Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-20.1 |
| NIST Control | PM-20.1: Privacy Policies on Websites, Applications, and Digital Services |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy policy, external-facing websites, mobile applications, digital services, plain language, PII collection |

## 1. POLICY STATEMENT
All external-facing websites, mobile applications, and digital services MUST display privacy policies written in plain language that enable informed public decision-making. Privacy policies MUST be updated with timestamps whenever substantive changes occur to organizational privacy practices.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External-facing websites | YES | All public websites operated by organization |
| Mobile applications | YES | All organization-developed mobile apps |
| Digital services | YES | All public-facing digital platforms and services |
| Internal applications | NO | Only external-facing services require privacy policies |
| Third-party hosted services | CONDITIONAL | If organization controls content and collects PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Approve all privacy policy content<br>• Ensure compliance with legal requirements<br>• Coordinate policy updates across platforms |
| Web Development Teams | • Implement privacy policy links on all applicable platforms<br>• Ensure policies are accessible from PII collection points<br>• Maintain timestamp accuracy |
| Legal Counsel | • Review privacy policies for regulatory compliance<br>• Advise on substantive change determinations<br>• Validate plain language requirements |

## 4. RULES
[RULE-01] All external-facing websites, mobile applications, and digital services MUST display a privacy policy accessible from the main entry point.
[VALIDATION] IF platform_type IN ["external_website", "mobile_app", "digital_service"] AND privacy_policy_link = FALSE THEN violation

[RULE-02] Privacy policies MUST be written in plain language with reading level not exceeding 8th grade and organized with clear navigation structure.
[VALIDATION] IF privacy_policy_reading_level > 8 OR navigation_structure = "unclear" THEN violation

[RULE-03] Privacy policies MUST provide sufficient information for public to make informed decisions about interaction with the organization.
[VALIDATION] IF policy_completeness_score < 80 OR missing_required_elements = TRUE THEN violation

[RULE-04] Any webpage, application screen, or digital service interface that collects PII MUST provide a direct link to the relevant privacy policy.
[VALIDATION] IF pii_collection = TRUE AND privacy_policy_link = FALSE THEN violation

[RULE-05] Privacy policies MUST be updated within 30 days of any substantive change to privacy practices and include accurate timestamp of last modification.
[VALIDATION] IF substantive_change_date < (current_date - 30_days) AND policy_update = FALSE THEN violation

[RULE-06] Privacy policy timestamps MUST accurately reflect the date of the most recent substantive changes, not minor editorial updates.
[VALIDATION] IF timestamp_date != last_substantive_change_date THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privacy Policy Development - Standardized process for creating compliant privacy policies
- [PROC-02] Substantive Change Assessment - Methodology for determining when policy updates are required
- [PROC-03] Plain Language Review - Process for validating readability and comprehension standards
- [PROC-04] Cross-Platform Policy Deployment - Procedures for consistent policy implementation across all digital touchpoints

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: New digital service launch, substantive privacy practice changes, regulatory updates, legal counsel recommendations

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Mobile App Launch]
IF platform_type = "mobile_app"
AND launch_status = "production"
AND privacy_policy_present = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: PII Collection Without Policy Link]
IF pii_collection_present = TRUE
AND privacy_policy_link = FALSE
AND platform_accessibility = "external"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Outdated Policy After Practice Change]
IF substantive_privacy_change = TRUE
AND change_date = "45_days_ago"
AND policy_last_updated = "90_days_ago"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Complex Language Policy]
IF privacy_policy_reading_level = "12th_grade"
AND technical_jargon_present = TRUE
AND plain_language_review = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Missing Timestamp]
IF privacy_policy_present = TRUE
AND timestamp_visible = FALSE
AND last_update_date = "unknown"
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privacy policies developed and posted on external-facing websites | [RULE-01] |
| Privacy policies developed and posted on mobile applications | [RULE-01] |
| Privacy policies developed and posted on other digital services | [RULE-01] |
| Privacy policies written in plain language | [RULE-02] |
| Privacy policies organized for easy understanding and navigation | [RULE-02] |
| Privacy policies provide information for informed public decisions | [RULE-03] |
| Privacy policies updated when substantive changes occur | [RULE-05] |
| Privacy policies include timestamp of most recent changes | [RULE-06] |