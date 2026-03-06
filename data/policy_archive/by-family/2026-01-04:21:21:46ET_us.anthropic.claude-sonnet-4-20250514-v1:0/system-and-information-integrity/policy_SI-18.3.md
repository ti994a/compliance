# POLICY: SI-18.3: Collection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18.3 |
| NIST Control | SI-18.3: Collection |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, data collection, direct collection, individual consent, privacy |

## 1. POLICY STATEMENT
All personally identifiable information (PII) MUST be collected directly from the individual or their designated representative. Organizations SHALL implement validation measures appropriate to the sensitivity and intended use of the collected PII.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes web forms, applications, databases |
| Third-party data brokers | NO | Cannot be primary collection source |
| Emergency response systems | CONDITIONAL | Exception process required |
| Public records integration | CONDITIONAL | Must supplement, not replace direct collection |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Collection Manager | • Ensure all PII collection mechanisms comply with direct collection requirements<br>• Validate data collection interfaces<br>• Maintain collection audit trails |
| Privacy Officer | • Review collection processes for compliance<br>• Approve exceptions to direct collection<br>• Monitor validation procedures |
| System Owners | • Implement technical controls for direct collection<br>• Configure systems to prevent indirect PII collection<br>• Document collection methods |

## 4. RULES
[RULE-01] PII collection systems MUST obtain information directly from the individual or their legally designated representative.
[VALIDATION] IF pii_source != "individual" AND pii_source != "designated_representative" AND exception_approved = FALSE THEN violation

[RULE-02] All PII collection interfaces MUST clearly identify the collecting organization and purpose of collection.
[VALIDATION] IF collection_interface_exists = TRUE AND (organization_identified = FALSE OR purpose_stated = FALSE) THEN violation

[RULE-03] Validation measures for collected PII MUST be proportional to the sensitivity level and intended use of the information.
[VALIDATION] IF pii_sensitivity = "high" AND validation_level < "comprehensive" THEN violation

[RULE-04] Systems MUST NOT automatically populate PII fields from third-party sources without explicit individual consent.
[VALIDATION] IF auto_populate = TRUE AND third_party_source = TRUE AND explicit_consent = FALSE THEN violation

[RULE-05] Exceptions to direct collection MUST be documented, approved by Privacy Officer, and reviewed annually.
[VALIDATION] IF collection_method = "indirect" AND (exception_documented = FALSE OR privacy_officer_approval = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Collection Interface Review - Quarterly assessment of all PII collection points
- [PROC-02] Validation Method Assessment - Annual review of PII validation procedures based on sensitivity
- [PROC-03] Exception Request Process - Formal process for requesting indirect collection exceptions
- [PROC-04] Third-party Integration Controls - Controls preventing unauthorized PII auto-population

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII collection system deployment, privacy incident, regulatory change

## 7. SCENARIO PATTERNS
[SCENARIO-01: Web Form Auto-Population]
IF collection_method = "web_form"
AND auto_populate_enabled = TRUE
AND data_source = "third_party_database"
AND user_consent = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Emergency Data Collection]
IF collection_context = "emergency_response"
AND pii_source = "family_member"
AND emergency_documented = TRUE
AND individual_unavailable = TRUE
THEN compliance = TRUE

[SCENARIO-03: Designated Representative Collection]
IF pii_source = "legal_guardian"
AND individual_age < 18
AND guardian_authority_verified = TRUE
AND collection_purpose = "benefits_enrollment"
THEN compliance = TRUE

[SCENARIO-04: Third-party Data Broker Usage]
IF pii_source = "commercial_data_broker"
AND collection_method = "bulk_purchase"
AND direct_collection_attempted = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Validation Mismatch]
IF pii_sensitivity = "high_risk"
AND intended_use = "benefit_determination"
AND validation_method = "basic_verification"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personally identifiable information is collected directly from the individual | [RULE-01], [RULE-04] |
| Appropriate validation measures are implemented | [RULE-03] |
| Collection interfaces properly identify organization and purpose | [RULE-02] |
| Exceptions are properly documented and approved | [RULE-05] |