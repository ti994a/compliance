# POLICY: SC-20(2): Data Origin and Integrity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-20-2 |
| NIST Control | SC-20(2): Data Origin and Integrity |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | DNS, DNSSEC, data integrity, origin authentication, name resolution, digital signatures |

## 1. POLICY STATEMENT
All internal name/address resolution queries must include data origin authentication and integrity protection mechanisms. The organization shall implement cryptographic protections to ensure DNS responses are authentic and have not been tampered with during transmission.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal DNS servers | YES | All authoritative and recursive resolvers |
| DNS queries/responses | YES | Internal network name resolution only |
| External DNS services | CONDITIONAL | Only if used for internal resolution |
| Development/test environments | YES | Same requirements as production |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Deploy and maintain DNSSEC infrastructure<br>• Monitor DNS integrity mechanisms<br>• Validate cryptographic signatures |
| System Administrators | • Configure DNS servers with integrity protection<br>• Maintain digital signing keys<br>• Implement secure DNS protocols |
| Security Operations | • Monitor for DNS tampering attempts<br>• Investigate integrity validation failures<br>• Maintain incident response procedures |

## 4. RULES
[RULE-01] All internal DNS servers MUST implement DNSSEC signing for authoritative zones to provide data origin authentication.
[VALIDATION] IF dns_server_type = "authoritative" AND dnssec_enabled = FALSE THEN critical_violation

[RULE-02] DNS recursive resolvers MUST validate DNSSEC signatures for all internal queries before returning responses.
[VALIDATION] IF dns_server_type = "recursive" AND signature_validation = FALSE THEN critical_violation

[RULE-03] DNS responses lacking valid origin authentication artifacts MUST be rejected and logged as security events.
[VALIDATION] IF dns_response_received = TRUE AND origin_authentication = FALSE AND response_accepted = TRUE THEN violation

[RULE-04] Cryptographic keys used for DNS signing MUST be rotated according to organizational key management policy, not exceeding 13 months for KSK and 3 months for ZSK.
[VALIDATION] IF key_type = "KSK" AND key_age > 13_months THEN violation
[VALIDATION] IF key_type = "ZSK" AND key_age > 3_months THEN violation

[RULE-05] All DNS integrity validation failures MUST be logged with sufficient detail for security analysis and incident response.
[VALIDATION] IF integrity_validation = "failed" AND event_logged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNSSEC Implementation - Deploy and configure DNSSEC on all internal DNS infrastructure
- [PROC-02] Key Management - Establish procedures for DNS signing key generation, rotation, and revocation
- [PROC-03] Integrity Monitoring - Implement continuous monitoring of DNS integrity mechanisms
- [PROC-04] Incident Response - Define response procedures for DNS integrity violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: DNS infrastructure changes, security incidents, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Authoritative Server Without DNSSEC]
IF server_role = "authoritative_dns"
AND dnssec_signing = FALSE
AND zone_type = "internal"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Recursive Resolver Accepting Invalid Signatures]
IF server_role = "recursive_resolver"
AND signature_validation_enabled = TRUE
AND invalid_signature_accepted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Expired Signing Keys]
IF dns_signing_key_present = TRUE
AND key_expiration_date < current_date
AND key_rotation_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Integrity Logging]
IF dns_integrity_check = "failed"
AND security_event_logged = FALSE
AND logging_system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper DNSSEC Implementation]
IF authoritative_server = TRUE
AND dnssec_enabled = TRUE
AND signature_validation = TRUE
AND key_rotation_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data origin artifacts are provided for internal name/address resolution queries | [RULE-01], [RULE-02] |
| Integrity protection artifacts are provided for internal name/address resolution queries | [RULE-01], [RULE-02], [RULE-03] |