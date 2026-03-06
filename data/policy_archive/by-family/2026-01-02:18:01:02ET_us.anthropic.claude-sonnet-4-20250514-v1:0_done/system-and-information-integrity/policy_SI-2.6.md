# POLICY: SI-2.6: Removal of Previous Versions of Software and Firmware

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-2.6 |
| NIST Control | SI-2.6: Removal of Previous Versions of Software and Firmware |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | software removal, firmware removal, version control, patch management, vulnerability mitigation |

## 1. POLICY STATEMENT
The organization SHALL remove previous versions of software and firmware components after updated versions have been successfully installed and validated. This policy ensures that outdated components cannot be exploited by adversaries and reduces the attack surface of information systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including production, development, and test environments |
| Software applications | YES | Operating systems, applications, middleware, utilities |
| Firmware components | YES | BIOS, network devices, storage systems, embedded systems |
| Third-party managed systems | CONDITIONAL | When organization has administrative control |
| Legacy systems | CONDITIONAL | Based on criticality and technical feasibility |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Execute removal of previous software/firmware versions<br>• Validate successful installation of updates<br>• Document removal activities |
| Security Team | • Define removal requirements and timelines<br>• Monitor compliance with removal procedures<br>• Assess security implications of version retention |
| Change Management | • Approve removal procedures<br>• Coordinate removal activities<br>• Maintain rollback capabilities when required |

## 4. RULES
[RULE-01] Previous versions of software and firmware components MUST be removed within 30 days after updated versions have been installed and validated in production environments.
[VALIDATION] IF update_installed = TRUE AND validation_complete = TRUE AND days_since_update > 30 AND previous_version_present = TRUE THEN violation

[RULE-02] Critical security updates MUST have previous versions removed within 7 days of successful installation and validation.
[VALIDATION] IF update_type = "critical_security" AND validation_complete = TRUE AND days_since_update > 7 AND previous_version_present = TRUE THEN critical_violation

[RULE-03] Organizations MUST maintain an inventory of software and firmware components that identifies current and previous versions present on systems.
[VALIDATION] IF system_inventory_exists = FALSE OR inventory_last_updated > 90_days THEN violation

[RULE-04] Automated removal mechanisms SHOULD be implemented where technically feasible to remove previous versions without manual intervention.
[VALIDATION] IF manual_removal_required = TRUE AND automation_feasible = TRUE AND automation_implemented = FALSE THEN minor_violation

[RULE-05] Removal activities MUST be documented with justification for any exceptions where previous versions are retained.
[VALIDATION] IF previous_version_present = TRUE AND (removal_documentation = FALSE OR exception_justification = FALSE) THEN violation

[RULE-06] Rollback procedures MUST be tested and validated before removing previous versions for mission-critical systems.
[VALIDATION] IF system_criticality = "mission_critical" AND rollback_tested = FALSE AND previous_version_removed = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Software Version Removal Procedure - Standardized process for identifying and removing outdated software versions
- [PROC-02] Firmware Update and Removal Procedure - Process for firmware updates including removal of previous versions
- [PROC-03] Version Inventory Management - Procedures for maintaining accurate inventory of software and firmware versions
- [PROC-04] Exception Management Process - Process for documenting and approving retention of previous versions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving outdated software, significant technology changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Software Update]
IF software_updated = TRUE
AND validation_complete = TRUE
AND days_since_update = 45
AND previous_version_present = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Critical Security Patch]
IF update_type = "critical_security"
AND validation_complete = TRUE
AND days_since_update = 10
AND previous_version_present = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Approved Exception]
IF previous_version_present = TRUE
AND days_since_update = 60
AND exception_documented = TRUE
AND exception_approved = TRUE
THEN compliance = TRUE

[SCENARIO-04: Mission Critical System]
IF system_criticality = "mission_critical"
AND previous_version_removed = TRUE
AND rollback_tested = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Automated Removal]
IF update_installed = TRUE
AND automatic_removal = TRUE
AND previous_version_present = FALSE
AND days_since_update = 1
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Previous versions of software and firmware components are defined | [RULE-03] |
| Previous versions are removed after updated versions are installed | [RULE-01], [RULE-02] |
| Removal activities are documented and tracked | [RULE-05] |
| Automated removal mechanisms are implemented where feasible | [RULE-04] |