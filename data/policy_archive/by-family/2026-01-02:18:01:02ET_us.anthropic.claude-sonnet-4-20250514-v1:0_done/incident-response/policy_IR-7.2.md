# POLICY: IR-7.2: Coordination with External Providers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IR-7.2 |
| NIST Control | IR-7.2: Coordination with External Providers |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | incident response, external providers, coordination, cooperative relationship, team identification |

## 1. POLICY STATEMENT
The organization SHALL establish direct, cooperative relationships with external system protection providers and identify incident response team members to these providers. These relationships enable coordinated incident detection, analysis, and response capabilities across organizational boundaries.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud and hybrid environments |
| Incident Response Teams | YES | All organizational IR personnel |
| External Security Providers | YES | Third-party monitoring and protection services |
| Contractors with IR Roles | YES | When performing incident response functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve external provider relationships<br>• Oversee coordination agreements<br>• Ensure compliance with policy |
| IR Team Lead | • Establish operational relationships with providers<br>• Maintain current team member identification<br>• Coordinate incident response activities |
| Legal/Contracts | • Review and approve provider agreements<br>• Ensure appropriate liability and confidentiality terms |

## 4. RULES
[RULE-01] The organization MUST establish formal, documented cooperative relationships with external providers of system protection capability before relying on their services.
[VALIDATION] IF external_provider_used = TRUE AND formal_relationship_documented = FALSE THEN violation

[RULE-02] Incident response team member contact information MUST be provided to external providers within 30 days of team changes.
[VALIDATION] IF team_member_change_date + 30_days < current_date AND provider_notification_sent = FALSE THEN violation

[RULE-03] Cooperative relationships MUST include defined roles, responsibilities, communication protocols, and escalation procedures.
[VALIDATION] IF cooperative_agreement_exists = TRUE AND (roles_defined = FALSE OR communication_protocols = FALSE OR escalation_procedures = FALSE) THEN violation

[RULE-04] External provider agreements SHALL include data sharing limitations, confidentiality requirements, and incident notification timeframes.
[VALIDATION] IF provider_agreement = TRUE AND (data_sharing_limits = FALSE OR confidentiality_terms = FALSE OR notification_timeframes = FALSE) THEN violation

[RULE-05] The organization MUST maintain current emergency contact information for all external providers and test communication channels quarterly.
[VALIDATION] IF last_communication_test + 90_days < current_date THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Provider Relationship Establishment - Process for vetting, contracting, and onboarding external security providers
- [PROC-02] Team Member Identification Management - Procedure for maintaining current IR team rosters with external providers
- [PROC-03] Incident Coordination Protocol - Guidelines for coordinating incident response activities with external providers
- [PROC-04] Communication Channel Testing - Quarterly verification of communication pathways with providers

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major incidents involving external providers, provider contract changes, significant IR team changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New External Provider Onboarding]
IF new_external_provider = TRUE
AND formal_agreement_signed = FALSE
AND services_initiated = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: IR Team Member Changes]
IF team_member_departed = TRUE
AND departure_date + 30_days < current_date
AND provider_notification_complete = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incident Coordination Without Relationship]
IF security_incident_occurred = TRUE
AND external_provider_assistance_needed = TRUE
AND formal_relationship_exists = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated Communication Channels]
IF last_communication_test + 90_days < current_date
AND external_provider_relationship_active = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Complete Coordination Framework]
IF formal_relationship_documented = TRUE
AND current_team_roster_provided = TRUE
AND communication_channels_tested = TRUE
AND roles_responsibilities_defined = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Direct, cooperative relationship established | RULE-01, RULE-03 |
| IR team members identified to external providers | RULE-02 |
| Communication protocols defined | RULE-03, RULE-05 |
| Data sharing and confidentiality controls | RULE-04 |