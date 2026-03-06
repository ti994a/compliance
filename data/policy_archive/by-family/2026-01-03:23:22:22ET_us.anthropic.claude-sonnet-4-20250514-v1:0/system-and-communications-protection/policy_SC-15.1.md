# POLICY: SC-15.1: Physical or Logical Disconnect

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-15.1 |
| NIST Control | SC-15.1: Physical or Logical Disconnect |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | collaborative computing, physical disconnect, ease of use, session termination |

## 1. POLICY STATEMENT
All collaborative computing devices MUST provide physical disconnect capabilities that support ease of use to prevent unauthorized access after sessions end. Disconnect procedures SHALL be simple, intuitive, and require minimal technical expertise to execute.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Video conferencing systems | YES | All organizational and personal devices |
| Shared workstations | YES | Public and semi-public access points |
| Interactive whiteboards | YES | Conference rooms and collaboration spaces |
| Telepresence equipment | YES | All remote collaboration tools |
| Mobile collaboration apps | YES | When used for organizational purposes |
| Personal devices | CONDITIONAL | Only when accessing organizational resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Manager | • Define disconnect requirements for collaborative devices<br>• Approve disconnect mechanisms and procedures<br>• Monitor compliance with disconnect policies |
| System Administrators | • Configure automatic disconnect features<br>• Implement physical disconnect capabilities<br>• Maintain disconnect mechanism functionality |
| End Users | • Execute proper disconnect procedures after sessions<br>• Report malfunctioning disconnect mechanisms<br>• Follow established disconnect protocols |

## 4. RULES
[RULE-01] All collaborative computing devices MUST provide a physical disconnect mechanism that can be activated without technical expertise.
[VALIDATION] IF device_type = "collaborative" AND physical_disconnect_available = FALSE THEN violation

[RULE-02] Physical disconnect procedures SHALL require no more than 3 user actions to complete successfully.
[VALIDATION] IF disconnect_steps > 3 THEN violation

[RULE-03] Collaborative devices MUST implement automatic disconnect after 15 minutes of inactivity for standard sessions and 5 minutes for sensitive sessions.
[VALIDATION] IF session_type = "standard" AND auto_disconnect_time > 15_minutes THEN violation
[VALIDATION] IF session_type = "sensitive" AND auto_disconnect_time > 5_minutes THEN violation

[RULE-04] Manual disconnect mechanisms MUST be clearly labeled and physically accessible to all authorized users.
[VALIDATION] IF disconnect_mechanism_labeled = FALSE OR disconnect_mechanism_accessible = FALSE THEN violation

[RULE-05] Disconnect functionality MUST be tested monthly and documented to ensure operational effectiveness.
[VALIDATION] IF last_disconnect_test > 30_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Device Disconnect Configuration - Standard procedures for implementing disconnect mechanisms on new collaborative devices
- [PROC-02] User Disconnect Training - Training program for proper disconnect procedures and troubleshooting
- [PROC-03] Disconnect Mechanism Testing - Monthly testing protocol for all disconnect capabilities
- [PROC-04] Incident Response for Failed Disconnects - Response procedures when disconnect mechanisms fail

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving collaborative devices, new device deployments, user feedback on disconnect difficulties

## 7. SCENARIO PATTERNS
[SCENARIO-01: Conference Room Video System]
IF device_type = "video_conferencing"
AND location = "conference_room"
AND physical_disconnect_button = TRUE
AND disconnect_steps <= 3
THEN compliance = TRUE

[SCENARIO-02: Shared Workstation Without Auto-Disconnect]
IF device_type = "shared_workstation"
AND auto_disconnect_enabled = FALSE
AND manual_disconnect_available = TRUE
AND user_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Mobile Device Extended Session]
IF device_type = "mobile_collaboration"
AND session_duration > 15_minutes
AND user_activity = "inactive"
AND auto_disconnect_triggered = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Sensitive Session Disconnect]
IF session_classification = "sensitive"
AND auto_disconnect_time <= 5_minutes
AND manual_disconnect_available = TRUE
AND disconnect_mechanism_tested = TRUE
THEN compliance = TRUE

[SCENARIO-05: Failed Disconnect Mechanism]
IF disconnect_mechanism_functional = FALSE
AND last_test_date > 30_days
AND alternative_disconnect_method = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical disconnect provided in manner supporting ease of use | [RULE-01], [RULE-02], [RULE-04] |
| Disconnect mechanism functionality verification | [RULE-05] |
| Automated disconnect capability | [RULE-03] |
| User accessibility to disconnect features | [RULE-04] |