# POLICY: CM-6.1: Automated Management, Application, and Verification

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-6.1 |
| NIST Control | CM-6.1: Automated Management, Application, and Verification |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | configuration management, automation, baseline configuration, hardening, system components |

## 1. POLICY STATEMENT
All system components SHALL use automated mechanisms to manage, apply, and verify configuration settings according to approved security baselines. Automated tools MUST provide consistent configuration enforcement, monitoring, and reporting capabilities across the organization's hybrid cloud infrastructure.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All cloud and on-premises systems |
| Development Systems | YES | Must align with production baselines |
| Network Infrastructure | YES | Routers, switches, firewalls, load balancers |
| Database Systems | YES | All DBMS platforms and instances |
| Third-party SaaS | CONDITIONAL | Where configuration control is available |
| End-user Devices | YES | Corporate managed devices only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement automated configuration tools<br>• Monitor configuration compliance dashboards<br>• Remediate configuration drift within SLA timeframes |
| Security Engineering | • Define security configuration baselines<br>• Validate automated tool effectiveness<br>• Review configuration exceptions and approvals |
| DevOps Teams | • Integrate configuration automation into CI/CD pipelines<br>• Maintain infrastructure-as-code templates<br>• Execute automated remediation workflows |

## 4. RULES
[RULE-01] All system components MUST use automated mechanisms to manage configuration settings according to organization-approved baselines.
[VALIDATION] IF system_component_exists = TRUE AND automated_config_mgmt = FALSE THEN violation

[RULE-02] Automated configuration tools MUST apply security settings within 4 hours of system deployment or configuration change.
[VALIDATION] IF config_application_time > 4_hours AND exception_approved = FALSE THEN violation

[RULE-03] Configuration compliance verification MUST be performed automatically at least every 24 hours for all in-scope systems.
[VALIDATION] IF last_verification_time > 24_hours AND system_status = "active" THEN violation

[RULE-04] Configuration drift detection MUST trigger automated alerts within 15 minutes of detection and initiate remediation workflows.
[VALIDATION] IF config_drift_detected = TRUE AND alert_time > 15_minutes THEN violation

[RULE-05] Automated configuration tools MUST maintain audit logs of all configuration changes, applications, and verifications for minimum 1 year.
[VALIDATION] IF config_audit_log_retention < 365_days THEN violation

[RULE-06] Configuration baselines MUST be updated within 30 days of new security guidance or vulnerability disclosures affecting baseline components.
[VALIDATION] IF security_guidance_age > 30_days AND baseline_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Configuration Baseline Development - Process for creating and approving security configuration standards
- [PROC-02] Automated Tool Deployment - Implementation and validation of configuration management tools
- [PROC-03] Configuration Drift Response - Automated and manual remediation workflows for non-compliant configurations
- [PROC-04] Exception Management - Approval process for systems requiring non-standard configurations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New compliance requirements, major security incidents, tool changes, infrastructure updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Deployment]
IF system_deployed = TRUE
AND automated_config_applied = FALSE
AND deployment_time > 4_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Configuration Drift Detection]
IF config_drift_detected = TRUE
AND remediation_initiated = FALSE
AND detection_time > 15_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Manual Configuration Override]
IF configuration_method = "manual"
AND exception_approved = FALSE
AND automated_tool_available = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Compliance Verification Gap]
IF last_verification_time > 24_hours
AND system_status = "production"
AND planned_maintenance = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Audit Log Retention]
IF config_audit_logs_retained < 365_days
AND legal_hold_active = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Configuration settings are managed using automated mechanisms | [RULE-01] |
| Configuration settings are applied using automated mechanisms | [RULE-02] |
| Configuration settings are verified using automated mechanisms | [RULE-03] |
| Automated mechanisms provide alerting capabilities | [RULE-04] |
| Configuration management activities are logged and retained | [RULE-05] |
| Configuration baselines are maintained current | [RULE-06] |