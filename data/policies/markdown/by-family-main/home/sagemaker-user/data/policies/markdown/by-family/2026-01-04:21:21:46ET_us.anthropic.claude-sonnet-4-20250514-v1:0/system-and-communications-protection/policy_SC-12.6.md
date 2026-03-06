# POLICY: SC-12.6: Physical Control of Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12.6 |
| NIST Control | SC-12.6: Physical Control of Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, physical control, external service providers, cloud encryption, key custody |

## 1. POLICY STATEMENT
The organization SHALL maintain physical control of cryptographic keys when stored information is encrypted by external service providers. Physical control ensures cryptographic keys remain under organizational custody and are not accessible to unauthorized parties including the external service provider.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud Service Providers | YES | All providers storing encrypted organizational data |
| Data Center Providers | YES | Third-party facilities hosting encrypted systems |
| SaaS Applications | YES | When organization-controlled encryption is used |
| Internal Data Centers | NO | Covered under base SC-12 control |
| Public Data | NO | No encryption requirements for public information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve external service provider encryption arrangements<br>• Define physical key control requirements<br>• Oversee compliance monitoring |
| Cryptographic Officer | • Implement physical key control mechanisms<br>• Validate key custody arrangements<br>• Monitor key access and handling |
| Vendor Management | • Negotiate contractual key control requirements<br>• Validate provider compliance capabilities<br>• Manage service provider assessments |

## 4. RULES
[RULE-01] Organizations MUST maintain physical custody of cryptographic keys used to encrypt data stored by external service providers.
[VALIDATION] IF data_location = "external_provider" AND encryption_enabled = TRUE AND key_custody != "organization" THEN violation

[RULE-02] External service providers SHALL NOT have access to cryptographic keys used to encrypt organizational data.
[VALIDATION] IF provider_key_access = TRUE AND data_classification != "public" THEN critical_violation

[RULE-03] Physical key storage mechanisms MUST be located within organization-controlled facilities or approved key escrow services.
[VALIDATION] IF key_storage_location NOT IN ["org_facility", "approved_escrow"] THEN violation

[RULE-04] Key management systems used with external providers MUST implement hardware security modules (HSMs) or equivalent physical protection.
[VALIDATION] IF external_encryption = TRUE AND hsm_protection = FALSE AND equivalent_protection = FALSE THEN violation

[RULE-05] Contractual agreements with external service providers MUST explicitly prohibit provider access to organizational cryptographic keys.
[VALIDATION] IF contract_signed = TRUE AND key_access_prohibition = FALSE THEN violation

[RULE-06] Physical key control arrangements MUST be validated through third-party assessment or audit at least annually.
[VALIDATION] IF last_key_control_audit > 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Provider Key Management - Establish and maintain cryptographic key control for third-party services
- [PROC-02] Physical Key Custody Validation - Verify and document organizational control of encryption keys
- [PROC-03] Provider Contract Review - Ensure contractual key control requirements in service agreements
- [PROC-04] Key Control Monitoring - Continuously monitor and audit physical key custody arrangements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New external service provider, change in encryption requirements, security incident involving keys

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Storage with Provider-Managed Keys]
IF service_type = "cloud_storage"
AND encryption_enabled = TRUE
AND key_management = "provider_managed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Customer-Managed Encryption Keys]
IF service_type = "external_provider"
AND encryption_enabled = TRUE
AND key_custody = "organization"
AND physical_control_verified = TRUE
THEN compliance = TRUE

[SCENARIO-03: Hybrid Key Management]
IF data_encryption = TRUE
AND key_storage = "external_hsm"
AND organizational_control = TRUE
AND provider_key_access = FALSE
THEN compliance = TRUE

[SCENARIO-04: Missing Key Control Validation]
IF external_encryption = TRUE
AND key_control_audit_date > 365_days
AND compensating_controls = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Contractual Key Access Rights]
IF service_contract_active = TRUE
AND provider_key_access_prohibited = FALSE
AND encrypted_data_stored = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical control of cryptographic keys is maintained when stored information is encrypted by external service providers | RULE-01, RULE-02, RULE-03 |
| Key custody verification and validation | RULE-06 |
| Provider access restrictions | RULE-02, RULE-05 |
| Physical protection mechanisms | RULE-04 |