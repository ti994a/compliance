```markdown
# POLICY: SA-11.5: Penetration Testing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.5 |
| NIST Control | SA-11.5: Penetration Testing |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | penetration testing, developer testing, security assessment, vulnerability testing, system acquisition |

## 1. POLICY STATEMENT
All system, system component, and system service developers MUST perform penetration testing at organization-defined levels of rigor and under specified constraints before system acceptance. Penetration testing MUST identify vulnerabilities resulting from implementation errors, configuration faults, and operational weaknesses while protecting any captured personally identifiable information.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Developers | YES | All contracted and internal developers |
| Component Vendors | YES | Third-party component providers |
| Service Providers | YES | External service providers |
| Legacy Systems | CONDITIONAL | Upon major updates or contract renewal |
| Development Environments | YES | Pre-production testing required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define penetration testing breadth and depth requirements<br>• Approve testing constraints and methodologies<br>• Review and accept testing results |
| Procurement Manager | • Include penetration testing requirements in contracts<br>• Verify developer compliance before acceptance<br>• Manage testing deliverable requirements |
| System Developer | • Perform penetration testing per specified requirements<br>• Document testing methodology and results<br>• Remediate identified vulnerabilities<br>• Protect PII during testing activities |

## 4. RULES

[RULE-01] Developers MUST perform penetration testing on all systems, components, and services before organizational acceptance using white-box, gray-box, or black-box methodologies as specified in contracts.
[VALIDATION] IF system_delivered = TRUE AND penetration_test_completed = FALSE THEN critical_violation

[RULE-02] Penetration testing breadth MUST cover all external interfaces, authentication mechanisms, data flows, and critical business functions as defined in the system security plan.
[VALIDATION] IF test_coverage < required_breadth_percentage THEN violation

[RULE-03] Penetration testing depth MUST include automated vulnerability scanning, manual testing by certified professionals, and source code analysis for custom applications.
[VALIDATION] IF test_methodology NOT IN [automated_scan, manual_test, code_review] THEN violation

[RULE-04] Penetration testing MUST be performed under production-like constraints including network segmentation, access controls, and monitoring systems active.
[VALIDATION] IF test_environment != production_like OR constraints_applied = FALSE THEN violation

[RULE-05] Any personally identifiable information captured during penetration testing MUST be handled according to privacy protection requirements and securely destroyed after testing completion.
[VALIDATION] IF pii_captured = TRUE AND privacy_controls_applied = FALSE THEN critical_violation

[RULE-06] Penetration testing results MUST be documented with vulnerability severity ratings, remediation recommendations, and developer response plans within 30 days of test completion.
[VALIDATION] IF test_completed = TRUE AND documentation_delivered > 30_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Penetration Testing Requirements - Define testing scope, methodology, and deliverables
- [PROC-02] Penetration Test Result Review - Evaluate findings and verify remediation
- [PROC-03] PII Protection During Testing - Safeguard captured sensitive data
- [PROC-04] Vulnerability Remediation Tracking - Monitor developer response to findings

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system acquisitions, contract renewals, significant security incidents

## 7. SCENARIO PATTERNS

[SCENARIO-01: Cloud Service Penetration Testing]
IF service_type = "cloud_service"
AND penetration_test_performed = TRUE
AND test_includes_api_security = TRUE
AND pii_protection_documented = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Source Code Review]
IF system_type = "custom_application"
AND penetration_test_completed = TRUE
AND source_code_review = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Inadequate Test Depth]
IF penetration_test_method = "automated_only"
AND manual_testing_performed = FALSE
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: PII Mishandling During Testing]
IF pii_captured_during_test = TRUE
AND privacy_controls_applied = FALSE
AND pii_retention > test_completion_date
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Delayed Testing Documentation]
IF penetration_test_completed = TRUE
AND documentation_delivery_days > 30
AND vulnerability_count > 0
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Breadth of penetration testing is defined | [RULE-02] |
| Depth of penetration testing is defined | [RULE-03] |
| Constraints of penetration testing are defined | [RULE-04] |
| Developer performs required testing | [RULE-01] |
| PII protection during testing | [RULE-05] |
| Testing documentation requirements | [RULE-06] |
```