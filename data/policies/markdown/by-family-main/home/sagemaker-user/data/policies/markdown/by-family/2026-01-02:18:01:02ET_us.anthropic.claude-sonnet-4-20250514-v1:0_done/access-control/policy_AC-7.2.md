# POLICY: AC-7.2: Purge or Wipe Mobile Device

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-7.2 |
| NIST Control | AC-7.2: Purge or Wipe Mobile Device |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mobile device, purge, wipe, unsuccessful logon, data protection, device security |

## 1. POLICY STATEMENT
Organization-managed mobile devices MUST automatically purge or wipe stored information after a defined number of consecutive unsuccessful logon attempts to prevent unauthorized access to organizational data. This control applies to device-level authentication failures and includes both full data wiping and selective purging based on data classification and device management capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Corporate mobile devices | YES | All organization-owned smartphones, tablets, laptops |
| BYOD devices with corporate data | YES | Only corporate data partitions/containers |
| Personal devices without corporate access | NO | Outside organizational control |
| IoT/embedded mobile devices | CONDITIONAL | If capable of storing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Define purge/wipe thresholds by device type<br>• Configure mobile device management (MDM) policies<br>• Monitor purge/wipe events and investigate triggers |
| IT Operations Team | • Implement technical controls on mobile devices<br>• Maintain device inventory and compliance status<br>• Execute emergency remote wipe procedures |
| Device Users | • Report lost or stolen devices immediately<br>• Comply with device authentication requirements<br>• Understand data backup and recovery procedures |

## 4. RULES
[RULE-01] Mobile devices containing organizational data MUST be configured to automatically purge or wipe after no more than 10 consecutive unsuccessful logon attempts for standard sensitivity data and no more than 5 attempts for high sensitivity data.
[VALIDATION] IF device_sensitivity = "standard" AND failed_attempts > 10 THEN violation
[VALIDATION] IF device_sensitivity = "high" AND failed_attempts > 5 THEN violation

[RULE-02] Purge/wipe mechanisms MUST distinguish between device-level authentication failures and individual application/account failures, applying the control only to device-level failures.
[VALIDATION] IF purge_trigger = "application_failure" AND device_authentication = "successful" THEN violation

[RULE-03] Successful device logon MUST reset the unsuccessful attempt counter to zero.
[VALIDATION] IF successful_logon = TRUE AND attempt_counter ≠ 0 THEN violation

[RULE-04] Devices with sufficiently strong encryption (AES-256 or equivalent) MAY be exempted from automatic purge/wipe requirements with documented risk acceptance.
[VALIDATION] IF encryption_strength < "AES-256" AND purge_exemption = TRUE AND risk_acceptance = FALSE THEN violation

[RULE-05] All purge/wipe events MUST be logged and reported to the security operations center within 24 hours.
[VALIDATION] IF purge_event = TRUE AND log_created = FALSE THEN violation
[VALIDATION] IF purge_event = TRUE AND soc_notification_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Mobile Device Purge/Wipe Configuration - Standard process for configuring automatic purge/wipe thresholds on mobile devices
- [PROC-02] Emergency Remote Wipe - Procedures for immediate remote wiping of lost or stolen devices
- [PROC-03] Data Recovery and Restoration - Process for restoring organizational data after legitimate purge/wipe events
- [PROC-04] Purge/Wipe Event Investigation - Analysis procedures for all automatic and manual purge/wipe events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving mobile devices, changes to mobile device technology, updates to data classification standards

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Device Exceeded Attempts]
IF device_type = "corporate_smartphone"
AND data_classification = "internal"
AND consecutive_failed_attempts = 11
AND auto_purge_enabled = TRUE
THEN compliance = TRUE

[SCENARIO-02: High Sensitivity Device Violation]
IF device_contains_data = "confidential"
AND consecutive_failed_attempts = 7
AND purge_threshold_configured = 10
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Encrypted Device Exemption]
IF device_encryption = "AES-256"
AND purge_exemption = TRUE
AND risk_acceptance_documented = TRUE
AND security_officer_approval = TRUE
THEN compliance = TRUE

[SCENARIO-04: Missing Purge Logging]
IF purge_event_occurred = TRUE
AND event_logged = FALSE
AND time_since_event > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Application vs Device Authentication]
IF failed_authentication_type = "email_app"
AND device_unlock = "successful"
AND purge_triggered = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Define number of unsuccessful attempts before purge/wipe | [RULE-01] |
| Implement purge/wipe after defined attempts | [RULE-01], [RULE-02] |
| Reset counter on successful logon | [RULE-03] |
| Document purge/wipe requirements and techniques | [RULE-04] |
| Log and monitor purge/wipe events | [RULE-05] |