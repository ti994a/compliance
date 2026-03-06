# POLICY: SI-4.14: Wireless Intrusion Detection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.14 |
| NIST Control | SI-4.14: Wireless Intrusion Detection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | wireless, intrusion detection, rogue devices, WIDS, wireless security, monitoring |

## 1. POLICY STATEMENT
The organization SHALL deploy and maintain wireless intrusion detection systems (WIDS) to identify unauthorized wireless devices, detect wireless-based attacks, and identify potential security compromises. All organizational facilities and perimeters must be continuously monitored for rogue wireless activity that could compromise system security.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational facilities | YES | Including data centers, offices, warehouses |
| Facility perimeters | YES | Areas outside facilities within wireless range |
| Guest networks | YES | Must be monitored for rogue connections |
| Temporary facilities | YES | Pop-up offices, conference venues |
| Remote work locations | CONDITIONAL | Only company-managed remote offices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish WIDS policy and requirements<br>• Approve WIDS architecture and deployment<br>• Review wireless security incidents |
| Network Security Team | • Deploy and configure WIDS sensors<br>• Monitor WIDS alerts and investigate anomalies<br>• Maintain WIDS signatures and detection rules |
| IT Operations | • Provide infrastructure support for WIDS deployment<br>• Coordinate authorized wireless device installations<br>• Execute wireless device removal procedures |

## 4. RULES
[RULE-01] Organizations MUST deploy wireless intrusion detection systems with sensor coverage for all areas where organizational systems operate and facility perimeters within 100 meters.
[VALIDATION] IF facility_has_systems = TRUE AND wids_sensor_coverage < 95% THEN violation

[RULE-02] WIDS MUST continuously monitor for rogue wireless access points, unauthorized wireless clients, and wireless attack patterns with real-time alerting enabled.
[VALIDATION] IF wids_monitoring = "discontinuous" OR alert_delay > 5_minutes THEN violation

[RULE-03] Detected rogue wireless devices MUST be investigated within 4 hours of detection and disabled within 24 hours if confirmed unauthorized.
[VALIDATION] IF rogue_device_detected = TRUE AND investigation_time > 4_hours THEN violation
[VALIDATION] IF rogue_device_confirmed = TRUE AND disable_time > 24_hours THEN critical_violation

[RULE-04] WIDS sensors MUST be deployed to detect wireless signals in areas outside organizational facilities within the effective range of potential unauthorized access points.
[VALIDATION] IF perimeter_sensor_coverage < 90% OR detection_range < 100_meters THEN violation

[RULE-05] WIDS systems MUST maintain detection signatures for current wireless attack methods and be updated within 30 days of vendor releases.
[VALIDATION] IF signature_age > 30_days OR update_status = "failed" THEN violation

[RULE-06] All WIDS alerts classified as "high" or "critical" MUST be investigated and documented within 2 hours of generation.
[VALIDATION] IF alert_severity IN ["high", "critical"] AND response_time > 2_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] WIDS Deployment and Configuration - Standardized sensor placement and detection rule configuration
- [PROC-02] Rogue Device Investigation - Process for validating and responding to unauthorized wireless devices
- [PROC-03] Wireless Attack Response - Incident response procedures for wireless-based security events
- [PROC-04] WIDS Maintenance and Updates - Regular system maintenance and signature update procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving wireless, facility changes, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Access Point Detection]
IF wireless_device_detected = TRUE
AND device_authorized = FALSE
AND device_type = "access_point"
AND investigation_completed = FALSE
AND detection_time > 4_hours_ago
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Wireless Attack Pattern Detected]
IF wids_alert_generated = TRUE
AND alert_severity = "critical"
AND attack_pattern = "deauth_flood"
AND response_time > 2_hours
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Perimeter Monitoring Gap]
IF facility_location = "data_center"
AND perimeter_sensor_coverage = 75%
AND coverage_gap > 25_meters
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: WIDS Signature Outdated]
IF wids_signature_age = 45_days
AND vendor_updates_available = TRUE
AND update_status = "pending"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Guest Network Rogue Device]
IF network_segment = "guest"
AND unauthorized_device_count > 0
AND device_investigation = "complete"
AND disable_time < 24_hours
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Wireless intrusion detection system employed to identify rogue devices | [RULE-01], [RULE-02] |
| WIDS employed to detect attack attempts on the system | [RULE-02], [RULE-05] |
| WIDS employed to detect potential compromises or breaches | [RULE-02], [RULE-06] |
| Proactive search for unauthorized wireless connections | [RULE-03], [RULE-04] |
| Wireless scans include areas outside facilities | [RULE-04] |