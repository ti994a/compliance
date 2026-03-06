```markdown
# POLICY: AC-19.5: Full Device or Container-based Encryption

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-19.5 |
| NIST Control | AC-19.5: Full Device or Container-based Encryption |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mobile device encryption, full-device encryption, container encryption, confidentiality, integrity, data protection |

## 1. POLICY STATEMENT
All mobile devices accessing organizational information systems MUST employ full-device encryption or approved container-based encryption to protect the confidentiality and integrity of organizational data. Encryption implementation SHALL follow organizational cryptographic standards and approved encryption algorithms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Corporate-owned mobile devices | YES | All smartphones, tablets, laptops |
| BYOD mobile devices | YES | When accessing organizational data |
| Guest devices | YES | When granted temporary access |
| IoT devices | CONDITIONAL | Only if capable of storing organizational data |
| Air-gapped devices | NO | Separate policy applies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve encryption standards and algorithms<br>• Define mobile device encryption requirements<br>• Oversee compliance monitoring |
| IT Security Team | • Implement encryption solutions<br>• Monitor encryption compliance<br>• Conduct encryption validation testing |
| Device Administrators | • Configure device encryption settings<br>• Verify encryption status during provisioning<br>• Maintain encryption key management |
| End Users | • Maintain device encryption settings<br>• Report encryption failures immediately<br>• Comply with device security requirements |

## 4. RULES
[RULE-01] All mobile devices accessing organizational systems MUST employ full-device encryption using FIPS 140-2 Level 1 or higher validated cryptographic modules.
[VALIDATION] IF device_type = "mobile" AND organizational_access = TRUE AND encryption_level < "FIPS_140-2_Level_1" THEN critical_violation

[RULE-02] Container-based encryption MAY be used as an alternative to full-device encryption only when approved by the CISO and meeting AES-256 minimum standards.
[VALIDATION] IF encryption_type = "container" AND ciso_approval = FALSE THEN violation

[RULE-03] Encryption keys MUST be managed through approved enterprise key management systems and SHALL NOT be stored locally on the device.
[VALIDATION] IF key_storage = "local_device" THEN critical_violation

[RULE-04] Mobile devices with failed or disabled encryption MUST be immediately disconnected from organizational networks and reported within 4 hours.
[VALIDATION] IF encryption_status = "failed" AND network_access = TRUE AND report_time > 4_hours THEN violation

[RULE-05] Encryption compliance verification MUST be performed during initial device provisioning and monthly thereafter.
[VALIDATION] IF last_encryption_check > 30_days THEN violation

[RULE-06] Lost or stolen encrypted mobile devices MUST be reported immediately and remote wipe capabilities SHALL be activated within 2 hours.
[VALIDATION] IF device_status = "lost_stolen" AND remote_wipe_time > 2_hours THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Mobile Device Encryption Implementation - Standard procedures for configuring and validating device encryption
- [PROC-02] Encryption Compliance Monitoring - Automated and manual verification processes
- [PROC-03] Key Management for Mobile Devices - Enterprise key lifecycle management procedures
- [PROC-04] Incident Response for Encryption Failures - Response procedures for encryption-related security events
- [PROC-05] BYOD Encryption Onboarding - Procedures for personal device encryption validation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Cryptographic standard updates, security incidents involving mobile devices, regulatory requirement changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: BYOD Device Access]
IF device_ownership = "personal"
AND organizational_data_access = TRUE
AND encryption_status = "none"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Container Encryption Alternative]
IF encryption_type = "container"
AND encryption_standard = "AES-256"
AND ciso_approval = TRUE
AND key_management = "enterprise"
THEN compliance = TRUE

[SCENARIO-03: Failed Encryption Detection]
IF encryption_status = "failed"
AND detection_time < current_time - 4_hours
AND network_disconnection = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Legacy Device Exception]
IF device_age > 5_years
AND encryption_capability = "limited"
AND business_justification = TRUE
AND compensating_controls = TRUE
AND ciso_exception = TRUE
THEN compliance = TRUE

[SCENARIO-05: Remote Worker Laptop]
IF device_type = "laptop"
AND work_location = "remote"
AND full_disk_encryption = TRUE
AND encryption_standard = "FIPS_140-2_Level_1"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Full-device encryption employed on mobile devices | [RULE-01] |
| Container-based encryption as approved alternative | [RULE-02] |
| Encryption protects confidentiality and integrity | [RULE-01], [RULE-02] |
| Proper key management implementation | [RULE-03] |
| Continuous encryption compliance monitoring | [RULE-05] |
| Incident response for encryption failures | [RULE-04], [RULE-06] |
```