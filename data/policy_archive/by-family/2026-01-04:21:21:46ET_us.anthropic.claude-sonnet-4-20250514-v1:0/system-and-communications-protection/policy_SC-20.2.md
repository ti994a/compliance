# POLICY: SC-20.2: Data Origin and Integrity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-20.2 |
| NIST Control | SC-20.2: Data Origin and Integrity |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | DNS, DNSSEC, data origin, integrity protection, name resolution, internal queries |

## 1. POLICY STATEMENT
All internal name/address resolution queries MUST be protected with data origin and integrity protection artifacts. The organization SHALL implement cryptographic mechanisms to ensure DNS responses are authentic and have not been tampered with during transmission.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal DNS servers | YES | All authoritative and recursive servers |
| DNS forwarders | YES | Must validate upstream responses |
| Client DNS queries | YES | Internal network queries only |
| External DNS services | CONDITIONAL | Only when used for internal resolution |
| Development/test environments | YES | Same protection requirements apply |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Implement DNSSEC validation<br>• Configure DNS server security settings<br>• Monitor DNS integrity violations |
| System Administrators | • Maintain DNS server configurations<br>• Apply security patches to DNS infrastructure<br>• Generate and manage DNSSEC keys |
| Security Operations Center | • Monitor DNS security events<br>• Investigate DNS integrity failures<br>• Respond to DNS-based security incidents |

## 4. RULES
[RULE-01] All internal DNS servers MUST implement DNSSEC signing for authoritative zones.
[VALIDATION] IF dns_server_type = "authoritative" AND dnssec_signing = FALSE THEN critical_violation

[RULE-02] DNS recursive resolvers MUST perform DNSSEC validation for all internal queries.
[VALIDATION] IF dns_server_type = "recursive" AND dnssec_validation = FALSE THEN critical_violation

[RULE-03] DNS responses lacking valid origin and integrity artifacts MUST be rejected or flagged.
[VALIDATION] IF dns_response_validated = FALSE AND response_accepted = TRUE THEN violation

[RULE-04] DNSSEC key rollover MUST occur at least annually for zone signing keys and every 3 years for key signing keys.
[VALIDATION] IF zsk_age > 365_days OR ksk_age > 1095_days THEN violation

[RULE-05] DNS servers MUST log all validation failures and integrity check results.
[VALIDATION] IF dnssec_validation_failure_logged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNSSEC Implementation - Deploy and configure DNSSEC on all internal DNS infrastructure
- [PROC-02] Key Management - Generate, rotate, and securely store DNSSEC cryptographic keys
- [PROC-03] Validation Monitoring - Monitor and respond to DNS integrity validation failures
- [PROC-04] Incident Response - Handle DNS security incidents and integrity violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: DNS infrastructure changes, security incidents, cryptographic standard updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: DNSSEC Not Enabled]
IF dns_server_role = "authoritative"
AND internal_zone = TRUE
AND dnssec_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Validation Bypass]
IF dns_query_source = "internal"
AND dnssec_validation_required = TRUE
AND validation_bypassed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Expired Keys]
IF dnssec_key_type = "ZSK"
AND key_age > 365_days
AND key_rotation_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unvalidated External Forwarder]
IF dns_forwarder_configured = TRUE
AND upstream_dnssec_support = FALSE
AND alternative_validation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Integrity Logging]
IF dns_validation_failure_occurred = TRUE
AND security_log_entry_created = FALSE
AND incident_tracking_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data origin artifacts provided for internal name/address resolution queries | [RULE-01], [RULE-02] |
| Integrity protection artifacts provided for internal name/address resolution queries | [RULE-01], [RULE-02], [RULE-03] |