# POLICY: SI-10.6: Injection Prevention

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-10.6 |
| NIST Control | SI-10.6: Injection Prevention |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | injection prevention, untrusted data, parameterized interfaces, output escaping, input validation |

## 1. POLICY STATEMENT
All systems SHALL prevent untrusted data injections through the implementation of parameterized interfaces, output escaping, or equivalent secure coding practices. Untrusted data inputs MUST be processed using techniques that separate data from executable code to prevent malicious code execution.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Web Applications | YES | All customer-facing and internal web applications |
| APIs | YES | REST, SOAP, GraphQL, and other API interfaces |
| Database Systems | YES | All systems accepting dynamic queries |
| Mobile Applications | YES | iOS, Android, and hybrid applications |
| Legacy Systems | CONDITIONAL | Must comply within 180 days or require exception |
| Third-party Integrations | YES | Must validate injection prevention controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Application Security Team | • Define secure coding standards<br>• Review injection prevention implementations<br>• Conduct security testing and validation |
| Development Teams | • Implement parameterized interfaces<br>• Apply output escaping techniques<br>• Follow secure coding practices |
| Security Operations | • Monitor for injection attack attempts<br>• Investigate security incidents<br>• Maintain detection signatures |

## 4. RULES
[RULE-01] All database queries MUST use parameterized statements or prepared statements when incorporating user-supplied data.
[VALIDATION] IF query_type = "dynamic" AND parameterized = FALSE AND user_input = TRUE THEN critical_violation

[RULE-02] Output data displayed to users MUST be escaped or encoded based on the output context (HTML, JavaScript, CSS, URL).
[VALIDATION] IF output_context IN ["html", "javascript", "css", "url"] AND encoding_applied = FALSE THEN violation

[RULE-03] Input validation MUST be performed on all untrusted data sources before processing, using allowlist validation where possible.
[VALIDATION] IF data_source = "untrusted" AND validation_performed = FALSE THEN violation

[RULE-04] Command injection prevention MUST be implemented when executing system commands with user-supplied parameters.
[VALIDATION] IF system_command = TRUE AND user_input = TRUE AND injection_prevention = FALSE THEN critical_violation

[RULE-05] All injection prevention implementations MUST be tested during development and validated through security testing.
[VALIDATION] IF injection_testing_completed = FALSE AND deployment_approved = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Secure Code Review Process - Mandatory review of injection prevention controls before production deployment
- [PROC-02] Security Testing Protocol - Automated and manual testing for injection vulnerabilities
- [PROC-03] Incident Response for Injection Attacks - Response procedures for detected injection attempts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving injection attacks, new application deployments, technology stack changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Database Query with User Input]
IF application_type = "web_application"
AND database_query = "dynamic"
AND user_input_included = TRUE
AND parameterized_query = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: API Output Encoding]
IF system_type = "api"
AND output_format = "json"
AND user_data_returned = TRUE
AND output_encoding = TRUE
THEN compliance = TRUE

[SCENARIO-03: Legacy System Exception]
IF system_age > 5_years
AND injection_prevention = FALSE
AND documented_exception = TRUE
AND compensating_controls = TRUE
AND remediation_plan_approved = TRUE
THEN compliance = TRUE

[SCENARIO-04: Third-party Integration]
IF integration_type = "third_party"
AND data_flow = "bidirectional"
AND vendor_injection_controls = "unknown"
AND security_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Command Execution]
IF functionality = "system_command"
AND user_input = TRUE
AND command_injection_prevention = TRUE
AND security_testing = "passed"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Untrusted data injections are prevented | RULE-01, RULE-02, RULE-03, RULE-04 |
| Parameterized interfaces implemented | RULE-01 |
| Output escaping applied | RULE-02 |
| Input validation performed | RULE-03 |
| Security testing conducted | RULE-05 |