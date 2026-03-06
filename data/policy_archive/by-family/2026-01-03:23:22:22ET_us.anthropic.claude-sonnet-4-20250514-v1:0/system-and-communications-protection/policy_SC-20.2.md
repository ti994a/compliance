# POLICY: SC-20(2): Data Origin and Integrity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-20-2 |
| NIST Control | SC-20(2): Data Origin and Integrity |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | DNS security, DNSSEC, data integrity, name resolution, origin authentication |

## 1. POLICY STATEMENT
All internal name/address resolution queries MUST be protected with data origin authentication and integrity verification mechanisms. The organization SHALL implement cryptographic protections to ensure DNS responses are authentic and have not been tampered with during transmission.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal DNS servers | YES | All authoritative and recursive resolvers |
| DNS forwarders | YES | Including cloud-hosted DNS services |
| Network devices performing DNS | YES | Firewalls, load balancers with DNS functions |
| Client DNS resolution | YES | Workstations and servers making DNS queries |
| External DNS queries | NO | Covered under base SC-20 control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Implement DNSSEC validation on all internal resolvers<br>• Configure DNS integrity protection mechanisms<br>• Monitor DNS security events and anomalies |
| System Administrators | • Deploy signed DNS zones for internal domains<br>• Maintain DNS security configurations<br>• Validate DNS response authenticity |
| Security Operations Center | • Monitor DNS integrity violations<br>• Respond to DNS spoofing incidents<br>• Maintain DNS security monitoring tools |

## 4. RULES
[RULE-01] All internal authoritative DNS servers MUST implement DNSSEC signing for internal zones.
[VALIDATION] IF dns_server_type = "authoritative" AND dnssec_enabled = FALSE THEN violation

[RULE-02] Internal DNS recursive resolvers MUST validate DNSSEC signatures for all signed zones.
[VALIDATION] IF resolver_type = "recursive" AND dnssec_validation = "disabled" THEN violation

[RULE-03] DNS responses for internal queries MUST include cryptographic integrity protection artifacts when available.
[VALIDATION] IF query_type = "internal" AND signed_zone = TRUE AND integrity_artifacts = FALSE THEN violation

[RULE-04] Systems performing internal name resolution MUST verify data origin authentication when DNSSEC records are present.
[VALIDATION] IF dnssec_records_present = TRUE AND origin_verification = FALSE THEN violation

[RULE-05] DNS integrity protection failures MUST be logged and generate security alerts within 5 minutes.
[VALIDATION] IF integrity_check = "failed" AND alert_generated = FALSE AND time_elapsed > 5_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNSSEC Zone Signing - Process for signing internal DNS zones and key management
- [PROC-02] DNS Validation Configuration - Setup and maintenance of DNSSEC validation on resolvers  
- [PROC-03] DNS Security Monitoring - Continuous monitoring of DNS integrity and origin validation
- [PROC-04] DNS Incident Response - Response procedures for DNS spoofing and integrity violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: DNS security incidents, infrastructure changes, new internal domains

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal DNS Query Without DNSSEC]
IF query_destination = "internal_domain"
AND dnssec_signed = TRUE
AND integrity_protection = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Recursive Resolver Missing Validation]
IF server_role = "recursive_resolver" 
AND dnssec_validation = "disabled"
AND internal_queries_processed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unsigned Internal Zone]
IF zone_type = "internal_authoritative"
AND dnssec_signing = FALSE
AND zone_active = TRUE
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-04: DNS Integrity Failure Not Logged]
IF dns_validation_result = "failed"
AND security_log_entry = FALSE
AND time_since_failure > 5_minutes
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-05: Compliant Internal DNS Resolution]
IF query_type = "internal"
AND dnssec_signed = TRUE
AND origin_verified = TRUE
AND integrity_validated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data origin artifacts provided for internal name/address resolution queries | [RULE-01], [RULE-04] |
| Integrity protection artifacts provided for internal name/address resolution queries | [RULE-02], [RULE-03] |