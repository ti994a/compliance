# POLICY: PM-30.1: Suppliers of Critical or Mission-essential Items

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-30.1 |
| NIST Control | PM-30.1: Suppliers of Critical or Mission-essential Items |
| Version | 1.0 |
| Owner | Chief Supply Chain Officer |
| Keywords | supplier assessment, critical suppliers, mission-essential, supply chain risk, vendor management |

## 1. POLICY STATEMENT
The organization SHALL identify, prioritize, and assess all suppliers of critical or mission-essential technologies, products, and services to ensure supply chain security and business continuity. This assessment process MUST be integrated with the organization's enterprise risk management framework and conducted using standardized supplier review processes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All suppliers | CONDITIONAL | Only those providing critical/mission-essential items |
| Cloud service providers | YES | All CSPs supporting critical systems |
| Software vendors | YES | Critical application and infrastructure software |
| Hardware vendors | YES | Network, server, and security equipment |
| Service providers | YES | Managed services for critical functions |
| Internal procurement teams | YES | All teams managing critical supplier relationships |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Officer | • Oversee supplier identification and prioritization process<br>• Approve critical supplier assessments<br>• Maintain enterprise supplier risk registry |
| Procurement Teams | • Identify suppliers of critical technologies/services<br>• Conduct initial supplier categorization<br>• Coordinate supplier assessment activities |
| Risk Management Office | • Define criticality criteria and assessment methodologies<br>• Review supplier risk assessments<br>• Monitor ongoing supplier risk posture |

## 4. RULES
[RULE-01] The organization MUST maintain a comprehensive inventory of all suppliers providing critical or mission-essential technologies, products, and services.
[VALIDATION] IF supplier_provides_critical_item = TRUE AND supplier_in_inventory = FALSE THEN violation

[RULE-02] Critical suppliers MUST be prioritized based on business impact, security risk, and availability requirements using a standardized scoring methodology.
[VALIDATION] IF supplier_criticality = "high" AND prioritization_score = NULL AND days_since_identification > 30 THEN violation

[RULE-03] All critical suppliers MUST undergo formal assessment within 90 days of identification and annually thereafter.
[VALIDATION] IF supplier_criticality = "critical" AND (last_assessment_date = NULL OR days_since_assessment > 365) THEN violation

[RULE-04] Supplier assessments MUST include security controls evaluation, financial stability review, and supply chain risk analysis.
[VALIDATION] IF assessment_completed = TRUE AND (security_review = FALSE OR financial_review = FALSE OR supply_chain_analysis = FALSE) THEN violation

[RULE-05] Assessment results MUST be documented and integrated into the enterprise risk management system within 15 days of completion.
[VALIDATION] IF assessment_completion_date + 15_days < current_date AND risk_system_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Supplier Identification - Process for categorizing suppliers based on criticality criteria
- [PROC-02] Supplier Prioritization Methodology - Standardized scoring system for supplier risk ranking  
- [PROC-03] Supplier Security Assessment - Comprehensive evaluation including controls testing
- [PROC-04] Supply Chain Risk Analysis - Assessment of multi-tier supplier dependencies
- [PROC-05] Continuous Monitoring - Ongoing surveillance of critical supplier risk posture

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when significant supply chain events occur
- Triggering events: Major supplier incidents, regulatory changes, business model changes, M&A activity

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Critical Cloud Provider]
IF supplier_type = "cloud_service_provider"
AND services_criticality = "mission_essential"
AND formal_assessment_completed = FALSE
AND days_since_contract_start > 90
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Overdue Supplier Reassessment]
IF supplier_criticality = "critical"
AND last_assessment_date + 365_days < current_date
AND assessment_extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incomplete Assessment Documentation]
IF supplier_assessment_status = "completed"
AND (security_controls_reviewed = FALSE OR financial_stability_assessed = FALSE)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Supplier Inventory Entry]
IF contract_value > 1000000
AND service_criticality = "mission_essential"
AND supplier_in_critical_inventory = FALSE
AND contract_active_days > 30
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Adequate Supplier Management]
IF supplier_criticality = "critical"
AND supplier_in_inventory = TRUE
AND last_assessment_date + 365_days >= current_date
AND risk_system_updated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Suppliers of critical technologies are identified | [RULE-01] |
| Suppliers of critical technologies are prioritized | [RULE-02] |
| Suppliers of critical technologies are assessed | [RULE-03], [RULE-04] |
| Assessment results are documented and tracked | [RULE-05] |