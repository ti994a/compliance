# POLICY: PE-20: Asset Monitoring and Tracking

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-20 |
| NIST Control | PE-20: Asset Monitoring and Tracking |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | asset tracking, location monitoring, controlled areas, physical assets, surveillance |

## 1. POLICY STATEMENT
The organization must employ asset location technologies to track and monitor the location and movement of critical assets within defined controlled areas. Asset tracking systems must be implemented with appropriate privacy considerations and legal review.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical IT equipment | YES | Servers, network devices, storage systems |
| Vehicles | YES | Company-owned vehicles and mobile assets |
| Portable devices | YES | Laptops, tablets, mobile phones |
| Controlled facility areas | YES | Data centers, secure zones, restricted areas |
| Personal devices | CONDITIONAL | Only if used for business purposes |
| Visitor assets | NO | Covered under separate visitor management |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Define controlled areas requiring monitoring<br>• Implement asset location technologies<br>• Maintain tracking system configurations |
| Asset Management Team | • Maintain inventory of trackable assets<br>• Monitor asset movement alerts<br>• Generate tracking compliance reports |
| Privacy Officer | • Review privacy implications of tracking<br>• Ensure legal compliance for monitoring<br>• Approve tracking technology deployment |

## 4. RULES
[RULE-01] Organizations MUST define and document which assets require location tracking and monitoring based on criticality and value.
[VALIDATION] IF asset_criticality >= "HIGH" AND tracking_requirement = "undefined" THEN violation

[RULE-02] Asset location technologies MUST be deployed to monitor defined critical assets within all controlled areas.
[VALIDATION] IF controlled_area = TRUE AND critical_assets_present = TRUE AND location_technology = "not_deployed" THEN violation

[RULE-03] Asset movement outside authorized locations MUST generate automated alerts within 15 minutes of detection.
[VALIDATION] IF asset_location != "authorized" AND alert_generated = FALSE AND time_elapsed > 15_minutes THEN violation

[RULE-04] Privacy and legal review MUST be completed before deploying any asset location tracking technology.
[VALIDATION] IF tracking_technology = "deployed" AND (privacy_review = "incomplete" OR legal_review = "incomplete") THEN critical_violation

[RULE-05] Asset tracking records MUST be maintained for a minimum of 12 months and reviewed monthly for anomalies.
[VALIDATION] IF tracking_records_age > 12_months AND archived = FALSE THEN violation
[VALIDATION] IF monthly_review_completed = FALSE AND current_month_end = TRUE THEN violation

[RULE-06] Controlled areas requiring asset monitoring MUST be clearly defined and documented with specific boundaries.
[VALIDATION] IF area_classification = "controlled" AND monitoring_boundaries = "undefined" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Asset Classification and Tracking Requirements - Defines criteria for assets requiring monitoring
- [PROC-02] Location Technology Deployment - Implementation process for tracking systems
- [PROC-03] Asset Movement Authorization - Process for approving asset relocations
- [PROC-04] Privacy Impact Assessment - Evaluation of tracking technology privacy implications
- [PROC-05] Incident Response for Asset Anomalies - Response procedures for unauthorized movements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New facility acquisition, technology changes, privacy regulation updates, security incidents involving asset theft

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Server Movement]
IF asset_type = "critical_server"
AND current_location != "authorized_data_center"
AND movement_authorized = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Laptop Tracking in Secure Area]
IF device_type = "laptop"
AND area_classification = "controlled"
AND tracking_technology = "active"
AND location_monitoring = TRUE
THEN compliance = TRUE

[SCENARIO-03: Unauthorized Vehicle Exit]
IF asset_type = "company_vehicle"
AND location_status = "outside_premises"
AND exit_authorization = FALSE
AND alert_generated = TRUE
AND response_time <= 15_minutes
THEN compliance = TRUE

[SCENARIO-04: Unmonitored Critical Asset]
IF asset_criticality = "HIGH"
AND controlled_area = TRUE
AND tracking_enabled = FALSE
AND privacy_review = "complete"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Privacy Review Missing]
IF tracking_system = "newly_deployed"
AND privacy_review = "not_conducted"
AND personal_data_collection = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Asset location technologies employed to track critical assets | [RULE-02] |
| Assets requiring tracking and monitoring are defined | [RULE-01] |
| Controlled areas for monitoring are defined | [RULE-06] |
| Privacy considerations addressed | [RULE-04] |
| Tracking records maintained | [RULE-05] |
| Movement monitoring and alerting | [RULE-03] |