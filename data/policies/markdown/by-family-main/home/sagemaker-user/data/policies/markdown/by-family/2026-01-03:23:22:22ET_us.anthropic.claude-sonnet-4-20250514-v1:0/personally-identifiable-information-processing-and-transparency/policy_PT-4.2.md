# POLICY: PT-4.2: Just-in-time Consent

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-4.2 |
| NIST Control | PT-4.2: Just-in-time Consent |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | consent, just-in-time, PII processing, user consent, privacy mechanisms |

## 1. POLICY STATEMENT
The organization SHALL implement just-in-time consent mechanisms that present consent options to individuals at the time of or in conjunction with personally identifiable information (PII) processing activities. Consent mechanisms MUST be clearly defined, appropriately timed, and presented at organization-defined frequencies to ensure meaningful individual participation in PII processing decisions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Including cloud and hybrid infrastructure |
| Customer-facing applications | YES | Web, mobile, and API interfaces |
| Employee PII systems | YES | HR and internal systems |
| Third-party integrations | YES | When processing customer/employee PII |
| Anonymous data systems | NO | No PII processing occurs |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define consent mechanism requirements<br>• Approve consent frequency policies<br>• Oversee compliance monitoring |
| Product Managers | • Implement just-in-time consent in applications<br>• Define user experience for consent collection<br>• Coordinate with privacy team on requirements |
| Development Teams | • Build consent mechanisms into systems<br>• Implement consent validation logic<br>• Maintain consent audit trails |
| Legal Team | • Review consent language and mechanisms<br>• Ensure regulatory compliance<br>• Approve consent policy changes |

## 4. RULES
[RULE-01] All systems processing PII MUST implement just-in-time consent mechanisms that present consent options at the time of or immediately before PII processing activities.
[VALIDATION] IF system_processes_pii = TRUE AND just_in_time_consent_implemented = FALSE THEN violation

[RULE-02] Consent mechanisms MUST be clearly defined with specific language, presentation format, and user interface requirements documented in the privacy plan.
[VALIDATION] IF consent_mechanism_defined = FALSE OR consent_language_documented = FALSE THEN violation

[RULE-03] Organizations MUST define and document the frequency at which consent mechanisms are presented to individuals for ongoing PII processing activities.
[VALIDATION] IF consent_frequency_defined = FALSE OR consent_frequency_documented = FALSE THEN violation

[RULE-04] Just-in-time consent MUST be presented for high-risk PII processing activities including data sharing with third parties, cross-border transfers, and sensitive data processing.
[VALIDATION] IF processing_risk_level = "high" AND just_in_time_consent_presented = FALSE THEN critical_violation

[RULE-05] Consent responses MUST be recorded with timestamps, user identifiers, and processing context to maintain an auditable consent trail.
[VALIDATION] IF consent_given = TRUE AND (timestamp_recorded = FALSE OR user_id_recorded = FALSE OR context_recorded = FALSE) THEN violation

[RULE-06] Systems MUST validate current consent status before processing PII and halt processing if valid consent is not present.
[VALIDATION] IF pii_processing_initiated = TRUE AND valid_consent_verified = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Consent Mechanism Design - Define and document consent presentation methods, timing, and user interface requirements
- [PROC-02] Consent Frequency Assessment - Establish and review frequency requirements for consent re-presentation based on processing risk
- [PROC-03] Consent Validation - Implement technical controls to verify valid consent before PII processing
- [PROC-04] Consent Audit Trail Management - Maintain comprehensive records of consent interactions and responses

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, regulatory changes, privacy incidents, system architecture changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Processing Feature]
IF new_feature_processes_pii = TRUE
AND just_in_time_consent_implemented = TRUE
AND consent_mechanism_defined = TRUE
THEN compliance = TRUE

[SCENARIO-02: Third-Party Data Sharing]
IF pii_shared_with_third_party = TRUE
AND just_in_time_consent_presented = FALSE
AND high_risk_processing = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Expired Consent Processing]
IF last_consent_date > organization_defined_frequency
AND pii_processing_continues = TRUE
AND consent_re_presented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Emergency Processing Override]
IF emergency_processing = TRUE
AND just_in_time_consent_bypassed = TRUE
AND legal_basis_documented = TRUE
AND post_processing_notification_sent = TRUE
THEN compliance = TRUE

[SCENARIO-05: Incomplete Consent Records]
IF consent_given = TRUE
AND (timestamp_missing = TRUE OR context_missing = TRUE)
AND audit_trail_incomplete = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Consent mechanisms presented to individuals are defined | [RULE-02] |
| Frequency for presenting consent mechanisms is defined | [RULE-03] |
| PII processing presented in conjunction with consent mechanisms | [RULE-01], [RULE-04] |
| Just-in-time consent implementation validation | [RULE-05], [RULE-06] |