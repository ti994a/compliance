# POLICY: AC-2.12: Account Monitoring for Atypical Usage

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-2.12 |
| NIST Control | AC-2.12: Account Monitoring for Atypical Usage |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | account monitoring, atypical usage, anomaly detection, behavioral analysis, security monitoring |

## 1. POLICY STATEMENT
The organization SHALL monitor all system accounts for atypical usage patterns that deviate from established baselines and immediately report suspicious activities to designated security personnel. This monitoring enables early detection of compromised accounts, insider threats, and unauthorized access attempts across all information systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All user accounts | YES | Including employees, contractors, service accounts |
| Administrative accounts | YES | Enhanced monitoring requirements |
| Service accounts | YES | Automated behavior pattern analysis |
| Guest/temporary accounts | YES | Limited duration monitoring |
| Cloud infrastructure accounts | YES | Multi-tenant environment monitoring |
| Third-party system accounts | CONDITIONAL | When integrated with corporate systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Monitor account usage dashboards 24/7<br>• Investigate atypical usage alerts<br>• Escalate confirmed incidents per IR procedures |
| System Administrators | • Configure monitoring tools and baselines<br>• Maintain account usage pattern databases<br>• Implement automated alerting mechanisms |
| Privacy Officer | • Assess privacy impacts of monitoring activities<br>• Ensure compliance with privacy regulations<br>• Review data retention policies for monitoring data |
| Account Owners | • Report known legitimate usage pattern changes<br>• Respond to account verification requests<br>• Participate in incident response activities |

## 4. RULES

[RULE-01] All system accounts MUST be continuously monitored for atypical usage patterns including unusual login times, geographic locations, access patterns, and resource utilization.
[VALIDATION] IF monitoring_coverage < 100% OF active_accounts THEN violation

[RULE-02] Atypical usage detection systems MUST establish behavioral baselines within 30 days of account creation and update baselines monthly thereafter.
[VALIDATION] IF account_age > 30_days AND baseline_established = FALSE THEN violation

[RULE-03] Atypical usage alerts MUST be reported to SOC personnel within 15 minutes of detection for high-risk accounts and within 1 hour for standard accounts.
[VALIDATION] IF alert_severity = "high" AND notification_time > 15_minutes THEN critical_violation
[VALIDATION] IF alert_severity = "standard" AND notification_time > 1_hour THEN violation

[RULE-04] Administrative and privileged accounts MUST have enhanced monitoring with real-time alerting for any usage outside normal business hours or approved maintenance windows.
[VALIDATION] IF account_privilege = "admin" AND access_time OUTSIDE business_hours AND maintenance_window = FALSE THEN immediate_alert

[RULE-05] Geographic location anomalies MUST trigger immediate alerts when account access occurs from countries not on the approved access list or simultaneous logins from geographically impossible locations.
[VALIDATION] IF login_country NOT IN approved_countries OR impossible_travel = TRUE THEN critical_alert

[RULE-06] Privacy impact assessments MUST be conducted and updated annually for all account monitoring activities to ensure compliance with privacy regulations.
[VALIDATION] IF privacy_assessment_date < (current_date - 365_days) THEN compliance_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Account Baseline Establishment - Define normal usage patterns for each account type
- [PROC-02] Atypical Usage Investigation - Standardized process for alert triage and investigation
- [PROC-03] Privacy Impact Assessment - Annual review of monitoring privacy implications
- [PROC-04] Monitoring Tool Configuration - Setup and maintenance of detection systems
- [PROC-05] Incident Escalation - Procedures for reporting confirmed account compromises

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving account compromise, new monitoring technologies, privacy regulation changes, significant organizational changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: After-Hours Administrative Access]
IF account_type = "administrative"
AND access_time BETWEEN 22:00 AND 06:00
AND maintenance_window = FALSE
AND approval_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Geographic Impossibility]
IF previous_login_location = "New York"
AND current_login_location = "China"
AND time_difference < 8_hours
AND VPN_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Service Account Human Usage Pattern]
IF account_type = "service"
AND login_method = "interactive"
AND usage_pattern = "human-like"
AND authorized_human_access = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Baseline Not Established]
IF account_age > 30_days
AND behavioral_baseline = "not_established"
AND monitoring_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Privacy Assessment Overdue]
IF monitoring_system = "active"
AND privacy_assessment_date < (current_date - 365_days)
AND personal_data_processed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System accounts are monitored for defined atypical usage | [RULE-01], [RULE-02] |
| Atypical usage is reported to designated personnel | [RULE-03], [RULE-04] |
| Enhanced monitoring for privileged accounts | [RULE-04] |
| Geographic anomaly detection | [RULE-05] |
| Privacy impact consideration | [RULE-06] |