# POLICY: IA-5.6: Protection of Authenticators

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5.6 |
| NIST Control | IA-5.6: Protection of Authenticators |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authenticators, protection, security category, access control, passwords, tokens, certificates |

## 1. POLICY STATEMENT
All authenticators (passwords, tokens, certificates, biometric data) MUST be protected with security controls that match or exceed the security category of the information systems and data they provide access to. For systems containing multiple security categories without reliable separation, authenticator protection MUST match the highest security category present.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All authenticators | YES | Passwords, tokens, certificates, biometric data |
| Information systems | YES | All company-owned and managed systems |
| Third-party systems | YES | When containing company data |
| Personal devices | CONDITIONAL | Only when accessing company resources |
| Guest/visitor access | YES | Temporary authenticators included |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Determine security categorization of their systems<br>• Implement appropriate authenticator protections<br>• Maintain documentation of protection measures |
| Security Team | • Define protection requirements by security category<br>• Audit authenticator protection implementations<br>• Approve exceptions and compensating controls |
| IT Operations | • Implement technical authenticator protections<br>• Monitor authenticator security events<br>• Maintain authenticator management systems |

## 4. RULES
[RULE-01] Authenticator protection levels MUST match the security category (Low, Moderate, High) of the information system or data being accessed.
[VALIDATION] IF system_security_category = "High" AND authenticator_protection_level < "High" THEN critical_violation

[RULE-02] For systems containing multiple security categories without reliable separation, authenticator protection MUST be implemented at the highest security category level present.
[VALIDATION] IF mixed_security_categories = TRUE AND reliable_separation = FALSE AND authenticator_protection < max_security_category THEN violation

[RULE-03] High-category authenticators MUST use multi-factor authentication with hardware-based tokens or certificates.
[VALIDATION] IF security_category = "High" AND (mfa_enabled = FALSE OR hardware_token = FALSE) THEN critical_violation

[RULE-04] Moderate-category authenticators MUST use multi-factor authentication with approved software or hardware tokens.
[VALIDATION] IF security_category = "Moderate" AND mfa_enabled = FALSE THEN violation

[RULE-05] Authenticator storage MUST use encryption that meets or exceeds the security category requirements.
[VALIDATION] IF authenticator_stored = TRUE AND encryption_level < required_encryption_level THEN violation

[RULE-06] Authenticator transmission MUST occur over encrypted channels appropriate to the security category.
[VALIDATION] IF authenticator_transmitted = TRUE AND channel_encryption < required_encryption THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Categorization Assessment - Determine security category for all systems and data
- [PROC-02] Authenticator Protection Mapping - Map protection requirements to security categories
- [PROC-03] Authenticator Security Monitoring - Monitor and log authenticator security events
- [PROC-04] Protection Control Validation - Regular testing of authenticator protection measures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployment, security category changes, security incidents involving authenticators

## 7. SCENARIO PATTERNS
[SCENARIO-01: High Security System Access]
IF system_security_category = "High"
AND authenticator_type = "password_only"
AND mfa_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Mixed Category System]
IF system_contains_categories = ["Low", "Moderate", "High"]
AND reliable_separation = FALSE
AND authenticator_protection_level = "Moderate"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Appropriate Protection Level]
IF system_security_category = "Moderate"
AND mfa_enabled = TRUE
AND token_type = "software_approved"
AND encryption_level >= "AES-256"
THEN compliance = TRUE

[SCENARIO-04: Contractor Access to High System]
IF user_type = "contractor"
AND system_security_category = "High"
AND authenticator_protection < "High"
AND compensating_controls = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Legacy System Exception]
IF system_type = "legacy"
AND security_category = "High"
AND authenticator_protection = "Moderate"
AND documented_exception = TRUE
AND compensating_controls = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authenticators protected commensurate with security category | RULE-01, RULE-02 |
| Multi-category system protection | RULE-02 |
| High-category protection requirements | RULE-03 |
| Moderate-category protection requirements | RULE-04 |
| Secure authenticator storage | RULE-05 |
| Secure authenticator transmission | RULE-06 |