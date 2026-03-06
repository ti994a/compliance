# POLICY: SC-34.2: Integrity Protection on Read-only Media

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-34.2 |
| NIST Control | SC-34.2: Integrity Protection on Read-only Media |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | read-only media, integrity protection, media control, programmable media, substitution prevention |

## 1. POLICY STATEMENT
The organization must protect the integrity of information prior to storage on read-only media and maintain strict control over such media after information has been recorded. This includes preventing unauthorized media substitution and reprogramming of programmable read-only media before installation into organizational systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Read-only media (CD-ROM, DVD-ROM, firmware) | YES | All media containing organizational data |
| Programmable read-only media (PROM, EPROM) | YES | Including firmware and embedded software |
| System firmware and BIOS | YES | Critical system components |
| Software distribution media | YES | Installation and update media |
| Third-party media | YES | Vendor-supplied media and components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Media Control Officer | • Oversee media integrity verification processes<br>• Maintain chain of custody for read-only media<br>• Approve media handling procedures |
| System Administrators | • Verify media integrity before installation<br>• Document media control activities<br>• Report integrity violations |
| Security Team | • Conduct integrity assessments<br>• Investigate media tampering incidents<br>• Maintain detection capabilities |

## 4. RULES
[RULE-01] All information MUST undergo integrity verification using cryptographic hash functions before being written to read-only media.
[VALIDATION] IF media_type = "read-only" AND pre_storage_hash_verification = FALSE THEN violation

[RULE-02] Read-only media containing organizational information MUST be stored in physically secured locations with access logging.
[VALIDATION] IF media_storage_location = "unsecured" OR access_logging = FALSE THEN violation

[RULE-03] Programmable read-only media MUST be write-protected immediately after information recording and verified before system installation.
[VALIDATION] IF media_type = "programmable_ROM" AND (write_protection = FALSE OR pre_install_verification = FALSE) THEN violation

[RULE-04] Media substitution prevention controls MUST include tamper-evident packaging and chain of custody documentation.
[VALIDATION] IF tamper_evident_packaging = FALSE OR chain_of_custody_documented = FALSE THEN violation

[RULE-05] All read-only media MUST be scanned for malware and integrity checked within 24 hours before system installation.
[VALIDATION] IF malware_scan_age > 24_hours OR integrity_check_age > 24_hours THEN violation

[RULE-06] Media control logs MUST be maintained for a minimum of 3 years and include creation, storage, and disposal activities.
[VALIDATION] IF log_retention_period < 3_years OR missing_activity_logs = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Integrity Verification - Cryptographic hash verification before storage
- [PROC-02] Secure Media Storage - Physical security and access control procedures
- [PROC-03] Chain of Custody Management - Documentation and tracking procedures
- [PROC-04] Pre-Installation Verification - Malware scanning and integrity checking
- [PROC-05] Incident Response - Response to media tampering or integrity violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving media, technology changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Firmware Installation]
IF media_type = "firmware"
AND pre_install_verification = TRUE
AND hash_verification = TRUE
AND tamper_evident_packaging = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unverified Media Installation]
IF media_type = "read-only"
AND pre_install_verification = FALSE
AND system_installation = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Compromised Chain of Custody]
IF chain_of_custody_documented = FALSE
OR custody_gap_detected = TRUE
AND media_contains_sensitive_data = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Expired Verification]
IF integrity_check_age > 24_hours
AND media_installation_pending = TRUE
AND re_verification_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Media Handling]
IF tamper_evident_packaging = TRUE
AND chain_of_custody_documented = TRUE
AND integrity_verification = "PASSED"
AND storage_location = "secured"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Integrity protection prior to storage | RULE-01 |
| Media control after recording | RULE-02, RULE-06 |
| Prevention of media substitution | RULE-04 |
| Programmable media protection | RULE-03 |
| Pre-installation verification | RULE-05 |