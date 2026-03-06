# POLICY: SR-2: Supply Chain Risk Management Plan

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-2 |
| NIST Control | SR-2: Supply Chain Risk Management Plan |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, risk management, SCRM plan, vendor management, third-party risk, system lifecycle |

## 1. POLICY STATEMENT
The organization SHALL develop, maintain, and protect comprehensive supply chain risk management (SCRM) plans that address risks across the entire system development lifecycle from research and development through disposal. SCRM plans MUST be regularly reviewed and updated to address evolving threats and organizational changes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Critical and high-impact systems require detailed SCRM plans |
| System components | YES | Hardware, software, and firmware components |
| Third-party services | YES | Cloud services, managed services, SaaS applications |
| Vendors and suppliers | YES | Direct and indirect supply chain participants |
| Contractors | YES | Development, integration, and maintenance contractors |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve SCRM plans<br>• Define organizational risk tolerance<br>• Ensure plan protection and access controls |
| Supply Chain Risk Manager | • Develop and maintain SCRM plans<br>• Conduct supply chain risk assessments<br>• Monitor supplier performance |
| System Owners | • Implement system-specific SCRM requirements<br>• Report supply chain incidents<br>• Validate supplier compliance |
| Procurement Team | • Integrate SCRM requirements into contracts<br>• Conduct supplier due diligence<br>• Manage vendor relationships |

## 4. RULES

[RULE-01] Organizations MUST develop a comprehensive SCRM plan that addresses risks across all lifecycle phases: research and development, design, manufacturing, acquisition, delivery, integration, operations and maintenance, and disposal.
[VALIDATION] IF scrm_plan_exists = TRUE AND lifecycle_phases_covered >= 8 THEN compliant ELSE violation

[RULE-02] SCRM plans MUST be reviewed and updated at least annually or within 30 days of significant threat, organizational, or environmental changes.
[VALIDATION] IF last_review_date > 365_days OR (significant_change = TRUE AND update_date > change_date + 30_days) THEN violation

[RULE-03] SCRM plans SHALL be classified and protected from unauthorized disclosure and modification with appropriate access controls and encryption.
[VALIDATION] IF scrm_plan_classification = NULL OR access_controls = FALSE OR encryption = FALSE THEN violation

[RULE-04] SCRM plans MUST include documented risk tolerance levels, mitigation strategies, evaluation processes, and assigned roles and responsibilities.
[VALIDATION] IF risk_tolerance_documented = FALSE OR mitigation_strategies = FALSE OR evaluation_process = FALSE OR roles_assigned = FALSE THEN violation

[RULE-05] Critical and high-impact systems MUST have dedicated SCRM plans that cannot be incorporated into general security plans without explicit CISO approval.
[VALIDATION] IF system_impact >= "HIGH" AND (dedicated_scrm_plan = FALSE AND ciso_approval = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SCRM Plan Development - Standardized process for creating comprehensive supply chain risk management plans
- [PROC-02] Supply Chain Risk Assessment - Regular evaluation of supplier risks and threat landscape changes  
- [PROC-03] SCRM Plan Review and Update - Scheduled and event-driven plan maintenance procedures
- [PROC-04] Plan Protection and Access Control - Security measures for SCRM plan confidentiality and integrity
- [PROC-05] Supplier Risk Monitoring - Ongoing assessment of supplier performance and risk posture

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Major supply chain incidents, regulatory changes, significant organizational changes, new threat intelligence

## 7. SCENARIO PATTERNS

[SCENARIO-01: Missing Lifecycle Coverage]
IF scrm_plan_exists = TRUE
AND lifecycle_phases_covered < 8
AND system_impact = "HIGH"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Plan After Incident]
IF supply_chain_incident = TRUE
AND incident_date < current_date - 30_days  
AND scrm_plan_last_updated < incident_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unprotected SCRM Plan]
IF scrm_plan_contains_sensitive_info = TRUE
AND (access_controls = FALSE OR encryption_at_rest = FALSE)
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Generic Plan for Critical System]
IF system_classification = "CRITICAL"
AND scrm_plan_type = "GENERIC"
AND ciso_approval_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant SCRM Implementation]
IF scrm_plan_exists = TRUE
AND lifecycle_phases_covered = 8
AND last_review_date <= 365_days
AND access_controls = TRUE
AND risk_tolerance_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| SCRM plan development covering all lifecycle phases | RULE-01 |
| Regular plan review and updates | RULE-02 |
| Plan protection from unauthorized access | RULE-03 |
| Documented risk tolerance and mitigation strategies | RULE-04 |
| Dedicated plans for high-impact systems | RULE-05 |