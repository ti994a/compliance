```markdown
# POLICY: SR-5.1: Adequate Supply

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-5.1 |
| NIST Control | SR-5.1: Adequate Supply |
| Version | 1.0 |
| Owner | Chief Supply Chain Officer |
| Keywords | supply chain, critical components, stockpiling, multiple suppliers, component availability |

## 1. POLICY STATEMENT
The organization SHALL define and employ controls to ensure adequate supply of critical system components to prevent disruption of operations. These controls include diversifying suppliers, maintaining strategic stockpiles, and identifying alternative components.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical System Components | YES | Components whose failure impacts mission-critical operations |
| Non-Critical Components | NO | Standard replacement timeline acceptable |
| Third-Party Suppliers | YES | All suppliers of critical components |
| Internal IT Systems | YES | Systems supporting critical business functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Officer | • Define critical component inventory<br>• Establish supplier diversity requirements<br>• Approve stockpile levels |
| IT Asset Manager | • Maintain component inventory tracking<br>• Monitor mean time to failure metrics<br>• Execute stockpile management |
| Procurement Manager | • Implement multi-supplier strategies<br>• Negotiate supply agreements<br>• Validate supplier capabilities |

## 4. RULES
[RULE-01] Critical system components MUST be identified and documented based on their impact to mission-critical operations and mean time to failure analysis.
[VALIDATION] IF component_criticality = "undefined" AND system_criticality = "high" THEN violation

[RULE-02] Organizations MUST employ at least two qualified suppliers for each critical system component to ensure supply chain resilience.
[VALIDATION] IF critical_component_suppliers < 2 AND no_documented_exception THEN violation

[RULE-03] Strategic stockpiles MUST be maintained for critical components with lead times exceeding 30 days or single-source dependencies.
[VALIDATION] IF component_lead_time > 30_days AND stockpile_quantity = 0 THEN violation

[RULE-04] Functionally identical or similar alternative components MUST be identified and validated for each critical component.
[VALIDATION] IF critical_component_alternatives = "none" AND component_type != "proprietary_unique" THEN violation

[RULE-05] Supply adequacy assessments MUST be conducted quarterly and after any supply chain disruption event.
[VALIDATION] IF last_supply_assessment > 90_days OR supply_disruption_event = TRUE AND assessment_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Component Identification - Process to assess and classify component criticality
- [PROC-02] Supplier Diversification - Methodology for qualifying and managing multiple suppliers
- [PROC-03] Stockpile Management - Procedures for determining, maintaining, and rotating stockpile inventory
- [PROC-04] Alternative Component Validation - Process to identify and test functionally equivalent components

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain disruptions, critical system changes, supplier failures, major acquisitions

## 7. SCENARIO PATTERNS
[SCENARIO-01: Single Supplier Dependency]
IF component_criticality = "high"
AND supplier_count = 1
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate Stockpile]
IF component_lead_time = 45_days
AND current_stockpile = 0
AND alternative_component = "none"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Undocumented Critical Components]
IF system_criticality = "mission_critical"
AND component_criticality_assessment = "not_performed"
AND system_age > 90_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Outdated Supply Assessment]
IF last_supply_assessment > 90_days
AND no_supply_disruptions = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Post-Disruption Response]
IF supply_disruption_occurred = TRUE
AND disruption_date < 30_days_ago
AND reassessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Critical system components are defined | [RULE-01] |
| Controls to ensure adequate supply are defined | [RULE-02], [RULE-03], [RULE-04] |
| Controls are employed to ensure adequate supply | [RULE-05] |
```