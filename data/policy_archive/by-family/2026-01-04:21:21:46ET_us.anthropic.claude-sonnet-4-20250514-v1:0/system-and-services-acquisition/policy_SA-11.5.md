# POLICY: SA-11.5: Penetration Testing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.5 |
| NIST Control | SA-11.5: Penetration Testing |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | penetration testing, developer testing, vulnerability assessment, security testing, system acquisition |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services acquired by the organization MUST perform penetration testing at organization-defined levels of rigor and under specified constraints. Penetration testing MUST be conducted to discover vulnerabilities resulting from implementation errors, configuration faults, or operational weaknesses before system deployment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Custom developed systems | YES | All internally developed systems |
| Third-party developed systems | YES | Systems developed specifically for organization |
| COTS software customizations | YES | When customization involves security-relevant code |
| Standard COTS products | NO | Unless organization-specific configuration required |
| Cloud service integrations | CONDITIONAL | When custom development is involved |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define penetration testing requirements and constraints<br>• Approve penetration testing methodologies<br>• Review and accept penetration testing results |
| Procurement Manager | • Include penetration testing requirements in contracts<br>• Verify developer compliance with testing requirements<br>• Manage penetration testing deliverables |
| System Developer | • Perform penetration testing per specified requirements<br>• Document testing methodology and results<br>• Remediate identified vulnerabilities |

## 4. RULES
[RULE-01] Developers MUST perform penetration testing on all custom-developed systems and components before delivery or deployment.
[VALIDATION] IF system_type = "custom_developed" AND penetration_testing_completed = FALSE THEN violation

[RULE-02] Penetration testing MUST include both breadth testing (coverage of attack surface) and depth testing (thorough analysis of critical components) as defined in the acquisition contract.
[VALIDATION] IF breadth_testing_documented = FALSE OR depth_testing_documented = FALSE THEN violation

[RULE-03] Penetration testing MUST be performed under organization-defined constraints including test environment limitations, time windows, and data handling requirements.
[VALIDATION] IF testing_constraints_defined = FALSE OR constraints_followed = FALSE THEN violation

[RULE-04] Penetration testing MUST be conducted by skilled professionals using white-box, gray-box, or black-box methodologies as specified in the contract.
[VALIDATION] IF tester_qualifications_verified = FALSE OR methodology_documented = FALSE THEN violation

[RULE-05] All vulnerabilities identified during penetration testing MUST be documented, risk-rated, and remediated before system acceptance.
[VALIDATION] IF vulnerabilities_documented = FALSE OR high_risk_vulnerabilities_open = TRUE THEN violation

[RULE-06] When personally identifiable information is captured during penetration testing, it MUST be handled according to privacy protection requirements.
[VALIDATION] IF pii_captured = TRUE AND privacy_controls_applied = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Penetration Testing Requirements - Define testing scope, methodology, and deliverables
- [PROC-02] Penetration Testing Result Review - Process for evaluating and accepting testing results
- [PROC-03] Vulnerability Remediation Tracking - Monitor and verify fix implementation
- [PROC-04] PII Handling During Testing - Protect privacy during security assessments

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system acquisitions, regulatory changes, security incidents involving tested systems

## 7. SCENARIO PATTERNS
[SCENARIO-01: Custom Application Development]
IF system_type = "custom_application"
AND development_phase = "pre-deployment"
AND penetration_testing_completed = TRUE
AND all_high_vulnerabilities_remediated = TRUE
THEN compliance = TRUE

[SCENARIO-02: Third-Party Development Missing Testing]
IF system_source = "third_party_developer"
AND penetration_testing_required = TRUE
AND penetration_testing_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Inadequate Testing Scope]
IF penetration_testing_completed = TRUE
AND breadth_testing_performed = FALSE
AND contract_requires_breadth_testing = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: PII Exposure During Testing]
IF penetration_testing_active = TRUE
AND pii_data_accessed = TRUE
AND privacy_controls_implemented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Unqualified Penetration Testers]
IF penetration_testing_performed = TRUE
AND tester_certification_verified = FALSE
AND skilled_professional_requirement = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer performs penetration testing | RULE-01 |
| Breadth of testing defined | RULE-02 |
| Depth of testing defined | RULE-02 |
| Testing constraints defined and followed | RULE-03 |
| Qualified professionals conduct testing | RULE-04 |
| Vulnerabilities properly addressed | RULE-05 |
| PII protection during testing | RULE-06 |