# POLICY: SI-4: System Monitoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4 |
| NIST Control | SI-4: System Monitoring |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | monitoring, detection, attacks, unauthorized access, anomalies, intrusion detection, network monitoring, security events |

## 1. POLICY STATEMENT
All organizational systems MUST implement continuous monitoring capabilities to detect attacks, indicators of potential attacks, and unauthorized activities in real-time or near real-time. Monitoring activities MUST comply with applicable legal requirements and provide actionable intelligence to security operations personnel for incident response and risk management.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | Systems with access to production data or networks |
| Cloud Infrastructure | YES | Including IaaS, PaaS, and SaaS environments |
| Network Infrastructure | YES | Routers, switches, firewalls, and network devices |
| End User Devices | YES | Laptops, desktops, mobile devices accessing corporate resources |
| Third-party Systems | CONDITIONAL | When processing organizational data or connected to networks |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define monitoring objectives and strategies<br>• Ensure legal compliance of monitoring activities<br>• Approve monitoring device deployment locations |
| SOC Manager | • Implement and maintain monitoring capabilities<br>• Analyze detected events and anomalies<br>• Coordinate incident response activities |
| System Administrators | • Deploy and configure monitoring tools<br>• Maintain monitoring device functionality<br>• Provide monitoring data to security teams |
| Legal Counsel | • Review monitoring activities for legal compliance<br>• Provide guidance on privacy and surveillance laws |

## 4. RULES

[RULE-01] Systems MUST implement monitoring capabilities to detect attacks and indicators of potential attacks based on organizationally-defined monitoring objectives.
[VALIDATION] IF system_has_monitoring = FALSE OR monitoring_objectives_undefined = TRUE THEN violation

[RULE-02] Systems MUST monitor for unauthorized local, network, and remote connections in real-time.
[VALIDATION] IF connection_monitoring_enabled = FALSE OR monitoring_scope NOT IN ["local", "network", "remote"] THEN violation

[RULE-03] Organizations MUST deploy monitoring devices strategically within systems to collect essential security information and at ad hoc locations to track specific transaction types.
[VALIDATION] IF strategic_monitoring_devices = 0 OR essential_info_collection = FALSE THEN violation

[RULE-04] Detected security events and anomalies MUST be analyzed within 4 hours of detection for critical systems and within 24 hours for standard systems.
[VALIDATION] IF system_criticality = "critical" AND analysis_time > 4_hours THEN critical_violation
[VALIDATION] IF system_criticality = "standard" AND analysis_time > 24_hours THEN violation

[RULE-05] Monitoring activity levels MUST be adjusted within 72 hours when there is a change in risk to organizational operations, assets, individuals, or other organizations.
[VALIDATION] IF risk_change_detected = TRUE AND monitoring_adjustment_time > 72_hours THEN violation

[RULE-06] Legal opinion regarding system monitoring activities MUST be obtained and documented before implementing new monitoring capabilities.
[VALIDATION] IF new_monitoring_capability = TRUE AND legal_opinion_obtained = FALSE THEN critical_violation

[RULE-07] System monitoring information MUST be provided to designated personnel and roles based on need-to-know and incident response requirements.
[VALIDATION] IF monitoring_info_distribution = "undefined" OR recipient_authorization = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Event Monitoring - Continuous monitoring and analysis of security events across all systems
- [PROC-02] Monitoring Device Deployment - Strategic placement and configuration of monitoring tools
- [PROC-03] Anomaly Analysis - Investigation and classification of detected security anomalies
- [PROC-04] Monitoring Adjustment - Risk-based adjustment of monitoring sensitivity and scope
- [PROC-05] Legal Review Process - Legal assessment of monitoring activities and privacy implications

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, regulatory changes, technology changes, legal opinion updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unmonitored Critical System]
IF system_criticality = "critical"
AND monitoring_deployed = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Delayed Event Analysis]
IF security_event_detected = TRUE
AND system_criticality = "critical"
AND analysis_completion_time > 4_hours
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unauthorized Connection Detection Gap]
IF connection_type IN ["local", "network", "remote"]
AND connection_authorized = FALSE
AND monitoring_detected = FALSE
AND connection_duration > 1_hour
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Monitoring Without Legal Review]
IF monitoring_capability = "new"
AND deployment_date < 30_days_ago
AND legal_opinion_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Risk Change Without Monitoring Adjustment]
IF organizational_risk_change = TRUE
AND risk_change_date > 72_hours_ago
AND monitoring_level_adjusted = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitor for attacks and indicators | RULE-01 |
| Detect unauthorized connections | RULE-02 |
| Strategic monitoring deployment | RULE-03 |
| Event and anomaly analysis | RULE-04 |
| Risk-based monitoring adjustment | RULE-05 |
| Legal compliance verification | RULE-06 |
| Information sharing requirements | RULE-07 |