# POLICY: SA-4.10: Use of Approved PIV Products

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.10 |
| NIST Control | SA-4.10: Use of Approved PIV Products |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | PIV, FIPS 201, approved products, personal identity verification, multi-factor authentication, procurement |

## 1. POLICY STATEMENT
The organization SHALL employ only information technology products that appear on the FIPS 201-approved products list for Personal Identity Verification (PIV) capability implemented within organizational systems. All PIV-related procurements and implementations MUST comply with NIST requirements for federal employee and contractor identity verification.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems requiring PIV capability | YES | Federal and contractor systems |
| PIV card readers and hardware | YES | Must be FIPS 201-approved |
| PIV middleware and software | YES | Must support approved products |
| Legacy authentication systems | CONDITIONAL | If implementing PIV capability |
| Third-party contractor systems | YES | When accessing organizational resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Maintain current FIPS 201-approved products list<br>• Approve PIV implementation standards<br>• Oversee compliance monitoring |
| Procurement Officer | • Verify products against FIPS 201-approved list<br>• Include PIV requirements in acquisition contracts<br>• Reject non-compliant product requests |
| System Owners | • Implement only approved PIV products<br>• Document PIV capability in system security plans<br>• Coordinate with identity management teams |

## 4. RULES
[RULE-01] All PIV-related IT products MUST be verified against the current FIPS 201-approved products list before procurement or implementation.
[VALIDATION] IF piv_product_procured = TRUE AND fips_201_approved_status = FALSE THEN critical_violation

[RULE-02] The FIPS 201-approved products list MUST be updated within 30 days of NIST publishing revisions.
[VALIDATION] IF nist_list_update_date > organization_list_update_date + 30_days THEN violation

[RULE-03] PIV capability implementations SHALL NOT use products that have been removed from the FIPS 201-approved products list.
[VALIDATION] IF product_removed_from_list = TRUE AND product_still_deployed = TRUE THEN critical_violation

[RULE-04] All acquisition contracts for PIV-related products MUST include FIPS 201 compliance requirements and verification clauses.
[VALIDATION] IF contract_type = "piv_related" AND fips_201_clause_included = FALSE THEN violation

[RULE-05] System security plans MUST document all implemented PIV products and their FIPS 201 approval status.
[VALIDATION] IF piv_products_deployed = TRUE AND ssp_documentation_complete = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PIV Product Verification - Validate products against FIPS 201-approved list before procurement
- [PROC-02] Approved Products List Management - Maintain current FIPS 201-approved products database
- [PROC-03] Contract Review Process - Ensure PIV procurement contracts include compliance requirements
- [PROC-04] Legacy System Assessment - Evaluate existing PIV implementations for compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: NIST FIPS 201-approved list updates, failed compliance assessments, security incidents involving PIV systems

## 7. SCENARIO PATTERNS
[SCENARIO-01: Emergency PIV Product Procurement]
IF procurement_urgency = "emergency"
AND fips_201_verification_bypassed = TRUE
AND temporary_approval_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Legacy PIV System with Removed Product]
IF piv_system_age > 2_years
AND product_approval_status = "removed_from_list"
AND remediation_plan_exists = TRUE
AND remediation_timeline <= 90_days
THEN compliance = TRUE

[SCENARIO-03: Contractor PIV Implementation]
IF system_operator = "contractor"
AND piv_products_used = TRUE
AND fips_201_compliance_verified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Multi-Factor Authentication Alternative]
IF system_requires_mfa = TRUE
AND piv_capability_implemented = FALSE
AND alternative_auth_method = "non_piv"
AND risk_acceptance_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: PIV Product End-of-Life]
IF product_eol_announced = TRUE
AND replacement_timeline > 180_days
AND continued_fips_201_approval = TRUE
AND migration_plan_approved = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Only FIPS 201-approved products employed for PIV capability | RULE-01, RULE-03 |
| Current approved products list maintained | RULE-02 |
| Procurement process ensures compliance | RULE-04 |
| PIV implementations documented in security plans | RULE-05 |