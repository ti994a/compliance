# POLICY: SI-4.17: Integrated Situational Awareness

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.17 |
| NIST Control | SI-4.17: Integrated Situational Awareness |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | situational awareness, monitoring correlation, physical security, cyber monitoring, supply chain, threat detection |

## 1. POLICY STATEMENT
The organization SHALL correlate information from monitoring physical, cyber, and supply chain activities to achieve integrated, organization-wide situational awareness. This correlation enables detection of sophisticated multi-vector attacks and provides comprehensive threat visibility across all organizational domains.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and hybrid infrastructure |
| Physical facilities | YES | Data centers, offices, manufacturing sites |
| Supply chain partners | YES | Critical suppliers and service providers |
| Monitoring tools | YES | SIEM, physical security, supply chain monitoring |
| Third-party services | CONDITIONAL | If they handle sensitive data or critical functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish correlation requirements<br>• Approve situational awareness procedures<br>• Review correlation effectiveness |
| SOC Manager | • Implement correlation capabilities<br>• Monitor integrated alerts<br>• Coordinate incident response across domains |
| Physical Security Manager | • Provide physical monitoring data<br>• Integrate with cyber monitoring systems<br>• Report physical security events |
| Supply Chain Risk Manager | • Monitor supplier security posture<br>• Report supply chain incidents<br>• Maintain supplier risk assessments |

## 4. RULES
[RULE-01] Organizations MUST implement automated correlation capabilities that integrate physical, cyber, and supply chain monitoring data within a centralized platform.
[VALIDATION] IF correlation_platform = "implemented" AND data_sources >= 3_domains THEN compliant

[RULE-02] Correlation analysis MUST be performed in real-time for critical alerts and within 4 hours for standard monitoring events.
[VALIDATION] IF alert_severity = "critical" AND correlation_time > real_time THEN violation
[VALIDATION] IF alert_severity = "standard" AND correlation_time > 4_hours THEN violation

[RULE-03] Physical security events that may indicate cyber threats MUST be automatically shared with the SOC within 15 minutes of detection.
[VALIDATION] IF physical_event = "security_relevant" AND soc_notification_time > 15_minutes THEN violation

[RULE-04] Supply chain security incidents MUST be correlated with internal monitoring data within 24 hours of notification.
[VALIDATION] IF supply_chain_incident = TRUE AND correlation_completed = FALSE AND time_elapsed > 24_hours THEN violation

[RULE-05] Correlation rules MUST be updated quarterly and after any significant security incident involving multiple attack vectors.
[VALIDATION] IF last_rule_update > 90_days OR (multi_vector_incident = TRUE AND rules_not_updated = TRUE) THEN violation

[RULE-06] Cross-domain correlation findings MUST be documented and reviewed by senior security leadership within 48 hours.
[VALIDATION] IF cross_domain_correlation = TRUE AND leadership_review_time > 48_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Multi-Domain Event Correlation - Automated correlation of physical, cyber, and supply chain events
- [PROC-02] Integrated Alert Escalation - Escalation procedures for correlated multi-domain threats
- [PROC-03] Cross-Domain Incident Response - Coordinated response across physical, cyber, and supply chain teams
- [PROC-04] Situational Awareness Reporting - Regular reporting of integrated threat landscape to leadership

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, infrastructure changes, new monitoring capabilities, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Multi-Vector Attack Detection]
IF cyber_alert = "suspicious_login"
AND physical_alert = "unauthorized_access_attempt"
AND time_correlation <= 2_hours
AND correlation_performed = TRUE
THEN compliance = TRUE

[SCENARIO-02: Supply Chain Compromise]
IF supplier_security_incident = TRUE
AND internal_monitoring_correlated = FALSE
AND incident_age > 24_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Physical-Cyber Event Correlation]
IF physical_security_event = "facility_breach"
AND soc_notification_time > 15_minutes
AND correlation_attempted = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Delayed Correlation Analysis]
IF alert_severity = "critical"
AND correlation_time > real_time
AND automated_correlation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Incomplete Domain Coverage]
IF monitoring_domains < 3
AND correlation_platform = "active"
AND coverage_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information correlation from physical, cyber, and supply chain monitoring | RULE-01, RULE-02 |
| Integrated organization-wide situational awareness | RULE-03, RULE-04, RULE-06 |
| Multi-domain attack detection capability | RULE-01, RULE-05 |
| Cross-domain incident coordination | RULE-06, PROC-03 |