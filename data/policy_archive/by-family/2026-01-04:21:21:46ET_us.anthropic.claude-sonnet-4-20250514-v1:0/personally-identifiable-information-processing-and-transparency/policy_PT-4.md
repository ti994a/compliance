# POLICY: PT-4: Consent

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-4 |
| NIST Control | PT-4: Consent |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | consent, PII processing, informed decision-making, opt-in, opt-out, revocation |

## 1. POLICY STATEMENT
The organization SHALL implement tools and mechanisms that enable individuals to provide informed consent prior to the collection and processing of their personally identifiable information (PII). Consent mechanisms MUST facilitate individuals' understanding of privacy risks and provide clear options for authorization or denial of PII processing.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Including cloud and hybrid environments |
| Customer-facing applications | YES | Direct consent collection points |
| Employee PII systems | CONDITIONAL | Where consent is legally required |
| Third-party data processors | YES | Must comply with consent requirements |
| Marketing systems | YES | Explicit consent required for processing |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define consent policy requirements<br>• Approve consent mechanisms<br>• Monitor compliance with consent obligations |
| Product Managers | • Implement consent interfaces in applications<br>• Ensure consent collection prior to PII processing<br>• Design user-friendly consent experiences |
| Legal Team | • Review consent language for legal compliance<br>• Assess regulatory consent requirements<br>• Validate consent mechanism adequacy |
| Engineering Teams | • Develop and maintain consent management systems<br>• Implement consent validation controls<br>• Enable consent revocation capabilities |

## 4. RULES
[RULE-01] Organizations MUST obtain explicit consent from individuals before collecting or processing their PII, except where legally exempted.
[VALIDATION] IF PII_collection = TRUE AND explicit_consent = FALSE AND legal_exemption = FALSE THEN violation

[RULE-02] Consent mechanisms MUST present information in plain language that enables individuals to make informed decisions about PII processing risks.
[VALIDATION] IF consent_language_complexity > grade_8_level OR technical_jargon = TRUE THEN violation

[RULE-03] Organizations MUST provide individuals with the ability to revoke previously granted consent within 30 days of the revocation request.
[VALIDATION] IF consent_revocation_request = TRUE AND processing_time > 30_days THEN violation

[RULE-04] Consent requests MUST clearly specify the types of PII to be collected, processing purposes, and data sharing arrangements.
[VALIDATION] IF consent_specificity_score < required_threshold THEN violation

[RULE-05] Organizations MUST maintain records of consent decisions including timestamps, IP addresses, and consent version for audit purposes.
[VALIDATION] IF consent_record_complete = FALSE OR retention_period < 7_years THEN violation

[RULE-06] Consent interfaces MUST be designed to avoid pre-checked boxes or other deceptive patterns that assume consent.
[VALIDATION] IF default_consent_state = TRUE OR deceptive_pattern_detected = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Consent Collection Procedure - Standardized process for obtaining and documenting user consent
- [PROC-02] Consent Revocation Procedure - Process for handling and implementing consent withdrawal requests
- [PROC-03] Consent Record Management - Maintenance and retention of consent decision records
- [PROC-04] Consent Interface Review - Regular assessment of consent presentation mechanisms

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, regulatory changes, privacy incidents involving consent

## 7. SCENARIO PATTERNS
[SCENARIO-01: Marketing Email Consent]
IF email_marketing = TRUE
AND explicit_opt_in = FALSE
AND pre_checked_box = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Mobile App PII Collection]
IF mobile_app_PII_collection = TRUE
AND consent_obtained_before_collection = TRUE
AND plain_language_used = TRUE
AND revocation_mechanism_available = TRUE
THEN compliance = TRUE

[SCENARIO-03: Third-Party Data Sharing]
IF data_sharing_with_third_party = TRUE
AND original_consent_covers_sharing = FALSE
AND new_consent_obtained = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Consent Revocation Request]
IF user_requests_consent_revocation = TRUE
AND processing_stopped_within_30_days = TRUE
AND confirmation_sent_to_user = TRUE
THEN compliance = TRUE

[SCENARIO-05: Minor's Consent Collection]
IF user_age < 13
AND parental_consent = FALSE
AND COPPA_applicable = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Tools/mechanisms for consent are defined | [RULE-01], [RULE-04] |
| Consent obtained prior to PII collection | [RULE-01] |
| Mechanisms facilitate informed decision-making | [RULE-02], [RULE-04] |
| Consent records maintained | [RULE-05] |
| Revocation capabilities provided | [RULE-03] |