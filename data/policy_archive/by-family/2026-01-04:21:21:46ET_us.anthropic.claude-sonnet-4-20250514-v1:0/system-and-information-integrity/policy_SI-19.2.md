# POLICY: SI-19.2: Archiving

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-19.2 |
| NIST Control | SI-19.2: Archiving |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | archiving, PII, data minimization, dataset, retention, de-identification |

## 1. POLICY STATEMENT
The organization SHALL prohibit archiving of personally identifiable information (PII) elements in datasets when those elements will not be needed after archival. All archived datasets MUST contain only the minimum PII necessary for the specified archival purposes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All datasets containing PII | YES | Includes structured and unstructured data |
| Data archival systems | YES | Both cloud and on-premises storage |
| Temporary data processing | NO | Only applies to formal archival processes |
| Backup systems | CONDITIONAL | Only if backups serve as archives |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Define archival purposes and PII requirements<br>• Approve PII element inclusion decisions<br>• Document business justification for archived PII |
| Privacy Officer | • Review archival decisions for privacy compliance<br>• Validate PII minimization implementation<br>• Approve exceptions with documented risk assessment |
| Data Custodian | • Implement PII removal procedures<br>• Execute archival processes per approved specifications<br>• Maintain archival audit logs |

## 4. RULES
[RULE-01] Organizations MUST define specific purposes for each archived dataset before archival begins.
[VALIDATION] IF archival_purpose = "undefined" OR archival_purpose = "general" THEN violation

[RULE-02] PII elements SHALL NOT be included in archived datasets unless explicitly required for the defined archival purpose.
[VALIDATION] IF pii_element_archived = TRUE AND pii_required_for_purpose = FALSE THEN violation

[RULE-03] Data owners MUST document business justification for each PII element included in archived datasets.
[VALIDATION] IF pii_element_count > 0 AND business_justification_documented = FALSE THEN violation

[RULE-04] Archived datasets MUST undergo PII minimization review before archival completion.
[VALIDATION] IF archival_status = "complete" AND pii_minimization_review = FALSE THEN violation

[RULE-05] Organizations SHALL maintain records of PII elements removed during archival processes.
[VALIDATION] IF pii_removal_occurred = TRUE AND removal_log_maintained = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Pre-Archival PII Assessment - Evaluate dataset PII elements against archival purposes
- [PROC-02] PII Minimization Process - Remove unnecessary PII elements before archival
- [PROC-03] Archival Purpose Documentation - Define and document specific use cases for archived data
- [PROC-04] Post-Archival Validation - Verify only necessary PII elements remain in archived datasets

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy incidents, regulatory changes, new archival technologies, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Social Security Number in Research Archive]
IF dataset_contains_ssn = TRUE
AND archival_purpose = "longitudinal_research"
AND ssn_required_for_research = FALSE
AND record_linkage_complete = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Marketing Data Long-term Storage]
IF dataset_type = "customer_marketing"
AND pii_elements = ["email", "phone", "address"]
AND archival_purpose = "trend_analysis"
AND contact_info_required = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Financial Records with Minimal PII]
IF dataset_type = "financial_transactions"
AND pii_elements = ["account_number"]
AND archival_purpose = "regulatory_compliance"
AND account_number_required = TRUE
AND business_justification_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Healthcare Data Archive Without Consent]
IF dataset_contains_phi = TRUE
AND archival_purpose = "quality_improvement"
AND patient_consent_for_archival = FALSE
AND phi_required_for_purpose = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: De-identified Research Dataset]
IF original_dataset_contained_pii = TRUE
AND pii_removal_completed = TRUE
AND de_identification_validated = TRUE
AND archival_purpose = "public_research"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibit archiving unnecessary PII elements | RULE-02 |
| Document archival purposes | RULE-01, RULE-03 |
| Implement PII minimization | RULE-04 |
| Maintain archival records | RULE-05 |