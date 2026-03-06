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
All system, system component, and system service developers MUST employ interactive application security testing (IAST) tools to identify security flaws during the development lifecycle. Testing results and identified vulnerabilities MUST be documented and tracked through remediation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All applications and system components |
| Third-Party Developers | YES | Contractual requirement for all engagements |
| Commercial Software Vendors | YES | Required for custom/modified solutions |
| Open Source Components | CONDITIONAL | When modified or integrated into custom solutions |
| Legacy Systems | CONDITIONAL | During major updates or security assessments |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Implement IAST tools in development pipeline<br>• Execute interactive security testing<br>• Document and remediate identified flaws |
| Security Team | • Define IAST tool requirements and standards<br>• Review testing results and documentation<br>• Validate remediation efforts |
| Procurement Team | • Include IAST requirements in vendor contracts<br>• Verify vendor compliance with testing requirements<br>• Maintain documentation of vendor testing results |

## 4. RULES
[RULE-01] Developers MUST employ NIST-approved interactive application security testing tools for all applications and system components.
[VALIDATION] IF development_project = TRUE AND iast_tool_approved = FALSE THEN violation

[RULE-02] Interactive security testing MUST be performed continuously throughout the system development lifecycle, not just at final testing phases.
[VALIDATION] IF development_phase IN ["design", "implementation", "testing"] AND iast_executed = FALSE THEN violation

[RULE-03] All security flaws identified through IAST MUST be documented with severity ratings, affected components, and remediation timelines.
[VALIDATION] IF flaw_identified = TRUE AND (documentation_complete = FALSE OR severity_rating = NULL OR remediation_timeline = NULL) THEN violation

[RULE-04] Critical and high-severity flaws identified through IAST MUST be remediated before system deployment or service delivery.
[VALIDATION] IF deployment_ready = TRUE AND (critical_flaws > 0 OR high_severity_flaws > 0) AND remediation_complete = FALSE THEN critical_violation

[RULE-05] IAST results and remediation status MUST be tracked and reported to security teams within 48 hours of test completion.
[VALIDATION] IF test_completion_time > 48_hours AND security_team_notified = FALSE THEN violation

[RULE-06] Third-party developers MUST provide IAST tool documentation, testing results, and remediation evidence as contractual deliverables.
[VALIDATION] IF vendor_engagement = TRUE AND (iast_documentation = FALSE OR test_results = FALSE OR remediation_evidence = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] IAST Tool Selection and Approval - Process for evaluating and approving interactive security testing tools
- [PROC-02] Developer IAST Implementation - Standard procedures for integrating IAST tools into development workflows
- [PROC-03] Vulnerability Documentation and Tracking - Process for documenting, categorizing, and tracking identified security flaws
- [PROC-04] Vendor IAST Compliance Verification - Procedures for validating third-party developer compliance with IAST requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New IAST tool technologies, major security incidents, regulatory changes, vendor contract renewals

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal Development Without IAST]
IF project_type = "internal_development"
AND iast_tool_implemented = FALSE
AND development_phase = "active"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Vendor Delivers Without Testing Evidence]
IF vendor_deliverable = TRUE
AND iast_results_provided = FALSE
AND contract_requires_iast = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Critical Flaws Not Remediated Before Deployment]
IF deployment_scheduled = TRUE
AND critical_vulnerabilities > 0
AND remediation_status = "incomplete"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: IAST Results Not Reported Timely]
IF test_completion_date < (current_date - 2_days)
AND security_team_notification = FALSE
AND testing_results_available = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Continuous Testing Implementation]
IF development_lifecycle = "active"
AND iast_integrated = TRUE
AND testing_frequency = "continuous"
AND results_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer required to employ IAST tools | [RULE-01], [RULE-02] |
| Developer required to identify flaws | [RULE-02], [RULE-03] |
| Developer required to document results | [RULE-03], [RULE-05] |
| Continuous testing throughout SDLC | [RULE-02] |
| Third-party compliance verification | [RULE-06] |