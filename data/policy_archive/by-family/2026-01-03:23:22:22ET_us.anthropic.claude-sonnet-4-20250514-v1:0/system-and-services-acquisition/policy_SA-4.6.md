```markdown
# POLICY: SA-4.6: Use of Information Assurance Products

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.6 |
| NIST Control | SA-4.6: Use of Information Assurance Products |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | information assurance, NSA-approved, classified information, COTS, GOTS, cryptographic protection |

## 1. POLICY STATEMENT
The organization SHALL employ only NSA-approved government off-the-shelf (GOTS) or commercial off-the-shelf (COTS) information assurance products to protect classified information transmitted over networks at lower classification levels. All information assurance products MUST be evaluated and validated by NSA or through NSA-approved procedures before deployment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified Information Systems | YES | All systems processing classified data |
| Cross-Domain Solutions | YES | Systems bridging classification levels |
| Cryptographic Products | YES | Products protecting classified information |
| Commercial IA Products | CONDITIONAL | Only if NSA-approved |
| Development/Test Systems | YES | If processing classified information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Maintain NSA-approved product list<br>• Approve IA product acquisitions<br>• Ensure compliance with NSA validation requirements |
| Acquisition Manager | • Verify NSA approval before procurement<br>• Include IA requirements in contracts<br>• Maintain acquisition documentation |
| System Administrator | • Deploy only approved IA products<br>• Implement NSA-approved configurations<br>• Monitor product compliance status |

## 4. RULES
[RULE-01] Organizations MUST employ only GOTS or COTS information assurance products that appear on the current NSA-approved solutions list when protecting classified information on lower classification networks.
[VALIDATION] IF product_type = "information_assurance" AND classified_data = TRUE AND network_level < data_classification AND nsa_approved = FALSE THEN critical_violation

[RULE-02] All information assurance products MUST be evaluated and validated by NSA or through NSA-approved procedures before deployment in classified environments.
[VALIDATION] IF ia_product_deployed = TRUE AND (nsa_evaluated = FALSE AND nsa_approved_procedure_validated = FALSE) THEN critical_violation

[RULE-03] Commercial IA products using cryptographic means MUST implement NSA-approved key management when protecting classified information.
[VALIDATION] IF product_type = "commercial_ia" AND cryptographic_protection = TRUE AND classified_data = TRUE AND nsa_approved_key_mgmt = FALSE THEN critical_violation

[RULE-04] Organizations SHALL maintain current documentation of all deployed IA products and their NSA approval status.
[VALIDATION] IF ia_product_inventory_current = FALSE OR nsa_approval_documentation = FALSE THEN moderate_violation

[RULE-05] IA product approvals MUST be revalidated when NSA approval lists are updated or products reach end-of-support.
[VALIDATION] IF nsa_list_updated = TRUE AND product_revalidation_complete = FALSE AND days_since_update > 30 THEN moderate_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] NSA Product Approval Verification - Process for validating products against current NSA-approved lists
- [PROC-02] IA Product Acquisition Review - Mandatory security review before procurement
- [PROC-03] Product Validation Documentation - Maintaining evidence of NSA evaluation/validation
- [PROC-04] Cross-Domain Solution Certification - Specialized approval process for CDS products

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: NSA list updates, new classified system deployments, security incidents involving IA products

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Commercial IA Product]
IF product_type = "commercial_ia"
AND classified_data_protection = TRUE
AND nsa_approved_list_status = FALSE
AND deployment_status = "active"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Expired NSA Validation]
IF ia_product_deployed = TRUE
AND nsa_validation_date < (current_date - 3_years)
AND revalidation_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Key Management Approval]
IF product_function = "cryptographic_protection"
AND classified_information = TRUE
AND nsa_key_management_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Proper NSA-Approved Deployment]
IF product_type IN ["GOTS", "COTS"]
AND nsa_approved_solution = TRUE
AND current_validation = TRUE
AND proper_configuration = TRUE
THEN compliance = TRUE

[SCENARIO-05: Cross-Domain Solution Validation]
IF system_type = "cross_domain_solution"
AND classification_levels_bridged = TRUE
AND nsa_evaluated = TRUE
AND current_approval_status = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Employ only NSA-approved GOTS/COTS IA products | [RULE-01] |
| Products evaluated/validated by NSA or approved procedures | [RULE-02] |
| NSA-approved key management for cryptographic products | [RULE-03] |
| Maintain current IA product documentation | [RULE-04] |
| Revalidate products per NSA updates | [RULE-05] |
```