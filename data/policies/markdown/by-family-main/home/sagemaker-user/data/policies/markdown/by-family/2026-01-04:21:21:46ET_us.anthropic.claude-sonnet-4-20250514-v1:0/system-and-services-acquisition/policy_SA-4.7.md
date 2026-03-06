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
The organization SHALL limit procurement of commercially provided information assurance and information technology products to those evaluated against NIAP-approved Protection Profiles when such profiles exist. Products without applicable NIAP profiles that rely on cryptographic functionality MUST use FIPS-validated or NSA-approved cryptographic modules.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Commercial IA products | YES | All information assurance products |
| IA-enabled IT products | YES | Products with security enforcement functions |
| Cryptographic products | YES | Products using crypto for security policy |
| Internal development | NO | Only commercially provided products |
| Open source products | CONDITIONAL | If used for IA functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Verify NIAP evaluation status before purchase<br>• Maintain approved product inventory<br>• Coordinate with security team on evaluations |
| CISO | • Define IA product categories requiring NIAP evaluation<br>• Approve exceptions with documented justification<br>• Oversee compliance monitoring |
| Security Architect | • Validate Protection Profile applicability<br>• Verify FIPS validation status<br>• Review cryptographic module compliance |

## 4. RULES
[RULE-01] Commercial IA products MUST be evaluated against applicable NIAP-approved Protection Profiles before procurement approval.
[VALIDATION] IF product_type = "information_assurance" AND niap_profile_exists = TRUE AND niap_evaluation_status ≠ "successfully_evaluated" THEN violation

[RULE-02] IA-enabled IT products MUST use NIAP-evaluated components when Protection Profiles exist for the specific technology type.
[VALIDATION] IF product_category = "ia_enabled_it" AND applicable_niap_profile = TRUE AND evaluation_status = "none" THEN violation

[RULE-03] Products without applicable NIAP profiles that rely on cryptographic functionality MUST use FIPS-validated or NSA-approved cryptographic modules.
[VALIDATION] IF niap_profile_exists = FALSE AND uses_cryptography = TRUE AND (fips_validated = FALSE AND nsa_approved = FALSE) THEN violation

[RULE-04] Exception requests for non-NIAP evaluated products MUST include documented risk assessment and compensating controls.
[VALIDATION] IF compliance_exception = TRUE AND (risk_assessment_documented = FALSE OR compensating_controls = FALSE) THEN violation

[RULE-05] Procurement documentation MUST include verification of NIAP evaluation status or FIPS validation before contract execution.
[VALIDATION] IF contract_status = "executed" AND (niap_verification_documented = FALSE AND fips_verification_documented = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] NIAP Evaluation Verification - Process for confirming product evaluation status against applicable Protection Profiles
- [PROC-02] FIPS Validation Confirmation - Procedure for verifying cryptographic module FIPS validation or NSA approval
- [PROC-03] Exception Request Process - Workflow for documenting and approving non-compliant product acquisitions
- [PROC-04] Vendor Assessment - Process for evaluating vendor compliance with NIAP/FIPS requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New NIAP Protection Profiles published, FIPS standard updates, significant procurement policy changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Firewall Procurement]
IF product_type = "network_firewall"
AND niap_protection_profile_exists = TRUE
AND vendor_evaluation_status = "not_evaluated"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: VPN Solution with Crypto]
IF product_type = "vpn_solution"
AND niap_protection_profile_exists = FALSE
AND uses_cryptographic_modules = TRUE
AND fips_validation_status = "validated"
THEN compliance = TRUE

[SCENARIO-03: Database Encryption Tool]
IF product_category = "database_security"
AND niap_profile_applicable = FALSE
AND cryptographic_enforcement = TRUE
AND fips_validated = FALSE
AND nsa_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Emergency Procurement Exception]
IF procurement_type = "emergency"
AND niap_compliant = FALSE
AND exception_documented = TRUE
AND risk_assessment_completed = TRUE
AND compensating_controls_implemented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Legacy System Crypto Module]
IF system_type = "legacy"
AND cryptographic_module_age > 3_years
AND current_fips_validation = FALSE
AND upgrade_plan_documented = TRUE
AND timeline < 12_months
THEN compliance = CONDITIONAL

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Limit IA products to NIAP-evaluated when profiles exist | [RULE-01], [RULE-02] |
| Require FIPS-validated crypto when no NIAP profile exists | [RULE-03] |
| Document procurement verification process | [RULE-05] |
| Maintain exception documentation | [RULE-04] |