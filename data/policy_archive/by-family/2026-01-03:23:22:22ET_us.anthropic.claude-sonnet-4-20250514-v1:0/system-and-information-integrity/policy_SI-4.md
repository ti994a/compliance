# POLICY: SI-4: System Monitoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4 |
| NIST Control | SI-4: System Monitoring |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system monitoring, intrusion detection, anomaly detection, security events, continuous monitoring |

## 1. POLICY STATEMENT
All information systems MUST implement continuous monitoring capabilities to detect attacks, unauthorized connections, and system misuse in real-time. Organizations SHALL deploy monitoring devices strategically and analyze detected events to maintain security posture and enable incident response.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | Systems with access to production data or networks |
| Cloud Infrastructure | YES | Including IaaS, PaaS, and SaaS components |
| Network Infrastructure | YES | Routers, switches, firewalls, and network devices |
| IoT/OT Devices | CONDITIONAL | If connected to organizational networks |
| Contractor Systems | CONDITIONAL | If processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Monitor security events 24/7<br>• Analyze anomalies and investigate incidents<br>• Maintain monitoring tools and signatures |
| System Administrators | • Deploy and configure monitoring agents<br>• Ensure system monitoring coverage<br>• Report monitoring failures immediately |
| Network Operations | • Monitor network traffic and connections<br>• Deploy network monitoring devices<br>• Maintain network monitoring infrastructure |
| Incident Response Team | • Respond to monitoring alerts<br>• Coordinate incident investigation<br>• Document lessons learned from monitoring events |

## 4. RULES
[RULE-01] All systems MUST implement continuous monitoring with coverage for attacks, unauthorized connections, and system misuse detection.
[VALIDATION] IF system_type = "production" AND monitoring_coverage < 100% THEN critical_violation

[RULE-02] Monitoring objectives MUST be defined and documented for each system based on risk assessment and regulatory requirements.
[VALIDATION] IF system_deployed = TRUE AND monitoring_objectives_documented = FALSE THEN violation

[RULE-03] Monitoring devices MUST be deployed strategically at network perimeters, critical system interfaces, and high-value asset locations.
[VALIDATION] IF critical_system = TRUE AND perimeter_monitoring = FALSE THEN violation

[RULE-04] Security events and anomalies MUST be analyzed within 4 hours of detection for high-severity events and within 24 hours for medium-severity events.
[VALIDATION] IF event_severity = "high" AND analysis_time > 4_hours THEN violation
[VALIDATION] IF event_severity = "medium" AND analysis_time > 24_hours THEN violation

[RULE-05] Monitoring activity levels MUST be adjusted within 72 hours when organizational risk posture changes.
[VALIDATION] IF risk_change_date + 72_hours < current_date AND monitoring_adjustment = FALSE THEN violation

[RULE-06] Legal review of monitoring activities MUST be conducted annually and when monitoring scope changes significantly.
[VALIDATION] IF last_legal_review + 365_days < current_date THEN violation

[RULE-07] Monitoring information MUST be provided to authorized personnel based on defined roles and need-to-know principles.
[VALIDATION] IF monitoring_access_granted = TRUE AND (role_authorized = FALSE OR need_to_know = FALSE) THEN violation

[RULE-08] Unauthorized local, network, and remote connections MUST be detected and blocked within 15 minutes of identification.
[VALIDATION] IF unauthorized_connection = TRUE AND block_time > 15_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Monitoring Deployment - Standardized process for implementing monitoring on new systems
- [PROC-02] Event Analysis and Investigation - Procedures for analyzing security events and anomalies
- [PROC-03] Monitoring Tuning and Optimization - Process for adjusting monitoring sensitivity and coverage
- [PROC-04] Legal Compliance Review - Annual review process for monitoring activities legality
- [PROC-05] Monitoring Data Retention - Procedures for retaining and disposing of monitoring data

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, regulatory changes, significant infrastructure changes, legal requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unmonitored Critical System]
IF system_classification = "critical"
AND monitoring_deployed = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Delayed Event Analysis]
IF security_event_severity = "high"
AND detection_time + 4_hours < current_time
AND analysis_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unauthorized Connection Not Blocked]
IF connection_authorized = FALSE
AND connection_detected = TRUE
AND detection_time + 15_minutes < current_time
AND connection_blocked = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Monitoring Objectives]
IF system_deployed = TRUE
AND system_age > 30_days
AND monitoring_objectives_documented = FALSE
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-05: Outdated Legal Review]
IF last_legal_review_date + 365_days < current_date
AND monitoring_scope_changed = TRUE
THEN compliance = FALSE
violation_severity = "Medium"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitor system to detect attacks and indicators | RULE-01, RULE-02 |
| Monitor unauthorized local connections | RULE-01, RULE-08 |
| Monitor unauthorized network connections | RULE-01, RULE-08 |
| Monitor unauthorized remote connections | RULE-01, RULE-08 |
| Identify unauthorized system use | RULE-01, RULE-04 |
| Deploy monitoring devices strategically | RULE-03 |
| Deploy monitoring at ad hoc locations | RULE-03 |
| Analyze detected events | RULE-04 |
| Analyze detected anomalies | RULE-04 |
| Adjust monitoring activity based on risk changes | RULE-05 |
| Obtain legal opinion on monitoring activities | RULE-06 |
| Provide monitoring information to authorized personnel | RULE-07 |