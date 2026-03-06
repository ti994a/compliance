```markdown
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
The organization SHALL implement a comprehensive insider threat program that includes a cross-discipline insider threat incident handling team to detect, prevent, and respond to malicious insider activities. The program SHALL integrate technical and non-technical information sources to identify potential insider threat concerns through centralized analysis capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Including contractors and temporary staff |
| All information systems | YES | Government-owned and contractor systems |
| Classified systems | YES | Enhanced monitoring requirements |
| Cloud infrastructure | YES | Hybrid cloud environments included |
| HR records | CONDITIONAL | Subject to privacy and legal review |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Senior Designated Official | • Provide program oversight and governance<br>• Ensure adequate resources and authority<br>• Report to agency head on program effectiveness |
| Insider Threat Program Manager | • Implement daily program operations<br>• Coordinate cross-discipline team activities<br>• Manage centralized analysis capabilities |
| Cross-Discipline Team Members | • Participate in threat analysis and investigations<br>• Provide subject matter expertise<br>• Execute incident response procedures |
| Legal Counsel | • Ensure compliance with applicable laws<br>• Review monitoring activities for privacy concerns<br>• Advise on investigation procedures |

## 4. RULES

[RULE-01] The organization MUST establish a formal insider threat program with a designated senior official responsible for implementation and oversight.
[VALIDATION] IF insider_threat_program_exists = FALSE OR designated_senior_official = NULL THEN critical_violation

[RULE-02] A cross-discipline insider threat incident handling team MUST be established and include representatives from security, HR, legal, IT, and management.
[VALIDATION] IF team_members < 5_disciplines OR security_rep = FALSE OR hr_rep = FALSE OR legal_rep = FALSE THEN violation

[RULE-03] The program MUST implement centralized integration and analysis capabilities for both technical and non-technical information sources.
[VALIDATION] IF centralized_analysis_capability = FALSE OR technical_integration = FALSE OR nontechnical_integration = FALSE THEN violation

[RULE-04] Host-based user monitoring MUST be implemented on all government-owned systems for employees with access to classified or sensitive information.
[VALIDATION] IF classified_access = TRUE AND host_monitoring = FALSE THEN critical_violation

[RULE-05] Insider threat awareness training MUST be provided to all employees and updated annually.
[VALIDATION] IF employee_training_date > 365_days OR training_completion_rate < 95% THEN violation

[RULE-06] The program MUST conduct annual self-assessments of the organization's insider threat posture and remediate identified gaps within 90 days.
[VALIDATION] IF last_self_assessment > 365_days OR gap_remediation_time > 90_days THEN violation

[RULE-07] Access to relevant information from organizational offices MUST be established for insider threat analysis purposes, subject to legal and privacy requirements.
[VALIDATION] IF information_access_agreements = FALSE OR privacy_review_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Insider Threat Detection and Analysis - Continuous monitoring and analysis of indicators
- [PROC-02] Incident Response and Investigation - Standardized response to insider threat incidents  
- [PROC-03] Information Sharing and Coordination - Cross-functional information sharing protocols
- [PROC-04] Employee Monitoring and Privacy Protection - Balanced monitoring with privacy safeguards
- [PROC-05] Training and Awareness Program - Regular education and awareness activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Security incidents, organizational changes, regulatory updates, technology changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Missing Cross-Discipline Team]
IF insider_threat_program = TRUE
AND cross_discipline_team_members < 4
AND legal_representation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate Monitoring Coverage]
IF classified_system_access = TRUE
AND host_based_monitoring = FALSE
AND user_activity_logging = "basic"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Outdated Training Program]
IF employee_count > 100
AND last_training_update > 18_months
AND training_completion_rate = 78%
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete Centralized Analysis]
IF technical_data_integration = TRUE
AND hr_data_integration = FALSE
AND centralized_analysis_capability = "partial"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Overdue Self-Assessment]
IF last_self_assessment_date > 400_days
AND identified_gaps_count > 0
AND remediation_status = "pending"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Insider threat program implementation | RULE-01 |
| Cross-discipline incident handling team | RULE-02 |
| Centralized integration and analysis | RULE-03 |
| Host-based user monitoring | RULE-04 |
| Awareness training provision | RULE-05 |
| Self-assessment execution | RULE-06 |
| Information access establishment | RULE-07 |
```