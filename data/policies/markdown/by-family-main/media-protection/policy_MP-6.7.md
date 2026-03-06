# POLICY: MP-6.7: Dual Authorization for Media Sanitization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-6.7 |
| NIST Control | MP-6.7: Dual Authorization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | dual authorization, media sanitization, two-person control, media disposal, storage media |

## 1. POLICY STATEMENT
The organization SHALL enforce dual authorization for the sanitization of designated system media to ensure proper destruction of sensitive data. Two technically qualified individuals MUST conduct and verify all sanitization activities for media containing sensitive information.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Storage media containing CUI/PII/PHI | YES | All designated sensitive media |
| Standard business data storage | CONDITIONAL | Based on data classification |
| Cloud storage instances | YES | When organization controls sanitization |
| Mobile devices | YES | When containing sensitive data |
| Backup media | YES | All backup media with sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Media Sanitization Officer | • Designate media requiring dual authorization<br>• Maintain authorized personnel list<br>• Oversee sanitization procedures |
| Authorized Sanitization Personnel | • Perform sanitization activities<br>• Document sanitization actions<br>• Verify completion of sanitization |
| IT Security Manager | • Define technical qualifications<br>• Monitor compliance<br>• Manage rotation schedules |

## 4. RULES
[RULE-01] Organizations MUST designate which system media requires dual authorization for sanitization based on data classification and sensitivity levels.
[VALIDATION] IF media_contains_sensitive_data = TRUE AND dual_auth_designation = FALSE THEN violation

[RULE-02] Two technically qualified individuals MUST be present and actively participate in all sanitization activities for designated media.
[VALIDATION] IF sanitization_personnel_count < 2 AND media_requires_dual_auth = TRUE THEN critical_violation

[RULE-03] Both authorized individuals MUST independently verify and document the completion of sanitization procedures.
[VALIDATION] IF verification_signatures < 2 AND dual_auth_required = TRUE THEN violation

[RULE-04] Organizations MUST maintain a current list of personnel authorized to perform dual authorization sanitization activities.
[VALIDATION] IF personnel_authorization_status = "expired" AND sanitization_performed = TRUE THEN violation

[RULE-05] Dual authorization personnel SHOULD be rotated periodically to reduce collusion risk, with rotation occurring at least annually.
[VALIDATION] IF personnel_rotation_period > 365_days THEN advisory_finding

[RULE-06] All dual authorization sanitization activities MUST be documented with timestamps, personnel identities, and verification signatures.
[VALIDATION] IF sanitization_record_complete = FALSE AND dual_auth_performed = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Classification and Designation - Process for identifying media requiring dual authorization
- [PROC-02] Personnel Authorization and Training - Qualification and authorization of sanitization personnel
- [PROC-03] Dual Authorization Sanitization - Step-by-step sanitization procedures requiring two-person control
- [PROC-04] Documentation and Record Keeping - Requirements for sanitization records and audit trails

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when sanitization methods change
- Triggering events: Security incidents involving media, changes in data classification, new sanitization technologies

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Dual Authorization Sanitization]
IF media_classification = "sensitive"
AND sanitization_personnel_count = 2
AND both_personnel_authorized = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-02: Single Person Sanitization]
IF media_requires_dual_auth = TRUE
AND sanitization_personnel_count = 1
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Unauthorized Personnel Sanitization]
IF personnel_1_authorized = FALSE
OR personnel_2_authorized = FALSE
AND dual_auth_sanitization_performed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Documentation]
IF dual_auth_sanitization_performed = TRUE
AND sanitization_record_exists = FALSE
OR verification_signatures < 2
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Collusion Risk - No Rotation]
IF personnel_rotation_period > 730_days
AND same_personnel_pair = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dual authorization for sanitization is enforced | [RULE-02], [RULE-03] |
| Media requiring dual authorization is defined | [RULE-01] |
| Personnel qualifications are maintained | [RULE-04] |
| Sanitization activities are documented | [RULE-06] |
| Collusion risks are mitigated | [RULE-05] |