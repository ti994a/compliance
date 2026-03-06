# POLICY: PM-30: Supply Chain Risk Management Strategy

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-30 |
| NIST Control | PM-30: Supply Chain Risk Management Strategy |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | supply chain, risk management, acquisition, vendor management, third-party risk |

## 1. POLICY STATEMENT
The organization SHALL develop, implement, and maintain an organization-wide supply chain risk management strategy that addresses security and privacy risks throughout the system lifecycle. This strategy MUST be consistently applied across all organizational units and regularly reviewed to ensure effectiveness and alignment with organizational changes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Systems | YES | Including cloud, on-premises, and hybrid |
| System Components | YES | Hardware, software, firmware |
| System Services | YES | Managed services, SaaS, consulting |
| All Business Units | YES | Must implement consistently |
| Contractors/Vendors | YES | Subject to supply chain requirements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Develop organization-wide supply chain risk strategy<br>• Ensure consistent implementation across organization<br>• Coordinate with business units on strategy execution |
| Procurement Team | • Implement supply chain risk controls in acquisition processes<br>• Conduct vendor risk assessments<br>• Maintain approved vendor lists |
| System Owners | • Develop system-level supply chain risk management plans<br>• Ensure compliance with organizational strategy<br>• Report supply chain incidents |

## 4. RULES
[RULE-01] The organization MUST develop a comprehensive supply chain risk management strategy that addresses development, acquisition, maintenance, and disposal phases for all systems, components, and services.
[VALIDATION] IF strategy_exists = FALSE OR lifecycle_phases_covered < 4 THEN violation

[RULE-02] The supply chain risk management strategy MUST include explicit risk appetite, tolerance levels, acceptable mitigation strategies, evaluation processes, and defined roles and responsibilities.
[VALIDATION] IF strategy_components_complete < 5 THEN violation

[RULE-03] The supply chain risk management strategy MUST be implemented consistently across all organizational units and business functions.
[VALIDATION] IF business_units_implementing / total_business_units < 1.0 THEN violation

[RULE-04] The supply chain risk management strategy MUST be reviewed and updated at least annually or when significant organizational changes occur.
[VALIDATION] IF last_review_date > 365_days_ago THEN violation

[RULE-05] All system-level supply chain risk management plans MUST align with and implement the organization-wide strategy.
[VALIDATION] IF system_plan_alignment = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment - Standardized process for evaluating vendor and component risks
- [PROC-02] Vendor Onboarding and Management - Due diligence and ongoing monitoring procedures
- [PROC-03] Supply Chain Incident Response - Process for addressing supply chain security events
- [PROC-04] Strategy Review and Update - Annual review and change management process

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major organizational restructuring, significant supply chain incidents, regulatory changes, merger/acquisition activities

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Strategy Components]
IF strategy_document_exists = TRUE
AND risk_appetite_defined = FALSE
AND mitigation_controls_defined = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inconsistent Implementation]
IF strategy_approved = TRUE
AND business_unit_A_implementing = TRUE
AND business_unit_B_implementing = FALSE
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated Strategy]
IF strategy_last_updated > 18_months_ago
AND organizational_changes_occurred = TRUE
AND no_review_conducted = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: System Plan Misalignment]
IF organization_strategy_exists = TRUE
AND system_scrm_plan_exists = TRUE
AND plan_references_org_strategy = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Complete Compliance]
IF strategy_comprehensive = TRUE
AND all_units_implementing = TRUE
AND annual_review_current = TRUE
AND system_plans_aligned = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Organization-wide strategy developed | RULE-01 |
| Strategy addresses development risks | RULE-01 |
| Strategy addresses acquisition risks | RULE-01 |
| Strategy addresses maintenance risks | RULE-01 |
| Strategy addresses disposal risks | RULE-01 |
| Strategy addresses system components | RULE-01 |
| Strategy addresses system services | RULE-01 |
| Strategy implemented consistently | RULE-03 |
| Strategy reviewed and updated regularly | RULE-04 |