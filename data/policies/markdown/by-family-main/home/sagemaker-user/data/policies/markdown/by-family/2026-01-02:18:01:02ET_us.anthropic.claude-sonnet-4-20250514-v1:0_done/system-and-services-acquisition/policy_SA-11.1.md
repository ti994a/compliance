# POLICY: SA-11.1: Static Code Analysis

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.1 |
| NIST Control | SA-11.1: Static Code Analysis |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | static analysis, code security, vulnerability scanning, secure development, developer requirements |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services must employ static code analysis tools to identify common security flaws and document analysis results. Static code analysis must be integrated into the development lifecycle to ensure early detection and remediation of security vulnerabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All custom code development |
| Third-party Vendors | YES | Contract requirement for delivered code |
| Open Source Components | CONDITIONAL | When modified or integrated |
| Commercial Off-the-Shelf | NO | Vendor responsibility |
| Legacy Systems | CONDITIONAL | During major updates only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Manager | • Ensure static analysis tools are implemented<br>• Verify developer compliance with scanning requirements<br>• Review and approve remediation timelines |
| Security Team | • Define static analysis tool requirements<br>• Review analysis results and false positive rates<br>• Validate remediation of critical findings |
| Procurement Team | • Include static analysis requirements in vendor contracts<br>• Verify vendor compliance with analysis documentation |

## 4. RULES
[RULE-01] Developers MUST employ approved static code analysis tools on all custom code before deployment to production environments.
[VALIDATION] IF code_deployment = "production" AND static_analysis_completed = FALSE THEN critical_violation

[RULE-02] Static code analysis MUST be performed on each code commit or at minimum weekly for active development projects.
[VALIDATION] IF days_since_last_scan > 7 AND development_status = "active" THEN violation

[RULE-03] All critical and high severity findings from static analysis MUST be remediated before production deployment.
[VALIDATION] IF finding_severity IN ["critical", "high"] AND finding_status != "remediated" AND deployment_target = "production" THEN critical_violation

[RULE-04] Static analysis results MUST be documented and retained for audit purposes for minimum 3 years.
[VALIDATION] IF analysis_documentation_age > 3_years AND audit_required = TRUE THEN violation

[RULE-05] False positive rates MUST NOT exceed 20% of total findings; rates above 20% require tool recalibration or replacement.
[VALIDATION] IF false_positive_rate > 0.20 THEN process_violation

[RULE-06] Third-party vendors MUST provide static analysis results and remediation evidence for all delivered code components.
[VALIDATION] IF vendor_delivery = TRUE AND static_analysis_results = NULL THEN contract_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Static Analysis Tool Selection - Evaluation and approval of scanning tools
- [PROC-02] Finding Remediation Workflow - Process for addressing identified vulnerabilities
- [PROC-03] False Positive Management - Procedures for validating and managing false positives
- [PROC-04] Vendor Analysis Requirements - Contract language and verification procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New tool implementations, significant false positive rate changes, vendor contract renewals

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production Deployment Without Scan]
IF deployment_environment = "production"
AND static_analysis_completed = FALSE
AND code_type = "custom"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Unresolved Critical Findings]
IF finding_severity = "critical"
AND finding_status = "open"
AND days_open > 30
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Vendor Delivery Missing Analysis]
IF delivery_source = "third_party_vendor"
AND static_analysis_documentation = FALSE
AND contract_requires_analysis = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Acceptable False Positive Rate]
IF total_findings = 100
AND false_positives = 15
AND false_positive_rate <= 0.20
THEN compliance = TRUE

[SCENARIO-05: Legacy System Exception]
IF system_type = "legacy"
AND modification_type = "minor_patch"
AND business_justification_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer employs static code analysis tools | [RULE-01], [RULE-06] |
| Developer documents analysis results | [RULE-04], [RULE-06] |
| Analysis identifies common flaws | [RULE-03], [RULE-05] |
| Evidence of proper implementation | [RULE-02], [RULE-04] |