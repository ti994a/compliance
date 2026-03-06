```markdown
# POLICY: SI-7.6: Cryptographic Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.6 |
| NIST Control | SI-7.6: Cryptographic Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic mechanisms, integrity protection, digital signatures, hash verification, unauthorized changes, software integrity, firmware integrity |

## 1. POLICY STATEMENT
The organization SHALL implement cryptographic mechanisms to detect unauthorized changes to software, firmware, and information assets. All cryptographic integrity protection MUST use approved algorithms and include proper key management procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Software | YES | All deployed applications and system software |
| Development Software | YES | Code repositories and build artifacts |
| System Firmware | YES | BIOS, UEFI, embedded device firmware |
| Critical Information | YES | Sensitive data requiring integrity protection |
| Test Environments | CONDITIONAL | When processing production-like data |
| Third-party Software | YES | All vendor-supplied components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Team | • Implement and maintain cryptographic integrity mechanisms<br>• Monitor for integrity violations<br>• Respond to unauthorized change alerts |
| System Administrators | • Configure hash verification systems<br>• Maintain baseline integrity measurements<br>• Execute integrity verification procedures |
| Cryptographic Officer | • Approve cryptographic algorithms and implementations<br>• Manage cryptographic keys for integrity protection<br>• Oversee key lifecycle management |

## 4. RULES
[RULE-01] All software deployed to production systems MUST have cryptographic hash verification implemented using FIPS 140-2 approved algorithms.
[VALIDATION] IF software_deployment = TRUE AND hash_verification = FALSE THEN critical_violation

[RULE-02] Firmware integrity verification MUST be performed using digital signatures from trusted certificate authorities or organizational PKI.
[VALIDATION] IF firmware_type IN ["BIOS", "UEFI", "embedded"] AND signature_verification = FALSE THEN critical_violation

[RULE-03] Critical information assets MUST be protected with cryptographic mechanisms that detect unauthorized modifications within 15 minutes of occurrence.
[VALIDATION] IF asset_criticality = "high" AND detection_time > 15_minutes THEN violation

[RULE-04] Cryptographic keys used for integrity protection MUST be managed according to NIST SP 800-57 key management requirements.
[VALIDATION] IF key_management_compliance = FALSE THEN violation

[RULE-05] Integrity verification failures MUST trigger automated alerts to security operations within 5 minutes of detection.
[VALIDATION] IF integrity_failure = TRUE AND alert_time > 5_minutes THEN violation

[RULE-06] Software and firmware baseline measurements MUST be updated within 24 hours of authorized changes.
[VALIDATION] IF authorized_change = TRUE AND baseline_update_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cryptographic Integrity Implementation - Deploy and configure hash verification systems
- [PROC-02] Baseline Management - Establish and maintain integrity baselines for software and firmware
- [PROC-03] Key Management - Generate, distribute, and rotate cryptographic keys for integrity protection
- [PROC-04] Incident Response - Respond to integrity verification failures and unauthorized changes
- [PROC-05] Algorithm Assessment - Evaluate and approve cryptographic algorithms for integrity protection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Cryptographic standard updates, integrity breach incidents, new system deployments, regulatory requirement changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production Software Deployment]
IF deployment_target = "production"
AND software_type = "application"
AND hash_verification = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Firmware Update Verification]
IF component_type = "firmware"
AND digital_signature_present = TRUE
AND signature_validation = "passed"
AND ca_trusted = TRUE
THEN compliance = TRUE

[SCENARIO-03: Critical Data Modification Detection]
IF data_classification = "critical"
AND unauthorized_change_detected = TRUE
AND detection_time <= 15_minutes
AND alert_generated = TRUE
THEN compliance = TRUE

[SCENARIO-04: Legacy System Exception]
IF system_age > 5_years
AND cryptographic_capability = FALSE
AND compensating_controls = FALSE
AND risk_acceptance = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Third-party Software Integration]
IF software_source = "third_party"
AND vendor_signature_verified = TRUE
AND hash_verification_enabled = TRUE
AND baseline_established = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic mechanisms implemented for software integrity detection | [RULE-01] |
| Cryptographic mechanisms implemented for firmware integrity detection | [RULE-02] |
| Cryptographic mechanisms implemented for information integrity detection | [RULE-03] |
| Proper cryptographic key management | [RULE-04] |
| Timely detection and alerting | [RULE-05] |
| Baseline maintenance | [RULE-06] |
```