# POLICY: PT-4.1: Tailored Consent

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-4.1 |
| NIST Control | PT-4.1: Tailored Consent |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | tailored consent, PII processing, individual choice, granular permissions, privacy controls |

## 1. POLICY STATEMENT
The organization SHALL provide tailoring mechanisms that allow individuals to selectively control processing permissions for specific elements of their personally identifiable information (PII). These mechanisms MUST enable granular consent choices beyond basic functionality requirements to reduce privacy risk and increase individual satisfaction.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes web applications, mobile apps, APIs |
| Cloud services handling PII | YES | Both company-operated and third-party |
| Employee PII systems | CONDITIONAL | Where processing beyond basic HR functions occurs |
| Marketing platforms | YES | All customer data collection and processing |
| Analytics systems | YES | Where individual PII elements are processed |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define tailored consent requirements<br>• Approve consent mechanisms<br>• Monitor compliance with tailoring policies |
| Product Managers | • Identify PII elements requiring tailored consent<br>• Design user-friendly consent interfaces<br>• Document processing purposes for each PII element |
| Engineering Teams | • Implement granular consent mechanisms<br>• Ensure consent choices are technically enforced<br>• Maintain audit logs of consent selections |
| Legal Team | • Review consent mechanisms for regulatory compliance<br>• Define minimum processing requirements<br>• Validate consent language and presentation |

## 4. RULES

[RULE-01] Systems MUST provide tailoring mechanisms that allow individuals to grant or deny processing permissions for each distinct PII element that is not essential for basic service functionality.
[VALIDATION] IF system_processes_PII = TRUE AND tailoring_mechanism_exists = FALSE AND non_essential_processing = TRUE THEN violation

[RULE-02] Tailored consent interfaces MUST clearly distinguish between PII processing that is required for basic functionality versus optional processing.
[VALIDATION] IF consent_interface_deployed = TRUE AND required_vs_optional_distinction = FALSE THEN violation

[RULE-03] Organizations SHALL honor individual tailoring choices and MUST NOT process PII elements for which consent has been denied or withdrawn.
[VALIDATION] IF individual_consent_denied = TRUE AND processing_continues = TRUE THEN critical_violation

[RULE-04] Tailoring mechanisms MUST allow individuals to modify their consent choices at any time through an accessible interface.
[VALIDATION] IF consent_modification_available = FALSE OR modification_interface_accessible = FALSE THEN violation

[RULE-05] Systems SHALL maintain auditable records of all tailored consent decisions and modifications for each individual.
[VALIDATION] IF consent_decision_logged = FALSE OR audit_trail_incomplete = TRUE THEN violation

[RULE-06] Default settings for tailored consent MUST be privacy-protective and SHALL NOT pre-select optional processing permissions.
[VALIDATION] IF default_consent_settings = "opt_in" AND optional_processing_preselected = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Element Classification - Categorize all PII elements as essential or optional for service functionality
- [PROC-02] Consent Interface Design - Develop user-friendly mechanisms for granular consent selection
- [PROC-03] Consent Enforcement - Implement technical controls to honor individual tailoring choices
- [PROC-04] Consent Audit Logging - Maintain comprehensive records of consent decisions and changes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, regulatory changes, privacy incidents, user interface modifications

## 7. SCENARIO PATTERNS

[SCENARIO-01: Marketing Email Preferences]
IF system = "marketing_platform"
AND PII_element = "email_address"
AND processing_purpose = "promotional_emails"
AND individual_consent = "denied"
AND emails_sent = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Analytics Data Collection]
IF system = "web_analytics"
AND PII_elements = ["location", "browsing_behavior"]
AND essential_for_service = FALSE
AND tailoring_mechanism_provided = TRUE
AND individual_choice_honored = TRUE
THEN compliance = TRUE

[SCENARIO-03: Required vs Optional Processing]
IF consent_interface_displayed = TRUE
AND required_processing_marked = "optional"
AND service_functionality_impacted = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Consent Modification Request]
IF individual_requests_consent_change = TRUE
AND modification_interface_available = FALSE
AND processing_continues_unchanged = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Default Consent Settings]
IF new_user_registration = TRUE
AND optional_processing_preselected = TRUE
AND user_action_required = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Tailoring mechanisms for PII processing permissions are defined | [RULE-01], [RULE-02] |
| Mechanisms allow individuals to tailor processing permissions to selected PII elements | [RULE-01], [RULE-04] |
| Individual consent choices are technically enforced | [RULE-03], [RULE-05] |
| Privacy-protective defaults are implemented | [RULE-06] |