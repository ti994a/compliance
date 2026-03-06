# POLICY: PM-12: Insider Threat Program

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-12 |
| NIST Control | PM-12: Insider Threat Program |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | insider threat, cross-discipline team, incident handling, monitoring, awareness training |

## 1. POLICY STATEMENT
The organization SHALL implement a comprehensive insider threat program that includes a cross-discipline insider threat incident handling team to detect, prevent, and respond to malicious insider activity. The program SHALL integrate technical and non-technical information sources to identify potential insider threat concerns through centralized analysis and monitoring capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Including full-time, part-time, contractors |
| All information systems | YES | Government-owned and contractor-operated |
| All facilities | YES | Physical and virtual environments |
| Third-party vendors | CONDITIONAL | When accessing organizational systems/data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Senior Insider Threat Official | • Provide program oversight and governance<br>• Report to agency head<br>• Ensure policy compliance<br>• Coordinate with legal counsel |
| Cross-Discipline Team Members | • Analyze technical and behavioral indicators<br>• Investigate insider threat incidents<br>• Coordinate response activities<br>• Maintain situational awareness |
| HR Representatives | • Provide employee behavior analysis<br>• Support background investigations<br>• Coordinate disciplinary actions |
| Legal Counsel | • Ensure compliance with privacy laws<br>• Review monitoring activities<br>• Support investigation procedures |

## 4. RULES
[RULE-01] The organization MUST establish a cross-discipline insider threat incident handling team with representatives from security, HR, legal, and IT.
[VALIDATION] IF team_established = FALSE OR team_disciplines < 4 THEN violation

[RULE-02] A senior official MUST be designated to implement and provide oversight for the insider threat program.
[VALIDATION] IF senior_official_designated = FALSE OR oversight_documented = FALSE THEN violation

[RULE-03] The program MUST include centralized integration and analysis capability for technical and non-technical information.
[VALIDATION] IF centralized_analysis = FALSE OR technical_integration = FALSE OR nontechnical_integration = FALSE THEN violation

[RULE-04] Host-based user monitoring MUST be implemented on government-owned systems for individual employee activities.
[VALIDATION] IF host_monitoring = FALSE OR monitoring_scope != "individual_activities" THEN violation

[RULE-05] Insider threat awareness training MUST be provided to all employees within 90 days of assignment and annually thereafter.
[VALIDATION] IF employee_training_date > 90_days_from_assignment OR last_annual_training > 365_days THEN violation

[RULE-06] The program MUST conduct annual self-assessments of the organization's insider threat posture.
[VALIDATION] IF last_self_assessment > 365_days OR assessment_documented = FALSE THEN violation

[RULE-07] Human resources records access MUST be provided to the insider threat program with appropriate privacy controls.
[VALIDATION] IF hr_records_access = FALSE OR privacy_controls_documented = FALSE THEN violation

[RULE-08] Legal counsel MUST review all monitoring activities to ensure compliance with applicable laws and privacy requirements.
[VALIDATION] IF legal_review_documented = FALSE OR privacy_compliance_verified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Insider Threat Program Charter - Formal establishment and governance structure
- [PROC-02] Cross-Discipline Team Operations - Team composition, roles, and coordination processes
- [PROC-03] Threat Indicator Analysis - Technical and behavioral indicator identification and analysis
- [PROC-04] Incident Response Procedures - Investigation and response protocols for insider threats
- [PROC-05] Employee Monitoring Protocols - Host-based monitoring implementation and privacy safeguards
- [PROC-06] Training and Awareness Program - Insider threat education and awareness delivery
- [PROC-07] Self-Assessment Process - Annual program evaluation and improvement procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents, regulatory changes, organizational restructuring, legal updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Cross-Discipline Team]
IF insider_threat_program = TRUE
AND team_disciplines < 4
AND security_rep = FALSE OR hr_rep = FALSE OR legal_rep = FALSE OR it_rep = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate Employee Monitoring]
IF government_owned_systems = TRUE
AND host_monitoring = FALSE
AND employee_activity_tracking = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Senior Official Oversight]
IF insider_threat_program = TRUE
AND senior_official_designated = FALSE
AND program_oversight_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Expired Training Requirements]
IF employee_assignment_date > 90_days
AND insider_threat_training_completed = FALSE
AND training_exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Privacy Non-Compliance]
IF hr_records_monitoring = TRUE
AND legal_review_completed = FALSE
AND privacy_controls_implemented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cross-discipline insider threat incident handling team implementation | [RULE-01] |
| Senior official program oversight designation | [RULE-02] |
| Centralized integration and analysis capability | [RULE-03] |
| Host-based user monitoring implementation | [RULE-04] |
| Insider threat awareness training provision | [RULE-05] |
| Annual self-assessment conduct | [RULE-06] |
| HR records access with privacy controls | [RULE-07] |
| Legal compliance review of monitoring activities | [RULE-08] |