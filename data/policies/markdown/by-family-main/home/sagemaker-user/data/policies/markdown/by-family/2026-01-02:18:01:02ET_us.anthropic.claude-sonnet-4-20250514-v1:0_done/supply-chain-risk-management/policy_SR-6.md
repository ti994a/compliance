# POLICY: SR-6: Supplier Assessments and Reviews

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-6 |
| NIST Control | SR-6: Supplier Assessments and Reviews |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | supplier assessment, supply chain risk, vendor review, third-party risk, contractor evaluation |

## 1. POLICY STATEMENT
The organization SHALL conduct comprehensive assessments and reviews of supply chain-related risks associated with all suppliers, contractors, and the systems, components, or services they provide. These assessments MUST be performed at defined frequencies and include evaluation of security processes, foreign ownership/control/influence, and subordinate supplier management capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All suppliers/contractors | YES | Providing systems, components, or services |
| Internal procurement teams | YES | Conducting assessments and reviews |
| Third-party assessors | YES | When performing independent reviews |
| Second/third-tier suppliers | YES | Through primary supplier evaluation |
| One-time vendors | CONDITIONAL | If providing critical/sensitive services |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Define assessment frequencies and criteria<br>• Approve supplier risk tolerance levels<br>• Oversee third-party assessment programs |
| Supply Chain Risk Manager | • Conduct supplier risk assessments<br>• Monitor open-source intelligence on suppliers<br>• Maintain supplier risk registers |
| Information Security Officer | • Define security requirements for assessments<br>• Review security-related findings<br>• Approve security exceptions |

## 4. RULES
[RULE-01] All suppliers providing systems, components, or services MUST undergo initial supply chain risk assessment before contract execution.
[VALIDATION] IF supplier_status = "new" AND contract_executed = TRUE AND initial_assessment_completed = FALSE THEN violation

[RULE-02] Supplier assessments MUST be reviewed and updated annually for standard suppliers and semi-annually for critical/high-risk suppliers.
[VALIDATION] IF supplier_risk_level = "critical" AND last_review_date > 6_months THEN violation
[VALIDATION] IF supplier_risk_level = "standard" AND last_review_date > 12_months THEN violation

[RULE-03] Assessments MUST evaluate security processes, foreign ownership/control/influence (FOCI), and supplier's ability to manage subordinate suppliers.
[VALIDATION] IF assessment_completed = TRUE AND (security_processes_evaluated = FALSE OR foci_evaluated = FALSE OR subordinate_supplier_management_evaluated = FALSE) THEN violation

[RULE-04] Organizations MUST utilize open-source intelligence and publicly available information to monitor suppliers for security incidents, counterfeits, or poor practices.
[VALIDATION] IF supplier_monitoring_enabled = FALSE OR last_osint_review > 90_days THEN violation

[RULE-05] High-risk findings from supplier assessments MUST be documented and addressed within 30 days of identification.
[VALIDATION] IF finding_risk_level = "high" AND finding_age > 30_days AND mitigation_status != "completed" THEN violation

[RULE-06] Third-party independent reviews MUST be conducted for suppliers supporting FedRAMP or FISMA systems at least every 24 months.
[VALIDATION] IF system_classification IN ["FedRAMP", "FISMA"] AND independent_review_date > 24_months THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supplier Risk Assessment Methodology - Standardized process for evaluating supply chain risks
- [PROC-02] Open Source Intelligence Monitoring - Continuous monitoring of supplier-related threat intelligence
- [PROC-03] FOCI Evaluation Process - Assessment of foreign ownership, control, or influence risks
- [PROC-04] Third-Party Assessment Management - Oversight of independent supplier reviews
- [PROC-05] Risk Finding Remediation - Process for addressing and tracking assessment findings

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supply chain incidents, regulatory changes, significant supplier changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Critical Supplier Onboarding]
IF supplier_type = "new"
AND service_criticality = "high"
AND initial_assessment_completed = FALSE
AND contract_execution_pending = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Overdue Supplier Review]
IF supplier_risk_level = "critical"
AND last_assessment_date > 6_months
AND review_extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: FOCI Supplier Without Enhanced Review]
IF foci_status = "identified"
AND enhanced_security_review_completed = FALSE
AND system_classification IN ["FedRAMP", "FISMA"]
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Open Source Intelligence Alert]
IF osint_alert_received = TRUE
AND alert_severity = "high"
AND investigation_initiated = FALSE
AND alert_age > 5_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Subordinate Supplier Risk]
IF primary_supplier_assessment = "completed"
AND subordinate_supplier_evaluation = "inadequate"
AND risk_mitigation_plan = "not_developed"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Supply chain risks are assessed and reviewed | [RULE-01], [RULE-02] |
| Assessment frequency is defined and followed | [RULE-02] |
| Security processes are evaluated | [RULE-03] |
| FOCI is assessed | [RULE-03] |
| Subordinate supplier management is evaluated | [RULE-03] |
| Open-source monitoring is conducted | [RULE-04] |
| Findings are remediated timely | [RULE-05] |
| Independent reviews are performed when required | [RULE-06] |