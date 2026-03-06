# POLICY: IA-2.12: Acceptance of PIV Credentials

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-2.12 |
| NIST Control | IA-2.12: Acceptance of PIV Credentials |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | PIV, credentials, electronic verification, FIPS 201, authentication, access control |

## 1. POLICY STATEMENT
The organization SHALL accept and electronically verify Personal Identity Verification (PIV)-compliant credentials for both logical and physical access control systems. All PIV credentials MUST conform to FIPS Publication 201 standards and be issued by authorized federal agencies or approved issuers.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Logical Access Control Systems | YES | All systems requiring authentication |
| Physical Access Control Systems | YES | All facilities with PIV capability |
| PIV-Compliant Credentials | YES | Including derived PIV credentials |
| Common Access Cards (CAC) | YES | DOD CAC as example PIV credential |
| Third-party Credentials | NO | Unless PIV-compliant and authorized |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Policy oversight and compliance monitoring<br>• Authorization of PIV issuer adequacy<br>• Exception approval for non-PIV systems |
| System Administrators | • Configure systems to accept PIV credentials<br>• Implement electronic verification mechanisms<br>• Maintain PIV verification logs |
| Identity Management Team | • Validate PIV credential compliance<br>• Manage derived PIV credential processes<br>• Coordinate with authorized PIV issuers |

## 4. RULES
[RULE-01] All access control systems capable of PIV authentication MUST be configured to accept PIV-compliant credentials.
[VALIDATION] IF system_supports_piv = TRUE AND piv_acceptance_enabled = FALSE THEN violation

[RULE-02] PIV credentials MUST be electronically verified against the issuing authority before granting access.
[VALIDATION] IF piv_credential_presented = TRUE AND electronic_verification_performed = FALSE THEN critical_violation

[RULE-03] Only PIV credentials issued by federal agencies or SP 800-79-2 authorized issuers SHALL be accepted.
[VALIDATION] IF piv_issuer_authorized = FALSE AND credential_accepted = TRUE THEN violation

[RULE-04] Derived PIV credentials MUST comply with SP 800-166 guidance when accepted for authentication.
[VALIDATION] IF credential_type = "derived_piv" AND sp800_166_compliant = FALSE THEN violation

[RULE-05] PIV verification activities MUST be logged and records retained for audit purposes.
[VALIDATION] IF piv_verification_occurred = TRUE AND verification_logged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PIV Credential Verification - Electronic validation against issuing authority
- [PROC-02] Authorized Issuer Management - Maintain list of SP 800-79-2 authorized PIV issuers
- [PROC-03] Derived PIV Credential Handling - Process for accepting derived credentials per SP 800-166
- [PROC-04] PIV Verification Logging - Audit trail maintenance for verification activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: FIPS 201 updates, SP 800-79-2 changes, new PIV issuer authorizations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard PIV Authentication]
IF credential_type = "PIV"
AND issuer_authorized = TRUE
AND electronic_verification = TRUE
AND verification_successful = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unauthorized PIV Issuer]
IF credential_type = "PIV"
AND issuer_authorized = FALSE
AND credential_accepted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Electronic Verification]
IF credential_type = "PIV"
AND issuer_authorized = TRUE
AND electronic_verification = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Derived PIV Non-Compliance]
IF credential_type = "derived_PIV"
AND sp800_166_compliant = FALSE
AND credential_accepted = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: PIV-Capable System Not Configured]
IF system_supports_piv = TRUE
AND piv_acceptance_enabled = FALSE
AND alternative_auth_only = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Accept PIV-compliant credentials | [RULE-01] |
| Electronically verify PIV credentials | [RULE-02] |
| Use authorized PIV issuers only | [RULE-03] |
| Handle derived PIV per SP 800-166 | [RULE-04] |
| Maintain verification audit trail | [RULE-05] |