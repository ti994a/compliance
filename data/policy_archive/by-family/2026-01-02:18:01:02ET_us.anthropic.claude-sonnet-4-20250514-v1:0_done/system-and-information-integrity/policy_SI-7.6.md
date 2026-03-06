# POLICY: SI-7.6: Cryptographic Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.6 |
| NIST Control | SI-7.6: Cryptographic Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic protection, integrity verification, digital signatures, hash validation, unauthorized changes |

## 1. POLICY STATEMENT
The organization SHALL implement cryptographic mechanisms to detect unauthorized changes to software, firmware, and information assets. All critical system components and data must be protected using approved cryptographic integrity verification methods including digital signatures and cryptographic hashes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Software | YES | All deployed applications and system software |
| System Firmware | YES | BIOS, UEFI, embedded device firmware |
| Critical Information | YES | Regulated data, configuration files, security policies |
| Development Code | CONDITIONAL | Pre-production code in staging environments |
| Personal Devices | CONDITIONAL | Only if processing company data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Team | • Implement and maintain cryptographic integrity mechanisms<br>• Monitor for integrity violations<br>• Respond to unauthorized change alerts |
| System Administrators | • Deploy approved cryptographic tools<br>• Configure integrity verification processes<br>• Maintain cryptographic key management |
| Development Teams | • Implement code signing processes<br>• Integrate integrity checks into CI/CD pipelines<br>• Document cryptographic implementations |

## 4. RULES
[RULE-01] All production software MUST be protected by digital signatures using approved cryptographic algorithms (RSA-2048, ECDSA P-256, or higher).
[VALIDATION] IF software_environment = "production" AND digital_signature_present = FALSE THEN critical_violation

[RULE-02] System firmware MUST implement cryptographic hash verification with SHA-256 or stronger algorithms before loading.
[VALIDATION] IF firmware_type = "system" AND hash_algorithm IN ["MD5", "SHA-1"] THEN critical_violation

[RULE-03] Critical information assets MUST have cryptographic integrity protection implemented within 30 days of classification as critical.
[VALIDATION] IF asset_classification = "critical" AND days_since_classification > 30 AND cryptographic_protection = FALSE THEN violation

[RULE-04] Cryptographic key management for integrity verification MUST follow NIST SP 800-57 guidelines with key rotation every 24 months maximum.
[VALIDATION] IF key_age > 24_months AND key_type = "integrity_verification" THEN violation

[RULE-05] Unauthorized change detection MUST trigger automated alerts within 15 minutes of detection.
[VALIDATION] IF unauthorized_change_detected = TRUE AND alert_time > 15_minutes THEN violation

[RULE-06] All cryptographic mechanisms used for integrity verification MUST be FIPS 140-2 Level 2 validated or higher.
[VALIDATION] IF cryptographic_module_validation < "FIPS_140-2_Level_2" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cryptographic Algorithm Selection - Process for selecting and approving cryptographic algorithms
- [PROC-02] Digital Signature Implementation - Procedures for implementing code and document signing
- [PROC-03] Integrity Violation Response - Incident response procedures for detected unauthorized changes
- [PROC-04] Key Management Operations - Cryptographic key lifecycle management procedures
- [PROC-05] Firmware Verification - Process for verifying firmware integrity before deployment

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Cryptographic standard updates, security incidents involving integrity violations, regulatory changes, technology refresh cycles

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production Software Deployment]
IF software_environment = "production"
AND deployment_method = "automated"
AND digital_signature_verified = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Firmware Update Process]
IF component_type = "firmware"
AND update_source = "vendor"
AND cryptographic_hash_verified = TRUE
AND hash_algorithm = "SHA-256"
THEN compliance = TRUE

[SCENARIO-03: Critical Data Integrity]
IF data_classification = "critical"
AND cryptographic_protection = TRUE
AND detection_mechanism = "real-time"
AND alert_generated = TRUE
THEN compliance = TRUE

[SCENARIO-04: Legacy System Exception]
IF system_age > 5_years
AND cryptographic_capability = "limited"
AND compensating_controls = FALSE
AND risk_acceptance = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Key Management Compliance]
IF key_type = "integrity_verification"
AND key_rotation_frequency <= 24_months
AND key_storage = "FIPS_140-2_Level_2"
AND access_controls = "implemented"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic mechanisms implemented for software | [RULE-01] |
| Cryptographic mechanisms implemented for firmware | [RULE-02] |
| Cryptographic mechanisms implemented for information | [RULE-03] |
| Key management compliance | [RULE-04] |
| Detection and alerting capability | [RULE-05] |
| Approved cryptographic standards | [RULE-06] |