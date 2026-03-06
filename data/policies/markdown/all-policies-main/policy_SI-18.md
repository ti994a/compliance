# POLICY: SI-18: Personally Identifiable Information Quality Operations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18 |
| NIST Control | SI-18: Personally Identifiable Information Quality Operations |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, data quality, accuracy, timeliness, completeness, information lifecycle, validation |

## 1. POLICY STATEMENT
The organization SHALL implement systematic quality operations to check the accuracy, relevance, timeliness, and completeness of personally identifiable information (PII) throughout its lifecycle. Inaccurate or outdated PII MUST be corrected or deleted to maintain data integrity and protect individual privacy rights.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes collection, storage, processing, and transmission |
| Third-party data processors | YES | Must comply with contractual quality requirements |
| Archived/backup PII data | YES | Subject to periodic quality checks |
| De-identified data | CONDITIONAL | If re-identification risk exists |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Stewards | • Implement quality check procedures<br>• Validate PII accuracy during collection<br>• Coordinate correction/deletion activities |
| System Owners | • Ensure automated validation controls are implemented<br>• Maintain quality operation logs<br>• Report quality issues to privacy office |
| Privacy Office | • Define quality check frequencies<br>• Monitor compliance with quality operations<br>• Approve correction/deletion procedures |

## 4. RULES
[RULE-01] PII accuracy, relevance, timeliness, and completeness MUST be checked at organization-defined frequencies based on data sensitivity and usage context.
[VALIDATION] IF pii_quality_check_date + defined_frequency < current_date THEN violation

[RULE-02] High-sensitivity PII used for federal program determinations MUST be validated quarterly, while standard PII MUST be validated annually.
[VALIDATION] IF pii_sensitivity = "high" AND last_validation_date + 90_days < current_date THEN violation
[VALIDATION] IF pii_sensitivity = "standard" AND last_validation_date + 365_days < current_date THEN violation

[RULE-03] Automated validation mechanisms MUST be implemented for PII collection points including address verification and data format validation.
[VALIDATION] IF pii_collection_point = TRUE AND automated_validation = FALSE THEN violation

[RULE-04] Inaccurate or outdated PII MUST be corrected within 30 days of identification or deleted if correction is not feasible.
[VALIDATION] IF pii_accuracy_status = "inaccurate" AND days_since_identification > 30 AND correction_status = "pending" THEN violation

[RULE-05] All PII quality operations MUST be logged with timestamps, data elements checked, results, and corrective actions taken.
[VALIDATION] IF quality_operation_performed = TRUE AND operation_logged = FALSE THEN violation

[RULE-06] Quality check procedures MUST track data lineage and change history to enable identification of error sources.
[VALIDATION] IF pii_modified = TRUE AND change_history_maintained = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Quality Assessment - Systematic evaluation of accuracy, relevance, timeliness, and completeness
- [PROC-02] Automated Validation Implementation - Deployment of real-time validation controls at collection points
- [PROC-03] Error Correction Workflow - Process for correcting or deleting inaccurate/outdated PII
- [PROC-04] Quality Metrics Reporting - Regular reporting of PII quality metrics to privacy office

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when significant system changes occur
- Triggering events: Privacy incidents, audit findings, regulatory changes, system modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Expired Customer Data]
IF pii_type = "customer_data"
AND last_updated > 2_years_ago
AND quality_check_performed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Missing Address Validation]
IF data_collection_point = "web_form"
AND pii_includes_address = TRUE
AND automated_address_validation = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-03: Unresolved Inaccuracy]
IF pii_accuracy_issue_identified = TRUE
AND days_since_identification = 45
AND correction_action = "none"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Federal Program Data Validation]
IF pii_usage = "federal_program_determination"
AND last_comprehensive_validation > 90_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Change Tracking]
IF pii_correction_made = TRUE
AND change_history_documented = FALSE
AND audit_trail_maintained = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Check accuracy across information lifecycle | RULE-01, RULE-02 |
| Check relevance across information lifecycle | RULE-01, RULE-02 |
| Check timeliness across information lifecycle | RULE-01, RULE-02 |
| Check completeness across information lifecycle | RULE-01, RULE-02 |
| Define frequency for quality checks | RULE-02 |
| Correct inaccurate PII | RULE-04 |
| Delete outdated PII | RULE-04 |
| Implement validation mechanisms | RULE-03 |
| Maintain quality operation records | RULE-05, RULE-06 |