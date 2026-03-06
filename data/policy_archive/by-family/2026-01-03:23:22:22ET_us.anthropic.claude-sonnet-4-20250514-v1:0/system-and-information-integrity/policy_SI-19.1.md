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
The organization SHALL de-identify datasets upon collection by not collecting personally identifiable information (PII) when such information is not required for business purposes. Data collection mechanisms MUST be configured to exclude PII elements that are not essential for the intended use of the dataset.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All data collection systems | YES | Including forms, APIs, databases |
| Third-party data sources | YES | When organization controls collection parameters |
| Legacy systems | YES | Must comply within 12 months |
| Emergency response systems | CONDITIONAL | Subject to business justification review |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Review data collection requirements<br>• Approve PII collection justifications<br>• Monitor compliance with de-identification procedures |
| System Owners | • Configure systems to exclude unnecessary PII<br>• Document business justification for any PII collection<br>• Implement technical controls for data minimization |
| Privacy Engineers | • Design de-identification mechanisms<br>• Validate technical implementation<br>• Conduct regular assessments of collection practices |

## 4. RULES
[RULE-01] Data collection forms and systems MUST NOT request or capture PII elements unless there is a documented business justification approved by the Data Protection Officer.
[VALIDATION] IF pii_element_collected = TRUE AND business_justification_approved = FALSE THEN violation

[RULE-02] System configurations SHALL prevent the collection of PII fields that are not explicitly required for the system's intended purpose.
[VALIDATION] IF system_collects_pii = TRUE AND pii_required_for_purpose = FALSE THEN violation

[RULE-03] All data collection mechanisms MUST be reviewed annually to identify and remove unnecessary PII collection points.
[VALIDATION] IF last_collection_review > 365_days THEN violation

[RULE-04] When PII collection is justified, the minimum necessary standard MUST be applied to limit collection to only essential data elements.
[VALIDATION] IF pii_collected > minimum_necessary_set THEN violation

[RULE-05] Automated systems SHALL be configured with technical controls to block collection of common PII identifiers when not required.
[VALIDATION] IF automated_pii_blocking = FALSE AND pii_collection_justified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Collection Assessment - Evaluate all collection points for PII necessity
- [PROC-02] System Configuration Review - Validate technical controls prevent unnecessary PII collection
- [PROC-03] Business Justification Process - Document and approve legitimate PII collection needs
- [PROC-04] De-identification Validation - Verify datasets are properly de-identified at collection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployment, data breach, regulatory changes, privacy impact assessment updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Application Form with Unnecessary SSN]
IF form_requests_ssn = TRUE
AND ssn_required_for_purpose = FALSE
AND business_justification = NULL
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: API Collecting Extra User Data]
IF api_collects_pii = TRUE
AND pii_elements > minimum_required
AND technical_controls_absent = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Legacy System Grandfathering]
IF system_age > 12_months
AND unnecessary_pii_collection = TRUE
AND remediation_plan = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Emergency System Exception]
IF system_type = "emergency_response"
AND pii_collection = TRUE
AND business_justification_documented = TRUE
AND dpo_approval = TRUE
THEN compliance = TRUE

[SCENARIO-05: Third-party Data Source]
IF data_source = "third_party"
AND organization_controls_collection = TRUE
AND unnecessary_pii_included = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dataset is de-identified upon collection by not collecting PII | RULE-01, RULE-02 |
| Technical controls prevent unnecessary PII collection | RULE-02, RULE-05 |
| Regular assessment of collection practices | RULE-03 |
| Minimum necessary standard applied | RULE-04 |