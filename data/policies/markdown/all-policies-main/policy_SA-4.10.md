# POLICY: SA-4.10: Use of Approved PIV Products

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.10 |
| NIST Control | SA-4.10: Use of Approved PIV Products |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | PIV, FIPS-201, approved-products, authentication, acquisition, procurement |

## 1. POLICY STATEMENT
The organization SHALL employ only information technology products that appear on the FIPS 201-approved products list for Personal Identity Verification (PIV) capability implemented within organizational systems. All PIV-related procurements and implementations MUST be validated against the current FIPS 201-approved products list before deployment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Systems requiring PIV authentication |
| PIV card readers | YES | Hardware components for PIV authentication |
| PIV middleware/software | YES | Software enabling PIV functionality |
| Third-party PIV products | YES | Must be FIPS 201-approved |
| Legacy authentication systems | CONDITIONAL | Only if implementing new PIV capability |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Verify FIPS 201 approval status before purchase<br>• Maintain approved vendor lists<br>• Document compliance in acquisition records |
| System Administrator | • Deploy only approved PIV products<br>• Validate product approval status during implementation<br>• Report non-compliant products immediately |
| CISO | • Maintain current FIPS 201-approved products list<br>• Approve exceptions and document rationale<br>• Conduct periodic compliance reviews |

## 4. RULES

[RULE-01] All PIV-related IT products MUST be verified against the current FIPS 201-approved products list before procurement approval.
[VALIDATION] IF product_category = "PIV" AND fips_201_approved = FALSE THEN procurement_violation

[RULE-02] Organizations SHALL maintain an up-to-date copy of the FIPS 201-approved products list and review it quarterly for updates.
[VALIDATION] IF approved_products_list_age > 90_days THEN compliance_violation

[RULE-03] PIV products already deployed MUST be validated against the approved list during annual system reviews and immediately when list updates occur.
[VALIDATION] IF deployed_piv_product NOT IN current_approved_list THEN remediation_required

[RULE-04] Non-approved PIV products SHALL NOT be implemented in organizational systems under any circumstances without formal CISO exception approval.
[VALIDATION] IF piv_product_deployed = TRUE AND fips_201_approved = FALSE AND ciso_exception = FALSE THEN critical_violation

[RULE-05] All PIV product procurement documentation MUST include evidence of FIPS 201 approval status verification.
[VALIDATION] IF procurement_type = "PIV" AND fips_201_verification_documented = FALSE THEN documentation_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PIV Product Verification - Process for validating FIPS 201 approval status
- [PROC-02] Approved Products List Management - Quarterly review and update process
- [PROC-03] Non-Compliant Product Remediation - Process for addressing unapproved products
- [PROC-04] Exception Request Process - Formal approval process for emergency exceptions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: FIPS 201 list updates, failed compliance audits, security incidents involving PIV

## 7. SCENARIO PATTERNS

[SCENARIO-01: Emergency PIV Reader Purchase]
IF procurement_urgency = "emergency"
AND product_type = "PIV_reader"
AND fips_201_verification_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved PIV Product Deployment]
IF product_type = "PIV_middleware"
AND fips_201_approved = TRUE
AND verification_documented = TRUE
THEN compliance = TRUE

[SCENARIO-03: Legacy Product Discovery]
IF system_review = "annual"
AND piv_product_found = TRUE
AND product_on_approved_list = FALSE
AND discovery_date > list_last_updated
THEN compliance = FALSE, remediation_required = TRUE
violation_severity = "Moderate"

[SCENARIO-04: Quarterly List Update Check]
IF current_date - last_list_check > 90_days
AND piv_products_in_use = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Exception Approved Product]
IF piv_product_deployed = TRUE
AND fips_201_approved = FALSE
AND ciso_exception_approved = TRUE
AND exception_documentation_complete = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Employ only FIPS 201-approved PIV products | [RULE-01], [RULE-04] |
| Maintain current approved products list | [RULE-02] |
| Validate deployed products against approved list | [RULE-03] |
| Document approval verification in procurement | [RULE-05] |