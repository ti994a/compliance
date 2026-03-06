# POLICY: SC-5.3: Detection and Monitoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-5.3 |
| NIST Control | SC-5.3: Detection and Monitoring |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | denial-of-service, DoS, monitoring, detection, system resources, capacity, availability |

## 1. POLICY STATEMENT
The organization must employ monitoring tools to detect denial-of-service (DoS) attacks against or launched from systems and continuously monitor system resources to ensure sufficient capacity exists to prevent effective DoS attacks. All monitoring activities must be documented and integrated with incident response procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All internet-facing and critical internal systems |
| Development Systems | CONDITIONAL | Only if processing production data |
| Network Infrastructure | YES | Routers, switches, firewalls, load balancers |
| Cloud Resources | YES | All IaaS, PaaS, and SaaS components |
| Third-party Services | CONDITIONAL | If under organizational control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Deploy and maintain DoS monitoring tools<br>• Monitor alerts and investigate incidents<br>• Coordinate incident response activities |
| System Administrators | • Configure resource monitoring thresholds<br>• Implement capacity management controls<br>• Maintain system performance baselines |
| Network Operations Center (NOC) | • Monitor network traffic patterns<br>• Implement traffic filtering and rate limiting<br>• Coordinate with SOC on network-based attacks |

## 4. RULES
[RULE-01] Organizations MUST deploy automated monitoring tools capable of detecting DoS attack indicators including traffic volume anomalies, connection rate spikes, and resource exhaustion patterns.
[VALIDATION] IF monitoring_tools_deployed = FALSE OR dos_detection_capability = FALSE THEN violation

[RULE-02] System resource monitoring MUST include CPU utilization, memory consumption, disk I/O, and network bandwidth with alerting thresholds set at 80% capacity.
[VALIDATION] IF resource_monitoring_coverage < 100% OR alert_threshold > 80% THEN violation

[RULE-03] DoS monitoring tools MUST generate alerts within 5 minutes of detecting attack indicators and automatically notify SOC personnel.
[VALIDATION] IF alert_generation_time > 5_minutes OR automatic_notification = FALSE THEN violation

[RULE-04] Organizations MUST maintain baseline performance metrics for all monitored systems and update baselines quarterly or after significant system changes.
[VALIDATION] IF baseline_age > 90_days AND no_significant_changes = TRUE THEN violation

[RULE-05] Resource capacity thresholds MUST be configured to trigger preventive actions when utilization exceeds 75% and emergency actions at 90%.
[VALIDATION] IF preventive_threshold > 75% OR emergency_threshold > 90% THEN violation

[RULE-06] All DoS detection events MUST be logged with sufficient detail for forensic analysis and retained for minimum 12 months.
[VALIDATION] IF logging_detail = "insufficient" OR retention_period < 12_months THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DoS Attack Response - Immediate response actions when attacks are detected
- [PROC-02] Resource Capacity Management - Regular assessment and adjustment of resource allocations
- [PROC-03] Monitoring Tool Configuration - Standardized deployment and configuration of detection tools
- [PROC-04] Baseline Establishment - Process for creating and maintaining performance baselines

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, significant infrastructure changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing DoS Detection]
IF system_classification = "critical"
AND dos_monitoring_tools = FALSE
AND internet_facing = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate Resource Monitoring]
IF cpu_monitoring = TRUE
AND memory_monitoring = TRUE
AND (disk_monitoring = FALSE OR network_monitoring = FALSE)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Alert Response]
IF dos_attack_detected = TRUE
AND alert_generation_time = 8_minutes
AND notification_sent = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Outdated Performance Baselines]
IF baseline_last_updated > 120_days
AND significant_system_changes = TRUE
AND capacity_planning_accurate = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Proper DoS Monitoring Implementation]
IF monitoring_tools_deployed = TRUE
AND resource_monitoring_complete = TRUE
AND alert_thresholds_configured = TRUE
AND baseline_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitoring tools for detecting DoS attacks are employed | [RULE-01], [RULE-03] |
| System resources are monitored for sufficient capacity | [RULE-02], [RULE-05] |
| DoS attack indicators are detected against the system | [RULE-01], [RULE-06] |
| DoS attack indicators are detected from the system | [RULE-01], [RULE-06] |
| Sufficient resources exist to prevent effective DoS attacks | [RULE-02], [RULE-04], [RULE-05] |