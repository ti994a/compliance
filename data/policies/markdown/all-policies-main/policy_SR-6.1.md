```markdown
# POLICY: SR-6.1: Testing and Analysis

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-6.1 |
| NIST Control | SR-6.1: Testing and Analysis |
| Version | 1.0 |
| Owner | Chief Supply Chain Risk Officer |
| Keywords | supply chain, testing, analysis, vendor assessment, third-party risk, SCRM |

## 1. POLICY STATEMENT
The organization MUST employ systematic analysis and testing of supply chain elements, processes, and actors associated with systems, system components, or system services. All evidence from supply chain analysis and testing MUST be documented and used to inform organizational risk management decisions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Systems | YES | Including cloud, hybrid, and on-premises |
| System Components | YES | Hardware, software, firmware components |
| System Services | YES | Outsourced and third-party services |
| Supply Chain Partners | YES | Vendors, contractors, service providers |
| Development Processes | YES | Internal and external development |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Risk Officer | • Define supply chain analysis requirements<br>• Approve testing methodologies<br>• Review analysis results and risk decisions |
| Supply Chain Risk Analysts | • Conduct supply chain element analysis<br>• Perform or coordinate testing activities<br>• Document findings and evidence |
| System Owners | • Identify supply chain elements for analysis<br>• Provide access for testing activities<br>• Implement risk mitigation measures |

## 4. RULES
[RULE-01] Organizations MUST define and document all supply chain elements, processes, and actors subject to analysis and testing before system deployment.
[VALIDATION] IF system_deployment_approved = TRUE AND supply_chain_elements_documented = FALSE THEN violation

[RULE-02] Supply chain analysis MUST be performed using organizational analysis, independent third-party analysis, or both for all critical system components.
[VALIDATION] IF component_criticality = "high" AND (organizational_analysis = FALSE AND third_party_analysis = FALSE) THEN violation

[RULE-03] Penetration testing MUST be conducted on supply chain processes for systems processing sensitive data, performed either organizationally or by independent third parties.
[VALIDATION] IF data_sensitivity >= "moderate" AND (org_pentest = FALSE AND third_party_pentest = FALSE) THEN violation

[RULE-04] All supply chain analysis and testing evidence MUST be documented within 30 days of completion and retained for minimum 3 years.
[VALIDATION] IF analysis_completion_date + 30_days < current_date AND documentation_complete = FALSE THEN violation

[RULE-05] Supply chain analysis results MUST be integrated into organizational risk management decisions and documented in risk assessments.
[VALIDATION] IF supply_chain_analysis_complete = TRUE AND risk_assessment_updated = FALSE THEN violation

[RULE-06] Supply chain testing MUST be repeated annually or when significant changes occur to supply chain elements, processes, or actors.
[VALIDATION] IF last_testing_date + 365_days < current_date AND no_significant_changes = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Element Identification - Systematic process to identify and catalog all supply chain components
- [PROC-02] Supply Chain Risk Analysis - Methodology for analyzing supply chain elements, processes, and actors
- [PROC-03] Third-Party Testing Coordination - Process for engaging and managing independent testing providers
- [PROC-04] Evidence Documentation and Retention - Standardized documentation and storage of analysis results

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supply chain changes, security incidents, regulatory changes, failed assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Critical Vendor Onboarding]
IF vendor_criticality = "high"
AND system_data_sensitivity >= "moderate"
AND supply_chain_analysis_complete = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Annual Testing Compliance]
IF last_supply_chain_testing + 365_days < current_date
AND no_significant_changes = TRUE
AND testing_scheduled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Third-Party Analysis Documentation]
IF third_party_analysis_complete = TRUE
AND analysis_completion_date + 30_days < current_date
AND evidence_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Risk Integration Requirement]
IF supply_chain_analysis_findings_available = TRUE
AND risk_assessment_last_updated < analysis_completion_date
AND findings_severity >= "moderate"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Penetration Testing Exemption]
IF system_data_sensitivity = "low"
AND supply_chain_pentest = FALSE
AND organizational_analysis = TRUE
THEN compliance = TRUE
violation_severity = "None"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Organizational analysis employed on supply chain elements | [RULE-02], [RULE-03] |
| Supply chain elements, processes, and actors defined | [RULE-01] |
| Analysis results documented and used for risk decisions | [RULE-04], [RULE-05] |
| Testing performed on supply chain components | [RULE-03], [RULE-06] |
| Evidence collection and documentation | [RULE-04] |
```