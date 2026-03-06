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
All user-installed software requiring integrity verification must be validated using approved verification methods prior to execution. Organizations must define categories of user-installed software requiring integrity verification and implement automated verification processes where feasible.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Applies to all user-installed software |
| Contractors | YES | Same requirements as employees |
| System administrators | YES | Enhanced verification requirements |
| Production systems | YES | Critical integrity verification required |
| Development systems | CONDITIONAL | Based on data classification |
| Personal devices (BYOD) | YES | If accessing corporate resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define software categories requiring verification<br>• Approve integrity verification tools<br>• Oversee policy compliance |
| System Administrators | • Implement verification mechanisms<br>• Monitor verification processes<br>• Maintain verification records |
| End Users | • Request approval for software installation<br>• Use only approved software sources<br>• Report verification failures |
| Security Team | • Validate verification tools<br>• Investigate integrity violations<br>• Maintain approved software catalog |

## 4. RULES
[RULE-01] All software in critical categories (security tools, system utilities, network applications) MUST undergo integrity verification prior to execution.
[VALIDATION] IF software_category IN ["security", "system", "network"] AND integrity_verified = FALSE THEN critical_violation

[RULE-02] Integrity verification MUST use cryptographic checksums (SHA-256 or stronger) from authorized software vendors or internal repositories.
[VALIDATION] IF verification_method NOT IN ["SHA-256", "SHA-384", "SHA-512"] THEN violation

[RULE-03] User-installed software from unauthorized sources MUST NOT be executed without explicit security team approval and enhanced verification.
[VALIDATION] IF software_source = "unauthorized" AND security_approval = FALSE THEN critical_violation

[RULE-04] Automated integrity verification tools MUST be deployed on all systems where user software installation is permitted.
[VALIDATION] IF user_install_permitted = TRUE AND verification_tool_installed = FALSE THEN violation

[RULE-05] Integrity verification failures MUST be logged and reported to the security team within 15 minutes of detection.
[VALIDATION] IF verification_status = "failed" AND report_time > 15_minutes THEN violation

[RULE-06] Software requiring integrity verification MUST be obtained from approved vendor repositories or internal software catalogs.
[VALIDATION] IF software_source NOT IN approved_sources AND verification_required = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Software Category Classification - Define and maintain categories of software requiring verification
- [PROC-02] Integrity Verification Process - Step-by-step verification procedures for different software types
- [PROC-03] Verification Failure Response - Incident response procedures for integrity verification failures
- [PROC-04] Approved Source Management - Maintain and update approved software source repositories

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving malicious software, new software categories, vendor security advisories

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Software Installation]
IF software_category = "security_tool"
AND integrity_verified = FALSE
AND execution_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Unauthorized Source Usage]
IF software_source NOT IN approved_vendor_list
AND verification_required = TRUE
AND security_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Verification Tool Bypass]
IF verification_tool_status = "disabled"
AND user_install_permitted = TRUE
AND system_type = "production"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Failed Verification Response]
IF verification_result = "checksum_mismatch"
AND incident_reported = FALSE
AND time_elapsed > 15_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Development System Exception]
IF system_type = "development"
AND data_classification = "public"
AND verification_required = FALSE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| User-installed software requiring verification is defined | [RULE-01], [RULE-06] |
| Integrity verification performed prior to execution | [RULE-01], [RULE-02] |
| Verification methods are cryptographically secure | [RULE-02] |
| Unauthorized sources are controlled | [RULE-03], [RULE-06] |
| Verification failures are detected and reported | [RULE-05] |
| Verification tools are properly deployed | [RULE-04] |