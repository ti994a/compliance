```markdown
# POLICY: SC-15.4: Explicitly Indicate Current Participants

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-15.4 |
| NIST Control | SC-15.4: Explicitly Indicate Current Participants |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | collaborative computing, online meetings, teleconferences, participant indication, unauthorized access |

## 1. POLICY STATEMENT
All online meetings and teleconferences must provide explicit indication of current participants to prevent unauthorized individuals from participating without other participants' knowledge. Organizations must define which types of meetings require participant indication and implement technical controls to display current participants.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Video conferencing systems | YES | All platforms used for business meetings |
| Audio-only teleconferences | CONDITIONAL | When handling sensitive information |
| Internal collaboration tools | YES | Teams, Slack, WebEx, etc. |
| External meeting platforms | YES | Zoom, Google Meet, third-party tools |
| Recorded meetings | YES | Participant lists must be captured |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Define meeting types requiring participant indication<br>• Configure collaboration platforms<br>• Monitor compliance with participant display requirements |
| Meeting Organizers | • Enable participant indication features<br>• Verify participant identity before sensitive discussions<br>• Document participants for compliance meetings |
| System Administrators | • Implement technical controls for participant display<br>• Maintain audit logs of meeting participants<br>• Ensure platform configurations meet policy requirements |

## 4. RULES
[RULE-01] All collaboration platforms MUST be configured to display current participants by default for meetings containing sensitive information.
[VALIDATION] IF meeting_sensitivity = "sensitive" AND participant_display = FALSE THEN violation

[RULE-02] Meeting organizers MUST verify that participant indication is active before discussing confidential, regulated, or proprietary information.
[VALIDATION] IF information_type IN ["confidential", "regulated", "proprietary"] AND participant_verification = FALSE THEN violation

[RULE-03] Organizations MUST maintain a defined list of meeting types that require explicit participant indication, including but not limited to SOX, FedRAMP, and PCI-DSS related discussions.
[VALIDATION] IF meeting_type IN compliance_required_list AND participant_indication = undefined THEN violation

[RULE-04] Collaboration platforms MUST NOT allow anonymous or unnamed participants in meetings handling regulated data.
[VALIDATION] IF data_classification = "regulated" AND anonymous_participants > 0 THEN critical_violation

[RULE-05] Participant lists MUST be logged and retained for compliance meetings for minimum 7 years per regulatory requirements.
[VALIDATION] IF meeting_type = "compliance" AND participant_log_retention < 7_years THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Meeting Classification Procedure - Process for determining which meetings require participant indication
- [PROC-02] Platform Configuration Procedure - Steps to configure collaboration tools for participant display
- [PROC-03] Participant Verification Procedure - Methods for verifying participant identity in sensitive meetings
- [PROC-04] Audit Logging Procedure - Requirements for capturing and retaining participant information

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New collaboration platform deployment, security incidents involving unauthorized meeting access, regulatory requirement changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: SOX Compliance Meeting]
IF meeting_type = "SOX_compliance"
AND participant_indication = FALSE
AND financial_data_discussed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: External Participant Access]
IF external_participants > 0
AND participant_verification = FALSE
AND proprietary_information = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Anonymous User in Regulated Discussion]
IF anonymous_participants > 0
AND data_classification IN ["PCI", "FedRAMP", "FISMA"]
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Internal Team Meeting]
IF all_participants = "internal_employees"
AND information_type = "general_business"
AND participant_display = TRUE
THEN compliance = TRUE

[SCENARIO-05: Recorded Compliance Meeting]
IF meeting_recorded = TRUE
AND meeting_type = "compliance"
AND participant_list_captured = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Explicit indication of current participants is provided | [RULE-01], [RULE-02] |
| Meeting types requiring participant indication are defined | [RULE-03] |
| Unauthorized participation prevention | [RULE-04] |
| Audit trail maintenance | [RULE-05] |
```