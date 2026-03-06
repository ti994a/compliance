```markdown
# POLICY: SC-42.4: Notice of Collection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-42.4 |
| NIST Control | SC-42.4: Notice of Collection |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII collection, sensor awareness, privacy notice, data collection transparency |

## 1. POLICY STATEMENT
The organization MUST implement measures to ensure individuals are aware when sensors are collecting their personally identifiable information (PII). All PII-collecting sensors MUST provide clear, usable notifications to affected individuals before or during data collection.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational sensors | YES | Physical and digital sensors collecting PII |
| Third-party sensors | YES | When used by organization or on premises |
| Employee monitoring systems | YES | Cameras, badge readers, biometric scanners |
| Customer-facing sensors | YES | Website tracking, mobile apps, IoT devices |
| Research equipment | CONDITIONAL | Only when collecting identifiable data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Privacy Officer | • Define notice requirements and templates<br>• Review sensor deployments for privacy impact<br>• Validate notice effectiveness |
| System Administrators | • Configure sensors with appropriate notices<br>• Maintain notification mechanisms<br>• Document sensor capabilities |
| Legal Team | • Ensure regulatory compliance of notices<br>• Review notice language and placement<br>• Assess legal adequacy |

## 4. RULES
[RULE-01] All sensors that collect PII MUST implement at least one awareness measure before or during data collection.
[VALIDATION] IF sensor_collects_PII = TRUE AND awareness_measure = NULL THEN critical_violation

[RULE-02] Privacy notices for sensors MUST be clear, conspicuous, and accessible to affected individuals.
[VALIDATION] IF notice_visibility = "hidden" OR notice_language = "unclear" THEN violation

[RULE-03] Sensor awareness measures MUST be tested for usability and effectiveness at least annually.
[VALIDATION] IF last_usability_test > 365_days THEN violation

[RULE-04] New sensor deployments MUST undergo privacy impact assessment including notice adequacy review.
[VALIDATION] IF sensor_deployment_date > privacy_assessment_date THEN violation

[RULE-05] Sensor notices MUST specify what PII is collected, purpose, and data handling practices.
[VALIDATION] IF notice_completeness_score < required_elements THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Sensor Privacy Impact Assessment - Evaluate privacy risks before sensor deployment
- [PROC-02] Notice Design and Placement - Standardize awareness measure implementation
- [PROC-03] Usability Testing - Validate effectiveness of privacy notices
- [PROC-04] Sensor Inventory Management - Maintain registry of PII-collecting sensors

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New sensor technology, regulatory changes, privacy incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Hidden Security Camera]
IF sensor_type = "camera"
AND collects_biometric_data = TRUE
AND visible_notice = FALSE
AND alternative_awareness_measure = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Website Analytics with Notice]
IF sensor_type = "web_tracking"
AND privacy_notice_displayed = TRUE
AND notice_before_collection = TRUE
AND opt_out_available = TRUE
THEN compliance = TRUE

[SCENARIO-03: Biometric Scanner Without Context]
IF sensor_type = "biometric_scanner"
AND purpose_disclosed = FALSE
AND data_retention_specified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: IoT Device with App Notice]
IF sensor_type = "IoT_device"
AND mobile_app_notice = TRUE
AND device_indicator_light = TRUE
AND notice_completeness = "adequate"
THEN compliance = TRUE

[SCENARIO-05: Research Sensor with Consent]
IF sensor_type = "research_equipment"
AND participant_consent = TRUE
AND data_anonymized = TRUE
AND notice_provided = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Measures to facilitate awareness are defined | [RULE-01], [RULE-02] |
| Measures are employed for PII-collecting sensors | [RULE-01], [RULE-04] |
| Individual awareness is facilitated | [RULE-02], [RULE-03] |
| Sensor PII collection is transparent | [RULE-05] |
```