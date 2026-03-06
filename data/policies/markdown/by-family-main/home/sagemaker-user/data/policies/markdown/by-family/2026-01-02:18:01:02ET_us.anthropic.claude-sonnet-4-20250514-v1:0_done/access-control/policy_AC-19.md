# POLICY: AC-19: Access Control for Mobile Devices

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-19 |
| NIST Control | AC-19: Access Control for Mobile Devices |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mobile devices, access control, configuration management, device authorization, endpoint security |

## 1. POLICY STATEMENT
The organization SHALL establish configuration requirements, connection requirements, and implementation guidance for all organization-controlled mobile devices accessing organizational systems. All mobile device connections to organizational systems MUST be explicitly authorized and comply with established security controls regardless of device location.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Organization-controlled mobile devices | YES | Smartphones, tablets, mobile workstations |
| Personal mobile devices (BYOD) | CONDITIONAL | Only if connecting to org systems |
| IoT/embedded mobile devices | YES | If capable of system connectivity |
| Contractor mobile devices | YES | When accessing org systems |
| Guest mobile devices | NO | Covered under AC-20 |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Manager | • Establish mobile device security requirements<br>• Approve mobile device connection authorizations<br>• Monitor mobile device compliance |
| Device Administrators | • Configure mobile devices per security standards<br>• Deploy and maintain mobile device management (MDM)<br>• Perform device compliance validation |
| End Users | • Comply with mobile device usage restrictions<br>• Report lost/stolen devices within required timeframes<br>• Maintain physical control of devices |

## 4. RULES

[RULE-01] All organization-controlled mobile devices MUST be enrolled in the approved Mobile Device Management (MDM) solution before accessing organizational systems.
[VALIDATION] IF device_type = "mobile" AND mdm_enrolled = FALSE AND system_access_attempted = TRUE THEN violation

[RULE-02] Mobile devices SHALL implement mandatory security configurations including device encryption, screen lock with maximum 15-minute timeout, and remote wipe capability.
[VALIDATION] IF mobile_device = TRUE AND (encryption_enabled = FALSE OR screen_timeout > 15_minutes OR remote_wipe_capable = FALSE) THEN violation

[RULE-03] Mobile device connections to organizational systems MUST be explicitly authorized by IT Security Manager or designated authority before initial access.
[VALIDATION] IF mobile_device_connection = TRUE AND authorization_status = "pending" OR "denied" THEN critical_violation

[RULE-04] Users MUST report lost or stolen mobile devices to IT Security within 4 hours of discovery during business hours or by start of next business day.
[VALIDATION] IF device_status = "lost" OR "stolen" AND report_time > 4_hours AND business_hours = TRUE THEN violation

[RULE-05] Mobile devices accessing organizational data MUST run approved anti-malware software with definitions updated within 7 days.
[VALIDATION] IF system_access = TRUE AND (antimalware_installed = FALSE OR definition_age > 7_days) THEN violation

[RULE-06] Jailbroken or rooted mobile devices SHALL NOT be permitted to connect to organizational systems.
[VALIDATION] IF (jailbroken = TRUE OR rooted = TRUE) AND system_connection_attempted = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Mobile Device Enrollment - Device registration and MDM deployment process
- [PROC-02] Mobile Device Authorization - Formal approval process for system connections
- [PROC-03] Lost/Stolen Device Response - Incident response and device remote wipe procedures
- [PROC-04] Mobile Device Compliance Monitoring - Regular assessment of device security posture

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving mobile devices, technology changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unmanaged Device Access]
IF device_type = "mobile"
AND mdm_enrolled = FALSE
AND organizational_system_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delayed Lost Device Reporting]
IF device_status = "lost"
AND discovery_time_business_hours = TRUE
AND report_delay > 4_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Compromised Device Detection]
IF mobile_device = TRUE
AND (jailbroken = TRUE OR rooted = TRUE)
AND system_connection_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Outdated Security Controls]
IF mobile_device_managed = TRUE
AND (antimalware_definitions > 7_days OR os_patch_level = "critical_missing")
AND organizational_data_access = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Mobile Device Usage]
IF device_type = "mobile"
AND mdm_enrolled = TRUE
AND authorization_status = "approved"
AND security_controls_compliant = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Configuration requirements established | RULE-02, RULE-05 |
| Connection requirements established | RULE-01, RULE-03 |
| Implementation guidance established | RULE-02, RULE-06 |
| Mobile device connections authorized | RULE-03 |