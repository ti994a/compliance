```markdown
# POLICY: IR-4.7: Insider Threats — Intra-organization Coordination

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IR-4.7 |
| NIST Control | IR-4.7: Insider Threats — Intra-organization Coordination |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | insider threats, incident coordination, incident response, threat management, organizational coordination |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain coordinated incident handling capabilities specifically for insider threat incidents across all relevant organizational entities. This coordination MUST include defined roles, communication protocols, and response procedures that enable effective detection, analysis, containment, and recovery from insider threat incidents.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Subject to insider threat monitoring and response |
| Contractors and vendors | YES | With system access or sensitive data exposure |
| Privileged users | YES | Enhanced monitoring and coordination requirements |
| Temporary staff | YES | During access period |
| Business units | YES | Must participate in coordination activities |
| External law enforcement | CONDITIONAL | When legally required or authorized |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Insider Threat Program Manager | • Coordinate cross-organizational response activities<br>• Maintain coordination protocols<br>• Lead incident response coordination |
| CISO/Security Team | • Technical incident analysis and containment<br>• Security control implementation<br>• Threat assessment and investigation |
| Human Resources | • Personnel action coordination<br>• Employee assistance and support<br>• Policy enforcement actions |
| Legal Counsel | • Legal compliance and guidance<br>• Law enforcement coordination<br>• Evidence preservation oversight |
| Business/Mission Owners | • Impact assessment and business continuity<br>• Resource allocation decisions<br>• Operational response coordination |

## 4. RULES

[RULE-01] The organization MUST establish formal coordination agreements with all entities involved in insider threat incident response within 90 days of policy implementation.
[VALIDATION] IF coordination_agreement_exists = FALSE AND days_since_implementation > 90 THEN violation

[RULE-02] Insider threat incidents MUST be reported to all coordinating entities within 4 hours of initial detection for high-severity incidents and within 24 hours for medium-severity incidents.
[VALIDATION] IF incident_severity = "high" AND notification_time > 4_hours THEN critical_violation
[VALIDATION] IF incident_severity = "medium" AND notification_time > 24_hours THEN violation

[RULE-03] Each coordinating entity MUST designate primary and alternate points of contact for insider threat incident coordination and update contact information quarterly.
[VALIDATION] IF contact_designated = FALSE OR contact_age > 90_days THEN violation

[RULE-04] Coordination protocols MUST include defined communication channels, escalation procedures, and decision-making authority for each phase of incident response.
[VALIDATION] IF protocol_defined = FALSE OR missing_communication_channels = TRUE THEN violation

[RULE-05] Joint training exercises involving all coordinating entities MUST be conducted at least annually to validate coordination effectiveness.
[VALIDATION] IF last_joint_exercise > 365_days THEN violation

[RULE-06] External law enforcement coordination MUST follow established legal protocols and require legal counsel approval before information sharing.
[VALIDATION] IF external_coordination = TRUE AND legal_approval = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Insider Threat Incident Coordination Protocol - Defines roles, responsibilities, and communication flows
- [PROC-02] Cross-Entity Notification Procedure - Standardizes incident reporting and escalation
- [PROC-03] Joint Investigation Coordination - Establishes collaborative investigation processes
- [PROC-04] External Agency Coordination - Governs law enforcement and regulatory coordination
- [PROC-05] Post-Incident Coordination Review - Evaluates coordination effectiveness and improvements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Significant insider threat incidents, organizational restructuring, regulatory changes, coordination failures

## 7. SCENARIO PATTERNS

[SCENARIO-01: High-Severity Incident Coordination]
IF incident_severity = "high"
AND insider_threat_detected = TRUE
AND coordination_initiated = TRUE
AND notification_time <= 4_hours
THEN compliance = TRUE

[SCENARIO-02: Missing Coordination Entity]
IF insider_incident_active = TRUE
AND required_entity_notified = FALSE
AND incident_age > 4_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: External Law Enforcement Coordination]
IF law_enforcement_involved = TRUE
AND legal_approval = FALSE
AND information_shared = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Outdated Coordination Contacts]
IF coordination_contact_age > 90_days
AND incident_notification_attempted = TRUE
AND contact_unreachable = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Annual Training Compliance]
IF current_date - last_joint_exercise > 365_days
AND no_scheduled_exercise = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Incident handling capability coordination established | RULE-01, RULE-04 |
| Coordinating entities properly defined and engaged | RULE-03, RULE-05 |
| Timely coordination during incidents | RULE-02, RULE-06 |
| Coordination effectiveness validated | RULE-05 |
```