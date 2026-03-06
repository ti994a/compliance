# POLICY: SI-19.1: Collection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-19.1 |
| NIST Control | SI-19.1: Collection |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | de-identification, PII, data collection, privacy, data minimization |

## 1. POLICY STATEMENT
The organization SHALL de-identify datasets upon collection by not collecting personally identifiable information (PII) that is not required for the intended business purpose. Data collection mechanisms MUST be configured to exclude PII elements when such information will not be used for authorized purposes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All data collection systems | YES | Including forms, APIs, databases |
| Third-party data sources | YES | When under organizational control |
| Customer-facing applications | YES | Web forms, mobile apps, surveys |
| Internal data processing | YES | HR systems, analytics platforms |
| Legacy systems | CONDITIONAL | Must comply within 12 months |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Review data collection requirements<br>• Approve PII collection justifications<br>• Monitor compliance with de-identification |
| System Owners | • Configure systems to exclude unnecessary PII<br>• Document business justification for PII collection<br>• Implement technical controls |
| Privacy Team | • Conduct privacy impact assessments<br>• Define PII data elements<br>• Validate de-identification procedures |

## 4. RULES
[RULE-01] Data collection systems MUST NOT collect PII elements unless there is documented business justification and legal authority.
[VALIDATION] IF pii_collected = TRUE AND business_justification = FALSE THEN violation

[RULE-02] Application forms and interfaces SHALL exclude PII fields when the information will not be used for authorized purposes.
[VALIDATION] IF form_contains_pii = TRUE AND pii_usage_documented = FALSE THEN violation

[RULE-03] System configurations MUST prevent the collection of PII elements identified as unnecessary during privacy impact assessment.
[VALIDATION] IF system_collects_unnecessary_pii = TRUE THEN critical_violation

[RULE-04] Data collection mechanisms SHALL implement technical controls to enforce PII minimization at the point of collection.
[VALIDATION] IF technical_controls_implemented = FALSE AND pii_collection_possible = TRUE THEN violation

[RULE-05] Business justification for PII collection MUST be documented and approved by the Data Protection Officer before system deployment.
[VALIDATION] IF pii_collection = TRUE AND dpo_approval = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Collection Assessment - Evaluate necessity of PII elements before system design
- [PROC-02] Form Design Review - Validate that forms exclude unnecessary PII fields
- [PROC-03] System Configuration Audit - Verify technical controls prevent unnecessary PII collection
- [PROC-04] Business Justification Documentation - Document and approve legitimate need for PII

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New data collection system deployment, privacy incident, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Job Application Form]
IF form_type = "job_application"
AND ssn_field_present = TRUE
AND ssn_usage_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Customer Survey]
IF data_type = "customer_feedback"
AND personal_identifiers_collected = TRUE
AND anonymous_option_available = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Analytics Data Collection]
IF purpose = "analytics"
AND ip_addresses_stored = TRUE
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Legacy System Migration]
IF system_type = "legacy"
AND migration_date < current_date
AND unnecessary_pii_fields_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Third-Party Integration]
IF data_source = "third_party"
AND pii_filtering_enabled = FALSE
AND contractual_requirement = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dataset is de-identified upon collection by not collecting PII | RULE-01, RULE-02, RULE-03 |
| Technical controls prevent unnecessary PII collection | RULE-03, RULE-04 |
| Business justification for PII collection is documented | RULE-05 |
| System configurations enforce PII minimization | RULE-03, RULE-04 |