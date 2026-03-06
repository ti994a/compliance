# POLICY: PT-5.1: Just-in-time Notice

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-5.1 |
| NIST Control | PT-5.1: Just-in-time Notice |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | just-in-time notice, PII processing, data actions, privacy transparency, individual notification |

## 1. POLICY STATEMENT
The organization MUST present notice of personally identifiable information (PII) processing to individuals at the time and location where PII is collected or in conjunction with data actions that may impact individual privacy. Just-in-time notices SHALL be provided to ensure individuals understand how their PII will be processed at the most relevant moments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems collecting PII | YES | Including web applications, mobile apps, APIs |
| Employee systems | YES | Internal HR and administrative systems |
| Third-party integrations | YES | When processing PII on behalf of organization |
| Archived systems | NO | Unless actively processing PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Approve just-in-time notice templates<br>• Define data actions requiring notices<br>• Oversee compliance monitoring |
| Product Managers | • Implement just-in-time notices in systems<br>• Coordinate with UX teams for notice placement<br>• Document notice delivery mechanisms |
| Development Teams | • Code notice presentation logic<br>• Ensure notices appear at appropriate triggers<br>• Maintain notice delivery logs |

## 4. RULES
[RULE-01] Just-in-time notices MUST be presented at the point of PII collection or immediately before data actions that increase privacy risk.
[VALIDATION] IF PII_collection = TRUE AND notice_presented = FALSE THEN violation

[RULE-02] Data actions with heightened privacy risk SHALL trigger just-in-time notices within 5 seconds of user interaction initiation.
[VALIDATION] IF data_action_risk_level = "high" AND notice_delay > 5_seconds THEN violation

[RULE-03] Just-in-time notices MUST be updated when processing purposes change or new data uses are implemented.
[VALIDATION] IF processing_purpose_changed = TRUE AND notice_updated = FALSE AND days_since_change > 30 THEN violation

[RULE-04] Systems SHALL log all just-in-time notice presentations including timestamp, user identifier, and notice version.
[VALIDATION] IF notice_presented = TRUE AND log_entry_created = FALSE THEN violation

[RULE-05] Just-in-time notices MUST be presented in the same interface and session where PII processing occurs.
[VALIDATION] IF PII_processing_interface ≠ notice_presentation_interface THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Just-in-Time Notice Design - Standard templates and placement guidelines for notices
- [PROC-02] Data Action Risk Assessment - Process to identify actions requiring just-in-time notices  
- [PROC-03] Notice Delivery Verification - Automated and manual validation of notice presentation
- [PROC-04] User Experience Testing - Evaluation of notice effectiveness and user comprehension

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, regulatory changes, user complaints about notice clarity

## 7. SCENARIO PATTERNS
[SCENARIO-01: PII Collection Without Notice]
IF user_provides_PII = TRUE
AND just_in_time_notice_shown = FALSE
AND collection_point_identified = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: High-Risk Data Action]
IF data_action_risk_level = "high"
AND user_interaction_initiated = TRUE
AND notice_presented_within_5_seconds = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Processing Purpose Change]
IF PII_processing_purpose_modified = TRUE
AND days_since_modification > 30
AND updated_notice_presented = FALSE
AND users_affected > 0
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Cross-Interface Processing]
IF PII_collected_interface = "web_form"
AND notice_presented_interface = "email"
AND same_session = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Just-in-Time Notice]
IF user_provides_PII = TRUE
AND notice_presented_at_collection = TRUE
AND notice_version_current = TRUE
AND delivery_logged = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Present notice at time and location of PII provision | RULE-01, RULE-05 |
| Present notice in conjunction with data actions | RULE-02 |
| Define frequency of notice presentation | RULE-03 |
| Maintain notice delivery documentation | RULE-04 |