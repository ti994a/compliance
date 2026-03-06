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
All information systems MUST have an appropriate NIST SP 800-53 control baseline selected based on system categorization, stakeholder needs, and regulatory requirements. The baseline selection MUST be documented and justified with consideration of mission requirements, business needs, and applicable legal mandates.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, on-premises, and hybrid |
| Development Systems | YES | Must select appropriate baseline for environment |
| Third-party Systems | CONDITIONAL | When processing organizational data |
| Personal Devices | CONDITIONAL | When accessing organizational systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Initiate baseline selection process<br>• Approve final baseline selection<br>• Ensure stakeholder needs are identified |
| CISO/Security Team | • Validate baseline selection methodology<br>• Review and approve baseline selections<br>• Maintain baseline selection procedures |
| Risk Management | • Conduct system categorization<br>• Perform risk assessments<br>• Validate baseline adequacy for risk profile |

## 4. RULES
[RULE-01] Every information system MUST have a control baseline selected from NIST SP 800-53B or equivalent approved framework within 30 days of system categorization completion.
[VALIDATION] IF system_categorized = TRUE AND baseline_selected = FALSE AND days_since_categorization > 30 THEN violation

[RULE-02] Baseline selection MUST be based on completed system categorization (FIPS 199), stakeholder needs analysis, and applicable regulatory requirements.
[VALIDATION] IF baseline_selected = TRUE AND (system_categorization = NULL OR stakeholder_analysis = NULL) THEN violation

[RULE-03] Systems processing Federal information MUST select baselines from NIST SP 800-53B (Low, Moderate, or High) unless alternative baselines are formally approved by the AO.
[VALIDATION] IF federal_data = TRUE AND baseline_source != "SP800-53B" AND ao_approval = FALSE THEN violation

[RULE-04] Baseline selection decisions MUST be documented with justification including system categorization results, stakeholder requirements, and regulatory mandates.
[VALIDATION] IF baseline_selected = TRUE AND documentation_complete = FALSE THEN violation

[RULE-05] National security systems MUST follow CNSSI-1253 guidance for baseline selection unless exempted by appropriate authority.
[VALIDATION] IF system_type = "national_security" AND baseline_guidance != "CNSSI-1253" AND exemption_approved = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Categorization Process - Systematic approach to determine system impact levels
- [PROC-02] Stakeholder Needs Analysis - Process to identify and document stakeholder security requirements
- [PROC-03] Baseline Selection Methodology - Step-by-step process for selecting appropriate baselines
- [PROC-04] Baseline Documentation Standards - Required documentation format and content

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when NIST updates SP 800-53
- Triggering events: New regulatory requirements, significant organizational changes, major security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Moderate Impact System]
IF system_categorization = "Moderate"
AND federal_data = TRUE
AND baseline_selected = "SP800-53B Moderate"
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-02: High Impact System with Custom Baseline]
IF system_categorization = "High"
AND baseline_selected = "Custom"
AND ao_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Cloud System Missing Categorization]
IF system_type = "cloud"
AND baseline_selected = TRUE
AND system_categorization = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: National Security System Non-Compliance]
IF system_type = "national_security"
AND baseline_guidance != "CNSSI-1253"
AND exemption_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Delayed Baseline Selection]
IF system_categorized = TRUE
AND days_since_categorization > 30
AND baseline_selected = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Control baseline for system is selected | RULE-01, RULE-02 |
| Selection based on system categorization | RULE-02 |
| Federal baseline compliance | RULE-03 |
| Documentation requirements | RULE-04 |
| National security system compliance | RULE-05 |