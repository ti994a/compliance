# POLICY: SA-4.7: NIAP-approved Protection Profiles

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.7 |
| NIST Control | SA-4.7: NIAP-approved Protection Profiles |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | NIAP, protection profiles, FIPS validation, cryptographic modules, information assurance, procurement |

## 1. POLICY STATEMENT
The organization SHALL limit the use of commercially provided information assurance and information technology products to those evaluated against NIAP-approved Protection Profiles when available. Products relying on cryptographic functionality without NIAP profiles MUST use FIPS-validated or NSA-approved cryptographic modules.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Commercial IA Products | YES | All commercially procured information assurance products |
| IT Products with Security Functions | YES | Products enforcing security policies through cryptographic means |
| Custom Developed Solutions | NO | Internal development not using commercial IA components |
| Open Source Security Tools | CONDITIONAL | If used for information assurance functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Verify NIAP evaluation status before purchase<br>• Validate FIPS certification for cryptographic products<br>• Maintain approved product inventory |
| Security Architect | • Determine when NIAP profiles apply to technology types<br>• Assess cryptographic functionality requirements<br>• Review product security policies |
| IT Asset Manager | • Track NIAP evaluation status of deployed products<br>• Monitor FIPS validation expiration dates<br>• Report non-compliant products |

## 4. RULES
[RULE-01] Commercial information assurance products MUST be successfully evaluated against applicable NIAP-approved Protection Profiles when such profiles exist for the technology type.
[VALIDATION] IF product_category = "information_assurance" AND niap_profile_exists = TRUE AND niap_evaluation_status != "successfully_evaluated" THEN violation

[RULE-02] Commercial IT products without applicable NIAP profiles that rely on cryptographic functionality MUST use FIPS-validated or NSA-approved cryptographic modules.
[VALIDATION] IF niap_profile_exists = FALSE AND uses_cryptography = TRUE AND (fips_validated = FALSE AND nsa_approved = FALSE) THEN violation

[RULE-03] Organizations MUST maintain current inventory of NIAP evaluation status and FIPS validation for all covered products.
[VALIDATION] IF product_in_scope = TRUE AND (niap_status_documented = FALSE OR fips_status_documented = FALSE) THEN violation

[RULE-04] FIPS validation certificates MUST be current and not expired for products relying on cryptographic modules.
[VALIDATION] IF fips_validated = TRUE AND fips_certificate_expired = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] NIAP Profile Verification - Process to check NIAP Common Criteria Evaluation and Validation Scheme before procurement
- [PROC-02] FIPS Validation Confirmation - Procedure to verify cryptographic module validation through NIST CMVP
- [PROC-03] Product Inventory Maintenance - Regular review and update of protection profile and validation status

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New NIAP profiles published, FIPS validations expired, major technology procurements

## 7. SCENARIO PATTERNS
[SCENARIO-01: Firewall Procurement]
IF product_type = "network_firewall"
AND niap_protection_profile_exists = TRUE
AND niap_evaluation_status = "not_evaluated"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: VPN Without NIAP Profile]
IF product_type = "vpn_solution"
AND niap_protection_profile_exists = FALSE
AND uses_cryptographic_functions = TRUE
AND fips_validated = TRUE
THEN compliance = TRUE

[SCENARIO-03: Database Encryption Product]
IF product_category = "information_assurance"
AND uses_cryptography = TRUE
AND niap_profile_exists = FALSE
AND fips_validated = FALSE
AND nsa_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Legacy Product with Expired FIPS]
IF product_deployed = TRUE
AND fips_validation_required = TRUE
AND fips_certificate_expiration < current_date
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Open Source Security Tool]
IF product_type = "open_source"
AND information_assurance_function = TRUE
AND commercial_support = TRUE
AND niap_evaluation_status = "not_applicable"
THEN compliance = CONDITIONAL
required_action = "Evaluate cryptographic requirements"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Products evaluated against NIAP-approved Protection Profiles when available | [RULE-01] |
| FIPS-validated or NSA-approved cryptographic modules when no NIAP profile exists | [RULE-02] |
| Documentation and tracking of evaluation/validation status | [RULE-03] |
| Current FIPS validation certificates | [RULE-04] |