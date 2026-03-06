# POLICY: IA-8.5: Acceptance of PIV-I Credentials

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-8.5 |
| NIST Control | IA-8.5: Acceptance of PIV-I Credentials |
| Version | 1.0 |
| Owner | Identity and Access Management Director |
| Keywords | PIV-I, federated credentials, PKI, FBCA, authentication, verification |

## 1. POLICY STATEMENT
The organization SHALL accept and verify PIV-I credentials that meet defined federated or PKI credential policies for both logical and physical access control systems. All PIV-I credentials MUST be issued by providers cross-certified with the Federal Bridge Certification Authority (FBCA) and comply with approved certificate policies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Both logical and physical access systems |
| Federal employees | YES | PIV and PIV-I credential holders |
| Contractors with PIV-I | YES | Non-federal PIV-I credential holders |
| Guest users | NO | Unless specifically authorized PIV-I credentials |
| Service accounts | NO | Technical accounts not applicable |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IAM Director | • Define PIV-I acceptance policies<br>• Approve PIV-I provider cross-certifications<br>• Oversee compliance with FBCA requirements |
| System Administrators | • Configure systems to accept PIV-I credentials<br>• Implement verification mechanisms<br>• Maintain PIV-I verification records |
| Security Officers | • Validate PIV-I credential authenticity<br>• Monitor PIV-I authentication events<br>• Report PIV-I security incidents |

## 4. RULES
[RULE-01] Systems MUST accept PIV-I credentials from providers cross-certified with FBCA either directly or through approved PKI bridges.
[VALIDATION] IF piv_i_provider_fbca_certified = FALSE THEN violation

[RULE-02] All PIV-I credentials MUST be verified against current certificate revocation lists before granting access.
[VALIDATION] IF crl_check_performed = FALSE AND access_granted = TRUE THEN violation

[RULE-03] PIV-I credential verification records MUST be maintained for all authentication attempts for minimum 90 days.
[VALIDATION] IF verification_record_retention < 90_days THEN violation

[RULE-04] Systems MUST validate PIV-I certificate policy mappings to approved FBCA PIV-I Certificate Policy before acceptance.
[VALIDATION] IF certificate_policy_mapping_validated = FALSE AND piv_i_accepted = TRUE THEN violation

[RULE-05] PIV-I credentials SHALL NOT be accepted for systems processing classified information unless explicitly authorized by system security plan.
[VALIDATION] IF system_classification > "unclassified" AND piv_i_enabled = TRUE AND sse_authorization = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PIV-I Provider Certification Validation - Verify FBCA cross-certification status
- [PROC-02] PIV-I Credential Verification Process - Technical validation of credentials
- [PROC-03] PIV-I Authentication Logging - Record all verification attempts and outcomes
- [PROC-04] PIV-I Certificate Policy Mapping Review - Validate policy compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: FBCA policy changes, new PIV-I providers, security incidents involving PIV-I credentials

## 7. SCENARIO PATTERNS
[SCENARIO-01: Valid PIV-I Authentication]
IF piv_i_provider_fbca_certified = TRUE
AND certificate_policy_mapped = TRUE
AND crl_check_passed = TRUE
THEN compliance = TRUE

[SCENARIO-02: Uncertified PIV-I Provider]
IF piv_i_provider_fbca_certified = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing CRL Verification]
IF piv_i_credential_presented = TRUE
AND crl_check_performed = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: PIV-I on Classified System]
IF system_classification = "secret"
AND piv_i_authentication_enabled = TRUE
AND sse_authorization = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Incomplete Verification Records]
IF piv_i_authentication_occurred = TRUE
AND verification_record_created = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| PIV-I credentials meeting policy are accepted | [RULE-01], [RULE-04] |
| PIV-I credentials meeting policy are verified | [RULE-02], [RULE-03] |
| FBCA cross-certification validated | [RULE-01] |
| Certificate policy mapping confirmed | [RULE-04] |