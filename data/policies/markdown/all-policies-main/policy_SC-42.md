# POLICY: SC-42: Sensor Capability and Data

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-42 |
| NIST Control | SC-42: Sensor Capability and Data |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | sensors, mobile devices, privacy, GPS, cameras, microphones, covert activation, location tracking |

## 1. POLICY STATEMENT
This policy prohibits the use of devices with specified sensor capabilities in designated sensitive areas and requires explicit notification when sensors are actively collecting data. Organizations must implement technical and administrative controls to prevent unauthorized sensor activation and protect against covert surveillance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Mobile devices (smartphones, tablets) | YES | All sensor-equipped devices |
| IoT devices with sensors | YES | Cameras, microphones, GPS, accelerometers |
| Employees and contractors | YES | All personnel with device access |
| Visitors | YES | When bringing personal devices |
| Classified facilities | YES | Enhanced restrictions apply |
| Controlled areas | YES | As designated by security team |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define prohibited sensor types and restricted areas<br>• Approve sensor usage policies<br>• Review compliance reports |
| Facility Security Manager | • Designate restricted areas<br>• Enforce physical device controls<br>• Monitor compliance in sensitive areas |
| IT Security Team | • Configure sensor notification mechanisms<br>• Monitor unauthorized sensor activation<br>• Implement technical controls |
| Device Users | • Comply with sensor usage restrictions<br>• Report unauthorized sensor activation<br>• Acknowledge sensor usage notifications |

## 4. RULES
[RULE-01] Devices with cameras, microphones, GPS, or accelerometers SHALL NOT be permitted in areas designated as classified or highly sensitive.
[VALIDATION] IF device_location = "classified_area" AND device_sensors = TRUE AND authorization = FALSE THEN critical_violation

[RULE-02] All sensor activation MUST provide explicit visual or audible indication to users when data collection is occurring.
[VALIDATION] IF sensor_active = TRUE AND user_notification = FALSE THEN violation

[RULE-03] Remote sensor activation capabilities MUST be disabled on all organization-managed mobile devices unless explicitly authorized for business purposes.
[VALIDATION] IF remote_sensor_activation = "enabled" AND business_justification = FALSE THEN violation

[RULE-04] Personal devices brought into controlled areas MUST have sensor capabilities physically disabled or covered when technically feasible.
[VALIDATION] IF area_type = "controlled" AND device_ownership = "personal" AND sensor_disabled = FALSE THEN violation

[RULE-05] Sensor data collection policies MUST be documented and communicated to all device users annually.
[VALIDATION] IF user_training_date < (current_date - 365_days) THEN administrative_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Sensor Risk Assessment - Annual evaluation of sensor-equipped devices and associated risks
- [PROC-02] Restricted Area Designation - Process for identifying and marking areas with sensor restrictions  
- [PROC-03] Device Configuration Management - Standard configurations for disabling unauthorized sensor capabilities
- [PROC-04] Incident Response - Procedures for responding to unauthorized sensor activation
- [PROC-05] User Training - Annual training on sensor usage policies and restrictions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Security incidents involving sensors, new facility designations, technology changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Personal Phone in Classified Area]
IF device_type = "personal_smartphone"
AND location = "classified_facility" 
AND sensors_present = TRUE
AND security_exception = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Corporate Device Remote Activation]
IF device_ownership = "corporate"
AND remote_sensor_activation = "enabled"
AND business_justification = "documented"
AND user_consent = TRUE
THEN compliance = TRUE

[SCENARIO-03: Camera Usage Without Notification]
IF sensor_type = "camera"
AND data_collection_active = TRUE
AND user_notification_displayed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Visitor Device in Controlled Area]
IF user_type = "visitor"
AND device_type = "tablet"
AND area_classification = "controlled"
AND sensor_coverage_applied = TRUE
THEN compliance = TRUE

[SCENARIO-05: IoT Device Covert Recording]
IF device_type = "IoT_sensor"
AND recording_active = TRUE
AND user_awareness = FALSE
AND explicit_consent = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibit devices with specified sensors in designated areas | [RULE-01], [RULE-04] |
| Provide explicit indication of sensor use | [RULE-02] |
| Control remote sensor activation | [RULE-03] |
| Document and communicate sensor policies | [RULE-05] |