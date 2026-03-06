# POLICY: SI-4.17: Integrated Situational Awareness

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.17 |
| NIST Control | SI-4.17: Integrated Situational Awareness |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | situational awareness, correlation, monitoring, physical security, cyber security, supply chain, threat detection |

## 1. POLICY STATEMENT
The organization SHALL correlate information from monitoring physical, cyber, and supply chain activities to achieve integrated, organization-wide situational awareness. This correlation capability enables detection of sophisticated multi-vector attacks and enhances the organization's ability to identify attack methods and techniques across all operational domains.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, and hybrid environments |
| Physical Security Systems | YES | Access controls, surveillance, environmental monitoring |
| Supply Chain Partners | YES | Tier 1 and critical Tier 2 suppliers |
| Third-party Services | YES | Cloud providers, managed services, SaaS applications |
| Remote Work Locations | CONDITIONAL | When accessing corporate resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) Manager | • Oversee correlation platform operations<br>• Ensure 24/7 monitoring coverage<br>• Coordinate incident response across domains |
| Physical Security Manager | • Provide physical monitoring data feeds<br>• Maintain physical security system integration<br>• Support correlation analysis for physical events |
| Supply Chain Risk Manager | • Monitor supplier security posture<br>• Provide supply chain threat intelligence<br>• Coordinate supplier incident reporting |
| IT Security Architect | • Design correlation architecture<br>• Ensure data integration capabilities<br>• Maintain correlation rule effectiveness |

## 4. RULES
[RULE-01] The organization MUST implement automated correlation capabilities that integrate data from physical security systems, cybersecurity monitoring tools, and supply chain risk monitoring systems.
[VALIDATION] IF correlation_platform_deployed = TRUE AND physical_integration = TRUE AND cyber_integration = TRUE AND supply_chain_integration = TRUE THEN compliant

[RULE-02] Correlation analysis MUST be performed in real-time with alert generation within 15 minutes of detecting correlated events across multiple domains.
[VALIDATION] IF correlation_time > 15_minutes THEN violation

[RULE-03] The organization SHALL maintain correlation rules that detect multi-vector attacks spanning physical, cyber, and supply chain domains, with rules reviewed and updated quarterly.
[VALIDATION] IF correlation_rules_review_date < (current_date - 90_days) THEN violation

[RULE-04] All correlation events with medium or higher severity MUST be investigated within 4 hours and documented with findings and actions taken.
[VALIDATION] IF correlation_event_severity >= "medium" AND investigation_time > 4_hours THEN violation

[RULE-05] Supply chain monitoring data MUST include security status updates from Tier 1 suppliers and critical Tier 2 suppliers, updated at least weekly.
[VALIDATION] IF supplier_tier <= 2 AND criticality = "high" AND last_update > 7_days THEN violation

[RULE-06] Physical security event data feeds MUST include access control violations, surveillance alerts, and environmental anomalies with correlation timestamps synchronized within 1 second.
[VALIDATION] IF timestamp_drift > 1_second THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Integrated Monitoring Correlation - Automated correlation of multi-domain security events
- [PROC-02] Cross-Domain Incident Response - Coordinated response to correlated threats
- [PROC-03] Supplier Security Monitoring - Continuous monitoring of supply chain security posture
- [PROC-04] Correlation Rule Management - Regular review and update of correlation algorithms

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incident, significant infrastructure changes, new threat intelligence, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Multi-Vector Attack Detection]
IF cyber_anomaly_detected = TRUE
AND physical_access_violation = TRUE
AND event_time_correlation < 30_minutes
AND correlation_alert_generated = TRUE
THEN compliance = TRUE

[SCENARIO-02: Supply Chain Compromise Correlation]
IF supplier_security_incident = TRUE
AND internal_network_anomaly = TRUE
AND correlation_analysis_performed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Correlation Response]
IF multi_domain_correlation = TRUE
AND alert_severity = "high"
AND investigation_start_time > 4_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete Data Integration]
IF physical_monitoring_integrated = FALSE
AND cyber_monitoring_integrated = TRUE
AND supply_chain_monitoring_integrated = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Correlation Rule Staleness]
IF correlation_rules_exist = TRUE
AND last_rule_review > 90_days
AND new_threat_intelligence_available = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information from monitoring physical, cyber, and supply chain activities are correlated | RULE-01, RULE-03 |
| Integrated, organization-wide situational awareness is achieved | RULE-02, RULE-04 |
| Multi-domain correlation capability is maintained | RULE-05, RULE-06 |