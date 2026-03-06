# POLICY: PM-21: Accounting of Disclosures

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-21 |
| NIST Control | PM-21: Accounting of Disclosures |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, disclosure, accounting, privacy, retention, audit trail |

## 1. POLICY STATEMENT
The organization SHALL develop and maintain accurate accounting records for all disclosures of personally identifiable information (PII). These records MUST include comprehensive disclosure details and be made available to data subjects upon request.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Including cloud and hybrid environments |
| Third-party processors | YES | When disclosing organization PII |
| Contractors handling PII | YES | Must follow same requirements |
| Public information | NO | Unless combined with other PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee disclosure accounting program<br>• Approve disclosure accounting procedures<br>• Review compliance reports |
| Data Protection Officer | • Maintain disclosure accounting systems<br>• Process individual requests for accounting records<br>• Ensure retention compliance |
| System Owners | • Implement automated disclosure tracking<br>• Report PII disclosures within required timeframes<br>• Maintain system-level accounting records |

## 4. RULES
[RULE-01] All PII disclosures MUST be recorded in the accounting system within 24 hours of the disclosure event.
[VALIDATION] IF pii_disclosure_occurred = TRUE AND accounting_record_created > 24_hours THEN violation

[RULE-02] Disclosure accounting records MUST include date, nature, purpose, and recipient name and contact information.
[VALIDATION] IF disclosure_record EXISTS AND (date = NULL OR nature = NULL OR purpose = NULL OR recipient_info = NULL) THEN violation

[RULE-03] Accounting records MUST be retained for the longer of: PII retention period OR five years after disclosure.
[VALIDATION] IF disclosure_date + 5_years < current_date AND pii_retention_expired = TRUE AND accounting_record_deleted = TRUE THEN compliant

[RULE-04] Accounting records MUST be provided to data subjects within 30 days of a valid request.
[VALIDATION] IF individual_request_received = TRUE AND response_time > 30_days THEN violation

[RULE-05] Automated mechanisms SHOULD be implemented to detect and record PII disclosures where technically feasible.
[VALIDATION] IF system_processes_pii = TRUE AND automated_tracking = FALSE THEN requires_justification

[RULE-06] Disclosure accounting systems MUST maintain audit trails of all record access and modifications.
[VALIDATION] IF accounting_system_access = TRUE AND audit_log_entry = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Disclosure Recording - Standardized process for capturing disclosure details
- [PROC-02] Individual Request Processing - Handling data subject requests for accounting records
- [PROC-03] Retention Management - Automated retention and disposal of accounting records
- [PROC-04] Third-Party Disclosure Notification - Process for tracking external disclosures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Privacy incidents, regulatory changes, system modifications affecting PII processing

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Disclosure Details]
IF pii_disclosure = TRUE
AND disclosure_record_exists = TRUE
AND (recipient_contact_info = NULL OR disclosure_purpose = NULL)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Late Individual Response]
IF individual_accounting_request = TRUE
AND request_date + 35_days < current_date
AND response_provided = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Premature Record Deletion]
IF disclosure_date + 4_years < current_date
AND pii_still_maintained = TRUE
AND accounting_record_deleted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Automated Tracking Implementation]
IF system_processes_pii = TRUE
AND pii_volume = "HIGH"
AND automated_disclosure_tracking = FALSE
AND manual_process_documented = TRUE
THEN compliance = TRUE
violation_severity = "None"

[SCENARIO-05: Third-Party Processor Disclosure]
IF third_party_disclosure = TRUE
AND disclosure_recorded_within_24hrs = TRUE
AND recipient_contact_verified = TRUE
AND purpose_documented = TRUE
THEN compliance = TRUE
violation_severity = "None"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Accurate accounting developed and maintained | RULE-01, RULE-02 |
| Date of disclosure included | RULE-02 |
| Nature of disclosure included | RULE-02 |
| Purpose of disclosure included | RULE-02 |
| Recipient name included | RULE-02 |
| Recipient contact information included | RULE-02 |
| Proper retention timeframe | RULE-03 |
| Available to individuals upon request | RULE-04 |