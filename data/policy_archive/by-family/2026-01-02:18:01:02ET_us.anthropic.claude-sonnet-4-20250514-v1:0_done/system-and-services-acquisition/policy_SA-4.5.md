# POLICY: SA-4.5: System, Component, and Service Configurations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.5 |
| NIST Control | SA-4.5: System, Component, and Service Configurations |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security configurations, developer requirements, default settings, system delivery, acquisition contracts |

## 1. POLICY STATEMENT
All system, component, and service developers MUST deliver products with defined and implemented security configurations that serve as defaults for installations and upgrades. These configurations MUST align with organizational security baselines and industry standards such as USGCB, STIGs, and organizational security requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External Developers | YES | All contracted system/component/service providers |
| Internal Development Teams | YES | All internally developed systems and components |
| COTS/SaaS Vendors | YES | Configuration requirements in procurement contracts |
| Cloud Service Providers | YES | Infrastructure and platform configuration requirements |
| Third-party Integrators | YES | Systems integration and deployment activities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve security configuration baselines<br>• Oversee policy compliance<br>• Define security configuration standards |
| Procurement Manager | • Include security configuration requirements in contracts<br>• Verify vendor compliance before acceptance<br>• Manage vendor security configuration deliverables |
| System Owner | • Validate delivered configurations meet requirements<br>• Approve configuration baselines for their systems<br>• Ensure ongoing compliance during upgrades |
| Developer/Vendor | • Implement required security configurations<br>• Document configuration settings and rationale<br>• Provide configuration verification evidence |

## 4. RULES
[RULE-01] All acquisition contracts MUST include explicit requirements for developers to deliver systems with defined, implemented, and documented security configurations.
[VALIDATION] IF contract_type IN ["system_development", "component_procurement", "service_acquisition"] AND security_config_requirements = FALSE THEN violation

[RULE-02] Developers MUST change all default passwords and disable unnecessary services, ports, and protocols before system delivery.
[VALIDATION] IF default_passwords_changed = FALSE OR unnecessary_services_disabled = FALSE THEN critical_violation

[RULE-03] Security configurations MUST be based on approved organizational baselines such as USGCB, STIGs, or equivalent industry standards.
[VALIDATION] IF security_baseline NOT IN ["USGCB", "STIG", "CIS_Benchmark", "org_approved_baseline"] THEN violation

[RULE-04] Delivered security configurations MUST serve as the default for all subsequent reinstallations, upgrades, and deployments.
[VALIDATION] IF upgrade_performed = TRUE AND default_config_maintained = FALSE THEN violation

[RULE-05] Developers MUST provide documentation detailing all implemented security configurations and their verification procedures.
[VALIDATION] IF config_documentation = FALSE OR verification_procedures = FALSE THEN violation

[RULE-06] Security configurations MUST be verified and validated before system acceptance and deployment.
[VALIDATION] IF config_verification_completed = FALSE AND system_status = "deployed" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Configuration Baseline Development - Define and maintain organizational security configuration standards
- [PROC-02] Contract Security Requirements Integration - Include security configuration requirements in all acquisition contracts
- [PROC-03] Delivered System Configuration Verification - Validate security configurations before system acceptance
- [PROC-04] Configuration Documentation Review - Assess completeness and accuracy of vendor-provided configuration documentation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New security baseline releases, major security incidents, regulatory changes, failed configuration audits

## 7. SCENARIO PATTERNS
[SCENARIO-01: COTS Software Deployment]
IF system_type = "COTS"
AND default_passwords_changed = FALSE
AND system_status = "ready_for_deployment"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Cloud Service Configuration]
IF service_type = "cloud_service"
AND security_baseline_applied = TRUE
AND config_documentation_provided = TRUE
AND verification_completed = TRUE
THEN compliance = TRUE

[SCENARIO-03: System Upgrade Without Baseline]
IF activity_type = "system_upgrade"
AND security_baseline_maintained = FALSE
AND upgrade_completed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Contract Missing Security Requirements]
IF contract_type = "system_development"
AND security_config_requirements_included = FALSE
AND contract_status = "executed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Undocumented Configuration Delivery]
IF system_delivered = TRUE
AND config_documentation_provided = FALSE
AND security_configs_implemented = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer required to deliver with defined security configurations | [RULE-01], [RULE-03] |
| Security configurations must be implemented | [RULE-02], [RULE-06] |
| Configurations used as default for reinstallation/upgrade | [RULE-04] |
| Configuration documentation and verification | [RULE-05], [RULE-06] |