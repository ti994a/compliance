```markdown
# POLICY: SI-19.1: De-identification - Collection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-19.1 |
| NIST Control | SI-19.1: De-identification - Collection |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | de-identification, PII, data collection, privacy, data minimization |

## 1. POLICY STATEMENT
The organization SHALL de-identify datasets upon collection by not collecting personally identifiable information (PII) that is not required for the intended business purpose. Data collection mechanisms MUST be configured to exclude PII elements when such information will not be used for authorized purposes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All data collection systems | YES | Including web forms, APIs, databases |
| Third-party data sources | YES | When organization controls collection parameters |
| Legacy systems | YES | Must comply within 12 months of policy effective date |
| Emergency response systems | CONDITIONAL | Subject to approved exceptions for life safety |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Approve data collection requirements<br>• Review collection mechanisms for PII exposure<br>• Maintain PII inventory and collection justifications |
| System Owners | • Configure systems to prevent unnecessary PII collection<br>• Document business justification for any PII collection<br>• Implement technical controls for data minimization |
| Development Teams | • Design collection mechanisms with privacy by design<br>• Implement automated PII detection and blocking<br>• Test de-identification effectiveness |

## 4. RULES
[RULE-01] Data collection systems MUST be configured to exclude PII elements that are not required for the documented business purpose.
[VALIDATION] IF system_collects_pii = TRUE AND pii_business_justification = FALSE THEN violation

[RULE-02] Collection forms and interfaces SHALL NOT request PII when alternative non-identifying data elements can satisfy the business requirement.
[VALIDATION] IF collection_form_requests_pii = TRUE AND alternative_non_pii_available = TRUE THEN violation

[RULE-03] Automated data collection mechanisms MUST implement PII detection and prevention controls to block inadvertent PII capture.
[VALIDATION] IF automated_collection = TRUE AND pii_prevention_controls = FALSE THEN violation

[RULE-04] Business justification for PII collection MUST be documented and approved by the Data Protection Officer before system deployment.
[VALIDATION] IF system_collects_pii = TRUE AND dpo_approval_date = NULL THEN critical_violation

[RULE-05] Data collection systems SHALL be reviewed annually to identify opportunities for additional PII elimination.
[VALIDATION] IF last_pii_review_date > 365_days AND system_collects_pii = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Collection Assessment - Evaluate business necessity before implementing data collection
- [PROC-02] De-identification Validation - Test and verify PII exclusion in collection mechanisms  
- [PROC-03] Collection Mechanism Review - Annual assessment of existing systems for PII minimization opportunities
- [PROC-04] Exception Management - Process for documenting and approving necessary PII collection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: New data collection system deployment, privacy incident, regulatory changes, third-party integration

## 7. SCENARIO PATTERNS
[SCENARIO-01: Web Form PII Collection]
IF collection_method = "web_form"
AND form_requests_ssn = TRUE
AND ssn_business_justification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: API Data Ingestion]
IF data_source = "external_api"
AND api_includes_pii = TRUE
AND pii_filtering_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Survey Data Collection]
IF collection_type = "survey"
AND survey_requests_email = TRUE
AND anonymous_survey_sufficient = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Legacy System Compliance]
IF system_age > 12_months_since_policy
AND system_collects_unnecessary_pii = TRUE
AND remediation_plan_exists = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Emergency Exception]
IF system_type = "emergency_response"
AND pii_collection_approved_exception = TRUE
AND exception_review_date < 365_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dataset is de-identified upon collection by not collecting PII | RULE-01, RULE-02 |
| Technical controls prevent unnecessary PII collection | RULE-03 |
| Business justification documented for any PII collection | RULE-04 |
| Regular review of collection practices | RULE-05 |
```