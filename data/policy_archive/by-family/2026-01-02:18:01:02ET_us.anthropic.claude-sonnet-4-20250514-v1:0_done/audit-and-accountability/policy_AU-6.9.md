# POLICY: AU-6.9: Correlation with Information from Nontechnical Sources

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-6.9 |
| NIST Control | AU-6.9: Correlation with Information from Nontechnical Sources |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit correlation, nontechnical sources, situational awareness, insider threat, policy violations |

## 1. POLICY STATEMENT
The organization SHALL correlate information from nontechnical sources with audit record information to enhance organization-wide situational awareness and detect potential malicious insider activity. Access to nontechnical source information MUST be limited to authorized personnel with a legitimate need to know.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems generating audit records |
| HR Policy Violations | YES | Harassment, misconduct, asset misuse |
| Physical Security Incidents | YES | Badge violations, facility access |
| Legal/Compliance Records | CONDITIONAL | When related to information security |
| External Partners | NO | Limited to internal organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Perform correlation analysis between technical and nontechnical sources<br>• Maintain correlation procedures and tools<br>• Escalate correlated findings to appropriate stakeholders |
| Human Resources | • Provide relevant policy violation records for correlation<br>• Ensure privacy protection of sensitive HR information<br>• Coordinate with legal on information sharing |
| Legal Counsel | • Review correlation activities for legal compliance<br>• Approve access to sensitive nontechnical sources<br>• Provide guidance on privacy and regulatory requirements |

## 4. RULES
[RULE-01] Organizations MUST establish formal procedures for correlating nontechnical source information with audit records to enhance situational awareness.
[VALIDATION] IF correlation_procedures_documented = FALSE THEN violation

[RULE-02] Access to nontechnical source information MUST be limited to authorized personnel with documented need-to-know and appropriate clearance levels.
[VALIDATION] IF nontechnical_access_controls = FALSE OR access_justification_documented = FALSE THEN violation

[RULE-03] Correlation activities involving suspected individuals MUST be initiated only after obtaining legal counsel approval and documenting the justification.
[VALIDATION] IF correlation_target = "individual" AND legal_approval = FALSE THEN critical_violation

[RULE-04] Nontechnical sources MUST include at minimum: HR policy violations, physical security incidents, and information asset misuse reports.
[VALIDATION] IF nontechnical_sources_count < 3 OR hr_violations_included = FALSE THEN violation

[RULE-05] Correlation results that indicate potential insider threats MUST be reported to security management within 4 hours of discovery.
[VALIDATION] IF insider_threat_indicator = TRUE AND reporting_time > 4_hours THEN violation

[RULE-06] All correlation activities MUST be logged with sufficient detail to support audit and legal review requirements.
[VALIDATION] IF correlation_logging = FALSE OR log_detail_level = "insufficient" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Nontechnical Source Correlation - Standard operating procedures for correlating HR, physical security, and policy violation data with audit records
- [PROC-02] Legal Review Process - Procedures for obtaining legal approval before initiating individual-focused correlation activities
- [PROC-03] Access Control Management - Procedures for granting and monitoring access to sensitive nontechnical sources
- [PROC-04] Incident Escalation - Procedures for escalating correlated findings that indicate potential security threats

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving insider threats, changes in legal requirements, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: HR Violation Correlation]
IF employee_hr_violation = TRUE
AND employee_system_access = "elevated"
AND audit_anomalies_detected = TRUE
AND correlation_performed = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Correlation Access]
IF user_access_nontechnical_sources = TRUE
AND need_to_know_documented = FALSE
AND access_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Individual Investigation Without Legal Approval]
IF correlation_target_type = "specific_individual"
AND legal_counsel_approval = FALSE
AND correlation_initiated = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Delayed Insider Threat Reporting]
IF correlation_result = "insider_threat_indicator"
AND discovery_time = "confirmed"
AND reporting_delay > 4_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Insufficient Nontechnical Sources]
IF nontechnical_sources_configured = TRUE
AND hr_violations_included = FALSE
AND physical_security_included = TRUE
AND asset_misuse_included = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information from non-technical sources is correlated with audit record information | [RULE-01], [RULE-04] |
| Enhanced organization-wide situational awareness | [RULE-01], [RULE-05] |
| Limited access to sensitive nontechnical information | [RULE-02] |
| Legal approval for individual-focused correlation | [RULE-03] |
| Proper documentation and logging of activities | [RULE-06] |