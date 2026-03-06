# POLICY: SI-7.12: Integrity Verification

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.12 |
| NIST Control | SI-7.12: Integrity Verification |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | integrity verification, user-installed software, checksums, malicious code, software validation |

## 1. POLICY STATEMENT
All user-installed software designated as requiring integrity verification must have its integrity validated using approved methods prior to execution. Organizations must define categories of user-installed software requiring verification and implement technical controls to enforce verification before execution.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Covers all user-installed software |
| Contractors | YES | Same requirements as employees |
| Third-party users | YES | When installing software on company systems |
| Personal devices (BYOD) | CONDITIONAL | Only when accessing company resources |
| Development environments | YES | Enhanced verification requirements |
| Production systems | YES | Mandatory verification for all software |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define software categories requiring verification<br>• Approve integrity verification tools<br>• Oversee policy compliance |
| IT Security Team | • Implement technical verification controls<br>• Maintain approved software catalogs<br>• Monitor verification compliance |
| System Administrators | • Configure verification mechanisms<br>• Maintain checksums and signatures<br>• Block unverified software execution |
| End Users | • Use only approved verification methods<br>• Report verification failures<br>• Comply with software installation procedures |

## 4. RULES

[RULE-01] Organizations MUST define categories of user-installed software that require integrity verification prior to execution.
[VALIDATION] IF software_category_defined = FALSE THEN violation

[RULE-02] All software in defined categories MUST undergo integrity verification using approved methods before execution is permitted.
[VALIDATION] IF software_category = "requires_verification" AND integrity_verified = FALSE AND execution_attempted = TRUE THEN critical_violation

[RULE-03] Integrity verification MUST use cryptographic checksums, digital signatures, or other approved verification methods from trusted sources.
[VALIDATION] IF verification_method NOT IN approved_methods THEN violation

[RULE-04] Systems MUST be configured to automatically block execution of unverified software in categories requiring verification.
[VALIDATION] IF auto_block_enabled = FALSE AND system_type = "production" THEN violation

[RULE-05] Verification failures MUST be logged and reported to the security team within 15 minutes of occurrence.
[VALIDATION] IF verification_failed = TRUE AND (logged = FALSE OR report_time > 15_minutes) THEN violation

[RULE-06] Software from untrusted or unauthorized sources MUST NOT be installed without explicit security team approval and enhanced verification procedures.
[VALIDATION] IF source_trusted = FALSE AND security_approval = FALSE AND installed = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Software Category Definition - Process for defining and updating software categories requiring verification
- [PROC-02] Integrity Verification Implementation - Technical procedures for configuring verification mechanisms
- [PROC-03] Verification Failure Response - Incident response procedures for verification failures
- [PROC-04] Approved Source Management - Maintaining and updating trusted software source lists

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New software categories, verification tool changes, security incidents involving unverified software

## 7. SCENARIO PATTERNS

[SCENARIO-01: Production Software Installation]
IF system_environment = "production"
AND software_category = "requires_verification"
AND integrity_verified = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Development Tool Installation]
IF user_role = "developer"
AND software_type = "development_tool"
AND source_authorized = TRUE
AND checksum_verified = TRUE
THEN compliance = TRUE

[SCENARIO-03: Untrusted Source Installation]
IF software_source = "untrusted"
AND security_approval = FALSE
AND installation_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Verification Failure Logging]
IF integrity_verification = "failed"
AND incident_logged = TRUE
AND security_notified_within_15min = TRUE
THEN compliance = TRUE

[SCENARIO-05: BYOD Software Installation]
IF device_type = "personal"
AND company_resource_access = TRUE
AND software_category = "requires_verification"
AND integrity_verified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Define user-installed software requiring integrity verification | [RULE-01] |
| Verify integrity prior to execution | [RULE-02] |
| Use approved verification methods | [RULE-03] |
| Implement technical enforcement controls | [RULE-04] |
| Log and report verification events | [RULE-05] |
| Control unauthorized software sources | [RULE-06] |