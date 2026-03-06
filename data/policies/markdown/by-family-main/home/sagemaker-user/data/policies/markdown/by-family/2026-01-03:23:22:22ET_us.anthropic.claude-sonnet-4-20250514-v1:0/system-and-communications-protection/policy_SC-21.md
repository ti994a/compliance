```markdown
# POLICY: SC-21: Secure Name/Address Resolution Service (Recursive or Caching Resolver)

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-21 |
| NIST Control | SC-21: Secure Name/Address Resolution Service (Recursive or Caching Resolver) |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | DNS, DNSSEC, name resolution, data origin authentication, data integrity verification, recursive resolver, caching resolver |

## 1. POLICY STATEMENT
All systems MUST request and perform data origin authentication and data integrity verification on name/address resolution responses received from authoritative sources. DNS resolvers MUST validate DNSSEC signatures or use authenticated channels to trusted validation providers.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| DNS servers (recursive/caching) | YES | Primary enforcement point |
| DNS client resolvers | YES | Must perform validation or use authenticated channels |
| Applications performing name resolution | YES | Must validate responses or use validated resolvers |
| Network infrastructure devices | YES | When performing DNS resolution |
| Third-party DNS services | CONDITIONAL | When used by organization systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure DNSSEC validation on DNS infrastructure<br>• Monitor DNS resolution security<br>• Maintain authenticated channels to validation providers |
| System Administrators | • Configure systems to use validated DNS resolvers<br>• Implement data origin authentication mechanisms<br>• Document DNS security configurations |
| Security Operations | • Monitor DNS resolution anomalies<br>• Investigate DNS security violations<br>• Maintain DNS security logging |

## 4. RULES
[RULE-01] All DNS recursive resolvers and caching servers MUST perform DNSSEC validation for domains that support it.
[VALIDATION] IF dns_server_type IN ["recursive", "caching"] AND dnssec_validation_enabled = FALSE THEN violation

[RULE-02] DNS clients MUST either perform DNSSEC validation locally OR use authenticated channels to trusted validation providers.
[VALIDATION] IF dns_client_validation = FALSE AND authenticated_channel_to_validator = FALSE THEN violation

[RULE-03] Systems using non-DNS name resolution technologies MUST implement equivalent data origin authentication and integrity verification mechanisms.
[VALIDATION] IF name_resolution_technology != "DNS" AND data_origin_auth = FALSE THEN violation

[RULE-04] All name/address resolution responses MUST be verified for data integrity before use by applications.
[VALIDATION] IF resolution_response_used = TRUE AND integrity_verification = FALSE THEN violation

[RULE-05] DNS servers MUST log all validation failures and security-related DNS events.
[VALIDATION] IF dns_validation_failure_occurred = TRUE AND logged = FALSE THEN violation

[RULE-06] Authenticated channels to DNS validation providers MUST use approved cryptographic protocols and be regularly validated.
[VALIDATION] IF authenticated_channel_crypto NOT IN approved_protocols OR channel_validation_date > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNSSEC Configuration Management - Standard procedures for configuring and maintaining DNSSEC validation
- [PROC-02] DNS Security Monitoring - Continuous monitoring of DNS resolution security and validation failures
- [PROC-03] Authenticated Channel Establishment - Process for establishing and maintaining authenticated channels to validation providers
- [PROC-04] DNS Security Incident Response - Procedures for responding to DNS security violations and attacks

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: DNS infrastructure changes, security incidents involving DNS, new DNS technologies deployment

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal DNS Server Without DNSSEC]
IF system_type = "internal_dns_server"
AND server_function IN ["recursive", "caching"]
AND dnssec_validation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Client Using Unvalidated External DNS]
IF dns_client = TRUE
AND external_dns_provider = TRUE
AND provider_performs_validation = FALSE
AND client_performs_validation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Application with Custom Name Resolution]
IF application_performs_name_resolution = TRUE
AND resolution_method != "standard_dns"
AND data_origin_authentication = FALSE
AND data_integrity_verification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Validated DNS with Proper Logging]
IF dns_server_type = "recursive"
AND dnssec_validation = TRUE
AND validation_failures_logged = TRUE
AND authenticated_channels_validated = TRUE
THEN compliance = TRUE

[SCENARIO-05: Mixed Environment with Partial Validation]
IF some_clients_validated = TRUE
AND some_clients_unvalidated = TRUE
AND unvalidated_clients > 0
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data origin authentication requested for name/address resolution responses | [RULE-01], [RULE-02] |
| Data origin authentication performed on name/address resolution responses | [RULE-01], [RULE-02], [RULE-03] |
| Data integrity verification requested for name/address resolution responses | [RULE-01], [RULE-04] |
| Data integrity verification performed on name/address resolution responses | [RULE-01], [RULE-03], [RULE-04] |
```