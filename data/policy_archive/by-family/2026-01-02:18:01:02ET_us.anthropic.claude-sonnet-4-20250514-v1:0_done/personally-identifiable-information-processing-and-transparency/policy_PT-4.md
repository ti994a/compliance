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
The organization SHALL implement tools and mechanisms that enable individuals to provide informed consent prior to the collection and processing of their personally identifiable information (PII). Consent mechanisms MUST facilitate individuals' informed decision-making about privacy risks and provide clear options for granting, managing, and revoking consent.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Including cloud and hybrid infrastructure |
| Third-party processors | YES | When processing PII on organization's behalf |
| Internal administrative systems | CONDITIONAL | When processing employee PII beyond employment requirements |
| Public-facing applications | YES | All customer and user-facing systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Establish consent policies and standards<br>• Oversee consent mechanism implementation<br>• Monitor consent compliance |
| System Owners | • Implement appropriate consent mechanisms<br>• Ensure consent is obtained prior to PII collection<br>• Maintain consent records |
| Legal Counsel | • Determine legal consent requirements<br>• Review consent language and mechanisms<br>• Advise on regulatory compliance |

## 4. RULES
[RULE-01] All systems MUST obtain explicit consent from individuals prior to collecting or processing their PII, except where legally exempted.
[VALIDATION] IF PII_collection = TRUE AND consent_obtained = FALSE AND legal_exemption = FALSE THEN violation

[RULE-02] Consent mechanisms MUST use plain language and avoid technical jargon to facilitate informed decision-making.
[VALIDATION] IF consent_language_complexity > grade_8_reading_level OR technical_jargon_present = TRUE THEN violation

[RULE-03] Organizations MUST provide individuals the ability to revoke previously granted consent through an accessible mechanism.
[VALIDATION] IF consent_revocation_mechanism = FALSE OR revocation_accessibility_compliant = FALSE THEN violation

[RULE-04] Consent records MUST be maintained for audit purposes and include timestamp, individual identity verification, and specific processing authorized.
[VALIDATION] IF consent_record_complete = FALSE OR (timestamp = NULL OR identity_verified = FALSE OR processing_scope = NULL) THEN violation

[RULE-05] Opt-in consent MUST be used for sensitive PII categories unless opt-out is specifically permitted by applicable regulations.
[VALIDATION] IF PII_sensitivity = "high" AND consent_type = "opt-out" AND regulatory_exception = FALSE THEN violation

[RULE-06] Consent interfaces MUST clearly distinguish between mandatory and optional data collection with separate consent options.
[VALIDATION] IF mandatory_optional_distinction = FALSE OR separate_consent_options = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Consent Mechanism Design - Standard process for designing and implementing user consent interfaces
- [PROC-02] Consent Record Management - Procedures for storing, accessing, and managing consent records
- [PROC-03] Consent Revocation Processing - Process for handling and implementing consent withdrawals
- [PROC-04] Consent Audit and Review - Regular review of consent mechanisms and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Regulatory changes, data breach incidents, system modifications affecting PII processing, legal requirement changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: E-commerce Customer Registration]
IF system_type = "customer-facing"
AND PII_collection = TRUE
AND consent_obtained = TRUE
AND consent_type = "opt-in"
AND plain_language = TRUE
THEN compliance = TRUE

[SCENARIO-02: Marketing Email Without Consent]
IF processing_purpose = "marketing"
AND consent_obtained = FALSE
AND legal_exemption = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Employee Data Beyond Employment]
IF user_type = "employee"
AND processing_scope = "beyond_employment_requirements"
AND consent_obtained = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Consent Revocation Request Ignored]
IF consent_revocation_requested = TRUE
AND revocation_processed = FALSE
AND request_age > 30_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Complex Technical Consent Language]
IF consent_language_complexity > grade_8_level
AND technical_jargon_present = TRUE
AND user_comprehension_facilitated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Tools or mechanisms for consent are defined | [RULE-01], [RULE-06] |
| Consent obtained prior to PII collection | [RULE-01] |
| Consent facilitates informed decision-making | [RULE-02], [RULE-06] |
| Appropriate consent mechanisms implemented | [RULE-03], [RULE-04], [RULE-05] |