# POLICY: IA-8.1: Acceptance of PIV Credentials from Other Agencies

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-8.1 |
| NIST Control | IA-8.1: Acceptance of PIV Credentials from Other Agencies |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | PIV, federal agencies, electronic verification, FIPS 201, credentials, authentication |

## 1. POLICY STATEMENT
The organization SHALL accept and electronically verify Personal Identity Verification (PIV)-compliant credentials from other federal agencies for both logical and physical access control systems. All PIV credentials MUST conform to FIPS Publication 201 standards and be issued by authorized federal agencies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All access control systems | YES | Both logical and physical systems |
| Federal agency PIV credentials | YES | FIPS 201 compliant only |
| Non-federal PIV credentials | NO | Federal agencies only |
| Legacy authentication systems | CONDITIONAL | Must support PIV verification |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish PIV acceptance policies<br>• Oversee compliance monitoring<br>• Approve PIV issuer authorizations |
| System Administrators | • Configure PIV verification mechanisms<br>• Maintain PIV validation systems<br>• Monitor authentication logs |
| Security Operations | • Verify PIV credential authenticity<br>• Investigate authentication failures<br>• Maintain PIV verification records |

## 4. RULES
[RULE-01] All access control systems MUST accept PIV credentials from authorized federal agencies that conform to FIPS Publication 201 standards.
[VALIDATION] IF piv_credential_source = "federal_agency" AND fips_201_compliant = TRUE AND system_accepts_piv = FALSE THEN violation

[RULE-02] PIV credentials MUST be electronically verified using cryptographic validation mechanisms before granting access.
[VALIDATION] IF piv_presented = TRUE AND electronic_verification = FALSE THEN critical_violation

[RULE-03] Only PIV credentials from federal agencies authorized under SP 800-79-2 SHALL be accepted for authentication.
[VALIDATION] IF piv_issuer NOT IN authorized_federal_agencies THEN violation

[RULE-04] PIV verification systems MUST maintain audit logs of all authentication attempts and verification results.
[VALIDATION] IF piv_authentication_attempt = TRUE AND audit_log_created = FALSE THEN violation

[RULE-05] PIV credential verification failures MUST be logged and investigated within 24 hours.
[VALIDATION] IF piv_verification_failure = TRUE AND investigation_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PIV Credential Verification - Electronic validation of PIV credentials using FIPS 201 standards
- [PROC-02] Federal Agency Authorization - Verification of PIV issuer authorization under SP 800-79-2
- [PROC-03] PIV Authentication Logging - Comprehensive logging of all PIV authentication events
- [PROC-04] PIV Failure Investigation - Investigation and response to PIV verification failures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: FIPS 201 updates, new federal agency authorizations, PIV system changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Valid Federal PIV Authentication]
IF credential_type = "PIV"
AND issuer_type = "federal_agency"
AND fips_201_compliant = TRUE
AND electronic_verification = TRUE
THEN compliance = TRUE

[SCENARIO-02: Non-Federal PIV Credential]
IF credential_type = "PIV"
AND issuer_type = "state_government"
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: PIV Without Electronic Verification]
IF credential_type = "PIV"
AND issuer_type = "federal_agency"
AND verification_method = "visual_only"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Unauthorized Federal Issuer]
IF credential_type = "PIV"
AND issuer_type = "federal_agency"
AND sp_800_79_2_authorized = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing PIV Audit Logs]
IF piv_authentication_occurred = TRUE
AND audit_log_exists = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Accept PIV credentials from federal agencies | [RULE-01] |
| Electronically verify PIV credentials | [RULE-02] |
| Ensure FIPS 201 compliance | [RULE-01], [RULE-03] |
| Maintain PIV verification records | [RULE-04] |
| Investigate verification failures | [RULE-05] |