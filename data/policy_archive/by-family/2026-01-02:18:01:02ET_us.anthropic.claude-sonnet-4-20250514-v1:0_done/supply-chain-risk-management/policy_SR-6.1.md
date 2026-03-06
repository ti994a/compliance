# POLICY: SR-6.1: Testing and Analysis

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-6.1 |
| NIST Control | SR-6.1: Testing and Analysis |
| Version | 1.0 |
| Owner | Supply Chain Risk Management Officer |
| Keywords | supply chain, testing, analysis, third-party, vendor assessment, SCRM |

## 1. POLICY STATEMENT
The organization MUST employ systematic analysis and testing of supply chain elements, processes, and actors associated with systems, system components, or system services. All evidence generated during supply chain analysis and testing MUST be documented and used to inform organizational risk management activities and decisions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Systems | YES | Including cloud, hybrid, and on-premises |
| System Components | YES | Hardware, software, firmware components |
| System Services | YES | Third-party and outsourced services |
| Supply Chain Vendors | YES | All tiers of suppliers and contractors |
| Internal Development | YES | In-house developed components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Management Officer | • Define supply chain analysis requirements<br>• Oversee testing programs<br>• Maintain vendor risk assessments |
| Security Architecture Team | • Conduct technical analysis of supply chain elements<br>• Perform penetration testing<br>• Document security findings |
| Procurement Team | • Ensure vendor compliance with testing requirements<br>• Validate supplier security documentation<br>• Maintain approved vendor lists |

## 4. RULES
[RULE-01] Organizations MUST define and maintain a comprehensive list of supply chain elements, processes, and actors subject to analysis and testing for each system.
[VALIDATION] IF system_deployed = TRUE AND supply_chain_inventory = NULL THEN violation

[RULE-02] Supply chain analysis MUST be conducted using organizational analysis, independent third-party analysis, or a combination of both methods.
[VALIDATION] IF vendor_risk_level = "HIGH" AND analysis_method != "third_party" THEN violation

[RULE-03] Penetration testing of critical supply chain elements MUST be performed annually and after significant changes.
[VALIDATION] IF element_criticality = "HIGH" AND last_pentest_date > 365_days THEN violation

[RULE-04] All supply chain analysis and testing evidence MUST be documented and retained for a minimum of three years.
[VALIDATION] IF analysis_conducted = TRUE AND documentation_complete = FALSE THEN violation

[RULE-05] Supply chain risk findings MUST be integrated into organizational risk management decisions within 30 days of discovery.
[VALIDATION] IF finding_severity = "HIGH" AND integration_date > discovery_date + 30_days THEN violation

[RULE-06] Third-party suppliers providing critical components MUST undergo security assessment before contract execution and annually thereafter.
[VALIDATION] IF supplier_criticality = "HIGH" AND assessment_status = "EXPIRED" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Element Identification - Systematic process for cataloging all supply chain components
- [PROC-02] Vendor Security Assessment - Standardized evaluation of supplier security controls
- [PROC-03] Third-Party Analysis Coordination - Management of external security assessments
- [PROC-04] Supply Chain Testing Documentation - Evidence collection and retention procedures
- [PROC-05] Risk Integration Process - Incorporation of findings into risk management decisions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: Major supply chain incidents, regulatory changes, significant vendor changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Vendor Assessment]
IF vendor_criticality = "HIGH"
AND contract_value > $1M
AND security_assessment_age > 12_months
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Supply Chain Documentation]
IF system_criticality = "HIGH"
AND supply_chain_analysis_conducted = TRUE
AND documentation_retained < 3_years
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Penetration Testing Compliance]
IF supply_chain_element = "CRITICAL"
AND last_pentest_date > 365_days
AND change_significance = "MAJOR"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Third-Party Analysis Requirement]
IF vendor_risk_level = "HIGH"
AND analysis_method = "internal_only"
AND regulatory_requirement = "FedRAMP"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Risk Integration Timeliness]
IF finding_severity = "CRITICAL"
AND days_since_discovery > 30
AND risk_mgmt_integration = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Organizational analysis employed on supply chain elements | RULE-01, RULE-02 |
| Testing of supply chain processes and actors | RULE-03, RULE-06 |
| Documentation of analysis evidence | RULE-04 |
| Integration with risk management activities | RULE-05 |