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
All external-facing websites, mobile applications, and digital services MUST display privacy policies written in plain language that enable informed public decision-making. Privacy policies MUST be updated with timestamped changes whenever substantive practice modifications occur.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External-facing websites | YES | All public websites operated by organization |
| Mobile applications | YES | All mobile apps available to external users |
| Digital services | YES | All externally accessible digital platforms |
| Internal applications | NO | Employee-only systems excluded |
| Third-party hosted services | CONDITIONAL | If organization controls content/branding |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Approve all privacy policy content<br>• Ensure legal compliance<br>• Coordinate with legal counsel |
| Web Development Teams | • Implement privacy policy links<br>• Ensure proper placement on PII collection pages<br>• Maintain timestamp accuracy |
| Content Management Teams | • Write policies in plain language<br>• Update content for substantive changes<br>• Organize information for easy navigation |

## 4. RULES
[RULE-01] All external-facing websites, mobile applications, and digital services MUST display a privacy policy accessible from major entry points.
[VALIDATION] IF external_service = TRUE AND privacy_policy_posted = FALSE THEN critical_violation

[RULE-02] Privacy policies MUST be written in plain language and organized for easy understanding and navigation.
[VALIDATION] IF privacy_policy_exists = TRUE AND plain_language_review = FALSE THEN violation

[RULE-03] Privacy policies MUST provide sufficient information for the public to make informed decisions about interaction with the organization.
[VALIDATION] IF privacy_policy_exists = TRUE AND informed_decision_elements < required_elements THEN violation

[RULE-04] Privacy policy links MUST be placed on any webpage, application screen, or digital service interface that collects personally identifiable information.
[VALIDATION] IF pii_collection = TRUE AND privacy_policy_link = FALSE THEN violation

[RULE-05] Privacy policies MUST be updated within 30 days whenever the organization makes substantive changes to described practices.
[VALIDATION] IF substantive_change_date > policy_update_date + 30_days THEN violation

[RULE-06] All privacy policy updates MUST include a timestamp indicating the date of the most recent changes.
[VALIDATION] IF policy_updated = TRUE AND timestamp_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privacy Policy Development - Standard process for creating compliant privacy policies
- [PROC-02] Plain Language Review - Assessment methodology for readability and comprehension
- [PROC-03] Substantive Change Assessment - Criteria for determining when policy updates are required
- [PROC-04] Link Placement Verification - Quality assurance for proper privacy policy positioning
- [PROC-05] Timestamp Management - Process for maintaining accurate change dates

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: New digital service launch, substantive practice changes, regulatory updates, legal counsel recommendations

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Mobile App Launch]
IF service_type = "mobile_application"
AND external_facing = TRUE
AND privacy_policy_posted = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: PII Collection Without Policy Link]
IF pii_collection = TRUE
AND privacy_policy_link_present = FALSE
AND page_type = "data_entry"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Policy After Practice Change]
IF substantive_change_implemented = TRUE
AND days_since_change > 30
AND privacy_policy_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Policy Without Timestamp]
IF privacy_policy_exists = TRUE
AND recent_updates = TRUE
AND timestamp_visible = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Third-Party Service with Organization Branding]
IF service_hosted_by = "third_party"
AND organization_branding = TRUE
AND content_control = TRUE
AND privacy_policy_posted = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privacy policies developed and posted on external-facing websites | [RULE-01] |
| Privacy policies developed and posted on mobile applications | [RULE-01] |
| Privacy policies developed and posted on other digital services | [RULE-01] |
| Privacy policies written in plain language | [RULE-02] |
| Privacy policies organized for easy understanding and navigation | [RULE-02] |
| Privacy policies provide information for informed interaction decisions | [RULE-03] |
| Privacy policies updated for substantive practice changes | [RULE-05] |
| Privacy policies include timestamp for recent changes | [RULE-06] |
| Privacy policy links on PII collection pages | [RULE-04] |