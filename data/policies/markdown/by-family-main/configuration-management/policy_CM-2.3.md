# POLICY: CM-2.3: Retention of Previous Configurations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-2.3 |
| NIST Control | CM-2.3: Retention of Previous Configurations |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | configuration management, baseline retention, rollback, version control, change management |

## 1. POLICY STATEMENT
The organization SHALL retain a defined number of previous baseline configuration versions for all information systems to support rollback capabilities. Configuration retention MUST include hardware, software, firmware, configuration files, configuration records, and associated documentation to ensure system recovery and operational continuity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All mission-critical and business systems |
| Development Systems | YES | Systems with regulatory requirements |
| Test/Staging Systems | CONDITIONAL | If used for compliance validation |
| Personal Devices | NO | Managed through separate MDM policies |
| Third-party SaaS | CONDITIONAL | If configuration data is accessible |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement automated configuration backup processes<br>• Maintain configuration version repositories<br>• Execute rollback procedures when authorized |
| Configuration Managers | • Define retention requirements per system classification<br>• Monitor compliance with retention policies<br>• Approve configuration rollback requests |
| Security Operations | • Validate configuration integrity<br>• Monitor unauthorized configuration changes<br>• Coordinate emergency rollback procedures |

## 4. RULES
[RULE-01] Organizations MUST define and document the number of previous baseline configuration versions to retain for each system based on criticality and regulatory requirements.
[VALIDATION] IF system_classification = "critical" AND retention_versions < 10 THEN violation
[VALIDATION] IF system_classification = "moderate" AND retention_versions < 5 THEN violation

[RULE-02] Previous baseline configurations MUST include hardware settings, software configurations, firmware versions, configuration files, configuration records, and associated documentation.
[VALIDATION] IF backup_components NOT CONTAINS ["hardware", "software", "firmware", "config_files", "documentation"] THEN violation

[RULE-03] Configuration versions MUST be retained for a minimum of 12 months or until superseded by the defined number of newer versions, whichever is longer.
[VALIDATION] IF oldest_config_age > 365_days AND retained_versions < minimum_required THEN violation

[RULE-04] Retained configurations MUST be stored in tamper-evident repositories with integrity verification mechanisms.
[VALIDATION] IF integrity_check_enabled = FALSE OR tamper_evidence = FALSE THEN violation

[RULE-05] Rollback procedures MUST be tested quarterly and documented with maximum recovery time objectives not exceeding 4 hours for critical systems.
[VALIDATION] IF last_rollback_test > 90_days OR recovery_time_objective > 4_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Configuration Baseline Creation - Establish and document system baseline configurations
- [PROC-02] Version Retention Management - Automated retention and purging of configuration versions
- [PROC-03] Rollback Execution - Step-by-step system rollback procedures
- [PROC-04] Integrity Verification - Regular validation of stored configuration integrity

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system changes, security incidents, regulatory updates, failed rollback attempts

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical System Insufficient Retention]
IF system_classification = "critical"
AND current_retained_versions < 10
AND regulatory_requirement = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Configuration Components]
IF backup_includes_hardware = FALSE
OR backup_includes_documentation = FALSE
AND system_type = "production"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Expired Rollback Testing]
IF last_rollback_test_date > 90_days
AND system_classification IN ["critical", "moderate"]
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Inadequate Retention Period]
IF oldest_configuration_age > 365_days
AND total_versions_retained < minimum_required_versions
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Successful Configuration Management]
IF retention_versions >= minimum_required
AND all_components_included = TRUE
AND integrity_verification = "PASS"
AND rollback_test_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Number of previous baseline configuration versions retained is defined | [RULE-01] |
| Previous baseline configuration versions are retained to support rollback | [RULE-02], [RULE-03] |
| Configuration integrity is maintained | [RULE-04] |
| Rollback capability is verified | [RULE-05] |