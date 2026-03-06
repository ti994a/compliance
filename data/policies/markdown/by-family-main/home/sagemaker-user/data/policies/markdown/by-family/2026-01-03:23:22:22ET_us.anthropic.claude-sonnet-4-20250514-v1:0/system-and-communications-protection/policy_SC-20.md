# POLICY: SC-20: Secure Name/Address Resolution Service (Authoritative Source)

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-20 |
| NIST Control | SC-20: Secure Name/Address Resolution Service (Authoritative Source) |
| Version | 1.0 |
| Owner | Network Security Manager |
| Keywords | DNS, DNSSEC, name resolution, data origin authentication, integrity verification, chain of trust |

## 1. POLICY STATEMENT
All name/address resolution services MUST provide cryptographic authentication and integrity verification for authoritative data returned to external clients. Systems operating in hierarchical namespaces MUST implement chain of trust mechanisms to validate security status across parent and child domains.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| DNS Servers | YES | All authoritative DNS servers |
| Name Resolution Services | YES | Any system providing hostname to IP mapping |
| External-Facing Services | YES | Services responding to external queries |
| Internal-Only DNS | CONDITIONAL | Only if accessible from DMZ or external networks |
| Third-Party DNS Providers | YES | Must meet same requirements via contract |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Manager | • Policy oversight and compliance monitoring<br>• DNSSEC key management approval<br>• Security status validation procedures |
| DNS Administrators | • DNSSEC implementation and maintenance<br>• Digital signature generation and validation<br>• Chain of trust configuration |
| Security Operations Center | • Monitoring DNS security events<br>• Incident response for DNS integrity violations<br>• Regular validation of cryptographic signatures |

## 4. RULES

[RULE-01] All authoritative DNS servers MUST implement DNSSEC digital signatures for all zone data returned to external queries.
[VALIDATION] IF server_type = "authoritative_DNS" AND external_query = TRUE AND dnssec_enabled = FALSE THEN violation

[RULE-02] DNS responses to external queries MUST include cryptographic keys and digital signatures for data origin authentication.
[VALIDATION] IF query_source = "external" AND response_includes_rrsig = FALSE THEN violation

[RULE-03] Systems operating in hierarchical namespaces MUST implement delegation signer (DS) records to indicate child zone security status.
[VALIDATION] IF namespace_type = "hierarchical" AND has_child_zones = TRUE AND ds_records_configured = FALSE THEN violation

[RULE-04] Parent domains MUST provide mechanisms to verify chain of trust to child domains supporting secure resolution services.
[VALIDATION] IF domain_role = "parent" AND child_supports_dnssec = TRUE AND chain_of_trust_verifiable = FALSE THEN violation

[RULE-05] Non-DNS name resolution services MUST implement equivalent cryptographic authentication and integrity verification mechanisms.
[VALIDATION] IF service_type != "DNS" AND provides_name_resolution = TRUE AND crypto_verification = FALSE THEN violation

[RULE-06] DNSSEC key signing keys (KSK) MUST be rotated at least annually and zone signing keys (ZSK) MUST be rotated at least quarterly.
[VALIDATION] IF ksk_age > 365_days OR zsk_age > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNSSEC Implementation - Configuration and deployment of DNS Security Extensions
- [PROC-02] Key Management - Generation, storage, rotation, and revocation of cryptographic keys
- [PROC-03] Chain of Trust Validation - Verification procedures for parent-child domain relationships
- [PROC-04] Security Status Monitoring - Continuous monitoring of DNS security mechanisms
- [PROC-05] Incident Response - Response procedures for DNS integrity violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: DNS infrastructure changes, cryptographic key compromises, namespace modifications, security incidents affecting DNS services

## 7. SCENARIO PATTERNS

[SCENARIO-01: External DNS Query Without DNSSEC]
IF query_source = "external"
AND server_type = "authoritative_DNS"
AND dnssec_signatures_present = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Child Zone Without Delegation Signer]
IF domain_has_child_zones = TRUE
AND child_zone_supports_dnssec = TRUE
AND ds_record_published = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Expired DNSSEC Keys]
IF dnssec_enabled = TRUE
AND (ksk_expired = TRUE OR zsk_expired = TRUE)
AND queries_being_served = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Non-DNS Service Without Crypto Verification]
IF service_provides_name_resolution = TRUE
AND service_type != "DNS"
AND cryptographic_authentication = FALSE
AND external_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Proper DNSSEC Implementation]
IF server_type = "authoritative_DNS"
AND dnssec_enabled = TRUE
AND signatures_valid = TRUE
AND chain_of_trust_intact = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Additional data origin authentication provided with authoritative name resolution data | [RULE-01], [RULE-02] |
| Integrity verification artifacts provided with authoritative name resolution data | [RULE-01], [RULE-02] |
| Means to indicate security status of child zones provided | [RULE-03] |
| Means to enable verification of chain of trust among parent and child domains | [RULE-04] |
| Non-DNS services provide equivalent authentication mechanisms | [RULE-05] |