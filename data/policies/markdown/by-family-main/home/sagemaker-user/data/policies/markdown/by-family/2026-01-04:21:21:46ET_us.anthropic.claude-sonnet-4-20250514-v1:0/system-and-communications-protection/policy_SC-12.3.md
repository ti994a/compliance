# POLICY: SC-12.3: Asymmetric Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12.3 |
| NIST Control | SC-12.3: Asymmetric Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | asymmetric keys, NSA-approved, key management, cryptographic keys, PKI, distribution, production, control |

## 1. POLICY STATEMENT
All asymmetric cryptographic keys used within organizational systems MUST be produced, controlled, and distributed exclusively using NSA-approved key management technology and processes. This requirement ensures cryptographic operations meet federal security standards and maintain appropriate key lifecycle security.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, hybrid, and on-premises |
| Third-party services | YES | When processing organizational data |
| Development environments | YES | When using production-equivalent crypto |
| Test environments | CONDITIONAL | Only if using real cryptographic keys |
| Personal devices | YES | When accessing organizational systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve NSA-approved key management technologies<br>• Oversee policy compliance<br>• Authorize exceptions |
| Cryptographic Officer | • Maintain list of approved technologies<br>• Validate key management processes<br>• Monitor key lifecycle operations |
| System Administrators | • Implement approved key management solutions<br>• Execute key generation and distribution<br>• Maintain key management documentation |
| Security Engineers | • Configure cryptographic systems<br>• Validate NSA-approval status<br>• Implement technical controls |

## 4. RULES
[RULE-01] All asymmetric cryptographic key production MUST use only NSA-approved key management technology and processes as listed in the approved cryptographic products list.
[VALIDATION] IF key_generation_technology NOT IN nsa_approved_list THEN violation

[RULE-02] Asymmetric cryptographic key control operations SHALL be performed exclusively through NSA-approved key management systems with documented processes.
[VALIDATION] IF key_control_system NOT IN nsa_approved_list OR process_documented = FALSE THEN violation

[RULE-03] Distribution of asymmetric cryptographic keys MUST occur only through NSA-approved distribution mechanisms and follow established secure distribution processes.
[VALIDATION] IF key_distribution_method NOT IN nsa_approved_methods THEN violation

[RULE-04] Organizations SHALL maintain an inventory of all NSA-approved cryptographic products and key management technologies in use.
[VALIDATION] IF cryptographic_inventory_updated > 90_days THEN violation

[RULE-05] PKI certificates used for asymmetric key operations MUST be Class 3 or Class 4 certificates from approved certificate authorities.
[VALIDATION] IF pki_certificate_class < 3 OR ca_approved = FALSE THEN violation

[RULE-06] Non-NSA-approved asymmetric key management technologies MUST NOT be deployed in production environments without documented CISO exception.
[VALIDATION] IF technology_nsa_approved = FALSE AND ciso_exception_documented = FALSE AND environment = "production" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] NSA Technology Validation - Process for verifying and maintaining NSA-approved technology list
- [PROC-02] Asymmetric Key Generation - Standardized procedures for producing cryptographic keys
- [PROC-03] Key Distribution Management - Secure processes for distributing asymmetric keys
- [PROC-04] Key Lifecycle Control - Procedures for managing keys throughout their operational lifecycle
- [PROC-05] Exception Management - Process for documenting and approving deviations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New NSA guidance, security incidents, technology changes, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Key Generation Tool]
IF key_generation_tool NOT IN nsa_approved_list
AND environment = "production"
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Legacy PKI Certificate Usage]
IF pki_certificate_class < 3
AND certificate_usage = "active"
AND migration_plan_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Third-Party Key Management Service]
IF service_provider_type = "third_party"
AND key_management_technology NOT IN nsa_approved_list
AND due_diligence_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Development Environment Exception]
IF environment = "development"
AND key_management_nsa_approved = FALSE
AND production_equivalent_crypto = TRUE
AND risk_assessment_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Approved Technology with Outdated Process]
IF key_management_technology IN nsa_approved_list
AND process_documented = TRUE
AND process_last_updated > 365_days
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Asymmetric cryptographic keys are produced using NSA-approved key management technology and processes | [RULE-01], [RULE-04] |
| Asymmetric cryptographic keys are controlled using NSA-approved key management technology and processes | [RULE-02], [RULE-04] |
| Asymmetric cryptographic keys are distributed using NSA-approved key management technology and processes | [RULE-03], [RULE-05] |