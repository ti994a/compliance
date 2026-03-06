# POLICY: SA-11.9: Interactive Application Security Testing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.9 |
| NIST Control | SA-11.9: Interactive Application Security Testing |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | interactive testing, application security, IAST, vulnerability detection, developer requirements, security testing, instrumentation |

## 1. POLICY STATEMENT
All system developers, system component developers, and system service providers MUST employ interactive application security testing (IAST) tools to identify security flaws during the development lifecycle. Testing results and identified vulnerabilities MUST be documented and tracked through resolution.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All applications and system components |
| Third-Party Developers | YES | Contractual requirement for custom development |
| COTS Software Vendors | CONDITIONAL | When customization or integration testing required |
| Cloud Service Providers | CONDITIONAL | For custom integrations and configurations |
| Legacy Systems | YES | During modernization or major updates |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Implement IAST tools in development pipeline<br>• Execute interactive security testing<br>• Document and remediate identified flaws |
| Security Team | • Define IAST tool requirements and standards<br>• Review testing results and documentation<br>• Validate flaw remediation |
| Procurement Team | • Include IAST requirements in vendor contracts<br>• Verify vendor compliance with testing requirements |
| Project Managers | • Ensure IAST testing is integrated into project timelines<br>• Track remediation of identified security flaws |

## 4. RULES
[RULE-01] Developers MUST employ interactive application security testing tools that provide real-time vulnerability detection during application runtime.
[VALIDATION] IF development_project = TRUE AND iast_tool_implemented = FALSE THEN violation

[RULE-02] IAST testing MUST be performed continuously throughout the system development lifecycle, not just at final testing phases.
[VALIDATION] IF sdlc_phase IN ["design", "development", "testing", "integration"] AND iast_testing_active = FALSE THEN violation

[RULE-03] All security flaws identified through IAST tools MUST be documented with severity level, affected components, and remediation timeline.
[VALIDATION] IF iast_flaw_identified = TRUE AND (documentation_complete = FALSE OR severity_assigned = FALSE) THEN violation

[RULE-04] Critical and high-severity flaws identified by IAST tools MUST be remediated before system deployment or release.
[VALIDATION] IF deployment_ready = TRUE AND (critical_flaws > 0 OR high_severity_flaws > 0) THEN critical_violation

[RULE-05] IAST tool results MUST be integrated with existing vulnerability management and tracking systems for centralized monitoring.
[VALIDATION] IF iast_results_generated = TRUE AND vulnerability_system_integration = FALSE THEN violation

[RULE-06] Third-party developers MUST provide evidence of IAST tool usage and testing results as part of deliverable acceptance criteria.
[VALIDATION] IF third_party_delivery = TRUE AND (iast_evidence_provided = FALSE OR testing_results_documented = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] IAST Tool Selection and Configuration - Standards for selecting, configuring, and maintaining interactive application security testing tools
- [PROC-02] Vulnerability Documentation and Tracking - Process for documenting, categorizing, and tracking security flaws identified through IAST
- [PROC-03] Flaw Remediation Workflow - Procedures for prioritizing, assigning, and verifying resolution of identified security vulnerabilities
- [PROC-04] Third-Party IAST Compliance Verification - Process for validating vendor compliance with interactive testing requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New IAST tool implementations, major security incidents, regulatory changes, development methodology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal Development Without IAST]
IF project_type = "internal_development"
AND application_type = "web_application"
AND iast_tool_configured = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Third-Party Development Missing Documentation]
IF vendor_type = "third_party_developer"
AND deliverable_status = "submitted"
AND iast_results_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Critical Flaws in Production Deployment]
IF deployment_stage = "production_ready"
AND iast_critical_flaws > 0
AND remediation_status = "pending"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Continuous IAST Implementation]
IF sdlc_phase = "development"
AND iast_tool_active = TRUE
AND real_time_monitoring = TRUE
AND flaw_documentation = "complete"
THEN compliance = TRUE

[SCENARIO-05: Legacy System Update Compliance]
IF system_type = "legacy"
AND update_type = "major_modification"
AND iast_testing_performed = TRUE
AND results_integrated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer must employ interactive application security testing tools | [RULE-01], [RULE-02] |
| Developer must identify flaws using IAST tools | [RULE-01], [RULE-05] |
| Developer must document results of flaw identification | [RULE-03], [RULE-06] |
| Testing must be performed throughout development lifecycle | [RULE-02] |
| Results must be tracked and managed | [RULE-05] |