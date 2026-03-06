# POLICY: SC-34.2: Integrity Protection on Read-only Media

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-34.2 |
| NIST Control | SC-34.2: Integrity Protection on Read-only Media |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | read-only media, integrity protection, media control, storage protection, programmable media |

## 1. POLICY STATEMENT
The organization SHALL protect the integrity of information prior to storage on read-only media and maintain strict control over such media after information recording. All read-only media must undergo integrity verification before deployment and be subject to continuous custody controls to prevent unauthorized substitution or tampering.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Read-only storage media | YES | CD-ROM, DVD-ROM, Blu-ray, EPROM, firmware |
| Programmable read-only media | YES | PROM, EPROM, EEPROM, flash memory |
| System firmware/BIOS | YES | Boot firmware, embedded system code |
| Software distribution media | YES | Installation media, update packages |
| Temporary storage devices | NO | RAM, cache memory excluded |
| Network-attached storage | NO | Unless specifically configured as read-only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Media Custodian | • Verify integrity before media creation<br>• Maintain chain of custody documentation<br>• Perform pre-installation validation |
| System Administrator | • Implement media control procedures<br>• Monitor for unauthorized media substitution<br>• Execute integrity verification protocols |
| Security Officer | • Audit media handling processes<br>• Investigate integrity violations<br>• Approve media handling exceptions |

## 4. RULES
[RULE-01] All information MUST undergo cryptographic integrity verification before storage on read-only media.
[VALIDATION] IF media_type = "read_only" AND integrity_check = FALSE THEN critical_violation

[RULE-02] Read-only media SHALL be stored in controlled access environments with documented chain of custody from creation to deployment.
[VALIDATION] IF custody_documentation = "incomplete" OR storage_environment != "controlled" THEN violation

[RULE-03] Programmable read-only media MUST be write-protected immediately after information recording and before system installation.
[VALIDATION] IF media_type = "programmable_readonly" AND write_protection = FALSE AND installation_status = "pending" THEN critical_violation

[RULE-04] Media integrity verification MUST be performed within 24 hours before installation into production systems.
[VALIDATION] IF installation_type = "production" AND verification_age > 24_hours THEN violation

[RULE-05] Unauthorized media substitution detection mechanisms SHALL be implemented and monitored continuously.
[VALIDATION] IF substitution_detection = "disabled" OR monitoring_status = "inactive" THEN violation

[RULE-06] All read-only media MUST be labeled with integrity hash values and creation timestamps.
[VALIDATION] IF integrity_hash = "missing" OR creation_timestamp = "missing" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Integrity Verification - Cryptographic hash validation before storage
- [PROC-02] Chain of Custody Management - Documentation and tracking procedures
- [PROC-03] Pre-Installation Validation - Integrity check before system deployment
- [PROC-04] Substitution Detection - Monitoring and alerting mechanisms
- [PROC-05] Incident Response - Response to integrity violations or unauthorized media

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving media, technology changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production Media Deployment]
IF media_type = "read_only"
AND environment = "production"
AND integrity_verification = "passed"
AND custody_chain = "documented"
THEN compliance = TRUE

[SCENARIO-02: Unverified Media Installation]
IF media_integrity_check = FALSE
AND installation_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Expired Verification Window]
IF verification_timestamp < (current_time - 24_hours)
AND installation_type = "production"
AND media_deployed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Chain of Custody]
IF custody_documentation = "incomplete"
AND media_location = "production_system"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Programmable Media Without Write Protection]
IF media_type = "programmable_readonly"
AND write_protection = FALSE
AND data_recorded = TRUE
AND storage_duration > 0
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Integrity protection prior to storage | [RULE-01], [RULE-06] |
| Media control after recording | [RULE-02], [RULE-03] |
| Prevention of substitution | [RULE-05] |
| Pre-installation validation | [RULE-04] |