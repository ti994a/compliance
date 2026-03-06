# POLICY: PT-4.2: Just-in-time Consent

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-4.2 |
| NIST Control | PT-4.2: Just-in-time Consent |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | just-in-time consent, PII processing, consent mechanisms, privacy, data processing |

## 1. POLICY STATEMENT
The organization SHALL implement just-in-time consent mechanisms that present individuals with consent options at the time of or in conjunction with specific personally identifiable information (PII) processing activities. These mechanisms enable individuals to make informed decisions about their PII processing when their participation is most meaningful and relevant.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes web applications, mobile apps, APIs |
| Customer-facing interfaces | YES | Primary focus for just-in-time consent |
| Employee systems | CONDITIONAL | When processing sensitive employee PII |
| Third-party integrations | YES | When sharing PII with external parties |
| Automated processing systems | YES | Especially for profiling or analytics |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define consent mechanism requirements<br>• Approve consent frequency parameters<br>• Oversee compliance monitoring |
| Product Managers | • Implement just-in-time consent in user interfaces<br>• Define consent presentation triggers<br>• Ensure user experience compliance |
| Development Teams | • Build consent mechanisms into applications<br>• Implement consent logging and tracking<br>• Integrate with consent management platforms |

## 4. RULES

[RULE-01] Organizations MUST define specific consent mechanisms that will be presented to individuals for each type of PII processing activity.
[VALIDATION] IF pii_processing_type EXISTS AND consent_mechanism NOT defined THEN violation

[RULE-02] Organizations MUST define the frequency at which consent mechanisms are presented to individuals based on processing risk and context.
[VALIDATION] IF consent_frequency NOT defined OR consent_frequency = "undefined" THEN violation

[RULE-03] Just-in-time consent MUST be presented in conjunction with or immediately before the specific PII processing activity occurs.
[VALIDATION] IF pii_processing_initiated = TRUE AND consent_timestamp > processing_timestamp THEN violation

[RULE-04] Consent mechanisms MUST be presented when processing creates significant privacy risk or when individual assumptions about processing may be inaccurate.
[VALIDATION] IF privacy_risk_level = "high" AND just_in_time_consent = FALSE THEN violation

[RULE-05] Organizations MUST maintain records of when and how just-in-time consent was presented and individual responses.
[VALIDATION] IF consent_presented = TRUE AND consent_record NOT EXISTS THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Consent Mechanism Design - Define and document consent presentation methods for each PII processing type
- [PROC-02] Consent Frequency Assessment - Establish criteria for determining when to re-present consent options
- [PROC-03] Just-in-Time Consent Implementation - Technical procedures for integrating consent mechanisms into systems
- [PROC-04] Consent Response Logging - Document and track individual consent decisions and timestamps

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, privacy incidents, regulatory changes, user interface modifications

## 7. SCENARIO PATTERNS

[SCENARIO-01: High-Risk Processing Without Just-in-Time Consent]
IF privacy_risk_level = "high"
AND pii_processing_active = TRUE
AND just_in_time_consent_presented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Consent Presented After Processing Begins]
IF pii_processing_initiated = TRUE
AND consent_timestamp > processing_start_timestamp
AND processing_type = "behavioral_analytics"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Consent Mechanism Definition]
IF pii_processing_type = "location_tracking"
AND consent_mechanism_defined = FALSE
AND system_status = "production"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Proper Just-in-Time Implementation]
IF consent_mechanism_defined = TRUE
AND consent_presented_before_processing = TRUE
AND consent_response_logged = TRUE
AND privacy_risk_assessment_completed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Undefined Consent Frequency]
IF pii_processing_ongoing = TRUE
AND consent_frequency = "undefined"
AND last_consent_date > 365_days_ago
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Consent mechanisms presented to individuals are defined | [RULE-01] |
| Frequency at which to present consent mechanisms is defined | [RULE-02] |
| PII processing presented in conjunction with consent mechanisms | [RULE-03] |
| Just-in-time consent implementation and logging | [RULE-05] |