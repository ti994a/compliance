# POLICY: RA-3.1: Supply Chain Risk Assessment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-3.1 |
| NIST Control | RA-3.1: Supply Chain Risk Assessment |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | supply chain, risk assessment, vendor management, third-party risk, component security |

## 1. POLICY STATEMENT
The organization SHALL conduct comprehensive supply chain risk assessments for all systems, system components, and system services to identify and evaluate potential security threats throughout the supply chain lifecycle. These assessments MUST be updated regularly and whenever significant changes occur to the supply chain, systems, or operational environment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, and hybrid |
| System Components | YES | Hardware, software, firmware |
| Third-Party Services | YES | SaaS, PaaS, IaaS providers |
| Vendors/Suppliers | YES | Direct and indirect suppliers |
| Internal Development | YES | Custom applications and components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee supply chain risk assessment program<br>• Approve risk assessment methodologies<br>• Review high-risk findings |
| Procurement Manager | • Conduct vendor risk assessments<br>• Maintain supplier risk profiles<br>• Coordinate with security team on acquisitions |
| System Owners | • Identify system components and dependencies<br>• Provide input on operational impacts<br>• Implement risk mitigation measures |

## 4. RULES
[RULE-01] Supply chain risk assessments MUST be conducted for all systems, system components, and system services before implementation or procurement.
[VALIDATION] IF system_deployed = TRUE AND supply_chain_assessment_completed = FALSE THEN critical_violation

[RULE-02] Supply chain risk assessments SHALL be updated annually at minimum.
[VALIDATION] IF last_assessment_date > 365_days AND no_update_completed = TRUE THEN violation

[RULE-03] Supply chain risk assessments MUST be updated within 30 days when significant changes occur to the supply chain, system, or operational environment.
[VALIDATION] IF significant_change_date > 30_days AND assessment_not_updated = TRUE THEN violation

[RULE-04] Supply chain risk assessments SHALL evaluate risks including disruption, defective components, counterfeits, theft, malicious development practices, improper delivery, and malicious code insertion.
[VALIDATION] IF assessment_scope_incomplete = TRUE AND required_risk_categories_missing > 0 THEN violation

[RULE-05] High-risk supply chain findings MUST be documented with specific mitigation plans and timelines not exceeding 90 days.
[VALIDATION] IF risk_level = "HIGH" AND mitigation_plan_missing = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment Methodology - Standardized approach for evaluating supplier and component risks
- [PROC-02] Vendor Security Evaluation Process - Due diligence procedures for new and existing vendors
- [PROC-03] Component Integrity Verification - Methods for validating authenticity and security of system components
- [PROC-04] Supply Chain Incident Response - Procedures for responding to supply chain security events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supply chain incidents, regulatory changes, significant vendor changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Critical Vendor Onboarding]
IF vendor_criticality = "HIGH"
AND supply_chain_assessment = "NOT_COMPLETED"
AND system_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Outdated Assessment Update]
IF last_assessment_date > 365_days
AND significant_changes_occurred = TRUE
AND assessment_update_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: High-Risk Finding Without Mitigation]
IF risk_rating = "HIGH"
AND finding_age > 90_days
AND mitigation_plan_status = "NOT_IMPLEMENTED"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Component Source Verification]
IF component_type = "CRITICAL_HARDWARE"
AND source_verification = "NOT_PERFORMED"
AND authenticity_validated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Supply Chain Change Management]
IF supplier_change_occurred = TRUE
AND change_significance = "MAJOR"
AND reassessment_completed_within_30_days = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Supply chain risks are assessed for systems, components, and services | [RULE-01], [RULE-04] |
| Assessment frequency is defined and followed | [RULE-02] |
| Assessments updated based on significant changes | [RULE-03] |
| Risk mitigation plans are documented and implemented | [RULE-05] |