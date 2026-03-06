# POLICY: CM-6.2: Respond to Unauthorized Changes

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-6.2 |
| NIST Control | CM-6.2: Respond to Unauthorized Changes |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | configuration management, unauthorized changes, incident response, alerting, restoration |

## 1. POLICY STATEMENT
The organization SHALL implement automated detection and response procedures for unauthorized changes to system configuration settings. All unauthorized configuration changes MUST trigger predefined response actions including notification, assessment, and remediation within established timeframes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing sensitive data |
| Development Systems | YES | Systems with external connectivity |
| Test/Staging Systems | CONDITIONAL | If containing production data |
| Network Infrastructure | YES | Routers, switches, firewalls, load balancers |
| Security Tools | YES | SIEM, IDS/IPS, vulnerability scanners |
| Cloud Resources | YES | IaaS, PaaS, SaaS configurations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center | • Monitor configuration change alerts<br>• Execute initial response procedures<br>• Escalate critical unauthorized changes |
| System Administrators | • Investigate unauthorized changes<br>• Implement remediation actions<br>• Document response activities |
| Configuration Management Team | • Define baseline configurations<br>• Maintain change detection tools<br>• Review and approve emergency changes |

## 4. RULES

[RULE-01] All systems MUST implement automated configuration monitoring that detects unauthorized changes within 15 minutes of occurrence.
[VALIDATION] IF change_detected = TRUE AND detection_time > 15_minutes THEN violation

[RULE-02] Critical unauthorized changes MUST trigger immediate alerts to the Security Operations Center and system owners within 5 minutes of detection.
[VALIDATION] IF change_criticality = "critical" AND alert_time > 5_minutes THEN critical_violation

[RULE-03] Initial response assessment MUST be completed within 30 minutes for critical changes and 4 hours for non-critical changes.
[VALIDATION] IF change_criticality = "critical" AND assessment_time > 30_minutes THEN violation
[VALIDATION] IF change_criticality = "non-critical" AND assessment_time > 4_hours THEN violation

[RULE-04] Unauthorized changes to security-relevant configurations MUST be reverted to approved baseline within 2 hours unless documented exception exists.
[VALIDATION] IF security_relevant = TRUE AND revert_time > 2_hours AND exception_approved = FALSE THEN violation

[RULE-05] All unauthorized configuration changes and response actions MUST be documented in the incident tracking system within 24 hours.
[VALIDATION] IF documentation_time > 24_hours THEN violation

[RULE-06] Systems with repeated unauthorized changes (3+ in 30 days) MUST undergo comprehensive security review and access control evaluation.
[VALIDATION] IF unauthorized_changes_30days >= 3 AND security_review_initiated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Configuration Change Detection - Automated monitoring and alerting procedures
- [PROC-02] Unauthorized Change Response - Step-by-step response and escalation procedures
- [PROC-03] Configuration Restoration - Baseline restoration and rollback procedures
- [PROC-04] Emergency Change Authorization - Expedited approval for urgent configuration changes
- [PROC-05] Post-Incident Analysis - Root cause analysis and preventive action procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving configuration changes, major system updates, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Critical Security Configuration Change]
IF configuration_type = "security_control"
AND change_authorized = FALSE
AND system_criticality = "high"
AND alert_sent = TRUE
AND response_time <= 30_minutes
THEN compliance = TRUE

[SCENARIO-02: Delayed Response to Unauthorized Change]
IF unauthorized_change_detected = TRUE
AND change_criticality = "critical"
AND response_time > 30_minutes
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Firewall Rule Unauthorized Modification]
IF asset_type = "firewall"
AND rule_change_authorized = FALSE
AND revert_action_taken = TRUE
AND revert_time <= 2_hours
AND incident_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Repeated Unauthorized Changes Without Review]
IF unauthorized_changes_30days >= 3
AND security_review_completed = FALSE
AND days_since_third_incident > 7
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Production Database Configuration Change]
IF system_type = "database"
AND environment = "production"
AND change_authorized = FALSE
AND detection_time <= 15_minutes
AND documentation_complete = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Actions taken upon unauthorized change are defined | [RULE-02], [RULE-03], [RULE-04] |
| Response procedures are implemented | [RULE-01], [RULE-05], [RULE-06] |
| Designated personnel are alerted | [RULE-02] |
| Configuration settings are restored | [RULE-04] |
| Response activities are documented | [RULE-05] |