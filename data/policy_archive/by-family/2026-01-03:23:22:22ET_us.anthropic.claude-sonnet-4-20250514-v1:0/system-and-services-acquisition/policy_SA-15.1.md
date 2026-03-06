# POLICY: SA-15.1: Quality Metrics

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-15.1 |
| NIST Control | SA-15.1: Quality Metrics |
| Version | 1.0 |
| Owner | Chief Information Officer |
| Keywords | quality metrics, development process, developer requirements, security standards, vulnerability thresholds |

## 1. POLICY STATEMENT
All system, system component, and system service developers MUST define quality metrics at the beginning of the development process and provide documented evidence of meeting these metrics. Quality metrics SHALL include security and privacy capability requirements with measurable completion criteria and vulnerability severity thresholds aligned with organizational risk tolerance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All systems and components developed internally |
| External Vendors/Contractors | YES | All contracted development work |
| COTS Software | CONDITIONAL | When customization or integration development occurs |
| Cloud Service Providers | YES | Custom development or significant configuration |
| Third-party Integrators | YES | System integration and custom development work |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Define quality metrics at project initiation<br>• Implement quality gates throughout development<br>• Provide evidence of metric compliance<br>• Remediate identified quality deficiencies |
| Procurement Office | • Include quality metric requirements in contracts<br>• Validate developer quality metric definitions<br>• Monitor compliance with quality requirements<br>• Enforce contractual quality obligations |
| Security Team | • Define security-specific quality requirements<br>• Review vulnerability severity thresholds<br>• Validate security quality evidence<br>• Approve quality metric exceptions |

## 4. RULES
[RULE-01] Developers MUST define quality metrics within 30 days of project initiation and before any development work begins.
[VALIDATION] IF development_start_date > project_initiation_date AND quality_metrics_defined = FALSE THEN violation

[RULE-02] Quality metrics MUST include vulnerability severity thresholds with no known vulnerabilities having CVSS scores of 7.0 or higher in delivered systems.
[VALIDATION] IF delivered_system_vulnerabilities.cvss_score >= 7.0 AND vulnerability_count > 0 THEN critical_violation

[RULE-03] Developers SHALL provide documented evidence of meeting all defined quality metrics before system delivery or deployment.
[VALIDATION] IF system_delivery_approved = TRUE AND quality_evidence_provided = FALSE THEN violation

[RULE-04] Quality gates MUST be established for each major development phase with clear completion criteria and sufficiency standards.
[VALIDATION] IF development_phase_complete = TRUE AND quality_gate_criteria_met = FALSE THEN violation

[RULE-05] All compiler warnings MUST be eliminated or documented as having no impact on required security or privacy capabilities.
[VALIDATION] IF compiler_warnings > 0 AND (warnings_eliminated = FALSE AND impact_assessment_documented = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Quality Metrics Definition Process - Standardized process for defining and documenting quality metrics at project initiation
- [PROC-02] Quality Gate Implementation - Procedures for implementing and validating quality gates throughout development lifecycle
- [PROC-03] Evidence Collection and Documentation - Process for collecting, documenting, and validating quality metric compliance evidence
- [PROC-04] Vulnerability Assessment and Remediation - Procedures for identifying, assessing, and remediating security vulnerabilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Major security incidents, failed quality assessments, regulatory changes, significant development methodology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Quality Metrics]
IF project_status = "active"
AND development_started = TRUE
AND quality_metrics_defined = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: High CVSS Vulnerability in Delivery]
IF system_delivery_pending = TRUE
AND vulnerability_scan_complete = TRUE
AND max_cvss_score >= 7.0
AND remediation_complete = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Quality Gate Bypass]
IF development_phase = "completed"
AND quality_gate_defined = TRUE
AND quality_criteria_met = FALSE
AND management_override = TRUE AND override_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Contractor Without Quality Evidence]
IF vendor_type = "external_developer"
AND contract_includes_quality_requirements = TRUE
AND delivery_date <= current_date
AND quality_evidence_submitted = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Acceptable Compiler Warning Documentation]
IF compiler_warnings_present = TRUE
AND warnings_count > 0
AND security_impact_assessment = "no_impact"
AND assessment_documented = TRUE
AND security_team_approved = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer defines quality metrics at beginning of development | [RULE-01] |
| Developer provides evidence of meeting quality metrics | [RULE-03] |
| Quality gates with completion criteria established | [RULE-04] |
| Vulnerability severity thresholds defined and enforced | [RULE-02] |
| Compiler warnings addressed appropriately | [RULE-05] |