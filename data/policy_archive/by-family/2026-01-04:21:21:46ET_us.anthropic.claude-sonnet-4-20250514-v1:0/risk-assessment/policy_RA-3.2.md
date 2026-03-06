# POLICY: RA-3(2): Use of All-source Intelligence

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-3(2) |
| NIST Control | RA-3(2): Use of All-source Intelligence |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | all-source intelligence, risk analysis, threat intelligence, supply chain, vulnerability assessment |

## 1. POLICY STATEMENT
The organization SHALL use all-source intelligence to enhance risk analysis activities across all systems, suppliers, and operational environments. All-source intelligence MUST be integrated into risk assessments to identify vulnerabilities from development, manufacturing, delivery processes, personnel, and environmental factors.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| Supply Chain Partners | YES | Multi-tier supplier assessment required |
| Third-party Services | YES | SaaS, PaaS, IaaS providers |
| Development Processes | YES | Internal and outsourced development |
| Personnel Risk Assessments | YES | Contractors and employees with privileged access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee all-source intelligence program<br>• Approve intelligence sharing agreements<br>• Ensure integration with enterprise risk management |
| Threat Intelligence Team | • Collect and analyze all-source intelligence<br>• Produce risk intelligence reports<br>• Maintain intelligence sources and feeds |
| Risk Assessment Teams | • Integrate intelligence into risk assessments<br>• Document intelligence-informed risk decisions<br>• Coordinate with threat intelligence team |

## 4. RULES
[RULE-01] Risk assessments MUST incorporate all-source intelligence including open-source information, measurement and signature intelligence, human intelligence, signals intelligence, and imagery intelligence.
[VALIDATION] IF risk_assessment_conducted = TRUE AND all_source_intelligence_used = FALSE THEN violation

[RULE-02] All-source intelligence analysis MUST be performed on suppliers at multiple tiers in the supply chain sufficient to manage identified risks.
[VALIDATION] IF supplier_risk_assessment = TRUE AND multi_tier_intelligence_analysis = FALSE THEN violation

[RULE-03] Risk intelligence reports MUST be updated at least quarterly or when significant threat landscape changes occur.
[VALIDATION] IF last_intelligence_update > 90_days AND no_significant_threat_change = TRUE THEN violation

[RULE-04] Intelligence sharing agreements with external organizations MUST be documented and approved by the Chief Risk Officer.
[VALIDATION] IF intelligence_sharing = TRUE AND documented_agreement = FALSE THEN violation

[RULE-05] All-source intelligence MUST inform engineering, acquisition, and risk management decisions with documented rationale.
[VALIDATION] IF major_decision_made = TRUE AND intelligence_consideration_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] All-source Intelligence Collection - Systematic gathering from multiple intelligence sources
- [PROC-02] Intelligence Analysis and Risk Correlation - Process for analyzing intelligence and correlating to organizational risks
- [PROC-03] Supply Chain Intelligence Assessment - Multi-tier supplier risk analysis using intelligence
- [PROC-04] Intelligence Sharing Agreement Management - Procedures for establishing and maintaining sharing agreements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major threat landscape changes, new intelligence sources, significant supply chain incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Risk Assessment Without Intelligence]
IF risk_assessment_completed = TRUE
AND all_source_intelligence_integrated = FALSE
AND system_criticality = "HIGH"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Intelligence Reports]
IF current_date - last_intelligence_report_date > 90_days
AND no_threat_landscape_changes = FALSE
AND critical_systems_in_scope = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Supplier Assessment Missing Intelligence]
IF supplier_tier_level <= 2
AND supplier_risk_rating = "HIGH"
AND all_source_intelligence_used = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Undocumented Intelligence Sharing]
IF intelligence_shared_externally = TRUE
AND sharing_agreement_documented = FALSE
AND data_sensitivity = "CONFIDENTIAL"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Decision Without Intelligence Consideration]
IF decision_type IN ["acquisition", "engineering", "risk_management"]
AND decision_impact = "HIGH"
AND intelligence_analysis_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| All-source intelligence is used to assist in the analysis of risk | RULE-01, RULE-02, RULE-05 |
| Intelligence informs engineering and acquisition decisions | RULE-05 |
| Multi-tier supply chain risk analysis | RULE-02 |
| Intelligence sharing agreements are established | RULE-04 |
| Risk intelligence is kept current | RULE-03 |