# POLICY: SI-7.6: Cryptographic Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.6 |
| NIST Control | SI-7.6: Cryptographic Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic mechanisms, digital signatures, hash verification, integrity protection, unauthorized changes |

## 1. POLICY STATEMENT
The organization SHALL implement cryptographic mechanisms to detect unauthorized changes to software, firmware, and information assets. All cryptographic integrity protection mechanisms MUST use approved algorithms and include comprehensive key management processes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production software | YES | All executable code in production |
| Firmware | YES | System and device firmware |
| Critical data | YES | As defined by data classification |
| Development environments | CONDITIONAL | If processing production data |
| Third-party software | YES | All deployed third-party components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Architecture Team | • Design cryptographic integrity mechanisms<br>• Define approved algorithms and key sizes<br>• Establish verification procedures |
| System Administrators | • Implement integrity monitoring tools<br>• Monitor cryptographic verification alerts<br>• Maintain cryptographic key infrastructure |
| Development Teams | • Implement code signing processes<br>• Generate and verify digital signatures<br>• Document integrity verification procedures |

## 4. RULES
[RULE-01] All production software MUST be protected by digital signatures using approved cryptographic algorithms (RSA-2048+ or ECDSA-256+).
[VALIDATION] IF software_environment = "production" AND (digital_signature = FALSE OR algorithm NOT IN approved_list) THEN violation

[RULE-02] Firmware integrity verification MUST be performed using cryptographic hashes (SHA-256 minimum) before installation and at system boot.
[VALIDATION] IF firmware_verification = FALSE OR hash_algorithm_strength < SHA-256 THEN critical_violation

[RULE-03] Critical and sensitive information MUST be protected by cryptographic integrity mechanisms with verification performed at least every 24 hours.
[VALIDATION] IF data_classification IN ["critical", "sensitive"] AND integrity_check_interval > 24_hours THEN violation

[RULE-04] Cryptographic keys used for integrity protection MUST be managed through approved key management systems with role-based access controls.
[VALIDATION] IF integrity_key_management != "approved_kms" OR rbac_enabled = FALSE THEN violation

[RULE-05] Unauthorized change detection MUST trigger automated alerts within 15 minutes and initiate incident response procedures.
[VALIDATION] IF unauthorized_change_detected = TRUE AND alert_time > 15_minutes THEN violation

[RULE-06] All cryptographic integrity mechanisms MUST use FIPS 140-2 Level 2 or higher validated modules for key operations.
[VALIDATION] IF cryptographic_module_validation < "FIPS_140-2_Level_2" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cryptographic Algorithm Selection - Process for evaluating and approving cryptographic algorithms
- [PROC-02] Digital Signature Implementation - Procedures for code and firmware signing
- [PROC-03] Integrity Verification Monitoring - Automated monitoring and alerting procedures
- [PROC-04] Key Management Lifecycle - Key generation, distribution, rotation, and revocation
- [PROC-05] Incident Response for Integrity Violations - Response procedures for detected unauthorized changes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Cryptographic standard updates, security incidents, regulatory changes, technology refresh

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production Software Deployment]
IF software_type = "production"
AND digital_signature = FALSE
AND deployment_approved = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Firmware Update Process]
IF component_type = "firmware"
AND cryptographic_verification = TRUE
AND hash_algorithm = "SHA-256"
AND verification_timing = "pre-installation"
THEN compliance = TRUE

[SCENARIO-03: Legacy System Exception]
IF system_age > 5_years
AND fips_validation = FALSE
AND documented_exception = TRUE
AND compensating_controls = TRUE
THEN compliance = CONDITIONAL
requires_review = TRUE

[SCENARIO-04: Unauthorized Change Detection]
IF integrity_violation_detected = TRUE
AND alert_generated = TRUE
AND response_time <= 15_minutes
AND incident_created = TRUE
THEN compliance = TRUE

[SCENARIO-05: Third-Party Software Verification]
IF software_source = "third-party"
AND digital_signature_verified = FALSE
AND production_deployment = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic mechanisms for software integrity | [RULE-01] |
| Cryptographic mechanisms for firmware integrity | [RULE-02] |
| Cryptographic mechanisms for information integrity | [RULE-03] |
| Key management for integrity protection | [RULE-04] |
| Detection and response capabilities | [RULE-05] |
| Cryptographic module validation | [RULE-06] |