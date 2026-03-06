# POLICY: SC-23.3: Unique System-generated Session Identifiers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-23.3 |
| NIST Control | SC-23.3: Unique System-generated Session Identifiers |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | session identifiers, randomness, system-generated, session management, authentication |

## 1. POLICY STATEMENT
All systems SHALL generate cryptographically unique session identifiers for each user session using approved randomness requirements. Systems MUST NOT accept or recognize session identifiers that are not system-generated or that originate from external sources.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Web Applications | YES | All customer-facing and internal web apps |
| API Services | YES | REST, GraphQL, and SOAP APIs |
| Mobile Applications | YES | Native and hybrid mobile apps |
| Desktop Applications | CONDITIONAL | Only those with session-based authentication |
| Legacy Systems | YES | Must comply or document compensating controls |
| Third-party SaaS | CONDITIONAL | Where session management is configurable |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Application Security Team | • Define approved randomness algorithms<br>• Review session identifier implementations<br>• Conduct security assessments |
| Development Teams | • Implement compliant session generation<br>• Use approved cryptographic libraries<br>• Document session management architecture |
| Infrastructure Team | • Configure session management middleware<br>• Monitor session identifier entropy<br>• Maintain cryptographic modules |

## 4. RULES
[RULE-01] All session identifiers MUST be generated using cryptographically secure pseudo-random number generators (CSPRNG) with minimum 128-bit entropy.
[VALIDATION] IF session_entropy < 128_bits OR generator_type != "CSPRNG" THEN critical_violation

[RULE-02] Systems SHALL NOT accept session identifiers provided by clients, URL parameters, or any external source.
[VALIDATION] IF session_source = "client_provided" OR session_source = "url_parameter" THEN critical_violation

[RULE-03] Session identifiers MUST be unique across all active sessions and MUST NOT be predictable or sequential.
[VALIDATION] IF session_collision_detected = TRUE OR session_pattern = "sequential" THEN critical_violation

[RULE-04] Session identifier generation algorithms MUST use FIPS 140-2 Level 1 or higher validated cryptographic modules.
[VALIDATION] IF crypto_module_fips_level < 1 THEN violation

[RULE-05] Session identifiers MUST have sufficient length with minimum 128 bits of randomness and SHOULD use 256 bits for high-security applications.
[VALIDATION] IF application_risk = "high" AND session_bits < 256 THEN violation

[RULE-06] Systems MUST regenerate session identifiers upon successful authentication and privilege escalation.
[VALIDATION] IF authentication_event = TRUE AND session_regenerated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Session Identifier Security Assessment - Annual review of session generation mechanisms
- [PROC-02] Cryptographic Module Validation - Verification of FIPS compliance for random number generators
- [PROC-03] Session Management Code Review - Security review of session handling implementation
- [PROC-04] Entropy Monitoring - Continuous monitoring of session identifier randomness quality

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Security incidents involving session compromise, new application deployments, cryptographic standard updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Web Application Session Generation]
IF application_type = "web_application"
AND session_generator = "system_generated"
AND entropy_bits >= 128
AND fips_validated = TRUE
THEN compliance = TRUE

[SCENARIO-02: Client-Provided Session ID]
IF session_source = "client_cookie"
AND session_validation = "accepted"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Insufficient Entropy]
IF session_entropy < 128
AND application_environment = "production"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Legacy System Exception]
IF system_type = "legacy"
AND compensating_controls = "documented"
AND risk_assessment = "completed"
AND approval_status = "approved"
THEN compliance = TRUE

[SCENARIO-05: API Session Token]
IF service_type = "API"
AND token_generation = "JWT_with_secure_random"
AND signing_algorithm = "RS256"
AND entropy_bits >= 256
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Generate unique session identifier for each session | RULE-01, RULE-03 |
| Randomness requirements are defined | RULE-01, RULE-04, RULE-05 |
| Only system-generated session identifiers are recognized | RULE-02, RULE-06 |