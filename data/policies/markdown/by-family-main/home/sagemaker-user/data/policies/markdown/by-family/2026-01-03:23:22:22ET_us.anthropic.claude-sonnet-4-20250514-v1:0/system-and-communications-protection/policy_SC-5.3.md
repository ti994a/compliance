# POLICY: SC-5.3: Detection and Monitoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-5.3 |
| NIST Control | SC-5.3: Detection and Monitoring |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | denial-of-service, monitoring, detection, system resources, availability, DoS attacks |

## 1. POLICY STATEMENT
The organization SHALL employ monitoring tools to detect denial-of-service (DoS) attack indicators against or launched from organizational systems. System resources MUST be continuously monitored to ensure sufficient capacity exists to prevent effective denial-of-service attacks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All internet-facing and internal systems |
| Development Systems | YES | Systems with external connectivity |
| Test Systems | CONDITIONAL | Only if connected to production networks |
| Isolated Systems | NO | Air-gapped systems without network connectivity |
| Cloud Infrastructure | YES | All hybrid cloud components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Monitor DoS detection tools 24/7<br>• Investigate DoS attack indicators<br>• Coordinate incident response for confirmed attacks |
| System Administrators | • Configure and maintain monitoring tools<br>• Set resource utilization thresholds<br>• Implement preventive measures |
| Network Operations Team | • Monitor network-level DoS indicators<br>• Maintain network capacity baselines<br>• Configure network-based protections |

## 4. RULES
[RULE-01] Organizations MUST deploy automated monitoring tools capable of detecting denial-of-service attack indicators in real-time.
[VALIDATION] IF monitoring_tools_deployed = FALSE OR real_time_detection = FALSE THEN critical_violation

[RULE-02] DoS detection tools MUST monitor both inbound attacks against organizational systems and outbound attacks launched from organizational systems.
[VALIDATION] IF inbound_monitoring = FALSE OR outbound_monitoring = FALSE THEN violation

[RULE-03] System resources including CPU, memory, disk storage, and network bandwidth MUST be continuously monitored with automated alerting when utilization exceeds 80%.
[VALIDATION] IF resource_monitoring = FALSE OR alert_threshold > 80% OR automated_alerting = FALSE THEN violation

[RULE-04] DoS monitoring tools MUST generate alerts within 5 minutes of detecting attack indicators.
[VALIDATION] IF alert_generation_time > 5_minutes THEN violation

[RULE-05] Resource capacity baselines MUST be established and reviewed quarterly to ensure adequate capacity for normal operations plus 25% overhead.
[VALIDATION] IF baseline_established = FALSE OR review_frequency > 90_days OR capacity_overhead < 25% THEN violation

[RULE-06] DoS attack indicators and resource utilization data MUST be logged and retained for minimum 90 days for forensic analysis.
[VALIDATION] IF logging_enabled = FALSE OR retention_period < 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DoS Detection Tool Configuration - Standardized deployment and configuration of monitoring tools
- [PROC-02] Resource Baseline Management - Quarterly review and update of capacity baselines  
- [PROC-03] DoS Incident Response - Coordinated response to confirmed denial-of-service attacks
- [PROC-04] Alert Escalation - Tiered escalation process for DoS-related alerts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major DoS incidents, infrastructure changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Outbound Monitoring]
IF inbound_dos_monitoring = TRUE
AND outbound_dos_monitoring = FALSE
AND system_has_internet_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delayed Alert Generation]
IF dos_attack_detected = TRUE
AND alert_generation_time = 8_minutes
AND monitoring_tools_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Insufficient Resource Monitoring]
IF cpu_monitoring = TRUE
AND memory_monitoring = FALSE
AND disk_monitoring = TRUE
AND network_monitoring = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Adequate Monitoring Coverage]
IF dos_detection_tools_deployed = TRUE
AND real_time_monitoring = TRUE
AND all_resources_monitored = TRUE
AND alert_threshold <= 80%
AND baseline_current = TRUE
THEN compliance = TRUE

[SCENARIO-05: Outdated Capacity Baseline]
IF resource_monitoring = TRUE
AND last_baseline_review > 120_days
AND quarterly_review_required = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitoring tools for detecting DoS attacks are defined and employed | [RULE-01], [RULE-02] |
| DoS attack indicators detected against the system | [RULE-01], [RULE-04] |
| DoS attack indicators detected from the system | [RULE-02], [RULE-04] |
| System resources monitored for sufficient capacity | [RULE-03], [RULE-05] |
| Resources monitored to prevent effective DoS attacks | [RULE-03], [RULE-05], [RULE-06] |