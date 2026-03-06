# POLICY: IR-6: Incident Reporting

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IR-6 |
| NIST Control | IR-6: Incident Reporting |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | incident reporting, suspected incidents, response capability, authorities, notification |

## 1. POLICY STATEMENT
All personnel MUST report suspected security incidents to the organizational incident response capability within defined timeframes. Incident information MUST be reported to designated authorities as required by applicable laws, regulations, and organizational policies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Employees | YES | Full-time, part-time, contractors |
| Temporary Staff | YES | Including interns and consultants |
| Third-party Users | YES | With system access privileges |
| External Partners | CONDITIONAL | When accessing company systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| All Personnel | • Report suspected incidents immediately<br>• Follow established reporting procedures<br>• Preserve evidence when safe to do so |
| Incident Response Team | • Receive and triage incident reports<br>• Coordinate response activities<br>• Report to external authorities as required |
| CISO | • Define reporting timeframes<br>• Designate reporting authorities<br>• Ensure compliance with regulatory requirements |

## 4. RULES

[RULE-01] Personnel MUST report suspected security incidents to the incident response capability within 1 hour for critical incidents and within 4 hours for all other incidents.
[VALIDATION] IF incident_severity = "critical" AND report_time > 1_hour THEN critical_violation
[VALIDATION] IF incident_severity != "critical" AND report_time > 4_hours THEN violation

[RULE-02] The incident response team MUST report incidents to designated external authorities within 24 hours for regulatory incidents and within 72 hours for privacy incidents.
[VALIDATION] IF incident_type = "regulatory" AND external_report_time > 24_hours THEN critical_violation
[VALIDATION] IF incident_type = "privacy" AND external_report_time > 72_hours THEN violation

[RULE-03] Incident reports MUST include all required information elements: incident description, affected systems, potential impact, and initial containment actions.
[VALIDATION] IF missing_required_fields > 0 THEN violation

[RULE-04] Personnel SHALL NOT delay incident reporting to conduct preliminary investigations that exceed the defined reporting timeframes.
[VALIDATION] IF investigation_delay = TRUE AND report_time > required_timeframe THEN violation

[RULE-05] All incident reports MUST be documented in the centralized incident management system within 2 hours of initial notification.
[VALIDATION] IF documentation_time > 2_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Incident Identification and Classification - Standard process for recognizing and categorizing incidents
- [PROC-02] Internal Incident Reporting - Step-by-step reporting to incident response team
- [PROC-03] External Authority Notification - Process for reporting to regulatory and law enforcement agencies
- [PROC-04] Incident Documentation - Requirements for recording incident details and response actions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major incidents, regulatory changes, organizational restructuring, audit findings

## 7. SCENARIO PATTERNS

[SCENARIO-01: Critical System Breach]
IF incident_type = "data_breach"
AND affected_systems = "critical"
AND report_time > 1_hour
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Delayed Privacy Incident Reporting]
IF incident_involves_pii = TRUE
AND discovery_time < current_time - 72_hours
AND external_authority_notified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Incomplete Incident Documentation]
IF incident_reported = TRUE
AND required_fields_complete < 100%
AND documentation_time < 2_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Contractor Incident Reporting]
IF reporter_type = "contractor"
AND incident_suspected = TRUE
AND report_submitted = TRUE
AND report_time <= 4_hours
THEN compliance = TRUE

[SCENARIO-05: Investigation Delay Violation]
IF preliminary_investigation = TRUE
AND investigation_duration > 1_hour
AND incident_severity = "critical"
AND total_report_time > 1_hour
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel report suspected incidents within defined timeframes | RULE-01 |
| Incident information reported to designated authorities | RULE-02 |
| Complete incident documentation maintained | RULE-03, RULE-05 |
| No inappropriate delays in reporting | RULE-04 |