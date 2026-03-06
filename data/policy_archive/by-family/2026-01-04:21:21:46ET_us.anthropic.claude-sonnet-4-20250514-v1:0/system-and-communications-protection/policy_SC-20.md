# POLICY: SC-20: Secure Name/Address Resolution Service (Authoritative Source)

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-20 |
| NIST Control | SC-20: Secure Name/Address Resolution Service (Authoritative Source) |
| Version | 1.0 |
| Owner | Network Security Manager |
| Keywords | DNS, DNSSEC, name resolution, digital signatures, chain of trust, data origin authentication |

## 1. POLICY STATEMENT
All name/address resolution services operated by the organization MUST provide cryptographic authentication and integrity verification for authoritative data returned to external queries. Systems operating in hierarchical namespaces MUST implement chain of trust mechanisms to verify parent-child domain relationships.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| DNS Servers | YES | All authoritative DNS servers |
| Internal DNS | CONDITIONAL | Only if serving external queries |
| Third-party DNS | YES | If operated on behalf of organization |
| Non-DNS Resolution | YES | Any system mapping names to addresses |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Manager | • Policy oversight and compliance monitoring<br>• DNSSEC key management approval<br>• Security status reporting |
| DNS Administrators | • DNSSEC implementation and maintenance<br>• Digital signature generation and validation<br>• Chain of trust configuration |
| Security Operations | • Monitoring resolution service integrity<br>• Incident response for DNS security events<br>• Validation of cryptographic artifacts |

## 4. RULES
[RULE-01] All authoritative name resolution services MUST provide DNSSEC digital signatures or equivalent cryptographic authentication artifacts with response data to external queries.
[VALIDATION] IF external_query = TRUE AND response_contains_crypto_signature = FALSE THEN violation

[RULE-02] DNS servers MUST generate and maintain current cryptographic keys with key rollover performed at least annually or when compromise is suspected.
[VALIDATION] IF key_age > 365_days OR key_compromise_suspected = TRUE THEN violation

[RULE-03] Systems operating in hierarchical namespaces MUST implement delegation signer (DS) records or equivalent mechanisms to indicate child zone security status.
[VALIDATION] IF hierarchical_namespace = TRUE AND child_zones_exist = TRUE AND ds_records_configured = FALSE THEN violation

[RULE-04] Chain of trust verification MUST be enabled between parent and child domains where both support secure resolution services.
[VALIDATION] IF parent_secure = TRUE AND child_secure = TRUE AND chain_of_trust_enabled = FALSE THEN violation

[RULE-05] Integrity verification artifacts MUST be validated before serving cached resolution data to external clients.
[VALIDATION] IF serving_cached_data = TRUE AND external_client = TRUE AND integrity_verified = FALSE THEN violation

[RULE-06] Non-DNS name resolution systems MUST implement equivalent authentication and integrity mechanisms appropriate to their technology.
[VALIDATION] IF non_dns_resolution = TRUE AND equivalent_security_mechanisms = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNSSEC Implementation - Configuration and deployment of DNS Security Extensions
- [PROC-02] Key Management - Generation, storage, and rotation of cryptographic keys
- [PROC-03] Chain of Trust Validation - Verification procedures for parent-child domain relationships
- [PROC-04] Integrity Monitoring - Continuous validation of resolution data authenticity

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: DNS infrastructure changes, key compromise, security incidents, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: External DNS Query Without DNSSEC]
IF query_source = "external"
AND dns_response_sent = TRUE
AND dnssec_signature_included = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Expired Cryptographic Keys]
IF dns_server_operational = TRUE
AND current_date > key_expiration_date
AND key_rollover_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Chain of Trust]
IF parent_domain_dnssec_enabled = TRUE
AND child_domain_dnssec_enabled = TRUE
AND delegation_signer_record_present = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Cached Data Integrity Failure]
IF serving_cached_response = TRUE
AND external_client_request = TRUE
AND cached_data_integrity_verified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Non-DNS Resolution Security]
IF resolution_service_type != "DNS"
AND external_queries_supported = TRUE
AND equivalent_authentication_mechanism = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Additional data origin authentication provided | [RULE-01] |
| Integrity verification artifacts provided | [RULE-01], [RULE-05] |
| Security status indication for child zones | [RULE-03] |
| Chain of trust verification capability | [RULE-04] |