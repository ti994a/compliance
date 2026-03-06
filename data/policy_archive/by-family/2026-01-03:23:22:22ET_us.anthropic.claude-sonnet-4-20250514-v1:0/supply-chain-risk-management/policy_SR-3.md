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
The organization SHALL establish comprehensive processes to identify and address weaknesses in supply chain elements and implement controls to protect against supply chain risks. All supply chain processes and controls MUST be documented in security and privacy plans and coordinated with designated supply chain personnel.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems and components | YES | Including hardware, software, firmware |
| Third-party vendors/suppliers | YES | All tiers of supply chain |
| System integrators | YES | Prime and subcontractors |
| Cloud service providers | YES | IaaS, PaaS, SaaS providers |
| Internal development teams | YES | In-house software/hardware development |
| Legacy systems | CONDITIONAL | Based on criticality assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Risk Officer | • Establish supply chain risk management strategy<br>• Coordinate with supply chain personnel<br>• Approve supply chain controls |
| Procurement Manager | • Implement supplier assessment processes<br>• Maintain vendor risk registers<br>• Execute contract security requirements |
| Security Team | • Define supply chain security controls<br>• Assess supply chain vulnerabilities<br>• Monitor supply chain incidents |
| System Owners | • Document supply chain controls in security plans<br>• Implement system-specific supply chain protections<br>• Report supply chain weaknesses |

## 4. RULES

[RULE-01] The organization MUST establish documented processes to identify and address weaknesses or deficiencies in supply chain elements and processes for all in-scope systems and components.
[VALIDATION] IF system_in_scope = TRUE AND supply_chain_process_documented = FALSE THEN violation

[RULE-02] Supply chain weakness identification processes MUST be coordinated with designated supply chain personnel and reviewed quarterly.
[VALIDATION] IF supply_chain_coordination = FALSE OR last_review_date > 90_days THEN violation

[RULE-03] The organization SHALL employ defined controls to protect against supply chain risks and limit harm from supply chain-related events.
[VALIDATION] IF supply_chain_controls_defined = FALSE OR supply_chain_controls_implemented = FALSE THEN violation

[RULE-04] All selected and implemented supply chain processes and controls MUST be documented in system security plans and privacy plans.
[VALIDATION] IF supply_chain_controls_in_ssp = FALSE OR supply_chain_controls_in_privacy_plan = FALSE THEN violation

[RULE-05] Supply chain elements and processes MUST be inventoried and risk-assessed at least annually or when significant changes occur.
[VALIDATION] IF last_supply_chain_assessment > 365_days AND no_significant_changes = FALSE THEN violation

[RULE-06] Critical supply chain vulnerabilities MUST be addressed within 30 days of identification, with temporary mitigations implemented within 72 hours.
[VALIDATION] IF vulnerability_severity = "critical" AND remediation_time > 30_days AND mitigation_time > 72_hours THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment - Annual comprehensive assessment of all supply chain elements
- [PROC-02] Vendor Security Evaluation - Pre-contract security assessment for new suppliers
- [PROC-03] Supply Chain Incident Response - Process for responding to supply chain security events
- [PROC-04] Supply Chain Monitoring - Continuous monitoring of supplier security posture
- [PROC-05] Contract Security Requirements - Standard security clauses for supplier agreements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major supply chain incidents, regulatory changes, significant vendor changes, M&A activity

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Critical Vendor Onboarding]
IF vendor_criticality = "high"
AND security_assessment_completed = FALSE
AND contract_signed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Supply Chain Vulnerability Discovery]
IF vulnerability_identified = TRUE
AND vulnerability_severity = "critical"
AND mitigation_implemented = FALSE
AND discovery_date > 72_hours_ago
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Undocumented Supply Chain Controls]
IF supply_chain_controls_implemented = TRUE
AND controls_documented_in_ssp = FALSE
AND system_authorization_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Supply Chain Process Coordination]
IF supply_chain_process_exists = TRUE
AND coordination_with_personnel = FALSE
AND last_coordination_meeting > 90_days_ago
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Annual Assessment Overdue]
IF last_supply_chain_assessment > 365_days
AND system_operational = TRUE
AND assessment_extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Establish process to identify supply chain weaknesses | RULE-01 |
| Coordinate with supply chain personnel | RULE-02 |
| Employ controls to protect against supply chain risks | RULE-03 |
| Document supply chain controls in security/privacy plans | RULE-04 |
| Regular assessment of supply chain elements | RULE-05 |
| Timely remediation of supply chain vulnerabilities | RULE-06 |