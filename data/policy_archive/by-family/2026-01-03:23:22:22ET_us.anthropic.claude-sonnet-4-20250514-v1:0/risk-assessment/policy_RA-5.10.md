# POLICY: RA-5.10: Correlate Scanning Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-5.10 |
| NIST Control | RA-5.10: Correlate Scanning Information |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | vulnerability scanning, attack vectors, correlation, multi-hop attacks, risk assessment |

## 1. POLICY STATEMENT
The organization SHALL correlate vulnerability scanning outputs to identify multi-vulnerability and multi-hop attack vectors that could enable adversary exploitation. Correlation analysis MUST be performed to understand how individual vulnerabilities combine to create complex attack paths across systems and network boundaries.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, hybrid, and on-premises |
| Network Infrastructure | YES | Routers, switches, firewalls, load balancers |
| Applications | YES | Web apps, databases, APIs, microservices |
| IoT/OT Devices | YES | When connected to corporate networks |
| Third-party Systems | CONDITIONAL | When integrated or interconnected |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Vulnerability Management Team | • Perform vulnerability scan correlation analysis<br>• Generate attack vector reports<br>• Maintain correlation tools and processes |
| Security Operations Center | • Monitor correlation outputs<br>• Escalate critical attack vector findings<br>• Integrate findings into threat hunting |
| Risk Management Office | • Assess risk impact of identified attack vectors<br>• Prioritize remediation based on attack complexity<br>• Report to executive leadership |

## 4. RULES
[RULE-01] Vulnerability scanning outputs MUST be correlated within 24 hours of scan completion to identify multi-vulnerability attack vectors.
[VALIDATION] IF scan_completion_time + 24_hours < correlation_analysis_time THEN violation

[RULE-02] Correlation analysis MUST identify and document attack paths that span multiple systems or network segments.
[VALIDATION] IF multi_hop_vectors_identified = FALSE AND interconnected_systems > 1 THEN incomplete_analysis

[RULE-03] Attack vector analysis SHALL utilize attack trees or equivalent methodologies to map vulnerability relationships and exploitation sequences.
[VALIDATION] IF correlation_methodology NOT IN ["attack_trees", "attack_graphs", "kill_chain_analysis"] THEN methodology_violation

[RULE-04] Technology transition periods (e.g., IPv4 to IPv6, legacy to cloud) MUST receive enhanced correlation analysis with weekly frequency.
[VALIDATION] IF technology_transition = TRUE AND correlation_frequency > 7_days THEN insufficient_monitoring

[RULE-05] Critical multi-hop attack vectors MUST be reported to security leadership within 4 hours of identification.
[VALIDATION] IF attack_vector_severity = "critical" AND reporting_time > 4_hours THEN escalation_violation

[RULE-06] Correlation tools and techniques MUST be validated annually and updated to address emerging attack patterns.
[VALIDATION] IF tool_validation_date + 365_days < current_date THEN validation_overdue

## 5. REQUIRED PROCEDURES
- [PROC-01] Vulnerability Scan Correlation - Standardized process for analyzing and correlating scan outputs
- [PROC-02] Attack Vector Documentation - Templates and requirements for documenting identified attack paths
- [PROC-03] Multi-hop Analysis - Methodology for tracing attack vectors across system boundaries
- [PROC-04] Technology Transition Monitoring - Enhanced correlation during infrastructure changes
- [PROC-05] Correlation Tool Management - Maintenance and validation of analysis tools

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major infrastructure changes, new attack vector discovery, correlation tool updates, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unmanaged System During Migration]
IF technology_transition = TRUE
AND unmanaged_systems_identified = TRUE
AND correlation_analysis_performed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Multi-Hop Attack Vector Identified]
IF vulnerability_count > 1
AND attack_path_spans_multiple_systems = TRUE
AND correlation_completed_within_24h = TRUE
AND attack_trees_documented = TRUE
THEN compliance = TRUE

[SCENARIO-03: Critical Attack Vector Delayed Reporting]
IF attack_vector_severity = "critical"
AND identification_to_reporting_time > 4_hours
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Legacy Tool Without Validation]
IF correlation_tool_last_validated + 365_days < current_date
AND tool_still_in_use = TRUE
AND validation_waiver = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Incomplete Cross-System Analysis]
IF interconnected_systems > 1
AND scan_correlation_performed = TRUE
AND multi_system_attack_paths_analyzed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Output correlation from vulnerability scanning tools | [RULE-01], [RULE-02] |
| Multi-vulnerability attack vector determination | [RULE-02], [RULE-03] |
| Multi-hop attack vector identification | [RULE-02], [RULE-04] |
| Technology transition consideration | [RULE-04] |
| Attack vector analysis methodology | [RULE-03] |