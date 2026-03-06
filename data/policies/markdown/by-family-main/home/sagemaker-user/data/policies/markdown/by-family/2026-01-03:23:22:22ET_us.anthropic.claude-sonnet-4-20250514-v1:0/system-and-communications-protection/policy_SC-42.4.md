# POLICY: SC-42.4: Notice of Collection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-42.4 |
| NIST Control | SC-42.4: Notice of Collection |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | sensor collection, PII notice, privacy awareness, data collection disclosure, sensor notification |

## 1. POLICY STATEMENT
The organization MUST implement measures to ensure individuals are aware when sensors collect their personally identifiable information (PII). All PII-collecting sensors SHALL provide clear, usable notice to individuals about data collection activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| IoT Devices | YES | All sensors collecting PII |
| Security Cameras | YES | Video/audio recording systems |
| Mobile Applications | YES | Apps using device sensors |
| Building Access Systems | YES | Biometric and tracking sensors |
| Network Monitoring | YES | Traffic analysis collecting PII |
| Employee Workstations | CONDITIONAL | Only if sensor-enabled |
| Third-party Sensors | YES | Contracted or partnered systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define notice requirements and standards<br>• Approve sensor deployment privacy measures<br>• Monitor compliance with notice obligations |
| System Administrators | • Configure sensor notification mechanisms<br>• Implement technical notice solutions<br>• Maintain sensor inventory and settings |
| Legal Counsel | • Review notice language and adequacy<br>• Ensure regulatory compliance<br>• Approve privacy impact assessments |

## 4. RULES
[RULE-01] All sensors that collect PII MUST provide notice to individuals before or during data collection.
[VALIDATION] IF sensor_collects_PII = TRUE AND notice_provided = FALSE THEN violation

[RULE-02] Notice mechanisms MUST be clearly visible, understandable, and accessible to affected individuals.
[VALIDATION] IF notice_visibility = "hidden" OR notice_language = "unclear" THEN violation

[RULE-03] Sensor configurations SHALL include automated notification capabilities where technically feasible.
[VALIDATION] IF sensor_type = "automated" AND notification_capability = FALSE AND technical_feasibility = TRUE THEN violation

[RULE-04] Alternative notice methods MUST be implemented when direct sensor notification is not possible.
[VALIDATION] IF direct_notification = FALSE AND alternative_notice = FALSE THEN violation

[RULE-05] Notice effectiveness MUST be evaluated through usability testing at least annually.
[VALIDATION] IF last_usability_test > 365_days THEN violation

[RULE-06] PII collection by sensors MUST be documented in privacy impact assessments.
[VALIDATION] IF sensor_collects_PII = TRUE AND PIA_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Sensor Privacy Impact Assessment - Evaluate privacy implications before sensor deployment
- [PROC-02] Notice Design and Testing - Develop and validate notification mechanisms
- [PROC-03] Sensor Inventory Management - Maintain current list of PII-collecting sensors
- [PROC-04] Notice Effectiveness Review - Annual evaluation of notification adequacy

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: New sensor deployment, privacy regulation changes, notice effectiveness issues

## 7. SCENARIO PATTERNS
[SCENARIO-01: Security Camera Installation]
IF sensor_type = "security_camera"
AND collects_facial_recognition = TRUE
AND visible_signage = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Mobile App Sensor Access]
IF app_accesses_sensors = TRUE
AND PII_collected = TRUE
AND in_app_notice = TRUE
AND notice_before_collection = TRUE
THEN compliance = TRUE

[SCENARIO-03: Building Access Biometrics]
IF sensor_type = "biometric_scanner"
AND mandatory_use = TRUE
AND notice_provided = "verbal_only"
AND written_notice = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: IoT Device Data Collection]
IF device_type = "IoT_sensor"
AND collects_behavioral_data = TRUE
AND notification_method = "device_indicator"
AND user_awareness_confirmed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Sensor Activation]
IF sensor_activation = "emergency"
AND immediate_safety_risk = TRUE
AND post_incident_notice = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Measures to facilitate awareness are defined | [RULE-01], [RULE-02] |
| Measures are employed for PII collection awareness | [RULE-03], [RULE-04] |
| Individual awareness of sensor data collection | [RULE-05], [RULE-06] |