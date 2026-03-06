# POLICY: SR-7: Supply Chain Operations Security

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-7 |
| NIST Control | SR-7: Supply Chain Operations Security |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, OPSEC, operations security, vendor management, supplier protection, critical information |

## 1. POLICY STATEMENT
The organization SHALL employ Operations Security (OPSEC) controls to protect supply chain-related information for systems, system components, and system services. Supply chain OPSEC controls MUST be defined, documented, and implemented to prevent adversaries from obtaining critical information about organizational operations, suppliers, and system configurations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Systems | YES | Including cloud, on-premises, and hybrid |
| System Components | YES | Hardware, software, firmware components |
| System Services | YES | Managed services, SaaS, PaaS, IaaS |
| Suppliers/Vendors | YES | All tiers of supply chain participants |
| Third-party Integrators | YES | Implementation and maintenance partners |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define organizational OPSEC requirements<br>• Approve supply chain OPSEC controls<br>• Oversee OPSEC program implementation |
| Procurement Officer | • Implement OPSEC controls in acquisition processes<br>• Manage supplier information disclosure<br>• Coordinate with intermediaries when required |
| Supply Chain Risk Manager | • Identify critical supply chain information<br>• Assess OPSEC vulnerabilities<br>• Monitor supplier OPSEC compliance |

## 4. RULES

[RULE-01] Organizations MUST define and document specific OPSEC controls for protecting supply chain-related information including user identities, system uses, supplier identities, security requirements, configurations, processes, and testing results.
[VALIDATION] IF supply_chain_opsec_controls_defined = FALSE THEN critical_violation

[RULE-02] Critical supply chain information MUST be classified and protected according to its sensitivity level, with formal procedures for information sharing with suppliers.
[VALIDATION] IF critical_info_classification = "undefined" AND supplier_access = TRUE THEN violation

[RULE-03] Organizations SHALL analyze and document potential indicators that adversaries might obtain from supply chain activities and implement countermeasures to eliminate or reduce exploitable vulnerabilities.
[VALIDATION] IF indicator_analysis_documented = FALSE OR countermeasures_implemented = FALSE THEN violation

[RULE-04] Mission or business information MAY be withheld from suppliers when necessary to maintain operational security, with justification documented in the supply chain risk management plan.
[VALIDATION] IF sensitive_info_withheld = TRUE AND justification_documented = FALSE THEN violation

[RULE-05] Organizations MUST use intermediaries or other obfuscation methods to hide end users or specific uses of systems when required by OPSEC analysis.
[VALIDATION] IF opsec_analysis_requires_intermediary = TRUE AND intermediary_used = FALSE THEN violation

[RULE-06] Supply chain OPSEC controls MUST be reviewed and updated annually or when significant changes occur to systems, suppliers, or threat environment.
[VALIDATION] IF last_opsec_review_date > 365_days AND no_significant_changes = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Critical Information Identification - Process for identifying and classifying sensitive supply chain information
- [PROC-02] OPSEC Vulnerability Assessment - Regular analysis of supply chain information exposure risks
- [PROC-03] Supplier Information Sharing Controls - Procedures for controlled disclosure of information to suppliers
- [PROC-04] Intermediary Management - Process for engaging and managing intermediary services when required

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New supplier onboarding, system changes, security incidents, threat intelligence updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Uncontrolled Supplier Information Sharing]
IF supplier_access_request = TRUE
AND information_classification = "critical"
AND opsec_controls_applied = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing OPSEC Analysis]
IF new_supplier_onboarding = TRUE
AND opsec_vulnerability_assessment = "not_performed"
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Intermediary Requirement Not Met]
IF opsec_analysis_result = "requires_intermediary"
AND direct_supplier_engagement = TRUE
AND intermediary_used = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Proper OPSEC Implementation]
IF opsec_controls_defined = TRUE
AND critical_info_protected = TRUE
AND countermeasures_implemented = TRUE
AND regular_reviews_conducted = TRUE
THEN compliance = TRUE

[SCENARIO-05: Information Withholding Without Justification]
IF sensitive_info_withheld_from_supplier = TRUE
AND business_justification_documented = FALSE
AND supply_chain_plan_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| OPSEC controls are defined | [RULE-01] |
| OPSEC controls are employed to protect supply chain information | [RULE-02], [RULE-03], [RULE-04], [RULE-05] |
| Supply chain information protection | [RULE-01], [RULE-02] |
| Vulnerability assessment and countermeasures | [RULE-03] |
| Information sharing controls | [RULE-04] |
| Intermediary usage when required | [RULE-05] |