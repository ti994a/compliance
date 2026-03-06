# POLICY: SA-8.23: Secure Defaults

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-8.23 |
| NIST Control | SA-8.23: Secure Defaults |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | secure defaults, system configuration, security design, baseline configuration, deny-by-default |

## 1. POLICY STATEMENT
All systems and system components must implement secure defaults that enforce restrictive and conservative security policies from initial deployment. Default configurations must follow a "deny unless explicitly authorized" approach and provide adequate self-protection before custom security policies are established.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All production, development, and test systems |
| System Components | YES | Hardware, software, network devices, applications |
| Cloud Services | YES | IaaS, PaaS, SaaS implementations |
| Third-party Systems | YES | Vendor-provided systems and components |
| Legacy Systems | CONDITIONAL | Must comply within 12 months or document risk acceptance |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Architects | • Define secure default requirements in system specifications<br>• Validate secure default implementation in design reviews<br>• Ensure "deny-by-default" principles in access control design |
| Development Teams | • Implement secure defaults in all system components<br>• Document default configuration security features<br>• Test secure failure modes and initialization processes |
| Security Engineering | • Review and approve secure default configurations<br>• Define security baseline requirements<br>• Validate compliance with secure default principles |

## 4. RULES
[RULE-01] All systems and system components MUST implement secure defaults that deny access or functionality unless explicitly authorized.
[VALIDATION] IF system_has_secure_defaults = FALSE OR default_policy = "allow_by_default" THEN critical_violation

[RULE-02] Default configurations MUST provide adequate self-protection and prevent security policy violations in "as-shipped" state.
[VALIDATION] IF as_shipped_config_secure = FALSE OR self_protection_adequate = FALSE THEN major_violation

[RULE-03] Systems that fail to complete initialization MUST either operate using secure defaults or fail to a secure state without performing the requested operation.
[VALIDATION] IF initialization_failed = TRUE AND (secure_failure_mode = FALSE OR insecure_operation_performed = TRUE) THEN critical_violation

[RULE-04] Security mechanisms MUST deny requests by default unless the request is well-formed and consistent with security policy.
[VALIDATION] IF default_request_handling = "allow" OR policy_validation_bypassed = TRUE THEN major_violation

[RULE-05] Risk assessment MUST be completed and documented when default protection is determined to be inadequate before system deployment.
[VALIDATION] IF default_protection_adequate = FALSE AND risk_assessment_completed = FALSE THEN major_violation

[RULE-06] Secure default implementation MUST be validated during system specification, design, development, and modification phases.
[VALIDATION] IF secure_defaults_validated = FALSE AND system_phase IN ["specification", "design", "development", "modification"] THEN moderate_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Secure Default Configuration Standards - Define organization-wide secure default requirements
- [PROC-02] System Initialization Security Validation - Verify secure startup and failure modes
- [PROC-03] Default Configuration Risk Assessment - Evaluate and document risks when defaults are inadequate
- [PROC-04] Secure Default Testing Procedures - Test deny-by-default mechanisms and secure failure modes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New system deployments, security incidents involving default configurations, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Deployment]
IF system_deployment_status = "new"
AND secure_defaults_implemented = TRUE
AND default_policy = "deny_by_default"
AND initialization_secure = TRUE
THEN compliance = TRUE

[SCENARIO-02: System with Inadequate Defaults]
IF default_protection_adequate = FALSE
AND risk_assessment_completed = FALSE
AND system_deployed = TRUE
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-03: Failed System Initialization]
IF system_initialization = "failed"
AND secure_failure_mode = TRUE
AND no_insecure_operations = TRUE
THEN compliance = TRUE

[SCENARIO-04: Legacy System Exception]
IF system_type = "legacy"
AND secure_defaults_implemented = FALSE
AND risk_acceptance_documented = TRUE
AND remediation_plan_exists = TRUE
AND remediation_timeline <= 12_months
THEN compliance = TRUE

[SCENARIO-05: Development Phase Validation Missing]
IF system_phase = "development"
AND secure_defaults_validated = FALSE
AND deployment_date <= 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Systems implement security design principle of secure defaults | [RULE-01], [RULE-02] |
| Define systems/components that implement secure defaults | [RULE-06] |
| Secure failure and initialization modes | [RULE-03] |
| Deny-by-default access control | [RULE-04] |
| Risk assessment for inadequate defaults | [RULE-05] |