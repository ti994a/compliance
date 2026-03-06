# POLICY: SR-2.1: Establish SCRM Team

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-2.1 |
| NIST Control | SR-2.1: Establish SCRM Team |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | supply chain, risk management, team, SCRM, personnel, roles, responsibilities |

## 1. POLICY STATEMENT
The organization SHALL establish a formal Supply Chain Risk Management (SCRM) team with defined personnel, roles, and responsibilities to lead and support all supply chain risk management activities. The SCRM team MUST consist of diverse organizational functions to ensure comprehensive coverage of supply chain risks across the enterprise.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including cloud, hybrid, and on-premises |
| Third-party suppliers | YES | Where contractual authority exists |
| Acquisition processes | YES | All procurement activities |
| Software development lifecycle | YES | Internal and contracted development |
| Business continuity functions | YES | Supply chain dependencies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| SCRM Team Lead | • Overall team coordination and strategy<br>• Executive reporting and communication<br>• Resource allocation and prioritization |
| Risk Executive | • Strategic risk oversight<br>• Risk appetite and tolerance setting<br>• Executive stakeholder engagement |
| IT/Security Representative | • Technical risk assessment<br>• Security control implementation<br>• Vulnerability and threat analysis |
| Procurement/Contracting | • Supplier evaluation and selection<br>• Contract risk terms negotiation<br>• Vendor relationship management |
| Legal Counsel | • Regulatory compliance guidance<br>• Contract review and approval<br>• Liability and indemnification matters |
| Business Continuity | • Impact assessment and planning<br>• Alternative supplier identification<br>• Recovery strategy development |

## 4. RULES
[RULE-01] The organization MUST establish a formal SCRM team with documented charter, roles, and responsibilities within 90 days of policy implementation.
[VALIDATION] IF scrm_team_established = FALSE OR charter_documented = FALSE OR days_since_policy > 90 THEN violation

[RULE-02] The SCRM team MUST include representatives from at minimum: risk management, IT/security, procurement, legal, and business continuity functions.
[VALIDATION] IF missing_required_functions > 0 THEN violation

[RULE-03] SCRM team members MUST receive role-specific training within 60 days of appointment and annually thereafter.
[VALIDATION] IF team_member_training_current = FALSE OR training_overdue > 60_days THEN violation

[RULE-04] The SCRM team MUST meet at least quarterly to review supply chain risks and mitigation activities.
[VALIDATION] IF quarterly_meetings_held < 4 AND current_year_complete = TRUE THEN violation

[RULE-05] SCRM team activities and decisions MUST be documented and maintained for audit purposes for minimum 3 years.
[VALIDATION] IF documentation_retention < 3_years OR meeting_minutes_missing = TRUE THEN violation

[RULE-06] The SCRM team charter MUST be reviewed and updated annually or when significant organizational changes occur.
[VALIDATION] IF charter_last_review > 365_days AND no_triggering_events = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SCRM Team Charter Development - Formal establishment and documentation of team structure
- [PROC-02] Team Member Selection and Training - Identification and preparation of team personnel
- [PROC-03] SCRM Activity Planning and Execution - Coordination of supply chain risk management activities
- [PROC-04] Stakeholder Communication - Internal and external communication protocols
- [PROC-05] Performance Monitoring and Reporting - Team effectiveness measurement and reporting

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Organizational restructuring, significant supply chain incidents, regulatory changes, acquisition of new business units

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Core Function]
IF scrm_team_established = TRUE
AND required_function_represented = FALSE
AND function_type IN ["risk_management", "IT_security", "procurement", "legal", "business_continuity"]
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inactive Team Operations]
IF scrm_team_established = TRUE
AND quarterly_meetings_held < required_minimum
AND current_quarter > 1
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Untrained Team Members]
IF team_member_appointed = TRUE
AND training_completion_date = NULL
AND days_since_appointment > 60
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Outdated Charter]
IF scrm_charter_exists = TRUE
AND charter_last_review > 365_days
AND organizational_changes = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Proper Team Establishment]
IF scrm_team_established = TRUE
AND all_required_functions_represented = TRUE
AND team_training_current = TRUE
AND quarterly_meetings_conducted = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Supply chain risk management team established | [RULE-01] |
| Personnel, roles, and responsibilities defined | [RULE-01], [RULE-02] |
| Team leads and supports SCRM activities | [RULE-04], [RULE-05] |
| Diverse organizational representation | [RULE-02] |
| Documented team charter and procedures | [RULE-01], [RULE-06] |