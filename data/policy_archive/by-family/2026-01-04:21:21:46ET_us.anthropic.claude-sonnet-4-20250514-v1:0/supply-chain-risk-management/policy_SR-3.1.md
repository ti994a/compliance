```markdown
# POLICY: SR-3.1: Diverse Supply Base

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-3.1 |
| NIST Control | SR-3.1: Diverse Supply Base |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | supply chain, vendor diversity, supplier risk, component sourcing, service providers |

## 1. POLICY STATEMENT
The organization MUST employ a diverse set of sources for critical system components and services to reduce supply chain risk and ensure continuity of operations. Supplier diversity requirements apply to all technology acquisitions supporting business-critical systems and regulatory compliance environments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical system components | YES | Hardware, software, firmware components |
| Business-critical services | YES | Cloud services, managed services, SaaS |
| Development services | YES | Software development, system integration |
| Non-critical commodity items | NO | Standard office supplies, non-IT equipment |
| Emergency procurements | CONDITIONAL | Subject to post-procurement review |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Establish supplier diversity requirements<br>• Approve supplier qualification criteria<br>• Monitor compliance with diversity mandates |
| IT Asset Manager | • Maintain inventory of critical components<br>• Identify single-source dependencies<br>• Track supplier performance metrics |
| Risk Management Team | • Assess supply chain concentration risks<br>• Review supplier geographic distribution<br>• Evaluate alternative sourcing options |

## 4. RULES
[RULE-01] Critical system components MUST have at least two qualified suppliers from different geographic regions or corporate entities.
[VALIDATION] IF component_criticality = "critical" AND qualified_suppliers < 2 THEN violation

[RULE-02] No single supplier SHALL provide more than 60% of components within any critical system category.
[VALIDATION] IF supplier_market_share > 60% AND system_category = "critical" THEN violation

[RULE-03] Service providers for business-critical functions MUST be diversified across at least two vendors with different operational models or geographic footprints.
[VALIDATION] IF service_criticality = "business_critical" AND unique_providers < 2 THEN violation

[RULE-04] Supplier qualification assessments MUST evaluate geographic diversity, financial stability, and alternative sourcing capabilities.
[VALIDATION] IF supplier_assessment_complete = FALSE AND procurement_value > threshold THEN violation

[RULE-05] Single-source dependencies MUST be documented with risk mitigation plans and executive approval for components exceeding $100K annually.
[VALIDATION] IF single_source = TRUE AND annual_spend > 100000 AND executive_approval = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supplier Diversity Assessment - Evaluate and document supplier diversity for critical procurements
- [PROC-02] Alternative Source Identification - Identify and qualify backup suppliers for critical components
- [PROC-03] Supply Chain Risk Monitoring - Quarterly review of supplier concentration and geographic risks
- [PROC-04] Emergency Procurement Review - Post-event assessment of emergency single-source procurements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major supplier consolidation, supply chain disruption, regulatory changes, critical system changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Component Single Source]
IF component_type = "critical"
AND qualified_suppliers = 1
AND risk_mitigation_plan = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Service Provider Concentration]
IF service_category = "business_critical"
AND primary_provider_percentage > 80%
AND backup_provider_qualified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Geographic Supplier Diversity]
IF supplier_count >= 2
AND all_suppliers_same_country = TRUE
AND geopolitical_risk_rating = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Emergency Procurement Exception]
IF procurement_type = "emergency"
AND single_source = TRUE
AND post_procurement_review_completed = TRUE
AND alternative_sourcing_plan_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Cloud Service Provider Diversity]
IF cloud_service_criticality = "high"
AND active_cloud_providers >= 2
AND providers_different_regions = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Diverse sources employed for system components | [RULE-01], [RULE-02] |
| Diverse sources employed for services | [RULE-03] |
| Supplier qualification and assessment | [RULE-04] |
| Single-source risk management | [RULE-05] |
```