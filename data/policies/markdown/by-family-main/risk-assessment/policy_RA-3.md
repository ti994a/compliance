# POLICY: RA-3: Risk Assessment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-3 |
| NIST Control | RA-3: Risk Assessment |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | risk assessment, threat identification, vulnerability analysis, impact assessment, privacy risk |

## 1. POLICY STATEMENT
The organization SHALL conduct comprehensive risk assessments to identify threats and vulnerabilities in systems, determine likelihood and magnitude of harm from security incidents, and assess privacy risks to individuals. Risk assessment results MUST be integrated across organizational levels, documented in security and privacy plans, and regularly reviewed and updated.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All production, development, and test systems |
| Cloud Services | YES | Including third-party and hybrid cloud environments |
| Mobile Applications | YES | Both corporate and BYOD applications |
| Third-party Integrations | YES | APIs, data feeds, and service providers |
| Legacy Systems | YES | Including systems pending decommission |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Risk Manager | • Oversee enterprise risk assessment program<br>• Ensure integration across organizational levels<br>• Review and approve risk assessment methodologies |
| System Owners | • Conduct system-level risk assessments<br>• Document results in security and privacy plans<br>• Coordinate with business stakeholders on risk decisions |
| Security Team | • Perform technical vulnerability assessments<br>• Analyze threat intelligence and attack vectors<br>• Support risk assessment methodology development |
| Privacy Officer | • Assess privacy risks from PII processing<br>• Evaluate impact on individuals<br>• Ensure privacy risk integration with security assessments |

## 4. RULES
[RULE-01] Risk assessments MUST identify threats to and vulnerabilities in all in-scope systems using approved methodologies and current threat intelligence.
[VALIDATION] IF system_in_scope = TRUE AND risk_assessment_conducted = FALSE THEN violation

[RULE-02] Risk assessments MUST determine likelihood and magnitude of harm from unauthorized access, use, disclosure, disruption, modification, or destruction of systems and data.
[VALIDATION] IF risk_assessment_exists = TRUE AND (likelihood_analysis = FALSE OR impact_analysis = FALSE) THEN violation

[RULE-03] Risk assessments MUST evaluate likelihood and impact of adverse effects on individuals from PII processing activities.
[VALIDATION] IF system_processes_pii = TRUE AND privacy_risk_assessment = FALSE THEN violation

[RULE-04] System-level risk assessments MUST integrate with organizational and mission/business process risk management decisions.
[VALIDATION] IF system_risk_assessment = TRUE AND organizational_integration = FALSE THEN violation

[RULE-05] Risk assessment results MUST be documented in system security plans and privacy plans within 30 days of completion.
[VALIDATION] IF risk_assessment_complete_date + 30_days < current_date AND documentation_complete = FALSE THEN violation

[RULE-06] Risk assessments MUST be reviewed at least annually and within 30 days of significant system changes.
[VALIDATION] IF last_review_date + 365_days < current_date THEN violation
[VALIDATION] IF significant_change_date + 30_days < current_date AND risk_assessment_updated = FALSE THEN violation

[RULE-07] Risk assessment results MUST be disseminated to system owners, authorizing officials, and relevant stakeholders within 15 days of completion.
[VALIDATION] IF risk_assessment_complete_date + 15_days < current_date AND dissemination_complete = FALSE THEN violation

[RULE-08] Risk assessments MUST be updated when there are significant changes to systems, operating environment, or threat landscape.
[VALIDATION] IF (system_change_significant = TRUE OR environment_change_significant = TRUE OR threat_change_significant = TRUE) AND risk_assessment_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Risk Assessment Methodology - Standardized approach for conducting risk assessments across all system types
- [PROC-02] Threat Intelligence Integration - Process for incorporating current threat data into risk assessments
- [PROC-03] Privacy Impact Assessment - Specific procedures for evaluating risks to individuals from PII processing
- [PROC-04] Risk Assessment Documentation - Templates and requirements for documenting results in security/privacy plans
- [PROC-05] Significant Change Evaluation - Criteria and process for determining when risk assessments must be updated

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major security incidents, regulatory changes, significant organizational changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Cloud Service Deployment]
IF new_system_deployment = TRUE
AND system_type = "cloud_service"
AND risk_assessment_conducted = FALSE
AND deployment_date + 30_days < current_date
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: PII Processing Without Privacy Assessment]
IF system_processes_pii = TRUE
AND privacy_risk_assessment = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Risk Assessment]
IF last_risk_assessment_date + 365_days < current_date
AND no_significant_changes = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Significant Change Without Update]
IF significant_system_change = TRUE
AND change_date + 30_days < current_date
AND risk_assessment_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Risk Assessment Without Integration]
IF system_risk_assessment = "complete"
AND organizational_risk_integration = FALSE
AND assessment_age_days < 90
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Risk assessment identifies threats and vulnerabilities | RULE-01 |
| Risk assessment determines likelihood and magnitude of harm | RULE-02 |
| Risk assessment evaluates privacy impacts on individuals | RULE-03 |
| Integration with organizational risk management | RULE-04 |
| Risk assessment results documented in plans | RULE-05 |
| Regular review of risk assessment results | RULE-06 |
| Dissemination of risk assessment results | RULE-07 |
| Updates based on significant changes | RULE-08 |