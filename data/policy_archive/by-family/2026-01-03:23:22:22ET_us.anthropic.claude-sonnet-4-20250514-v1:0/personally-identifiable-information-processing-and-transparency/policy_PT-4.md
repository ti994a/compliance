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
The organization SHALL implement tools and mechanisms that enable individuals to provide informed consent prior to the collection and processing of their personally identifiable information (PII). Consent mechanisms MUST facilitate individuals' understanding of privacy risks and support their decision-making regarding PII processing authorization.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes customer, employee, and third-party PII |
| Web applications | YES | User-facing consent interfaces required |
| Data collection forms | YES | Both digital and physical forms |
| Third-party integrations | YES | When collecting PII on behalf of organization |
| Anonymous data collection | NO | Unless re-identification is possible |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define consent requirements and mechanisms<br>• Approve consent language and processes<br>• Monitor consent compliance |
| Product Managers | • Implement consent mechanisms in systems<br>• Ensure user interface supports informed decision-making<br>• Document consent collection processes |
| Legal Team | • Review consent language for legal compliance<br>• Advise on consent requirements by jurisdiction<br>• Validate consent mechanisms meet regulatory standards |

## 4. RULES
[RULE-01] Consent MUST be obtained prior to any collection or processing of PII, except where legally exempted.
[VALIDATION] IF pii_collected = TRUE AND consent_obtained = FALSE AND legal_exemption = FALSE THEN violation

[RULE-02] Consent mechanisms MUST use plain language and avoid technical jargon to facilitate informed decision-making.
[VALIDATION] IF consent_language_complexity > grade_8_reading_level OR technical_jargon_present = TRUE THEN violation

[RULE-03] Organizations MUST provide individuals with the ability to revoke previously given consent through an accessible mechanism.
[VALIDATION] IF consent_revocation_mechanism = FALSE OR revocation_accessibility_compliant = FALSE THEN violation

[RULE-04] Consent requests MUST clearly specify the types of PII being collected, processing purposes, and data sharing practices.
[VALIDATION] IF consent_specificity_score < required_threshold THEN violation

[RULE-05] Opt-in consent MUST be used for sensitive PII categories including biometric, financial, health, or children's data.
[VALIDATION] IF sensitive_pii = TRUE AND consent_type != "opt-in" THEN critical_violation

[RULE-06] Consent mechanisms MUST authenticate individual identity when processing high-risk PII or for regulatory compliance.
[VALIDATION] IF high_risk_pii = TRUE AND identity_authentication = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Consent Mechanism Design - Define and implement user interfaces for obtaining informed consent
- [PROC-02] Consent Language Review - Regular review of consent language for clarity and legal compliance
- [PROC-03] Consent Revocation Processing - Handle and process individual requests to revoke consent
- [PROC-04] Consent Record Maintenance - Maintain records of consent decisions and revocations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, regulatory changes, privacy incidents, system modifications affecting consent

## 7. SCENARIO PATTERNS
[SCENARIO-01: Web Application User Registration]
IF pii_collection = TRUE
AND consent_obtained_before_collection = TRUE
AND consent_language_clear = TRUE
AND revocation_mechanism_available = TRUE
THEN compliance = TRUE

[SCENARIO-02: Sensitive Data Without Opt-in]
IF data_type = "biometric"
AND consent_type = "opt-out"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Third-party Data Sharing Without Specific Consent]
IF data_sharing_with_third_party = TRUE
AND consent_covers_sharing = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Children's Data Collection]
IF individual_age < 13
AND parental_consent = FALSE
AND consent_type != "opt-in"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Consent Revocation Request Ignored]
IF consent_revocation_requested = TRUE
AND revocation_processed_within_timeframe = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Tools/mechanisms for consent are defined | RULE-01, RULE-04 |
| Consent obtained prior to PII collection | RULE-01 |
| Mechanisms facilitate informed decision-making | RULE-02, RULE-04 |
| Appropriate consent type implementation | RULE-05 |
| Identity authentication for consent | RULE-06 |
| Consent revocation capability | RULE-03 |