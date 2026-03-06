# POLICY: SI-18.3: Collection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18.3 |
| NIST Control | SI-18.3: Collection |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII collection, direct collection, data validation, individual consent, privacy |

## 1. POLICY STATEMENT
The organization SHALL collect personally identifiable information (PII) directly from the individual whenever possible. When direct collection is not feasible, the organization MUST implement additional validation measures and document justification for indirect collection methods.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes customer, employee, and third-party PII |
| Data collection interfaces | YES | Web forms, mobile apps, paper forms, APIs |
| Third-party data sources | CONDITIONAL | Only when direct collection not feasible |
| Public datasets | CONDITIONAL | Must validate accuracy before use |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee PII collection policy compliance<br>• Approve exceptions to direct collection<br>• Review validation procedures |
| System Owners | • Implement direct collection mechanisms<br>• Document collection methods<br>• Ensure user interface compliance |
| Data Stewards | • Validate PII accuracy<br>• Monitor collection processes<br>• Report compliance issues |

## 4. RULES
[RULE-01] Systems MUST collect PII directly from the individual through authenticated interfaces whenever technically and operationally feasible.
[VALIDATION] IF pii_collected = TRUE AND collection_source != "individual_direct" AND justification_documented = FALSE THEN violation

[RULE-02] When direct collection is not possible, organizations MUST implement enhanced validation procedures and document the business justification within 5 business days.
[VALIDATION] IF collection_source = "third_party" AND validation_procedure_implemented = FALSE THEN violation

[RULE-03] All PII collection interfaces MUST clearly identify what information is being collected and provide individuals the opportunity to review and correct data before submission.
[VALIDATION] IF collection_interface_exists = TRUE AND review_mechanism = FALSE THEN violation

[RULE-04] For high-risk PII processing, organizations SHALL implement multi-factor validation when collecting information indirectly from third-party sources.
[VALIDATION] IF pii_risk_level = "high" AND collection_source = "third_party" AND validation_factors < 2 THEN critical_violation

[RULE-05] Organizations MUST maintain audit logs of all PII collection activities, including source, method, and validation results for minimum 3 years.
[VALIDATION] IF pii_collection_event = TRUE AND audit_log_created = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Collection Assessment - Evaluate feasibility of direct collection for each system
- [PROC-02] Indirect Collection Validation - Enhanced verification procedures for third-party sources
- [PROC-03] Collection Interface Review - Regular assessment of user-facing collection mechanisms
- [PROC-04] Data Accuracy Validation - Procedures for verifying PII accuracy based on sensitivity level

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployment, privacy incident, regulatory change, third-party integration

## 7. SCENARIO PATTERNS
[SCENARIO-01: Direct Collection via Web Portal]
IF collection_method = "web_portal"
AND user_authenticated = TRUE
AND pii_source = "individual_direct"
THEN compliance = TRUE

[SCENARIO-02: Third-Party Data Purchase]
IF collection_source = "data_broker"
AND business_justification = "not_documented"
AND validation_procedure = "none"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Employee Onboarding]
IF pii_type = "employee_data"
AND collection_source = "hr_system_direct"
AND individual_review_opportunity = TRUE
THEN compliance = TRUE

[SCENARIO-04: Emergency Contact Collection]
IF collection_source = "emergency_contact_reference"
AND pii_sensitivity = "low"
AND validation_attempted = TRUE
AND justification_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Background Check Data]
IF pii_sensitivity = "high"
AND collection_source = "third_party_vendor"
AND validation_factors >= 2
AND individual_consent = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| PII collected directly from individual | [RULE-01] |
| Enhanced validation for indirect collection | [RULE-02], [RULE-04] |
| Individual review and correction opportunity | [RULE-03] |
| Audit trail maintenance | [RULE-05] |