# POLICY: SC-15.4: Explicitly Indicate Current Participants

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-15.4 |
| NIST Control | SC-15.4: Explicitly Indicate Current Participants |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | online meetings, teleconferences, participants, collaborative computing, unauthorized access |

## 1. POLICY STATEMENT
All online meetings and teleconferences MUST provide explicit indication of current participants to prevent unauthorized individuals from participating without knowledge of other attendees. Organizations SHALL define which types of meetings require participant visibility and implement technical controls to display current participants.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Video conferencing systems | YES | All corporate-managed platforms |
| Audio-only teleconferences | YES | When participant lists are technically feasible |
| Internal meetings | YES | All business-related meetings |
| External client meetings | YES | When containing confidential information |
| Public webinars | CONDITIONAL | Only if containing sensitive business data |
| Personal devices | YES | When used for business meetings |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Meeting Organizers | • Enable participant visibility features<br>• Monitor participant lists during meetings<br>• Remove unauthorized participants immediately |
| IT Security Team | • Configure platforms to display participants by default<br>• Maintain approved meeting platform list<br>• Monitor for unauthorized meeting access |
| System Administrators | • Implement technical controls for participant indication<br>• Configure meeting room systems with participant displays<br>• Ensure platform compliance settings |

## 4. RULES
[RULE-01] All video conferencing platforms MUST display current participants by default and SHALL NOT allow this feature to be disabled for business meetings.
[VALIDATION] IF meeting_type = "business" AND participant_display = FALSE THEN critical_violation

[RULE-02] Meeting organizers MUST verify participant identity before discussing confidential information and SHALL remove any unidentified participants.
[VALIDATION] IF confidential_content = TRUE AND unidentified_participants > 0 THEN violation

[RULE-03] Audio-only teleconferences MUST announce participant names when joining/leaving OR provide alternative participant indication methods.
[VALIDATION] IF meeting_type = "audio_only" AND participant_announcement = FALSE AND participant_list = FALSE THEN violation

[RULE-04] Meeting platforms SHALL be configured to require explicit admission for external participants and MUST display their organization affiliation.
[VALIDATION] IF external_participant = TRUE AND auto_admit = TRUE THEN violation

[RULE-05] Waiting room functionality MUST be enabled for all meetings containing SOX, FedRAMP, or PCI-DSS related content.
[VALIDATION] IF meeting_classification IN ["SOX", "FedRAMP", "PCI-DSS"] AND waiting_room = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Meeting Platform Configuration - Standard settings for participant visibility across all approved platforms
- [PROC-02] Participant Verification Process - Steps for verifying identity of meeting attendees
- [PROC-03] Unauthorized Access Response - Immediate actions when unauthorized participants are detected
- [PROC-04] Meeting Classification Guidelines - Criteria for determining meeting sensitivity levels

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving meeting platforms, new platform deployments, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unidentified Participant in SOX Meeting]
IF meeting_classification = "SOX"
AND participant_identity_verified = FALSE
AND meeting_in_progress = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Disabled Participant List]
IF meeting_type = "business"
AND participant_display_enabled = FALSE
AND override_authorization = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: External Auto-Admit Enabled]
IF external_participants_expected = TRUE
AND auto_admit = TRUE
AND waiting_room = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Audio Conference Without Participant Indication]
IF meeting_type = "audio_only"
AND confidential_content = TRUE
AND participant_announcement = FALSE
AND participant_list_available = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Meeting Setup]
IF participant_display_enabled = TRUE
AND waiting_room = TRUE
AND identity_verification_completed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Explicit indication of current participants is provided | RULE-01, RULE-03 |
| Unauthorized participation prevention | RULE-02, RULE-04, RULE-05 |
| Meeting platform configuration compliance | RULE-01, RULE-04, RULE-05 |