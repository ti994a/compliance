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
All systems MUST request and perform data origin authentication and data integrity verification on name/address resolution responses received from authoritative sources. DNS resolvers and name resolution services MUST validate authenticity and integrity of response data through DNSSEC validation or authenticated channels to trusted validation providers.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| DNS Servers | YES | All recursive and caching DNS servers |
| Client Systems | YES | All systems performing name resolution |
| Network Infrastructure | YES | Load balancers, firewalls with DNS capabilities |
| Cloud Services | YES | Cloud-hosted DNS and name resolution services |
| Third-party DNS Services | CONDITIONAL | When used for organizational name resolution |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Operations Team | • Configure and maintain DNS infrastructure<br>• Implement DNSSEC validation<br>• Monitor DNS resolution integrity |
| System Administrators | • Configure client DNS settings<br>• Ensure authenticated channels to resolvers<br>• Validate system DNS configurations |
| Security Operations Team | • Monitor DNS security events<br>• Investigate DNS integrity violations<br>• Maintain DNS security policies |

## 4. RULES
[RULE-01] All recursive and caching DNS resolvers MUST perform DNSSEC validation for domains that support DNSSEC signatures.
[VALIDATION] IF dns_server_type IN ["recursive", "caching"] AND dnssec_validation_enabled = FALSE THEN violation

[RULE-02] DNS clients MUST either perform DNSSEC validation locally OR use authenticated channels to trusted recursive resolvers that perform validation.
[VALIDATION] IF client_dnssec_validation = FALSE AND authenticated_channel_to_validator = FALSE THEN violation

[RULE-03] Systems using non-DNS name resolution technologies MUST implement equivalent data origin authentication and integrity verification mechanisms.
[VALIDATION] IF name_resolution_type != "DNS" AND data_authentication_mechanism = NULL THEN violation

[RULE-04] All name/address resolution responses from authoritative sources MUST be validated for data origin authentication before use.
[VALIDATION] IF resolution_response_used = TRUE AND origin_authentication_performed = FALSE THEN violation

[RULE-05] DNS infrastructure MUST log all DNSSEC validation failures and authentication errors for security monitoring.
[VALIDATION] IF dnssec_validation_failure_logged = FALSE OR authentication_error_logged = FALSE THEN violation

[RULE-06] Authenticated channels to DNS validation providers MUST use encrypted transport (DNS over HTTPS/TLS) or equivalent secure mechanisms.
[VALIDATION] IF dns_transport_encryption = FALSE AND authentication_required = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNSSEC Configuration - Standard procedures for enabling and configuring DNSSEC validation
- [PROC-02] DNS Client Authentication - Process for establishing authenticated channels to trusted resolvers  
- [PROC-03] DNS Security Monitoring - Procedures for monitoring and responding to DNS integrity violations
- [PROC-04] Alternative Name Resolution Validation - Process for validating non-DNS name resolution mechanisms

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: DNS infrastructure changes, security incidents involving name resolution, new DNS technologies deployment

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal DNS Server Without DNSSEC]
IF server_type = "recursive_dns"
AND dnssec_validation_enabled = FALSE
AND serves_internal_clients = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Client with Unvalidated DNS]
IF system_type = "client"
AND local_dnssec_validation = FALSE
AND dns_server_authenticated_channel = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Cloud DNS with Proper Validation]
IF dns_service_type = "cloud"
AND dnssec_validation_enabled = TRUE
AND transport_encryption = TRUE
AND logging_enabled = TRUE
THEN compliance = TRUE

[SCENARIO-04: Legacy System Alternative Resolution]
IF name_resolution_type = "non_dns"
AND data_origin_authentication = TRUE
AND integrity_verification = TRUE
THEN compliance = TRUE

[SCENARIO-05: DNSSEC Validation Failure Not Logged]
IF dnssec_validation_result = "failure"
AND security_event_logged = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data origin authentication requested for name/address resolution responses | [RULE-04] |
| Data origin authentication performed on name/address resolution responses | [RULE-01], [RULE-02] |
| Data integrity verification requested for name/address resolution responses | [RULE-04] |
| Data integrity verification performed on name/address resolution responses | [RULE-01], [RULE-02], [RULE-03] |