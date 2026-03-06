```markdown
# POLICY: PM-21: Accounting of Disclosures

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-21 |
| NIST Control | PM-21: Accounting of Disclosures |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII disclosure, accounting records, privacy tracking, disclosure logging, data sharing |

## 1. POLICY STATEMENT
The organization SHALL develop and maintain accurate accounting of all personally identifiable information (PII) disclosures. Disclosure records MUST be retained for the longer of PII retention period or five years after disclosure and made available to data subjects upon request.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Systems Processing PII | YES | Federal and contractor systems |
| PII Disclosures to Third Parties | YES | Internal and external disclosures |
| Automated Data Sharing | YES | API transfers, bulk exports |
| Manual PII Sharing | YES | Email, physical documents |
| De-identified Data | CONDITIONAL | If re-identification possible |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Establish disclosure accounting procedures<br>• Oversee compliance monitoring<br>• Review disclosure patterns |
| System Owners | • Implement disclosure logging mechanisms<br>• Maintain accurate disclosure records<br>• Respond to individual requests |
| Data Custodians | • Log all PII disclosures in real-time<br>• Validate disclosure record completeness<br>• Retain records per policy requirements |

## 4. RULES
[RULE-01] All PII disclosures MUST be logged with date, nature, purpose, and recipient contact information within 24 hours of disclosure.
[VALIDATION] IF pii_disclosed = TRUE AND logging_delay > 24_hours THEN violation

[RULE-02] Disclosure accounting records MUST be retained for the longer of PII retention period or five years after disclosure date.
[VALIDATION] IF disclosure_record_age > MAX(pii_retention_period, 5_years) AND record_deleted = TRUE THEN violation

[RULE-03] Disclosure accounting records MUST include complete recipient identification with name and current contact information.
[VALIDATION] IF disclosure_logged = TRUE AND (recipient_name = NULL OR recipient_contact = NULL) THEN violation

[RULE-04] Organizations MUST provide disclosure accounting to data subjects within 30 days of written request.
[VALIDATION] IF subject_request_received = TRUE AND response_time > 30_days THEN violation

[RULE-05] Automated disclosure mechanisms MUST generate disclosure accounting records without manual intervention.
[VALIDATION] IF automated_disclosure = TRUE AND manual_logging_required = TRUE THEN violation

[RULE-06] Disclosure accounting systems MUST maintain audit trails of all record access and modifications.
[VALIDATION] IF accounting_record_modified = TRUE AND audit_trail = NULL THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Disclosure Logging - Real-time capture of disclosure metadata
- [PROC-02] Disclosure Record Retention - Automated retention schedule management
- [PROC-03] Subject Request Processing - Response to individual accounting requests
- [PROC-04] Disclosure Audit Review - Periodic compliance verification

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy incidents, regulatory changes, system modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Complete Automated Disclosure]
IF pii_disclosed = TRUE
AND disclosure_date_logged = TRUE
AND recipient_info_complete = TRUE
AND automated_logging = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Recipient Information]
IF pii_disclosed = TRUE
AND disclosure_logged = TRUE
AND recipient_contact_info = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Subject Response]
IF subject_accounting_request = TRUE
AND request_date + 30_days < current_date
AND response_provided = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Premature Record Deletion]
IF disclosure_record_deleted = TRUE
AND pii_still_maintained = TRUE
AND deletion_date < disclosure_date + 5_years
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Manual Disclosure Without Logging]
IF manual_pii_sharing = TRUE
AND disclosure_logged = FALSE
AND disclosure_date + 24_hours < current_date
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Accurate accounting developed and maintained | RULE-01, RULE-06 |
| Date of disclosure included | RULE-01 |
| Nature of disclosure included | RULE-01 |
| Purpose of disclosure included | RULE-01 |
| Recipient name included | RULE-03 |
| Recipient contact information included | RULE-03 |
| Proper retention period maintained | RULE-02 |
| Available to subjects upon request | RULE-04 |
```