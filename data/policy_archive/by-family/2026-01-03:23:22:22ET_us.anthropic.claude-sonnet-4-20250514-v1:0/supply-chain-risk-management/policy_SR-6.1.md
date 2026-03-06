```markdown
POLICY: SR-6.1: Testing and Analysis

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-6.1 |
| NIST Control | SR-6.1: Testing and Analysis |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, testing, analysis, SCRM, third-party, penetration testing |

## 1. POLICY STATEMENT
The organization MUST employ comprehensive analysis and testing of supply chain elements, processes, and actors associated with systems, system components, and system services. All evidence generated during testing and analysis SHALL be documented and used to inform organizational risk management activities and decisions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including development, test, and production |
| System components | YES | Hardware, software, firmware from external sources |
| System services | YES | Cloud services, managed services, SaaS |
| Supply chain vendors | YES | Primary and sub-tier suppliers |
| Internal development | CONDITIONAL | When using third-party components or tools |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve supply chain testing strategy<br>• Review critical findings<br>• Authorize risk acceptance decisions |
| Supply Chain Risk Manager | • Define testing requirements for vendors<br>• Coordinate analysis activities<br>• Maintain testing documentation<br>• Report findings to leadership |
| Procurement Manager | • Include testing requirements in contracts<br>• Verify vendor compliance with testing obligations<br>• Escalate non-compliance issues |

## 4. RULES
[RULE-01] Organizations MUST define and document specific supply chain elements, processes, and actors subject to analysis and testing before system deployment.
[VALIDATION] IF system_deployment = TRUE AND supply_chain_elements_defined = FALSE THEN violation

[RULE-02] Supply chain analysis MUST include organizational analysis, and MAY include independent third-party analysis based on risk assessment.
[VALIDATION] IF high_risk_supplier = TRUE AND third_party_analysis = FALSE AND risk_acceptance_documented = FALSE THEN violation

[RULE-03] Penetration testing of supply chain elements SHALL be conducted for critical systems and high-risk suppliers at least annually.
[VALIDATION] IF system_criticality = "high" AND last_penetration_test > 365_days THEN violation

[RULE-04] All testing and analysis evidence MUST be documented within 30 days of completion and integrated into risk management decisions.
[VALIDATION] IF testing_completed = TRUE AND documentation_date > testing_date + 30_days THEN violation

[RULE-05] Supply chain testing requirements MUST be included in all vendor contracts and service agreements for systems handling sensitive data.
[VALIDATION] IF contract_signed = TRUE AND data_sensitivity = "high" AND testing_requirements_included = FALSE THEN violation

[RULE-06] Testing scope MUST cover development processes, delivery mechanisms, configuration management, and operational procedures of critical suppliers.
[VALIDATION] IF supplier_criticality = "high" AND testing_scope_complete = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Element Identification - Process for cataloging and classifying supply chain components requiring testing
- [PROC-02] Risk-Based Testing Selection - Methodology for determining appropriate testing methods based on risk assessment
- [PROC-03] Third-Party Testing Coordination - Process for engaging and managing independent testing providers
- [PROC-04] Evidence Collection and Analysis - Standardized approach for documenting and analyzing testing results
- [PROC-05] Risk Management Integration - Process for incorporating findings into organizational risk decisions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after major supply chain incidents
- Triggering events: New high-risk suppliers, supply chain security incidents, regulatory changes, failed testing results

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical System Deployment]
IF system_criticality = "high"
AND supply_chain_elements_defined = TRUE
AND organizational_analysis_completed = TRUE
AND penetration_testing_completed = TRUE
THEN compliance = TRUE

[SCENARIO-02: High-Risk Supplier Without Third-Party Analysis]
IF supplier_risk_rating = "high"
AND organizational_analysis_only = TRUE
AND third_party_analysis = FALSE
AND risk_acceptance_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Testing Evidence]
IF last_supply_chain_test > 365_days
AND system_criticality = "high"
AND no_compensating_controls = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Undocumented Testing Results]
IF testing_completed = TRUE
AND documentation_status = "incomplete"
AND days_since_testing > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Contract Missing Testing Requirements]
IF new_vendor_contract = TRUE
AND data_classification = "confidential"
AND supply_chain_testing_clause = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Organizational analysis employed on defined supply chain elements | [RULE-01], [RULE-02] |
| Testing covers supply chain processes and actors | [RULE-06] |
| Evidence documented and used for risk management | [RULE-04] |
| Analysis appropriate for system criticality | [RULE-03], [RULE-05] |
```