# POLICY: SI-4.14: Wireless Intrusion Detection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.14 |
| NIST Control | SI-4.14: Wireless Intrusion Detection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | wireless, intrusion detection, rogue devices, attack detection, wireless security, WIDS |

## 1. POLICY STATEMENT
The organization MUST deploy and maintain wireless intrusion detection systems (WIDS) to identify unauthorized wireless devices, detect attack attempts, and identify potential security compromises or breaches. WIDS monitoring SHALL extend beyond organizational facility boundaries to detect unauthorized wireless access points connected to organizational systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational facilities | YES | Including physical perimeters |
| Remote work locations | CONDITIONAL | Where organizational systems are accessed |
| Third-party facilities | CONDITIONAL | Where organizational data is processed |
| Mobile devices | YES | When connecting to organizational networks |
| Guest networks | YES | Must be monitored for rogue connections |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center | • Monitor WIDS alerts 24/7<br>• Investigate wireless security incidents<br>• Coordinate response to rogue device detection |
| Network Security Team | • Deploy and configure WIDS sensors<br>• Maintain WIDS signature databases<br>• Conduct wireless security assessments |
| Facilities Security | • Provide physical access for WIDS sensor installation<br>• Report suspicious wireless activity<br>• Coordinate perimeter wireless scans |

## 4. RULES
[RULE-01] Organizations MUST deploy wireless intrusion detection systems capable of identifying rogue wireless devices within and around organizational facilities.
[VALIDATION] IF facility_has_wids = FALSE THEN critical_violation

[RULE-02] WIDS MUST continuously monitor for attack attempts against wireless infrastructure and connected systems.
[VALIDATION] IF wids_monitoring_status = "inactive" AND duration > 15_minutes THEN violation

[RULE-03] WIDS coverage MUST extend beyond facility boundaries to detect unauthorized wireless access points connected to organizational systems.
[VALIDATION] IF perimeter_scan_frequency < monthly THEN violation

[RULE-04] Rogue wireless device detection MUST trigger immediate investigation within 2 hours of identification.
[VALIDATION] IF rogue_device_detected = TRUE AND investigation_start_time > 2_hours THEN violation

[RULE-05] WIDS sensors MUST be positioned to provide comprehensive coverage of all areas where organizational systems operate.
[VALIDATION] IF coverage_gap_exists = TRUE AND gap_size > 50_square_meters THEN violation

[RULE-06] WIDS signature databases MUST be updated within 72 hours of vendor release.
[VALIDATION] IF signature_age > 72_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Wireless Intrusion Detection System Deployment - Installation and configuration of WIDS sensors
- [PROC-02] Rogue Device Response - Investigation and remediation of unauthorized wireless devices
- [PROC-03] Wireless Security Scanning - Periodic comprehensive wireless security assessments
- [PROC-04] WIDS Alert Triage - Classification and prioritization of wireless security alerts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility changes, technology updates, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Rogue Access Point Detection]
IF wireless_device_detected = TRUE
AND device_authorized = FALSE
AND device_connected_to_network = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: WIDS Sensor Failure]
IF wids_sensor_status = "offline"
AND outage_duration > 4_hours
AND backup_coverage = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Attack Investigation]
IF wireless_attack_detected = TRUE
AND investigation_initiated = FALSE
AND time_elapsed > 2_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Perimeter Coverage Gap]
IF facility_perimeter_scanned = FALSE
AND last_scan_date > 30_days_ago
AND organizational_systems_present = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Outdated WIDS Signatures]
IF wids_signatures_updated = FALSE
AND vendor_release_date > 72_hours_ago
AND critical_vulnerability_addressed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Wireless intrusion detection system employed to identify rogue devices | [RULE-01], [RULE-05] |
| WIDS employed to detect attack attempts | [RULE-02], [RULE-06] |
| WIDS employed to detect potential compromises or breaches | [RULE-02], [RULE-04] |
| Coverage extends beyond facility boundaries | [RULE-03] |
| Timely response to wireless threats | [RULE-04] |