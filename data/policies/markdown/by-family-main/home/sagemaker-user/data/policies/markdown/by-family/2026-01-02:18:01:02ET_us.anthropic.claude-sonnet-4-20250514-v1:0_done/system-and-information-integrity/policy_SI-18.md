# POLICY: SI-18: Personally Identifiable Information Quality Operations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18 |
| NIST Control | SI-18: Personally Identifiable Information Quality Operations |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, data quality, accuracy, timeliness, completeness, relevance, information lifecycle |

## 1. POLICY STATEMENT
The organization SHALL implement systematic quality operations to check the accuracy, relevance, timeliness, and completeness of personally identifiable information (PII) throughout its entire information lifecycle at defined frequencies. Inaccurate or outdated PII MUST be corrected or deleted promptly to maintain data integrity and protect individual privacy rights.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII Processing Systems | YES | Including cloud, hybrid, and on-premises |
| Third-party Data Processors | YES | Via contractual requirements |
| Employee PII | YES | HR and administrative systems |
| Customer PII | YES | All customer-facing applications |
| Archived/Backup PII | YES | Including long-term storage |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Define PII quality check frequencies<br>• Oversee quality operations program<br>• Approve correction/deletion procedures |
| System Owners | • Implement automated quality checks<br>• Execute regular quality assessments<br>• Maintain quality operation logs |
| Data Stewards | • Perform manual quality reviews<br>• Validate automated quality results<br>• Execute correction/deletion actions |

## 4. RULES
[RULE-01] PII accuracy checks MUST be performed at least quarterly for active data and annually for archived data.
[VALIDATION] IF pii_data_status = "active" AND last_accuracy_check > 90_days THEN violation
[VALIDATION] IF pii_data_status = "archived" AND last_accuracy_check > 365_days THEN violation

[RULE-02] PII relevance assessments MUST be conducted annually to determine continued business necessity.
[VALIDATION] IF pii_relevance_review_date < (current_date - 365_days) THEN violation

[RULE-03] PII timeliness checks MUST verify data currency based on data sensitivity: monthly for high-sensitivity, quarterly for medium-sensitivity, and annually for low-sensitivity PII.
[VALIDATION] IF pii_sensitivity = "high" AND last_timeliness_check > 30_days THEN violation
[VALIDATION] IF pii_sensitivity = "medium" AND last_timeliness_check > 90_days THEN violation
[VALIDATION] IF pii_sensitivity = "low" AND last_timeliness_check > 365_days THEN violation

[RULE-04] PII completeness validation MUST occur during data collection and quarterly thereafter for active processing.
[VALIDATION] IF pii_collection_event = TRUE AND completeness_check = FALSE THEN critical_violation
[VALIDATION] IF pii_status = "active_processing" AND last_completeness_check > 90_days THEN violation

[RULE-05] Inaccurate PII MUST be corrected within 30 days of identification, and outdated PII MUST be deleted within 15 days unless legal retention requirements apply.
[VALIDATION] IF pii_accuracy_status = "inaccurate" AND days_since_identification > 30 THEN violation
[VALIDATION] IF pii_status = "outdated" AND legal_hold = FALSE AND days_since_identification > 15 THEN violation

[RULE-06] Automated address verification APIs MUST be implemented for all address collection points.
[VALIDATION] IF system_collects_addresses = TRUE AND address_verification_api = FALSE THEN violation

[RULE-07] PII quality operations SHALL maintain audit trails documenting all checks, corrections, and deletions.
[VALIDATION] IF quality_operation_performed = TRUE AND audit_trail_created = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Quality Assessment - Systematic evaluation of accuracy, relevance, timeliness, and completeness
- [PROC-02] PII Correction Process - Standardized workflow for correcting inaccurate PII
- [PROC-03] PII Deletion Process - Secure deletion of outdated or irrelevant PII
- [PROC-04] Quality Metrics Reporting - Regular reporting on PII quality operations effectiveness
- [PROC-05] Third-party Quality Validation - Verification of PII quality in vendor-managed systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Privacy incidents, regulatory changes, system implementations, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Customer Address Update]
IF customer_address_changed = TRUE
AND address_verification_performed = TRUE
AND old_address_retained = TRUE
AND retention_period > 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Employee Termination Data]
IF employee_status = "terminated"
AND termination_date < (current_date - 90_days)
AND non_essential_pii_retained = TRUE
AND legal_hold = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Automated Quality Check Failure]
IF automated_quality_check = "failed"
AND manual_review_initiated = FALSE
AND failure_age > 48_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: High-Sensitivity PII Review]
IF pii_sensitivity = "high"
AND last_quality_check > 30_days
AND system_status = "production"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Third-party Data Quality]
IF data_source = "third_party"
AND quality_validation_performed = TRUE
AND validation_frequency = "quarterly"
AND last_validation < 90_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Check accuracy of PII across information lifecycle | RULE-01, RULE-07 |
| Check relevance of PII across information lifecycle | RULE-02, RULE-07 |
| Check timeliness of PII across information lifecycle | RULE-03, RULE-07 |
| Check completeness of PII across information lifecycle | RULE-04, RULE-07 |
| Correct inaccurate PII | RULE-05, RULE-06 |
| Delete outdated PII | RULE-05 |
| Define quality check frequencies | RULE-01, RULE-02, RULE-03, RULE-04 |