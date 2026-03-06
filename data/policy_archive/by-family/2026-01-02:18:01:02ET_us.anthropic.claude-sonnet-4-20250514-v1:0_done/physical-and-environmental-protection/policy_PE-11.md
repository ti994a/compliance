# POLICY: PE-11: Emergency Power

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-11 |
| NIST Control | PE-11: Emergency Power |
| Version | 1.0 |
| Owner | Facilities Manager |
| Keywords | emergency power, UPS, uninterruptible power supply, orderly shutdown, power loss, backup power |

## 1. POLICY STATEMENT
The organization SHALL provide uninterruptible power supply (UPS) systems to facilitate orderly shutdown of information systems in the event of primary power source loss. UPS systems MUST provide sufficient power duration to enable proper system shutdown or transfer to backup power sources.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All production data centers |
| Server Rooms | YES | Rooms housing critical systems |
| Network Equipment | YES | Core network infrastructure |
| Workstations | CONDITIONAL | Only for critical operations |
| Cloud Infrastructure | CONDITIONAL | Hybrid cloud components only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Procure and maintain UPS systems<br>• Coordinate UPS testing and maintenance<br>• Ensure adequate power capacity planning |
| IT Operations Manager | • Define critical system power requirements<br>• Coordinate orderly shutdown procedures<br>• Monitor UPS performance and alerts |
| System Administrators | • Configure systems for graceful shutdown<br>• Test shutdown procedures<br>• Document power requirements |

## 4. RULES
[RULE-01] All critical information systems MUST be protected by UPS systems that provide minimum 15 minutes of backup power for orderly shutdown.
[VALIDATION] IF system_criticality = "critical" AND ups_protection = FALSE THEN violation

[RULE-02] UPS systems MUST provide sufficient capacity to support 100% of connected load for the minimum backup duration.
[VALIDATION] IF ups_capacity < (connected_load * minimum_duration) THEN violation

[RULE-03] UPS systems MUST be tested monthly to verify proper operation and battery capacity.
[VALIDATION] IF last_test_date > 30_days AND test_status != "passed" THEN violation

[RULE-04] Critical systems MUST have automated shutdown procedures configured to activate when UPS battery reaches 25% capacity.
[VALIDATION] IF system_criticality = "critical" AND auto_shutdown_configured = FALSE THEN violation

[RULE-05] UPS battery replacement MUST occur according to manufacturer specifications or when capacity falls below 80% of rated capacity.
[VALIDATION] IF battery_capacity < 80% OR days_since_install > manufacturer_replacement_schedule THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] UPS Installation and Configuration - Standard process for sizing, installing, and configuring UPS systems
- [PROC-02] Monthly UPS Testing - Procedures for testing UPS functionality and battery capacity
- [PROC-03] Emergency Shutdown Procedures - Step-by-step process for orderly system shutdown during power events
- [PROC-04] UPS Maintenance and Battery Replacement - Scheduled maintenance and battery replacement procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Power outage incidents, UPS failures, facility changes, new critical system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Server Without UPS]
IF system_type = "critical_server"
AND ups_protection = FALSE
AND facility_type = "data_center"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: UPS Overloaded]
IF ups_current_load > ups_rated_capacity
AND system_criticality = "critical"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missed UPS Testing]
IF last_ups_test > 35_days
AND ups_supports_critical_systems = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Degraded Battery Capacity]
IF battery_capacity_percentage < 80
AND replacement_scheduled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper UPS Configuration]
IF system_criticality = "critical"
AND ups_protection = TRUE
AND ups_capacity >= required_load
AND last_test_date <= 30_days
AND auto_shutdown_configured = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Uninterruptible power supply provided for orderly shutdown | RULE-01, RULE-02 |
| UPS facilitates orderly shutdown during power loss | RULE-04 |
| UPS systems properly maintained and tested | RULE-03, RULE-05 |