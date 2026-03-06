# POLICY: SI-7.1: Integrity Checks

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.1 |
| NIST Control | SI-7.1: Integrity Checks |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | integrity checks, startup verification, software integrity, firmware integrity, system boot, hash validation |

## 1. POLICY STATEMENT
All organizational systems MUST perform automated integrity verification of critical software, firmware, and information during system startup to detect unauthorized modifications. This policy ensures system components have not been compromised before becoming operational.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All customer-facing and business-critical systems |
| Development Systems | YES | Systems processing production data or code |
| Test/Staging Systems | YES | Systems with production data access |
| Desktop/Laptop Systems | CONDITIONAL | Systems with privileged access or sensitive data |
| IoT/Embedded Devices | YES | All network-connected operational devices |
| Virtual Machines | YES | All production and development VMs |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure integrity checking mechanisms<br>• Monitor integrity check results<br>• Respond to integrity failures |
| Security Operations Center | • Monitor integrity check alerts<br>• Investigate integrity violations<br>• Escalate critical integrity failures |
| DevOps Engineers | • Implement integrity checks in deployment pipelines<br>• Maintain baseline integrity measurements<br>• Update integrity baselines for approved changes |

## 4. RULES

[RULE-01] All systems MUST perform integrity checks on operating system boot files, kernel modules, and critical system binaries during startup.
[VALIDATION] IF system_startup = TRUE AND integrity_check_performed = FALSE THEN critical_violation

[RULE-02] Firmware integrity verification MUST be enabled on all systems supporting Secure Boot or equivalent technology.
[VALIDATION] IF secure_boot_capable = TRUE AND secure_boot_enabled = FALSE THEN violation

[RULE-03] Critical application software MUST have integrity verification performed before execution during system startup.
[VALIDATION] IF critical_application = TRUE AND startup_integrity_check = FALSE THEN violation

[RULE-04] Integrity check failures MUST prevent system startup and generate security alerts within 5 minutes.
[VALIDATION] IF integrity_check_result = "FAILED" AND system_started = TRUE THEN critical_violation

[RULE-05] Baseline integrity measurements MUST be updated within 24 hours of approved software or firmware changes.
[VALIDATION] IF approved_change_date < current_date AND baseline_update_date > (approved_change_date + 24_hours) THEN violation

[RULE-06] Systems MUST maintain cryptographic hashes or digital signatures for all components subject to integrity checking.
[VALIDATION] IF integrity_check_required = TRUE AND (hash_present = FALSE AND signature_present = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Integrity Baseline Management - Establish and maintain cryptographic baselines for system components
- [PROC-02] Integrity Failure Response - Define response procedures for integrity check failures
- [PROC-03] Secure Boot Configuration - Configure and maintain secure boot mechanisms
- [PROC-04] Integrity Monitoring - Monitor and report on integrity check status across systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving system integrity, major system updates, new system deployments

## 7. SCENARIO PATTERNS

[SCENARIO-01: Production Server Boot Integrity]
IF system_type = "production_server"
AND startup_event = TRUE
AND os_integrity_check = "PASSED"
AND firmware_integrity_check = "PASSED"
THEN compliance = TRUE

[SCENARIO-02: Failed Integrity Check at Startup]
IF system_startup = TRUE
AND integrity_check_result = "FAILED"
AND system_boot_prevented = TRUE
AND security_alert_generated = TRUE
THEN compliance = TRUE

[SCENARIO-03: Missing Integrity Baseline]
IF system_in_production = TRUE
AND integrity_checking_enabled = FALSE
AND baseline_hash_missing = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated Integrity Baseline After Change]
IF approved_software_change = TRUE
AND change_completion_date < (current_date - 2_days)
AND integrity_baseline_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Disabled Secure Boot on Capable System]
IF secure_boot_capable = TRUE
AND secure_boot_enabled = FALSE
AND business_justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Software integrity check performed at startup | RULE-01, RULE-03 |
| Firmware integrity check performed at startup | RULE-02 |
| Information integrity check performed at startup | RULE-06 |
| Integrity verification mechanisms configured | RULE-01, RULE-02, RULE-06 |
| Response to integrity check failures | RULE-04 |
| Maintenance of integrity baselines | RULE-05, RULE-06 |