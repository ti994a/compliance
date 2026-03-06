```markdown
# POLICY: IA-5.2: Public Key-based Authentication

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5.2 |
| NIST Control | IA-5.2: Public Key-based Authentication |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | PKI, public key, private key, certificates, authentication, revocation, trust anchor |

## 1. POLICY STATEMENT
The organization SHALL implement public key-based authentication with proper private key protection, identity mapping, and certificate validation. When PKI is used, certificate paths MUST be validated to trusted anchors with local revocation data caching.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Systems using public key authentication |
| Users (employees, contractors) | YES | Users with PKI certificates |
| Service accounts | YES | Automated systems using PKI |
| External partners | CONDITIONAL | When accessing company systems |
| Mobile devices | YES | Company-managed devices with certificates |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| PKI Administrator | • Manage certificate lifecycle<br>• Maintain trust anchors<br>• Configure revocation checking |
| System Administrator | • Implement private key protection<br>• Configure identity mapping<br>• Deploy local revocation cache |
| Security Team | • Monitor PKI compliance<br>• Validate certificate policies<br>• Audit authentication events |

## 4. RULES
[RULE-01] Private keys used for authentication MUST be protected with hardware security modules (HSMs) or equivalent cryptographic protection rated FIPS 140-2 Level 2 or higher.
[VALIDATION] IF private_key_protection != "HSM" AND protection_level < "FIPS_140-2_Level_2" THEN violation

[RULE-02] Authenticated identities MUST be mapped to specific user accounts within 5 seconds of successful certificate validation.
[VALIDATION] IF identity_mapping_time > 5_seconds OR mapping_failed = TRUE THEN violation

[RULE-03] Certificate validation MUST construct and verify a complete certification path to an approved trust anchor before granting access.
[VALIDATION] IF cert_path_complete = FALSE OR trust_anchor_approved = FALSE THEN critical_violation

[RULE-04] Certificate revocation status MUST be checked against current Certificate Revocation Lists (CRL) or Online Certificate Status Protocol (OCSP) responses.
[VALIDATION] IF revocation_check_performed = FALSE OR revocation_data_age > 24_hours THEN violation

[RULE-05] Local cache of revocation data MUST be maintained and updated at least every 4 hours to support offline validation.
[VALIDATION] IF local_cache_exists = FALSE OR cache_update_interval > 4_hours THEN violation

[RULE-06] PIV cards MUST validate against Common Policy Root trust anchor with certificate policy processing enabled.
[VALIDATION] IF card_type = "PIV" AND trust_anchor != "Common_Policy_Root" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Certificate Lifecycle Management - Issuance, renewal, and revocation processes
- [PROC-02] Private Key Escrow and Recovery - Secure key backup and restoration procedures  
- [PROC-03] Trust Anchor Management - Approval and maintenance of root certificates
- [PROC-04] Revocation Data Synchronization - Automated CRL/OCSP cache updates

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, certificate authority changes, trust anchor updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Expired Certificate Access Attempt]
IF certificate_status = "expired"
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Offline Revocation Validation]
IF network_connectivity = FALSE
AND local_cache_available = TRUE
AND cache_age < 4_hours
AND access_granted_with_cache = TRUE
THEN compliance = TRUE

[SCENARIO-03: Private Key Compromise Response]
IF private_key_compromised = TRUE
AND certificate_revoked_within = 1_hour
AND access_blocked = TRUE
THEN compliance = TRUE

[SCENARIO-04: Invalid Certificate Chain]
IF cert_chain_valid = FALSE
AND trust_anchor_reachable = FALSE
AND access_denied = TRUE
THEN compliance = TRUE

[SCENARIO-05: PIV Card Authentication]
IF authentication_method = "PIV"
AND trust_anchor = "Common_Policy_Root"
AND policy_processing = "enabled"
AND identity_mapped = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authorized access to corresponding private key is enforced | [RULE-01] |
| Authenticated identity is mapped to account of individual or group | [RULE-02] |
| Certificates validated by constructing certification path to trust anchor | [RULE-03] |
| Certificate status information is checked | [RULE-04] |
| Local cache of revocation data implemented | [RULE-05] |
```