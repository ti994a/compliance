# POLICY: CM-7.4: Unauthorized Software — Deny-by-exception

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-7.4 |
| NIST Control | CM-7.4: Unauthorized Software — Deny-by-exception |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | unauthorized software, deny-by-exception, software execution, allow-all policy, software inventory |

## 1. POLICY STATEMENT
The organization SHALL implement a deny-by-exception policy that allows all software to execute except for specifically identified unauthorized programs. All systems MUST maintain and enforce current lists of prohibited software programs and review these lists regularly to prevent execution of unauthorized applications.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing company or customer data |
| Development Systems | YES | Systems with access to production networks |
| Test/Staging Systems | YES | Systems containing production-like data |
| Personal Devices | CONDITIONAL | Only if accessing corporate resources |
| Contractor Systems | CONDITIONAL | Only if processing company data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement and maintain unauthorized software lists<br>• Configure enforcement mechanisms<br>• Monitor for unauthorized software execution |
| Security Team | • Define unauthorized software categories<br>• Review and approve software lists<br>• Conduct compliance assessments |
| Asset Managers | • Maintain software inventory<br>• Track software versions and sources<br>• Coordinate list updates |

## 4. RULES

[RULE-01] All systems MUST maintain a current list of software programs not authorized to execute, including specific versions and sources where applicable.
[VALIDATION] IF system_has_unauthorized_software_list = FALSE THEN critical_violation

[RULE-02] Systems MUST employ technical controls that implement an allow-all, deny-by-exception policy to prevent execution of unauthorized software programs.
[VALIDATION] IF deny_by_exception_policy_implemented = FALSE THEN critical_violation

[RULE-03] Unauthorized software lists MUST be reviewed and updated at least quarterly or within 30 days of identifying new unauthorized software.
[VALIDATION] IF last_review_date > 90_days OR (new_unauthorized_software_identified = TRUE AND update_time > 30_days) THEN violation

[RULE-04] Unauthorized software detection MUST generate alerts and prevent execution in real-time on all production systems.
[VALIDATION] IF unauthorized_software_executed = TRUE AND alert_generated = FALSE THEN critical_violation

[RULE-05] All unauthorized software incidents MUST be logged with details including software name, version, source, user, and timestamp.
[VALIDATION] IF unauthorized_software_detected = TRUE AND incident_logged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Unauthorized Software Identification - Process for identifying and categorizing prohibited software
- [PROC-02] Software List Management - Procedures for maintaining and updating unauthorized software lists
- [PROC-03] Enforcement Mechanism Configuration - Technical implementation of deny-by-exception controls
- [PROC-04] Incident Response - Response procedures for unauthorized software detection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized software, new system deployments, significant infrastructure changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Software Execution]
IF software_execution_attempted = TRUE
AND software_on_unauthorized_list = TRUE
AND execution_blocked = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Outdated Unauthorized Software List]
IF last_list_review > 90_days
AND new_threats_identified = TRUE
AND list_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Enforcement Controls]
IF system_type = "production"
AND unauthorized_software_controls = "not_implemented"
AND system_processes_sensitive_data = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Incident Logging]
IF unauthorized_software_detected = TRUE
AND execution_blocked = TRUE
AND incident_details_logged = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Contractor System Exception]
IF user_type = "contractor"
AND system_access = "corporate_network"
AND unauthorized_software_policy_applied = FALSE
AND data_classification >= "internal"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Software programs not authorized to execute are identified | [RULE-01] |
| Allow-all, deny-by-exception policy is employed | [RULE-02] |
| List of unauthorized software programs is reviewed and updated regularly | [RULE-03] |
| Unauthorized software execution is prevented | [RULE-04] |
| Incidents are properly documented | [RULE-05] |