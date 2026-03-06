# POLICY: SR-3: Supply Chain Controls and Processes

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-3 |
| NIST Control | SR-3: Supply Chain Controls and Processes |
| Version | 1.0 |
| Owner | Chief Supply Chain Risk Officer |
| Keywords | supply chain, risk management, vendor assessment, third-party controls, procurement security |

## 1. POLICY STATEMENT
The organization SHALL establish documented processes to identify and address weaknesses in supply chain elements and processes for all systems and components. Supply chain controls MUST be implemented to protect against supply chain risks and limit harm from supply chain-related events.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid |
| System components | YES | Hardware, software, firmware |
| Third-party suppliers | YES | All tiers of supply chain |
| Service providers | YES | Cloud, managed services, contractors |
| Development processes | YES | Internal and external development |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Risk Officer | • Establish supply chain risk management strategy<br>• Coordinate with supply chain personnel<br>• Oversee supply chain control implementation |
| Procurement Team | • Implement supply chain controls in acquisition processes<br>• Conduct supplier risk assessments<br>• Maintain supplier documentation |
| System Owners | • Document supply chain processes in security plans<br>• Monitor supply chain risks for owned systems<br>• Report supply chain incidents |

## 4. RULES
[RULE-01] Organizations MUST establish documented processes to identify and address weaknesses or deficiencies in supply chain elements and processes for all systems and system components.
[VALIDATION] IF system_deployed = TRUE AND supply_chain_process_documented = FALSE THEN violation

[RULE-02] Supply chain weakness identification processes MUST be coordinated with designated supply chain personnel who have defined roles and responsibilities.
[VALIDATION] IF supply_chain_process_exists = TRUE AND coordination_with_personnel = FALSE THEN violation

[RULE-03] Organizations SHALL employ defined supply chain controls to protect against supply chain risks and limit harm from supply chain-related events.
[VALIDATION] IF supply_chain_controls_defined = TRUE AND controls_implemented = FALSE THEN violation

[RULE-04] Selected and implemented supply chain processes and controls MUST be documented in system security plans and privacy plans.
[VALIDATION] IF supply_chain_controls_implemented = TRUE AND documented_in_plans = FALSE THEN violation

[RULE-05] Supply chain risk assessments MUST be conducted for all critical system components and high-risk suppliers within 90 days of engagement.
[VALIDATION] IF supplier_risk_level = "high" AND assessment_date > engagement_date + 90_days THEN violation

[RULE-06] Supply chain control effectiveness MUST be reviewed annually and updated based on threat landscape changes.
[VALIDATION] IF last_review_date > current_date - 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment - Systematic evaluation of supplier risks and vulnerabilities
- [PROC-02] Supplier Security Requirements - Definition and enforcement of security requirements for suppliers
- [PROC-03] Supply Chain Incident Response - Process for responding to supply chain security events
- [PROC-04] Third-Party Monitoring - Ongoing monitoring of supplier security posture
- [PROC-05] Supply Chain Documentation - Maintenance of supply chain security documentation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supply chain incidents, significant threat intelligence, regulatory changes, new critical suppliers

## 7. SCENARIO PATTERNS
[SCENARIO-01: Undocumented Critical Supplier]
IF supplier_criticality = "high"
AND supply_chain_assessment_completed = FALSE
AND engagement_duration > 90_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Security Plan Documentation]
IF supply_chain_controls_implemented = TRUE
AND security_plan_updated = FALSE
AND privacy_plan_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Uncoordinated Supply Chain Process]
IF supply_chain_process_documented = TRUE
AND supply_chain_personnel_identified = FALSE
AND coordination_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Outdated Risk Assessment]
IF supplier_risk_assessment_exists = TRUE
AND last_assessment_date > current_date - 365_days
AND supplier_risk_level = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Supply Chain Incident Without Controls]
IF supply_chain_incident_occurred = TRUE
AND preventive_controls_implemented = FALSE
AND corrective_actions_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Process establishment for identifying supply chain weaknesses | RULE-01 |
| Coordination with supply chain personnel | RULE-02 |
| Employment of supply chain controls | RULE-03 |
| Documentation in security and privacy plans | RULE-04 |
| Timely risk assessment of critical components | RULE-05 |
| Regular review and updates of controls | RULE-06 |