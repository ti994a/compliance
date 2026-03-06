# POLICY: SR-2: Supply Chain Risk Management Plan

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-2 |
| NIST Control | SR-2: Supply Chain Risk Management Plan |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, risk management, SCRM, vendor management, third-party risk, procurement |

## 1. POLICY STATEMENT
The organization SHALL develop, maintain, and protect comprehensive supply chain risk management (SCRM) plans that address risks across the entire system lifecycle from research and development through disposal. These plans MUST be regularly reviewed and updated to address evolving threats and organizational changes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems | YES | Including cloud, on-premises, and hybrid |
| System components | YES | Hardware, software, firmware |
| Third-party services | YES | SaaS, PaaS, IaaS providers |
| Contractors/vendors | YES | All supply chain participants |
| Development teams | YES | Internal and external development |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve SCRM plans<br>• Define risk tolerance<br>• Oversee plan protection |
| Procurement Officer | • Implement SCRM requirements in contracts<br>• Conduct supplier assessments<br>• Monitor vendor compliance |
| System Owner | • Develop system-specific SCRM plans<br>• Coordinate with suppliers<br>• Report supply chain incidents |

## 4. RULES

[RULE-01] Organizations MUST develop a comprehensive SCRM plan for all systems, system components, and services that addresses risks across all lifecycle phases: research and development, design, manufacturing, acquisition, delivery, integration, operations and maintenance, and disposal.
[VALIDATION] IF system_in_scope = TRUE AND scrm_plan_exists = FALSE THEN violation

[RULE-02] SCRM plans MUST be reviewed and updated at least annually or immediately when threat, organizational, or environmental changes occur.
[VALIDATION] IF last_review_date > 365_days OR (threat_change = TRUE AND plan_updated = FALSE) THEN violation

[RULE-03] SCRM plans SHALL be classified and protected from unauthorized disclosure and modification with appropriate access controls and encryption.
[VALIDATION] IF scrm_plan_classification = NULL OR access_controls = FALSE THEN violation

[RULE-04] SCRM plans MUST include explicit risk tolerance statements, mitigation strategies, evaluation processes, implementation approaches, and defined roles and responsibilities.
[VALIDATION] IF missing_required_elements > 0 THEN violation

[RULE-05] All suppliers and vendors MUST be assessed for supply chain risks before contract execution and periodically thereafter based on risk level.
[VALIDATION] IF supplier_assessment_date = NULL OR (high_risk_supplier = TRUE AND assessment_age > 180_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SCRM Plan Development - Standardized process for creating lifecycle-specific risk management plans
- [PROC-02] Supplier Risk Assessment - Due diligence procedures for evaluating supply chain partners
- [PROC-03] Plan Review and Update - Regular review cycles and change-triggered updates
- [PROC-04] Incident Response Integration - Procedures for supply chain security incidents
- [PROC-05] Plan Protection - Classification, handling, and access control procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supply chain incidents, regulatory changes, significant vendor changes, threat landscape evolution

## 7. SCENARIO PATTERNS

[SCENARIO-01: Missing SCRM Plan]
IF system_criticality = "high"
AND scrm_plan_exists = FALSE
AND system_age > 90_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Plan During Threat Change]
IF threat_intelligence_update = TRUE
AND scrm_plan_last_updated > threat_update_date
AND days_since_threat_update > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unauthorized Plan Access]
IF scrm_plan_accessed = TRUE
AND user_authorization = FALSE
AND access_logged = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Unassessed High-Risk Supplier]
IF supplier_risk_level = "high"
AND last_assessment_date > 180_days
AND active_contract = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Incomplete Plan Elements]
IF scrm_plan_exists = TRUE
AND (risk_tolerance_defined = FALSE OR mitigation_strategies = FALSE OR roles_defined = FALSE)
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| SCRM plan development for all lifecycle phases | RULE-01 |
| Regular plan review and updates | RULE-02 |
| Plan protection from unauthorized access | RULE-03 |
| Required plan elements and content | RULE-04 |
| Supplier risk assessment requirements | RULE-05 |