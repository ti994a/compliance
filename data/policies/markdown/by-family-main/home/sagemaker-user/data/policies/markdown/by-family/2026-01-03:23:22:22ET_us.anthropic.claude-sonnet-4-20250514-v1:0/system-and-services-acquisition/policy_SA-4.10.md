# POLICY: SA-4.10: Use of Approved PIV Products

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.10 |
| NIST Control | SA-4.10: Use of Approved PIV Products |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | PIV, FIPS201, identity verification, multi-factor authentication, approved products |

## 1. POLICY STATEMENT
The organization SHALL employ only information technology products that appear on the FIPS 201-approved products list for Personal Identity Verification (PIV) capability implemented within organizational systems. All PIV-related procurements and implementations MUST comply with NIST FIPS 201 requirements for federal employee and contractor identity verification.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems requiring PIV | YES | Federal and contractor systems |
| PIV card readers | YES | Must be FIPS 201-approved |
| PIV middleware software | YES | Must be FIPS 201-approved |
| Authentication systems | YES | When implementing PIV capability |
| Third-party services | YES | When PIV integration required |
| Legacy systems | CONDITIONAL | Must comply when PIV capability added |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Maintain approved PIV products list<br>• Oversee PIV compliance program<br>• Approve PIV implementation exceptions |
| Procurement Officer | • Verify FIPS 201 approval before purchase<br>• Include PIV requirements in contracts<br>• Maintain procurement documentation |
| System Administrator | • Implement only approved PIV products<br>• Configure PIV systems per NIST guidelines<br>• Monitor PIV system compliance |

## 4. RULES
[RULE-01] All PIV-capable IT products procured or implemented MUST appear on the current FIPS 201-approved products list maintained by NIST.
[VALIDATION] IF piv_product_implemented = TRUE AND fips201_approved_list_status = FALSE THEN critical_violation

[RULE-02] Procurement personnel MUST verify FIPS 201 approval status before purchasing any PIV-related technology products.
[VALIDATION] IF procurement_type = "piv_related" AND fips201_verification_completed = FALSE THEN violation

[RULE-03] System administrators SHALL NOT deploy PIV products that are not on the FIPS 201-approved products list.
[VALIDATION] IF piv_product_deployed = TRUE AND fips201_approved = FALSE THEN critical_violation

[RULE-04] The approved PIV products list MUST be reviewed and updated within 30 days of any NIST FIPS 201 list updates.
[VALIDATION] IF nist_list_update_date > internal_list_update_date + 30_days THEN violation

[RULE-05] All PIV implementation contracts MUST include FIPS 201 compliance requirements and approved products list references.
[VALIDATION] IF contract_type = "piv_implementation" AND fips201_requirements_included = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PIV Product Verification - Validate FIPS 201 approval before procurement
- [PROC-02] Approved Products List Management - Maintain current NIST FIPS 201 list
- [PROC-03] PIV Deployment Validation - Verify compliance before system deployment
- [PROC-04] Contract Review Process - Ensure FIPS 201 requirements in PIV contracts
- [PROC-05] Exception Management - Document and approve any temporary deviations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: NIST FIPS 201 list updates, PIV security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved PIV Reader Deployment]
IF device_type = "piv_card_reader"
AND fips201_approved = FALSE
AND deployed_in_production = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Legacy System PIV Integration]
IF system_type = "legacy"
AND piv_capability_required = TRUE
AND approved_products_used = TRUE
THEN compliance = TRUE

[SCENARIO-03: Emergency PIV Product Procurement]
IF procurement_urgency = "emergency"
AND fips201_verification_bypassed = TRUE
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Third-Party PIV Service]
IF service_type = "third_party_piv"
AND vendor_uses_approved_products = TRUE
AND contract_includes_fips201_requirements = TRUE
THEN compliance = TRUE

[SCENARIO-05: Outdated Approved Products List]
IF internal_piv_list_age > 30_days
AND nist_list_updated = TRUE
AND products_deployed_from_outdated_list = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Only FIPS 201-approved products employed | [RULE-01], [RULE-03] |
| Procurement verification process | [RULE-02] |
| Current approved products list maintenance | [RULE-04] |
| Contract compliance requirements | [RULE-05] |