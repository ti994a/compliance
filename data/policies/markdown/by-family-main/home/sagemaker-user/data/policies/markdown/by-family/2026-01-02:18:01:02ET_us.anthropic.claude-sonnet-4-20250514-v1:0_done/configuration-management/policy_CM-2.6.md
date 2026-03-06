# POLICY: CM-2.6: Development and Test Environments

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-2.6 |
| NIST Control | CM-2.6: Development and Test Environments |
| Version | 1.0 |
| Owner | Configuration Management Team |
| Keywords | baseline configuration, development environment, test environment, operational environment, configuration management, separation |

## 1. POLICY STATEMENT
The organization MUST maintain separate baseline configurations for development and test environments that are managed independently from operational baseline configurations. These environments SHALL support appropriate configuration management practices while maintaining sufficient similarity to operational systems for meaningful testing results.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Development environments | YES | All systems used for software/system development |
| Test environments | YES | All systems used for testing activities |
| Operational environments | YES | For baseline separation requirements |
| Sandbox environments | YES | When used for development or testing |
| Production systems | NO | Covered under base CM-2 control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Configuration Management Team | • Maintain separate baseline configurations<br>• Ensure proper separation between environment types<br>• Document configuration differences and rationale |
| Development Teams | • Adhere to development environment baseline requirements<br>• Request configuration changes through proper channels<br>• Maintain environment integrity |
| QA/Test Teams | • Follow test environment baseline configurations<br>• Ensure test environments mirror operational configurations appropriately<br>• Report configuration drift issues |

## 4. RULES
[RULE-01] Development environments MUST maintain baseline configurations that are documented and managed separately from operational baseline configurations.
[VALIDATION] IF environment_type = "development" AND baseline_config_separation = FALSE THEN violation

[RULE-02] Test environments MUST maintain baseline configurations that are documented and managed separately from operational baseline configurations.
[VALIDATION] IF environment_type = "test" AND baseline_config_separation = FALSE THEN violation

[RULE-03] Test environment configurations SHOULD mirror operational environment configurations to the extent practicable while maintaining separate management processes.
[VALIDATION] IF environment_type = "test" AND operational_similarity_documented = FALSE THEN minor_violation

[RULE-04] Configuration changes in development and test environments MUST be managed through separate change control processes from operational environments.
[VALIDATION] IF (environment_type = "development" OR environment_type = "test") AND change_control_process = "operational" THEN violation

[RULE-05] Baseline configuration documentation MUST clearly identify the environment type and management responsibilities for each configuration.
[VALIDATION] IF baseline_documentation_exists = TRUE AND environment_type_identified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Environment Baseline Management - Establish and maintain separate baseline configurations for each environment type
- [PROC-02] Configuration Change Control - Implement separate change management processes for non-operational environments
- [PROC-03] Environment Similarity Assessment - Evaluate and document appropriate levels of similarity between test and operational configurations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system changes, environment architecture changes, security incidents affecting configuration management

## 7. SCENARIO PATTERNS
[SCENARIO-01: Shared Configuration Management]
IF development_environment_exists = TRUE
AND operational_environment_exists = TRUE
AND configuration_management_process = "shared"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Undocumented Test Environment]
IF test_environment_exists = TRUE
AND baseline_configuration_documented = FALSE
AND separate_management = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Proper Environment Separation]
IF development_baseline_separate = TRUE
AND test_baseline_separate = TRUE
AND operational_baseline_separate = TRUE
AND management_processes_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Test Environment Drift]
IF test_environment_baseline_defined = TRUE
AND operational_similarity_required = TRUE
AND similarity_assessment_current = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Development Environment Using Operational Controls]
IF environment_type = "development"
AND using_operational_change_control = TRUE
AND separate_baseline_management = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Baseline configuration for development environments managed separately | RULE-01, RULE-04 |
| Baseline configuration for test environments managed separately | RULE-02, RULE-04 |
| Appropriate similarity between test and operational environments | RULE-03 |
| Documented environment identification and management | RULE-05 |