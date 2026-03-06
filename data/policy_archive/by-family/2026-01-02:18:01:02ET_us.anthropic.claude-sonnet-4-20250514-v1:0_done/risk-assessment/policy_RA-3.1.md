# POLICY: RA-3.1: Supply Chain Risk Assessment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-3.1 |
| NIST Control | RA-3.1: Supply Chain Risk Assessment |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | supply chain, risk assessment, vendors, components, services, third-party |

## 1. POLICY STATEMENT
The organization SHALL assess supply chain risks associated with systems, system components, and system services to identify potential threats to confidentiality, integrity, and availability. Supply chain risk assessments MUST be updated at defined frequencies and when significant changes occur to the supply chain or operational environment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| System Components | YES | Hardware, software, firmware |
| Third-Party Services | YES | SaaS, PaaS, IaaS providers |
| Vendors and Suppliers | YES | Direct and indirect suppliers |
| Development Partners | YES | Custom software development |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee supply chain risk assessment program<br>• Approve risk assessment methodology<br>• Review high-risk findings |
| Supply Chain Manager | • Conduct supply chain risk assessments<br>• Maintain vendor risk profiles<br>• Coordinate with procurement teams |
| System Owners | • Provide system component inventories<br>• Report supply chain changes<br>• Implement risk mitigation measures |

## 4. RULES

[RULE-01] Supply chain risk assessments MUST be conducted for all critical systems, system components, and system services before implementation or procurement.
[VALIDATION] IF system_criticality >= "moderate" AND supply_chain_assessment = FALSE THEN violation

[RULE-02] Supply chain risk assessments SHALL be updated annually and within 30 days of significant supply chain changes.
[VALIDATION] IF last_assessment_date > 365_days OR (significant_change = TRUE AND update_date > 30_days) THEN violation

[RULE-03] Supply chain risk assessments MUST evaluate disruption, counterfeit components, malicious code insertion, and improper delivery practices.
[VALIDATION] IF assessment_scope NOT INCLUDES ["disruption", "counterfeits", "malicious_code", "delivery_practices"] THEN violation

[RULE-04] High-risk supply chain findings MUST be documented and escalated to the Chief Risk Officer within 5 business days.
[VALIDATION] IF risk_level = "high" AND escalation_date > 5_business_days THEN violation

[RULE-05] Supply chain risk mitigation plans MUST be developed for all identified medium and high-risk findings within 30 days of assessment completion.
[VALIDATION] IF (risk_level = "medium" OR risk_level = "high") AND mitigation_plan = FALSE AND days_since_assessment > 30 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment Methodology - Standardized approach for evaluating vendor and component risks
- [PROC-02] Vendor Risk Scoring - Quantitative scoring system for supplier risk levels
- [PROC-03] Supply Chain Incident Response - Process for responding to supply chain security events
- [PROC-04] Third-Party Risk Monitoring - Continuous monitoring of supplier security posture

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supply chain incidents, regulatory changes, significant vendor changes, system architecture changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Critical System Deployment]
IF system_criticality = "high"
AND deployment_status = "pending"
AND supply_chain_assessment = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Vendor Change Without Assessment]
IF vendor_change = TRUE
AND vendor_risk_level = "unknown"
AND days_since_change > 30
AND assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-03: Overdue Assessment Update]
IF last_assessment_date > 365_days
AND system_status = "active"
AND extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-04: High-Risk Finding Not Escalated]
IF risk_finding_level = "high"
AND discovery_date > 5_business_days
AND cro_notification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Mitigation Plan]
IF risk_level IN ["medium", "high"]
AND assessment_completion_date > 30_days
AND mitigation_plan_status = "not_created"
THEN compliance = FALSE
violation_severity = "Medium"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Supply chain risks are assessed for systems, components, and services | [RULE-01], [RULE-03] |
| Risk assessments are updated at defined frequencies | [RULE-02] |
| Risk assessments address significant supply chain changes | [RULE-02] |
| High-risk findings are properly escalated | [RULE-04] |
| Risk mitigation measures are implemented | [RULE-05] |