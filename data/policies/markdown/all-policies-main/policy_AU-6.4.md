# POLICY: AU-6.4: Central Review and Analysis

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-6.4 |
| NIST Control | AU-6.4: Central Review and Analysis |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit records, central review, SIEM, log analysis, security monitoring, event correlation |

## 1. POLICY STATEMENT
The organization SHALL provide and implement centralized capability to review and analyze audit records from multiple system components. All audit records from system components MUST be aggregated and analyzed through centralized security monitoring tools to enable comprehensive security oversight and incident detection.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems generating audit records |
| Network Components | YES | Routers, switches, firewalls, IDS/IPS |
| Applications | YES | Custom and commercial applications |
| Cloud Services | YES | IaaS, PaaS, SaaS components |
| IoT Devices | CONDITIONAL | If capable of audit record generation |
| Development Systems | YES | Non-production systems with sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Policy oversight and compliance validation<br>• Resource allocation for centralized monitoring<br>• Incident response coordination |
| SOC Manager | • Daily operation of centralized review capabilities<br>• Staff training and procedure development<br>• Tool configuration and maintenance |
| System Administrators | • Configure audit record forwarding to central systems<br>• Maintain connectivity to centralized platforms<br>• Respond to centralized monitoring alerts |

## 4. RULES
[RULE-01] All system components that generate audit records MUST forward logs to the centralized Security Information and Event Management (SIEM) platform within 15 minutes of generation.
[VALIDATION] IF component_generates_logs = TRUE AND forward_time > 15_minutes THEN violation

[RULE-02] The centralized review capability MUST aggregate audit records from at least 95% of in-scope system components at any given time.
[VALIDATION] IF (connected_components / total_components) < 0.95 THEN violation

[RULE-03] Centralized analysis tools MUST perform automated correlation and analysis of audit records across multiple system components in real-time.
[VALIDATION] IF correlation_enabled = FALSE OR analysis_delay > 5_minutes THEN violation

[RULE-04] Security analysts MUST review centralized audit analysis results and security alerts within 4 hours during business hours and 8 hours during non-business hours.
[VALIDATION] IF alert_severity = "high" AND review_time > 4_hours AND business_hours = TRUE THEN violation

[RULE-05] The centralized review system MUST maintain 99.5% uptime availability measured monthly.
[VALIDATION] IF monthly_uptime < 0.995 THEN violation

[RULE-06] All centralized audit review activities MUST be logged and retained for a minimum of 1 year.
[VALIDATION] IF review_activity_logged = FALSE OR retention_period < 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SIEM Configuration Management - Standardized onboarding of new audit sources
- [PROC-02] Alert Response Procedures - Escalation and investigation workflows for centralized alerts
- [PROC-03] System Integration Testing - Validation of audit record forwarding and correlation
- [PROC-04] Capacity Management - Monitoring and scaling of centralized review infrastructure

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system changes, security incidents, technology refresh, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Complete SIEM Integration]
IF system_generates_audit_records = TRUE
AND siem_integration = "configured"
AND log_forwarding_active = TRUE
AND correlation_rules_enabled = TRUE
THEN compliance = TRUE

[SCENARIO-02: Partial System Coverage]
IF total_components = 100
AND connected_components = 92
AND coverage_percentage < 95%
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Alert Response]
IF alert_generated = TRUE
AND alert_severity = "critical"
AND business_hours = TRUE
AND response_time = 6_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: SIEM System Outage]
IF siem_availability = 98%
AND measurement_period = "monthly"
AND required_uptime = 99.5%
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Audit Source]
IF network_firewall_logs = "not_forwarded"
AND system_in_scope = TRUE
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Capability to centrally review audit records is provided | [RULE-01], [RULE-02], [RULE-05] |
| Capability to centrally analyze audit records is implemented | [RULE-03], [RULE-04], [RULE-06] |
| Multiple system components are included in central review | [RULE-02] |
| Centralized analysis functionality is operational | [RULE-03], [RULE-04] |