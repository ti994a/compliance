# POLICY: SA-4.7: NIAP-approved Protection Profiles

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.7 |
| NIST Control | SA-4.7: NIAP-approved Protection Profiles |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | NIAP, protection profiles, FIPS validation, NSA approval, cryptographic modules, information assurance |

## 1. POLICY STATEMENT
The organization SHALL limit commercially provided information assurance and information technology products to those evaluated against NIAP-approved Protection Profiles when such profiles exist. For products without applicable NIAP profiles that rely on cryptographic functionality, cryptographic modules MUST be FIPS-validated or NSA-approved.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Commercial IT Products | YES | Information assurance and IA-enabled products |
| Cryptographic Modules | YES | When no NIAP profile exists |
| Custom Developed Software | NO | Only commercial products covered |
| Open Source Products | CONDITIONAL | If commercially provided/supported |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Manager | • Verify NIAP evaluation status before purchase<br>• Maintain approved product registry<br>• Coordinate with security team on product validation |
| Security Architect | • Identify applicable NIAP Protection Profiles<br>• Validate FIPS/NSA approval status<br>• Assess cryptographic functionality requirements |
| Vendor Management | • Obtain validation documentation from vendors<br>• Maintain current certification status records |

## 4. RULES
[RULE-01] Commercial information assurance products MUST be evaluated against applicable NIAP-approved Protection Profiles when such profiles exist for the specific technology type.
[VALIDATION] IF product_type = "information_assurance" AND niap_profile_exists = TRUE AND niap_evaluation_status != "successfully_evaluated" THEN violation

[RULE-02] Commercial IT products without applicable NIAP Protection Profiles that rely on cryptographic functionality MUST use FIPS-validated or NSA-approved cryptographic modules.
[VALIDATION] IF niap_profile_exists = FALSE AND uses_cryptography = TRUE AND (fips_validated = FALSE AND nsa_approved = FALSE) THEN violation

[RULE-03] Organizations MUST verify and document NIAP evaluation status or FIPS/NSA approval before procurement of covered products.
[VALIDATION] IF procurement_approved = TRUE AND (niap_verification_documented = FALSE AND crypto_validation_documented = FALSE) THEN violation

[RULE-04] Product validation status MUST be re-verified annually and when products are updated or replaced.
[VALIDATION] IF last_validation_check > 365_days OR product_version_changed = TRUE AND validation_reverified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] NIAP Protection Profile Verification - Process for identifying and validating applicable protection profiles
- [PROC-02] FIPS/NSA Cryptographic Module Validation - Procedure for verifying cryptographic module certifications
- [PROC-03] Approved Product Registry Maintenance - Maintaining current list of validated products
- [PROC-04] Vendor Certification Documentation - Process for obtaining and validating vendor certification evidence

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New NIAP profiles published, FIPS validation updates, major product acquisitions

## 7. SCENARIO PATTERNS
[SCENARIO-01: Firewall Procurement]
IF product_type = "network_firewall"
AND niap_profile_exists = TRUE
AND vendor_niap_evaluation = "not_evaluated"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: VPN Solution with Crypto]
IF product_type = "vpn_solution"
AND niap_profile_exists = FALSE
AND uses_cryptography = TRUE
AND fips_validated = TRUE
THEN compliance = TRUE

[SCENARIO-03: Legacy Product Exception]
IF product_deployment_date < "2020-01-01"
AND niap_profile_published_date > product_deployment_date
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Updated Product Version]
IF product_version_changed = TRUE
AND validation_status = "previous_version_only"
AND reverification_completed = FALSE
AND days_since_update > 90
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Crypto Module Without Validation]
IF product_category = "encryption_software"
AND niap_profile_exists = FALSE
AND cryptographic_module_validated = FALSE
AND nsa_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Limit products to NIAP-evaluated when profiles exist | [RULE-01] |
| Require FIPS/NSA validation for crypto modules | [RULE-02] |
| Document validation status before procurement | [RULE-03] |
| Maintain current validation status | [RULE-04] |