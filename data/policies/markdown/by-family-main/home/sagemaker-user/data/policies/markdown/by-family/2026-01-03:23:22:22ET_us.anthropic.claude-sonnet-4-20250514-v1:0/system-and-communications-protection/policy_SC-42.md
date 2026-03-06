# POLICY: SC-42: Sensor Capability and Data

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-42 |
| NIST Control | SC-42: Sensor Capability and Data |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | sensors, mobile devices, cameras, microphones, GPS, tracking, privacy, covert activation |

## 1. POLICY STATEMENT
The organization prohibits the use of devices with specific sensor capabilities in designated areas and ensures explicit indication of sensor use to protect against unauthorized data collection and surveillance. Mobile devices and embedded sensors must be controlled to prevent covert activation and unauthorized information gathering.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Mobile Devices | YES | Smartphones, tablets, wearables with sensors |
| Embedded Systems | YES | IoT devices, smart building systems with sensors |
| Personal Devices | YES | When used in corporate facilities or networks |
| Contractor Equipment | YES | All third-party devices entering facilities |
| Visitor Devices | YES | Personal devices in controlled areas |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facility Security Manager | • Define restricted areas and sensor prohibitions<br>• Enforce device restrictions at entry points<br>• Maintain signage and user notifications |
| IT Security Team | • Configure sensor controls on corporate devices<br>• Monitor for unauthorized sensor activation<br>• Implement technical safeguards |
| Mobile Device Administrator | • Deploy sensor management policies<br>• Provide explicit sensor use indicators<br>• Audit device sensor capabilities |

## 4. RULES
[RULE-01] Devices with cameras, microphones, GPS, or accelerometers SHALL be prohibited in classified areas, executive meeting rooms, and secure development facilities.
[VALIDATION] IF device_location IN restricted_areas AND device_sensors CONTAINS prohibited_sensors THEN violation

[RULE-02] All corporate mobile devices MUST provide explicit visual or audible indication when sensors are actively collecting data.
[VALIDATION] IF sensor_active = TRUE AND user_indication = FALSE THEN violation

[RULE-03] Personal devices with sensor capabilities MUST be secured in designated storage areas before entering restricted zones.
[VALIDATION] IF area_classification >= "restricted" AND personal_device_present = TRUE AND device_secured = FALSE THEN violation

[RULE-04] Remote activation of device sensors MUST require explicit user consent and provide continuous indication during use.
[VALIDATION] IF sensor_activation = "remote" AND user_consent = FALSE THEN critical_violation

[RULE-05] Sensor data collection policies MUST be disclosed to users before device provisioning or facility access.
[VALIDATION] IF device_provisioned = TRUE AND policy_acknowledged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Facility Entry Screening - Screen and secure sensor-capable devices at facility entry points
- [PROC-02] Mobile Device Configuration - Configure corporate devices with sensor management and indication capabilities
- [PROC-03] Visitor Device Management - Manage visitor device storage and restricted area access
- [PROC-04] Sensor Audit and Monitoring - Monitor and audit sensor usage across corporate devices

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New facility designations, sensor technology changes, security incidents involving unauthorized recording

## 7. SCENARIO PATTERNS
[SCENARIO-01: Personal Phone in Classified Area]
IF device_type = "personal_smartphone"
AND current_location = "classified_facility"
AND device_secured = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Corporate Device Covert Recording]
IF device_type = "corporate_mobile"
AND microphone_active = TRUE
AND user_indication = FALSE
AND user_consent = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Visitor Camera in Meeting Room]
IF user_type = "visitor"
AND device_type = "camera_phone"
AND location = "executive_meeting_room"
AND exception_granted = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: IoT Sensor Data Collection]
IF device_type = "iot_sensor"
AND data_collection_active = TRUE
AND user_notification = TRUE
AND consent_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Remote GPS Activation]
IF activation_type = "remote"
AND sensor_type = "GPS"
AND user_consent = TRUE
AND indication_provided = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibit devices with specified sensors in designated areas | [RULE-01], [RULE-03] |
| Provide explicit indication of sensor use | [RULE-02], [RULE-04] |
| Control remote sensor activation | [RULE-04] |
| User awareness and consent | [RULE-05] |