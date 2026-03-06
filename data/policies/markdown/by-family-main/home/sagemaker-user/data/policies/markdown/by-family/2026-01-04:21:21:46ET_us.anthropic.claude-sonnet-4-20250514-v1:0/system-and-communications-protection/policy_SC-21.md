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
All systems MUST request and perform data origin authentication and data integrity verification on name/address resolution responses received from authoritative sources. DNS resolvers SHALL implement DNSSEC validation or use authenticated channels to trusted validation providers to ensure the authenticity and integrity of resolution data.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| DNS Servers (Recursive/Caching) | YES | Primary enforcement point |
| DNS Client Systems | YES | Must validate or use authenticated channels |
| Network Infrastructure | YES | Routers, switches with DNS functionality |
| Cloud DNS Services | YES | AWS Route 53, Azure DNS, etc. |
| Legacy Systems | CONDITIONAL | Must comply by [current_date + 180_days] |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure DNSSEC validation on DNS infrastructure<br>• Monitor DNS security events<br>• Maintain authenticated channels to validation providers |
| System Administrators | • Implement DNSSEC validation on managed systems<br>• Configure DNS clients for secure resolution<br>• Document DNS security configurations |
| Cloud Operations Team | • Configure cloud DNS services for DNSSEC validation<br>• Ensure authenticated channels in hybrid environments<br>• Monitor cloud DNS security compliance |

## 4. RULES

[RULE-01] All recursive and caching DNS resolvers MUST perform DNSSEC validation for domains that support DNSSEC signatures.
[VALIDATION] IF dns_resolver_type IN ["recursive", "caching"] AND dnssec_validation_enabled = FALSE THEN violation

[RULE-02] DNS clients MUST either perform local DNSSEC validation or use authenticated channels to trusted recursive resolvers that perform validation.
[VALIDATION] IF dns_client_validation = FALSE AND authenticated_channel_to_validator = FALSE THEN violation

[RULE-03] Systems using non-DNS name resolution technologies MUST implement equivalent data origin authentication and integrity verification mechanisms.
[VALIDATION] IF name_resolution_type != "DNS" AND origin_authentication_enabled = FALSE THEN violation

[RULE-04] DNS resolution responses from authoritative sources MUST be validated for data origin authentication before being cached or forwarded.
[VALIDATION] IF response_source = "authoritative" AND origin_authentication_performed = FALSE THEN violation

[RULE-05] All DNS infrastructure MUST log validation failures and security events for monitoring and incident response.
[VALIDATION] IF dns_security_logging_enabled = FALSE OR log_retention_days < 90 THEN violation

[RULE-06] DNS forwarders and proxy servers MUST maintain chain of trust when forwarding validated responses to clients.
[VALIDATION] IF dns_forwarder = TRUE AND chain_of_trust_maintained = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNSSEC Configuration Management - Standard procedures for enabling and maintaining DNSSEC validation
- [PROC-02] DNS Security Monitoring - Continuous monitoring of DNS validation failures and security events  
- [PROC-03] Authenticated Channel Establishment - Process for establishing secure channels to trusted DNS validators
- [PROC-04] Legacy System DNS Migration - Procedure for upgrading non-compliant DNS implementations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: DNS infrastructure changes, security incidents, technology updates, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Corporate DNS Server Without DNSSEC]
IF system_type = "dns_server"
AND dns_function IN ["recursive", "caching"]
AND dnssec_validation_enabled = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Client Using Unvalidated External DNS]
IF dns_client = TRUE
AND external_dns_provider = TRUE
AND dnssec_validation_verified = FALSE
AND authenticated_channel = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Cloud DNS Service with DNSSEC]
IF cloud_dns_service = TRUE
AND dnssec_validation_enabled = TRUE
AND security_logging_enabled = TRUE
THEN compliance = TRUE

[SCENARIO-04: Legacy System with Alternative Validation]
IF system_age > "legacy_threshold"
AND dns_validation_native = FALSE
AND alternative_validation_mechanism = TRUE
AND validation_effectiveness_verified = TRUE
THEN compliance = TRUE

[SCENARIO-05: DNS Forwarder Breaking Chain of Trust]
IF dns_forwarder = TRUE
AND receives_validated_responses = TRUE
AND forwards_validation_status = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data origin authentication requested | [RULE-01], [RULE-02] |
| Data origin authentication performed | [RULE-01], [RULE-04] |
| Data integrity verification requested | [RULE-01], [RULE-02] |
| Data integrity verification performed | [RULE-01], [RULE-04] |