# POLICY: SA-10.4: Trusted Generation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-10.4 |
| NIST Control | SA-10.4: Trusted Generation |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | trusted generation, version comparison, developer tools, configuration management, source code, object code, hardware descriptions |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST employ automated tools to compare newly generated versions of security-relevant hardware descriptions, source code, and object code with previous versions. This ensures authorized changes maintain security policy enforcement and enables detection of unauthorized modifications during the development lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All teams developing security-relevant components |
| Third-Party Developers | YES | Required via contractual agreements |
| Vendor-Supplied Components | YES | Verification requirements for custom/modified components |
| COTS Products | NO | Standard commercial products without customization |
| Open Source Components | CONDITIONAL | When modified or integrated into security-relevant functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Team Lead | • Ensure comparison tools are implemented and operational<br>• Verify all security-relevant code changes are properly compared<br>• Maintain documentation of comparison results |
| Security Architecture Team | • Define security-relevant components requiring comparison<br>• Approve comparison tools and methodologies<br>• Review comparison results for security implications |
| Procurement Manager | • Include trusted generation requirements in vendor contracts<br>• Verify vendor compliance with comparison tool requirements<br>• Ensure service level agreements address comparison obligations |

## 4. RULES
[RULE-01] Developers MUST employ automated comparison tools for all newly generated versions of security-relevant hardware descriptions before deployment.
[VALIDATION] IF security_relevant_hardware = TRUE AND comparison_tool_used = FALSE THEN critical_violation

[RULE-02] Developers MUST employ automated comparison tools for all newly generated versions of source code that implement security functions before compilation.
[VALIDATION] IF security_relevant_source_code = TRUE AND version_comparison_performed = FALSE THEN critical_violation

[RULE-03] Developers MUST employ automated comparison tools for all newly generated versions of object code that enforce security policies before deployment.
[VALIDATION] IF security_relevant_object_code = TRUE AND object_code_comparison = FALSE THEN critical_violation

[RULE-04] Comparison tool results MUST be documented and retained for audit purposes for a minimum of three years.
[VALIDATION] IF comparison_performed = TRUE AND documentation_retained = FALSE THEN moderate_violation

[RULE-05] Third-party developers SHALL be contractually required to implement trusted generation processes with comparison tools for all security-relevant components.
[VALIDATION] IF third_party_developer = TRUE AND contract_includes_trusted_generation = FALSE THEN high_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Trusted Generation Tool Selection - Process for evaluating and approving comparison tools
- [PROC-02] Security-Relevant Component Classification - Methodology for identifying components requiring comparison
- [PROC-03] Version Comparison Workflow - Step-by-step process for performing and documenting comparisons
- [PROC-04] Vendor Compliance Verification - Process for validating third-party adherence to trusted generation requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving code integrity, new development methodologies, vendor contract renewals, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal Development Release]
IF component_type = "security_relevant"
AND developer_type = "internal"
AND version_comparison_performed = FALSE
AND deployment_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Third-Party Custom Component]
IF developer_type = "third_party"
AND component_customized = TRUE
AND security_function_implemented = TRUE
AND contract_requires_comparison = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Hardware Description Update]
IF component_type = "hardware_description"
AND security_relevant = TRUE
AND comparison_tool_employed = TRUE
AND results_documented = TRUE
THEN compliance = TRUE
violation_severity = "None"

[SCENARIO-04: Source Code Without Comparison]
IF code_type = "source_code"
AND security_policy_enforced = TRUE
AND new_version_generated = TRUE
AND comparison_performed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: COTS Product Integration]
IF product_type = "COTS"
AND customization_performed = FALSE
AND security_relevant_modifications = FALSE
THEN compliance = TRUE
violation_severity = "None"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer employs tools for comparing hardware descriptions | [RULE-01] |
| Developer employs tools for comparing source code versions | [RULE-02] |
| Developer employs tools for comparing object code versions | [RULE-03] |
| Documentation and audit trail maintenance | [RULE-04] |
| Third-party developer contractual requirements | [RULE-05] |