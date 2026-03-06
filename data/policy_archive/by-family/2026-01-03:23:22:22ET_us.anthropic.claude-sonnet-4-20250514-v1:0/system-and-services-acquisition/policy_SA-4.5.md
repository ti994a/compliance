# POLICY: SA-4.5: System, Component, and Service Configurations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.5 |
| NIST Control | SA-4.5: System, Component, and Service Configurations |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security configurations, system development, vendor requirements, baseline configurations, STIG, USGCB |

## 1. POLICY STATEMENT
All developers of systems, components, or services MUST deliver products with defined and implemented security configurations that serve as defaults for installations and upgrades. Security configurations MUST align with approved baselines such as USGCB, STIGs, or organization-specific security standards.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Developers | YES | Internal and external development teams |
| Component Vendors | YES | Hardware and software component suppliers |
| Service Providers | YES | Cloud and managed service providers |
| COTS Products | YES | Commercial off-the-shelf software/hardware |
| Open Source Software | CONDITIONAL | When integrated into enterprise systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Include security configuration requirements in contracts<br>• Validate vendor compliance with configuration standards<br>• Manage vendor security configuration deliverables |
| Security Architect | • Define approved security configuration baselines<br>• Review and approve vendor-provided configurations<br>• Establish configuration validation criteria |
| System Owner | • Ensure deployed systems use approved configurations<br>• Maintain configuration compliance during operations<br>• Coordinate with vendors on configuration updates |

## 4. RULES
[RULE-01] Developers MUST deliver systems, components, or services with security configurations that are fully defined and documented according to approved baseline standards.
[VALIDATION] IF delivery_includes_security_config = FALSE OR config_documentation = "incomplete" THEN violation

[RULE-02] All delivered security configurations MUST be implemented and active by default, not requiring additional configuration steps by the organization.
[VALIDATION] IF default_config_secure = FALSE OR manual_config_required = TRUE THEN violation

[RULE-03] Default passwords and authentication credentials MUST be changed from vendor defaults before delivery or during initial setup.
[VALIDATION] IF default_passwords_unchanged = TRUE THEN critical_violation

[RULE-04] Security configurations MUST be preserved and reapplied automatically during system reinstallation or upgrade processes.
[VALIDATION] IF upgrade_resets_security_config = TRUE AND auto_reapply = FALSE THEN violation

[RULE-05] Delivered configurations MUST disable unnecessary functions, ports, protocols, and services according to the principle of least functionality.
[VALIDATION] IF unnecessary_services_enabled = TRUE OR ports_not_minimized = TRUE THEN violation

[RULE-06] Vendors MUST provide configuration verification mechanisms or documentation to validate proper implementation.
[VALIDATION] IF verification_mechanism = "none" AND verification_docs = "absent" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Vendor Security Configuration Assessment - Evaluate and approve vendor-provided security configurations
- [PROC-02] Configuration Baseline Management - Maintain and update approved security configuration standards
- [PROC-03] Delivery Acceptance Testing - Verify security configurations meet requirements before acceptance
- [PROC-04] Configuration Change Control - Manage updates to security configurations through formal change process

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New baseline releases, vendor configuration changes, security incidents related to misconfigurations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Vendor Default Configuration]
IF vendor_delivery = TRUE
AND security_configs_defined = FALSE
AND contract_requires_configs = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Upgrade Configuration Reset]
IF system_upgrade = TRUE
AND security_configs_reset = TRUE
AND auto_reapply_disabled = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Default Password Delivery]
IF system_delivered = TRUE
AND default_passwords_present = TRUE
AND password_change_required = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: STIG Compliant Delivery]
IF vendor_delivery = TRUE
AND stig_baseline_applied = TRUE
AND unnecessary_services_disabled = TRUE
AND verification_provided = TRUE
THEN compliance = TRUE

[SCENARIO-05: Cloud Service Configuration]
IF service_type = "cloud"
AND security_configs_documented = TRUE
AND configs_implemented_by_default = TRUE
AND upgrade_preserves_configs = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer delivers system with defined security configurations | [RULE-01] |
| Security configurations are implemented by default | [RULE-02] |
| Configurations used as default for reinstallation/upgrade | [RULE-04] |
| Default passwords are changed | [RULE-03] |
| Unnecessary functions/services are disabled | [RULE-05] |
| Configuration verification mechanisms provided | [RULE-06] |