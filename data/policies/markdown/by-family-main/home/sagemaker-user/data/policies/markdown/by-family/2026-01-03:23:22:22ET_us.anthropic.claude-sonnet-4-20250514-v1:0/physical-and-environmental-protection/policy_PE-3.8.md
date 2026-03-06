# POLICY: PE-3.8: Access Control Vestibules

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3.8 |
| NIST Control | PE-3.8: Access Control Vestibules |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | access control, vestibules, piggybacking, tailgating, physical security, interlocking doors |

## 1. POLICY STATEMENT
The organization SHALL employ access control vestibules at designated high-security facility locations to prevent unauthorized individuals from following authorized personnel into controlled access areas. Vestibules MUST utilize interlocking door systems that restrict passage and verify authorization before granting access to secure areas.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and secondary data centers |
| Executive Floors | YES | C-suite and board meeting areas |
| Security Operations Centers | YES | SOC and incident response facilities |
| R&D Labs | YES | Facilities containing proprietary technology |
| General Office Space | NO | Standard office areas with badge access |
| Public Areas | NO | Lobbies, cafeterias, common areas |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Define vestibule locations and requirements<br>• Maintain vestibule access control lists<br>• Monitor vestibule effectiveness |
| Facilities Management | • Install and maintain vestibule infrastructure<br>• Ensure proper functioning of interlocking systems<br>• Coordinate with security for access modifications |
| Security Operations | • Monitor vestibule access events<br>• Respond to vestibule security violations<br>• Conduct regular vestibule security assessments |

## 4. RULES
[RULE-01] Access control vestibules MUST be deployed at all facility locations designated as high-security areas in the Physical Security Assessment.
[VALIDATION] IF location_security_level = "high" AND vestibule_present = FALSE THEN violation

[RULE-02] Vestibule interlocking door systems MUST prevent both doors from being open simultaneously for more than 15 seconds during normal operation.
[VALIDATION] IF door1_open = TRUE AND door2_open = TRUE AND duration > 15_seconds THEN violation

[RULE-03] Vestibules MUST authenticate individual identity before granting access to the second door, preventing piggybacking attempts.
[VALIDATION] IF person_count > authenticated_count AND second_door_opened = TRUE THEN critical_violation

[RULE-04] Vestibule access events MUST be logged with timestamp, user identity, entry/exit status, and any anomalies detected.
[VALIDATION] IF vestibule_access = TRUE AND log_entry_created = FALSE THEN violation

[RULE-05] Vestibule systems MUST include visual monitoring capabilities and alert security personnel of access violations within 30 seconds.
[VALIDATION] IF violation_detected = TRUE AND security_alert_time > 30_seconds THEN violation

[RULE-06] Emergency egress from vestibules MUST be possible without authentication during fire alarm or emergency conditions.
[VALIDATION] IF emergency_alarm = TRUE AND egress_blocked = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Vestibule Location Assessment - Annual review of high-security areas requiring vestibule protection
- [PROC-02] Access Authorization Management - Process for granting and revoking vestibule access permissions
- [PROC-03] Incident Response - Procedures for responding to vestibule security violations and tailgating attempts
- [PROC-04] Maintenance and Testing - Regular testing of interlocking systems and emergency egress functions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility modifications, regulatory changes, technology upgrades

## 7. SCENARIO PATTERNS
[SCENARIO-01: Piggybacking Detection]
IF person_count_sensor = 2
AND authenticated_users = 1
AND second_door_request = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Door Interlock Failure]
IF door1_status = "open"
AND door2_status = "open"
AND duration > 15_seconds
AND emergency_mode = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Vestibule in High-Security Area]
IF facility_area_classification = "high_security"
AND vestibule_installed = FALSE
AND area_contains_sensitive_systems = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Emergency Egress Test]
IF emergency_alarm_active = TRUE
AND vestibule_egress_time > 5_seconds
AND occupant_present = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Logging Failure]
IF vestibule_access_event = TRUE
AND log_entry_timestamp = NULL
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Access control vestibules employed at defined locations | [RULE-01] |
| Prevention of unauthorized access through piggybacking | [RULE-03] |
| Proper functioning of interlocking door systems | [RULE-02] |
| Monitoring and alerting capabilities | [RULE-05] |
| Event logging and audit trail | [RULE-04] |
| Emergency egress capabilities | [RULE-06] |