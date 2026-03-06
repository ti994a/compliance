# POLICY: SC-23.3: Unique System-generated Session Identifiers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-23.3 |
| NIST Control | SC-23.3: Unique System-generated Session Identifiers |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | session management, randomness, authentication, session identifiers, cryptographic security |

## 1. POLICY STATEMENT
All systems SHALL generate cryptographically unique session identifiers for each user session using approved randomness requirements. Only system-generated session identifiers SHALL be recognized and accepted by applications and systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Web Applications | YES | All customer-facing and internal web apps |
| API Services | YES | REST, GraphQL, and SOAP APIs |
| Mobile Applications | YES | Native and hybrid mobile apps |
| Legacy Systems | CONDITIONAL | Must comply within 180 days or obtain exception |
| Third-party Integrations | YES | When session management is under our control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Implement approved session ID generation libraries<br>• Configure randomness parameters per standards<br>• Validate session ID uniqueness in code reviews |
| Security Architecture | • Define approved cryptographic libraries<br>• Set minimum entropy requirements<br>• Review session management implementations |
| Platform Engineering | • Deploy secure session management infrastructure<br>• Monitor session ID collision rates<br>• Maintain approved randomness sources |

## 4. RULES
[RULE-01] All session identifiers MUST be generated using cryptographically secure pseudo-random number generators (CSPRNG) with minimum 128-bit entropy.
[VALIDATION] IF session_id_entropy < 128_bits OR rng_type != "CSPRNG" THEN violation

[RULE-02] Session identifiers MUST be unique across all active sessions and MUST NOT be predictable or sequential.
[VALIDATION] IF session_id_collision = TRUE OR session_id_pattern = "sequential" THEN critical_violation

[RULE-03] Systems MUST reject any user-provided or externally generated session identifiers and SHALL only accept system-generated identifiers.
[VALIDATION] IF session_id_source != "system_generated" THEN violation

[RULE-04] Session identifier generation MUST use approved libraries from the corporate security standards list and MUST NOT implement custom randomness algorithms.
[VALIDATION] IF crypto_library NOT IN approved_libraries_list OR custom_random_algorithm = TRUE THEN violation

[RULE-05] Session identifiers MUST be regenerated upon authentication, privilege escalation, and at least every 8 hours for long-running sessions.
[VALIDATION] IF session_regeneration_trigger = FALSE OR session_age > 8_hours AND regenerated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Session ID Security Review - Mandatory security review for all session management implementations
- [PROC-02] Randomness Testing - Quarterly statistical testing of session ID randomness quality
- [PROC-03] Session Collision Monitoring - Real-time monitoring for session ID collisions and anomalies
- [PROC-04] Library Approval Process - Formal approval process for cryptographic libraries used in session management

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving session management, new cryptographic standards, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Custom Session ID Implementation]
IF application_uses_custom_session_generation = TRUE
AND approved_library_usage = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Weak Randomness Source]
IF session_id_entropy < 128_bits
AND randomness_source != "CSPRNG"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: User-Provided Session ID]
IF session_id_source = "user_provided"
AND system_accepts_external_session_id = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Session ID Collision Detected]
IF session_collision_rate > 0
AND collision_monitoring = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Legacy System Exception]
IF system_type = "legacy"
AND exception_approved = TRUE
AND remediation_plan_exists = TRUE
AND remediation_deadline <= 180_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Generate unique session identifier for each session with defined randomness requirements | [RULE-01], [RULE-02] |
| Recognize only system-generated session identifiers | [RULE-03] |
| Use approved cryptographic mechanisms | [RULE-04] |
| Implement proper session lifecycle management | [RULE-05] |