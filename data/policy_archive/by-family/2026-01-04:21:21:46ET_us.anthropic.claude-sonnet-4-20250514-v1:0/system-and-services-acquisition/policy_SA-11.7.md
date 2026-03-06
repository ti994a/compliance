# POLICY: SA-11.7: Verify Scope of Testing and Evaluation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.7 |
| NIST Control | SA-11.7: Verify Scope of Testing and Evaluation |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer testing, security controls coverage, testing scope verification, evaluation rigor, control validation |

## 1. POLICY STATEMENT
All system developers MUST verify that security testing and evaluation provides complete coverage of required controls at organization-defined levels of breadth and depth. Testing scope verification MUST be documented and validated before system acceptance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Developers | YES | Internal and external developers |
| System Components | YES | COTS, custom, and hybrid components |
| System Services | YES | Cloud and on-premise services |
| Development Contractors | YES | All contracted development work |
| Legacy Systems | CONDITIONAL | When undergoing major updates |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Developers | • Conduct comprehensive control testing<br>• Document testing scope and coverage<br>• Verify completeness of security control validation |
| Security Architecture Team | • Define required testing breadth and depth<br>• Review testing plans for adequacy<br>• Validate control coverage completeness |
| Procurement Team | • Include testing requirements in contracts<br>• Monitor developer compliance with testing standards<br>• Ensure contractual testing deliverables |

## 4. RULES
[RULE-01] Developers MUST verify testing scope covers 100% of required security controls before system delivery.
[VALIDATION] IF required_controls_tested < total_required_controls THEN violation

[RULE-02] Testing breadth MUST include all control families applicable to the system's security categorization level.
[VALIDATION] IF applicable_control_families_tested < total_applicable_families THEN violation

[RULE-03] Testing depth MUST achieve organization-defined rigor levels: basic (functional testing), moderate (boundary testing), or high (formal analysis).
[VALIDATION] IF testing_rigor_level < required_rigor_level THEN violation

[RULE-04] Developers MUST provide testing coverage documentation mapping each required control to specific test cases.
[VALIDATION] IF control_to_testcase_mapping = incomplete THEN violation

[RULE-05] Testing scope verification MUST be completed and approved before system acceptance or deployment authorization.
[VALIDATION] IF system_deployed = TRUE AND testing_verification_approved = FALSE THEN critical_violation

[RULE-06] For high-impact systems, developers MUST use formal modeling and analysis techniques to demonstrate control coverage.
[VALIDATION] IF system_impact = "high" AND formal_analysis_used = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Control Testing Plan Development - Define comprehensive testing approach for all required controls
- [PROC-02] Testing Coverage Verification - Validate completeness of control testing scope
- [PROC-03] Test Case to Control Mapping - Document traceability between controls and test procedures
- [PROC-04] Testing Rigor Assessment - Evaluate adequacy of testing depth and analytical techniques

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: New system acquisitions, major system updates, control baseline changes, security incidents related to inadequate testing

## 7. SCENARIO PATTERNS
[SCENARIO-01: Incomplete Control Testing]
IF total_required_controls = 50
AND controls_tested = 45
AND system_ready_for_deployment = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate Testing Rigor]
IF system_impact_level = "high"
AND required_rigor = "formal_analysis"
AND actual_testing_method = "functional_only"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Control Mapping]
IF testing_completed = TRUE
AND control_testcase_mapping = "not_provided"
AND system_acceptance_requested = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Approved Comprehensive Testing]
IF required_controls_coverage = 100%
AND testing_rigor_adequate = TRUE
AND documentation_complete = TRUE
AND verification_approved = TRUE
THEN compliance = TRUE

[SCENARIO-05: Legacy System Exception]
IF system_type = "legacy"
AND major_update = FALSE
AND current_testing_waiver = "approved"
AND waiver_expiration > current_date
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer verification of complete control coverage | [RULE-01], [RULE-04] |
| Breadth of testing defined and implemented | [RULE-02] |
| Depth of testing defined and implemented | [RULE-03], [RULE-06] |
| Testing scope verification before acceptance | [RULE-05] |