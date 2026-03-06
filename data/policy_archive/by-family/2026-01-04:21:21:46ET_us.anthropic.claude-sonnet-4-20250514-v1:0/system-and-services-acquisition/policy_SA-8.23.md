# POLICY: SA-8.23: Secure Defaults

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-8.23 |
| NIST Control | SA-8.23: Secure Defaults |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | secure defaults, system configuration, access control, deny-by-default, baseline security |

## 1. POLICY STATEMENT
All systems and system components must implement the security design principle of secure defaults, ensuring restrictive and conservative security configurations are applied by default. Systems must operate with adequate self-protection in their default state and follow a "deny unless explicitly authorized" strategy for security functions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All cloud and on-premises systems |
| Development Systems | YES | Must follow secure defaults during development |
| Third-party Components | YES | Vendor products must meet secure default requirements |
| Network Infrastructure | YES | Routers, switches, firewalls, load balancers |
| Applications | YES | Custom and commercial applications |
| Test/Staging Systems | YES | Must mirror production security defaults |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Architects | • Define secure default configurations for system designs<br>• Ensure "deny-by-default" principles in access control design<br>• Document security configuration requirements |
| DevOps Engineers | • Implement secure default configurations in deployment pipelines<br>• Validate default configurations before system deployment<br>• Maintain configuration baselines |
| Security Engineers | • Review and approve secure default configurations<br>• Assess risk of systems that cannot meet secure default requirements<br>• Monitor compliance with secure default principles |

## 4. RULES
[RULE-01] All systems MUST be deployed with secure default configurations that enforce restrictive security policies without requiring additional configuration.
[VALIDATION] IF system_deployed = TRUE AND secure_defaults_applied = FALSE THEN critical_violation

[RULE-02] Access control mechanisms MUST implement "deny unless explicitly authorized" logic by default.
[VALIDATION] IF access_control_type = "allow_by_default" THEN critical_violation

[RULE-03] Systems that cannot operate securely in default configuration MUST undergo risk assessment and approval before deployment.
[VALIDATION] IF secure_defaults_adequate = FALSE AND risk_assessment_completed = FALSE THEN violation

[RULE-04] Default system configurations MUST NOT contain default passwords, open unnecessary ports, or enabled unnecessary services.
[VALIDATION] IF default_passwords_present = TRUE OR unnecessary_ports_open = TRUE OR unnecessary_services_enabled = TRUE THEN critical_violation

[RULE-05] System initialization failures MUST result in secure failure modes that either perform operations using secure defaults or deny the operation.
[VALIDATION] IF initialization_failed = TRUE AND failure_mode != "secure" THEN critical_violation

[RULE-06] All system components MUST be documented with their secure default configuration requirements and validation procedures.
[VALIDATION] IF system_component_deployed = TRUE AND secure_defaults_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Secure Configuration Baseline Management - Establish and maintain secure default configurations for all system types
- [PROC-02] Pre-Deployment Security Validation - Verify secure defaults are properly implemented before system deployment
- [PROC-03] Risk Assessment for Inadequate Defaults - Assess and approve systems that cannot meet secure default requirements
- [PROC-04] Configuration Drift Detection - Monitor and remediate deviations from secure default configurations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system types, security incidents related to default configurations, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Application Deployment]
IF application_type = "web_application"
AND default_authentication = "enabled"
AND default_access_level = "deny_all"
AND unnecessary_features = "disabled"
THEN compliance = TRUE

[SCENARIO-02: Database Default Configuration]
IF system_type = "database"
AND default_accounts = "disabled_or_removed"
AND default_ports = "non_standard"
AND encryption = "enabled_by_default"
THEN compliance = TRUE

[SCENARIO-03: Network Device with Weak Defaults]
IF device_type = "network_infrastructure"
AND default_passwords = "unchanged"
AND unnecessary_protocols = "enabled"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: System Initialization Failure]
IF system_initialization = "failed"
AND failure_response = "allow_all_access"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Third-party Component Assessment]
IF component_source = "third_party"
AND secure_defaults_adequate = FALSE
AND risk_assessment = "completed"
AND compensating_controls = "implemented"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Systems implement secure defaults principle | [RULE-01] |
| Deny-by-default access control implementation | [RULE-02] |
| Risk assessment for inadequate defaults | [RULE-03] |
| Secure failure modes during initialization | [RULE-05] |
| Documentation of secure default requirements | [RULE-06] |