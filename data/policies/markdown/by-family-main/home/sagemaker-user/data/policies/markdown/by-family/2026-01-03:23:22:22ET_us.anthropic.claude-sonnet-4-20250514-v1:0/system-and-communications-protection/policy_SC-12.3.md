```markdown
# POLICY: SC-12.3: Asymmetric Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12.3 |
| NIST Control | SC-12.3: Asymmetric Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | asymmetric cryptography, NSA-approved, key management, PKI, cryptographic keys |

## 1. POLICY STATEMENT
All asymmetric cryptographic keys used within the organization MUST be produced, controlled, and distributed using NSA-approved key management technology and processes. This policy ensures cryptographic operations meet federal security standards for protecting sensitive information.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, hybrid, and on-premises |
| Third-party services | YES | When handling organizational data |
| Development environments | YES | When using production-like cryptography |
| Test environments | CONDITIONAL | Only if using real cryptographic keys |
| Personal devices | YES | When accessing organizational systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve NSA-approved key management technologies<br>• Oversee policy compliance<br>• Authorize exceptions |
| Cryptographic Officer | • Maintain list of approved technologies<br>• Validate key management processes<br>• Monitor compliance |
| System Administrators | • Implement approved key management solutions<br>• Configure systems per approved processes<br>• Report compliance issues |
| Security Engineers | • Design cryptographic implementations<br>• Validate technical compliance<br>• Conduct security assessments |

## 4. RULES
[RULE-01] All asymmetric cryptographic key production MUST use NSA-approved key management technology exclusively.
[VALIDATION] IF key_production_technology NOT IN nsa_approved_list THEN violation

[RULE-02] Asymmetric cryptographic key control mechanisms MUST implement NSA-approved processes for key lifecycle management.
[VALIDATION] IF key_control_process NOT IN nsa_approved_processes THEN violation

[RULE-03] Distribution of asymmetric cryptographic keys MUST occur only through NSA-approved key distribution methods.
[VALIDATION] IF key_distribution_method NOT IN nsa_approved_distribution THEN violation

[RULE-04] Organizations MUST maintain current documentation of all NSA-approved key management technologies in use.
[VALIDATION] IF nsa_approved_inventory_age > 90_days THEN violation

[RULE-05] Non-NSA-approved cryptographic key management technologies SHALL NOT be used for asymmetric key operations.
[VALIDATION] IF unapproved_technology_detected = TRUE THEN critical_violation

[RULE-06] All asymmetric key management implementations MUST be validated against NSA-approved standards before deployment.
[VALIDATION] IF nsa_validation_completed = FALSE AND deployment_status = "active" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] NSA Technology Approval Process - Validate and approve key management technologies
- [PROC-02] Key Lifecycle Management - Define production, control, and distribution procedures
- [PROC-03] Compliance Monitoring - Regular assessment of key management implementations
- [PROC-04] Exception Management - Handle temporary deviations with risk assessment

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: NSA guidance updates, security incidents, technology changes, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Key Generation]
IF key_generation_technology = "non_nsa_approved"
AND system_classification = "federal"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Legacy Key Management System]
IF key_management_system_age > 5_years
AND nsa_approval_status = "deprecated"
AND migration_plan = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Third-Party Key Distribution]
IF key_distribution_vendor NOT IN nsa_approved_vendors
AND data_classification >= "sensitive"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Emergency Key Operations]
IF emergency_key_generation = TRUE
AND nsa_approved_process = FALSE
AND duration > 72_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant PKI Implementation]
IF pki_technology IN nsa_approved_list
AND key_production_process = "nsa_compliant"
AND distribution_method = "approved_channels"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Asymmetric keys produced using NSA-approved technology | [RULE-01] |
| Asymmetric keys controlled using NSA-approved processes | [RULE-02] |
| Asymmetric keys distributed using NSA-approved methods | [RULE-03] |
| Documentation of approved technologies maintained | [RULE-04] |
| Prohibition of unapproved technologies | [RULE-05] |
| Pre-deployment validation required | [RULE-06] |
```