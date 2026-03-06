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
All designated online meetings and teleconferences MUST provide explicit visual or audible indication of current participants to prevent unauthorized individuals from participating without the knowledge of other attendees. The organization SHALL define which types of meetings and teleconferences require explicit participant indication based on sensitivity and business requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Applies when hosting or participating in designated meetings |
| Contractors | YES | Same requirements as employees |
| External participants | YES | Must be clearly identified in participant lists |
| Video conferencing platforms | YES | Must support explicit participant indication |
| Audio-only teleconferences | CONDITIONAL | Only those designated as requiring participant indication |
| Internal collaboration tools | YES | All tools used for multi-party communication |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define meeting types requiring participant indication<br>• Approve collaboration platform configurations<br>• Monitor compliance with participant indication requirements |
| IT Security Team | • Configure collaboration platforms for participant indication<br>• Monitor and audit meeting participant logs<br>• Investigate unauthorized participation incidents |
| Meeting Hosts | • Enable participant indication features<br>• Verify participant identities before sensitive discussions<br>• Report suspected unauthorized participants |

## 4. RULES
[RULE-01] The organization MUST define and document which types of online meetings and teleconferences require explicit participant indication based on data classification and business sensitivity.
[VALIDATION] IF meeting_type_defined = FALSE OR documentation_exists = FALSE THEN violation

[RULE-02] All collaboration platforms used for designated meeting types MUST be configured to display current participants explicitly through visual participant lists or audible announcements.
[VALIDATION] IF platform_configured = FALSE AND meeting_type IN designated_types THEN violation

[RULE-03] Meeting hosts MUST enable participant indication features for all meetings designated as requiring explicit participant indication.
[VALIDATION] IF meeting_type IN designated_types AND participant_indication_enabled = FALSE THEN violation

[RULE-04] Participant lists MUST be visible or audible to all authorized participants throughout the duration of designated meetings.
[VALIDATION] IF participant_list_visible = FALSE AND meeting_active = TRUE AND meeting_type IN designated_types THEN violation

[RULE-05] Meeting hosts MUST verify the identity of participants before discussing sensitive information in meetings requiring explicit participant indication.
[VALIDATION] IF sensitive_discussion = TRUE AND participant_verification_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Meeting Type Classification - Process for determining which meetings require participant indication
- [PROC-02] Platform Configuration Management - Procedures for configuring collaboration tools with participant indication features
- [PROC-03] Participant Verification - Process for verifying participant identities in sensitive meetings
- [PROC-04] Incident Response - Procedures for responding to unauthorized participant detection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized meeting access, new collaboration platform deployments, changes to data classification standards

## 7. SCENARIO PATTERNS
[SCENARIO-01: Sensitive Meeting Without Participant List]
IF meeting_classification = "confidential"
AND participant_indication_enabled = FALSE
AND meeting_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unverified External Participant]
IF participant_type = "external"
AND identity_verified = FALSE
AND sensitive_discussion = TRUE
AND meeting_type IN designated_types
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Platform Missing Participant Features]
IF collaboration_platform_approved = TRUE
AND participant_indication_capability = FALSE
AND used_for_designated_meetings = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Compliant Internal Meeting]
IF meeting_type = "internal_status"
AND meeting_classification = "internal"
AND participant_indication_required = FALSE
THEN compliance = TRUE

[SCENARIO-05: Properly Configured Executive Meeting]
IF meeting_type = "executive_briefing"
AND participant_list_visible = TRUE
AND all_participants_verified = TRUE
AND meeting_type IN designated_types
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Define meetings requiring participant indication | [RULE-01] |
| Configure platforms for participant indication | [RULE-02] |
| Enable participant indication features | [RULE-03] |
| Maintain visible participant lists | [RULE-04] |
| Verify participant identities | [RULE-05] |