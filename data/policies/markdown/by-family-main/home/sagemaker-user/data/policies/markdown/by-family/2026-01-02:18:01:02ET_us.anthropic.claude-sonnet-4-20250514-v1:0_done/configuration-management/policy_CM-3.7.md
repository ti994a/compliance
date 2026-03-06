# POLICY: CM-3.7: Review System Changes

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-3.7 |
| NIST Control | CM-3.7: Review System Changes |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system changes, unauthorized changes, change review, configuration management, change control |

## 1. POLICY STATEMENT
The organization SHALL review system changes at defined frequencies or under defined circumstances to identify unauthorized modifications. All system changes MUST be systematically evaluated to ensure they were properly authorized and implemented according to approved change control procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | CONDITIONAL | Only if connected to production networks |
| Test Systems | CONDITIONAL | Only if containing production data |
| Cloud Infrastructure | YES | Including IaaS, PaaS, and SaaS configurations |
| Network Devices | YES | Routers, switches, firewalls, load balancers |
| Security Tools | YES | SIEM, vulnerability scanners, monitoring tools |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Change Control Board | • Review and approve change review procedures<br>• Define circumstances requiring immediate review<br>• Escalate unauthorized changes |
| System Administrators | • Conduct scheduled change reviews<br>• Document review findings<br>• Report unauthorized changes immediately |
| Security Operations Center | • Monitor for unauthorized changes<br>• Trigger change reviews based on alerts<br>• Coordinate incident response for unauthorized changes |

## 4. RULES
[RULE-01] System changes MUST be reviewed at least monthly for all production systems and weekly for critical systems.
[VALIDATION] IF system_criticality = "critical" AND last_review_date > 7_days THEN violation
[VALIDATION] IF system_criticality = "production" AND last_review_date > 30_days THEN violation

[RULE-02] Change reviews MUST be triggered immediately when security monitoring tools detect unauthorized modifications.
[VALIDATION] IF unauthorized_change_detected = TRUE AND review_initiated_time > 4_hours THEN violation

[RULE-03] All change reviews MUST document findings, including verification of authorization status and compliance with change procedures.
[VALIDATION] IF change_review_completed = TRUE AND documentation_complete = FALSE THEN violation

[RULE-04] Unauthorized changes MUST be reported to the security team within 2 hours of discovery and remediated within 24 hours.
[VALIDATION] IF unauthorized_change_found = TRUE AND report_time > 2_hours THEN violation
[VALIDATION] IF unauthorized_change_found = TRUE AND remediation_time > 24_hours THEN critical_violation

[RULE-05] Change review procedures MUST define specific circumstances that trigger immediate reviews, including security incidents and compliance audits.
[VALIDATION] IF trigger_circumstances_defined = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Scheduled Change Review - Monthly review process for identifying unauthorized changes
- [PROC-02] Event-Triggered Review - Process for immediate reviews based on security alerts
- [PROC-03] Unauthorized Change Response - Incident response procedures for unauthorized modifications
- [PROC-04] Change Review Documentation - Requirements for documenting review activities and findings

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized changes, audit findings, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missed Monthly Review]
IF system_type = "production"
AND last_change_review > 30_days
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Undetected Critical System Change]
IF system_criticality = "critical"
AND unauthorized_change_detected = TRUE
AND detection_time > 24_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Response to Security Alert]
IF security_alert_triggered = TRUE
AND change_review_initiated = FALSE
AND alert_age > 4_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Incomplete Change Documentation]
IF change_review_conducted = TRUE
AND findings_documented = FALSE
AND review_date < 30_days_ago
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Proper Emergency Review]
IF emergency_change_detected = TRUE
AND review_initiated_within = 1_hour
AND security_team_notified = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Changes reviewed at defined frequency | [RULE-01] |
| Changes reviewed under defined circumstances | [RULE-02], [RULE-05] |
| Unauthorized changes identified through review | [RULE-03], [RULE-04] |
| Review process documented and followed | [RULE-03] |