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
All integrity verification tools deployed across the organization's information systems MUST be centrally managed to ensure consistent application and comprehensive coverage. The organization SHALL maintain centralized oversight of integrity verification activities to detect unauthorized changes to critical files, software, and firmware.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing sensitive data |
| Development Systems | YES | Systems with access to production code |
| Test/Staging Systems | YES | Systems mirroring production environments |
| End-user Workstations | CONDITIONAL | Only privileged user workstations |
| Network Infrastructure | YES | Routers, switches, firewalls, security appliances |
| Cloud Resources | YES | All cloud-hosted systems and services |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Deploy and configure centralized integrity tools<br>• Monitor integrity verification alerts<br>• Investigate integrity violations |
| System Administrators | • Install integrity agents on assigned systems<br>• Maintain system connectivity to central management<br>• Report integrity tool failures |
| Security Architecture Team | • Define integrity verification requirements<br>• Approve integrity tool technologies<br>• Establish baseline configurations |

## 4. RULES

[RULE-01] All integrity verification tools MUST be centrally managed through approved enterprise platforms.
[VALIDATION] IF integrity_tool_deployed = TRUE AND central_management = FALSE THEN violation

[RULE-02] Centralized integrity management platforms MUST maintain real-time visibility into all deployed integrity agents.
[VALIDATION] IF agent_last_checkin > 24_hours AND system_status = "active" THEN violation

[RULE-03] Integrity verification policies and baselines MUST be centrally defined and consistently applied across all systems.
[VALIDATION] IF system_baseline_version != current_approved_baseline THEN violation

[RULE-04] Central integrity management systems MUST generate alerts for unauthorized changes within 15 minutes of detection.
[VALIDATION] IF unauthorized_change_detected = TRUE AND alert_generation_time > 15_minutes THEN violation

[RULE-05] Integrity verification coverage MUST be maintained at 95% or higher for all in-scope systems.
[VALIDATION] IF (systems_with_integrity_monitoring / total_inscope_systems) < 0.95 THEN violation

[RULE-06] Central management platforms MUST retain integrity verification logs for minimum 12 months.
[VALIDATION] IF log_retention_period < 12_months THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Integrity Tool Deployment - Standardized process for deploying and configuring integrity agents
- [PROC-02] Baseline Management - Process for creating, updating, and distributing integrity baselines
- [PROC-03] Alert Response - Procedures for investigating and responding to integrity violations
- [PROC-04] Agent Health Monitoring - Process for monitoring and maintaining integrity agent health

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving integrity violations, technology changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standalone Integrity Tool]
IF integrity_tool_installed = TRUE
AND central_management_connection = FALSE
AND standalone_deployment = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Agent Communication Failure]
IF integrity_agent_installed = TRUE
AND last_communication > 24_hours
AND system_online = TRUE
AND maintenance_window = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Inconsistent Baseline Application]
IF system_type = "production"
AND integrity_baseline_applied = TRUE
AND baseline_version != approved_standard
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed Alert Generation]
IF unauthorized_file_change = TRUE
AND detection_time = timestamp_1
AND alert_generated_time = timestamp_2
AND (alert_generated_time - detection_time) > 15_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Adequate Coverage Maintained]
IF total_inscope_systems = 1000
AND systems_with_monitoring = 960
AND coverage_percentage >= 95%
AND all_agents_reporting = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Centrally managed integrity verification tools are employed | RULE-01, RULE-02, RULE-03 |
| Consistent application of integrity tools | RULE-03, RULE-05 |
| Comprehensive coverage of integrity verification | RULE-05 |
| Central management platform functionality | RULE-02, RULE-04, RULE-06 |