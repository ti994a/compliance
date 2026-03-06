# POLICY: SA-11.4: Manual Code Reviews

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.4 |
| NIST Control | SA-11.4: Manual Code Reviews |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | manual code review, developer requirements, critical software, firmware, static analysis, dynamic analysis |

## 1. POLICY STATEMENT
The organization MUST require developers of systems, system components, or system services to perform manual code reviews of critical software and firmware components using defined processes, procedures, and techniques. Manual code reviews SHALL supplement automated analysis tools to identify security weaknesses that require contextual knowledge and application-specific understanding.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Custom-developed software | YES | All internally developed applications |
| Third-party developed software | YES | When contractually feasible |
| Commercial off-the-shelf (COTS) | CONDITIONAL | Only when source code access available |
| Firmware components | YES | All custom and modified firmware |
| System integrators | YES | Must comply with manual review requirements |
| Cloud service providers | CONDITIONAL | When providing custom development services |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define manual code review requirements<br>• Approve review processes and techniques<br>• Oversee compliance monitoring |
| Development Manager | • Ensure developer compliance with manual review requirements<br>• Validate review completion before deployment<br>• Maintain review documentation |
| Security Architect | • Define critical code requiring manual review<br>• Establish review procedures and techniques<br>• Review and approve manual review results |
| Procurement Officer | • Include manual code review requirements in contracts<br>• Verify vendor compliance capabilities<br>• Monitor contractor adherence to review requirements |

## 4. RULES
[RULE-01] Developers MUST perform manual code reviews on all critical software and firmware components as defined by the Security Architecture team.
[VALIDATION] IF component_criticality = "critical" AND manual_review_completed = FALSE THEN violation

[RULE-02] Manual code review processes and techniques MUST be formally defined and documented before implementation begins.
[VALIDATION] IF development_started = TRUE AND review_process_documented = FALSE THEN violation

[RULE-03] Manual code reviews MUST be performed by qualified personnel with appropriate security knowledge and application context understanding.
[VALIDATION] IF reviewer_qualified = FALSE OR reviewer_security_training = FALSE THEN violation

[RULE-04] Manual code review results MUST be documented and include identification of security weaknesses, access control verification, and cryptographic implementation analysis.
[VALIDATION] IF review_completed = TRUE AND (security_findings_documented = FALSE OR access_controls_verified = FALSE OR crypto_reviewed = FALSE) THEN violation

[RULE-05] Critical code components MUST NOT be deployed to production without completed manual code review and remediation of identified security issues.
[VALIDATION] IF deployment_status = "production" AND (manual_review_completed = FALSE OR critical_findings_unresolved = TRUE) THEN critical_violation

[RULE-06] Acquisition contracts MUST include manual code review requirements with specific deliverables and acceptance criteria.
[VALIDATION] IF contract_type = "development" AND manual_review_clause = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Code Identification - Process for determining which code components require manual review
- [PROC-02] Manual Review Execution - Step-by-step procedures for conducting manual code reviews
- [PROC-03] Review Documentation - Standards for documenting review findings and remediation
- [PROC-04] Contractor Compliance Verification - Process for validating third-party developer compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, regulatory changes, significant development methodology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Component Deployment]
IF component_criticality = "critical"
AND deployment_target = "production"
AND manual_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Third-Party Development Contract]
IF contract_type = "software_development"
AND manual_review_requirements = "not_specified"
AND component_criticality = "critical"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incomplete Review Documentation]
IF manual_review_completed = TRUE
AND security_findings_documented = TRUE
AND access_control_matrix_verified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unqualified Reviewer Assignment]
IF reviewer_assigned = TRUE
AND reviewer_security_certification = FALSE
AND component_type = "cryptographic_module"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: COTS with Source Code Access]
IF software_type = "COTS"
AND source_code_available = TRUE
AND component_criticality = "critical"
AND manual_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer performs manual code review of defined critical code | [RULE-01], [RULE-05] |
| Manual review processes and techniques are defined | [RULE-02] |
| Qualified personnel perform reviews | [RULE-03] |
| Review results are properly documented | [RULE-04] |
| Contract requirements include manual review clauses | [RULE-06] |