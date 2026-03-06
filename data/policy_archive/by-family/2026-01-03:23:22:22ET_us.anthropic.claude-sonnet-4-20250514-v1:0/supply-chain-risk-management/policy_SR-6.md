# POLICY: SR-6: Supplier Assessments and Reviews

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-6 |
| NIST Control | SR-6: Supplier Assessments and Reviews |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | supplier assessment, supply chain risk, contractor review, third-party risk, vendor management |

## 1. POLICY STATEMENT
The organization SHALL conduct regular assessments and reviews of supply chain-related risks associated with suppliers, contractors, and the systems, components, or services they provide. These assessments MUST evaluate security processes, foreign ownership/control/influence, and the supplier's ability to manage subordinate suppliers.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All suppliers/contractors | YES | Providing systems, components, or services |
| Internal procurement teams | YES | Responsible for conducting assessments |
| Third-party assessors | CONDITIONAL | When independent reviews required |
| Subordinate suppliers | YES | Second-tier and third-tier suppliers |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Define assessment frequency and criteria<br>• Approve supplier risk assessments<br>• Oversee supplier review program |
| Supply Chain Risk Manager | • Conduct supplier risk assessments<br>• Monitor open-source intelligence<br>• Document assessment results<br>• Coordinate with security teams |
| Information Security Officer | • Define security requirements for assessments<br>• Review security-related findings<br>• Validate supplier security controls |

## 4. RULES
[RULE-01] Organizations MUST assess supply chain-related risks for all suppliers and contractors providing systems, system components, or system services.
[VALIDATION] IF supplier_provides_services = TRUE AND risk_assessment_completed = FALSE THEN violation

[RULE-02] Supplier assessments MUST be conducted at organization-defined frequencies, with high-risk suppliers assessed annually and standard suppliers assessed every three years.
[VALIDATION] IF supplier_risk_level = "high" AND last_assessment_age > 365_days THEN violation
[VALIDATION] IF supplier_risk_level = "standard" AND last_assessment_age > 1095_days THEN violation

[RULE-03] Assessments MUST evaluate supplier security processes, foreign ownership/control/influence (FOCI), and ability to manage subordinate suppliers.
[VALIDATION] IF assessment_includes_security_processes = FALSE OR assessment_includes_foci = FALSE OR assessment_includes_subordinate_management = FALSE THEN violation

[RULE-04] Organizations MUST use documented processes, controls assessment, all-source intelligence, and publicly available information in supplier reviews.
[VALIDATION] IF assessment_sources < 3 OR documented_process_used = FALSE THEN violation

[RULE-05] Critical supplier assessments MUST be conducted by independent third parties or include independent validation.
[VALIDATION] IF supplier_criticality = "critical" AND independent_assessment = FALSE THEN violation

[RULE-06] Assessment results MUST be documented and shared with relevant stakeholders according to applicable agreements and security requirements.
[VALIDATION] IF assessment_documented = FALSE OR stakeholder_notification = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supplier Risk Assessment - Standardized process for evaluating supplier risks
- [PROC-02] FOCI Evaluation - Process for assessing foreign ownership, control, or influence
- [PROC-03] Open Source Intelligence Monitoring - Continuous monitoring of public information
- [PROC-04] Third-Party Assessment Coordination - Managing independent supplier reviews
- [PROC-05] Assessment Results Documentation - Recording and sharing assessment findings

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: New regulatory requirements, significant supply chain incidents, changes in threat landscape

## 7. SCENARIO PATTERNS
[SCENARIO-01: Overdue High-Risk Supplier Assessment]
IF supplier_risk_level = "high"
AND last_assessment_date < (current_date - 365_days)
AND active_contract = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Assessment Scope]
IF supplier_assessment_completed = TRUE
AND (foci_evaluation = FALSE OR subordinate_supplier_review = FALSE)
AND supplier_provides_critical_services = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Independent Review for Critical Supplier]
IF supplier_criticality = "critical"
AND contract_value > 10000000
AND independent_assessment = FALSE
AND assessment_age < 180_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Undocumented Assessment Results]
IF supplier_assessment_completed = TRUE
AND assessment_documentation = FALSE
AND assessment_completion_date < (current_date - 30_days)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Standard Supplier Within Assessment Window]
IF supplier_risk_level = "standard"
AND last_assessment_date > (current_date - 1095_days)
AND assessment_includes_all_required_elements = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Supply chain risks are assessed and reviewed | [RULE-01] |
| Assessment frequency is defined and followed | [RULE-02] |
| Assessments include security processes and FOCI | [RULE-03] |
| Multiple information sources are used | [RULE-04] |
| Independent reviews for critical suppliers | [RULE-05] |
| Results are documented and shared | [RULE-06] |