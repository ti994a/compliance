# POLICY: PT-7: Specific Categories of Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-7 |
| NIST Control | PT-7: Specific Categories of Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, personally identifiable information, processing conditions, privacy protection, data categories |

## 1. POLICY STATEMENT
The organization SHALL define and apply specific processing conditions and protections for categories of personally identifiable information (PII) based on legal requirements, regulatory obligations, and privacy risk assessments. Enhanced protections MUST be implemented for sensitive PII categories that pose elevated privacy risks or require special handling under applicable laws and regulations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII Processing Systems | YES | Including cloud, hybrid, and on-premises |
| Third-Party Processors | YES | Via contractual requirements |
| Employees Handling PII | YES | All roles with PII access |
| Business Partners | CONDITIONAL | When processing organization PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define PII categories and processing conditions<br>• Approve category-specific protections<br>• Oversee compliance monitoring |
| Data Protection Officer | • Conduct privacy risk assessments<br>• Document processing conditions<br>• Monitor implementation effectiveness |
| System Owners | • Implement category-specific controls<br>• Maintain PII inventory and classifications<br>• Report compliance status |

## 4. RULES
[RULE-01] Organizations MUST define specific categories of PII based on legal requirements, regulatory obligations, and privacy risk assessment results.
[VALIDATION] IF PII_categories_documented = FALSE OR legal_requirements_mapped = FALSE THEN violation

[RULE-02] Processing conditions for each defined PII category SHALL be documented and include applicable legal, regulatory, and policy requirements.
[VALIDATION] IF PII_category_exists = TRUE AND processing_conditions_documented = FALSE THEN violation

[RULE-03] Enhanced protections MUST be applied to sensitive PII categories including but not limited to SSN, financial data, health information, and biometric data.
[VALIDATION] IF PII_category = "sensitive" AND enhanced_protections = FALSE THEN critical_violation

[RULE-04] All PII processing activities MUST comply with category-specific conditions before processing begins.
[VALIDATION] IF processing_active = TRUE AND conditions_verified = FALSE THEN violation

[RULE-05] Organizations SHALL consult with legal counsel and senior agency official for privacy when defining category-specific protections.
[VALIDATION] IF new_PII_category = TRUE AND legal_consultation = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Category Definition - Process for identifying and categorizing PII types
- [PROC-02] Processing Condition Documentation - Procedure for documenting category-specific requirements
- [PROC-03] Privacy Risk Assessment - Assessment process for determining category sensitivity
- [PROC-04] Legal Consultation Process - Procedure for engaging legal counsel on PII protections

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New legal requirements, privacy incidents, system changes, new PII categories identified

## 7. SCENARIO PATTERNS
[SCENARIO-01: Sensitive PII Without Enhanced Protection]
IF PII_category = "SSN" OR PII_category = "financial" OR PII_category = "health"
AND enhanced_protections = FALSE
AND processing_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Undefined PII Category Processing]
IF PII_processing = TRUE
AND PII_category_defined = FALSE
AND processing_conditions = "undefined"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Processing Without Condition Verification]
IF PII_category_defined = TRUE
AND processing_conditions_documented = TRUE
AND condition_compliance_verified = FALSE
AND processing_initiated = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Compliant Category-Specific Processing]
IF PII_category_defined = TRUE
AND processing_conditions_documented = TRUE
AND legal_consultation_completed = TRUE
AND enhanced_protections = TRUE (for sensitive categories)
THEN compliance = TRUE

[SCENARIO-05: Third-Party Processing Without Conditions]
IF third_party_processor = TRUE
AND PII_transfer = TRUE
AND category_specific_contract_terms = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Processing conditions for specific PII categories are defined | [RULE-01], [RULE-02] |
| Processing conditions are applied for specific PII categories | [RULE-03], [RULE-04] |
| Legal consultation for PII protections | [RULE-05] |
| Enhanced protections for sensitive categories | [RULE-03] |