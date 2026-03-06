# POLICY: SA-11.9: Interactive Application Security Testing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.9 |
| NIST Control | SA-11.9: Interactive Application Security Testing |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | interactive testing, IAST, application security, vulnerability assessment, developer testing, instrumentation |

## 1. POLICY STATEMENT
All system, system component, and system service developers MUST employ interactive application security testing (IAST) tools to identify security flaws during the development lifecycle. Testing results and identified vulnerabilities MUST be documented and tracked through remediation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal development teams | YES | All applications and system components |
| Third-party developers | YES | Contractual requirement for custom development |
| COTS software vendors | CONDITIONAL | When source code access available |
| Cloud service providers | CONDITIONAL | For custom integrations and configurations |
| Legacy systems | YES | During major updates or security reviews |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Implement IAST tools in CI/CD pipelines<br>• Execute interactive security testing<br>• Document and remediate identified flaws |
| Security Team | • Define IAST tool requirements and standards<br>• Review testing results and remediation plans<br>• Validate flaw remediation |
| Procurement Team | • Include IAST requirements in vendor contracts<br>• Verify vendor compliance with testing requirements |

## 4. RULES
[RULE-01] All developers MUST employ NIST-approved interactive application security testing tools during system development and testing phases.
[VALIDATION] IF development_project = TRUE AND iast_tool_employed = FALSE THEN violation

[RULE-02] Interactive security testing MUST be performed continuously throughout the system development lifecycle, not just at final testing phases.
[VALIDATION] IF development_phase IN ["design", "implementation", "testing"] AND iast_testing_performed = FALSE THEN violation

[RULE-03] All security flaws identified through IAST tools MUST be documented within 24 hours of discovery with severity classification.
[VALIDATION] IF flaw_identified = TRUE AND documentation_time > 24_hours THEN violation

[RULE-04] Critical and high-severity flaws identified by IAST tools MUST be remediated before system deployment or release.
[VALIDATION] IF flaw_severity IN ["critical", "high"] AND system_deployed = TRUE AND flaw_status != "remediated" THEN critical_violation

[RULE-05] IAST testing results and remediation tracking reports MUST be maintained for audit purposes for minimum 3 years.
[VALIDATION] IF report_age > 3_years AND report_retained = FALSE THEN violation

[RULE-06] Third-party developers MUST provide evidence of IAST tool usage and testing results as part of deliverable acceptance criteria.
[VALIDATION] IF vendor_deliverable = TRUE AND iast_evidence_provided = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] IAST Tool Selection and Approval - Process for evaluating and approving interactive testing tools
- [PROC-02] Developer IAST Integration - Guidelines for integrating IAST tools into development workflows
- [PROC-03] Vulnerability Documentation and Tracking - Standard process for documenting and tracking identified flaws
- [PROC-04] Vendor IAST Compliance Verification - Process for verifying third-party developer compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New IAST tool deployments, significant security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing IAST in Development]
IF development_project = TRUE
AND iast_tool_integrated = FALSE
AND project_phase = "implementation"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unresolved Critical Flaw at Deployment]
IF iast_flaw_severity = "critical"
AND system_deployment_approved = TRUE
AND flaw_remediation_status != "completed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Vendor Without IAST Evidence]
IF vendor_type = "custom_development"
AND deliverable_acceptance = "pending"
AND iast_results_provided = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed Flaw Documentation]
IF flaw_discovery_date < current_date - 2_days
AND flaw_documentation_status = "incomplete"
AND flaw_severity IN ["medium", "high", "critical"]
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant IAST Implementation]
IF iast_tool_approved = TRUE
AND testing_frequency = "continuous"
AND flaw_documentation_complete = TRUE
AND critical_flaws_remediated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer employs interactive application security testing tools | RULE-01, RULE-02 |
| Developer documents flaw identification results | RULE-03, RULE-05 |
| Testing tools identify security flaws effectively | RULE-01, RULE-04 |
| Results documentation and tracking maintained | RULE-03, RULE-05, RULE-06 |