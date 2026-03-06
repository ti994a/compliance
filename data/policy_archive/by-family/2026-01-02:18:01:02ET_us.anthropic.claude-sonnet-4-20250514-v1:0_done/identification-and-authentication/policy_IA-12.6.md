# POLICY: IA-12.6: Accept Externally-proofed Identities

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-12.6 |
| NIST Control | IA-12.6: Accept Externally-proofed Identities |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | externally-proofed identities, identity assurance level, federated identities, proofing, PIV, non-PIV users |

## 1. POLICY STATEMENT
The organization SHALL accept externally-proofed identities from trusted external agencies or organizations at defined identity assurance levels to limit unnecessary re-proofing. Acceptance of external proofing MUST be consistent with organizational security policy and appropriate for the assurance level required by the system, application, or information being accessed.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Systems accepting federated identities |
| External users | YES | Non-PIV users from trusted organizations |
| Service providers | YES | Cloud and SaaS providers with federated access |
| Partner organizations | YES | Organizations with established trust relationships |
| Internal employees | CONDITIONAL | Only when using externally-proofed credentials |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity Management Team | • Define identity assurance levels for external proofing<br>• Maintain list of trusted external proofing authorities<br>• Establish technical integration requirements |
| System Owners | • Determine appropriate assurance levels for their systems<br>• Configure systems to accept approved external identities<br>• Document external identity acceptance criteria |
| Security Team | • Assess external proofing authorities for trustworthiness<br>• Monitor compliance with external identity policies<br>• Review and approve trust relationships |

## 4. RULES
[RULE-01] Organizations MUST define specific identity assurance levels required for accepting externally-proofed identities for each system or application.
[VALIDATION] IF system_has_external_users = TRUE AND assurance_level_defined = FALSE THEN violation

[RULE-02] External proofing authorities MUST be formally assessed and approved before their proofed identities can be accepted.
[VALIDATION] IF external_authority_used = TRUE AND formal_approval = FALSE THEN critical_violation

[RULE-03] The assurance level of externally-proofed identities MUST be commensurate with or exceed the minimum assurance level required by the target system.
[VALIDATION] IF external_assurance_level < required_assurance_level THEN violation

[RULE-04] Organizations MUST maintain documentation of all approved external proofing authorities and their corresponding assurance levels.
[VALIDATION] IF external_authority_count > 0 AND documentation_current = FALSE THEN violation

[RULE-05] External identity acceptance criteria MUST be reviewed and revalidated at least annually or when trust relationships change.
[VALIDATION] IF last_review_date > 365_days AND trust_relationship_active = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Proofing Authority Assessment - Formal evaluation process for approving external identity providers
- [PROC-02] Identity Assurance Level Mapping - Process for determining and documenting required assurance levels
- [PROC-03] Trust Relationship Management - Procedures for establishing, maintaining, and terminating external trust relationships
- [PROC-04] External Identity Monitoring - Ongoing validation of externally-proofed identity usage and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New external partnerships, security incidents involving external identities, changes in assurance level requirements, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Partner Organization Access]
IF user_type = "external"
AND proofing_authority = "approved_partner"
AND partner_assurance_level >= system_required_level
AND trust_agreement_active = TRUE
THEN compliance = TRUE

[SCENARIO-02: Insufficient Assurance Level]
IF user_type = "external"
AND external_assurance_level = "IAL1"
AND system_required_level = "IAL2"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unapproved External Authority]
IF user_type = "external"
AND proofing_authority NOT IN approved_authorities_list
AND system_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Expired Trust Relationship]
IF external_authority_used = TRUE
AND trust_agreement_expiration < current_date
AND access_still_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Proper Federal Agency Integration]
IF user_type = "external"
AND proofing_authority = "federal_agency"
AND piv_credential = TRUE
AND assurance_mapping_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Identity assurance level for accepting externally proofed identities is defined | [RULE-01] |
| Externally proofed identities are accepted at defined assurance levels | [RULE-03] |
| External proofing authorities are properly vetted | [RULE-02] |
| Documentation of external identity acceptance is maintained | [RULE-04] |
| Regular review of external trust relationships | [RULE-05] |