# POLICY: SI-18.3: Collection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18.3 |
| NIST Control | SI-18.3: Collection |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII collection, direct collection, data validation, privacy controls, individual consent |

## 1. POLICY STATEMENT
All personally identifiable information (PII) MUST be collected directly from the individual or their designated representative whenever feasible. Organizations SHALL implement validation measures appropriate to the sensitivity and intended use of the collected PII to ensure accuracy and integrity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes web forms, applications, databases |
| Third-party data brokers | NO | Prohibited as primary collection source |
| Employee HR systems | YES | Direct collection from employees required |
| Customer-facing applications | YES | Must collect directly from customers |
| Marketing systems | YES | Opt-in collection mechanisms required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Oversee PII collection policies<br>• Validate collection mechanisms<br>• Conduct privacy impact assessments |
| System Owners | • Implement direct collection controls<br>• Document collection procedures<br>• Maintain audit trails of PII collection |
| Application Developers | • Design systems for direct collection<br>• Implement validation controls<br>• Ensure proper consent mechanisms |

## 4. RULES

[RULE-01] PII collection systems MUST obtain information directly from the individual or their legally designated representative.
[VALIDATION] IF pii_source != "individual" AND pii_source != "designated_representative" AND exception_approved = FALSE THEN violation

[RULE-02] Collection interfaces MUST clearly identify what PII is being collected and the purpose for collection before data entry.
[VALIDATION] IF collection_purpose_disclosed = FALSE OR pii_fields_identified = FALSE THEN violation

[RULE-03] Validation measures MUST be implemented based on PII sensitivity level: HIGH sensitivity requires multi-factor validation, MODERATE requires single validation method, LOW requires basic format validation.
[VALIDATION] IF pii_sensitivity = "HIGH" AND validation_factors < 2 THEN critical_violation
[VALIDATION] IF pii_sensitivity = "MODERATE" AND validation_methods < 1 THEN violation

[RULE-04] Third-party PII sources SHALL NOT be used as the primary collection method without documented business justification and individual consent.
[VALIDATION] IF primary_source = "third_party" AND (business_justification = FALSE OR individual_consent = FALSE) THEN violation

[RULE-05] All PII collection events MUST be logged with timestamp, source, collection method, and validation results.
[VALIDATION] IF pii_collected = TRUE AND (audit_log = FALSE OR required_fields_missing = TRUE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Collection Assessment - Evaluate and approve new PII collection mechanisms
- [PROC-02] Direct Collection Validation - Verify identity and accuracy of collected PII
- [PROC-03] Exception Management - Document and approve cases where direct collection is not feasible
- [PROC-04] Collection Audit Review - Regular review of PII collection logs and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: New PII collection systems, privacy incidents, regulatory changes, third-party integrations

## 7. SCENARIO PATTERNS

[SCENARIO-01: Web Form PII Collection]
IF collection_method = "web_form"
AND source_verification = "individual"
AND purpose_disclosed = TRUE
AND validation_implemented = TRUE
THEN compliance = TRUE

[SCENARIO-02: Third-Party Data Purchase]
IF pii_source = "data_broker"
AND primary_collection = TRUE
AND individual_consent = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Employee Onboarding]
IF system_type = "HR_system"
AND pii_source = "employee_direct"
AND validation_method = "document_verification"
AND audit_logged = TRUE
THEN compliance = TRUE

[SCENARIO-04: Marketing List Import]
IF collection_source = "purchased_list"
AND individual_consent_verified = FALSE
AND business_justification = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: High-Sensitivity PII Collection]
IF pii_sensitivity = "HIGH"
AND validation_factors = 1
AND collection_source = "individual"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personally identifiable information is collected directly from the individual | RULE-01, RULE-04 |
| Validation measures appropriate to PII sensitivity | RULE-03 |
| Proper documentation and audit trails | RULE-05 |
| Transparency in collection process | RULE-02 |