# POLICY: SI-7: Software, Firmware, and Information Integrity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7 |
| NIST Control | SI-7: Software, Firmware, and Information Integrity |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | integrity verification, unauthorized changes, software integrity, firmware integrity, cryptographic hashes, UEFI, BIOS |

## 1. POLICY STATEMENT
The organization must employ integrity verification tools to detect unauthorized changes to critical software, firmware, and information assets. When unauthorized changes are detected, predefined response actions must be executed immediately to maintain system security and data integrity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing business data |
| Development Systems | CONDITIONAL | Systems with access to production data |
| Operating Systems | YES | Including kernels, drivers, middleware |
| Firmware (UEFI/BIOS) | YES | All system firmware interfaces |
| Applications | YES | Business-critical and security applications |
| PII/Sensitive Data | YES | All regulated and classified information |
| Test/Sandbox Systems | NO | Isolated non-production environments |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Deploy and configure integrity verification tools<br>• Monitor integrity alerts and notifications<br>• Execute response procedures for detected changes |
| Security Operations Center | • Review integrity violation reports<br>• Escalate critical integrity failures<br>• Coordinate incident response activities |
| Asset Owners | • Define criticality levels for protected assets<br>• Approve baseline configurations<br>• Validate authorized changes |

## 4. RULES
[RULE-01] Integrity verification tools MUST be deployed on all in-scope systems to monitor software, firmware, and information for unauthorized changes.
[VALIDATION] IF system_in_scope = TRUE AND integrity_tool_deployed = FALSE THEN violation

[RULE-02] Cryptographic hash verification MUST be performed at minimum every 24 hours for critical assets and every 72 hours for standard assets.
[VALIDATION] IF asset_criticality = "critical" AND last_hash_check > 24_hours THEN violation
[VALIDATION] IF asset_criticality = "standard" AND last_hash_check > 72_hours THEN violation

[RULE-03] Automated response actions MUST be executed within 15 minutes of detecting unauthorized changes to critical systems.
[VALIDATION] IF change_detected = TRUE AND asset_criticality = "critical" AND response_time > 15_minutes THEN critical_violation

[RULE-04] All integrity verification failures MUST be logged and reported to the Security Operations Center within 30 minutes.
[VALIDATION] IF integrity_failure = TRUE AND soc_notification_time > 30_minutes THEN violation

[RULE-05] Firmware integrity checks MUST be performed during system boot and at minimum weekly during runtime.
[VALIDATION] IF firmware_boot_check = FALSE OR last_runtime_check > 7_days THEN violation

[RULE-06] Baseline integrity measurements MUST be updated within 24 hours of any approved software or firmware changes.
[VALIDATION] IF approved_change = TRUE AND baseline_update_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Integrity Tool Deployment - Installation and configuration of verification tools
- [PROC-02] Baseline Establishment - Creating and maintaining integrity baselines
- [PROC-03] Change Detection Response - Actions when unauthorized changes detected
- [PROC-04] False Positive Handling - Process for validating and dismissing false alerts
- [PROC-05] Firmware Integrity Verification - UEFI/BIOS monitoring procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, system architecture changes, new regulatory requirements

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical System File Modification]
IF file_type = "system_critical"
AND unauthorized_change_detected = TRUE
AND response_action_taken = FALSE
AND detection_time > 15_minutes
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Firmware Tampering Detection]
IF component_type = "firmware"
AND integrity_check_failed = TRUE
AND boot_process_blocked = TRUE
AND incident_logged = TRUE
THEN compliance = TRUE

[SCENARIO-03: Hash Verification Failure]
IF asset_criticality = "standard"
AND last_hash_verification > 72_hours
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Approved Change Without Baseline Update]
IF change_status = "approved"
AND change_implemented = TRUE
AND baseline_updated = FALSE
AND time_since_change > 24_hours
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: PII Data Integrity Violation]
IF data_type = "PII"
AND unauthorized_modification = TRUE
AND privacy_team_notified = FALSE
AND detection_time > 30_minutes
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Integrity verification tools employed for software | RULE-01, RULE-02 |
| Integrity verification tools employed for firmware | RULE-01, RULE-05 |
| Integrity verification tools employed for information | RULE-01, RULE-02 |
| Actions taken when unauthorized software changes detected | RULE-03, RULE-04 |
| Actions taken when unauthorized firmware changes detected | RULE-03, RULE-05 |
| Actions taken when unauthorized information changes detected | RULE-03, RULE-04 |
| Baseline maintenance for approved changes | RULE-06 |