# POLICY: SC-12.3: Asymmetric Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12.3 |
| NIST Control | SC-12.3: Asymmetric Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | asymmetric keys, NSA-approved, key management, cryptographic keys, PKI, certificates |

## 1. POLICY STATEMENT
All asymmetric cryptographic keys used within the organization MUST be produced, controlled, and distributed using only NSA-approved key management technology and processes. This requirement applies to all cryptographic operations including PKI certificates, digital signatures, and encrypted communications across all systems and environments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, on-premises, and hybrid |
| Third-party Applications | YES | Must use approved key management |
| Development/Test Systems | YES | No exception for non-production |
| IoT/Embedded Devices | YES | Must meet same standards |
| External Partners | CONDITIONAL | When accessing internal systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve NSA-approved key management technologies<br>• Oversee policy compliance and enforcement<br>• Maintain approved technology list |
| PKI Administrator | • Implement NSA-approved key generation processes<br>• Manage certificate lifecycle using approved tools<br>• Monitor key distribution mechanisms |
| System Administrators | • Configure systems to use only approved key management<br>• Implement proper key storage and access controls<br>• Report non-compliant key usage |
| Security Architecture Team | • Validate NSA-approval status of key management technologies<br>• Design compliant key management workflows<br>• Review and approve cryptographic implementations |

## 4. RULES
[RULE-01] All asymmetric cryptographic key generation MUST use NSA-approved key management technology and processes as defined in FIPS 140-2 Level 3 or higher validated modules.
[VALIDATION] IF key_generation_technology NOT IN nsa_approved_list THEN critical_violation

[RULE-02] Asymmetric key distribution MUST occur only through NSA-approved channels and protocols with end-to-end authentication and integrity protection.
[VALIDATION] IF key_distribution_method NOT IN approved_distribution_channels THEN violation

[RULE-03] All asymmetric keys MUST be controlled using NSA-approved key management systems that provide secure storage, access logging, and lifecycle management.
[VALIDATION] IF key_storage_system.nsa_approved = FALSE THEN critical_violation

[RULE-04] PKI certificates MUST be issued only by Certificate Authorities using NSA-approved key management processes and Class 3 or Class 4 certificate standards.
[VALIDATION] IF certificate_authority.nsa_approved = FALSE OR certificate_class < 3 THEN violation

[RULE-05] Non-NSA-approved asymmetric key management technologies MUST NOT be deployed or used for any cryptographic operations.
[VALIDATION] IF deployed_technology NOT IN nsa_approved_list AND cryptographic_use = TRUE THEN critical_violation

[RULE-06] All asymmetric key operations MUST be logged and monitored through NSA-approved audit mechanisms with tamper-evident storage.
[VALIDATION] IF key_operation_logged = FALSE OR audit_system.nsa_approved = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] NSA Technology Validation - Process for validating and maintaining list of NSA-approved key management technologies
- [PROC-02] Key Lifecycle Management - Standardized procedures for key generation, distribution, storage, rotation, and destruction
- [PROC-03] Certificate Authority Approval - Process for evaluating and approving PKI Certificate Authorities
- [PROC-04] Compliance Monitoring - Continuous monitoring and assessment of key management technology compliance
- [PROC-05] Incident Response - Response procedures for detection of non-approved key management technology usage

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New NSA guidance, security incidents, technology changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Third-party Application Integration]
IF application_type = "third_party"
AND key_management_technology NOT IN nsa_approved_list
AND system_access = "granted"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Development Environment Keys]
IF environment_type = "development"
AND asymmetric_keys_present = TRUE
AND key_generation_method NOT IN nsa_approved_processes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Certificate Authority Validation]
IF certificate_authority.nsa_approved = TRUE
AND certificate_class >= 3
AND key_management_process.nsa_approved = TRUE
THEN compliance = TRUE

[SCENARIO-04: Legacy System Exception]
IF system_type = "legacy"
AND exception_documented = TRUE
AND migration_plan_approved = TRUE
AND timeline <= 12_months
THEN compliance = CONDITIONAL
violation_severity = "Moderate"

[SCENARIO-05: Cloud Service Key Management]
IF deployment_type = "cloud"
AND cloud_provider_key_management.nsa_approved = FALSE
AND customer_managed_keys = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Asymmetric cryptographic keys are produced using NSA-approved key management technology and processes | [RULE-01] |
| Asymmetric cryptographic keys are controlled using NSA-approved key management technology and processes | [RULE-03] |
| Asymmetric cryptographic keys are distributed using NSA-approved key management technology and processes | [RULE-02] |