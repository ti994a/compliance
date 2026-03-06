# POLICY: PT-7: Specific Categories of Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-7 |
| NIST Control | PT-7: Specific Categories of Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, processing conditions, sensitive data, privacy protections, data categories |

## 1. POLICY STATEMENT
The organization SHALL define and apply specific processing conditions and protections for categories of personally identifiable information (PII) based on sensitivity levels, legal requirements, and privacy risk assessments. All PII processing activities MUST comply with category-specific requirements derived from applicable laws, regulations, policies, and organizational privacy risk determinations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems processing any category of PII |
| Cloud Services | YES | Including third-party processors |
| Business Applications | YES | Customer-facing and internal applications |
| Data Analytics Platforms | YES | Especially those processing sensitive PII |
| Contractors/Vendors | YES | When processing PII on behalf of organization |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define PII categories and processing conditions<br>• Approve category-specific protections<br>• Oversee privacy risk assessments |
| Data Protection Officer | • Implement category-specific controls<br>• Monitor compliance with processing conditions<br>• Coordinate with legal counsel on requirements |
| System Owners | • Apply appropriate protections for PII categories<br>• Document processing conditions in privacy plans<br>• Ensure system compliance with category requirements |
| Legal Counsel | • Identify legal requirements for PII categories<br>• Review processing conditions for compliance<br>• Advise on regulatory obligations |

## 4. RULES
[RULE-01] The organization MUST define specific categories of PII and document applicable processing conditions for each category within 30 days of system deployment or PII category identification.
[VALIDATION] IF pii_category_defined = FALSE OR processing_conditions_documented = FALSE THEN violation

[RULE-02] Processing conditions for sensitive PII categories (SSN, financial data, health information, biometrics) MUST include enhanced protections beyond standard PII controls.
[VALIDATION] IF pii_category = "sensitive" AND enhanced_protections = FALSE THEN critical_violation

[RULE-03] All PII processing activities MUST comply with category-specific conditions as defined in the organizational privacy plan and applicable legal requirements.
[VALIDATION] IF processing_activity_compliant = FALSE AND pii_category_applicable = TRUE THEN violation

[RULE-04] Changes to PII categories or processing conditions MUST be reviewed by the Chief Privacy Officer and legal counsel before implementation.
[VALIDATION] IF category_change = TRUE AND (cpo_review = FALSE OR legal_review = FALSE) THEN violation

[RULE-05] Systems processing multiple PII categories MUST apply the most restrictive processing conditions applicable to any category processed.
[VALIDATION] IF multiple_categories = TRUE AND most_restrictive_applied = FALSE THEN violation

[RULE-06] Processing conditions for each PII category MUST be reviewed annually and updated based on privacy risk assessments, legal changes, or contextual factors.
[VALIDATION] IF last_review_date > 365_days OR privacy_risk_assessment_current = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Category Classification - Systematic identification and classification of PII types
- [PROC-02] Processing Condition Definition - Documentation of specific requirements per category
- [PROC-03] Enhanced Protection Implementation - Application of additional controls for sensitive categories
- [PROC-04] Privacy Risk Assessment - Regular evaluation of category-specific privacy risks
- [PROC-05] Legal Compliance Review - Ongoing assessment of regulatory requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon legal/regulatory changes
- Triggering events: New PII categories identified, legal requirement changes, privacy incidents, system modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Sensitive PII Without Enhanced Protections]
IF pii_category = "SSN" OR pii_category = "financial" OR pii_category = "health"
AND enhanced_protections = FALSE
AND processing_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Undefined PII Category Processing]
IF pii_processing = TRUE
AND pii_category_defined = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Mixed Category Processing]
IF pii_categories_count > 1
AND most_restrictive_conditions_applied = TRUE
AND all_categories_defined = TRUE
THEN compliance = TRUE

[SCENARIO-04: Outdated Processing Conditions]
IF processing_conditions_defined = TRUE
AND last_review_date > 365_days
AND privacy_risk_assessment_current = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Third-Party Processing Compliance]
IF vendor_processes_pii = TRUE
AND category_specific_requirements_in_contract = TRUE
AND vendor_compliance_verified = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Processing conditions for specific PII categories are defined | [RULE-01], [RULE-02] |
| Processing conditions are applied for specific PII categories | [RULE-03], [RULE-05] |
| Enhanced protections for sensitive categories | [RULE-02] |
| Regular review and updates | [RULE-06] |
| Change management for categories | [RULE-04] |