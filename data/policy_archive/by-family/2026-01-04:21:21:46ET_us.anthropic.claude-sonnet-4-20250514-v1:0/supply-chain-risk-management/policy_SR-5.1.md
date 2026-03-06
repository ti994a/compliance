# POLICY: SR-5.1: Adequate Supply

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-5.1 |
| NIST Control | SR-5.1: Adequate Supply |
| Version | 1.0 |
| Owner | Chief Supply Chain Officer |
| Keywords | supply chain, critical components, supplier diversity, stockpiling, contingency |

## 1. POLICY STATEMENT
The organization must define and employ controls to ensure an adequate supply of critical system components necessary for continued operations. This includes establishing supplier diversity, maintaining strategic stockpiles, and identifying alternative components to mitigate supply chain disruptions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical system components | YES | As defined in asset inventory |
| Non-critical components | NO | Standard procurement applies |
| Cloud services | CONDITIONAL | If deemed critical to operations |
| Third-party suppliers | YES | All suppliers of critical components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Officer | • Define critical component requirements<br>• Approve supplier diversity strategies<br>• Oversee stockpile management |
| IT Asset Manager | • Maintain critical component inventory<br>• Monitor component failure rates<br>• Coordinate with procurement |
| Procurement Manager | • Execute multi-supplier strategies<br>• Manage supplier relationships<br>• Maintain emergency procurement procedures |

## 4. RULES
[RULE-01] Critical system components requiring adequate supply assurance MUST be formally defined and documented in the organizational asset inventory.
[VALIDATION] IF component_criticality = "critical" AND adequate_supply_required = TRUE AND documented_in_inventory = FALSE THEN violation

[RULE-02] Organizations MUST employ at least two independent suppliers for each critical system component to ensure supply chain resilience.
[VALIDATION] IF component_criticality = "critical" AND supplier_count < 2 AND exception_approved = FALSE THEN violation

[RULE-03] Strategic stockpiles of critical components MUST be maintained at levels sufficient to support operations for a minimum of 30 days during supply disruptions.
[VALIDATION] IF stockpile_days < 30 AND component_criticality = "critical" AND alternative_source = FALSE THEN violation

[RULE-04] Functionally identical or similar alternative components MUST be identified and tested for compatibility with critical systems.
[VALIDATION] IF component_criticality = "critical" AND alternative_identified = FALSE AND compatibility_tested = FALSE THEN violation

[RULE-05] Mean time to failure (MTTF) data MUST be tracked for all critical components to inform supply planning decisions.
[VALIDATION] IF component_criticality = "critical" AND mttf_tracked = FALSE THEN violation

[RULE-06] Supply adequacy assessments MUST be conducted quarterly and after any significant supply chain disruption event.
[VALIDATION] IF last_assessment_date > 90_days AND disruption_event_occurred = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Component Identification - Process for defining and classifying components requiring supply assurance
- [PROC-02] Supplier Diversity Management - Procedures for maintaining multiple qualified suppliers
- [PROC-03] Strategic Stockpile Management - Inventory management and rotation procedures
- [PROC-04] Alternative Component Qualification - Testing and approval process for substitute components
- [PROC-05] Supply Chain Disruption Response - Emergency procurement and component allocation procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major supply chain disruptions, critical component changes, supplier consolidation events

## 7. SCENARIO PATTERNS
[SCENARIO-01: Single Supplier Dependency]
IF component_criticality = "critical"
AND supplier_count = 1
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Insufficient Stockpile]
IF component_criticality = "critical"
AND stockpile_days < 30
AND supply_disruption_risk = "high"
AND alternative_source = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Untested Alternative Components]
IF component_criticality = "critical"
AND alternative_identified = TRUE
AND compatibility_tested = FALSE
AND deployment_planned = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing MTTF Data]
IF component_criticality = "critical"
AND mttf_tracked = FALSE
AND component_age > 12_months
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Overdue Supply Assessment]
IF last_assessment_date > 90_days
AND supply_chain_changes = TRUE
AND critical_components_affected = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Critical system components requiring adequate supply are defined | [RULE-01] |
| Controls to ensure adequate supply are employed | [RULE-02], [RULE-03], [RULE-04] |
| Supply chain resilience through supplier diversity | [RULE-02] |
| Strategic stockpiling of critical components | [RULE-03] |
| Alternative component identification and testing | [RULE-04] |
| Component reliability tracking | [RULE-05] |
| Regular supply adequacy assessment | [RULE-06] |