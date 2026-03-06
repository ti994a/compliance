# POLICY: PE-11: Emergency Power

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-11 |
| NIST Control | PE-11: Emergency Power |
| Version | 1.0 |
| Owner | Facilities Manager |
| Keywords | uninterruptible power supply, UPS, emergency power, orderly shutdown, power loss, backup power |

## 1. POLICY STATEMENT
All critical information systems and supporting infrastructure MUST be protected by uninterruptible power supply (UPS) systems to ensure orderly shutdown capabilities during primary power source failures. UPS systems SHALL provide sufficient backup power duration to either complete critical operations or perform safe system shutdown procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and secondary facilities |
| Server Rooms | YES | Including departmental server closets |
| Network Infrastructure | YES | Core switches, routers, firewalls |
| Critical Workstations | CONDITIONAL | Only those supporting critical business functions |
| Desktop Computers | NO | Standard office workstations excluded |
| Cloud Infrastructure | CONDITIONAL | Hybrid cloud components under organizational control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Procure and maintain UPS systems<br>• Coordinate UPS testing and maintenance<br>• Ensure adequate power capacity planning |
| IT Operations Team | • Monitor UPS status and alerts<br>• Execute emergency shutdown procedures<br>• Coordinate with facilities during power events |
| System Administrators | • Configure systems for graceful shutdown<br>• Test automated shutdown procedures<br>• Maintain system-specific power requirements |

## 4. RULES
[RULE-01] All critical information systems MUST be connected to UPS systems that provide minimum 15 minutes of backup power for orderly shutdown.
[VALIDATION] IF system_criticality = "critical" AND ups_runtime < 15_minutes THEN violation

[RULE-02] UPS systems MUST be tested monthly to verify proper operation and battery capacity.
[VALIDATION] IF last_ups_test > 30_days THEN violation

[RULE-03] UPS capacity MUST be sized to support 125% of connected load to account for battery aging and future growth.
[VALIDATION] IF ups_capacity < (connected_load * 1.25) THEN violation

[RULE-04] Automated shutdown procedures MUST be configured for all systems connected to UPS with shutdown initiation at 50% remaining battery capacity.
[VALIDATION] IF automated_shutdown = FALSE OR shutdown_threshold > 50_percent THEN violation

[RULE-05] UPS failure alerts MUST be sent to IT Operations and Facilities teams within 2 minutes of detection.
[VALIDATION] IF ups_alert_time > 2_minutes THEN violation

[RULE-06] UPS maintenance records MUST be retained for minimum 3 years and include battery replacement dates and test results.
[VALIDATION] IF maintenance_records_age > 3_years OR missing_battery_records = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] UPS Installation and Commissioning - Standard process for new UPS deployments
- [PROC-02] Monthly UPS Testing - Systematic testing of battery capacity and transfer switches
- [PROC-03] Emergency Shutdown Procedures - Step-by-step system shutdown during extended outages
- [PROC-04] UPS Maintenance and Battery Replacement - Preventive maintenance scheduling and execution

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Power outage incidents, UPS failures, facility changes, system criticality changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical System Without UPS]
IF system_criticality = "critical"
AND ups_protection = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: UPS with Insufficient Runtime]
IF ups_installed = TRUE
AND ups_runtime < 15_minutes
AND system_type = "critical"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Overdue UPS Testing]
IF last_ups_test > 30_days
AND ups_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Automated Shutdown]
IF ups_connected = TRUE
AND automated_shutdown = FALSE
AND manual_shutdown_procedure = "undefined"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Proper UPS Implementation]
IF system_criticality = "critical"
AND ups_runtime >= 15_minutes
AND last_test <= 30_days
AND automated_shutdown = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Uninterruptible power supply provided for orderly shutdown | RULE-01, RULE-04 |
| UPS capacity adequate for system protection | RULE-03 |
| UPS systems properly maintained and tested | RULE-02, RULE-06 |
| Emergency response procedures established | RULE-05, PROC-03 |