```markdown
# POLICY: SC-42: Sensor Capability and Data

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-42 |
| NIST Control | SC-42: Sensor Capability and Data |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | sensors, mobile devices, privacy, location tracking, cameras, microphones, GPS, covert surveillance |

## 1. POLICY STATEMENT
This policy prohibits the use of devices with specified sensor capabilities in designated controlled areas and requires explicit indication when sensors are actively collecting data. Organizations must implement controls to prevent covert sensor activation and protect against unauthorized data collection in sensitive environments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Mobile Devices | YES | Smartphones, tablets, wearables with sensors |
| IoT Devices | YES | Connected devices with sensor capabilities |
| Contractor Equipment | YES | Personal and company-issued devices |
| Visitor Devices | YES | All devices entering controlled areas |
| Fixed Sensors | CONDITIONAL | Only if remotely activatable |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facility Security Manager | • Define controlled areas and sensor restrictions<br>• Implement physical controls and signage<br>• Monitor compliance in restricted zones |
| IT Security Team | • Configure sensor controls on managed devices<br>• Implement technical controls for sensor indication<br>• Monitor for unauthorized sensor activation |
| Device Users | • Comply with sensor restrictions in controlled areas<br>• Report suspicious sensor activity<br>• Maintain awareness of sensor status indicators |

## 4. RULES

[RULE-01] Devices with cameras, microphones, GPS, or accelerometers MUST be prohibited in classified information storage areas, secure meeting rooms, and other designated controlled areas.
[VALIDATION] IF device_location = "controlled_area" AND device_has_sensors = TRUE AND authorization_exception = FALSE THEN violation

[RULE-02] All sensor-capable devices MUST provide explicit visual or audible indication when sensors are actively collecting data.
[VALIDATION] IF sensor_active = TRUE AND user_indication = FALSE THEN violation

[RULE-03] Organizations MUST maintain a documented list of controlled areas where sensor-capable devices are prohibited or restricted.
[VALIDATION] IF controlled_areas_documented = FALSE OR last_review_date > 12_months THEN violation

[RULE-04] Remote activation of device sensors MUST be technically prevented or require explicit user consent with clear indication.
[VALIDATION] IF remote_sensor_activation = TRUE AND user_consent = FALSE THEN critical_violation

[RULE-05] Visitors and contractors MUST be informed of sensor restrictions before entering controlled areas and surrender non-compliant devices.
[VALIDATION] IF visitor_briefed = FALSE AND entered_controlled_area = TRUE THEN violation

[RULE-06] Managed mobile devices MUST have sensor controls configured to disable unauthorized sensor activation and provide usage indicators.
[VALIDATION] IF managed_device = TRUE AND sensor_controls_configured = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Controlled Area Designation - Process for identifying and marking areas with sensor restrictions
- [PROC-02] Device Screening - Procedures for screening devices at controlled area entry points
- [PROC-03] Sensor Indication Configuration - Technical implementation of sensor usage indicators
- [PROC-04] Visitor Device Management - Process for handling visitor devices in controlled areas
- [PROC-05] Incident Response - Response procedures for unauthorized sensor usage detection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving sensors, facility changes, new device types

## 7. SCENARIO PATTERNS

[SCENARIO-01: Smartphone in Classified Area]
IF device_type = "smartphone"
AND location = "classified_storage_area"
AND sensors_present = TRUE
AND security_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Camera Usage Without Indication]
IF camera_active = TRUE
AND visual_indicator = FALSE
AND audio_indicator = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Remote Microphone Activation]
IF microphone_activated = TRUE
AND activation_source = "remote"
AND user_consent_obtained = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Visitor Device in Secure Meeting]
IF user_type = "visitor"
AND location = "secure_conference_room"
AND device_sensors_disabled = FALSE
AND briefing_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Managed Device Without Controls]
IF device_management = "corporate_managed"
AND sensor_controls_enabled = FALSE
AND device_age < 90_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibit sensor devices in controlled areas | [RULE-01], [RULE-05] |
| Provide explicit indication of sensor use | [RULE-02], [RULE-06] |
| Document controlled areas | [RULE-03] |
| Prevent unauthorized remote activation | [RULE-04], [RULE-06] |
| Implement visitor controls | [RULE-05] |
| Configure managed device controls | [RULE-06] |
```