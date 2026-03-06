# POLICY: SI-18.5: Notice of Correction or Deletion

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18.5 |
| NIST Control | SI-18.5: Notice of Correction or Deletion |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, correction, deletion, notification, recipients, privacy |

## 1. POLICY STATEMENT
The organization SHALL notify all authorized recipients and affected individuals when personally identifiable information (PII) has been corrected or deleted. Notification procedures MUST ensure timely and complete communication to maintain data accuracy and individual privacy rights.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII Processing Systems | YES | Systems that collect, store, or process PII |
| Third-party Data Recipients | YES | External entities receiving organizational PII |
| Contractors/Vendors | YES | When processing PII on organization's behalf |
| Public Information | NO | Publicly available information excluded |
| De-identified Data | CONDITIONAL | Only if re-identification possible |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define notification procedures and timelines<br>• Oversee compliance monitoring<br>• Approve notification templates |
| Data Protection Officer | • Maintain recipient registries<br>• Execute notification procedures<br>• Document notification activities |
| System Administrators | • Implement automated notification mechanisms<br>• Maintain audit logs of corrections/deletions<br>• Support notification delivery |
| Legal Counsel | • Review notification requirements<br>• Assess regulatory compliance<br>• Handle notification disputes |

## 4. RULES
[RULE-01] The organization MUST maintain a current registry of all authorized PII recipients for each data processing activity.
[VALIDATION] IF PII_processing_activity EXISTS AND recipient_registry NOT current THEN violation

[RULE-02] All authorized recipients MUST be notified within 30 days when PII has been corrected or deleted.
[VALIDATION] IF PII_corrected OR PII_deleted AND notification_sent > 30_days THEN violation

[RULE-03] Affected individuals MUST be notified within 15 days when their PII has been corrected or deleted.
[VALIDATION] IF individual_PII_modified AND individual_notification > 15_days THEN violation

[RULE-04] Notifications MUST include the nature of the correction or deletion, the date of action, and any impact on the recipient's use of the information.
[VALIDATION] IF notification_sent AND (nature_missing OR date_missing OR impact_missing) THEN violation

[RULE-05] The organization MUST maintain audit logs of all correction/deletion notifications for at least 6 years.
[VALIDATION] IF notification_log_retention < 6_years THEN violation

[RULE-06] Automated notification mechanisms MUST be implemented where technically feasible to ensure consistent and timely notifications.
[VALIDATION] IF manual_notification_only AND automation_feasible = TRUE THEN non_compliance

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Recipient Registry Management - Maintain current list of all authorized PII recipients
- [PROC-02] Correction/Deletion Notification Process - Execute timely notifications to recipients and individuals
- [PROC-03] Notification Content Standards - Ensure complete and accurate notification information
- [PROC-04] Delivery Confirmation Tracking - Verify successful notification delivery
- [PROC-05] Audit Log Maintenance - Document all notification activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy incidents, regulatory changes, system modifications, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard PII Correction]
IF PII_correction_made = TRUE
AND recipient_registry_current = TRUE
AND recipients_notified_within_30_days = TRUE
AND individual_notified_within_15_days = TRUE
THEN compliance = TRUE

[SCENARIO-02: Delayed Individual Notification]
IF PII_deleted = TRUE
AND recipients_notified_within_30_days = TRUE
AND individual_notification_time = 20_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Recipient Registry]
IF PII_correction_made = TRUE
AND recipient_registry_exists = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Incomplete Notification Content]
IF notification_sent = TRUE
AND notification_includes_nature = FALSE
AND notification_delivery_time < 15_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Third-party Processing Correction]
IF contractor_corrects_PII = TRUE
AND organization_notified = TRUE
AND end_recipients_notified_within_30_days = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Recipients of PII notified when corrected/deleted are defined | RULE-01 |
| Individuals notified when PII corrected or deleted | RULE-03 |
| Authorized recipients notified of corrections/deletions | RULE-02 |
| Notification content requirements | RULE-04 |
| Documentation and audit requirements | RULE-05 |