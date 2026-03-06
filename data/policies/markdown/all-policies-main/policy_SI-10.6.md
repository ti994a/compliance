```markdown
# POLICY: SI-10.6: Injection Prevention

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-10.6 |
| NIST Control | SI-10.6: Injection Prevention |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | injection prevention, input validation, parameterized interfaces, output escaping, untrusted data, secure coding |

## 1. POLICY STATEMENT
All systems MUST implement technical controls to prevent untrusted data injections that could compromise system integrity or enable unauthorized access. Prevention mechanisms SHALL use parameterized interfaces, output escaping, or equivalent validated techniques for all data inputs from untrusted sources.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Web Applications | YES | All customer-facing and internal web apps |
| APIs | YES | REST, GraphQL, SOAP, and all programmatic interfaces |
| Database Systems | YES | All DBMS accepting external inputs |
| Mobile Applications | YES | iOS, Android, and hybrid applications |
| Legacy Systems | CONDITIONAL | Must comply within 180 days of policy effective date |
| Development Tools | YES | IDEs, CI/CD pipelines, code analysis tools |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Application Security Team | • Define secure coding standards<br>• Review injection prevention implementations<br>• Maintain approved parameterization libraries |
| Development Teams | • Implement parameterized interfaces for all data inputs<br>• Use approved output escaping methods<br>• Conduct code reviews for injection vulnerabilities |
| Security Operations | • Monitor for injection attack attempts<br>• Validate prevention controls during assessments<br>• Report injection prevention failures |

## 4. RULES
[RULE-01] All applications MUST use parameterized queries or prepared statements when interfacing with databases to prevent SQL injection attacks.
[VALIDATION] IF application_uses_dynamic_sql = TRUE AND parameterized_queries = FALSE THEN critical_violation

[RULE-02] Web applications MUST implement output escaping for all user-controlled data displayed in HTML contexts to prevent cross-site scripting (XSS).
[VALIDATION] IF user_data_in_output = TRUE AND output_escaping = FALSE THEN violation

[RULE-03] API endpoints MUST validate and sanitize all input parameters using approved validation libraries before processing requests.
[VALIDATION] IF api_endpoint = TRUE AND input_validation = FALSE THEN violation

[RULE-04] Applications SHALL NOT construct system commands using string concatenation with untrusted input data.
[VALIDATION] IF command_construction_method = "concatenation" AND input_source = "untrusted" THEN critical_violation

[RULE-05] All injection prevention mechanisms MUST be tested during security assessments and penetration testing activities conducted at least annually.
[VALIDATION] IF last_injection_test_date > 365_days THEN violation

[RULE-06] Development frameworks and libraries used for injection prevention MUST be maintained with security patches applied within 30 days of release.
[VALIDATION] IF security_patch_age > 30_days AND component_handles_injection_prevention = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Secure Coding Standards - Mandatory parameterization and escaping requirements
- [PROC-02] Code Review Process - Security-focused review including injection prevention validation  
- [PROC-03] Security Testing Protocol - Automated and manual injection testing procedures
- [PROC-04] Incident Response - Process for handling successful injection attacks

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving injection attacks, new application deployments, framework updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: SQL Injection Prevention]
IF application_type = "web_application"
AND database_queries = "dynamic"
AND parameterized_queries = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: API Input Validation]
IF system_type = "API"
AND accepts_external_input = TRUE
AND input_validation_implemented = TRUE
AND validation_library = "approved"
THEN compliance = TRUE

[SCENARIO-03: Legacy System Exception]
IF system_age > 5_years
AND injection_prevention = FALSE
AND remediation_plan_approved = TRUE
AND remediation_deadline < 180_days
THEN compliance = TRUE (temporary)

[SCENARIO-04: XSS Prevention Failure]
IF user_input_displayed = TRUE
AND output_context = "HTML"
AND output_escaping = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Command Injection Risk]
IF system_command_execution = TRUE
AND input_source = "user_controlled"
AND parameterized_interface = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Untrusted data injections are prevented | RULE-01, RULE-02, RULE-03, RULE-04 |
| Prevention mechanisms are properly implemented | RULE-01, RULE-02, RULE-03 |
| Controls are regularly tested and validated | RULE-05 |
| Prevention tools are maintained securely | RULE-06 |
```