# POLICY: PL-10: Baseline Selection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PL-10 |
| NIST Control | PL-10: Baseline Selection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | baseline, control selection, FISMA, system categorization, risk assessment, stakeholder requirements |

## 1. POLICY STATEMENT
All information systems MUST have an appropriate NIST SP 800-53 control baseline selected based on system categorization, stakeholder needs, and regulatory requirements. The baseline selection SHALL be documented and justified based on mission requirements, business needs, and applicable legal/regulatory mandates.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Information Systems | YES | FISMA compliance required |
| Cloud Services | YES | Including FedRAMP authorized services |
| Development Systems | YES | Must align with production baseline |
| Legacy Systems | YES | Baseline required within 90 days |
| Third-party Systems | CONDITIONAL | When processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Select appropriate baseline for system<br>• Document baseline selection rationale<br>• Ensure stakeholder needs assessment |
| CISO | • Approve baseline selections<br>• Maintain baseline selection procedures<br>• Oversee compliance monitoring |
| Risk Manager | • Validate baseline aligns with risk assessment<br>• Review impact analysis supporting selection<br>• Approve risk-based deviations |

## 4. RULES
[RULE-01] System owners MUST select a control baseline from NIST SP 800-53B that corresponds to the system's security categorization level.
[VALIDATION] IF system_categorization = "Low" AND baseline != "Low" THEN violation
[VALIDATION] IF system_categorization = "Moderate" AND baseline != "Moderate" THEN violation  
[VALIDATION] IF system_categorization = "High" AND baseline != "High" THEN violation

[RULE-02] Baseline selection MUST be completed within 30 days of system categorization and documented in the System Security Plan.
[VALIDATION] IF categorization_date + 30_days < current_date AND baseline_selected = FALSE THEN violation

[RULE-03] Organizations MUST conduct stakeholder needs analysis prior to baseline selection to identify mission, business, and regulatory requirements.
[VALIDATION] IF baseline_selected = TRUE AND stakeholder_analysis_completed = FALSE THEN violation

[RULE-04] Baseline selection MUST consider applicable regulatory requirements including FISMA, FedRAMP, SOX, and PCI-DSS where relevant.
[VALIDATION] IF regulatory_scope != "none" AND regulatory_requirements_considered = FALSE THEN violation

[RULE-05] System owners MUST document the rationale for baseline selection including risk assessment results and business impact analysis.
[VALIDATION] IF baseline_selected = TRUE AND selection_rationale_documented = FALSE THEN violation

[RULE-06] Alternative baseline selections MUST be approved by the CISO and Risk Manager when deviating from standard categorization mapping.
[VALIDATION] IF baseline_deviation = TRUE AND (ciso_approval = FALSE OR risk_manager_approval = FALSE) THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Stakeholder Needs Assessment - Process for identifying mission, business, and regulatory requirements
- [PROC-02] Baseline Selection Decision Matrix - Framework for mapping requirements to appropriate baselines
- [PROC-03] Baseline Deviation Approval - Process for requesting and approving non-standard baseline selections
- [PROC-04] Baseline Documentation - Requirements for documenting selection rationale in security plans

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: New regulatory requirements, significant system changes, security incidents affecting baseline adequacy

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Low Impact System]
IF system_categorization = "Low"
AND regulatory_requirements = "FISMA only"
AND baseline_selected = "Low"
AND stakeholder_analysis_completed = TRUE
THEN compliance = TRUE

[SCENARIO-02: High Impact System with Inadequate Baseline]
IF system_categorization = "High"
AND baseline_selected = "Moderate"
AND ciso_approval = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Multi-Regulatory Environment]
IF regulatory_scope = ["FISMA", "FedRAMP", "SOX"]
AND baseline_selected = "Moderate"
AND regulatory_requirements_considered = TRUE
AND selection_rationale_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Undocumented Baseline Selection]
IF baseline_selected = TRUE
AND selection_rationale_documented = FALSE
AND days_since_selection > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Delayed Baseline Selection]
IF system_categorization_date + 45_days < current_date
AND baseline_selected = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Control baseline selected for system | RULE-01, RULE-02 |
| Selection based on system categorization | RULE-01 |
| Stakeholder needs considered | RULE-03 |
| Regulatory requirements addressed | RULE-04 |
| Selection rationale documented | RULE-05 |
| Appropriate approvals obtained | RULE-06 |