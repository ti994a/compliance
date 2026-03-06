# POLICY: SI-4.14: Wireless Intrusion Detection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.14 |
| NIST Control | SI-4.14: Wireless Intrusion Detection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | wireless, intrusion detection, rogue devices, wireless security, monitoring |

## 1. POLICY STATEMENT
The organization SHALL employ wireless intrusion detection systems to identify rogue wireless devices and detect attack attempts, compromises, or breaches to organizational systems. Wireless monitoring SHALL extend beyond organizational facility boundaries to detect unauthorized wireless access points connected to organizational systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational facilities | YES | Including areas outside facility perimeters |
| All wireless-enabled systems | YES | Regardless of location or classification |
| Third-party wireless devices | YES | When connected to organizational networks |
| Guest wireless networks | YES | Must be monitored for security threats |
| IoT and mobile devices | YES | All wireless-capable organizational assets |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve wireless intrusion detection policy<br>• Ensure adequate funding for WIDS capabilities<br>• Review wireless security incidents |
| Network Security Team | • Deploy and maintain wireless intrusion detection systems<br>• Monitor wireless security alerts and incidents<br>• Conduct regular wireless security scans |
| SOC Analysts | • Monitor WIDS alerts 24/7<br>• Investigate wireless security incidents<br>• Escalate critical wireless threats |
| Facility Security | • Coordinate physical wireless scans<br>• Report suspicious wireless devices<br>• Support wireless security investigations |

## 4. RULES
[RULE-01] Organizations MUST deploy wireless intrusion detection systems capable of identifying rogue wireless devices within and around organizational facilities.
[VALIDATION] IF facility_has_wids = FALSE THEN critical_violation

[RULE-02] Wireless intrusion detection systems MUST monitor for attack attempts against organizational wireless infrastructure and connected systems.
[VALIDATION] IF wids_attack_monitoring = FALSE THEN violation

[RULE-03] WIDS MUST detect and alert on potential compromises or breaches to systems via wireless vectors within 15 minutes of detection.
[VALIDATION] IF wireless_breach_detected = TRUE AND alert_time > 15_minutes THEN violation

[RULE-04] Wireless security scans MUST be conducted beyond facility perimeters to identify unauthorized wireless access points connected to organizational systems.
[VALIDATION] IF external_wireless_scan_frequency < monthly THEN violation

[RULE-05] Rogue wireless devices MUST be investigated and remediated within 4 hours of detection for high-risk environments and 24 hours for standard environments.
[VALIDATION] IF rogue_device_detected = TRUE AND environment_risk = "high" AND remediation_time > 4_hours THEN critical_violation
[VALIDATION] IF rogue_device_detected = TRUE AND environment_risk = "standard" AND remediation_time > 24_hours THEN violation

[RULE-06] WIDS MUST maintain continuous monitoring coverage with no more than 2 hours of downtime per month for maintenance.
[VALIDATION] IF wids_downtime > 2_hours_monthly THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Wireless Intrusion Detection System Deployment - Standard procedures for WIDS installation and configuration
- [PROC-02] Rogue Device Response - Incident response procedures for unauthorized wireless devices
- [PROC-03] Wireless Security Scanning - Regular scanning procedures for internal and external wireless threats
- [PROC-04] WIDS Alert Investigation - Standard operating procedures for analyzing wireless security alerts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major wireless security incidents, technology changes, regulatory updates, facility modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Rogue Access Point Detection]
IF unauthorized_ap_detected = TRUE
AND ap_connected_to_org_network = TRUE
AND investigation_initiated = FALSE
AND detection_time > 1_hour
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: External Wireless Scanning Gap]
IF last_external_wireless_scan > 30_days
AND facility_has_sensitive_systems = TRUE
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: WIDS Coverage Gap]
IF facility_area_monitored < 95_percent
AND area_contains_wireless_systems = TRUE
AND no_compensating_controls = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Delayed Attack Response]
IF wireless_attack_detected = TRUE
AND attack_severity = "high"
AND response_time > 15_minutes
AND no_documented_justification = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Maintenance Window Exceeded]
IF wids_maintenance_downtime > 2_hours
AND month_period = TRUE
AND no_emergency_exception = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Wireless intrusion detection system employed to identify rogue wireless devices | [RULE-01] |
| Wireless intrusion detection system employed to detect attack attempts | [RULE-02] |
| Wireless intrusion detection system employed to detect potential compromises or breaches | [RULE-03] |
| Proactive search for unauthorized wireless connections | [RULE-04] |
| Thorough scans including areas outside facilities | [RULE-04] |
| Continuous monitoring capability | [RULE-06] |