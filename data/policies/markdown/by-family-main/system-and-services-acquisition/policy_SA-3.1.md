# POLICY: SA-3.1: Manage Preproduction Environment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-3.1 |
| NIST Control | SA-3.1: Manage Preproduction Environment |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | preproduction, development, testing, integration, environment protection, SDLC, risk assessment |

## 1. POLICY STATEMENT
All system preproduction environments including development, test, and integration environments MUST be protected with security controls commensurate with the risk level of the target production system throughout the entire system development life cycle. Protection measures SHALL be implemented based on criticality analysis and documented risk assessments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Development environments | YES | All code development platforms |
| Test environments | YES | Including automated and manual testing |
| Integration environments | YES | Pre-production integration testing |
| Staging environments | YES | Production-like pre-deployment environments |
| Sandbox environments | CONDITIONAL | If processing production-like data |
| Third-party contractor environments | YES | When developing company systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Implement security controls in preproduction environments<br>• Follow secure development practices<br>• Report security incidents in preproduction |
| Security Architecture Team | • Define risk-appropriate security controls<br>• Conduct criticality analysis<br>• Review environment security configurations |
| DevOps/Platform Teams | • Configure and maintain secure preproduction infrastructure<br>• Implement access controls and monitoring<br>• Ensure environment isolation |

## 4. RULES
[RULE-01] Preproduction environments MUST implement security controls proportionate to the risk level of the target production system as determined by system categorization.
[VALIDATION] IF environment_type = "preproduction" AND security_controls < risk_appropriate_baseline THEN violation

[RULE-02] Development, test, and integration environments SHALL be subject to documented criticality analysis before deployment.
[VALIDATION] IF environment_status = "active" AND criticality_analysis_completed = FALSE THEN violation

[RULE-03] Access to preproduction environments MUST be restricted to authorized personnel with documented business justification and appropriate clearance levels.
[VALIDATION] IF user_access = TRUE AND (authorization_documented = FALSE OR business_justification = FALSE) THEN violation

[RULE-04] Preproduction environments processing sensitive data MUST implement data protection controls equivalent to production systems.
[VALIDATION] IF data_sensitivity_level = "high" AND environment_type = "preproduction" AND data_protection_controls < production_equivalent THEN critical_violation

[RULE-05] Security configurations and controls in preproduction environments SHALL be reviewed and updated at each SDLC phase transition.
[VALIDATION] IF sdlc_phase_change = TRUE AND security_review_completed = FALSE AND days_since_transition > 5 THEN violation

[RULE-06] Third-party contractor preproduction environments MUST meet the same security requirements as internal environments when developing company systems.
[VALIDATION] IF contractor_environment = TRUE AND security_requirements_compliance = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Preproduction Environment Security Assessment - Risk-based security control selection and implementation
- [PROC-02] Criticality Analysis Process - Systematic evaluation of environment importance and risk
- [PROC-03] Environment Access Management - Authorization and deprovisioning procedures
- [PROC-04] SDLC Security Review Gates - Phase-based security control validation
- [PROC-05] Contractor Environment Oversight - Third-party security compliance verification

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major SDLC process changes, security incidents in preproduction, new regulatory requirements, third-party contractor onboarding

## 7. SCENARIO PATTERNS
[SCENARIO-01: High-Risk System Development Environment]
IF target_system_risk_level = "high"
AND preproduction_environment_controls = "basic"
AND data_classification = "confidential"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Development Environment]
IF contractor_managed = TRUE
AND developing_company_system = TRUE
AND security_assessment_completed = TRUE
AND controls_equivalent_to_internal = TRUE
THEN compliance = TRUE

[SCENARIO-03: Test Environment Data Exposure]
IF environment_type = "test"
AND production_data_present = TRUE
AND data_protection_controls = "none"
AND data_sensitivity = "PII"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: SDLC Phase Transition Without Review]
IF sdlc_phase = "changed"
AND days_since_transition = 10
AND security_review_completed = FALSE
AND environment_risk_level = "medium"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Authorized Development Access]
IF user_role = "developer"
AND project_assignment = "active"
AND authorization_documented = TRUE
AND access_level = "appropriate_for_role"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System pre-production environments are protected commensurate with risk throughout SDLC | [RULE-01], [RULE-04], [RULE-05] |
| Criticality analysis applied to preproduction environments | [RULE-02] |
| Access controls implemented for preproduction environments | [RULE-03] |
| Third-party contractor environment oversight | [RULE-06] |