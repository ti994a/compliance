# POLICY: SA-11.1: Static Code Analysis

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.1 |
| NIST Control | SA-11.1: Static Code Analysis |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | static analysis, code security, developer requirements, vulnerability scanning, secure coding |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST employ static code analysis tools to identify common security flaws and document analysis results. Static code analysis MUST be integrated into the development lifecycle to detect vulnerabilities early and enforce secure coding practices.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All custom software development |
| Third-party Developers | YES | Contractual requirement for all engagements |
| Commercial Off-the-Shelf Software | CONDITIONAL | When source code access is available |
| Open Source Components | YES | Before integration into systems |
| Legacy Systems | CONDITIONAL | During major updates or security reviews |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Execute static code analysis on all code changes<br>• Review and remediate identified vulnerabilities<br>• Document analysis results and remediation actions |
| Security Team | • Define static analysis tool requirements and configurations<br>• Review high-risk findings and remediation plans<br>• Monitor analysis metrics and false positive rates |
| Procurement Team | • Include static analysis requirements in vendor contracts<br>• Verify vendor compliance with analysis requirements<br>• Collect and review vendor analysis documentation |

## 4. RULES
[RULE-01] All developers MUST employ approved static code analysis tools on every code commit or build.
[VALIDATION] IF code_commit = TRUE AND static_analysis_executed = FALSE THEN violation

[RULE-02] Static analysis results MUST be documented with findings categorized by severity level (Critical, High, Medium, Low).
[VALIDATION] IF static_analysis_executed = TRUE AND results_documented = FALSE THEN violation

[RULE-03] Critical and High severity findings MUST be remediated before production deployment.
[VALIDATION] IF deployment_target = "production" AND (critical_findings > 0 OR high_findings > 0) AND remediated = FALSE THEN critical_violation

[RULE-04] Static analysis tools MUST be configured to detect OWASP Top 10 vulnerabilities and organization-specific security patterns.
[VALIDATION] IF tool_configured = TRUE AND owasp_coverage < 100% THEN violation

[RULE-05] False positive rates MUST be monitored and maintained below 20% for each analysis tool.
[VALIDATION] IF false_positive_rate > 20% THEN review_required

[RULE-06] Third-party developers MUST provide static analysis reports within 5 business days of code delivery.
[VALIDATION] IF vendor_delivery = TRUE AND analysis_report_received = FALSE AND days_elapsed > 5 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Static Analysis Tool Selection - Evaluation and approval process for analysis tools
- [PROC-02] Analysis Result Review - Process for reviewing, triaging, and tracking findings
- [PROC-03] Vendor Compliance Verification - Validation of third-party analysis requirements
- [PROC-04] False Positive Management - Process for identifying and suppressing false positives

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New tool implementations, significant false positive rate changes, security incidents related to code vulnerabilities

## 7. SCENARIO PATTERNS
[SCENARIO-01: Pre-Production Deployment]
IF deployment_target = "production"
AND static_analysis_completed = TRUE
AND critical_findings = 0
AND high_findings = 0
THEN compliance = TRUE

[SCENARIO-02: Third-Party Code Delivery]
IF code_source = "third_party"
AND delivery_date <= current_date - 5_days
AND static_analysis_report_received = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: High False Positive Rate]
IF static_analysis_tool_active = TRUE
AND false_positive_rate > 20%
AND remediation_plan_created = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Legacy System Update]
IF system_type = "legacy"
AND modification_scope = "major"
AND static_analysis_executed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Open Source Integration]
IF component_type = "open_source"
AND integration_planned = TRUE
AND static_analysis_completed = TRUE
AND findings_reviewed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer must employ static code analysis tools | [RULE-01], [RULE-04] |
| Developer must document analysis results | [RULE-02] |
| Analysis must identify common flaws | [RULE-04] |
| Results must be actionable and reviewed | [RULE-03], [RULE-05] |