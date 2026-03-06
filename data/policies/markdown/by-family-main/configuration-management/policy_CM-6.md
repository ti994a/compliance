# POLICY: CM-6: Configuration Settings

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-6 |
| NIST Control | CM-6: Configuration Settings |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | configuration management, secure baselines, hardening, SCAP, STIG, deviation approval |

## 1. POLICY STATEMENT
All system components must be configured using the most restrictive security settings consistent with operational requirements, based on approved secure configuration baselines. Configuration changes must be monitored, controlled, and any deviations from established baselines must be documented and approved through formal processes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, hybrid |
| Network Devices | YES | Routers, switches, firewalls, load balancers |
| Endpoints | YES | Workstations, servers, mobile devices |
| Applications | YES | Custom and commercial software |
| Third-party Services | CONDITIONAL | When configuration control is available |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement approved configuration baselines<br>• Monitor configuration drift<br>• Report unauthorized changes |
| Security Team | • Develop secure configuration standards<br>• Review deviation requests<br>• Conduct compliance assessments |
| Change Control Board | • Approve configuration baseline changes<br>• Review deviation requests<br>• Authorize emergency changes |

## 4. RULES

[RULE-01] All system components MUST be configured according to approved secure configuration baselines derived from industry standards (STIG, CIS, NIST) within 30 days of deployment.
[VALIDATION] IF component_deployed = TRUE AND baseline_applied = FALSE AND days_since_deployment > 30 THEN violation

[RULE-02] Configuration baselines MUST reflect the most restrictive security settings consistent with operational requirements and be documented in the configuration management database.
[VALIDATION] IF baseline_documented = FALSE OR security_review_approved = FALSE THEN violation

[RULE-03] Any deviations from approved configuration baselines MUST be documented with business justification and approved by the Change Control Board before implementation.
[VALIDATION] IF configuration_deviation = TRUE AND (justification_documented = FALSE OR ccb_approved = FALSE) THEN violation

[RULE-04] Automated configuration monitoring MUST be implemented to detect unauthorized changes within 24 hours of occurrence.
[VALIDATION] IF unauthorized_change_detected = TRUE AND detection_time > 24_hours THEN violation

[RULE-05] Configuration compliance assessments MUST be performed quarterly using automated scanning tools (SCAP-compliant where available).
[VALIDATION] IF last_compliance_scan > 90_days THEN violation

[RULE-06] Critical security configuration changes MUST be tested in non-production environments before production deployment.
[VALIDATION] IF change_criticality = "high" AND pre_prod_testing = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Secure Configuration Baseline Development - Process for creating and maintaining security baselines
- [PROC-02] Configuration Deviation Management - Workflow for requesting and approving baseline deviations  
- [PROC-03] Configuration Monitoring and Alerting - Automated detection and response to configuration drift
- [PROC-04] Compliance Assessment and Remediation - Regular scanning and remediation of non-compliant configurations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents, regulatory changes, technology refresh, audit findings

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Configuration Change]
IF configuration_change_detected = TRUE
AND change_authorized = FALSE  
AND detection_time <= 24_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved Deviation Implementation]
IF configuration_deviation = TRUE
AND business_justification_documented = TRUE
AND ccb_approval = TRUE
AND implementation_date <= approval_date + 30_days
THEN compliance = TRUE

[SCENARIO-03: Missing Baseline Application]
IF system_deployed = TRUE
AND deployment_date < current_date - 30_days
AND security_baseline_applied = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Overdue Compliance Assessment]
IF system_type = "production"
AND last_compliance_scan_date < current_date - 90_days
AND system_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Change Without Baseline Update]
IF emergency_change = TRUE
AND change_implemented = TRUE
AND baseline_updated = FALSE
AND days_since_change > 7
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Establish and document configuration settings using secure configurations | RULE-01, RULE-02 |
| Implement the documented configuration settings | RULE-01 |
| Identify, document, and approve deviations from established settings | RULE-03 |
| Monitor changes to configuration settings | RULE-04, RULE-05 |
| Control changes to configuration settings | RULE-06 |