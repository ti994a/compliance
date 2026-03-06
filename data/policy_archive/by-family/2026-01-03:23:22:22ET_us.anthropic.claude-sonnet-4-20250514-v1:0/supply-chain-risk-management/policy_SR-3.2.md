# POLICY: SR-3.2: Limitation of Harm

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-3.2 |
| NIST Control | SR-3.2: Limitation of Harm |
| Version | 1.0 |
| Owner | Chief Supply Chain Risk Officer |
| Keywords | supply chain, adversary identification, targeting mitigation, vendor management, procurement security |

## 1. POLICY STATEMENT
The organization SHALL implement defined controls to limit harm from potential adversaries identifying and targeting the organizational supply chain. These controls MUST reduce the probability of successful supply chain attacks through strategic procurement, vendor management, and delivery practices.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All procurement activities | YES | Including IT, OT, and facilities |
| Third-party vendors | YES | All tiers of suppliers |
| Supply chain partners | YES | Logistics, distributors, integrators |
| Custom configurations | YES | Higher risk requiring additional controls |
| Emergency procurements | CONDITIONAL | Must follow expedited review process |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Risk Officer | • Define supply chain protection controls<br>• Approve vendor lists and procurement strategies<br>• Oversee contingency planning |
| Procurement Manager | • Implement approved vendor lists<br>• Execute diverse delivery routes<br>• Manage procurement carve-outs |
| Security Architecture Team | • Assess configuration standardization<br>• Review custom component risks<br>• Validate security requirements integration |

## 4. RULES
[RULE-01] The organization MUST maintain an approved vendor list with suppliers having established industry reputations and security track records.
[VALIDATION] IF vendor NOT IN approved_vendor_list AND security_assessment = "incomplete" THEN violation

[RULE-02] Custom or non-standardized configurations SHALL be avoided unless justified by documented business requirements and approved by the Chief Supply Chain Risk Officer.
[VALIDATION] IF configuration_type = "custom" AND business_justification = "absent" AND cscro_approval = FALSE THEN violation

[RULE-03] All procurement activities MUST follow pre-agreed maintenance schedules and update/patch delivery mechanisms with vendors.
[VALIDATION] IF maintenance_schedule = "undefined" OR patch_delivery_mechanism = "unspecified" THEN violation

[RULE-04] Supply chain contingency plans MUST be maintained and tested annually to address potential supply chain disruptions.
[VALIDATION] IF contingency_plan_age > 365_days OR last_test_date > 365_days THEN violation

[RULE-05] Procurement contracts SHALL include carve-outs that provide exclusions for security-related commitments and obligations.
[VALIDATION] IF contract_type = "supply_chain" AND security_carveouts = "absent" THEN violation

[RULE-06] Diverse delivery routes MUST be used for critical system components to minimize targeting risks.
[VALIDATION] IF component_criticality = "high" AND delivery_route_diversity = FALSE THEN violation

[RULE-07] The time between purchase decisions and delivery SHALL be minimized to reduce exposure windows for adversary targeting.
[VALIDATION] IF purchase_to_delivery_time > organization_defined_threshold THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Approved Vendor List Management - Quarterly review and annual assessment of vendor security posture
- [PROC-02] Custom Configuration Risk Assessment - Security evaluation process for non-standard procurements
- [PROC-03] Supply Chain Contingency Planning - Annual plan updates and testing procedures
- [PROC-04] Diverse Delivery Route Selection - Risk-based routing decisions for critical components

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain incidents, vendor security breaches, regulatory changes, threat landscape updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Custom Configuration Procurement]
IF configuration_type = "custom"
AND business_justification = "documented"
AND cscro_approval = TRUE
AND additional_security_controls = "implemented"
THEN compliance = TRUE

[SCENARIO-02: Unapproved Vendor Usage]
IF vendor NOT IN approved_vendor_list
AND emergency_procurement = FALSE
AND security_assessment = "incomplete"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Single Delivery Route for Critical Component]
IF component_criticality = "high"
AND delivery_routes_count = 1
AND risk_assessment = "not_performed"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Extended Purchase-to-Delivery Timeline]
IF purchase_to_delivery_time > 30_days
AND component_sensitivity = "high"
AND timeline_justification = "absent"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Missing Contingency Plan Testing]
IF contingency_plan_exists = TRUE
AND last_test_date > 365_days
AND test_results = "not_documented"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls to limit harm from potential supply chain adversaries are defined | [RULE-01], [RULE-02], [RULE-03] |
| Controls are employed to limit harm from adversaries identifying and targeting supply chain | [RULE-04], [RULE-05], [RULE-06], [RULE-07] |