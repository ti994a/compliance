# POLICY: SA-11.1: Static Code Analysis

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.1 |
| NIST Control | SA-11.1: Static Code Analysis |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | static code analysis, secure coding, vulnerability detection, developer requirements, code security |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST employ static code analysis tools to identify common security flaws and document analysis results. Static code analysis SHALL be integrated into the development lifecycle to detect vulnerabilities early and enforce secure coding practices.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All custom software development |
| Third-Party Developers | YES | Contractual requirement for all engagements |
| Vendor Software Components | CONDITIONAL | When source code access is available |
| Open Source Components | YES | Before integration into systems |
| Legacy Systems | CONDITIONAL | During major updates or security reviews |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Team Lead | • Ensure static analysis tools are configured and operational<br>• Review and approve remediation plans<br>• Track defect resolution metrics |
| Security Engineering | • Define static analysis tool requirements<br>• Review high-severity findings<br>• Validate remediation effectiveness |
| Third-Party Vendors | • Execute static code analysis on deliverables<br>• Provide documented analysis results<br>• Remediate identified critical vulnerabilities |

## 4. RULES
[RULE-01] All developers MUST employ approved static code analysis tools on source code before deployment to production environments.
[VALIDATION] IF code_deployed = TRUE AND static_analysis_completed = FALSE THEN critical_violation

[RULE-02] Static code analysis results MUST be documented and include defect density metrics, remediation status, and security professional review evidence.
[VALIDATION] IF analysis_completed = TRUE AND (documentation_complete = FALSE OR remediation_status = NULL) THEN violation

[RULE-03] Critical and high-severity vulnerabilities identified by static analysis MUST be remediated before production deployment.
[VALIDATION] IF vulnerability_severity IN ["critical", "high"] AND remediation_status != "fixed" AND deployment_approved = TRUE THEN critical_violation

[RULE-04] Static code analysis MUST be performed on each code change in automated CI/CD pipelines for systems processing sensitive data.
[VALIDATION] IF system_classification >= "sensitive" AND code_change = TRUE AND automated_analysis = FALSE THEN violation

[RULE-05] False positive rates exceeding 30% MUST trigger tool reconfiguration or replacement evaluation within 30 days.
[VALIDATION] IF false_positive_rate > 0.30 AND evaluation_initiated = FALSE AND days_since_detection > 30 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Static Analysis Tool Selection - Evaluation and approval of static code analysis tools
- [PROC-02] Defect Remediation Workflow - Process for reviewing, prioritizing, and fixing identified vulnerabilities
- [PROC-03] Third-Party Analysis Verification - Validation of vendor-provided static analysis results
- [PROC-04] False Positive Management - Process for handling and reducing false positive findings

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New tool deployment, significant false positive rate changes, security incidents related to code vulnerabilities

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production Deployment Without Analysis]
IF deployment_environment = "production"
AND static_analysis_completed = FALSE
AND system_classification >= "moderate"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Vendor Code Analysis Documentation]
IF vendor_code = TRUE
AND analysis_results_provided = TRUE
AND security_review_completed = TRUE
AND critical_findings_remediated = TRUE
THEN compliance = TRUE

[SCENARIO-03: High False Positive Rate]
IF false_positive_rate > 0.30
AND rate_duration > 30_days
AND tool_evaluation_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: CI/CD Pipeline Integration]
IF system_classification = "high"
AND code_commit = TRUE
AND automated_static_analysis = TRUE
AND pipeline_blocked_on_critical = TRUE
THEN compliance = TRUE

[SCENARIO-05: Legacy System Exception]
IF system_type = "legacy"
AND major_update = FALSE
AND risk_assessment_current = TRUE
AND compensating_controls = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer employment of static code analysis tools | [RULE-01], [RULE-04] |
| Documentation of analysis results | [RULE-02] |
| Vulnerability remediation tracking | [RULE-03] |
| Tool effectiveness monitoring | [RULE-05] |