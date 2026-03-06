# POLICY: SR-3(2): Limitation of Harm

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-3(2) |
| NIST Control | SR-3(2): Limitation of Harm |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, adversary targeting, harm limitation, vendor management, procurement |

## 1. POLICY STATEMENT
The organization SHALL implement specific controls to limit harm from potential adversaries identifying and targeting the organizational supply chain. These controls MUST be formally defined, documented, and consistently employed across all supply chain activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All procurement activities | YES | Including hardware, software, and services |
| Third-party vendors | YES | All suppliers in the supply chain |
| Custom configurations | YES | Special focus on non-standard items |
| Maintenance contracts | YES | Including update and patch delivery |
| Cloud service providers | YES | All external service dependencies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define supply chain adversary limitation controls<br>• Approve vendor security requirements<br>• Oversee supply chain risk assessments |
| Procurement Manager | • Implement approved vendor list requirements<br>• Execute procurement carve-outs<br>• Coordinate diverse delivery routes |
| Supply Chain Risk Manager | • Maintain contingency plans for supply chain events<br>• Monitor threat intelligence for supply chain risks<br>• Assess vendor security postures |

## 4. RULES
[RULE-01] The organization MUST maintain a formally documented list of controls designed to limit harm from supply chain adversaries.
[VALIDATION] IF supply_chain_controls_documented = FALSE THEN violation

[RULE-02] Procurement activities MUST prioritize standardized configurations over custom solutions unless business justification is documented and approved.
[VALIDATION] IF configuration_type = "custom" AND business_justification_approved = FALSE THEN violation

[RULE-03] All vendors MUST be selected from an approved vendor list that includes reputation verification and security assessment results.
[VALIDATION] IF vendor_on_approved_list = FALSE AND emergency_exception = FALSE THEN violation

[RULE-04] Maintenance schedules and update delivery mechanisms MUST follow pre-agreed timelines and security protocols.
[VALIDATION] IF maintenance_schedule_agreed = FALSE OR security_protocols_defined = FALSE THEN violation

[RULE-05] Supply chain contingency plans MUST be maintained and tested annually for critical suppliers.
[VALIDATION] IF supplier_criticality = "high" AND (contingency_plan_exists = FALSE OR last_test_date > 365_days) THEN violation

[RULE-06] Procurement contracts MUST include carve-out provisions for security-related exclusions and obligations.
[VALIDATION] IF contract_type = "supply_chain" AND security_carveouts_included = FALSE THEN violation

[RULE-07] Delivery mechanisms MUST utilize diverse routes for critical supply chain components when feasible.
[VALIDATION] IF component_criticality = "high" AND delivery_route_diversity = FALSE AND feasibility_documented = FALSE THEN violation

[RULE-08] Time between purchase decisions and delivery MUST be minimized and monitored for security exposure periods.
[VALIDATION] IF purchase_to_delivery_time > defined_threshold AND risk_mitigation_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Adversary Control Definition - Establish and maintain controls to limit adversary targeting
- [PROC-02] Approved Vendor List Management - Maintain and regularly update vendor reputation assessments
- [PROC-03] Supply Chain Contingency Planning - Develop and test response plans for supply chain disruptions
- [PROC-04] Procurement Security Review - Assess security implications of procurement decisions
- [PROC-05] Delivery Route Diversification - Implement multiple delivery channels for critical components

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain security incidents, new threat intelligence, vendor security breaches, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Custom Configuration Procurement]
IF configuration_type = "custom"
AND business_justification_approved = FALSE
AND security_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Unapproved Vendor Usage]
IF vendor_on_approved_list = FALSE
AND emergency_exception = FALSE
AND procurement_value > threshold
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Contingency Plan]
IF supplier_criticality = "high"
AND contingency_plan_exists = FALSE
AND dependency_level = "critical"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Single Delivery Route Risk]
IF component_criticality = "high"
AND delivery_route_diversity = FALSE
AND feasibility_assessment_completed = TRUE
AND alternative_routes_available = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Extended Purchase Timeline]
IF purchase_to_delivery_time > 30_days
AND risk_mitigation_documented = FALSE
AND component_security_sensitivity = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls to limit harm from potential supply chain adversaries are defined | [RULE-01] |
| Controls are employed to limit harm from potential adversaries identifying and targeting the organizational supply chain | [RULE-02], [RULE-03], [RULE-04], [RULE-05], [RULE-06], [RULE-07], [RULE-08] |