# POLICY: SC-12.6: Physical Control of Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12.6 |
| NIST Control | SC-12.6: Physical Control of Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, physical control, external service providers, cloud security, key management |

## 1. POLICY STATEMENT
The organization SHALL maintain physical control of cryptographic keys when stored information is encrypted by external service providers. This ensures that cryptographic keys used to protect organizational data remain under direct organizational control even when data is processed or stored by third-party providers.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud Service Providers | YES | All providers storing encrypted organizational data |
| Data Center Providers | YES | External facilities hosting organizational systems |
| SaaS Applications | YES | When organization provides encryption keys |
| Managed Service Providers | YES | Providers with access to encrypted data |
| Internal Data Centers | NO | Organization maintains direct physical control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve external service provider key management arrangements<br>• Ensure policy compliance across all third-party relationships<br>• Review and approve key escrow arrangements |
| Security Architecture Team | • Design key management solutions for external providers<br>• Validate physical control mechanisms<br>• Assess provider key handling capabilities |
| Vendor Management | • Include key control requirements in contracts<br>• Monitor provider compliance with key control obligations<br>• Manage key-related SLA requirements |

## 4. RULES
[RULE-01] Organizations MUST retain physical control of cryptographic keys when using external service providers for encrypted data storage or processing.
[VALIDATION] IF external_provider = TRUE AND encrypted_data = TRUE AND physical_key_control = FALSE THEN critical_violation

[RULE-02] External service provider contracts MUST include explicit requirements for organizational control of cryptographic keys used to encrypt organizational data.
[VALIDATION] IF contract_type = "external_provider" AND encrypted_services = TRUE AND key_control_clause = FALSE THEN violation

[RULE-03] Cryptographic keys SHALL NOT be stored, processed, or managed by external service providers unless under documented organizational control mechanisms.
[VALIDATION] IF key_location = "external_provider" AND organizational_control = FALSE THEN critical_violation

[RULE-04] Organizations MUST implement technical controls to prevent external service providers from accessing cryptographic keys used to encrypt organizational data.
[VALIDATION] IF provider_key_access = TRUE AND technical_controls = FALSE THEN critical_violation

[RULE-05] Key management procedures MUST be documented and validated for all external service arrangements involving encrypted organizational data.
[VALIDATION] IF external_encrypted_service = TRUE AND documented_key_procedures = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Provider Key Control Assessment - Evaluate provider capabilities for supporting organizational key control
- [PROC-02] Contract Key Management Requirements - Define and negotiate key control obligations in service agreements
- [PROC-03] Key Control Monitoring - Ongoing verification of key control effectiveness with external providers
- [PROC-04] Key Escrow Management - Secure handling of keys when escrow arrangements are necessary

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon significant changes to external provider relationships
- Triggering events: New external provider onboarding, contract renewals, security incidents involving external providers, changes to encryption requirements

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Storage with Provider-Managed Keys]
IF service_type = "cloud_storage"
AND encryption_enabled = TRUE
AND key_management = "provider_managed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Customer-Managed Encryption Keys]
IF external_provider = TRUE
AND encryption_method = "customer_managed_keys"
AND physical_key_control = "organization"
THEN compliance = TRUE

[SCENARIO-03: Hybrid Key Management]
IF service_provider = "external"
AND key_storage = "provider_facility"
AND organizational_control = TRUE
AND technical_controls = "implemented"
THEN compliance = TRUE

[SCENARIO-04: SaaS Application with Shared Keys]
IF application_type = "SaaS"
AND encryption_keys = "shared_with_provider"
AND key_access_controls = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Managed Service with Key Escrow]
IF service_type = "managed_service"
AND key_escrow = TRUE
AND escrow_controls = "documented"
AND organizational_access = "maintained"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical control of cryptographic keys is maintained when stored information is encrypted by external service providers | [RULE-01], [RULE-03], [RULE-04] |
| Contractual obligations for key control with external providers | [RULE-02] |
| Documented key management procedures for external arrangements | [RULE-05] |