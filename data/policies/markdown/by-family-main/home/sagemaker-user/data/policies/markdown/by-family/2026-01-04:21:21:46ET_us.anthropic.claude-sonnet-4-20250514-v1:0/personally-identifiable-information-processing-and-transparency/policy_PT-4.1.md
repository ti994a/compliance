# POLICY: PT-4.1: Tailored Consent

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-4.1 |
| NIST Control | PT-4.1: Tailored Consent |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | tailored consent, PII processing, granular permissions, individual choice, privacy controls |

## 1. POLICY STATEMENT
The organization SHALL provide tailoring mechanisms that allow individuals to select how specific personally identifiable information (PII) elements may be processed beyond basic functionality requirements. These mechanisms enable granular control over PII processing permissions to reduce privacy risk and increase individual satisfaction.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Applies to optional PII processing beyond basic functionality |
| Third-party services collecting PII | YES | Must implement tailored consent mechanisms |
| Internal HR systems | CONDITIONAL | Only for optional processing beyond employment requirements |
| Public-facing applications | YES | All consumer and external user interfaces |
| API endpoints processing PII | YES | Must support granular consent validation |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define tailoring mechanisms and granular consent requirements<br>• Approve PII processing categorization (essential vs. optional)<br>• Review consent interface designs |
| Product Managers | • Identify optional PII processing activities<br>• Implement user-friendly consent interfaces<br>• Ensure consent mechanisms are accessible |
| Engineering Teams | • Build granular consent collection and validation systems<br>• Implement consent preference storage and retrieval<br>• Ensure consent choices are honored in processing |

## 4. RULES
[RULE-01] Systems MUST categorize PII processing into essential (required for basic functionality) and optional (enhancing but not required for service delivery) categories.
[VALIDATION] IF pii_processing_activity = "undefined_category" THEN violation

[RULE-02] For optional PII processing, systems MUST provide granular consent mechanisms allowing individuals to select specific PII elements they consent to process.
[VALIDATION] IF processing_type = "optional" AND granular_consent_available = FALSE THEN violation

[RULE-03] Consent interfaces MUST clearly distinguish between essential and optional PII processing with separate consent controls for each optional processing purpose.
[VALIDATION] IF consent_interface_separates_essential_optional = FALSE THEN violation

[RULE-04] Systems MUST honor individual tailored consent choices and SHALL NOT process PII elements for purposes where consent was not granted.
[VALIDATION] IF consent_granted = FALSE AND processing_occurred = TRUE THEN critical_violation

[RULE-05] Tailored consent preferences MUST be stored securely and remain accessible to individuals for review and modification at any time.
[VALIDATION] IF consent_preferences_modifiable = FALSE OR consent_preferences_viewable = FALSE THEN violation

[RULE-06] Default consent settings for optional processing MUST be set to "opt-in" rather than "opt-out" to ensure explicit individual choice.
[VALIDATION] IF optional_processing_default = "opt-out" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Processing Categorization - Systematic review and classification of all PII processing activities
- [PROC-02] Consent Interface Design - Development and testing of user-friendly granular consent mechanisms
- [PROC-03] Consent Validation - Real-time checking of consent status before PII processing
- [PROC-04] Consent Preference Management - Secure storage, retrieval, and modification of individual consent choices

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, privacy incidents, regulatory changes, user interface modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Marketing Email Consent]
IF user_registers_for_service = TRUE
AND marketing_email_processing = "optional"
AND granular_consent_for_marketing = provided
THEN compliance = TRUE

[SCENARIO-02: Analytics Processing Without Consent]
IF user_opts_out_analytics = TRUE
AND behavioral_data_processing = "optional"
AND analytics_processing_continues = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Essential vs Optional Processing]
IF account_creation_requires_email = TRUE
AND promotional_email_consent = "separate_choice"
AND user_can_decline_promotional = TRUE
THEN compliance = TRUE

[SCENARIO-04: Bundled Consent Violation]
IF multiple_optional_processing_purposes = TRUE
AND single_consent_checkbox = TRUE
AND granular_choices_unavailable = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Consent Modification Access]
IF user_requests_consent_changes = TRUE
AND consent_modification_mechanism = "unavailable"
AND user_cannot_update_preferences = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Tailoring mechanisms for processing selected PII elements are defined | [RULE-01], [RULE-02] |
| Mechanisms allow individuals to tailor processing permissions | [RULE-03], [RULE-05] |
| Selected elements of PII have granular consent controls | [RULE-02], [RULE-06] |
| Processing permissions respect individual choices | [RULE-04] |