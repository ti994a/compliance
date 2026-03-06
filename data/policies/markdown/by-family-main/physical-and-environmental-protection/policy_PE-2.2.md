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
All visitors seeking access to facilities housing information systems MUST present exactly two forms of identification from the organization's approved identification list. Acceptable forms of identification include government-issued photo ID, PIV cards, passports, REAL ID-compliant driver's licenses, and biometric credentials for automated access systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All visitors | YES | Non-employees seeking facility access |
| Contractors | YES | When accessing as visitors without permanent credentials |
| Employees | NO | Covered under separate access policies |
| Delivery personnel | YES | When requiring access beyond reception areas |
| Emergency responders | CONDITIONAL | During non-emergency situations only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Maintain approved identification forms list<br>• Define facility access requirements<br>• Oversee visitor access procedures |
| Security Guards/Reception | • Verify two forms of visitor identification<br>• Document visitor access attempts<br>• Escort visitors as required |
| Facility Manager | • Implement physical access controls<br>• Coordinate with security personnel<br>• Maintain access control systems |

## 4. RULES
[RULE-01] Visitors MUST present exactly two forms of identification from the approved identification list before being granted facility access.
[VALIDATION] IF visitor_id_count < 2 THEN access_denied

[RULE-02] All presented identification MUST be verified as authentic and belong to the presenting individual through visual inspection and system validation where applicable.
[VALIDATION] IF id_verification_status = "failed" OR id_authenticity = "questionable" THEN access_denied

[RULE-03] The organization MUST maintain a current list of acceptable identification forms that includes government-issued photo ID, PIV cards, passports, and REAL ID-compliant driver's licenses.
[VALIDATION] IF identification_list_last_updated > 365_days THEN policy_violation

[RULE-04] Visitor access attempts and identification verification results MUST be logged with timestamp, visitor identity, presented credentials, and access decision.
[VALIDATION] IF visitor_access_logged = FALSE THEN documentation_violation

[RULE-05] Automated access mechanisms MAY accept PIV cards, key cards, PINs, and biometric credentials as valid identification forms when two different types are presented.
[VALIDATION] IF automated_access = TRUE AND credential_types < 2 THEN access_denied

## 5. REQUIRED PROCEDURES
- [PROC-01] Visitor Identification Verification - Process for validating two forms of visitor identification
- [PROC-02] Access Credential Management - Maintenance of approved identification forms list
- [PROC-03] Visitor Access Logging - Documentation requirements for all visitor access attempts
- [PROC-04] Emergency Access Override - Procedures for emergency responder access during incidents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility changes, regulatory updates, identification technology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Valid Two-Form Access]
IF visitor_presents_count = 2
AND id_form_1 IN approved_list
AND id_form_2 IN approved_list
AND verification_successful = TRUE
THEN compliance = TRUE

[SCENARIO-02: Insufficient Identification]
IF visitor_presents_count = 1
AND id_verification = "valid"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Automated System Access]
IF access_method = "automated"
AND credential_type_1 = "PIV_card"
AND credential_type_2 = "biometric"
AND both_verified = TRUE
THEN compliance = TRUE

[SCENARIO-04: Emergency Responder Override]
IF visitor_type = "emergency_responder"
AND emergency_active = TRUE
AND override_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Expired Identification]
IF visitor_presents_count = 2
AND id_form_1_expired = TRUE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Two forms of identification required for visitor access | [RULE-01] |
| Acceptable forms of identification defined | [RULE-03] |
| Identification verification process | [RULE-02] |
| Access logging and documentation | [RULE-04] |
| Automated mechanism requirements | [RULE-05] |