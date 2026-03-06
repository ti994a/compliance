# POLICY: SR-2.1: Establish SCRM Team

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-2.1 |
| NIST Control | SR-2.1: Establish SCRM Team |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | supply chain, risk management, SCRM team, roles, responsibilities, team charter |

## 1. POLICY STATEMENT
The organization SHALL establish a formal supply chain risk management (SCRM) team with clearly defined personnel, roles, and responsibilities to lead and support all supply chain risk management activities. The SCRM team MUST be properly chartered and include representatives from all relevant organizational functions to ensure comprehensive supply chain risk oversight.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Includes internal and external supply chains |
| Third-party suppliers | YES | Subject to SCRM team oversight |
| Acquisition processes | YES | SCRM team involvement required |
| Business continuity operations | YES | Supply chain dependencies |
| Development lifecycle activities | YES | SDLC integration required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| SCRM Team Lead | • Coordinate all SCRM activities<br>• Report to executive leadership<br>• Maintain team charter and documentation |
| Risk Executive | • Provide strategic risk oversight<br>• Approve risk tolerance levels<br>• Authorize risk mitigation resources |
| IT Security Representative | • Assess technical supply chain risks<br>• Implement security controls<br>• Monitor threat intelligence |
| Procurement/Contracting | • Evaluate supplier risk assessments<br>• Include SCRM requirements in contracts<br>• Manage supplier relationships |
| Legal Counsel | • Review regulatory compliance<br>• Address contractual risk issues<br>• Support incident response activities |

## 4. RULES

[RULE-01] The organization MUST establish a formal SCRM team with documented charter, roles, and responsibilities within 90 days of policy implementation.
[VALIDATION] IF scrm_team_established = FALSE OR charter_documented = FALSE OR days_since_policy > 90 THEN violation

[RULE-02] The SCRM team MUST include representatives from at least seven core functions: risk management, IT security, procurement, legal, business operations, supply chain/logistics, and business continuity.
[VALIDATION] IF scrm_team_functions < 7 OR missing_core_function = TRUE THEN violation

[RULE-03] SCRM team members MUST collectively possess expertise in acquisition processes, legal practices, vulnerabilities, threats, attack vectors, and technical system dependencies.
[VALIDATION] IF expertise_gaps_identified = TRUE AND mitigation_plan = FALSE THEN violation

[RULE-04] The SCRM team SHALL meet at least monthly and maintain documented meeting records with action items and decisions.
[VALIDATION] IF days_since_last_meeting > 35 OR meeting_documentation = FALSE THEN violation

[RULE-05] SCRM team composition and charter MUST be reviewed and updated annually or when significant organizational changes occur.
[VALIDATION] IF days_since_charter_review > 365 OR significant_change_no_review = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SCRM Team Charter Development - Establish formal team structure and governance
- [PROC-02] Team Member Selection and Training - Ensure appropriate expertise and knowledge
- [PROC-03] SCRM Activity Coordination - Define workflows and communication protocols
- [PROC-04] Stakeholder Engagement - Interface with internal and external partners
- [PROC-05] Performance Measurement - Track team effectiveness and outcomes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Organizational restructuring, significant supply chain incidents, regulatory changes, merger/acquisition activities

## 7. SCENARIO PATTERNS

[SCENARIO-01: Incomplete Team Formation]
IF scrm_team_established = TRUE
AND core_functions_represented < 7
AND charter_approved = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Expertise Gap Without Mitigation]
IF scrm_team_established = TRUE
AND technical_expertise_gap = TRUE
AND training_plan = FALSE
AND external_consultation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Inactive Team Operations]
IF scrm_team_established = TRUE
AND days_since_last_meeting > 60
AND active_scrm_activities = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Proper Team with Regular Activities]
IF scrm_team_established = TRUE
AND core_functions_represented >= 7
AND charter_current = TRUE
AND monthly_meetings_held = TRUE
AND documented_activities = TRUE
THEN compliance = TRUE

[SCENARIO-05: Organizational Change Without Review]
IF scrm_team_established = TRUE
AND major_org_restructure = TRUE
AND days_since_restructure > 90
AND team_composition_reviewed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| SCRM team establishment with defined roles and responsibilities | [RULE-01], [RULE-02] |
| Team leads and supports SCRM activities | [RULE-04], [PROC-03] |
| Appropriate personnel expertise and awareness | [RULE-03], [PROC-02] |
| Coordinated team-based approach implementation | [RULE-04], [PROC-04] |