# POLICY: SA-11.2: Threat Modeling and Vulnerability Analyses

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.2 |
| NIST Control | SA-11.2: Threat Modeling and Vulnerability Analyses |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | threat modeling, vulnerability analysis, developer requirements, SDLC, testing, evaluation |

## 1. POLICY STATEMENT
All system developers MUST perform comprehensive threat modeling and vulnerability analyses during both development and testing phases using organization-defined contextual information, tools, and acceptance criteria. These analyses MUST be conducted at specified rigor levels and produce evidence meeting established acceptance criteria to ensure security vulnerabilities are identified and mitigated before system deployment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal development teams | YES | All systems and components |
| Third-party developers | YES | Contract requirements mandatory |
| Vendor-supplied components | YES | Evidence required from vendor |
| COTS software | CONDITIONAL | When source code access available |
| Cloud service providers | YES | SaaS/PaaS development activities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Conduct threat modeling during development phases<br>• Perform vulnerability analyses using approved tools<br>• Document findings and remediation actions<br>• Provide evidence meeting acceptance criteria |
| Security Architecture | • Define contextual information requirements<br>• Approve threat modeling tools and methodologies<br>• Establish acceptance criteria for evidence<br>• Review and validate analysis results |
| Procurement | • Include threat modeling requirements in contracts<br>• Verify vendor compliance with analysis requirements<br>• Collect and validate evidence from third parties |

## 4. RULES
[RULE-01] Developers MUST perform threat modeling during initial development phase using organization-defined impact levels, operational environment, known threats, and acceptable risk levels as contextual information.
[VALIDATION] IF development_phase = "active" AND threat_modeling_completed = FALSE THEN violation

[RULE-02] Developers MUST conduct vulnerability analyses during development using approved scanning tools and manual assessment methods with minimum CVSS 4.0+ detection capability.
[VALIDATION] IF vulnerability_analysis_completed = FALSE AND development_phase = "active" THEN violation

[RULE-03] Threat modeling and vulnerability analyses MUST be repeated during testing and evaluation phases when design or implementation changes occur.
[VALIDATION] IF testing_phase = "active" AND (design_changes = TRUE OR implementation_changes = TRUE) AND updated_analysis = FALSE THEN violation

[RULE-04] All threat modeling MUST employ organization-approved tools including STRIDE methodology, attack trees, and data flow diagrams with comprehensive asset identification.
[VALIDATION] IF threat_modeling_tools NOT IN approved_tools_list THEN violation

[RULE-05] Vulnerability analyses MUST achieve minimum 95% code coverage for static analysis and include dynamic testing of all external interfaces.
[VALIDATION] IF static_analysis_coverage < 95% OR dynamic_testing_complete = FALSE THEN violation

[RULE-06] Analysis evidence MUST include executive summary, detailed findings, risk ratings, and remediation recommendations meeting organization-defined acceptance criteria.
[VALIDATION] IF evidence_completeness_score < acceptance_threshold THEN violation

[RULE-07] Critical and high-severity vulnerabilities identified during analyses MUST be remediated before system deployment or receive documented risk acceptance.
[VALIDATION] IF (vulnerability_severity = "critical" OR vulnerability_severity = "high") AND remediated = FALSE AND risk_accepted = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Threat Modeling Execution - Standardized process for conducting STRIDE-based threat modeling
- [PROC-02] Vulnerability Analysis Workflow - Procedures for static and dynamic security testing
- [PROC-03] Evidence Collection and Validation - Requirements for documenting and reviewing analysis results
- [PROC-04] Third-Party Vendor Assessment - Process for validating contractor threat modeling compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, tool updates, regulatory changes, failed assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal Development Compliance]
IF development_type = "internal"
AND threat_modeling_completed = TRUE
AND vulnerability_analysis_completed = TRUE
AND approved_tools_used = TRUE
AND evidence_meets_criteria = TRUE
THEN compliance = TRUE

[SCENARIO-02: Third-Party Development Gap]
IF development_type = "third_party"
AND contract_includes_requirements = TRUE
AND threat_modeling_evidence = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Testing Phase Changes]
IF phase = "testing"
AND implementation_changes = TRUE
AND updated_threat_model = FALSE
AND days_since_change > 14
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Critical Vulnerability Deployment]
IF vulnerability_severity = "critical"
AND remediated = FALSE
AND risk_accepted = FALSE
AND deployment_approved = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Inadequate Tool Usage]
IF threat_modeling_method NOT IN ["STRIDE", "PASTA", "TRIKE"]
AND manual_review_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Threat modeling during development with contextual information | [RULE-01] |
| Vulnerability analyses during development with contextual information | [RULE-02] |
| Threat modeling during testing and evaluation | [RULE-03] |
| Vulnerability analyses during testing and evaluation | [RULE-03] |
| Use of approved tools and methods for threat modeling | [RULE-04] |
| Use of approved tools and methods for vulnerability analyses | [RULE-04], [RULE-05] |
| Defined rigor level for analyses | [RULE-05] |
| Evidence meeting acceptance criteria | [RULE-06] |