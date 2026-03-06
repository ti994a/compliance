# POLICY: SA-11.6: Attack Surface Reviews

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.6 |
| NIST Control | SA-11.6: Attack Surface Reviews |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | attack surface, developer requirements, vulnerability assessment, system acquisition, security testing |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services SHALL perform attack surface reviews to identify and mitigate vulnerabilities in exposed areas. These reviews MUST analyze design and implementation changes to identify attack vectors and ensure unsafe functions are deprecated.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All systems developed internally |
| Third-party Vendors | YES | Contractual requirement for all acquisitions |
| System Components | YES | Including COTS and custom components |
| Legacy Systems | CONDITIONAL | During major updates or modifications |
| Cloud Services | YES | Custom configurations and integrations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish attack surface review requirements<br>• Approve review methodologies<br>• Monitor compliance across acquisitions |
| Procurement Team | • Include attack surface review clauses in contracts<br>• Validate vendor compliance documentation<br>• Escalate non-compliance issues |
| Development Teams | • Conduct attack surface reviews for internal projects<br>• Document identified vulnerabilities and mitigations<br>• Implement secure coding practices |
| Security Architecture | • Define attack surface review standards<br>• Review and validate developer assessments<br>• Provide guidance on vulnerability remediation |

## 4. RULES
[RULE-01] All system developers MUST perform attack surface reviews before each major release and after significant design changes.
[VALIDATION] IF major_release = TRUE AND attack_surface_review_completed = FALSE THEN violation

[RULE-02] Attack surface reviews MUST identify all accessible areas including hardware, software, and firmware components that could be exploited by adversaries.
[VALIDATION] IF review_scope NOT INCLUDES ["hardware", "software", "firmware"] THEN incomplete_review

[RULE-03] Developers MUST document all identified attack vectors and provide mitigation strategies within 30 days of discovery.
[VALIDATION] IF attack_vector_identified = TRUE AND documentation_date > discovery_date + 30_days THEN violation

[RULE-04] Unsafe functions identified during attack surface reviews MUST be deprecated and replaced with secure alternatives.
[VALIDATION] IF unsafe_function_identified = TRUE AND deprecation_plan = NULL THEN violation

[RULE-05] Third-party vendors MUST provide attack surface review documentation as part of contract deliverables before system acceptance.
[VALIDATION] IF vendor_system = TRUE AND attack_surface_documentation = FALSE AND system_accepted = TRUE THEN critical_violation

[RULE-06] Attack surface reviews MUST be performed by qualified security professionals with demonstrated expertise in vulnerability assessment.
[VALIDATION] IF reviewer_certification = NULL OR reviewer_experience < 2_years THEN qualification_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Attack Surface Review Methodology - Standard approach for conducting comprehensive attack surface assessments
- [PROC-02] Vendor Contract Requirements - Template clauses requiring attack surface reviews in acquisition contracts
- [PROC-03] Vulnerability Documentation - Process for documenting and tracking identified attack vectors and mitigations
- [PROC-04] Review Quality Assurance - Validation process to ensure attack surface reviews meet organizational standards

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, new threat intelligence, regulatory changes, significant architecture changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal Development Release]
IF development_type = "internal"
AND release_type = "major"
AND attack_surface_review = "completed"
AND vulnerabilities_documented = TRUE
THEN compliance = TRUE

[SCENARIO-02: Vendor System Without Review]
IF system_source = "third_party"
AND contract_includes_attack_surface_requirement = TRUE
AND vendor_provided_review = FALSE
AND system_deployment_approved = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Incomplete Attack Surface Coverage]
IF attack_surface_review = "completed"
AND review_includes_hardware = FALSE
AND system_has_hardware_components = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed Vulnerability Documentation]
IF attack_vector_identified = TRUE
AND discovery_date = "2024-01-01"
AND documentation_date = "2024-02-15"
AND current_date = "2024-02-20"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unqualified Reviewer]
IF attack_surface_review = "completed"
AND reviewer_security_certification = FALSE
AND reviewer_experience_years < 2
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer performs attack surface reviews | [RULE-01], [RULE-05] |
| Reviews cover all system components | [RULE-02] |
| Attack vectors are documented and mitigated | [RULE-03] |
| Unsafe functions are deprecated | [RULE-04] |
| Qualified personnel conduct reviews | [RULE-06] |