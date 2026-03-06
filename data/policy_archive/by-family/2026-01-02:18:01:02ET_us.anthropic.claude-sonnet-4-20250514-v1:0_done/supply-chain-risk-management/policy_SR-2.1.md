# POLICY: SR-2.1: Establish SCRM Team

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-2.1 |
| NIST Control | SR-2.1: Establish SCRM Team |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | supply chain, risk management, SCRM team, personnel, roles, responsibilities |

## 1. POLICY STATEMENT
The organization SHALL establish a formal Supply Chain Risk Management (SCRM) team with defined personnel, roles, and responsibilities to lead and support supply chain risk management activities. The SCRM team MUST consist of diverse organizational functions to ensure comprehensive supply chain risk identification, assessment, and mitigation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational units | YES | All departments must participate in SCRM activities |
| Third-party suppliers | CONDITIONAL | Subject to SCRM team oversight and assessment |
| Contractors and vendors | CONDITIONAL | Must comply with SCRM requirements when specified |
| Cloud service providers | YES | Critical components of supply chain |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| SCRM Team Lead | • Coordinate SCRM activities across organization<br>• Report to executive leadership<br>• Ensure team charter compliance |
| Risk Executive | • Provide executive oversight<br>• Approve SCRM strategies<br>• Allocate resources for SCRM activities |
| IT Security Representative | • Assess technical security risks<br>• Implement security controls<br>• Monitor supply chain vulnerabilities |
| Procurement/Contracting | • Integrate SCRM into acquisition processes<br>• Evaluate supplier risk profiles<br>• Manage contractual risk requirements |
| Legal Counsel | • Ensure regulatory compliance<br>• Review contractual risk provisions<br>• Address liability and legal risks |

## 4. RULES
[RULE-01] The organization MUST establish a formal SCRM team with documented charter, roles, and responsibilities within 90 days of policy implementation.
[VALIDATION] IF scrm_team_established = FALSE OR team_charter_documented = FALSE THEN violation

[RULE-02] The SCRM team MUST include representatives from at least five core functions: risk management, IT security, procurement, legal, and business operations.
[VALIDATION] IF scrm_team_functions < 5 OR missing_core_function = TRUE THEN violation

[RULE-03] SCRM team members MUST receive role-specific training within 60 days of appointment and annually thereafter.
[VALIDATION] IF member_training_date > appointment_date + 60_days OR annual_training_overdue = TRUE THEN violation

[RULE-04] The SCRM team MUST meet at least quarterly and maintain documented meeting records with action items and decisions.
[VALIDATION] IF quarterly_meetings_held < 4 OR meeting_documentation = FALSE THEN violation

[RULE-05] The SCRM team SHALL define and document specific supply chain risk management activities within their charter.
[VALIDATION] IF scrm_activities_defined = FALSE OR activities_documented = FALSE THEN violation

[RULE-06] SCRM team composition MUST be reviewed and updated annually or when significant organizational changes occur.
[VALIDATION] IF team_review_date > 365_days OR organizational_change = TRUE AND team_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SCRM Team Charter Development - Establish formal team structure and responsibilities
- [PROC-02] Member Selection and Appointment - Define criteria and process for team membership
- [PROC-03] Training and Competency Management - Ensure team members maintain required expertise
- [PROC-04] Meeting Management and Documentation - Standardize team meeting processes
- [PROC-05] Team Performance Review - Annual assessment of team effectiveness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Organizational restructuring, significant supply chain incidents, regulatory changes, executive leadership changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Incomplete Team Formation]
IF scrm_team_established = TRUE
AND core_functions_represented < 5
AND team_charter_approved = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Training Records]
IF scrm_team_member_appointed = TRUE
AND appointment_date + 90_days < current_date
AND training_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Inadequate Meeting Frequency]
IF current_year_quarters = 4
AND documented_meetings < 4
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Properly Functioning Team]
IF scrm_team_established = TRUE
AND core_functions_represented >= 5
AND quarterly_meetings_current = TRUE
AND all_members_trained = TRUE
THEN compliance = TRUE

[SCENARIO-05: Organizational Change Response]
IF major_organizational_change = TRUE
AND change_date + 60_days < current_date
AND scrm_team_composition_reviewed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Supply chain risk management team established | [RULE-01] |
| Personnel, roles, and responsibilities defined | [RULE-02], [RULE-05] |
| Team leads and supports SCRM activities | [RULE-04], [RULE-05] |
| Diverse organizational representation | [RULE-02] |
| Documented team charter and activities | [RULE-01], [RULE-05] |