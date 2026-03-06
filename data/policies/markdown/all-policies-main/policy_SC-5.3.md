# POLICY: SC-5.3: Detection and Monitoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-5.3 |
| NIST Control | SC-5.3: Detection and Monitoring |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | denial-of-service, monitoring, detection, system resources, availability, capacity |

## 1. POLICY STATEMENT
The organization must employ monitoring tools to detect denial-of-service (DoS) attack indicators against or launched from systems and monitor system resources to ensure sufficient capacity exists to prevent effective DoS attacks. This policy ensures proactive detection and resource management to maintain system availability.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All production systems | YES | Including cloud and on-premises |
| Development systems | CONDITIONAL | If handling sensitive data |
| Network infrastructure | YES | Routers, switches, firewalls |
| Third-party hosted systems | CONDITIONAL | If organization has monitoring access |
| Personal devices | NO | Unless accessing critical systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Deploy and maintain DoS detection tools<br>• Monitor alerts and investigate incidents<br>• Coordinate response activities |
| Infrastructure Team | • Configure resource monitoring thresholds<br>• Maintain system capacity baselines<br>• Implement resource protection measures |
| Network Operations | • Monitor network traffic patterns<br>• Configure network-based DoS detection<br>• Implement traffic filtering controls |

## 4. RULES
[RULE-01] Organizations MUST deploy automated monitoring tools capable of detecting DoS attack indicators on all in-scope systems within 30 days of system deployment.
[VALIDATION] IF system_in_production = TRUE AND monitoring_tools_deployed = FALSE AND days_since_deployment > 30 THEN violation

[RULE-02] DoS detection tools MUST monitor both inbound attacks against the system and outbound attacks launched from the system.
[VALIDATION] IF monitoring_tool_configured = TRUE AND (inbound_monitoring = FALSE OR outbound_monitoring = FALSE) THEN violation

[RULE-03] System resource monitoring MUST include CPU utilization, memory usage, disk storage capacity, and network bandwidth with defined alert thresholds.
[VALIDATION] IF resource_monitoring = TRUE AND (cpu_monitoring = FALSE OR memory_monitoring = FALSE OR disk_monitoring = FALSE OR network_monitoring = FALSE) THEN violation

[RULE-04] Resource monitoring thresholds MUST be configured to alert when utilization exceeds 80% of capacity for any monitored resource.
[VALIDATION] IF monitoring_threshold > 80_percent OR monitoring_threshold = undefined THEN violation

[RULE-05] DoS attack alerts MUST be investigated within 15 minutes of detection during business hours and within 1 hour during off-hours.
[VALIDATION] IF alert_type = "dos_attack" AND business_hours = TRUE AND response_time > 15_minutes THEN violation
[VALIDATION] IF alert_type = "dos_attack" AND business_hours = FALSE AND response_time > 60_minutes THEN violation

[RULE-06] System resource utilization data MUST be retained for a minimum of 90 days for trend analysis and capacity planning.
[VALIDATION] IF resource_data_retention < 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DoS Detection Tool Configuration - Standard configuration and deployment of monitoring tools
- [PROC-02] Resource Threshold Management - Setting and maintaining appropriate alert thresholds
- [PROC-03] DoS Incident Response - Investigation and response procedures for detected attacks
- [PROC-04] Capacity Planning Review - Quarterly review of resource utilization trends

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major infrastructure changes, significant DoS incidents, technology refresh

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Outbound Monitoring]
IF system_has_dos_detection = TRUE
AND inbound_monitoring = TRUE
AND outbound_monitoring = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate Resource Monitoring]
IF system_monitors_cpu = TRUE
AND system_monitors_memory = FALSE
AND system_monitors_disk = TRUE
AND system_monitors_network = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: High Alert Threshold]
IF resource_monitoring_enabled = TRUE
AND cpu_alert_threshold = 95_percent
AND memory_alert_threshold = 90_percent
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed Response]
IF dos_alert_generated = TRUE
AND business_hours = TRUE
AND investigation_start_time > 20_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Insufficient Data Retention]
IF resource_monitoring_enabled = TRUE
AND data_retention_period = 60_days
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitoring tools for detecting DoS indicators are employed | [RULE-01], [RULE-02] |
| System resources are monitored for sufficient capacity | [RULE-03], [RULE-04] |
| DoS detection covers attacks against the system | [RULE-02] |
| DoS detection covers attacks launched from the system | [RULE-02] |