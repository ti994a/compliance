# POLICY: RA-3: Risk Assessment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-3 |
| NIST Control | RA-3: Risk Assessment |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | risk assessment, threat identification, vulnerability analysis, impact assessment, privacy impact, documentation |

## 1. POLICY STATEMENT
The organization SHALL conduct comprehensive risk assessments to identify threats and vulnerabilities, determine likelihood and magnitude of harm, and assess privacy impacts on individuals. Risk assessment results MUST be integrated across organizational levels, documented in security and privacy plans, and regularly reviewed and updated based on defined frequencies and significant changes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing organizational data |
| Cloud Services | YES | Including third-party and hybrid environments |
| Business Processes | YES | Mission-critical and support processes |
| PII Processing Activities | YES | All activities handling personal information |
| Contractors/Vendors | YES | Systems operated on behalf of organization |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Risk Officer | • Oversee enterprise risk assessment program<br>• Approve risk assessment methodologies<br>• Review and approve high-impact risk assessments |
| System Owners | • Conduct system-level risk assessments<br>• Document results in security/privacy plans<br>• Coordinate with organizational risk management |
| Risk Analysts | • Perform threat and vulnerability analysis<br>• Calculate likelihood and impact ratings<br>• Maintain risk assessment documentation |
| Privacy Officers | • Assess privacy impacts on individuals<br>• Ensure PII processing risks are evaluated<br>• Review privacy-related risk findings |

## 4. RULES
[RULE-01] Risk assessments MUST identify threats to and vulnerabilities in all in-scope systems and processes.
[VALIDATION] IF system_in_scope = TRUE AND (threats_identified = FALSE OR vulnerabilities_identified = FALSE) THEN violation

[RULE-02] Risk assessments MUST determine likelihood and magnitude of harm from unauthorized access, use, disclosure, disruption, modification, or destruction.
[VALIDATION] IF risk_assessment_exists = TRUE AND (likelihood_rating = NULL OR impact_rating = NULL) THEN violation

[RULE-03] Risk assessments MUST evaluate likelihood and impact of adverse effects on individuals from PII processing activities.
[VALIDATION] IF pii_processing = TRUE AND privacy_impact_assessment = FALSE THEN violation

[RULE-04] System-level risk assessments MUST integrate with organizational and mission/business process risk management decisions.
[VALIDATION] IF system_risk_assessment = TRUE AND organizational_integration = FALSE THEN violation

[RULE-05] Risk assessment results MUST be documented in security and privacy plans within 30 days of completion.
[VALIDATION] IF risk_assessment_completed = TRUE AND documentation_age > 30_days THEN violation

[RULE-06] Risk assessments MUST be reviewed at least annually and within 30 days of significant system changes.
[VALIDATION] IF last_review_date > 365_days OR (significant_change = TRUE AND review_date > change_date + 30_days) THEN violation

[RULE-07] Risk assessment results MUST be disseminated to designated personnel within 15 days of completion or update.
[VALIDATION] IF risk_assessment_updated = TRUE AND dissemination_date > completion_date + 15_days THEN violation

[RULE-08] Risk assessments MUST be updated when significant changes occur to systems, operational environment, or security/privacy posture.
[VALIDATION] IF significant_change = TRUE AND risk_assessment_updated = FALSE AND days_since_change > 60 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Risk Assessment Methodology - Standardized approach for conducting organizational, process, and system-level assessments
- [PROC-02] Threat Intelligence Integration - Process for incorporating current threat information into assessments
- [PROC-03] Vulnerability Assessment - Systematic identification and analysis of system vulnerabilities
- [PROC-04] Privacy Impact Assessment - Evaluation of risks to individuals from PII processing
- [PROC-05] Risk Assessment Documentation - Templates and requirements for documenting results
- [PROC-06] Risk Assessment Review and Update - Process for periodic review and change-triggered updates

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major regulatory changes, significant security incidents, organizational restructuring, new technology implementations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Privacy Impact Assessment]
IF system_processes_pii = TRUE
AND privacy_impact_assessment = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Risk Assessment After Major Change]
IF significant_system_change = TRUE
AND days_since_change > 60
AND risk_assessment_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Risk Assessment Not Integrated with Organizational Risk Management]
IF system_risk_assessment = TRUE
AND organizational_risk_integration = FALSE
AND system_criticality = "High"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Risk Assessment Results Not Disseminated]
IF risk_assessment_completed = TRUE
AND days_since_completion > 15
AND results_disseminated = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Annual Review Overdue]
IF last_risk_assessment_review > 365_days
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Risk assessment identifies threats and vulnerabilities | [RULE-01] |
| Risk assessment determines likelihood and magnitude of harm | [RULE-02] |
| Risk assessment evaluates privacy impacts on individuals | [RULE-03] |
| Risk assessments integrated across organizational levels | [RULE-04] |
| Risk assessment results documented in security/privacy plans | [RULE-05] |
| Risk assessment results reviewed per defined frequency | [RULE-06] |
| Risk assessment results disseminated to designated personnel | [RULE-07] |
| Risk assessment updated per defined frequency or significant changes | [RULE-08] |