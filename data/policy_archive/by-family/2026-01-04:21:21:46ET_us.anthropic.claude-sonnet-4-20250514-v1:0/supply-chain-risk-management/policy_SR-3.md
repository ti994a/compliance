# POLICY: SR-3: Supply Chain Controls and Processes

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-3 |
| NIST Control | SR-3: Supply Chain Controls and Processes |
| Version | 1.0 |
| Owner | Chief Supply Chain Risk Officer |
| Keywords | supply chain, vendor management, third-party risk, procurement, supplier assessment |

## 1. POLICY STATEMENT
The organization SHALL establish comprehensive processes to identify and address supply chain weaknesses and deficiencies in coordination with supply chain personnel. All supply chain controls and processes MUST be documented in security and privacy plans to protect against supply chain risks and limit harm from supply chain-related events.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems and system components | YES | Including hardware, software, firmware |
| Third-party suppliers and vendors | YES | Throughout entire lifecycle |
| Supply chain personnel | YES | Internal and external stakeholders |
| Development and manufacturing processes | YES | From design through disposal |
| Service providers | YES | Including cloud and managed services |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Risk Officer | • Establish supply chain risk management strategy<br>• Coordinate with supply chain personnel<br>• Oversee supply chain control implementation |
| Procurement Manager | • Implement supplier assessment processes<br>• Maintain supplier risk registers<br>• Execute contract security requirements |
| Security Team | • Define supply chain security controls<br>• Assess supplier security posture<br>• Monitor supply chain threats |
| System Owners | • Document supply chain controls in security plans<br>• Implement system-specific supply chain protections<br>• Report supply chain incidents |

## 4. RULES
[RULE-01] Organizations MUST establish documented processes to identify and address weaknesses or deficiencies in supply chain elements and processes for all systems and system components.
[VALIDATION] IF system_has_supply_chain_process = FALSE THEN violation

[RULE-02] Supply chain weakness identification processes MUST be coordinated with designated supply chain personnel including suppliers, integrators, and internal stakeholders.
[VALIDATION] IF supply_chain_coordination_documented = FALSE THEN violation

[RULE-03] Organizations SHALL employ defined supply chain controls to protect against supply chain risks and limit harm from supply chain-related events.
[VALIDATION] IF supply_chain_controls_implemented = FALSE OR supply_chain_controls_defined = FALSE THEN violation

[RULE-04] All selected and implemented supply chain processes and controls MUST be documented in system security plans and privacy plans.
[VALIDATION] IF supply_chain_controls_in_security_plan = FALSE OR supply_chain_controls_in_privacy_plan = FALSE THEN violation

[RULE-05] Supply chain risk assessments MUST be conducted for all suppliers handling sensitive data or critical system components within 90 days of engagement.
[VALIDATION] IF supplier_risk_assessment_date > engagement_date + 90_days THEN violation

[RULE-06] Supply chain personnel roles and responsibilities MUST be clearly defined and documented with annual review requirements.
[VALIDATION] IF supply_chain_roles_documented = FALSE OR last_review_date > 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supplier Risk Assessment - Evaluate security posture of all supply chain partners
- [PROC-02] Supply Chain Monitoring - Continuous monitoring of supplier security status
- [PROC-03] Weakness Remediation - Process for addressing identified supply chain deficiencies
- [PROC-04] Supply Chain Incident Response - Response procedures for supply chain security events
- [PROC-05] Contract Security Requirements - Standard security clauses for supplier agreements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain incidents, new supplier onboarding, regulatory changes, significant system modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Critical Supplier Onboarding]
IF supplier_criticality = "high"
AND risk_assessment_completed = FALSE
AND engagement_date < current_date - 90_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Undocumented Supply Chain Controls]
IF system_security_plan_exists = TRUE
AND supply_chain_controls_documented = FALSE
AND system_has_suppliers = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Supply Chain Coordination Gap]
IF supply_chain_process_exists = TRUE
AND coordination_with_personnel_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Supply Chain Weakness Process]
IF system_operational = TRUE
AND supply_chain_weakness_process_established = FALSE
AND external_dependencies = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Outdated Supply Chain Documentation]
IF supply_chain_controls_documented = TRUE
AND last_update_date > current_date - 365_days
AND system_changes_occurred = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Process established to identify supply chain weaknesses | RULE-01 |
| Coordination with supply chain personnel | RULE-02, RULE-06 |
| Supply chain controls employed | RULE-03 |
| Controls documented in security/privacy plans | RULE-04 |
| Supplier risk assessment requirements | RULE-05 |
| Supply chain personnel definition | RULE-06 |