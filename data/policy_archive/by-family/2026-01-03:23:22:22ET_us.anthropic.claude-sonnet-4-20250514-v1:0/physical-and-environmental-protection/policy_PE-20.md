# POLICY: PE-20: Asset Monitoring and Tracking

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-20 |
| NIST Control | PE-20: Asset Monitoring and Tracking |
| Version | 1.0 |
| Owner | Chief Physical Security Officer |
| Keywords | asset tracking, location monitoring, controlled areas, physical security, asset management |

## 1. POLICY STATEMENT
The organization SHALL employ asset location technologies to track and monitor the location and movement of critical assets within defined controlled areas. Asset tracking capabilities must be implemented to ensure critical assets remain in authorized locations and to detect unauthorized movement or removal.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical IT Assets | YES | Servers, network equipment, security devices |
| Mobile Computing Devices | YES | Laptops, tablets assigned to employees |
| Vehicles | CONDITIONAL | Only company-owned vehicles with critical equipment |
| Facilities Equipment | YES | High-value equipment in data centers and secure areas |
| Personal Devices | NO | BYOD devices not subject to tracking |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Physical Security Officer | • Define asset tracking requirements<br>• Approve tracking technologies<br>• Oversee controlled area designations |
| Facilities Management | • Implement tracking systems<br>• Monitor asset locations<br>• Report unauthorized movements |
| Asset Management Team | • Maintain asset inventory<br>• Configure tracking parameters<br>• Generate location reports |
| Privacy Officer | • Review tracking implementations for privacy compliance<br>• Approve tracking policies<br>• Handle privacy concerns |

## 4. RULES
[RULE-01] Organizations MUST define and document which assets require location tracking and monitoring based on criticality and value thresholds exceeding $5,000 or containing sensitive data.
[VALIDATION] IF asset_value > $5000 OR contains_sensitive_data = TRUE THEN tracking_required = TRUE

[RULE-02] Asset location technologies MUST be deployed within all controlled areas designated as Tier 1 (data centers) and Tier 2 (server rooms) facilities.
[VALIDATION] IF facility_tier IN ["Tier1", "Tier2"] THEN location_technology_required = TRUE

[RULE-03] Asset movement alerts MUST be generated within 5 minutes when tracked assets move outside authorized boundaries without proper authorization.
[VALIDATION] IF asset_location = "outside_boundary" AND movement_authorized = FALSE AND alert_time > 5_minutes THEN violation

[RULE-04] Privacy impact assessments MUST be completed before implementing any asset tracking technology that could monitor personnel locations.
[VALIDATION] IF tracking_technology_deployed = TRUE AND personnel_privacy_impact = TRUE AND pia_completed = FALSE THEN violation

[RULE-05] Asset location data MUST be retained for minimum 90 days and maximum 2 years unless required by legal hold.
[VALIDATION] IF location_data_retention < 90_days OR (location_data_retention > 730_days AND legal_hold = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Asset Tracking Technology Selection - Evaluate and approve location technologies
- [PROC-02] Controlled Area Designation - Define and document areas requiring asset tracking
- [PROC-03] Privacy Impact Assessment - Assess privacy implications of tracking implementations
- [PROC-04] Asset Movement Authorization - Process for authorizing temporary asset relocations
- [PROC-05] Tracking Alert Response - Respond to unauthorized asset movement alerts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy incidents, asset theft, technology changes, facility modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Server Movement]
IF asset_type = "server"
AND asset_criticality = "high"
AND current_location != authorized_location
AND movement_authorization = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Laptop Tracking in Office]
IF asset_type = "laptop"
AND location = "office_space"
AND tracking_monitors_employee = TRUE
AND privacy_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Authorized Asset Maintenance]
IF asset_movement = TRUE
AND maintenance_authorization = VALID
AND movement_duration < authorized_timeframe
AND return_location = original_location
THEN compliance = TRUE

[SCENARIO-04: Asset Tracking Data Retention]
IF location_data_age = 800_days
AND legal_hold = FALSE
AND data_deleted = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Untracked High-Value Equipment]
IF asset_value = 8000
AND contains_sensitive_data = TRUE
AND tracking_enabled = FALSE
AND controlled_area = "Tier1"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Asset location technologies employed to track and monitor location and movement | [RULE-01], [RULE-02] |
| Assets whose location and movement are tracked and monitored are defined | [RULE-01] |
| Controlled areas within which asset location and movement are tracked are defined | [RULE-02] |
| Privacy considerations for asset location technologies | [RULE-04] |
| Monitoring and alerting for unauthorized asset movement | [RULE-03] |