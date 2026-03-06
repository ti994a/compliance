# POLICY: PM-12: Insider Threat Program

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-12 |
| NIST Control | PM-12: Insider Threat Program |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | insider threat, incident handling, cross-discipline team, monitoring, malicious activity |

## 1. POLICY STATEMENT
The organization SHALL implement a comprehensive insider threat program that includes a cross-discipline insider threat incident handling team to detect, prevent, and respond to malicious insider activities. The program SHALL integrate technical and nontechnical monitoring capabilities with centralized analysis to identify potential insider threat concerns across all organizational systems and personnel.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full-time, part-time, temporary |
| Contractors | YES | All contracted personnel with system access |
| Privileged users | YES | Enhanced monitoring requirements |
| All information systems | YES | Government-owned and contractor systems |
| HR records | CONDITIONAL | Subject to privacy and legal review |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Senior Insider Threat Official | • Provide executive oversight and program implementation<br>• Report to department/agency head<br>• Ensure cross-organizational coordination |
| Cross-Discipline Team Lead | • Coordinate incident response activities<br>• Manage technical and nontechnical analysis<br>• Interface with legal and HR teams |
| Security Operations Center | • Conduct continuous monitoring<br>• Perform initial threat analysis<br>• Escalate suspicious activities |
| Legal Counsel | • Ensure compliance with privacy laws<br>• Review monitoring procedures<br>• Approve investigation activities |

## 4. RULES

[RULE-01] The organization MUST establish a cross-discipline insider threat incident handling team with representatives from security, HR, legal, and operational units.
[VALIDATION] IF team_established = FALSE OR team_missing_discipline = TRUE THEN violation

[RULE-02] A senior official MUST be designated by the department or agency head to implement and provide oversight for the insider threat program.
[VALIDATION] IF senior_official_designated = FALSE OR designation_authority != "department_head" THEN violation

[RULE-03] The program MUST include centralized integration and analysis capability for both technical and nontechnical information.
[VALIDATION] IF centralized_analysis = FALSE OR technical_integration = FALSE OR nontechnical_integration = FALSE THEN violation

[RULE-04] Host-based user monitoring MUST be implemented on government-owned systems for individual employee activities.
[VALIDATION] IF host_monitoring_enabled = FALSE OR coverage < 100% THEN violation

[RULE-05] Insider threat awareness training MUST be provided to all employees and updated annually.
[VALIDATION] IF employee_training_current = FALSE OR training_age > 365_days THEN violation

[RULE-06] The program MUST have access to HR records and other organizational information necessary for insider threat analysis, subject to legal and privacy review.
[VALIDATION] IF hr_access_approved = FALSE OR legal_review_completed = FALSE THEN violation

[RULE-07] Self-assessments of the insider threat program posture MUST be conducted annually.
[VALIDATION] IF last_assessment_date > 365_days OR assessment_completed = FALSE THEN violation

[RULE-08] Insider threat policies and implementation plans MUST be documented and approved by senior leadership.
[VALIDATION] IF policy_documented = FALSE OR senior_approval = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Insider Threat Detection - Continuous monitoring and analysis procedures
- [PROC-02] Incident Response - Cross-discipline team activation and response protocols  
- [PROC-03] Investigation Management - Coordinated investigation procedures with legal oversight
- [PROC-04] Information Sharing - Secure information exchange between organizational units
- [PROC-05] Training Delivery - Insider threat awareness training program implementation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after major incidents
- Triggering events: Security incidents, organizational changes, regulatory updates, executive orders

## 7. SCENARIO PATTERNS

[SCENARIO-01: Missing Cross-Discipline Team]
IF insider_threat_program = "implemented"
AND cross_discipline_team = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate Monitoring Coverage]
IF host_monitoring = "enabled"
AND system_coverage < 90%
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated Training Program]
IF awareness_training = "implemented"
AND last_training_update > 18_months
AND employee_completion_rate < 95%
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unauthorized HR Access]
IF hr_records_access = TRUE
AND legal_review_status = "pending"
AND privacy_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Complete Program Implementation]
IF cross_discipline_team = TRUE
AND senior_official_designated = TRUE
AND centralized_analysis = TRUE
AND host_monitoring_coverage >= 95%
AND training_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cross-discipline insider threat incident handling team implemented | [RULE-01] |
| Senior official designated for program oversight | [RULE-02] |
| Centralized integration and analysis capability | [RULE-03] |
| Host-based user monitoring implemented | [RULE-04] |
| Insider threat awareness training provided | [RULE-05] |
| Access to organizational information for analysis | [RULE-06] |
| Self-assessments conducted | [RULE-07] |
| Policies and implementation plans documented | [RULE-08] |