# POLICY: SA-15.1: Quality Metrics

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-15.1 |
| NIST Control | SA-15.1: Quality Metrics |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | quality metrics, development process, vulnerability thresholds, quality gates, CVSS, developer requirements |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST define quality metrics at the beginning of the development process and provide evidence of meeting these quality metrics throughout development. Quality metrics SHALL include security and privacy requirements with measurable completion criteria and vulnerability severity thresholds aligned with organizational risk tolerance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All software development projects |
| External Vendors/Contractors | YES | Per contract requirements |
| Third-party Components | YES | When integration involves custom development |
| COTS Software | NO | Unless customization/integration development required |
| Cloud Service Configurations | CONDITIONAL | When custom development is involved |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Manager | • Define quality metrics framework<br>• Ensure metrics alignment with security requirements<br>• Validate evidence collection processes |
| Security Architect | • Review and approve security-related quality metrics<br>• Define vulnerability severity thresholds<br>• Validate security quality gates |
| Procurement Manager | • Include quality metrics requirements in contracts<br>• Verify vendor compliance with metrics<br>• Manage evidence collection from external developers |

## 4. RULES
[RULE-01] Developers MUST define quality metrics within 30 days of project initiation and before any development work begins.
[VALIDATION] IF development_started = TRUE AND quality_metrics_defined = FALSE THEN violation

[RULE-02] Quality metrics MUST include vulnerability severity thresholds with no CVSS medium or high severity vulnerabilities permitted in delivered systems.
[VALIDATION] IF delivered_system = TRUE AND (cvss_medium > 0 OR cvss_high > 0 OR cvss_critical > 0) THEN critical_violation

[RULE-03] Developers SHALL provide evidence of meeting quality metrics at each defined quality gate and upon project completion.
[VALIDATION] IF quality_gate_reached = TRUE AND evidence_provided = FALSE THEN violation

[RULE-04] Quality gates MUST include elimination of all compiler warnings or documented determination that warnings do not impact security/privacy capabilities.
[VALIDATION] IF quality_gate_passed = TRUE AND (compiler_warnings > 0 AND warning_impact_analysis = FALSE) THEN violation

[RULE-05] External developers MUST contractually commit to organizational quality metrics before contract execution.
[VALIDATION] IF contract_executed = TRUE AND external_developer = TRUE AND quality_metrics_commitment = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Quality Metrics Definition - Establish metrics framework and thresholds for each development project
- [PROC-02] Evidence Collection - Document and validate compliance with quality metrics at each gate
- [PROC-03] Vulnerability Assessment - Scan and assess delivered systems against CVSS thresholds
- [PROC-04] Contract Review - Ensure external developer agreements include quality metrics requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major security incidents, failed quality gates, contract violations, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Quality Metrics]
IF development_project = TRUE
AND project_start_date < (current_date - 30_days)
AND quality_metrics_defined = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delivered System with Vulnerabilities]
IF system_delivery = TRUE
AND vulnerability_scan_complete = TRUE
AND (cvss_medium_count > 0 OR cvss_high_count > 0)
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Quality Gate Without Evidence]
IF quality_gate_milestone = TRUE
AND gate_completion_claimed = TRUE
AND supporting_evidence = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: External Developer Non-Compliance]
IF developer_type = "external"
AND contract_active = TRUE
AND quality_metrics_evidence_provided = FALSE
AND evidence_due_date < current_date
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compiler Warnings Without Analysis]
IF code_compilation = TRUE
AND compiler_warnings > 0
AND security_impact_analysis = FALSE
AND quality_gate_passed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer required to define quality metrics at beginning of development process | RULE-01, RULE-05 |
| Developer required to provide evidence of meeting quality metrics | RULE-03 |
| Quality metrics include vulnerability severity thresholds | RULE-02 |
| Quality gates include compiler warning elimination or impact analysis | RULE-04 |