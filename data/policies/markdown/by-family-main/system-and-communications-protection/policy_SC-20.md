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
All authoritative name/address resolution services MUST provide cryptographic data origin authentication and integrity verification artifacts with resolution responses. Systems operating in hierarchical namespaces MUST implement mechanisms to establish and verify chains of trust between parent and child domains.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| DNS Servers | YES | All authoritative DNS servers |
| External-facing Resolution Services | YES | Services responding to external queries |
| Internal DNS Services | CONDITIONAL | If providing authoritative responses |
| Third-party DNS Providers | YES | Must meet same requirements |
| Legacy Name Resolution Systems | YES | Non-DNS systems mapping names to addresses |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Manager | • Oversee DNSSEC implementation and key management<br>• Approve DNS security configurations<br>• Monitor chain of trust integrity |
| DNS Administrators | • Configure and maintain DNSSEC signing<br>• Manage cryptographic keys and signatures<br>• Implement delegation signer records |
| Security Operations Team | • Monitor DNS security events<br>• Validate integrity verification mechanisms<br>• Respond to DNS security incidents |

## 4. RULES
[RULE-01] All authoritative DNS servers MUST implement DNSSEC signing for all hosted zones.
[VALIDATION] IF server_type = "authoritative_dns" AND dnssec_enabled = FALSE THEN violation

[RULE-02] DNS responses to external queries MUST include cryptographic signatures and verification artifacts.
[VALIDATION] IF query_source = "external" AND response_includes_signatures = FALSE THEN violation

[RULE-03] Parent zones MUST publish delegation signer (DS) records for all signed child zones within 24 hours of child zone signing.
[VALIDATION] IF child_zone_signed = TRUE AND ds_record_published = FALSE AND hours_elapsed > 24 THEN violation

[RULE-04] Key signing keys (KSK) MUST be rotated at least annually and zone signing keys (ZSK) MUST be rotated at least quarterly.
[VALIDATION] IF ksk_age > 365_days OR zsk_age > 90_days THEN violation

[RULE-05] Chain of trust validation MUST be verifiable from root to leaf for all hierarchical zones.
[VALIDATION] IF chain_validation_status = "broken" OR chain_validation_status = "unverifiable" THEN critical_violation

[RULE-06] Non-DNS name resolution services MUST implement equivalent cryptographic authentication and integrity mechanisms.
[VALIDATION] IF service_type != "dns" AND crypto_auth_enabled = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNSSEC Key Management - Generate, store, rotate, and revoke cryptographic keys
- [PROC-02] Zone Signing Process - Sign DNS zones and publish signatures
- [PROC-03] Chain of Trust Validation - Verify parent-child trust relationships
- [PROC-04] Incident Response for DNS Security - Handle DNS compromise and key compromise events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: DNS security incidents, key compromise, major DNS infrastructure changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: External DNS Query Without DNSSEC]
IF query_source = "external"
AND server_type = "authoritative_dns"
AND dnssec_signatures_included = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Broken Chain of Trust]
IF zone_type = "child_zone"
AND parent_ds_record = "missing"
AND zone_signed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Expired Cryptographic Keys]
IF ksk_expiration_date < current_date
OR zsk_expiration_date < current_date
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Third-party DNS Provider Compliance]
IF dns_provider = "third_party"
AND dnssec_support = FALSE
AND external_queries_served = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Legacy System Without Crypto Auth]
IF system_type = "legacy_name_resolution"
AND cryptographic_authentication = FALSE
AND serves_external_requests = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Additional data origin authentication provided | [RULE-01], [RULE-02] |
| Integrity verification artifacts provided | [RULE-01], [RULE-02] |
| Security status indication for child zones | [RULE-03] |
| Chain of trust verification capability | [RULE-05] |
| Non-DNS system authentication mechanisms | [RULE-06] |