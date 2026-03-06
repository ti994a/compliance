# POLICY: SI-18(5): Notice of Correction or Deletion

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18-5 |
| NIST Control | SI-18(5): Notice of Correction or Deletion |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, correction, deletion, notification, recipients, privacy |

## 1. POLICY STATEMENT
The organization MUST notify all authorized recipients and affected individuals when personally identifiable information (PII) has been corrected or deleted. Recipients of PII correction or deletion notifications SHALL be explicitly defined and maintained in organizational procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII processing systems | YES | Including cloud and hybrid environments |
| Third-party PII recipients | YES | External partners, vendors, contractors |
| Data subjects/individuals | YES | Persons whose PII was corrected/deleted |
| Automated PII sharing systems | YES | APIs, data feeds, integrations |
| Archived/backup PII | CONDITIONAL | If technically feasible to correct/delete |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define notification recipient categories<br>• Approve notification procedures<br>• Monitor compliance with notification requirements |
| Data Protection Officer | • Maintain recipient notification lists<br>• Execute notification procedures<br>• Document notification activities |
| System Administrators | • Implement automated notification mechanisms<br>• Ensure system audit logging of notifications<br>• Maintain technical notification capabilities |

## 4. RULES
[RULE-01] All authorized recipients of PII MUST be defined and documented in a maintained registry before initial PII sharing occurs.
[VALIDATION] IF PII_shared = TRUE AND recipient_documented = FALSE THEN critical_violation

[RULE-02] When PII is corrected or deleted, ALL defined recipients MUST be notified within 72 hours of the correction or deletion action.
[VALIDATION] IF PII_corrected_or_deleted = TRUE AND notification_time > 72_hours THEN violation

[RULE-03] Affected individuals MUST be notified of PII corrections or deletions within 30 days unless legally prohibited or technically infeasible.
[VALIDATION] IF individual_notification_time > 30_days AND legal_prohibition = FALSE AND technical_feasibility = TRUE THEN violation

[RULE-04] Notification records MUST be maintained for all PII correction and deletion notifications for a minimum of 3 years.
[VALIDATION] IF notification_record_retention < 3_years THEN violation

[RULE-05] Automated notification mechanisms MUST be implemented for systems that regularly share PII with multiple recipients.
[VALIDATION] IF regular_PII_sharing = TRUE AND recipient_count > 5 AND automated_notification = FALSE THEN violation

[RULE-06] Notifications MUST include the specific PII elements that were corrected or deleted and the effective date of the action.
[VALIDATION] IF notification_sent = TRUE AND (PII_elements_specified = FALSE OR effective_date_included = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Recipient Registry Management - Maintain current list of all authorized PII recipients
- [PROC-02] Correction/Deletion Notification Process - Execute notifications to recipients and individuals
- [PROC-03] Notification Tracking and Documentation - Record all notification activities and responses
- [PROC-04] Technical Notification Implementation - Configure automated notification systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Data breach, new PII sharing agreements, regulatory changes, system modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard PII Correction]
IF PII_corrected = TRUE
AND all_recipients_notified = TRUE
AND notification_time <= 72_hours
AND individual_notified = TRUE
THEN compliance = TRUE

[SCENARIO-02: Delayed Recipient Notification]
IF PII_deleted = TRUE
AND recipient_notification_time > 72_hours
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Individual Notification]
IF PII_corrected = TRUE
AND recipients_notified = TRUE
AND individual_notification = FALSE
AND legal_prohibition = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Undocumented Recipients]
IF PII_shared = TRUE
AND correction_occurred = TRUE
AND recipient_registry_incomplete = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Automated System Notification]
IF regular_PII_sharing = TRUE
AND recipient_count > 5
AND automated_notification = TRUE
AND notification_successful = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Recipients of PII correction/deletion notifications are defined | [RULE-01] |
| Individuals are notified when PII has been corrected or deleted | [RULE-03] |
| All authorized recipients receive notifications | [RULE-02] |
| Notification process is documented and maintained | [RULE-04] |
| Technical implementation supports notification requirements | [RULE-05] |