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
The organization SHALL present notice of personally identifiable information (PII) processing to individuals at the time and location where PII is collected or in conjunction with specific data actions. Just-in-time notices MUST inform individuals about PII processing when such information is most relevant and useful to their decision-making.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems collecting PII | YES | Includes web applications, mobile apps, APIs |
| Employee systems | YES | Internal HR and administrative systems |
| Third-party integrations | YES | When processing PII on behalf of organization |
| Public-facing services | YES | Customer and visitor interactions |
| Legacy systems | CONDITIONAL | Must comply within 12 months of policy effective date |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Establish just-in-time notice standards<br>• Review and approve notice templates<br>• Monitor compliance across organization |
| Product Managers | • Identify data actions requiring just-in-time notice<br>• Coordinate notice implementation in user interfaces<br>• Conduct user experience testing for notice effectiveness |
| Development Teams | • Implement just-in-time notice mechanisms<br>• Ensure notices appear at appropriate collection points<br>• Maintain notice delivery logs |
| Legal Team | • Review notice content for legal adequacy<br>• Ensure compliance with applicable privacy laws<br>• Update notices based on regulatory changes |

## 4. RULES
[RULE-01] Just-in-time notices MUST be presented at the exact time and location where individuals provide PII or immediately before a data action occurs.
[VALIDATION] IF PII_collection_event = TRUE AND notice_timestamp != collection_timestamp THEN violation

[RULE-02] Just-in-time notices MUST be displayed for high-risk data actions including data sharing with third parties, automated decision-making, and purpose changes.
[VALIDATION] IF data_action_risk_level = "high" AND just_in_time_notice = FALSE THEN violation

[RULE-03] Notice content MUST be updated within 30 days when data processing practices change materially from previously disclosed practices.
[VALIDATION] IF processing_change_date + 30_days < current_date AND notice_updated = FALSE THEN violation

[RULE-04] Just-in-time notices MUST include specific information about the data action being performed and its purpose rather than generic privacy statements.
[VALIDATION] IF notice_type = "generic" AND data_action_specific = FALSE THEN violation

[RULE-05] Organizations MUST maintain logs of when just-in-time notices are presented to individuals for audit purposes.
[VALIDATION] IF notice_presented = TRUE AND audit_log_entry = FALSE THEN violation

[RULE-06] Just-in-time notices MUST be presented in the same language as the primary user interface or the individual's preferred language when known.
[VALIDATION] IF user_language != notice_language AND preferred_language_available = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Action Risk Assessment - Evaluate and classify data actions requiring just-in-time notice
- [PROC-02] Notice Content Development - Create and maintain standardized just-in-time notice templates
- [PROC-03] User Interface Integration - Implement notice delivery mechanisms in applications and systems
- [PROC-04] Notice Effectiveness Monitoring - Track user engagement and comprehension of notices
- [PROC-05] Audit Log Management - Maintain and review logs of notice presentations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New data collection systems, material changes to data processing, regulatory updates, user complaints about notice clarity

## 7. SCENARIO PATTERNS
[SCENARIO-01: Third-Party Data Sharing]
IF data_sharing_with_third_party = TRUE
AND just_in_time_notice_presented = FALSE
AND user_consent_obtained = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Mobile App Location Collection]
IF location_data_collection = TRUE
AND notice_presented_at_permission_request = TRUE
AND notice_includes_specific_purpose = TRUE
THEN compliance = TRUE

[SCENARIO-03: Automated Decision Notice]
IF automated_decision_making = TRUE
AND decision_affects_individual = TRUE
AND just_in_time_notice = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Purpose Change Notification]
IF original_purpose != current_purpose
AND purpose_change_date + 30_days < current_date
AND updated_notice_presented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Generic Privacy Policy Display]
IF data_collection_active = TRUE
AND notice_type = "generic_privacy_policy"
AND specific_data_action_notice = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Notice presented at time and location of PII provision | [RULE-01] |
| Notice presented in conjunction with data actions | [RULE-02] |
| Notice frequency defined for ongoing processing | [RULE-03] |
| Notice content specificity for data actions | [RULE-04] |
| Audit trail maintenance | [RULE-05] |
| Accessibility and language requirements | [RULE-06] |