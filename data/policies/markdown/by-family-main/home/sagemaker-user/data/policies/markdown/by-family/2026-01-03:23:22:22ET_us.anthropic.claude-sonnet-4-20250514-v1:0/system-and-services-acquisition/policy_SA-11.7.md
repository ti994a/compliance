# POLICY: SA-11.7: Verify Scope of Testing and Evaluation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.7 |
| NIST Control | SA-11.7: Verify Scope of Testing and Evaluation |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer testing, security evaluation, control coverage, testing scope, verification |

## 1. POLICY STATEMENT
The organization SHALL require all system developers to verify that security testing and evaluation provides complete coverage of required security controls at organization-defined levels of rigor. Testing scope verification MUST demonstrate comprehensive control implementation coverage through appropriate analytic techniques.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All internal system development projects |
| External Contractors/Vendors | YES | All contracted development services |
| COTS Software Vendors | CONDITIONAL | When security testing is contractually required |
| Third-party Integrators | YES | Custom integrations and configurations |
| Cloud Service Providers | CONDITIONAL | When custom development is involved |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define testing rigor requirements<br>• Approve testing scope verification methods<br>• Oversee compliance monitoring |
| Procurement Manager | • Include testing verification requirements in contracts<br>• Validate vendor testing capabilities<br>• Monitor contract compliance |
| Security Architect | • Define required control coverage<br>• Review testing scope documentation<br>• Validate coverage completeness |
| Development Manager | • Ensure developer compliance<br>• Review testing verification results<br>• Coordinate with security teams |

## 4. RULES
[RULE-01] Developers MUST verify testing scope covers 100% of required security controls before system acceptance.
[VALIDATION] IF required_controls_tested < total_required_controls THEN violation

[RULE-02] Testing verification documentation MUST include breadth and depth analysis as defined by organizational requirements.
[VALIDATION] IF breadth_analysis = FALSE OR depth_analysis = FALSE THEN violation

[RULE-03] Verification methods SHALL correspond to system categorization: formal methods for HIGH systems, structured analysis for MODERATE systems, informal analysis acceptable for LOW systems.
[VALIDATION] IF system_impact = "HIGH" AND verification_method != "formal" THEN violation

[RULE-04] All acquisition contracts MUST specify testing scope verification requirements and deliverables.
[VALIDATION] IF contract_type = "development" AND testing_verification_clause = FALSE THEN violation

[RULE-05] Independent verification SHALL be required for systems processing PII or financial data.
[VALIDATION] IF (processes_PII = TRUE OR processes_financial = TRUE) AND independent_verification = FALSE THEN violation

[RULE-06] Testing coverage gaps MUST be documented and approved by CISO before system deployment.
[VALIDATION] IF coverage_gaps_exist = TRUE AND ciso_approval = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Testing Scope Verification - Standardized process for validating control coverage
- [PROC-02] Contract Security Testing Requirements - Template clauses and verification criteria
- [PROC-03] Coverage Gap Assessment - Process for identifying and approving testing exceptions
- [PROC-04] Independent Verification Management - Procedures for third-party testing validation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New regulatory requirements, significant security incidents, major system acquisitions

## 7. SCENARIO PATTERNS
[SCENARIO-01: Complete Coverage Verification]
IF all_required_controls_tested = TRUE
AND verification_documentation = "complete"
AND rigor_level = "appropriate_for_impact"
THEN compliance = TRUE

[SCENARIO-02: Incomplete Control Coverage]
IF required_controls_tested < 100%
AND coverage_gaps_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Inadequate Verification Method]
IF system_impact = "HIGH"
AND verification_method = "informal"
AND formal_analysis_waiver = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Contract Requirements]
IF contract_type = "custom_development"
AND testing_verification_requirements = FALSE
AND contract_executed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: PII System Without Independent Verification]
IF processes_PII = TRUE
AND independent_verification_completed = FALSE
AND system_deployment_approved = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer verification of complete control coverage | [RULE-01] |
| Breadth and depth of testing defined | [RULE-02] |
| Appropriate rigor level for system impact | [RULE-03] |
| Contract requirements specification | [RULE-04] |
| Independent verification for sensitive systems | [RULE-05] |
| Coverage gap management | [RULE-06] |