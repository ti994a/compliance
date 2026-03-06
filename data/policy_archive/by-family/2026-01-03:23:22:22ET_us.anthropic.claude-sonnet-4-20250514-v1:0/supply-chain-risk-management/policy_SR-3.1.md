```markdown
POLICY: SR-3(1): Diverse Supply Base

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-3(1) |
| NIST Control | SR-3(1): Diverse Supply Base |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | supply chain, vendor diversity, supplier management, risk mitigation, procurement |

1. POLICY STATEMENT
The organization MUST employ a diverse set of sources for critical system components and services to reduce supply chain risk and ensure business continuity. Multiple qualified suppliers SHALL be maintained for all mission-critical components and services.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems | YES | Including cloud and on-premises |
| Critical system components | YES | Hardware, software, firmware |
| IT services | YES | Development, maintenance, support |
| Non-critical components | CONDITIONAL | Based on risk assessment |
| Legacy systems | YES | During refresh cycles |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Establish supplier diversity requirements<br>• Approve supplier qualification criteria<br>• Monitor supplier performance metrics |
| IT Asset Manager | • Maintain inventory of critical components<br>• Track supplier dependencies<br>• Coordinate supplier assessments |
| Risk Management Office | • Assess supply chain risks<br>• Define criticality criteria<br>• Monitor threat landscape |

4. RULES
[RULE-01] Critical system components MUST have at least two qualified suppliers with no single supplier providing more than 60% of total volume.
[VALIDATION] IF component_criticality = "critical" AND qualified_suppliers < 2 THEN violation
[VALIDATION] IF component_criticality = "critical" AND single_supplier_percentage > 60 THEN violation

[RULE-02] Mission-critical services MUST have at least two independent service providers with documented failover capabilities.
[VALIDATION] IF service_criticality = "mission-critical" AND service_providers < 2 THEN violation
[VALIDATION] IF service_criticality = "mission-critical" AND failover_documented = FALSE THEN violation

[RULE-03] Supplier diversity assessments MUST be conducted annually and whenever new critical suppliers are onboarded.
[VALIDATION] IF last_diversity_assessment > 365_days THEN violation
[VALIDATION] IF new_critical_supplier = TRUE AND diversity_assessment_completed = FALSE THEN violation

[RULE-04] Geographic diversity MUST be maintained with no more than 70% of critical suppliers located in the same country or region.
[VALIDATION] IF critical_suppliers_same_region_percentage > 70 THEN violation

[RULE-05] Alternative suppliers MUST be pre-qualified and contracts established within 90 days of identifying single-source dependencies.
[VALIDATION] IF single_source_dependency_identified = TRUE AND alternative_supplier_qualified = FALSE AND days_elapsed > 90 THEN violation

5. REQUIRED PROCEDURES
- [PROC-01] Supplier Diversity Assessment - Annual evaluation of supplier base diversity and risk concentration
- [PROC-02] Critical Component Identification - Process to classify and inventory mission-critical components
- [PROC-03] Alternative Supplier Qualification - Standardized process for qualifying backup suppliers
- [PROC-04] Supply Chain Risk Monitoring - Continuous monitoring of supplier performance and availability

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: Major supply chain disruption, new regulatory requirements, significant vendor consolidation

7. SCENARIO PATTERNS
[SCENARIO-01: Single Critical Supplier]
IF component_type = "critical"
AND qualified_suppliers = 1
AND alternative_supplier_qualification = "in_progress"
AND days_since_identification > 90
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Geographic Concentration Risk]
IF critical_suppliers_in_region = 8
AND total_critical_suppliers = 10
AND region_risk_level = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Service Provider Diversity]
IF service_type = "mission-critical"
AND primary_provider = "vendor_a"
AND backup_provider = "vendor_a_subsidiary"
AND independence_verified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Compliant Diverse Supply]
IF component_criticality = "critical"
AND qualified_suppliers >= 2
AND max_supplier_percentage <= 60
AND geographic_diversity = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Single Source Exception]
IF emergency_procurement = TRUE
AND single_source_justified = TRUE
AND exception_approved = TRUE
AND remediation_plan_exists = TRUE
AND remediation_timeline <= 180_days
THEN compliance = TRUE

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Diverse set of sources for system components | [RULE-01], [RULE-04] |
| Diverse set of sources for services | [RULE-02], [RULE-04] |
| Ongoing diversity management | [RULE-03], [RULE-05] |
| Risk mitigation through diversification | [RULE-01], [RULE-02], [RULE-04] |
```