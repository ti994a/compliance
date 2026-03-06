# POLICY: PT-5.1: Just-in-time Notice

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-5.1 |
| NIST Control | PT-5.1: Just-in-time Notice |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | just-in-time notice, PII processing, data actions, privacy transparency, user consent |

## 1. POLICY STATEMENT
The organization SHALL present notice of personally identifiable information (PII) processing to individuals at the time and location where PII is provided or in conjunction with data actions. Just-in-time notices MUST inform individuals about PII processing when such information is most relevant and useful to their decision-making.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Web Applications | YES | All customer-facing applications |
| Mobile Applications | YES | All apps collecting PII |
| APIs | YES | When directly interfacing with users |
| Internal Systems | CONDITIONAL | Only when processing employee PII |
| Third-party Integrations | YES | When triggering new data actions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Privacy Officer | • Define notice timing requirements<br>• Approve notice content and placement<br>• Monitor compliance with notice delivery |
| Product Managers | • Implement just-in-time notices in user workflows<br>• Coordinate with UX teams on notice placement<br>• Ensure notices align with data collection points |
| Development Teams | • Build technical mechanisms for notice delivery<br>• Implement notice tracking and logging<br>• Ensure notices display before PII processing |

## 4. RULES
[RULE-01] Just-in-time notices MUST be presented immediately before or at the moment of PII collection or processing.
[VALIDATION] IF pii_collection_event = TRUE AND notice_timestamp > collection_timestamp THEN violation

[RULE-02] Notices MUST be displayed when data actions create new privacy risks or change existing processing purposes.
[VALIDATION] IF data_action_risk_level = "high" AND just_in_time_notice_shown = FALSE THEN violation

[RULE-03] Notice content MUST explain the specific data action being performed and its purpose in plain language.
[VALIDATION] IF notice_contains_data_action_description = FALSE OR notice_language_complexity > "8th_grade" THEN violation

[RULE-04] Users MUST acknowledge receipt of just-in-time notices before proceeding with the data action.
[VALIDATION] IF user_acknowledgment = FALSE AND data_processing_initiated = TRUE THEN violation

[RULE-05] Notice delivery mechanisms MUST log timestamp, content version, and user response for audit purposes.
[VALIDATION] IF notice_delivered = TRUE AND (log_timestamp = NULL OR content_version = NULL OR user_response = NULL) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Notice Content Development - Define and approve standardized notice templates for common data actions
- [PROC-02] Risk Assessment for Data Actions - Evaluate when just-in-time notices are required based on privacy risk
- [PROC-03] Notice Delivery Tracking - Log and monitor notice presentation and user responses
- [PROC-04] User Experience Testing - Validate notice effectiveness and user comprehension

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New data collection methods, regulatory changes, privacy incidents, user complaints about notice clarity

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Collection Feature]
IF new_pii_field_added = TRUE
AND just_in_time_notice_implemented = FALSE
AND feature_deployed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Third-party Data Sharing]
IF data_shared_with_third_party = TRUE
AND sharing_purpose_changed = TRUE
AND contextual_notice_shown = TRUE
AND user_acknowledged = TRUE
THEN compliance = TRUE

[SCENARIO-03: Biometric Data Processing]
IF data_type = "biometric"
AND processing_initiated = TRUE
AND just_in_time_notice_shown = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Marketing Use of Data]
IF data_action = "marketing_use"
AND original_purpose = "service_delivery"
AND contextual_notice_provided = TRUE
AND notice_explains_new_purpose = TRUE
THEN compliance = TRUE

[SCENARIO-05: Location Data Collection]
IF location_data_requested = TRUE
AND app_context = "unrelated_to_location_service"
AND just_in_time_notice_shown = TRUE
AND notice_logged = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Notice presented at time of PII collection | [RULE-01] |
| Notice provided in conjunction with data actions | [RULE-02] |
| Notice content explains processing purpose | [RULE-03] |
| User acknowledgment captured | [RULE-04] |
| Notice delivery documented | [RULE-05] |