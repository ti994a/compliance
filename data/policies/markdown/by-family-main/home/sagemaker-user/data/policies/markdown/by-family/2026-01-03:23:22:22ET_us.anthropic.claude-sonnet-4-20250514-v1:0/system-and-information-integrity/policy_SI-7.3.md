# POLICY: SI-7.3: Centrally Managed Integrity Tools

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.3 |
| NIST Control | SI-7.3: Centrally Managed Integrity Tools |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | integrity verification, centralized management, file integrity monitoring, system integrity, security tools |

## 1. POLICY STATEMENT
The organization SHALL employ centrally managed integrity verification tools to ensure consistent application and comprehensive coverage of integrity verification actions across all information systems. All integrity verification tools MUST be managed through a centralized platform to maintain standardized configurations, policies, and reporting.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | Systems containing sensitive code or data |
| Test Systems | CONDITIONAL | If containing production-like data |
| Personal Devices | NO | BYOD devices excluded |
| Cloud Infrastructure | YES | IaaS, PaaS, and SaaS components |
| Third-party Systems | CONDITIONAL | If under organizational control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve integrity verification tool selection<br>• Oversee centralized management strategy<br>• Ensure policy compliance |
| Security Operations Team | • Deploy and configure centralized integrity tools<br>• Monitor integrity verification alerts<br>• Maintain tool configurations and policies |
| System Administrators | • Install integrity verification agents<br>• Ensure system compliance with integrity policies<br>• Report integrity violations |

## 4. RULES

[RULE-01] All integrity verification tools MUST be managed through a centralized platform that provides unified policy management, configuration control, and reporting capabilities.
[VALIDATION] IF integrity_tool_deployed = TRUE AND centrally_managed = FALSE THEN violation

[RULE-02] Integrity verification tools SHALL be deployed on all in-scope systems within 30 days of system deployment or policy implementation.
[VALIDATION] IF system_in_scope = TRUE AND days_since_deployment > 30 AND integrity_tool_installed = FALSE THEN violation

[RULE-03] Centralized integrity verification tools MUST perform automated scans at least daily for critical systems and weekly for non-critical systems.
[VALIDATION] IF system_criticality = "critical" AND scan_frequency > 24_hours THEN violation
[VALIDATION] IF system_criticality = "non-critical" AND scan_frequency > 168_hours THEN violation

[RULE-04] All integrity verification tool configurations MUST be standardized and managed centrally, with no local modifications permitted without documented approval.
[VALIDATION] IF local_config_changes = TRUE AND approval_documented = FALSE THEN violation

[RULE-05] Integrity verification alerts MUST be centrally monitored and responded to within 4 hours for critical alerts and 24 hours for non-critical alerts.
[VALIDATION] IF alert_severity = "critical" AND response_time > 4_hours THEN violation
[VALIDATION] IF alert_severity = "non-critical" AND response_time > 24_hours THEN violation

[RULE-06] Central integrity management platform MUST maintain audit logs of all configuration changes, policy updates, and administrative actions for minimum 1 year.
[VALIDATION] IF audit_log_retention < 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Centralized Integrity Tool Deployment - Standard process for deploying agents to new systems
- [PROC-02] Integrity Alert Response - Procedures for investigating and responding to integrity violations
- [PROC-03] Tool Configuration Management - Process for managing and updating centralized configurations
- [PROC-04] Integrity Reporting - Regular reporting on integrity verification coverage and findings

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving integrity violations, major infrastructure changes, new regulatory requirements

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unmanaged Integrity Tool]
IF integrity_tool_deployed = TRUE
AND centrally_managed = FALSE
AND system_in_scope = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Integrity Coverage]
IF system_deployment_date < (current_date - 30_days)
AND system_in_scope = TRUE
AND integrity_tool_installed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Alert Response]
IF integrity_alert_generated = TRUE
AND alert_severity = "critical"
AND response_time > 4_hours
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-04: Unauthorized Local Configuration]
IF integrity_tool_config_modified = TRUE
AND modification_source = "local"
AND approval_documented = FALSE
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-05: Compliant Centralized Management]
IF integrity_tools_centrally_managed = TRUE
AND all_systems_covered = TRUE
AND scan_frequency_compliant = TRUE
AND alert_response_timely = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Centrally managed integrity verification tools are employed | RULE-01, RULE-04 |
| Comprehensive coverage of integrity verification actions | RULE-02, RULE-03 |
| Consistent application of integrity tools | RULE-04, RULE-06 |
| Effective monitoring and response capabilities | RULE-05 |