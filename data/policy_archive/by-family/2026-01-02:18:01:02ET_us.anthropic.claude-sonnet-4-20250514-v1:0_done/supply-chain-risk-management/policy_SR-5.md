# POLICY: SR-5: Acquisition Strategies, Tools, and Methods

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-5 |
| NIST Control | SR-5: Acquisition Strategies, Tools, and Methods |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | supply chain, acquisition, procurement, vendor risk, contract tools, supply chain risk assessment |

## 1. POLICY STATEMENT
The organization must employ defined acquisition strategies, contract tools, and procurement methods to protect against, identify, and mitigate supply chain risks throughout the procurement lifecycle. All acquisitions of systems, components, and services must incorporate supply chain risk management controls based on risk assessment results.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| IT Systems | YES | All production and development systems |
| System Components | YES | Hardware, software, firmware components |
| Third-party Services | YES | Cloud services, managed services, SaaS |
| Development Tools | YES | Software development and testing tools |
| Non-IT Procurement | CONDITIONAL | Only if supporting IT operations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Define acquisition strategies and contract tools<br>• Approve high-risk vendor engagements<br>• Ensure policy compliance across procurement |
| Supply Chain Risk Manager | • Conduct supply chain risk assessments<br>• Maintain approved vendor lists<br>• Monitor vendor security posture |
| Procurement Teams | • Implement defined acquisition strategies<br>• Execute contract tools and methods<br>• Document procurement decisions |

## 4. RULES
[RULE-01] Organizations MUST define and document acquisition strategies, contract tools, and procurement methods specifically designed to protect against, identify, and mitigate supply chain risks.
[VALIDATION] IF acquisition_strategy_documented = FALSE OR contract_tools_defined = FALSE THEN violation

[RULE-02] All procurement activities MUST employ the defined acquisition strategies and contract tools appropriate to the assessed supply chain risk level.
[VALIDATION] IF procurement_activity = TRUE AND risk_appropriate_controls = FALSE THEN violation

[RULE-03] High-risk acquisitions MUST utilize enhanced protection methods including blind buys, tamper-evident packaging, or controlled distribution channels.
[VALIDATION] IF risk_level = "HIGH" AND enhanced_protection_methods = FALSE THEN violation

[RULE-04] Contract language MUST include provisions prohibiting tainted or counterfeit components and requiring supplier transparency into security practices.
[VALIDATION] IF contract_security_provisions = FALSE OR counterfeit_prohibition = FALSE THEN violation

[RULE-05] Procurement personnel MUST complete supply chain risk training before engaging in acquisition activities and annually thereafter.
[VALIDATION] IF personnel_training_current = FALSE AND procurement_authority = TRUE THEN violation

[RULE-06] Supply chain risk assessments MUST be conducted and documented before selecting acquisition strategies for medium and high-risk procurements.
[VALIDATION] IF risk_level IN ["MEDIUM", "HIGH"] AND risk_assessment_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment - Evaluate and document risks before procurement
- [PROC-02] Acquisition Strategy Selection - Choose appropriate strategies based on risk level
- [PROC-03] Contract Tool Implementation - Apply security provisions and monitoring requirements
- [PROC-04] Vendor Security Evaluation - Assess supplier security practices and controls
- [PROC-05] Procurement Training Program - Educate personnel on supply chain risks and mitigation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: Major supply chain incidents, regulatory changes, significant vendor security breaches

## 7. SCENARIO PATTERNS
[SCENARIO-01: High-Risk Hardware Procurement]
IF component_type = "critical_hardware"
AND risk_assessment_score >= 7
AND enhanced_protection_methods = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Cloud Service Contract Missing Security Provisions]
IF service_type = "cloud_service"
AND contract_security_provisions = FALSE
AND data_sensitivity = "confidential"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Untrained Procurement Personnel]
IF personnel_role = "procurement_officer"
AND supply_chain_training_date < (current_date - 365_days)
AND active_procurement_authority = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Medium-Risk Acquisition Without Assessment]
IF procurement_value > $100000
AND risk_level = "MEDIUM"
AND supply_chain_risk_assessment = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Low-Risk Procurement]
IF risk_level = "LOW"
AND standard_contract_tools_applied = TRUE
AND procurement_documentation_complete = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Acquisition strategies defined | RULE-01 |
| Contract tools defined | RULE-01 |
| Procurement methods defined | RULE-01 |
| Strategies employed to protect against risks | RULE-02, RULE-03 |
| Strategies employed to identify risks | RULE-06 |
| Strategies employed to mitigate risks | RULE-02, RULE-04 |