# POLICY: PM-30.1: Suppliers of Critical or Mission-essential Items

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-30.1 |
| NIST Control | PM-30.1: Suppliers of Critical or Mission-essential Items |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | suppliers, critical technologies, mission-essential, supply chain risk, vendor assessment, prioritization |

## 1. POLICY STATEMENT
The organization SHALL identify, prioritize, and assess all suppliers providing critical or mission-essential technologies, products, and services to ensure supply chain security and business continuity. This assessment process enables informed risk-based decisions regarding supplier relationships and supply chain risk mitigation strategies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All suppliers | CONDITIONAL | Only those providing critical/mission-essential items |
| Technology vendors | YES | Hardware, software, cloud services |
| Service providers | CONDITIONAL | Only mission-essential services |
| Subcontractors | YES | When supporting critical functions |
| Internal procurement teams | YES | All procurement activities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Oversee supplier identification and prioritization process<br>• Approve critical supplier classifications<br>• Ensure policy compliance across procurement activities |
| Supply Chain Risk Manager | • Conduct supplier risk assessments<br>• Maintain supplier inventory and risk ratings<br>• Coordinate with security teams on risk mitigation |
| Business Unit Leaders | • Identify critical/mission-essential requirements<br>• Participate in supplier prioritization decisions<br>• Implement approved risk mitigation measures |

## 4. RULES

[RULE-01] The organization MUST maintain a comprehensive inventory of all suppliers providing critical or mission-essential technologies, products, and services.
[VALIDATION] IF supplier_provides_critical_items = TRUE AND supplier_in_inventory = FALSE THEN violation

[RULE-02] Critical and mission-essential suppliers MUST be prioritized based on business impact, security risk, and operational dependency using a documented risk-based methodology.
[VALIDATION] IF supplier_criticality_level IS NULL AND supplier_provides_critical_items = TRUE THEN violation

[RULE-03] All identified critical suppliers MUST undergo formal risk assessment within 90 days of identification and annually thereafter.
[VALIDATION] IF supplier_criticality_level >= "HIGH" AND (assessment_date IS NULL OR days_since_assessment > 365) THEN violation

[RULE-04] Supplier assessments MUST evaluate security controls, financial stability, geographic risk, and supply chain dependencies as minimum criteria.
[VALIDATION] IF assessment_completed = TRUE AND (security_controls_evaluated = FALSE OR financial_stability_evaluated = FALSE OR geographic_risk_evaluated = FALSE OR supply_chain_dependencies_evaluated = FALSE) THEN violation

[RULE-05] High-risk critical suppliers MUST have documented risk mitigation plans implemented within 60 days of assessment completion.
[VALIDATION] IF supplier_risk_level = "HIGH" AND supplier_criticality_level >= "HIGH" AND (mitigation_plan_exists = FALSE OR mitigation_implementation_date IS NULL) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supplier Identification and Classification - Process for identifying and categorizing suppliers by criticality
- [PROC-02] Supplier Risk Assessment - Standardized assessment methodology and criteria
- [PROC-03] Supplier Prioritization Matrix - Risk-based prioritization framework
- [PROC-04] Risk Mitigation Planning - Development and implementation of supplier risk mitigation strategies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supply chain incidents, regulatory changes, significant business model changes, merger/acquisition activities

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unassessed Critical Cloud Provider]
IF supplier_type = "cloud_service_provider"
AND services_provided CONTAINS "critical_business_applications"
AND formal_assessment_completed = FALSE
AND contract_duration > 90_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated High-Risk Supplier Assessment]
IF supplier_criticality_level = "HIGH"
AND supplier_risk_level = "HIGH"
AND days_since_last_assessment > 365
AND business_dependency = "CRITICAL"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Risk Mitigation for Critical Supplier]
IF supplier_criticality_level >= "HIGH"
AND supplier_risk_level = "HIGH"
AND mitigation_plan_exists = FALSE
AND days_since_assessment_completion > 60
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Compliant Prioritized Supplier Management]
IF supplier_in_inventory = TRUE
AND supplier_criticality_level IS NOT NULL
AND days_since_assessment <= 365
AND (supplier_risk_level != "HIGH" OR mitigation_plan_implemented = TRUE)
THEN compliance = TRUE

[SCENARIO-05: Critical Supplier Without Inventory Documentation]
IF supplier_provides_critical_items = TRUE
AND supplier_in_inventory = FALSE
AND contract_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Suppliers of critical or mission-essential technologies, products, and services are identified | [RULE-01] |
| Suppliers of critical or mission-essential technologies, products, and services are prioritized | [RULE-02] |
| Suppliers of critical or mission-essential technologies, products, and services are assessed | [RULE-03], [RULE-04] |