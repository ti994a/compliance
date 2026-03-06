# POLICY: SC-12.1: Availability

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-12.1 |
| NIST Control | SC-12.1: Availability |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, key recovery, availability, escrow, backup, passphrase |

## 1. POLICY STATEMENT
The organization MUST maintain availability of information in the event users lose cryptographic keys. Key recovery mechanisms SHALL be implemented to ensure business continuity and data accessibility when cryptographic keys become unavailable due to user error, forgotten passphrases, or other key loss scenarios.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All encrypted data systems | YES | Including databases, file systems, applications |
| User-managed encryption keys | YES | Personal certificates, file encryption keys |
| System-managed keys | YES | Database encryption, application keys |
| Temporary/session keys | NO | Short-lived keys with acceptable recreation cost |
| Development environments | CONDITIONAL | If containing production data copies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve key recovery policies and procedures<br>• Ensure compliance with regulatory requirements<br>• Oversee key recovery capability testing |
| IT Security Manager | • Implement key escrow and recovery systems<br>• Manage key recovery procedures<br>• Monitor key recovery events and metrics |
| System Administrators | • Configure automated key backup mechanisms<br>• Execute key recovery procedures when authorized<br>• Maintain key recovery system availability |
| Data Owners | • Identify critical encrypted data requiring recovery capability<br>• Approve key recovery requests for their data<br>• Define recovery time objectives for their systems |

## 4. RULES
[RULE-01] All systems containing encrypted data MUST implement automated key backup or escrow mechanisms that enable data recovery without user intervention.
[VALIDATION] IF system_contains_encrypted_data = TRUE AND key_recovery_mechanism = FALSE THEN violation

[RULE-02] Key recovery mechanisms MUST be tested quarterly to verify successful data recovery within defined RTO parameters.
[VALIDATION] IF last_recovery_test > 90_days OR recovery_test_success = FALSE THEN violation

[RULE-03] Escrowed keys MUST be encrypted and stored separately from the data they protect with equivalent or stronger security controls.
[VALIDATION] IF escrow_location = data_location OR escrow_encryption < data_encryption_strength THEN critical_violation

[RULE-04] Key recovery procedures MUST be documented and executable by authorized personnel within 4 hours of a recovery request.
[VALIDATION] IF recovery_documentation = FALSE OR max_recovery_time > 4_hours THEN violation

[RULE-05] All key recovery events MUST be logged with dual approval and reviewed within 24 hours for unauthorized access attempts.
[VALIDATION] IF recovery_event_logged = FALSE OR approval_count < 2 OR review_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Key Escrow Setup - Establish automated key backup for new encrypted systems
- [PROC-02] Key Recovery Request - Process and authorize data recovery requests
- [PROC-03] Recovery Testing - Quarterly validation of key recovery capabilities
- [PROC-04] Emergency Recovery - Expedited procedures for critical business systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Failed recovery test, security incident involving key loss, regulatory changes, major system changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: User Loses File Encryption Key]
IF user_lost_key = TRUE
AND encrypted_data_exists = TRUE
AND key_escrow_available = TRUE
AND dual_approval_obtained = TRUE
THEN compliance = TRUE

[SCENARIO-02: Database Encryption Key Corruption]
IF system_key_corrupted = TRUE
AND automated_key_backup = FALSE
AND data_recovery_impossible = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Quarterly Recovery Test Failure]
IF recovery_test_performed = TRUE
AND test_success = FALSE
AND remediation_plan_created = FALSE
AND retest_scheduled > 30_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Key Recovery Without Proper Authorization]
IF key_recovery_performed = TRUE
AND approval_count < 2
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Escrow Key Storage Vulnerability]
IF escrow_keys_encrypted = FALSE
OR escrow_location = production_environment
OR escrow_access_controls < production_controls
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information availability maintained during key loss events | [RULE-01], [RULE-04] |
| Key recovery mechanisms properly implemented and tested | [RULE-02], [RULE-03] |
| Proper authorization and logging of recovery events | [RULE-05] |