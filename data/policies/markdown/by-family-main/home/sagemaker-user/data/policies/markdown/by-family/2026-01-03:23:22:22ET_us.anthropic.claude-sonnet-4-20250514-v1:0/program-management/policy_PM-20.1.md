# POLICY: PM-20.1: Privacy Policies on Websites, Applications, and Digital Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-20.1 |
| NIST Control | PM-20.1: Privacy Policies on Websites, Applications, and Digital Services |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy policy, external-facing, websites, mobile applications, digital services, plain language, PII collection |

## 1. POLICY STATEMENT
The organization SHALL develop and post comprehensive privacy policies on all external-facing websites, mobile applications, and digital services written in plain language. These policies MUST provide sufficient information for users to make informed decisions about interactions and be updated with timestamps whenever substantive changes occur.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External-facing websites | YES | All public websites owned/operated by organization |
| Mobile applications | YES | All organization-developed mobile apps |
| Digital services | YES | All customer-facing digital platforms |
| Internal systems | NO | Internal-only systems excluded |
| Third-party hosted services | CONDITIONAL | If organization controls content/branding |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee privacy policy development and approval<br>• Ensure legal compliance and accuracy<br>• Coordinate policy updates |
| Web Development Teams | • Implement privacy policy links and placement<br>• Ensure technical accessibility requirements<br>• Maintain timestamp functionality |
| Legal Counsel | • Review policy content for legal compliance<br>• Advise on regulatory requirements<br>• Approve substantive changes |
| Content Management Teams | • Write policies in plain language<br>• Organize content for user comprehension<br>• Maintain version control |

## 4. RULES
[RULE-01] Privacy policies MUST be posted on all external-facing websites, mobile applications, and digital services before public launch.
[VALIDATION] IF service_type IN ["external_website", "mobile_app", "digital_service"] AND privacy_policy_posted = FALSE THEN critical_violation

[RULE-02] Privacy policy links MUST be prominently displayed on major entry points and all pages collecting personally identifiable information.
[VALIDATION] IF page_collects_PII = TRUE AND privacy_policy_link_present = FALSE THEN violation

[RULE-03] Privacy policies SHALL be written in plain language with reading level not exceeding 8th grade comprehension.
[VALIDATION] IF reading_level > 8th_grade OR plain_language_review = FALSE THEN violation

[RULE-04] Privacy policies MUST include sufficient information for users to make informed decisions about whether and how to interact with the organization.
[VALIDATION] IF required_elements_complete < 100% THEN violation

[RULE-05] Privacy policies SHALL be updated within 30 days of any substantive change to described practices and include accurate timestamps.
[VALIDATION] IF substantive_change_date + 30_days < current_date AND policy_updated = FALSE THEN violation

[RULE-06] All privacy policy updates MUST include visible date/time stamps indicating the most recent modification date.
[VALIDATION] IF policy_updated = TRUE AND timestamp_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privacy Policy Development - Standard process for creating compliant privacy policies
- [PROC-02] Plain Language Review - Methodology for ensuring readability and comprehension
- [PROC-03] Policy Update Management - Process for tracking and implementing policy changes
- [PROC-04] Link Placement Verification - Procedure for ensuring proper policy link placement
- [PROC-05] Timestamp Management - Technical procedure for maintaining accurate modification dates

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: New digital service launch, substantive practice changes, regulatory updates, user feedback indicating confusion

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Mobile App Launch]
IF service_type = "mobile_application"
AND launch_status = "ready"
AND privacy_policy_posted = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: PII Collection Page Missing Policy Link]
IF page_collects_PII = TRUE
AND privacy_policy_link_present = FALSE
AND page_type = "external_facing"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Policy After Practice Change]
IF substantive_practice_change = TRUE
AND change_date + 30_days < current_date
AND privacy_policy_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Policy Without Timestamp]
IF privacy_policy_exists = TRUE
AND last_modified_timestamp_visible = FALSE
AND policy_updated_within_year = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Complex Language Usage]
IF privacy_policy_reading_level > 8th_grade
AND plain_language_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privacy policies developed and posted on external-facing websites | [RULE-01] |
| Privacy policies developed and posted on mobile applications | [RULE-01] |
| Privacy policies developed and posted on other digital services | [RULE-01] |
| Privacy policies written in plain language | [RULE-03] |
| Privacy policies organized for easy understanding and navigation | [RULE-03] |
| Privacy policies provide information for informed decision-making (whether) | [RULE-04] |
| Privacy policies provide information for informed decision-making (how) | [RULE-04] |
| Privacy policies updated when substantive changes occur | [RULE-05] |
| Privacy policies include time/date stamps for recent changes | [RULE-06] |