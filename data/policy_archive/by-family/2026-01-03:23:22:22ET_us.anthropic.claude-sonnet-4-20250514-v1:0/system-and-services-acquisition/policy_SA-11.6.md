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
All developers of systems, system components, or system services SHALL perform attack surface reviews to identify and mitigate vulnerabilities in accessible areas of the system. Attack surface reviews MUST analyze design and implementation changes to identify and correct security flaws including deprecation of unsafe functions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All systems developed internally |
| Third-Party Vendors | YES | Contractual requirement for all acquisitions |
| System Components | YES | Hardware, software, and firmware components |
| Cloud Services | YES | Custom configurations and integrations |
| COTS Products | CONDITIONAL | When source code access available |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish attack surface review requirements<br>• Approve review methodologies<br>• Monitor compliance across acquisitions |
| Procurement Manager | • Include attack surface review requirements in contracts<br>• Validate developer compliance before acceptance<br>• Maintain vendor compliance documentation |
| Development Manager | • Ensure internal teams perform attack surface reviews<br>• Validate review completeness and quality<br>• Implement identified remediation measures |

## 4. RULES
[RULE-01] All system developers MUST perform attack surface reviews for new systems, system components, and system services before deployment.
[VALIDATION] IF system_type IN ["new_system", "component", "service"] AND attack_surface_review_completed = FALSE THEN violation

[RULE-02] Attack surface reviews MUST be performed when design or implementation changes occur that could affect system exposure.
[VALIDATION] IF design_change = TRUE OR implementation_change = TRUE AND attack_surface_review_updated = FALSE THEN violation

[RULE-03] Attack surface reviews MUST identify and document all accessible areas including hardware, software, and firmware attack vectors.
[VALIDATION] IF review_scope NOT INCLUDES ["hardware", "software", "firmware"] THEN violation

[RULE-04] Developers MUST remediate identified attack surface vulnerabilities before system acceptance, including deprecation of unsafe functions.
[VALIDATION] IF vulnerabilities_identified > 0 AND remediation_status != "complete" AND system_status = "accepted" THEN violation

[RULE-05] Third-party vendors MUST provide attack surface review documentation as part of contract deliverables.
[VALIDATION] IF vendor_type = "third_party" AND attack_surface_documentation = FALSE AND contract_active = TRUE THEN violation

[RULE-06] Attack surface reviews MUST be updated within 30 days of significant system modifications or version updates.
[VALIDATION] IF system_modification_date > (current_date - 30_days) AND review_update_date < system_modification_date THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Attack Surface Review Methodology - Standardized approach for conducting comprehensive attack surface analysis
- [PROC-02] Vendor Contract Requirements - Template language requiring attack surface reviews in acquisition contracts
- [PROC-03] Vulnerability Remediation Process - Procedures for addressing identified attack surface vulnerabilities
- [PROC-04] Review Documentation Standards - Requirements for attack surface review reporting and documentation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, regulatory changes, significant acquisition process updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Deployment]
IF system_status = "ready_for_deployment"
AND attack_surface_review_completed = FALSE
AND system_type = "new_development"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Third-Party Service Integration]
IF vendor_type = "third_party"
AND service_type = "cloud_integration"
AND attack_surface_documentation_provided = TRUE
AND vulnerabilities_remediated = TRUE
THEN compliance = TRUE

[SCENARIO-03: System Modification Without Review Update]
IF system_modification_date = "2024-01-15"
AND last_attack_surface_review_date = "2023-12-01"
AND current_date = "2024-02-20"
AND review_update_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Vendor Non-Compliance]
IF contract_requires_attack_surface_review = TRUE
AND vendor_documentation_submitted = FALSE
AND system_acceptance_date > contract_deadline
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Identified Vulnerabilities Not Remediated]
IF attack_surface_review_completed = TRUE
AND critical_vulnerabilities_count > 0
AND remediation_status = "pending"
AND system_status = "production"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer performs attack surface reviews | [RULE-01], [RULE-05] |
| Reviews analyze design and implementation changes | [RULE-02], [RULE-06] |
| Attack vectors are identified and mitigated | [RULE-03], [RULE-04] |
| Unsafe functions are deprecated | [RULE-04] |