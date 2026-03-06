```markdown
# POLICY: SC-15: Collaborative Computing Devices and Applications

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-15 |
| NIST Control | SC-15: Collaborative Computing Devices and Applications |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | collaborative computing, remote activation, cameras, microphones, conferencing, privacy indicators |

## 1. POLICY STATEMENT
Remote activation of collaborative computing devices and applications is prohibited except for explicitly defined and approved exceptions. All collaborative computing devices MUST provide clear visual or audible indication when active to users physically present at the device location.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Conference room cameras/microphones | YES | All meeting room equipment |
| Desktop/laptop webcams | YES | Company-owned and BYOD devices |
| Networked whiteboards | YES | Interactive display systems |
| Remote meeting applications | YES | Zoom, Teams, WebEx, etc. |
| IP phones with video | YES | VoIP systems with camera capability |
| IoT devices with A/V capability | YES | Smart displays, voice assistants |
| Personal mobile devices | CONDITIONAL | Only when used for business |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Define remote activation exceptions<br>• Monitor compliance with indicator requirements<br>• Maintain approved device inventory |
| Facilities Management | • Ensure proper installation of indicator systems<br>• Coordinate physical security with device placement |
| Device Administrators | • Configure devices per policy requirements<br>• Implement and test indicator mechanisms<br>• Document exception approvals |

## 4. RULES

[RULE-01] Remote activation of collaborative computing devices SHALL be prohibited by default unless explicitly included in the approved exceptions list.
[VALIDATION] IF device_type = "collaborative_computing" AND remote_activation_enabled = TRUE AND approved_exception = FALSE THEN violation

[RULE-02] All collaborative computing devices MUST provide explicit visual or audible indication when recording, transmitting, or otherwise active.
[VALIDATION] IF device_status = "active" AND (visual_indicator = FALSE AND audible_indicator = FALSE) THEN violation

[RULE-03] Exception requests for remote activation MUST be documented, risk-assessed, and approved by IT Security before implementation.
[VALIDATION] IF remote_activation_exception = TRUE AND (documented = FALSE OR risk_assessed = FALSE OR security_approved = FALSE) THEN violation

[RULE-04] Visual indicators MUST be clearly visible to all users within the device's capture range and SHALL NOT be easily disabled or obscured.
[VALIDATION] IF visual_indicator_present = TRUE AND (easily_disabled = TRUE OR easily_obscured = TRUE) THEN violation

[RULE-05] Remote activation exceptions SHALL be reviewed and reapproved annually or when device configuration changes.
[VALIDATION] IF exception_approval_date < (current_date - 365_days) OR device_config_changed = TRUE THEN review_required

## 5. REQUIRED PROCEDURES
- [PROC-01] Device Inventory Management - Maintain current inventory of all collaborative computing devices
- [PROC-02] Exception Request Process - Document process for requesting and approving remote activation exceptions
- [PROC-03] Indicator Testing Protocol - Regular testing of visual and audible indicators
- [PROC-04] Incident Response - Process for addressing unauthorized remote activation attempts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New device deployments, security incidents, technology changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Conference Room Camera with Remote Admin Access]
IF device_type = "conference_camera"
AND remote_activation_capability = TRUE
AND approved_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved Remote Activation with Indicators]
IF device_type = "collaborative_computing"
AND remote_activation_enabled = TRUE
AND approved_exception = TRUE
AND visual_indicator_functional = TRUE
THEN compliance = TRUE

[SCENARIO-03: Active Device Without Indication]
IF device_status = "recording"
AND users_present = TRUE
AND visual_indicator = FALSE
AND audible_indicator = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Expired Exception Approval]
IF remote_activation_exception = TRUE
AND exception_approval_date < (current_date - 365_days)
AND reapproval_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Disabled Privacy Indicator]
IF device_type = "webcam"
AND privacy_indicator_disabled = TRUE
AND device_status = "active"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Remote activation prohibition with defined exceptions | [RULE-01], [RULE-03] |
| Explicit indication of use to physically present users | [RULE-02], [RULE-04] |
| Exception documentation and approval | [RULE-03], [RULE-05] |
| Indicator functionality and visibility | [RULE-02], [RULE-04] |
```