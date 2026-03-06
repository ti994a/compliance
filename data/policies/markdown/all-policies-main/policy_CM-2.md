# POLICY: CM-2: Baseline Configuration

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-2 |
| NIST Control | CM-2: Baseline Configuration |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | baseline configuration, configuration management, system components, configuration control, system architecture |

## 1. POLICY STATEMENT
The organization must develop, document, and maintain current baseline configurations for all information systems under configuration control. Baseline configurations must be reviewed and updated at defined intervals, when circumstances require changes, and when system components are installed or upgraded.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | Systems containing production-like data |
| Test Systems | CONDITIONAL | Only if containing sensitive data |
| Network Infrastructure | YES | Routers, switches, firewalls, load balancers |
| Cloud Resources | YES | IaaS, PaaS, and SaaS configurations |
| Mobile Devices | YES | Organization-managed devices only |
| IoT Devices | YES | Connected to organizational networks |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Ensure baseline configurations are developed and maintained<br>• Approve baseline configuration changes<br>• Review baselines quarterly |
| Configuration Managers | • Document and maintain baseline configurations<br>• Implement configuration control processes<br>• Track configuration changes |
| Security Team | • Review baseline configurations for security compliance<br>• Validate security control implementations<br>• Monitor configuration drift |

## 4. RULES
[RULE-01] All information systems MUST have a documented baseline configuration that includes connectivity, operational, and communications aspects.
[VALIDATION] IF system_in_production = TRUE AND baseline_configuration_exists = FALSE THEN critical_violation

[RULE-02] Baseline configurations MUST be maintained under formal configuration control with version tracking and change approval processes.
[VALIDATION] IF baseline_exists = TRUE AND configuration_control = FALSE THEN major_violation

[RULE-03] Baseline configurations MUST be reviewed and updated at least quarterly or within 30 days of significant system changes.
[VALIDATION] IF last_baseline_review > 90_days AND no_documented_exception = TRUE THEN major_violation

[RULE-04] Baseline configurations MUST be updated within 5 business days when system components are installed or upgraded.
[VALIDATION] IF component_change_date + 5_business_days < current_date AND baseline_updated = FALSE THEN major_violation

[RULE-05] Baseline configurations MUST include security and privacy control implementations, network topology, and logical component placement.
[VALIDATION] IF baseline_missing_security_controls = TRUE OR baseline_missing_network_topology = TRUE THEN major_violation

[RULE-06] All baseline configuration changes MUST be formally reviewed and approved by the system owner and security team.
[VALIDATION] IF baseline_change = TRUE AND (owner_approval = FALSE OR security_approval = FALSE) THEN major_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Baseline Configuration Development - Process for creating initial system baseline configurations
- [PROC-02] Configuration Control Management - Process for managing changes to baseline configurations
- [PROC-03] Baseline Review and Update - Quarterly review process and change-triggered update procedures
- [PROC-04] Configuration Drift Detection - Automated monitoring and remediation of configuration deviations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system changes, security incidents involving configuration issues, regulatory requirement changes, technology refresh cycles

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Deployment]
IF system_status = "production"
AND baseline_configuration_documented = FALSE
AND deployment_date > 0_days
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Component Upgrade Without Baseline Update]
IF component_upgraded = TRUE
AND upgrade_date + 5_business_days < current_date
AND baseline_updated = FALSE
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-03: Quarterly Review Overdue]
IF last_baseline_review > 90_days
AND system_changes_occurred = TRUE
AND documented_exception = FALSE
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-04: Configuration Drift Detected]
IF current_configuration != baseline_configuration
AND drift_duration > 24_hours
AND remediation_plan = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Change Without Approval]
IF baseline_change = TRUE
AND change_type = "emergency"
AND post_change_approval_within_72_hours = FALSE
THEN compliance = FALSE
violation_severity = "Major"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Current baseline configuration developed and documented | [RULE-01] |
| Baseline configuration maintained under configuration control | [RULE-02] |
| Baseline reviewed and updated at defined frequency | [RULE-03] |
| Baseline updated when circumstances require | [RULE-03] |
| Baseline updated when components installed or upgraded | [RULE-04] |
| Baseline includes required technical specifications | [RULE-05] |