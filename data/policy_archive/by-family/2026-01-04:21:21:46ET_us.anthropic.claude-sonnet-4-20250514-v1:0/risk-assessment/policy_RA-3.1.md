```markdown
# POLICY: RA-3.1: Supply Chain Risk Assessment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-3.1 |
| NIST Control | RA-3.1: Supply Chain Risk Assessment |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | supply chain, risk assessment, vendors, components, third-party, procurement |

## 1. POLICY STATEMENT
The organization SHALL conduct comprehensive supply chain risk assessments for all systems, components, and services to identify and mitigate risks from suppliers, vendors, and third-party dependencies. Supply chain risk assessments MUST be updated regularly and when significant changes occur to suppliers, systems, or operational environments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems | YES | Including cloud, on-premises, and hybrid |
| System components | YES | Hardware, software, firmware |
| Third-party services | YES | SaaS, managed services, outsourced functions |
| Internal development | YES | When using external components or libraries |
| Legacy systems | YES | Risk assessment required for continued operation |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee supply chain risk management program<br>• Approve risk assessment methodologies<br>• Review high-risk supplier assessments |
| Procurement Team | • Conduct supplier risk assessments before contracting<br>• Maintain supplier risk profiles<br>• Coordinate with security team on vendor evaluations |
| Security Team | • Define technical risk assessment criteria<br>• Review security aspects of supplier assessments<br>• Monitor threat intelligence for supply chain risks |
| System Owners | • Identify supply chain dependencies for their systems<br>• Participate in risk assessment processes<br>• Implement required supply chain risk mitigations |

## 4. RULES
[RULE-01] Supply chain risk assessments MUST be conducted for all new systems, components, and services before implementation or procurement.
[VALIDATION] IF new_system_component = TRUE AND risk_assessment_completed = FALSE THEN violation

[RULE-02] Supply chain risk assessments MUST be updated annually at minimum and within 30 days of significant supply chain changes.
[VALIDATION] IF last_assessment_date > 365_days OR (significant_change = TRUE AND update_within_30_days = FALSE) THEN violation

[RULE-03] Supply chain risk assessments MUST evaluate disruption risks, counterfeit components, malicious code insertion, and improper delivery practices.
[VALIDATION] IF assessment_scope NOT INCLUDES [disruption, counterfeits, malicious_code, delivery_practices] THEN violation

[RULE-04] High-risk suppliers MUST undergo enhanced due diligence including security assessments and continuous monitoring.
[VALIDATION] IF supplier_risk_rating = "HIGH" AND enhanced_due_diligence = FALSE THEN violation

[RULE-05] Supply chain risk assessment results MUST be documented and integrated into system risk management processes.
[VALIDATION] IF assessment_completed = TRUE AND (documentation = FALSE OR integration_with_system_risk = FALSE) THEN violation

[RULE-06] Critical system components from high-risk geographic regions MUST undergo additional security validation.
[VALIDATION] IF component_criticality = "HIGH" AND supplier_location IN high_risk_regions AND additional_validation = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment Methodology - Standardized process for evaluating supplier and component risks
- [PROC-02] Vendor Security Assessment - Security evaluation process for new and existing suppliers
- [PROC-03] Supply Chain Incident Response - Process for responding to supply chain security events
- [PROC-04] Continuous Supplier Monitoring - Ongoing monitoring of supplier risk profiles and threat intelligence

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supply chain incidents, new regulatory requirements, significant organizational changes, threat landscape changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Critical Vendor]
IF vendor_criticality = "HIGH"
AND risk_assessment_completed = FALSE
AND contract_signed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Assessment]
IF last_assessment_date > 365_days
AND system_criticality = "HIGH"
AND no_documented_extension = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Geographic Risk]
IF component_source = "high_risk_country"
AND component_criticality = "CRITICAL"
AND enhanced_validation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Supply Chain Change]
IF supplier_ownership_change = TRUE
AND change_date > 30_days_ago
AND reassessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Incomplete Assessment Scope]
IF assessment_exists = TRUE
AND malicious_code_evaluation = FALSE
AND counterfeit_evaluation = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Supply chain risks are assessed for systems, components, and services | [RULE-01], [RULE-03] |
| Risk assessments are updated at defined frequency | [RULE-02] |
| Assessments updated when significant changes occur | [RULE-02] |
| Assessment results are documented and integrated | [RULE-05] |
| High-risk suppliers receive enhanced scrutiny | [RULE-04], [RULE-06] |
```