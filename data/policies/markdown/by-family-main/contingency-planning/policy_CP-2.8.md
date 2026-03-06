```markdown
# POLICY: CP-2.8: Identify Critical Assets

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-2.8 |
| NIST Control | CP-2.8: Identify Critical Assets |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | critical assets, contingency planning, business continuity, mission functions, asset identification |

## 1. POLICY STATEMENT
The organization MUST identify and maintain an inventory of critical system assets that support all mission and business functions to enable prioritized protection and continuity planning. Critical assets include both technical components and operational aspects necessary for organizational operations during normal and contingency scenarios.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, on-premises, and hybrid environments |
| External Service Providers | YES | When hosting or supporting critical assets |
| Business Units | YES | Must identify mission-critical functions |
| Contractors | YES | When managing critical system components |
| Development/Test Systems | CONDITIONAL | Only if supporting production critical functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Business Continuity Manager | • Lead critical asset identification process<br>• Coordinate with business units for function mapping<br>• Maintain critical asset inventory |
| System Owners | • Identify technical components within their systems<br>• Validate criticality assessments<br>• Report changes to critical assets |
| CISO | • Approve critical asset classifications<br>• Ensure adequate protection controls<br>• Review criticality determinations |

## 4. RULES
[RULE-01] Organizations MUST identify critical system assets supporting all mission and business functions through formal criticality analysis, business continuity planning, or business impact analysis.
[VALIDATION] IF critical_asset_identification_process = "none" OR methodology_documented = FALSE THEN violation

[RULE-02] Critical asset identification MUST include both technical aspects (system components, IT services, IT products, mechanisms) and operational aspects (procedures, personnel).
[VALIDATION] IF technical_assets_identified = TRUE AND operational_assets_identified = FALSE THEN violation

[RULE-03] Critical asset inventory MUST be reviewed and updated at least annually or when significant changes occur to mission/business functions.
[VALIDATION] IF last_review_date > 365_days OR significant_changes_pending = TRUE AND inventory_updated = FALSE THEN violation

[RULE-04] Organizations MUST prioritize resources and implement additional controls for identified critical assets beyond standard baseline controls.
[VALIDATION] IF critical_asset_identified = TRUE AND additional_controls_implemented = FALSE THEN violation

[RULE-05] When critical assets are supported by external service providers, organizations MUST implement CP-2(7) coordinate with external service providers control enhancement.
[VALIDATION] IF critical_assets_external = TRUE AND cp_2_7_implemented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Asset Identification - Systematic process for identifying and categorizing critical assets
- [PROC-02] Business Impact Analysis - Assessment methodology for determining asset criticality
- [PROC-03] Critical Asset Inventory Management - Procedures for maintaining and updating asset records
- [PROC-04] Criticality Review Process - Regular assessment and validation of asset criticality determinations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, business reorganization, new mission functions, significant security incidents affecting critical assets

## 7. SCENARIO PATTERNS
[SCENARIO-01: Complete Critical Asset Identification]
IF business_impact_analysis_conducted = TRUE
AND technical_assets_identified = TRUE
AND operational_assets_identified = TRUE
AND inventory_maintained = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Operational Aspects]
IF technical_assets_identified = TRUE
AND operational_assets_identified = FALSE
AND critical_procedures_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated Critical Asset Inventory]
IF last_inventory_update > 365_days
AND business_functions_changed = TRUE
AND new_critical_systems_deployed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: External Provider Critical Assets]
IF critical_assets_external = TRUE
AND service_provider_coordination = FALSE
AND cp_2_7_implemented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Inadequate Protection for Critical Assets]
IF critical_asset_identified = TRUE
AND baseline_controls_only = TRUE
AND additional_controls_implemented = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Critical system assets supporting all mission and business functions are identified | [RULE-01], [RULE-02] |
| Technical aspects of critical assets are identified | [RULE-02] |
| Operational aspects of critical assets are identified | [RULE-02] |
| Critical asset inventory is maintained current | [RULE-03] |
| Additional controls implemented for critical assets | [RULE-04] |
| External service provider coordination for critical assets | [RULE-05] |
```