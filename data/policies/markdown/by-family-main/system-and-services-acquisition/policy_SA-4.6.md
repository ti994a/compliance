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
The organization SHALL employ only NSA-approved government off-the-shelf (GOTS) or commercial off-the-shelf (COTS) information assurance products to protect classified information transmitted over networks at lower classification levels. All information assurance products MUST be evaluated and validated by NSA or through NSA-approved procedures before deployment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified Information Systems | YES | All systems processing classified data |
| Cross-Domain Solutions | YES | Systems bridging classification levels |
| Cryptographic Products | YES | Products protecting classified information |
| Commercial Networks | YES | When transmitting classified data |
| Development Systems | CONDITIONAL | Only if processing classified information |
| Unclassified Systems | NO | Unless handling classified data transmission |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve information assurance product selections<br>• Ensure NSA validation requirements are met<br>• Maintain approved product inventory |
| Security Architecture Team | • Validate NSA approval status of products<br>• Design solutions using approved components<br>• Maintain technical evaluation documentation |
| Procurement Team | • Verify NSA approval before purchase<br>• Include security requirements in contracts<br>• Coordinate with security team on product selection |

## 4. RULES
[RULE-01] Organizations MUST employ only GOTS or COTS information assurance products that compose an NSA-approved solution when protecting classified information transmitted over lower classification networks.
[VALIDATION] IF classified_data_transmission = TRUE AND network_classification < data_classification AND product_nsa_approved = FALSE THEN critical_violation

[RULE-02] All information assurance products SHALL be evaluated and validated by NSA or through NSA-approved procedures before deployment.
[VALIDATION] IF product_deployed = TRUE AND (nsa_evaluated = FALSE AND nsa_approved_procedure_validated = FALSE) THEN critical_violation

[RULE-03] Cryptographic products used for classified information protection MUST use NSA-approved key management when required.
[VALIDATION] IF product_type = "cryptographic" AND classified_protection = TRUE AND nsa_approved_key_mgmt = FALSE THEN critical_violation

[RULE-04] Organizations SHALL maintain an inventory of all deployed NSA-approved information assurance products with current validation status.
[VALIDATION] IF ia_product_deployed = TRUE AND inventory_record_exists = FALSE THEN moderate_violation

[RULE-05] Product validation status MUST be verified annually and upon any product updates or configuration changes.
[VALIDATION] IF last_validation_check > 365_days OR (product_updated = TRUE AND post_update_validation = FALSE) THEN moderate_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] NSA Product Approval Verification - Process for validating NSA approval status before procurement
- [PROC-02] Information Assurance Product Inventory Management - Maintaining current inventory of approved products
- [PROC-03] Cross-Domain Solution Validation - Specific procedures for validating cross-classification transmission solutions
- [PROC-04] Annual Validation Review - Process for conducting annual validation status reviews

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: NSA guidance updates, product security incidents, new classified system deployments, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Cryptographic Product]
IF product_type = "cryptographic"
AND classified_data_protection = TRUE
AND nsa_approved = FALSE
AND deployed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Outdated Validation Status]
IF ia_product_deployed = TRUE
AND last_nsa_validation > 365_days
AND validation_extension_granted = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Cross-Domain Transmission Without Approval]
IF data_classification = "SECRET"
AND network_classification = "UNCLASSIFIED"
AND transmission_solution_nsa_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Compliant Approved Product Usage]
IF product_nsa_approved = TRUE
AND validation_current = TRUE
AND proper_classification_handling = TRUE
AND inventory_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Deployment Exception]
IF emergency_deployment = TRUE
AND temporary_authorization_documented = TRUE
AND validation_timeline_established = TRUE
AND timeline < 30_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Employ only NSA-approved GOTS/COTS IA products for classified information protection | [RULE-01] |
| Ensure products are evaluated/validated by NSA or NSA-approved procedures | [RULE-02] |
| Use NSA-approved key management for cryptographic products | [RULE-03] |
| Maintain inventory of deployed IA products | [RULE-04] |
| Conduct regular validation status reviews | [RULE-05] |