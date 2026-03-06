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
All system developers MUST verify that their testing and evaluation activities provide complete coverage of required security controls at organization-defined levels of rigor. The organization SHALL define the required breadth and depth of testing to ensure comprehensive security control validation before system deployment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal development teams | YES | All internally developed systems |
| External vendors/contractors | YES | All contracted development work |
| COTS software | CONDITIONAL | When customization involves security controls |
| System integrators | YES | When integrating multiple components |
| Cloud service providers | CONDITIONAL | When custom configurations affect security controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Conduct comprehensive testing per defined scope<br>• Document test coverage mapping<br>• Verify all required controls are tested |
| Security Architecture Team | • Define testing breadth and depth requirements<br>• Review test coverage documentation<br>• Validate testing methodology |
| Procurement Office | • Include testing requirements in contracts<br>• Monitor vendor compliance with testing scope<br>• Enforce contractual testing obligations |

## 4. RULES
[RULE-01] Developers MUST verify that testing scope covers 100% of required security controls identified in the system security plan.
[VALIDATION] IF required_controls_tested / total_required_controls < 1.0 THEN violation

[RULE-02] Testing breadth MUST include functional testing, integration testing, and regression testing for all security controls.
[VALIDATION] IF testing_types_completed < ["functional", "integration", "regression"] THEN violation

[RULE-03] Testing depth MUST achieve the rigor level defined in the acquisition contract, ranging from basic functional testing to formal verification methods.
[VALIDATION] IF achieved_rigor_level < contracted_rigor_level THEN violation

[RULE-04] Developers MUST provide traceability matrices mapping each required control to specific test cases and results.
[VALIDATION] IF control_to_test_mapping_complete = FALSE THEN violation

[RULE-05] Test coverage verification MUST be completed before system acceptance and SHALL be documented with evidence.
[VALIDATION] IF system_accepted = TRUE AND coverage_verification_complete = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Control Test Planning - Define testing scope and rigor requirements
- [PROC-02] Test Coverage Analysis - Verify complete control coverage mapping
- [PROC-03] Developer Testing Validation - Review and approve developer test results
- [PROC-04] Contract Compliance Monitoring - Ensure vendor adherence to testing requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon significant acquisition process changes
- Triggering events: Failed test coverage validation, new regulatory requirements, major system acquisitions

## 7. SCENARIO PATTERNS
[SCENARIO-01: Incomplete Control Coverage]
IF total_required_controls = 50
AND controls_tested = 45
AND coverage_percentage < 100%
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Insufficient Testing Rigor]
IF contract_requires_formal_verification = TRUE
AND developer_performed_basic_testing = TRUE
AND formal_verification_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Traceability Documentation]
IF all_controls_tested = TRUE
AND test_results_available = TRUE
AND traceability_matrix_provided = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Vendor Contract Compliance]
IF vendor_type = "external"
AND contract_specifies_testing_scope = TRUE
AND vendor_testing_meets_contract = TRUE
AND coverage_verification_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: System Acceptance Without Verification]
IF system_deployment_approved = TRUE
AND test_coverage_verification = "pending"
AND security_controls_count > 0
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer verification of testing scope completeness | [RULE-01], [RULE-04] |
| Defined breadth of testing and evaluation | [RULE-02] |
| Defined depth of testing and evaluation | [RULE-03] |
| Complete coverage of required controls | [RULE-01], [RULE-05] |