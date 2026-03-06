# POLICY: SA-11.6: Attack Surface Reviews

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.6 |
| NIST Control | SA-11.6: Attack Surface Reviews |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | attack surface, developer requirements, vulnerability assessment, secure development, system acquisition |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST perform attack surface reviews to identify and mitigate vulnerabilities in exposed areas. Attack surface reviews SHALL analyze design and implementation changes to identify new attack vectors and ensure appropriate remediation of identified security flaws.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal development teams | YES | All systems and components |
| Third-party developers | YES | Contractual requirement |
| COTS software vendors | CONDITIONAL | When customization occurs |
| Cloud service providers | CONDITIONAL | When developing custom services |
| Legacy systems | YES | During major updates only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish attack surface review requirements<br>• Approve review methodologies<br>• Oversee compliance monitoring |
| Procurement Manager | • Include attack surface review requirements in contracts<br>• Verify developer compliance<br>• Maintain vendor assessment records |
| Development Teams | • Conduct attack surface reviews<br>• Document identified vulnerabilities<br>• Implement required mitigations |
| Security Architecture | • Define attack surface review standards<br>• Review and validate assessment results<br>• Provide remediation guidance |

## 4. RULES
[RULE-01] All developers MUST perform attack surface reviews for new systems, system components, and system services before deployment.
[VALIDATION] IF system_status = "pre-deployment" AND attack_surface_review_completed = FALSE THEN violation

[RULE-02] Attack surface reviews MUST be conducted whenever design or implementation changes are made that could affect system exposure.
[VALIDATION] IF design_change = TRUE AND implementation_change = TRUE AND attack_surface_review_conducted = FALSE THEN violation

[RULE-03] Developers SHALL document all identified attack vectors and provide mitigation plans for each finding within 30 days of discovery.
[VALIDATION] IF attack_vector_identified = TRUE AND (mitigation_plan_exists = FALSE OR documentation_date > discovery_date + 30_days) THEN violation

[RULE-04] Attack surface reviews MUST include analysis of hardware, software, and firmware components for accessible weaknesses and deficiencies.
[VALIDATION] IF review_scope NOT includes ["hardware", "software", "firmware"] THEN violation

[RULE-05] Developers MUST deprecate or remove unsafe functions identified during attack surface reviews within 90 days unless a documented exception is approved.
[VALIDATION] IF unsafe_function_identified = TRUE AND function_status = "active" AND days_since_identification > 90 AND approved_exception = FALSE THEN violation

[RULE-06] Third-party developers SHALL provide attack surface review documentation as a contractual deliverable before system acceptance.
[VALIDATION] IF developer_type = "third-party" AND contract_deliverable_received = FALSE AND system_acceptance_requested = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Attack Surface Review Methodology - Standardized approach for conducting comprehensive attack surface assessments
- [PROC-02] Vulnerability Documentation Process - Requirements for documenting and tracking identified attack vectors
- [PROC-03] Mitigation Planning and Implementation - Process for developing and executing remediation plans
- [PROC-04] Contractor Assessment Requirements - Procedures for evaluating third-party developer compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, significant system changes, new regulatory requirements, failed compliance assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Third-party Development Contract]
IF developer_type = "third-party"
AND contract_signed = TRUE
AND attack_surface_review_clause = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: System Update Without Review]
IF system_change_type = "major_update"
AND attack_surface_modified = TRUE
AND post_change_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Identified Vulnerability Not Mitigated]
IF attack_vector_severity = "critical"
AND days_since_identification > 30
AND mitigation_status = "not_started"
AND approved_exception = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Review Scope]
IF attack_surface_review_completed = TRUE
AND reviewed_components NOT includes "firmware"
AND system_includes_firmware = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Internal Development]
IF developer_type = "internal"
AND attack_surface_review_completed = TRUE
AND all_findings_documented = TRUE
AND mitigation_plans_approved = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer performs attack surface reviews | [RULE-01], [RULE-06] |
| Reviews analyze design and implementation changes | [RULE-02] |
| Attack vectors are identified and mitigated | [RULE-03], [RULE-05] |
| Reviews cover hardware, software, and firmware | [RULE-04] |
| Unsafe functions are deprecated | [RULE-05] |