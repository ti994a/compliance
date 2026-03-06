# POLICY: PT-7: Specific Categories of Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-7 |
| NIST Control | PT-7: Specific Categories of Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, personally identifiable information, processing conditions, privacy protection, sensitive data |

## 1. POLICY STATEMENT
The organization SHALL define and apply specific processing conditions and protections for categories of personally identifiable information (PII) based on legal requirements, regulatory mandates, and privacy risk assessments. All PII processing activities MUST comply with category-specific protections established through consultation with the senior agency official for privacy and legal counsel.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems processing any category of PII |
| Cloud Services | YES | Including hybrid and third-party services |
| Business Applications | YES | Customer-facing and internal applications |
| Data Analytics Platforms | YES | Platforms processing PII for analysis |
| Contractors/Vendors | YES | When processing PII on behalf of organization |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define PII categories and processing conditions<br>• Approve category-specific protections<br>• Oversee compliance monitoring |
| Data Protection Officers | • Implement category-specific controls<br>• Conduct PII processing assessments<br>• Monitor compliance with processing conditions |
| System Owners | • Apply required protections for PII categories<br>• Maintain documentation of processing conditions<br>• Report compliance status |
| Legal Counsel | • Provide guidance on regulatory requirements<br>• Review processing conditions for legal compliance<br>• Advise on category-specific protections |

## 4. RULES
[RULE-01] The organization MUST define specific categories of PII and their associated processing conditions based on legal requirements, regulations, and privacy risk assessments.
[VALIDATION] IF pii_categories_defined = FALSE OR processing_conditions_undefined = TRUE THEN violation

[RULE-02] Processing conditions for each PII category MUST be documented and approved by the Chief Privacy Officer and legal counsel.
[VALIDATION] IF processing_conditions_documented = FALSE OR cpo_approval = FALSE OR legal_approval = FALSE THEN violation

[RULE-03] Systems processing specific categories of PII MUST implement all required category-specific protections and controls.
[VALIDATION] IF pii_category_processed = TRUE AND required_protections_implemented = FALSE THEN violation

[RULE-04] PII processing activities MUST be assessed for compliance with category-specific conditions at least annually or when processing changes occur.
[VALIDATION] IF last_assessment_date > 365_days OR processing_changes = TRUE AND reassessment_completed = FALSE THEN violation

[RULE-05] Highly sensitive PII categories (SSN, financial data, health records) MUST have enhanced protections including encryption at rest and in transit.
[VALIDATION] IF pii_category = "highly_sensitive" AND (encryption_at_rest = FALSE OR encryption_in_transit = FALSE) THEN critical_violation

[RULE-06] Third-party processors MUST acknowledge and implement category-specific processing conditions through contractual agreements.
[VALIDATION] IF third_party_processor = TRUE AND (contract_includes_conditions = FALSE OR implementation_verified = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Category Classification - Systematic identification and classification of PII types
- [PROC-02] Processing Condition Definition - Establishment of category-specific requirements
- [PROC-03] Protection Implementation - Deployment of technical and administrative safeguards
- [PROC-04] Compliance Assessment - Regular evaluation of processing condition adherence
- [PROC-05] Third-Party Verification - Validation of vendor compliance with category requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon regulatory changes
- Triggering events: New privacy regulations, data breach incidents, significant processing changes, privacy risk assessment findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unprotected Sensitive PII Processing]
IF pii_category = "SSN" OR pii_category = "financial_account"
AND encryption_implemented = FALSE
AND processing_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Third-Party Processing Without Conditions]
IF data_processor = "third_party"
AND pii_categories_processed = TRUE
AND contract_includes_processing_conditions = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Undefined Processing Conditions]
IF new_pii_category_identified = TRUE
AND processing_conditions_defined = FALSE
AND processing_duration > 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Outdated Assessment]
IF pii_processing_active = TRUE
AND last_compliance_assessment > 365_days
AND no_assessment_scheduled = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Category Processing]
IF pii_category_defined = TRUE
AND processing_conditions_documented = TRUE
AND required_protections_implemented = TRUE
AND compliance_assessment_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Processing conditions defined for specific PII categories | [RULE-01], [RULE-02] |
| Processing conditions applied for specific PII categories | [RULE-03], [RULE-06] |
| Regular assessment of condition compliance | [RULE-04] |
| Enhanced protections for sensitive categories | [RULE-05] |