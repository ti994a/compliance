# POLICY: PM-11: Mission and Business Process Definition

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-11 |
| NIST Control | PM-11: Mission and Business Process Definition |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mission definition, business processes, information protection, privacy requirements, risk assessment, PII processing |

## 1. POLICY STATEMENT
The organization SHALL define mission and business processes with explicit consideration for information security, privacy, and resulting risks to operations, assets, individuals, other organizations, and the Nation. Information protection and personally identifiable information (PII) processing needs SHALL be determined from these defined processes and reviewed at established intervals.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational units | YES | Must define mission-critical processes |
| Business process owners | YES | Responsible for security/privacy integration |
| Information systems | YES | Must align with defined protection needs |
| Third-party processes | YES | When processing organizational data |
| Legacy systems | CONDITIONAL | Must comply within 12 months |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Business Process Owners | • Define mission and business processes with security/privacy considerations<br>• Identify information protection needs<br>• Participate in regular process reviews |
| CISO/Privacy Officer | • Ensure security and privacy requirements are integrated<br>• Validate protection needs determinations<br>• Oversee review and revision processes |
| Risk Management Team | • Assess risks to operations, assets, individuals, and Nation<br>• Support categorization and impact determinations<br>• Conduct privacy risk assessments |

## 4. RULES
[RULE-01] All organizational mission and business processes MUST be formally defined with explicit consideration for information security requirements.
[VALIDATION] IF business_process_documented = TRUE AND security_considerations_included = FALSE THEN violation

[RULE-02] All organizational mission and business processes MUST be formally defined with explicit consideration for privacy requirements.
[VALIDATION] IF business_process_documented = TRUE AND privacy_considerations_included = FALSE THEN violation

[RULE-03] Information protection needs arising from defined mission and business processes MUST be documented and categorized according to potential adverse impact.
[VALIDATION] IF business_process_defined = TRUE AND protection_needs_undocumented = TRUE THEN violation

[RULE-04] Personally identifiable information processing needs MUST be identified and documented for all defined mission and business processes that handle PII.
[VALIDATION] IF process_handles_PII = TRUE AND PII_processing_needs_undefined = TRUE THEN violation

[RULE-05] Mission and business processes MUST be reviewed and revised at least annually or when significant changes occur.
[VALIDATION] IF last_review_date > 365_days AND no_triggering_event = TRUE THEN violation

[RULE-06] Risk assessments MUST consider potential impact to organizational operations, assets, individuals, other organizations, and the Nation.
[VALIDATION] IF risk_assessment_complete = TRUE AND stakeholder_impact_missing = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Business Process Definition - Standardized methodology for defining processes with security/privacy integration
- [PROC-02] Protection Needs Assessment - Process for determining information protection requirements
- [PROC-03] PII Processing Analysis - Systematic identification of PII processing needs and risks
- [PROC-04] Mission Process Review - Annual review and revision of mission and business processes
- [PROC-05] Impact Categorization - Framework for assessing potential adverse impacts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major organizational changes, significant security incidents, regulatory changes, new business processes, privacy breaches

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Business Process Launch]
IF new_business_process = TRUE
AND security_considerations_documented = FALSE
AND process_approved = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: PII Processing Without Assessment]
IF process_handles_PII = TRUE
AND PII_processing_needs_documented = FALSE
AND process_operational = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Overdue Process Review]
IF last_process_review > 365_days
AND no_documented_exception = TRUE
AND business_critical_process = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete Risk Assessment]
IF risk_assessment_exists = TRUE
AND national_impact_considered = FALSE
AND high_risk_process = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Legacy Process Compliance]
IF legacy_process = TRUE
AND security_integration_complete = TRUE
AND privacy_considerations_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Mission and business processes defined with information security consideration | [RULE-01] |
| Mission and business processes defined with privacy consideration | [RULE-02] |
| Risk consideration to operations, assets, individuals, organizations, and Nation | [RULE-06] |
| Information protection needs determination | [RULE-03] |
| PII processing needs determination | [RULE-04] |
| Regular review and revision of processes | [RULE-05] |