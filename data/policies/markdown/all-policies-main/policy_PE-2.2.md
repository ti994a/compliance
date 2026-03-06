# POLICY: PE-2.2: Two Forms of Identification

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-2.2 |
| NIST Control | PE-2.2: Two Forms of Identification |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | visitor access, identification, facility access, PIV cards, biometrics |

## 1. POLICY STATEMENT
All visitors accessing facilities where information systems reside MUST present two forms of identification from an organization-approved list of acceptable identification types. This policy ensures proper visitor authentication and maintains facility security through multi-factor identification verification.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All visitors | YES | Non-employees requiring facility access |
| Contractors | YES | When accessing as visitors without permanent credentials |
| Employees | NO | Covered under separate employee access controls |
| Delivery personnel | YES | When requiring access beyond reception areas |
| Emergency responders | CONDITIONAL | During non-emergency situations only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Maintain approved identification list<br>• Train security personnel on verification procedures<br>• Review and approve identification policy exceptions |
| Security Guards | • Verify two forms of visitor identification<br>• Document identification types in access logs<br>• Escalate identification discrepancies |
| Facility Managers | • Ensure compliance at all facility entry points<br>• Coordinate with security for access control implementation<br>• Report policy violations |

## 4. RULES
[RULE-01] Visitors MUST present exactly two forms of identification from the organization-approved list before facility access is granted.
[VALIDATION] IF visitor_id_count < 2 OR visitor_id_types NOT IN approved_list THEN access_denied

[RULE-02] Acceptable identification forms SHALL include passports, REAL ID-compliant driver's licenses, Personal Identity Verification (PIV) cards, military IDs, and government-issued photo IDs.
[VALIDATION] IF identification_type NOT IN [passport, real_id_license, piv_card, military_id, government_photo_id] THEN invalid_identification

[RULE-03] Security personnel MUST verify the authenticity of both identification forms and record the identification types in the visitor access log.
[VALIDATION] IF id_verification_completed = FALSE OR access_log_entry = NULL THEN procedure_violation

[RULE-04] Automated access mechanisms MAY accept PIV cards, key cards, PINs, and biometrics as valid identification forms when two different types are used.
[VALIDATION] IF automated_access = TRUE AND (auth_factor_count < 2 OR auth_factor_types_same = TRUE) THEN access_denied

[RULE-05] Expired or damaged identification forms MUST NOT be accepted as valid identification regardless of other credentials presented.
[VALIDATION] IF identification_expired = TRUE OR identification_damaged = TRUE THEN invalid_identification

## 5. REQUIRED PROCEDURES
- [PROC-01] Visitor Identification Verification - Standard process for validating two forms of ID
- [PROC-02] Identification Exception Handling - Process for addressing invalid or missing identification
- [PROC-03] Access Log Documentation - Recording visitor identification details and access times
- [PROC-04] Automated System Configuration - Setting up multi-factor authentication for facility access

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, identification fraud attempts, regulatory changes, facility modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Visitor Access]
IF visitor_presents_passport = TRUE
AND visitor_presents_drivers_license = TRUE
AND both_ids_valid = TRUE
THEN compliance = TRUE

[SCENARIO-02: Insufficient Identification]
IF visitor_id_count = 1
AND security_guard_grants_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Invalid ID Type]
IF visitor_presents_student_id = TRUE
AND visitor_presents_credit_card = TRUE
AND security_accepts_access = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Automated Access Compliance]
IF access_method = "automated"
AND piv_card_used = TRUE
AND biometric_scan_used = TRUE
THEN compliance = TRUE

[SCENARIO-05: Expired Identification]
IF identification_1_expired = TRUE
AND identification_2_valid = TRUE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Two forms of identification required for visitor access | [RULE-01] |
| Acceptable forms of identification defined | [RULE-02] |
| Identification verification and documentation | [RULE-03] |
| Automated mechanism authentication requirements | [RULE-04] |
| Identification validity verification | [RULE-05] |