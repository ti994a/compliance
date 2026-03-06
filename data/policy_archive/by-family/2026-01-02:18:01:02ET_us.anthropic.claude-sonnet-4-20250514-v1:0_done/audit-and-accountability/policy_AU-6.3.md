# POLICY: AU-6.3: Correlate Audit Record Repositories

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-6.3 |
| NIST Control | AU-6.3: Correlate Audit Record Repositories |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit correlation, situational awareness, log analysis, security monitoring, cross-repository |

## 1. POLICY STATEMENT
The organization SHALL analyze and correlate audit records across different repositories to achieve organization-wide situational awareness. This correlation must span organizational, mission/business process, and information system levels to support comprehensive security monitoring and incident detection.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid |
| Third-party audit repositories | YES | Where contractually accessible |
| Network infrastructure logs | YES | Firewalls, routers, switches |
| Application audit logs | YES | Including SaaS applications |
| Security tools | YES | SIEM, IDS/IPS, endpoint protection |
| Standalone systems | CONDITIONAL | If generating security-relevant events |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Perform daily audit correlation activities<br>• Monitor correlation tools and alerts<br>• Escalate identified security incidents |
| Security Architect | • Design audit correlation architecture<br>• Define correlation rules and use cases<br>• Ensure repository integration capabilities |
| System Administrators | • Configure audit forwarding to central repositories<br>• Maintain log quality and completeness<br>• Support correlation tool deployment |

## 4. RULES
[RULE-01] All security-relevant audit repositories MUST be integrated into the centralized correlation platform within 30 days of system deployment.
[VALIDATION] IF system_type = "security_relevant" AND deployment_date + 30_days < current_date AND correlation_integrated = FALSE THEN violation

[RULE-02] Audit correlation analysis MUST be performed continuously with automated alerting for predefined threat patterns.
[VALIDATION] IF correlation_analysis = "manual_only" OR alert_automation = FALSE THEN violation

[RULE-03] Cross-repository correlation rules MUST cover at least the following scenarios: failed authentication patterns, privilege escalation attempts, data exfiltration indicators, and lateral movement detection.
[VALIDATION] IF correlation_rules_count < 4 OR required_scenarios_covered < 100% THEN violation

[RULE-04] Correlation results indicating potential security incidents MUST be investigated within 4 hours for high-severity alerts and 24 hours for medium-severity alerts.
[VALIDATION] IF alert_severity = "high" AND investigation_start_time > 4_hours THEN critical_violation
[VALIDATION] IF alert_severity = "medium" AND investigation_start_time > 24_hours THEN violation

[RULE-05] Audit correlation capabilities MUST maintain at least 90 days of searchable historical data for trend analysis and forensic investigation.
[VALIDATION] IF historical_data_retention < 90_days THEN violation

[RULE-06] Repository correlation status MUST be monitored with alerts generated when any critical audit source becomes unavailable for more than 15 minutes.
[VALIDATION] IF audit_source = "critical" AND unavailable_time > 15_minutes AND alert_generated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Audit Repository Integration - Process for onboarding new audit sources into correlation platform
- [PROC-02] Correlation Rule Management - Procedures for creating, testing, and maintaining correlation rules
- [PROC-03] Incident Escalation from Correlation - Workflow for escalating correlated security events
- [PROC-04] Cross-Organization Awareness Reporting - Process for sharing situational awareness across business units

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, new audit sources, correlation tool changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Critical Repository]
IF repository_type = "critical_security_system"
AND correlation_integrated = FALSE
AND deployment_age > 30_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delayed Incident Investigation]
IF correlation_alert_severity = "high"
AND alert_timestamp + 4_hours < current_time
AND investigation_status = "not_started"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Insufficient Correlation Coverage]
IF required_correlation_scenarios = ["auth_failure", "privilege_escalation", "data_exfiltration", "lateral_movement"]
AND implemented_scenarios < 4
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Inadequate Historical Retention]
IF correlation_platform_retention < 90_days
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Repository Monitoring Gap]
IF critical_audit_source_downtime > 15_minutes
AND monitoring_alert_generated = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Analyze audit records across different repositories | [RULE-01], [RULE-02] |
| Correlate audit records for situational awareness | [RULE-03], [RULE-05] |
| Gain organization-wide situational awareness | [RULE-04], [RULE-06] |
| Support cross-organization awareness | [PROC-04] |