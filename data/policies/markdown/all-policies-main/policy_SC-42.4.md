# POLICY: SC-42.4: Notice of Collection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-42.4 |
| NIST Control | SC-42.4: Notice of Collection |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | sensor, PII collection, notice, awareness, privacy, data collection |

## 1. POLICY STATEMENT
The organization MUST implement measures to ensure individuals are aware when sensors collect their personally identifiable information (PII). All PII-collecting sensors MUST provide clear, usable notice to affected individuals through appropriate awareness mechanisms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Physical sensors | YES | Cameras, biometric readers, location trackers |
| Digital sensors | YES | Web trackers, mobile app sensors, IoT devices |
| Third-party sensors | YES | When under organizational control |
| Employee workstations | CONDITIONAL | Only when collecting PII beyond standard monitoring |
| Public areas | YES | All sensors in publicly accessible spaces |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Approve sensor notice requirements<br>• Review notice effectiveness<br>• Oversee compliance monitoring |
| System Administrators | • Implement technical notice mechanisms<br>• Configure sensor awareness settings<br>• Maintain notice delivery systems |
| Facility Managers | • Deploy physical signage<br>• Coordinate sensor placement with notice requirements<br>• Ensure visibility of awareness measures |

## 4. RULES
[RULE-01] All sensors that collect PII MUST implement at least one awareness measure before or during data collection.
[VALIDATION] IF sensor_collects_PII = TRUE AND awareness_measure_implemented = FALSE THEN critical_violation

[RULE-02] Notice mechanisms MUST be clearly visible, understandable, and positioned where individuals can reasonably observe them before entering the collection area.
[VALIDATION] IF notice_visibility = "poor" OR notice_clarity = "unclear" THEN violation

[RULE-03] Digital sensors MUST provide notice through system interfaces, pop-up notifications, or prominent display indicators at the point of collection.
[VALIDATION] IF sensor_type = "digital" AND (interface_notice = FALSE AND popup_notice = FALSE AND display_indicator = FALSE) THEN violation

[RULE-04] Physical sensors in public areas MUST display visible signage within 10 feet of the sensor or at area entry points.
[VALIDATION] IF sensor_location = "public" AND signage_distance > 10_feet AND entry_signage = FALSE THEN violation

[RULE-05] Sensor notices MUST specify the type of PII being collected and organizational contact information for privacy inquiries.
[VALIDATION] IF notice_content_complete = FALSE OR privacy_contact_missing = TRUE THEN violation

[RULE-06] Notice effectiveness MUST be reviewed annually and updated based on usability assessments and privacy risk changes.
[VALIDATION] IF last_notice_review > 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Sensor Privacy Impact Assessment - Evaluate PII collection and notice requirements for new sensors
- [PROC-02] Notice Design and Placement - Standardize awareness measure implementation across sensor types
- [PROC-03] Notice Effectiveness Review - Annual assessment of awareness measure usability and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: New sensor deployments, privacy incidents, regulatory changes, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Security Camera in Lobby]
IF sensor_type = "camera"
AND location = "public_lobby" 
AND PII_collected = TRUE
AND visible_signage = TRUE
AND signage_distance <= 10_feet
THEN compliance = TRUE

[SCENARIO-02: Mobile App Location Tracking]
IF sensor_type = "GPS"
AND platform = "mobile_app"
AND PII_collected = TRUE
AND popup_notice = FALSE
AND interface_notice = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Biometric Reader Without Notice]
IF sensor_type = "biometric"
AND PII_collected = TRUE
AND awareness_measure_implemented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Website Analytics Tracking]
IF sensor_type = "web_tracker"
AND PII_collected = TRUE
AND privacy_notice_link = TRUE
AND collection_purpose_specified = TRUE
THEN compliance = TRUE

[SCENARIO-05: Conference Room Camera]
IF sensor_type = "camera"
AND location = "private_meeting_room"
AND PII_collected = TRUE
AND entry_signage = TRUE
AND notice_content_complete = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Measures to facilitate awareness are defined | [RULE-01], [RULE-02], [RULE-03] |
| Measures are employed for PII-collecting sensors | [RULE-01], [RULE-04], [RULE-05] |
| Individual awareness is facilitated | [RULE-02], [RULE-03], [RULE-06] |