# POLICY: SR-3(2): Supply Chain Risk Management - Limitation of Harm

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-3-2 |
| NIST Control | SR-3(2): Supply Chain Risk Management - Limitation of Harm |
| Version | 1.0 |
| Owner | Chief Supply Chain Officer |
| Keywords | supply chain, adversary targeting, harm limitation, vendor management, procurement |

## 1. POLICY STATEMENT
The organization SHALL implement specific controls to limit harm from potential adversaries who attempt to identify and target the organizational supply chain. These controls MUST be formally defined, documented, and consistently employed across all supply chain activities to reduce the probability of successful supply chain attacks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All procurement activities | YES | Including hardware, software, services |
| Third-party vendors | YES | All tiers of suppliers |
| Custom configurations | YES | Higher risk requiring additional controls |
| Maintenance contracts | YES | Including updates and patches |
| Delivery mechanisms | YES | Physical and digital delivery routes |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Officer | • Define supply chain harm limitation controls<br>• Approve vendor selection criteria<br>• Oversee contingency planning |
| Procurement Manager | • Implement approved vendor lists<br>• Execute procurement carve-outs<br>• Coordinate diverse delivery routes |
| Security Team | • Assess supply chain threats<br>• Monitor for targeting attempts<br>• Validate security controls implementation |

## 4. RULES

[RULE-01] The organization MUST maintain a formally documented list of controls designed to limit harm from supply chain adversaries.
[VALIDATION] IF supply_chain_controls_documented = FALSE THEN violation

[RULE-02] Custom or non-standardized configurations SHALL be avoided unless justified by documented business requirements and approved by the Chief Supply Chain Officer.
[VALIDATION] IF configuration_type = "custom" AND business_justification = FALSE THEN violation

[RULE-03] All vendors MUST be selected from pre-approved vendor lists that include suppliers with established industry reputations and security track records.
[VALIDATION] IF vendor_status != "pre_approved" AND exception_documented = FALSE THEN violation

[RULE-04] Maintenance schedules, updates, and patch delivery mechanisms MUST follow pre-agreed timelines and approved delivery methods.
[VALIDATION] IF maintenance_schedule = "ad_hoc" OR delivery_method != "approved" THEN violation

[RULE-05] A supply chain contingency plan MUST be maintained and tested annually to address potential supply chain disruption events.
[VALIDATION] IF contingency_plan_exists = FALSE OR last_test_date > 365_days THEN violation

[RULE-06] Procurement contracts MUST include carve-out provisions that provide exclusions from commitments during security incidents or supply chain compromises.
[VALIDATION] IF contract_carveouts = FALSE AND contract_value > threshold THEN violation

[RULE-07] Critical deliveries MUST utilize diverse delivery routes to minimize single points of failure and targeting opportunities.
[VALIDATION] IF delivery_criticality = "high" AND delivery_routes < 2 THEN violation

[RULE-08] The time between purchase decisions and delivery MUST be minimized to reduce adversary targeting windows, with maximum timelines defined per asset category.
[VALIDATION] IF purchase_to_delivery_time > category_maximum THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Threat Assessment - Quarterly evaluation of potential adversary targeting
- [PROC-02] Vendor Reputation Verification - Annual review of approved vendor security posture
- [PROC-03] Contingency Plan Activation - Response procedures for supply chain compromise events
- [PROC-04] Delivery Route Diversification - Selection and management of multiple delivery channels

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain incidents, vendor security breaches, threat landscape changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Custom Configuration Request]
IF configuration_type = "custom"
AND business_justification = "documented"
AND cso_approval = TRUE
AND additional_controls = "implemented"
THEN compliance = TRUE

[SCENARIO-02: Unapproved Vendor Usage]
IF vendor_status = "not_pre_approved"
AND emergency_exception = FALSE
AND contract_value > $10000
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Single Delivery Route for Critical Asset]
IF asset_criticality = "high"
AND delivery_routes = 1
AND risk_acceptance = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Extended Purchase-to-Delivery Timeline]
IF asset_category = "network_equipment"
AND purchase_to_delivery_days > 30
AND delay_justification = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Outdated Contingency Plan]
IF contingency_plan_exists = TRUE
AND last_test_date > 365_days
AND last_update_date > 365_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls to limit harm from potential supply chain adversaries are defined | [RULE-01] |
| Controls are employed to limit harm from potential adversaries targeting supply chain | [RULE-02], [RULE-03], [RULE-04], [RULE-05], [RULE-06], [RULE-07], [RULE-08] |