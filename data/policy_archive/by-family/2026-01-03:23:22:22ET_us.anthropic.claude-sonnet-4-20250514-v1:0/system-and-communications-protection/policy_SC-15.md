# POLICY: SC-15: Collaborative Computing Devices and Applications

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-15 |
| NIST Control | SC-15: Collaborative Computing Devices and Applications |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | collaborative computing, remote activation, cameras, microphones, meeting devices, privacy indicators |

## 1. POLICY STATEMENT
The organization prohibits unauthorized remote activation of collaborative computing devices and applications to prevent unauthorized surveillance and privacy violations. All collaborative computing devices must provide explicit visual or audible indicators when activated and in use.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Conference room cameras/microphones | YES | All meeting room equipment |
| Employee workstation cameras/microphones | YES | Laptops, desktops, mobile devices |
| Networked whiteboards | YES | Interactive displays with network connectivity |
| Video conferencing systems | YES | Dedicated VC equipment and software |
| Third-party collaboration apps | YES | Teams, Zoom, WebEx, etc. |
| Personal devices (BYOD) | CONDITIONAL | Only when accessing corporate resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Define approved remote activation exceptions<br>• Monitor compliance with activation controls<br>• Investigate unauthorized activation incidents |
| Facilities Management | • Ensure physical indicator mechanisms function properly<br>• Maintain inventory of collaborative computing devices<br>• Coordinate device installation and configuration |
| Device Users | • Report malfunctioning privacy indicators<br>• Follow approved procedures for device activation<br>• Report suspected unauthorized activations |

## 4. RULES
[RULE-01] Remote activation of collaborative computing devices SHALL be prohibited by default unless explicitly authorized through documented exceptions.
[VALIDATION] IF device_type = "collaborative_computing" AND remote_activation = TRUE AND documented_exception = FALSE THEN violation

[RULE-02] All collaborative computing devices MUST provide explicit visual or audible indication when activated and in use.
[VALIDATION] IF device_status = "active" AND privacy_indicator = FALSE THEN critical_violation

[RULE-03] Approved remote activation exceptions MUST be documented with business justification, security controls, and approval from IT Security.
[VALIDATION] IF remote_activation_exception = TRUE AND (business_justification = FALSE OR security_approval = FALSE) THEN violation

[RULE-04] Privacy indicators MUST be tested monthly to ensure proper functionality and cannot be disabled by users.
[VALIDATION] IF indicator_test_date < (current_date - 30_days) THEN violation
[VALIDATION] IF user_disable_capability = TRUE THEN violation

[RULE-05] Collaborative computing devices MUST be configured to prevent unauthorized remote access through firmware settings and network controls.
[VALIDATION] IF firmware_remote_access = "enabled" AND authorization_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Device Configuration Standards - Standard configurations preventing unauthorized remote activation
- [PROC-02] Privacy Indicator Testing - Monthly verification of visual/audible indicators
- [PROC-03] Exception Management - Process for requesting and approving remote activation exceptions
- [PROC-04] Incident Response - Response procedures for suspected unauthorized activations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, new device deployments, regulatory changes, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Conference Room Camera Remote Activation]
IF device_type = "conference_camera"
AND remote_activation = TRUE
AND documented_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Privacy Indicator]
IF device_status = "recording"
AND privacy_light = FALSE
AND audible_indicator = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Approved Remote Access Exception]
IF device_type = "collaborative_computing"
AND remote_activation = TRUE
AND security_approval = TRUE
AND business_justification_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: User-Disabled Privacy Indicator]
IF privacy_indicator_status = "disabled"
AND disabled_by = "user"
AND device_in_use = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Overdue Indicator Testing]
IF last_indicator_test < (current_date - 35_days)
AND device_type = "collaborative_computing"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Remote activation is prohibited except for defined exceptions | [RULE-01], [RULE-03] |
| Explicit indication of use provided to physically present users | [RULE-02], [RULE-04] |
| Documented exception management process | [RULE-03] |
| Technical controls prevent unauthorized access | [RULE-05] |