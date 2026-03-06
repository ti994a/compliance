# POLICY: SA-4.6: Use of Information Assurance Products

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.6 |
| NIST Control | SA-4.6: Use of Information Assurance Products |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | information assurance, NSA-approved, classified information, COTS, GOTS, cryptographic products |

## 1. POLICY STATEMENT
The organization SHALL employ only NSA-approved government off-the-shelf (GOTS) or commercial off-the-shelf (COTS) information assurance products when protecting classified information transmitted over networks at lower classification levels. All information assurance products MUST be evaluated and validated by NSA or through NSA-approved procedures before deployment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified Information Systems | YES | All systems handling classified data |
| Cross-Domain Solutions | YES | Systems bridging classification levels |
| Cryptographic Products | YES | Products protecting classified information |
| Unclassified Systems | NO | Unless interfacing with classified networks |
| Development/Test Environments | CONDITIONAL | Only if processing classified data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Maintain NSA-approved product lists<br>• Approve information assurance product acquisitions<br>• Ensure compliance with NSA validation requirements |
| Procurement Officer | • Verify NSA approval status before purchase<br>• Document product evaluation credentials<br>• Coordinate with security team on IA product acquisitions |
| System Administrator | • Deploy only approved IA products<br>• Maintain current product validation status<br>• Report non-compliant product discoveries |

## 4. RULES
[RULE-01] Organizations MUST employ only GOTS or COTS information assurance products that appear on the current NSA-approved solutions list when protecting classified information on lower classification networks.
[VALIDATION] IF product_type = "information_assurance" AND classified_data = TRUE AND network_classification < data_classification AND nsa_approved = FALSE THEN critical_violation

[RULE-02] All information assurance products SHALL be evaluated and validated by NSA or through NSA-approved procedures before deployment in classified environments.
[VALIDATION] IF product_deployment = TRUE AND classified_environment = TRUE AND (nsa_evaluated = FALSE AND nsa_approved_procedure_validated = FALSE) THEN critical_violation

[RULE-03] Commercial off-the-shelf IA products using cryptographic means MUST implement NSA-approved key management when protecting classified information.
[VALIDATION] IF product_type = "COTS_IA" AND cryptographic_protection = TRUE AND classified_data = TRUE AND nsa_approved_key_mgmt = FALSE THEN major_violation

[RULE-04] Organizations MUST maintain current documentation of NSA approval status for all deployed information assurance products.
[VALIDATION] IF ia_product_deployed = TRUE AND (approval_documentation = FALSE OR approval_status = "expired") THEN moderate_violation

[RULE-05] Information assurance products SHALL NOT be deployed in classified environments without verified NSA Commercial Solutions for Classified (CSfC) compliance when applicable.
[VALIDATION] IF classified_deployment = TRUE AND csfc_applicable = TRUE AND csfc_compliant = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] NSA Product Approval Verification - Process for validating NSA approval status before procurement
- [PROC-02] IA Product Inventory Management - Maintaining current list of deployed IA products and approval status
- [PROC-03] Cross-Domain Solution Validation - Procedures for validating products used in cross-domain environments
- [PROC-04] Key Management Implementation - Process for implementing NSA-approved key management in COTS products

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: NSA product list updates, new classified system deployments, security incidents involving IA products

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved IA Product Deployment]
IF product_category = "information_assurance"
AND deployment_environment = "classified"
AND nsa_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Expired NSA Validation]
IF ia_product_status = "deployed"
AND nsa_validation_date < (current_date - validation_period)
AND revalidation_completed = FALSE
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-03: COTS Product Without Approved Key Management]
IF product_type = "COTS"
AND cryptographic_function = TRUE
AND classified_data_protection = TRUE
AND nsa_approved_key_management = FALSE
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-04: Cross-Domain Solution Compliance]
IF network_classification_source = "SECRET"
AND network_classification_destination = "UNCLASSIFIED"
AND ia_solution_type = "cross_domain"
AND nsa_csfc_approved = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Deployment Exception]
IF deployment_urgency = "emergency"
AND temporary_approval_obtained = TRUE
AND approval_duration < 30_days
AND permanent_approval_in_progress = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Employ only NSA-approved GOTS/COTS IA products | [RULE-01] |
| Ensure products are NSA evaluated/validated | [RULE-02] |
| Implement NSA-approved key management | [RULE-03] |
| Maintain current approval documentation | [RULE-04] |
| Verify CSfC compliance when applicable | [RULE-05] |