# POLICY: PT-4.2: Just-in-time Consent

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-4.2 |
| NIST Control | PT-4.2: Just-in-time Consent |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | consent, just-in-time, PII processing, individual participation, privacy controls |

## 1. POLICY STATEMENT
The organization SHALL present consent mechanisms to individuals at defined frequencies and in conjunction with personally identifiable information (PII) processing activities. Just-in-time consent mechanisms MUST enable individuals to make informed decisions about their PII processing at the time when such participation is most relevant and useful.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes customer, employee, and third-party data |
| Applications with user interfaces | YES | Web, mobile, and desktop applications |
| Automated PII processing systems | YES | Requires programmatic consent mechanisms |
| Legacy systems | CONDITIONAL | Must implement within 12 months |
| Emergency processing systems | CONDITIONAL | May use post-processing consent notification |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define consent mechanism requirements<br>• Approve consent frequency schedules<br>• Monitor compliance with consent policies |
| Product Managers | • Implement just-in-time consent in user workflows<br>• Define PII processing activities requiring consent<br>• Ensure consent mechanisms are user-friendly |
| Development Teams | • Build consent capture and management systems<br>• Implement consent validation logic<br>• Maintain consent audit trails |
| Legal Team | • Review consent language and mechanisms<br>• Ensure regulatory compliance<br>• Define consent withdrawal procedures |

## 4. RULES
[RULE-01] Consent mechanisms MUST be presented to individuals before each new type of PII processing activity that was not covered by previous consent.
[VALIDATION] IF new_pii_processing = TRUE AND previous_consent_covers_activity = FALSE THEN consent_required = TRUE

[RULE-02] Just-in-time consent MUST be presented for high-risk PII processing activities regardless of previous general consent.
[VALIDATION] IF pii_risk_level = "HIGH" AND processing_initiated = TRUE THEN just_in_time_consent_required = TRUE

[RULE-03] Consent mechanisms SHALL be presented at organization-defined frequencies not exceeding 12 months for ongoing PII processing.
[VALIDATION] IF last_consent_date + defined_frequency > current_date THEN consent_renewal_required = TRUE

[RULE-04] Individuals MUST be able to withdraw consent at any time through the same mechanism used to provide consent.
[VALIDATION] IF consent_withdrawal_requested = TRUE AND withdrawal_mechanism_available = FALSE THEN violation = TRUE

[RULE-05] All consent interactions MUST be logged with timestamp, individual identifier, processing purpose, and consent decision.
[VALIDATION] IF consent_interaction = TRUE AND (timestamp = NULL OR individual_id = NULL OR purpose = NULL OR decision = NULL) THEN logging_violation = TRUE

[RULE-06] Consent mechanisms MUST clearly describe the specific PII processing activity and its purpose in plain language.
[VALIDATION] IF consent_mechanism_deployed = TRUE AND (processing_description = NULL OR purpose_description = NULL OR plain_language_score < 8) THEN clarity_violation = TRUE

## 5. REQUIRED PROCEDURES
- [PROC-01] Consent Mechanism Design - Define user interface requirements and consent language standards
- [PROC-02] PII Processing Risk Assessment - Evaluate when just-in-time consent is required
- [PROC-03] Consent Frequency Management - Establish and maintain consent renewal schedules
- [PROC-04] Consent Audit and Monitoring - Regular review of consent compliance and effectiveness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, regulatory changes, privacy incidents, user experience feedback

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Sharing Partnership]
IF new_third_party_sharing = TRUE
AND previous_consent_covers_sharing = FALSE
AND pii_transfer_initiated = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Biometric Data Collection]
IF data_type = "biometric"
AND processing_purpose = "authentication"
AND just_in_time_consent_presented = TRUE
AND individual_consent = "granted"
THEN compliance = TRUE

[SCENARIO-03: Marketing Use After 12 Months]
IF original_consent_date + 365_days < current_date
AND processing_purpose = "marketing"
AND consent_renewal_presented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Emergency Processing Override]
IF processing_context = "emergency"
AND life_safety_risk = TRUE
AND post_processing_notification = TRUE
AND consent_sought_within_72_hours = TRUE
THEN compliance = TRUE

[SCENARIO-05: Consent Withdrawal Request]
IF consent_withdrawal_requested = TRUE
AND withdrawal_processed_within_24_hours = TRUE
AND pii_processing_stopped = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Consent mechanisms presented to individuals are defined | [RULE-01], [RULE-06] |
| Frequency at which to present consent mechanisms is defined | [RULE-03] |
| PII processing presented in conjunction with consent mechanisms is defined | [RULE-02], [RULE-06] |
| Just-in-time consent implementation | [RULE-01], [RULE-02] |
| Consent mechanism effectiveness | [RULE-04], [RULE-05] |