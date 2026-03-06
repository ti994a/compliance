# POLICY: SA-4.5: System, Component, and Service Configurations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.5 |
| NIST Control | SA-4.5: System, Component, and Service Configurations |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security configurations, developer requirements, baseline configurations, STIG, USGCB, default settings |

## 1. POLICY STATEMENT
All system, component, and service developers MUST deliver products with defined and implemented security configurations that serve as defaults for installations and upgrades. These configurations MUST align with approved security baselines and be maintained throughout the system lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Developers | YES | All contracted and internal development |
| Component Vendors | YES | Hardware and software components |
| Service Providers | YES | Cloud and managed services |
| COTS Products | YES | Commercial off-the-shelf acquisitions |
| Internal Applications | YES | Internally developed systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve security configuration standards<br>• Define baseline requirements<br>• Oversee compliance validation |
| Procurement Manager | • Include security configuration requirements in contracts<br>• Validate developer compliance before acceptance<br>• Maintain vendor accountability |
| System Developer | • Implement required security configurations<br>• Document configuration settings<br>• Ensure defaults persist through upgrades |

## 4. RULES
[RULE-01] Developers MUST deliver systems with security configurations that implement USGCB, STIGs, or organization-approved baselines.
[VALIDATION] IF security_baseline_implemented = FALSE OR baseline_type NOT IN ["USGCB", "STIG", "ORG_APPROVED"] THEN violation

[RULE-02] All default passwords MUST be changed and documented before system delivery.
[VALIDATION] IF default_passwords_changed = FALSE THEN critical_violation

[RULE-03] Security configurations MUST be automatically applied as defaults during reinstallation or upgrade processes.
[VALIDATION] IF upgrade_maintains_security_config = FALSE THEN violation

[RULE-04] Developers MUST provide documentation of all implemented security configurations and their validation methods.
[VALIDATION] IF security_config_documentation = NULL OR validation_methods_documented = FALSE THEN violation

[RULE-05] Unnecessary functions, ports, protocols, and services MUST be disabled by default according to principle of least functionality.
[VALIDATION] IF unnecessary_services_enabled = TRUE OR ports_minimized = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Configuration Validation - Verify developer-implemented configurations against approved baselines
- [PROC-02] Contract Security Requirements - Include specific security configuration clauses in acquisition contracts
- [PROC-03] Acceptance Testing - Validate security configurations before system acceptance
- [PROC-04] Configuration Management - Maintain and update security configuration requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New baseline releases, security incidents, failed audits, contract renewals

## 7. SCENARIO PATTERNS
[SCENARIO-01: COTS Software Delivery]
IF product_type = "COTS"
AND security_baseline_applied = FALSE
AND contract_specifies_config_requirements = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Cloud Service Default Configurations]
IF service_type = "cloud_service"
AND default_passwords_changed = TRUE
AND security_configs_documented = TRUE
AND baseline_compliance_verified = TRUE
THEN compliance = TRUE

[SCENARIO-03: System Upgrade Scenario]
IF event_type = "system_upgrade"
AND security_configs_maintained = FALSE
AND default_settings_reverted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Internal Development Delivery]
IF developer_type = "internal"
AND STIG_compliance = TRUE
AND unnecessary_services_disabled = TRUE
AND config_documentation_provided = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Deployment]
IF deployment_type = "emergency"
AND security_baseline_implemented = FALSE
AND risk_acceptance_documented = TRUE
AND remediation_plan_exists = TRUE
THEN compliance = CONDITIONAL
required_action = "Implement configurations within 30 days"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security configurations defined and implemented by developer | RULE-01, RULE-05 |
| Configurations used as default for reinstallation/upgrade | RULE-03 |
| Default passwords changed | RULE-02 |
| Security configuration documentation | RULE-04 |