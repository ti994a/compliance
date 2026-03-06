# POLICY: IA-5.1: Password-based Authentication

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5.1 |
| NIST Control | IA-5.1: Password-based Authentication |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | password, authentication, compromised, transmission, storage, recovery, complexity |

## 1. POLICY STATEMENT
The organization shall implement secure password-based authentication controls including maintenance of compromised password lists, secure transmission and storage, and support for strong password selection. All password operations must follow cryptographic protection requirements and enforce security validation against known compromised credentials.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premise, and hybrid |
| Employee accounts | YES | All authentication methods using passwords |
| Contractor/vendor accounts | YES | When accessing organizational systems |
| Service accounts | YES | When using password authentication |
| Guest/temporary accounts | YES | All password-based access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Policy oversight and compliance monitoring<br>• Approve password security standards<br>• Review compromised password incidents |
| IT Security Team | • Maintain compromised password lists<br>• Implement automated validation tools<br>• Monitor password transmission security |
| System Administrators | • Configure password storage mechanisms<br>• Enforce composition rules<br>• Implement account recovery procedures |
| Users | • Create compliant passwords<br>• Report suspected compromise<br>• Follow recovery procedures |

## 4. RULES
[RULE-01] The organization MUST maintain a list of commonly-used, expected, or compromised passwords and update it at least quarterly and immediately when organizational passwords are suspected to be compromised.
[VALIDATION] IF compromised_list_age > 90_days OR suspected_compromise = TRUE AND list_updated = FALSE THEN violation

[RULE-02] Password creation and updates MUST be verified against the compromised password list before acceptance.
[VALIDATION] IF password IN compromised_list AND password_accepted = TRUE THEN critical_violation

[RULE-03] Passwords MUST be transmitted only over cryptographically-protected channels using approved encryption protocols.
[VALIDATION] IF password_transmission = TRUE AND encryption_enabled = FALSE THEN critical_violation

[RULE-04] Passwords MUST be stored using approved salted key derivation functions, preferably using keyed hash algorithms.
[VALIDATION] IF password_storage_method NOT IN approved_kdf_list THEN critical_violation

[RULE-05] Users MUST immediately select a new password upon account recovery processes.
[VALIDATION] IF account_recovery = TRUE AND new_password_required = FALSE THEN violation

[RULE-06] Systems MUST allow user selection of long passwords and passphrases including spaces and all printable characters with minimum length of 12 characters.
[VALIDATION] IF password_min_length < 12 OR printable_chars_blocked = TRUE THEN violation

[RULE-07] Automated tools MUST be employed to assist users in selecting strong password authenticators.
[VALIDATION] IF password_strength_tool_available = FALSE THEN violation

[RULE-08] Password composition and complexity rules MUST be defined and enforced according to organizational standards.
[VALIDATION] IF composition_rules_defined = FALSE OR enforcement_enabled = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Compromised Password List Management - Quarterly updates and incident-driven maintenance
- [PROC-02] Password Validation Process - Real-time checking against compromised lists
- [PROC-03] Secure Password Transmission - Encryption requirements and monitoring
- [PROC-04] Password Storage Security - Implementation of approved cryptographic functions
- [PROC-05] Account Recovery Process - Mandatory password reset procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, password breaches, regulatory changes, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Password Creation Validation]
IF user_creating_password = TRUE
AND password IN compromised_password_list
AND system_blocks_password = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Unencrypted Password Transmission]
IF password_transmission = TRUE
AND channel_encryption = FALSE
AND transmission_method = "plaintext"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Account Recovery Without Password Reset]
IF account_recovery_initiated = TRUE
AND user_access_restored = TRUE
AND new_password_required = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Outdated Compromised Password List]
IF compromised_list_last_update > 90_days
AND no_suspected_compromise = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Weak Password Storage]
IF password_storage_method = "plaintext"
OR password_storage_method = "unsalted_hash"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Maintain compromised password list | [RULE-01] |
| Verify passwords against compromised list | [RULE-02] |
| Transmit passwords over protected channels | [RULE-03] |
| Store passwords using approved functions | [RULE-04] |
| Require new password on recovery | [RULE-05] |
| Allow long passwords and passphrases | [RULE-06] |
| Employ automated password tools | [RULE-07] |
| Enforce composition rules | [RULE-08] |