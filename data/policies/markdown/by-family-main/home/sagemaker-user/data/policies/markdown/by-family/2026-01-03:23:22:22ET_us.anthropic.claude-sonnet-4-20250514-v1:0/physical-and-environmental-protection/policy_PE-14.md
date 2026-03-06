```markdown
# POLICY: PE-14: Environmental Controls

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-14 |
| NIST Control | PE-14: Environmental Controls |
| Version | 1.0 |
| Owner | Facilities Management |
| Keywords | temperature, humidity, environmental, monitoring, data center, server room, facility |

## 1. POLICY STATEMENT
The organization must maintain temperature and humidity levels within acceptable ranges in facilities housing information systems and continuously monitor environmental conditions. Environmental controls are critical for system availability and must be actively managed to prevent equipment failure and service disruption.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary facilities with system concentrations |
| Server Rooms | YES | Dedicated rooms housing critical systems |
| Network Equipment Rooms | YES | Rooms with networking infrastructure |
| Office Areas | CONDITIONAL | Only if housing critical systems |
| Cloud Provider Facilities | YES | Must verify compliance through contracts |
| Remote/Branch Offices | CONDITIONAL | Based on criticality of hosted systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Management | • Maintain environmental control systems<br>• Monitor temperature and humidity levels<br>• Respond to environmental alerts<br>• Document environmental incidents |
| IT Operations | • Report environmental concerns<br>• Coordinate with facilities for maintenance<br>• Monitor system performance related to environmental conditions |
| Security Team | • Audit environmental control compliance<br>• Review environmental monitoring logs<br>• Assess environmental risks |

## 4. RULES
[RULE-01] Temperature levels in data centers and server rooms MUST be maintained between 64°F and 81°F (18°C to 27°C) at all times.
[VALIDATION] IF facility_type IN ["data_center", "server_room"] AND (temperature < 64°F OR temperature > 81°F) THEN violation

[RULE-02] Humidity levels in data centers and server rooms MUST be maintained between 20% and 80% relative humidity.
[VALIDATION] IF facility_type IN ["data_center", "server_room"] AND (humidity < 20% OR humidity > 80%) THEN violation

[RULE-03] Environmental conditions MUST be monitored continuously with automated alerts for out-of-range conditions.
[VALIDATION] IF monitoring_frequency != "continuous" OR alert_system = FALSE THEN violation

[RULE-04] Environmental monitoring systems MUST generate alerts within 5 minutes of detecting out-of-range conditions.
[VALIDATION] IF alert_delay > 5_minutes THEN violation

[RULE-05] Environmental control failures MUST be responded to within 30 minutes during business hours and 60 minutes outside business hours.
[VALIDATION] IF response_time > 30_minutes AND business_hours = TRUE THEN violation
[VALIDATION] IF response_time > 60_minutes AND business_hours = FALSE THEN violation

[RULE-06] Backup environmental controls MUST be available for all critical facilities housing Tier 1 and Tier 2 systems.
[VALIDATION] IF system_tier IN ["Tier1", "Tier2"] AND backup_environmental_controls = FALSE THEN violation

[RULE-07] Environmental monitoring logs MUST be retained for a minimum of 12 months and reviewed monthly.
[VALIDATION] IF log_retention < 12_months OR review_frequency > 30_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Environmental Monitoring - Continuous monitoring of temperature, humidity, and other environmental factors
- [PROC-02] Alert Response - Procedures for responding to environmental control alerts and failures
- [PROC-03] Preventive Maintenance - Regular maintenance of HVAC and environmental control systems
- [PROC-04] Incident Documentation - Recording and reporting environmental incidents and responses
- [PROC-05] Backup System Activation - Procedures for activating backup environmental controls

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Environmental incidents, system failures due to environmental conditions, facility changes, new system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Data Center Temperature Spike]
IF facility_type = "data_center"
AND temperature > 81°F
AND duration > 15_minutes
AND backup_cooling = "not_activated"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Server Room Humidity Drop]
IF facility_type = "server_room"
AND humidity < 20%
AND alert_generated = TRUE
AND response_time <= 30_minutes
THEN compliance = TRUE

[SCENARIO-03: Environmental Monitoring Failure]
IF monitoring_system = "offline"
AND duration > 4_hours
AND manual_monitoring = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Cloud Provider Environmental SLA]
IF deployment_type = "cloud"
AND provider_environmental_sla = "undefined"
AND system_tier IN ["Tier1", "Tier2"]
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Backup Environmental System Test]
IF backup_environmental_controls = TRUE
AND last_test_date > 90_days_ago
AND system_tier = "Tier1"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Temperature levels maintained at acceptable levels | [RULE-01] |
| Humidity levels maintained at acceptable levels | [RULE-02] |
| Environmental control levels monitored continuously | [RULE-03], [RULE-04] |
| Backup controls for critical systems | [RULE-06] |
| Environmental incident response | [RULE-05] |
| Monitoring documentation and review | [RULE-07] |
```