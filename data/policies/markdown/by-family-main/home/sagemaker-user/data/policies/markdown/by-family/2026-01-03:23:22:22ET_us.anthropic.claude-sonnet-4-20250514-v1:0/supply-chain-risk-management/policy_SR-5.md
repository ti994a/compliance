# POLICY: SR-5: Acquisition Strategies, Tools, and Methods

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-5 |
| NIST Control | SR-5: Acquisition Strategies, Tools, and Methods |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | acquisition, supply chain, procurement, contract tools, risk mitigation, supplier assessment |

## 1. POLICY STATEMENT
The organization SHALL employ defined acquisition strategies, contract tools, and procurement methods to protect against, identify, and mitigate supply chain risks throughout the system development lifecycle. All procurement activities MUST incorporate supply chain risk assessments and implement appropriate protective measures based on the security and privacy requirements of acquired systems and components.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All procurement activities | YES | Including systems, components, and services |
| Third-party suppliers | YES | All vendors providing technology products/services |
| Contract negotiations | YES | Must include supply chain risk provisions |
| Development contractors | YES | Custom software and system development |
| COTS purchases | YES | Commercial off-the-shelf products |
| Cloud service acquisitions | YES | IaaS, PaaS, SaaS procurement |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Define acquisition strategies and procurement methods<br>• Approve high-risk supplier engagements<br>• Ensure contract tools include supply chain protections |
| Supply Chain Risk Manager | • Conduct supplier risk assessments<br>• Define risk mitigation strategies<br>• Monitor supplier compliance with security requirements |
| Procurement Team | • Implement defined acquisition strategies<br>• Execute contract tools and protective measures<br>• Document procurement decisions and risk considerations |
| Security Team | • Define security requirements for acquisitions<br>• Review supplier security practices<br>• Validate implementation of protective measures |

## 4. RULES

[RULE-01] Organizations MUST define and document acquisition strategies, contract tools, and procurement methods specifically designed to protect against, identify, and mitigate supply chain risks.
[VALIDATION] IF acquisition_strategy_documented = FALSE OR contract_tools_defined = FALSE THEN violation

[RULE-02] Supply chain risk assessments MUST be conducted for all acquisitions exceeding $100,000 or involving systems processing sensitive data, regardless of cost.
[VALIDATION] IF (acquisition_value > $100000 OR data_sensitivity = "high") AND risk_assessment_completed = FALSE THEN violation

[RULE-03] Contract language MUST include provisions prohibiting tainted or counterfeit components and requiring supplier transparency into security practices.
[VALIDATION] IF contract_includes_counterfeit_prohibition = FALSE OR supplier_transparency_required = FALSE THEN violation

[RULE-04] Procurement methods MUST employ protective techniques such as obscured end-use, tamper-evident packaging, or trusted distribution channels for high-risk acquisitions.
[VALIDATION] IF risk_level = "high" AND protective_techniques_employed = FALSE THEN violation

[RULE-05] Supplier training and awareness programs MUST be provided to personnel involved in procurement activities within 90 days of role assignment.
[VALIDATION] IF personnel_role = "procurement" AND training_completion_date > (role_start_date + 90_days) THEN violation

[RULE-06] Documentation protection requirements MUST be specified in contracts for custom development or when proprietary information is shared.
[VALIDATION] IF (contract_type = "development" OR proprietary_info_shared = TRUE) AND documentation_protection_specified = FALSE THEN violation

[RULE-07] Acquisitions from suppliers on the organization's restricted or untrustworthy supplier list are PROHIBITED without executive approval and additional risk mitigation measures.
[VALIDATION] IF supplier_status = "restricted" AND executive_approval = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment - Evaluate supplier security practices and component integrity
- [PROC-02] Acquisition Strategy Development - Define risk-based procurement approaches
- [PROC-03] Contract Security Review - Ensure contracts include required supply chain protections
- [PROC-04] Supplier Security Validation - Verify implementation of required security controls
- [PROC-05] Procurement Personnel Training - Educate staff on supply chain risks and mitigation strategies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supply chain incidents, regulatory changes, significant supplier security breaches

## 7. SCENARIO PATTERNS

[SCENARIO-01: High-Value COTS Acquisition]
IF acquisition_type = "COTS"
AND acquisition_value > $500000
AND supply_chain_risk_assessment = "completed"
AND protective_measures_implemented = TRUE
THEN compliance = TRUE

[SCENARIO-02: Restricted Supplier Engagement]
IF supplier_status = "restricted"
AND executive_approval = FALSE
AND acquisition_proceeding = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Development Contract Without Documentation Protection]
IF contract_type = "custom_development"
AND proprietary_information_shared = TRUE
AND documentation_protection_clause = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Cloud Service Acquisition]
IF service_type = "cloud"
AND data_classification = "sensitive"
AND supplier_transparency_verified = TRUE
AND contract_includes_security_requirements = TRUE
THEN compliance = TRUE

[SCENARIO-05: Untrained Procurement Personnel]
IF personnel_role = "procurement"
AND supply_chain_training_completed = FALSE
AND days_in_role > 90
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Acquisition strategies defined and employed for protection | RULE-01, RULE-04 |
| Acquisition strategies defined and employed for identification | RULE-01, RULE-02 |
| Acquisition strategies defined and employed for mitigation | RULE-01, RULE-07 |
| Contract tools protect against supply chain risks | RULE-03, RULE-06 |
| Procurement methods mitigate supply chain risks | RULE-04, RULE-07 |
| Personnel training on supply chain risks | RULE-05 |