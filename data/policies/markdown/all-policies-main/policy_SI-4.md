# POLICY: SI-4: System Monitoring

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4 |
| NIST Control | SI-4: System Monitoring |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system monitoring, intrusion detection, anomaly detection, security monitoring, threat detection, incident response |

## 1. POLICY STATEMENT
All information systems MUST implement continuous monitoring capabilities to detect attacks, unauthorized connections, and system misuse in real-time. Monitoring devices SHALL be strategically deployed and configured to collect essential security information and support incident response activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | Systems with access to production data or networks |
| Cloud Infrastructure | YES | Including IaaS, PaaS, and SaaS environments |
| Network Infrastructure | YES | Routers, switches, firewalls, and security devices |
| End-user Devices | CONDITIONAL | Devices with privileged access or sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define monitoring objectives and strategy<br>• Approve monitoring device deployment<br>• Ensure legal compliance of monitoring activities |
| SOC Manager | • Implement and maintain monitoring capabilities<br>• Analyze detected events and anomalies<br>• Coordinate incident response activities |
| System Administrators | • Deploy and configure monitoring devices<br>• Maintain monitoring system performance<br>• Provide monitoring data to security teams |

## 4. RULES

[RULE-01] All systems MUST implement continuous monitoring to detect attacks, unauthorized connections, and system misuse according to defined monitoring objectives.
[VALIDATION] IF system_in_scope = TRUE AND monitoring_capability = FALSE THEN critical_violation

[RULE-02] Monitoring devices MUST be strategically deployed within systems to collect organization-determined essential information and at ad hoc locations to track specific transaction types.
[VALIDATION] IF critical_system = TRUE AND strategic_monitoring = FALSE THEN violation

[RULE-03] All detected security events and anomalies MUST be analyzed within 4 hours for critical systems and 24 hours for standard systems.
[VALIDATION] IF event_criticality = "high" AND analysis_time > 4_hours THEN violation
[VALIDATION] IF event_criticality = "medium" AND analysis_time > 24_hours THEN violation

[RULE-04] System monitoring activity levels MUST be adjusted within 72 hours when risk changes to organizational operations, assets, individuals, or other organizations occur.
[VALIDATION] IF risk_change_detected = TRUE AND monitoring_adjustment_time > 72_hours THEN violation

[RULE-05] Legal opinion regarding system monitoring activities MUST be obtained and documented before implementing new monitoring capabilities.
[VALIDATION] IF new_monitoring_capability = TRUE AND legal_opinion_documented = FALSE THEN violation

[RULE-06] System monitoring information MUST be provided to designated personnel and roles based on need-to-know and incident response requirements.
[VALIDATION] IF monitoring_data_shared = TRUE AND recipient_authorized = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Monitoring Implementation - Deploy and configure monitoring tools across all in-scope systems
- [PROC-02] Event Analysis and Response - Analyze security events and coordinate incident response activities
- [PROC-03] Monitoring Adjustment - Modify monitoring levels based on risk assessment changes
- [PROC-04] Legal Compliance Review - Obtain legal approval for monitoring activities and data handling

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, regulatory changes, system architecture changes, legal requirement updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unmonitored Critical System]
IF system_criticality = "high"
AND monitoring_deployed = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Delayed Event Analysis]
IF security_event_detected = TRUE
AND system_criticality = "high"
AND analysis_completion_time > 4_hours
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unauthorized Monitoring Data Access]
IF monitoring_data_accessed = TRUE
AND accessor_role_authorized = FALSE
AND incident_response_active = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Legal Opinion]
IF monitoring_capability = "new"
AND deployment_date < current_date
AND legal_opinion_obtained = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Risk-Based Monitoring Adjustment]
IF organizational_risk_level = "increased"
AND risk_change_date < (current_date - 72_hours)
AND monitoring_level_adjusted = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitor system to detect attacks and indicators | RULE-01 |
| Deploy monitoring devices strategically | RULE-02 |
| Analyze detected events and anomalies | RULE-03 |
| Adjust monitoring levels based on risk changes | RULE-04 |
| Obtain legal opinion for monitoring activities | RULE-05 |
| Provide monitoring information to authorized personnel | RULE-06 |