```markdown
# POLICY: SA-11.4: Manual Code Reviews

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.4 |
| NIST Control | SA-11.4: Manual Code Reviews |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | manual code review, developer requirements, critical software, security testing, code analysis |

## 1. POLICY STATEMENT
The organization SHALL require developers of systems, system components, or system services to perform manual code reviews on critical software and firmware components using defined processes and techniques. Manual code reviews MUST complement automated analysis tools to identify security weaknesses requiring contextual knowledge and domain expertise.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All critical system components |
| Third-Party Developers | YES | Contractual requirement for critical components |
| COTS Software | NO | Limited to custom/modified components |
| Open Source Components | CONDITIONAL | Only if modified or critical integration points |
| Legacy Systems | YES | During major updates or security reviews |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define critical code categories requiring manual review<br>• Approve manual code review processes and techniques<br>• Oversee compliance monitoring |
| Development Manager | • Ensure manual code reviews are performed per policy<br>• Maintain qualified code reviewers<br>• Document review results and remediation |
| Security Architect | • Define security-focused review criteria<br>• Validate review processes and techniques<br>• Review critical findings and recommendations |

## 4. RULES
[RULE-01] Developers MUST perform manual code reviews on all code components classified as critical for security, safety, or regulatory compliance.
[VALIDATION] IF code_classification = "critical" AND manual_review_completed = FALSE THEN violation

[RULE-02] Manual code review processes MUST include examination of access control matrices, cryptographic implementations, and security control logic.
[VALIDATION] IF manual_review_scope NOT includes ["access_controls", "cryptography", "security_logic"] THEN violation

[RULE-03] Manual code reviews SHALL be performed by qualified reviewers with security expertise and knowledge of the application's security requirements.
[VALIDATION] IF reviewer_security_qualified = FALSE OR reviewer_domain_knowledge = FALSE THEN violation

[RULE-04] Manual code review results MUST be documented with identified weaknesses, risk ratings, and remediation recommendations.
[VALIDATION] IF review_documentation NOT includes ["weaknesses", "risk_ratings", "remediation"] THEN violation

[RULE-05] Critical security findings from manual code reviews MUST be remediated before system deployment or release.
[VALIDATION] IF critical_findings_count > 0 AND deployment_approved = TRUE THEN critical_violation

[RULE-06] Manual code review processes and techniques MUST be formally defined and documented in development procedures.
[VALIDATION] IF manual_review_process_documented = FALSE OR techniques_defined = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Code Classification - Process for identifying code requiring manual review
- [PROC-02] Manual Review Execution - Step-by-step procedures for conducting reviews
- [PROC-03] Reviewer Qualification - Requirements and training for code reviewers
- [PROC-04] Finding Management - Process for tracking and remediating identified issues

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents related to code vulnerabilities, new critical system deployments, regulatory requirement changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Component Without Manual Review]
IF code_classification = "critical"
AND manual_review_completed = FALSE
AND deployment_requested = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unqualified Reviewer]
IF manual_review_completed = TRUE
AND reviewer_security_certified = FALSE
AND code_classification = "critical"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incomplete Review Documentation]
IF manual_review_completed = TRUE
AND (findings_documented = FALSE OR risk_assessment_missing = TRUE)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unresolved Critical Findings]
IF manual_review_findings_severity = "critical"
AND findings_status = "open"
AND system_deployed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Compliant Manual Review Process]
IF code_classification = "critical"
AND manual_review_completed = TRUE
AND reviewer_qualified = TRUE
AND findings_documented = TRUE
AND critical_findings_resolved = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer performs manual code review of specific code | [RULE-01] |
| Uses defined processes, procedures, and techniques | [RULE-06] |
| Reviews critical software and firmware components | [RULE-01], [RULE-02] |
| Qualified reviewers conduct reviews | [RULE-03] |
| Results documented and acted upon | [RULE-04], [RULE-05] |
```