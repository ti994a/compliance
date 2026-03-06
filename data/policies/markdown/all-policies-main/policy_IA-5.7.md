# POLICY: IA-5.7: No Embedded Unencrypted Static Authenticators

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5.7 |
| NIST Control | IA-5.7: No Embedded Unencrypted Static Authenticators |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authenticators, embedded, unencrypted, static, applications, storage, credentials, hardcoded |

## 1. POLICY STATEMENT
All applications, scripts, and static storage systems SHALL NOT contain unencrypted static authenticators including passwords, API keys, certificates, or other credentials. Any authenticators stored or embedded in code MUST be encrypted or externally managed through secure credential management systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Applications (internal/external) | YES | All custom and commercial applications |
| Source code repositories | YES | All development repositories and branches |
| Configuration files | YES | System and application configuration files |
| Scripts and automation | YES | Access scripts, deployment scripts, function keys |
| Databases and data stores | YES | All forms of persistent storage |
| Third-party integrations | YES | APIs, webhooks, external service connections |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Implement secure credential management practices<br>• Conduct code reviews for embedded authenticators<br>• Use approved credential management tools |
| Security Team | • Define approved credential management solutions<br>• Perform security assessments and code reviews<br>• Monitor for policy violations |
| DevOps/Platform Teams | • Implement and maintain credential management infrastructure<br>• Provide secure deployment pipelines<br>• Configure automated scanning tools |

## 4. RULES
[RULE-01] Applications and scripts MUST NOT contain hardcoded unencrypted authenticators including passwords, API keys, tokens, or certificates.
[VALIDATION] IF authenticator_found = TRUE AND encryption_status = "unencrypted" AND storage_location = "embedded" THEN critical_violation

[RULE-02] All static authenticators MUST be stored using approved credential management systems with encryption at rest and in transit.
[VALIDATION] IF authenticator_storage = "credential_manager" AND encryption_at_rest = TRUE AND encryption_in_transit = TRUE THEN compliant

[RULE-03] Source code repositories MUST be scanned for embedded authenticators before each release and at least weekly for active development branches.
[VALIDATION] IF scan_frequency < 7_days AND pre_release_scan = TRUE THEN compliant

[RULE-04] Configuration files containing authenticators MUST use encrypted storage or reference external credential management systems.
[VALIDATION] IF config_contains_auth = TRUE AND (encrypted = TRUE OR external_reference = TRUE) THEN compliant

[RULE-05] Access scripts and function keys MUST NOT store authenticators in plaintext and MUST use runtime credential retrieval.
[VALIDATION] IF script_type = "access" AND plaintext_auth = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Secure Credential Management - Implementation and configuration of approved credential management solutions
- [PROC-02] Code Review Process - Mandatory security review process including authenticator detection
- [PROC-03] Automated Scanning - Configuration and monitoring of automated credential scanning tools
- [PROC-04] Incident Response - Response procedures for discovered embedded authenticators
- [PROC-05] Developer Training - Regular training on secure coding practices and credential management

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving credential exposure, new development frameworks, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Hardcoded Database Password]
IF application_code_contains = "database_password"
AND password_encryption = FALSE
AND storage_type = "source_code"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: API Key in Configuration File]
IF config_file_contains = "api_key"
AND key_format = "plaintext"
AND external_reference = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Encrypted Certificate in Keystore]
IF certificate_storage = "keystore"
AND encryption_status = "encrypted"
AND access_control = "restricted"
THEN compliance = TRUE

[SCENARIO-04: Environment Variable Credential]
IF credential_source = "environment_variable"
AND runtime_retrieval = TRUE
AND plaintext_storage = FALSE
THEN compliance = TRUE

[SCENARIO-05: Legacy Script with Embedded Token]
IF script_age > 2_years
AND embedded_token = TRUE
AND token_encryption = FALSE
AND remediation_plan = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Unencrypted static authenticators are not embedded in applications | [RULE-01], [RULE-02] |
| Unencrypted static authenticators are not embedded in other forms of static storage | [RULE-04], [RULE-05] |
| Authenticator management controls are implemented | [RULE-02], [RULE-03] |
| Security assessments detect embedded authenticators | [RULE-03] |