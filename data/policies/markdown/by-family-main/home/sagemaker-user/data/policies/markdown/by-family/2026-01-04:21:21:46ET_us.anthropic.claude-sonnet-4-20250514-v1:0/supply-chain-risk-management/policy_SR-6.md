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
The organization SHALL conduct regular assessments and reviews of supply chain-related risks associated with suppliers, contractors, and the systems, components, or services they provide. These assessments MUST evaluate security processes, foreign ownership and control influences, and the supplier's ability to manage subordinate suppliers effectively.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All suppliers/contractors | YES | Providing systems, components, or services |
| Internal procurement teams | YES | Responsible for supplier management |
| Critical suppliers | YES | Enhanced assessment requirements |
| Low-risk suppliers | CONDITIONAL | Risk-based assessment frequency |
| Subcontractors (2nd/3rd tier) | YES | Through primary supplier evaluation |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Define supplier assessment frequency and criteria<br>• Approve supplier risk assessment methodology<br>• Oversee supplier review program |
| Supply Chain Risk Manager | • Conduct supplier risk assessments<br>• Monitor supplier security posture<br>• Coordinate with third-party assessment providers |
| Information Security Officer | • Define security requirements for supplier assessments<br>• Review security-related assessment findings<br>• Approve security controls for high-risk suppliers |

## 4. RULES
[RULE-01] All suppliers providing critical systems, components, or services MUST undergo comprehensive risk assessment before contract execution and at defined intervals thereafter.
[VALIDATION] IF supplier_criticality = "high" AND (initial_assessment = FALSE OR days_since_last_assessment > assessment_frequency) THEN violation

[RULE-02] Supplier assessments MUST evaluate security processes, foreign ownership/control/influence (FOCI), and the supplier's subordinate supplier management capabilities.
[VALIDATION] IF assessment_completed = TRUE AND (security_processes_evaluated = FALSE OR foci_evaluated = FALSE OR subordinate_supplier_mgmt_evaluated = FALSE) THEN violation

[RULE-03] Assessment frequency SHALL be defined based on supplier risk classification: Critical suppliers annually, High-risk suppliers every 2 years, Medium-risk suppliers every 3 years.
[VALIDATION] IF supplier_risk = "critical" AND days_since_assessment > 365 THEN violation
[VALIDATION] IF supplier_risk = "high" AND days_since_assessment > 730 THEN violation
[VALIDATION] IF supplier_risk = "medium" AND days_since_assessment > 1095 THEN violation

[RULE-04] Organizations MUST utilize open-source intelligence and publicly available information to monitor suppliers for security incidents, poor practices, or counterfeits.
[VALIDATION] IF supplier_monitoring_program = FALSE OR open_source_monitoring = FALSE THEN violation

[RULE-05] Assessment results MAY be shared with other organizations when required by applicable rules, policies, or agreements, with appropriate data protection controls.
[VALIDATION] IF assessment_sharing_required = TRUE AND sharing_controls_documented = FALSE THEN violation

[RULE-06] Third-party independent assessments MUST be conducted for suppliers providing services subject to FedRAMP or FISMA requirements.
[VALIDATION] IF (fedramp_applicable = TRUE OR fisma_applicable = TRUE) AND independent_assessment = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supplier Risk Classification - Process for categorizing suppliers based on criticality and risk
- [PROC-02] Supplier Security Assessment - Standardized assessment methodology and criteria
- [PROC-03] FOCI Evaluation - Process for assessing foreign ownership, control, and influence
- [PROC-04] Continuous Supplier Monitoring - Ongoing monitoring using open-source intelligence
- [PROC-05] Assessment Results Sharing - Procedures for sharing assessment information with authorized parties

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Major supply chain incidents, regulatory changes, new critical supplier onboarding

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Supplier Overdue Assessment]
IF supplier_risk_level = "critical"
AND days_since_last_assessment > 365
AND assessment_in_progress = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Assessment Components]
IF supplier_assessment_completed = TRUE
AND (foci_assessment = FALSE OR security_process_review = FALSE)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: FedRAMP Supplier Missing Independent Assessment]
IF supplier_provides_fedramp_service = TRUE
AND independent_third_party_assessment = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Sharing Assessment Without Controls]
IF assessment_results_shared = TRUE
AND data_protection_controls = FALSE
AND sharing_agreement_exists = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: New Critical Supplier Without Assessment]
IF supplier_criticality = "critical"
AND contract_execution_date <= current_date
AND pre_contract_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Supply chain risks assessed and reviewed | [RULE-01], [RULE-02] |
| Assessment frequency defined | [RULE-03] |
| Supplier security processes evaluated | [RULE-02] |
| FOCI assessment conducted | [RULE-02] |
| Subordinate supplier management assessed | [RULE-02] |
| Open-source monitoring implemented | [RULE-04] |
| Independent assessments for regulated services | [RULE-06] |