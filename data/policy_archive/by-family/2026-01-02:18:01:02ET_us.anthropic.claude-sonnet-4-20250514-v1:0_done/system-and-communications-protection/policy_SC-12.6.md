# POLICY: SC-12.6: Physical Control of Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12.6 |
| NIST Control | SC-12.6: Physical Control of Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, external service providers, cloud security, physical control, encryption |

## 1. POLICY STATEMENT
The organization MUST maintain physical control of cryptographic keys when information is encrypted by external service providers. This ensures encrypted data stored with third-party providers remains protected from unauthorized disclosure or modification through compromised key management.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud Service Providers | YES | All providers storing encrypted organizational data |
| Data Center Providers | YES | External facilities hosting encrypted systems |
| Managed Security Providers | YES | When handling organizational cryptographic keys |
| Internal Data Centers | NO | Covered under base SC-12 control |
| Public Cloud Storage | YES | When used for organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve external provider key management arrangements<br>• Oversee compliance monitoring<br>• Define physical control requirements |
| Cryptographic Key Manager | • Implement physical key control mechanisms<br>• Monitor key custody with external providers<br>• Validate provider compliance with physical control requirements |
| Vendor Management | • Evaluate provider key management capabilities<br>• Negotiate contractual key control requirements<br>• Monitor provider compliance |

## 4. RULES

[RULE-01] Organizations MUST retain physical control of cryptographic keys when using external service providers for encrypted data storage.
[VALIDATION] IF external_provider = TRUE AND encrypted_data = TRUE AND physical_key_control = FALSE THEN violation

[RULE-02] External service provider contracts MUST include explicit requirements for organizational physical control of cryptographic keys.
[VALIDATION] IF contract_key_control_clause = FALSE AND external_encryption = TRUE THEN violation

[RULE-03] Physical key control mechanisms MUST be validated through on-site assessments or third-party attestations at least annually.
[VALIDATION] IF last_physical_assessment > 365_days AND external_provider = TRUE THEN violation

[RULE-04] Organizations MUST implement alternative controls when physical key control cannot be maintained with external providers.
[VALIDATION] IF physical_key_control = FALSE AND compensating_controls = FALSE AND external_encryption = TRUE THEN critical_violation

[RULE-05] Key escrow or split-knowledge arrangements MUST be documented and approved when physical control is shared with external providers.
[VALIDATION] IF shared_key_control = TRUE AND (escrow_documentation = FALSE OR ciso_approval = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Provider Key Control Assessment - Annual evaluation of provider physical key management
- [PROC-02] Key Control Contract Review - Validation of contractual key control requirements
- [PROC-03] Physical Key Custody Verification - Ongoing monitoring of key physical location and access
- [PROC-04] Alternative Control Implementation - Deployment of compensating controls when needed

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New external provider contracts, provider security incidents, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Cloud Storage with Provider-Managed Keys]
IF cloud_provider = "active"
AND encrypted_data = TRUE
AND key_management = "provider_controlled"
AND physical_key_control = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Hybrid Key Management with Escrow]
IF external_provider = TRUE
AND key_escrow = TRUE
AND escrow_documentation = TRUE
AND annual_assessment = "current"
THEN compliance = TRUE

[SCENARIO-03: Data Center with Customer Key Control]
IF data_center_provider = TRUE
AND encryption = "customer_managed"
AND physical_key_access = "customer_only"
AND access_controls = "documented"
THEN compliance = TRUE

[SCENARIO-04: Multi-Cloud without Key Control Strategy]
IF multiple_cloud_providers = TRUE
AND encrypted_data = TRUE
AND key_control_strategy = "undefined"
AND provider_key_access = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Managed Service with Split Knowledge]
IF managed_service_provider = TRUE
AND split_knowledge_keys = TRUE
AND organizational_key_portion = "physically_controlled"
AND provider_assessment = "current"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical control of cryptographic keys is maintained when stored information is encrypted by external service providers | [RULE-01], [RULE-03] |
| Contractual requirements for key physical control | [RULE-02] |
| Validation of physical control mechanisms | [RULE-03] |
| Alternative controls when physical control unavailable | [RULE-04] |
| Documentation of shared control arrangements | [RULE-05] |