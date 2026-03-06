# POLICY: PM-30.1: Suppliers of Critical or Mission-essential Items

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-30.1 |
| NIST Control | PM-30.1: Suppliers of Critical or Mission-essential Items |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | supply chain, critical suppliers, mission-essential, supplier assessment, vendor management |

## 1. POLICY STATEMENT
The organization must identify, prioritize, and assess all suppliers providing critical or mission-essential technologies, products, and services to ensure supply chain security and business continuity. This assessment process enables targeted risk mitigation for high-impact supplier relationships.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All suppliers | CONDITIONAL | Only those providing critical/mission-essential items |
| Cloud service providers | YES | All cloud infrastructure and SaaS providers |
| Hardware vendors | YES | Servers, network equipment, security appliances |
| Software vendors | YES | Enterprise applications, security tools, development platforms |
| Critical service providers | YES | Managed services, consulting, maintenance |
| Non-critical vendors | NO | Office supplies, facilities, non-technical services |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee supplier risk assessment program<br>• Approve critical supplier classifications<br>• Review high-risk supplier assessments |
| Procurement Team | • Maintain supplier inventory<br>• Conduct initial supplier classifications<br>• Coordinate supplier assessments |
| Information Security | • Define security assessment criteria<br>• Review supplier security posture<br>• Validate security controls |
| Business Unit Owners | • Identify mission-critical dependencies<br>• Participate in supplier prioritization<br>• Define business impact criteria |

## 4. RULES
[RULE-01] The organization MUST maintain a comprehensive inventory of all suppliers providing technologies, products, or services to the organization.
[VALIDATION] IF supplier_provides_services = TRUE AND supplier_in_inventory = FALSE THEN violation

[RULE-02] Critical or mission-essential suppliers MUST be identified based on defined business impact criteria including system criticality, data sensitivity, and operational dependencies.
[VALIDATION] IF supplier_business_impact >= "HIGH" AND critical_classification = NULL THEN violation

[RULE-03] Critical suppliers MUST be prioritized using a risk-based approach considering business impact, security posture, and alternative availability.
[VALIDATION] IF supplier_classification = "critical" AND priority_score = NULL THEN violation

[RULE-04] All critical suppliers MUST undergo formal assessment within 90 days of classification and annually thereafter.
[VALIDATION] IF supplier_classification = "critical" AND days_since_assessment > 365 THEN violation

[RULE-05] Supplier assessments MUST include security reviews per SR-6 and supply chain risk assessments per RA-3(1).
[VALIDATION] IF supplier_assessment_complete = TRUE AND (security_review_complete = FALSE OR risk_assessment_complete = FALSE) THEN violation

[RULE-06] High-risk critical suppliers MUST have documented risk mitigation plans implemented within 60 days of assessment completion.
[VALIDATION] IF supplier_risk_level = "HIGH" AND supplier_classification = "critical" AND mitigation_plan_implemented = FALSE AND days_since_assessment > 60 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supplier Inventory Management - Maintain current database of all suppliers with service classifications
- [PROC-02] Critical Supplier Identification - Process for classifying suppliers based on business impact criteria
- [PROC-03] Supplier Risk Prioritization - Risk-based ranking methodology for critical suppliers
- [PROC-04] Supplier Security Assessment - Comprehensive evaluation including questionnaires, audits, and reviews
- [PROC-05] Supply Chain Risk Mitigation - Development and implementation of risk treatment plans

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supplier changes, significant security incidents, regulatory updates, merger/acquisition activities

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Cloud Provider]
IF service_type = "cloud_infrastructure"
AND business_impact = "HIGH"
AND assessment_completed = FALSE
AND days_since_onboarding > 90
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unassessed Critical Vendor]
IF supplier_classification = "critical"
AND last_assessment_date > 365_days_ago
AND assessment_in_progress = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: High-Risk Supplier Without Mitigation]
IF supplier_risk_score >= 7.0
AND supplier_classification = "critical"
AND mitigation_plan_status = "not_implemented"
AND days_since_assessment > 60
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Supplier Inventory Gap]
IF supplier_provides_services = TRUE
AND contract_value > 100000
AND supplier_in_inventory = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Critical Supplier]
IF supplier_classification = "critical"
AND last_assessment_date <= 365_days_ago
AND risk_mitigation_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Suppliers of critical technologies are identified | RULE-02 |
| Suppliers of critical technologies are prioritized | RULE-03 |
| Suppliers of critical technologies are assessed | RULE-04, RULE-05 |
| Supplier inventory is maintained | RULE-01 |
| Risk mitigation is implemented | RULE-06 |