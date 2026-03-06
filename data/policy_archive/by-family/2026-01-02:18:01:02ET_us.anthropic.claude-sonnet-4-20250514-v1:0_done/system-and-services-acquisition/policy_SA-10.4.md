# POLICY: SA-10.4: Trusted Generation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-10.4 |
| NIST Control | SA-10.4: Trusted Generation |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | trusted generation, version comparison, source code, object code, hardware descriptions, developer tools, configuration management |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST employ automated tools to compare newly generated versions of security-relevant hardware descriptions, source code, and object code with previous versions. This ensures authorized changes maintain security policy enforcement and prevents unauthorized modifications during development.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All security-relevant code development |
| Third-Party Developers | YES | Contractual requirement for all engagements |
| Vendor Software Components | YES | Must provide evidence of comparison processes |
| Open Source Components | CONDITIONAL | When modified or customized internally |
| Commercial Off-the-Shelf (COTS) | NO | Vendor responsibility, evidence required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Manager | • Ensure comparison tools are implemented and maintained<br>• Verify developer compliance with comparison requirements<br>• Maintain records of version comparison activities |
| Security Architect | • Define security-relevant components requiring comparison<br>• Approve comparison tools and methodologies<br>• Review comparison results for security policy compliance |
| Procurement Officer | • Include trusted generation requirements in contracts<br>• Verify vendor compliance with comparison tool requirements<br>• Obtain evidence of developer comparison processes |

## 4. RULES
[RULE-01] Developers MUST employ automated comparison tools for all newly generated versions of security-relevant hardware descriptions, source code, and object code.
[VALIDATION] IF security_relevant_component = TRUE AND comparison_tool_used = FALSE THEN critical_violation

[RULE-02] Version comparison activities MUST be documented with timestamps, tool outputs, and reviewer approval within 24 hours of code generation.
[VALIDATION] IF comparison_completed = TRUE AND documentation_time > 24_hours THEN violation

[RULE-03] Comparison tools MUST be capable of detecting unauthorized changes and generating detailed difference reports between versions.
[VALIDATION] IF tool_capability_verified = FALSE OR difference_report_generated = FALSE THEN violation

[RULE-04] Third-party developers MUST provide evidence of comparison tool usage and maintain comparison records for audit purposes.
[VALIDATION] IF vendor_type = "third_party" AND comparison_evidence_provided = FALSE THEN violation

[RULE-05] Security-relevant components MUST be identified and classified before development begins to ensure proper comparison coverage.
[VALIDATION] IF development_started = TRUE AND security_components_identified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Component Classification - Process for identifying security-relevant hardware, software, and firmware components
- [PROC-02] Comparison Tool Selection - Evaluation and approval of automated comparison tools and methodologies
- [PROC-03] Version Comparison Execution - Step-by-step process for conducting version comparisons during development
- [PROC-04] Vendor Compliance Verification - Process for validating third-party developer comparison activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized code changes, new development tools, vendor contract renewals

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal Development Compliance]
IF component_type = "security_relevant"
AND developer_type = "internal"
AND comparison_tool_employed = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Comparison Documentation]
IF security_relevant_component = TRUE
AND comparison_performed = TRUE
AND documentation_within_24hrs = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Third-Party Vendor Non-Compliance]
IF developer_type = "third_party"
AND comparison_evidence_provided = FALSE
AND contract_requires_comparison = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Inadequate Comparison Tool]
IF comparison_tool_deployed = TRUE
AND unauthorized_change_detection = FALSE
AND difference_reporting_capability = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Unclassified Security Component]
IF development_phase = "active"
AND security_classification_complete = FALSE
AND component_handles_sensitive_data = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer employs tools for comparing hardware descriptions | [RULE-01], [RULE-03] |
| Developer employs tools for comparing source code versions | [RULE-01], [RULE-03] |
| Developer employs tools for comparing object code versions | [RULE-01], [RULE-03] |
| Comparison activities are documented and auditable | [RULE-02], [RULE-04] |
| Security-relevant components are properly identified | [RULE-05] |