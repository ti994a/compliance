# POLICY: SR-3.1: Diverse Supply Base

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-3.1 |
| NIST Control | SR-3.1: Diverse Supply Base |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | supply chain, diversity, suppliers, components, services, risk management |

## 1. POLICY STATEMENT
The organization SHALL employ a diverse set of sources for critical system components and services to reduce supply chain risk and ensure continuity of operations. Supply diversity requirements apply to all technology acquisitions supporting business-critical functions and regulated systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical system components | YES | Hardware, software, firmware components |
| Essential services | YES | Cloud services, managed services, support services |
| Non-critical purchases | CONDITIONAL | If part of critical system supply chain |
| Emergency procurements | YES | Must follow expedited diversity assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Establish supplier diversity requirements<br>• Approve supplier diversity strategies<br>• Monitor compliance with diversity targets |
| IT Asset Manager | • Maintain inventory of critical components<br>• Track supplier dependencies<br>• Coordinate replacement sourcing |
| Supply Chain Risk Manager | • Assess supplier concentration risks<br>• Develop contingency sourcing plans<br>• Monitor supply chain threat intelligence |

## 4. RULES
[RULE-01] Critical system components MUST be sourced from at least two independent suppliers when feasible, with no single supplier providing more than 70% of any component category.
[VALIDATION] IF component_category_single_supplier_percentage > 70 THEN violation

[RULE-02] Essential services MUST maintain alternate suppliers or service providers identified and pre-qualified within 90 days of primary service establishment.
[VALIDATION] IF essential_service = TRUE AND alternate_supplier_identified = FALSE AND days_since_establishment > 90 THEN violation

[RULE-03] Supplier diversity assessments MUST be conducted annually for all critical suppliers and whenever new critical suppliers are onboarded.
[VALIDATION] IF supplier_type = "critical" AND days_since_last_diversity_assessment > 365 THEN violation

[RULE-04] Geographic diversity MUST be maintained with critical suppliers distributed across at least two different geographic regions when possible.
[VALIDATION] IF critical_suppliers_geographic_regions < 2 AND feasible = TRUE THEN violation

[RULE-05] Supply chain concentration risk reports MUST be generated quarterly and reviewed by the Supply Chain Risk Manager.
[VALIDATION] IF days_since_last_concentration_report > 90 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supplier Diversity Assessment - Evaluate supplier concentration and identify diversification opportunities
- [PROC-02] Critical Component Inventory Management - Maintain current inventory of critical components and their suppliers
- [PROC-03] Alternate Supplier Qualification - Pre-qualify backup suppliers for critical components and services
- [PROC-04] Supply Chain Risk Monitoring - Continuously monitor supplier dependencies and concentration risks

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supplier changes, supply chain disruptions, new critical system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Single Supplier Dependency]
IF component_type = "critical"
AND supplier_count = 1
AND alternate_supplier_identified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Geographic Concentration Risk]
IF critical_suppliers_same_region = TRUE
AND supplier_count >= 2
AND geographic_diversification_feasible = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Service Provider Backup Missing]
IF service_type = "essential"
AND days_operational > 90
AND backup_provider_qualified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Supplier Concentration Threshold Exceeded]
IF component_category = "network_hardware"
AND single_supplier_percentage > 70
AND diversification_attempted = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compliant Diverse Sourcing]
IF critical_component = TRUE
AND supplier_count >= 2
AND max_supplier_percentage <= 70
AND geographic_diversity = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Diverse set of sources employed for system components | [RULE-01], [RULE-04] |
| Diverse set of sources employed for services | [RULE-02], [RULE-04] |
| Supply chain diversity monitoring and assessment | [RULE-03], [RULE-05] |