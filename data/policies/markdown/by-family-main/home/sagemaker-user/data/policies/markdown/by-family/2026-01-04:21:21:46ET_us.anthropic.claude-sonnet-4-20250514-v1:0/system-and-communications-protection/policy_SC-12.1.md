# POLICY: SC-12(1): Availability

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12-1 |
| NIST Control | SC-12(1): Availability |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, key recovery, availability, escrow, backup, key loss |

## 1. POLICY STATEMENT
The organization SHALL maintain availability of information in the event of cryptographic key loss by users through established key recovery mechanisms. All cryptographic implementations MUST include provisions for key recovery to prevent permanent data loss due to forgotten passphrases, lost tokens, or other key compromise scenarios.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Systems using encryption for data protection |
| Cloud services | YES | Including third-party encrypted storage |
| Mobile devices | YES | Corporate and BYOD with encrypted data |
| Backup systems | YES | Encrypted backup and archive systems |
| Development environments | CONDITIONAL | Only if processing sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve key recovery policies and procedures<br>• Oversee key escrow program governance<br>• Ensure compliance with regulatory requirements |
| System Administrators | • Implement key recovery mechanisms<br>• Maintain key escrow systems<br>• Execute key recovery procedures when authorized |
| Data Owners | • Classify data requiring key recovery capabilities<br>• Approve key recovery requests for their data<br>• Define recovery time objectives |

## 4. RULES
[RULE-01] All systems using encryption for data protection MUST implement key recovery mechanisms that allow authorized recovery of encrypted information within 4 hours of approved request.
[VALIDATION] IF system_uses_encryption = TRUE AND key_recovery_mechanism = FALSE THEN violation

[RULE-02] Cryptographic keys used for data encryption SHALL be escrowed or backed up using FIPS 140-2 Level 3 or higher key management systems.
[VALIDATION] IF encryption_keys_escrowed = FALSE OR escrow_system_fips_level < 3 THEN violation

[RULE-03] Key recovery procedures MUST require dual authorization from data owner and security administrator before key release.
[VALIDATION] IF key_recovery_approvals < 2 OR (data_owner_approval = FALSE OR security_admin_approval = FALSE) THEN violation

[RULE-04] Escrowed keys SHALL be tested for recoverability at least quarterly and after any key management system changes.
[VALIDATION] IF days_since_last_key_recovery_test > 90 THEN violation

[RULE-05] Key recovery events MUST be logged with user identity, data accessed, business justification, and approving authorities.
[VALIDATION] IF key_recovery_event = TRUE AND (user_logged = FALSE OR justification_documented = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Key Escrow Setup - Establish secure key backup during initial encryption
- [PROC-02] Emergency Key Recovery - Expedited recovery process for business-critical systems
- [PROC-03] Key Recovery Testing - Quarterly validation of recovery capabilities
- [PROC-04] Key Recovery Audit - Monthly review of all recovery events and approvals

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Cryptographic system changes, failed recovery tests, regulatory updates, security incidents involving key loss

## 7. SCENARIO PATTERNS
[SCENARIO-01: Employee Forgotten Passphrase]
IF user_forgot_passphrase = TRUE
AND data_owner_approval = TRUE
AND security_admin_approval = TRUE
AND business_justification_provided = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unescrowable Encryption System]
IF system_uses_encryption = TRUE
AND key_recovery_mechanism = FALSE
AND system_in_production = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Key Recovery]
IF key_recovery_request_approved = TRUE
AND recovery_time > 4_hours
AND emergency_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Untested Key Escrow]
IF key_escrow_system = TRUE
AND days_since_last_test > 90
AND system_changes_occurred = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Single Authorization Recovery]
IF key_recovery_executed = TRUE
AND total_approvals = 1
AND emergency_override = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information availability maintained during key loss | [RULE-01], [RULE-02] |
| Key recovery mechanisms implemented | [RULE-01], [RULE-04] |
| Proper authorization controls | [RULE-03], [RULE-05] |
| Regular testing and validation | [RULE-04] |