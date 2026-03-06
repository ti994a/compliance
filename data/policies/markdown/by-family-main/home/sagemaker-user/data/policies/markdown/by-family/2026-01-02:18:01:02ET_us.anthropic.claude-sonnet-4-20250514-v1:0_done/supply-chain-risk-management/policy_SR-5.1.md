# POLICY: SR-5.1: Adequate Supply

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-5.1 |
| NIST Control | SR-5.1: Adequate Supply |
| Version | 1.0 |
| Owner | Chief Supply Chain Risk Officer |
| Keywords | supply chain, critical components, supplier diversity, stockpiling, business continuity |

## 1. POLICY STATEMENT
The organization must define and employ controls to ensure adequate supply of critical system components to maintain operational continuity. This includes identifying critical components, establishing supplier diversity, maintaining strategic stockpiles, and identifying alternative components to mitigate supply chain disruptions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical System Components | YES | As defined in organizational inventory |
| Non-Critical Components | CONDITIONAL | If supporting critical functions |
| Third-Party Suppliers | YES | Primary and backup suppliers |
| Cloud Service Providers | YES | For critical infrastructure services |
| Legacy Systems | YES | If business-critical |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define critical component inventory<br>• Establish supplier diversity requirements<br>• Monitor supply chain health metrics |
| Procurement Manager | • Implement multi-supplier strategies<br>• Maintain supplier performance records<br>• Execute emergency procurement procedures |
| System Owners | • Identify critical components for their systems<br>• Report supply-related risks<br>• Validate component alternatives |

## 4. RULES
[RULE-01] Organizations MUST maintain a documented inventory of critical system components that require adequate supply assurance.
[VALIDATION] IF critical_component_inventory = NULL OR last_updated > 12_months THEN violation

[RULE-02] For each critical component, organizations MUST establish relationships with at least two qualified suppliers to prevent single points of failure.
[VALIDATION] IF critical_component.supplier_count < 2 AND waiver_approved = FALSE THEN violation

[RULE-03] Organizations MUST maintain strategic stockpiles of critical components based on mean time to failure analysis and lead time requirements.
[VALIDATION] IF component.stock_level < (MTTF_days + lead_time_days) * usage_rate AND justification_documented = FALSE THEN violation

[RULE-04] Organizations MUST identify and validate functionally identical or similar alternative components for each critical component.
[VALIDATION] IF critical_component.alternatives_count = 0 AND single_source_approved = FALSE THEN violation

[RULE-05] Supply adequacy assessments MUST be conducted annually and after any significant supply chain disruption event.
[VALIDATION] IF last_supply_assessment > 365_days OR (disruption_event_occurred = TRUE AND post_event_assessment = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Component Identification - Process for identifying and classifying components requiring supply assurance
- [PROC-02] Supplier Qualification and Diversity - Procedures for vetting and maintaining multiple suppliers
- [PROC-03] Strategic Stockpile Management - Inventory management and refresh procedures for stockpiled components
- [PROC-04] Alternative Component Validation - Testing and approval process for component substitutes
- [PROC-05] Supply Chain Disruption Response - Emergency procurement and component allocation procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Supply chain disruptions, critical system changes, supplier failures, geopolitical events

## 7. SCENARIO PATTERNS
[SCENARIO-01: Single Supplier Dependency]
IF critical_component.supplier_count = 1
AND waiver_documentation = FALSE
AND component_criticality = "HIGH"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate Stockpile]
IF component.current_stock < minimum_required_stock
AND lead_time > 30_days
AND no_alternative_suppliers = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated Supply Assessment]
IF last_supply_adequacy_assessment > 365_days
AND critical_system_changes_occurred = TRUE
AND supply_risk_level = "HIGH"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Approved Alternative Components]
IF critical_component.alternatives_identified = TRUE
AND alternatives_tested = TRUE
AND alternatives_approved = TRUE
THEN compliance = TRUE

[SCENARIO-05: Supply Chain Disruption Response]
IF supply_disruption_detected = TRUE
AND response_time < 24_hours
AND alternative_suppliers_activated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Critical system components requiring adequate supply are defined | [RULE-01] |
| Controls to ensure adequate supply are defined and employed | [RULE-02], [RULE-03], [RULE-04] |
| Supply adequacy monitoring and assessment | [RULE-05] |