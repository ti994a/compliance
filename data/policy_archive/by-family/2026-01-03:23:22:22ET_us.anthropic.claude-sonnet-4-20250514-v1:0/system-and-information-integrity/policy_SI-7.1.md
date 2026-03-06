# POLICY: SI-7.1: Integrity Checks

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.1 |
| NIST Control | SI-7.1: Integrity Checks |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | integrity, startup, software, firmware, information, verification, checksums, hashing |

## 1. POLICY STATEMENT
All organization-defined software, firmware, and information SHALL undergo automated integrity verification during system startup to detect unauthorized modifications. Integrity checks MUST use cryptographic mechanisms to validate the authenticity and integrity of critical system components before operational use.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing sensitive data |
| Development Systems | YES | Systems with access to production networks |
| Test Systems | CONDITIONAL | Only if containing production data |
| Personal Devices | CONDITIONAL | Only if domain-joined or accessing corporate resources |
| IoT Devices | YES | All network-connected operational technology |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure integrity checking tools<br>• Monitor integrity verification results<br>• Respond to integrity failures |
| Security Team | • Define integrity check requirements<br>• Maintain baseline integrity measurements<br>• Investigate integrity violations |
| System Owners | • Identify critical software/firmware for integrity checking<br>• Approve integrity check configurations<br>• Ensure business continuity during integrity failures |

## 4. RULES
[RULE-01] All systems MUST perform automated integrity checks on organization-defined software, firmware, and information during startup before becoming operational.
[VALIDATION] IF system_startup = TRUE AND integrity_check_performed = FALSE THEN critical_violation

[RULE-02] Integrity checks MUST use cryptographically secure hash algorithms (SHA-256 or stronger) and be compared against known-good baseline measurements.
[VALIDATION] IF hash_algorithm IN ["MD5", "SHA-1"] OR baseline_comparison = FALSE THEN violation

[RULE-03] Systems MUST NOT proceed to operational state if integrity checks fail, unless explicitly authorized emergency override is documented and approved.
[VALIDATION] IF integrity_check_result = "FAIL" AND operational_state = TRUE AND emergency_override = FALSE THEN critical_violation

[RULE-04] Integrity check failures MUST generate security alerts and be logged with timestamp, affected components, and failure details within 5 minutes.
[VALIDATION] IF integrity_failure = TRUE AND (alert_generated = FALSE OR log_created = FALSE OR response_time > 5_minutes) THEN violation

[RULE-05] Organization-defined critical software and firmware components MUST be identified and documented in system security plans with integrity check requirements.
[VALIDATION] IF component_criticality = "HIGH" AND (documented_in_ssp = FALSE OR integrity_required = FALSE) THEN violation

[RULE-06] Integrity baselines MUST be updated within 24 hours of authorized software or firmware changes and re-validated before deployment.
[VALIDATION] IF authorized_change = TRUE AND (baseline_updated = FALSE OR update_time > 24_hours) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Integrity Baseline Management - Establish and maintain cryptographic baselines for critical components
- [PROC-02] Startup Integrity Verification - Automated integrity checking during system initialization
- [PROC-03] Integrity Failure Response - Incident response procedures for integrity check failures
- [PROC-04] Emergency Override Process - Documented process for bypassing failed integrity checks

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving integrity violations, major system changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: Normal Startup with Passing Integrity]
IF system_startup = TRUE
AND integrity_check_performed = TRUE
AND integrity_result = "PASS"
THEN compliance = TRUE

[SCENARIO-02: Startup with Failed Integrity Check]
IF system_startup = TRUE
AND integrity_check_result = "FAIL"
AND system_operational = TRUE
AND emergency_override = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Integrity Check Configuration]
IF system_criticality = "HIGH"
AND integrity_check_configured = FALSE
AND startup_completed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Weak Hash Algorithm Usage]
IF integrity_check_enabled = TRUE
AND hash_algorithm IN ["MD5", "SHA-1"]
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Delayed Alert Generation]
IF integrity_failure = TRUE
AND alert_generated = TRUE
AND alert_delay > 5_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Integrity check of software is performed at startup | [RULE-01] |
| Integrity check of firmware is performed at startup | [RULE-01] |
| Integrity check of information is performed at startup | [RULE-01] |
| Organization-defined software for integrity checking is defined | [RULE-05] |
| Organization-defined firmware for integrity checking is defined | [RULE-05] |
| Organization-defined information for integrity checking is defined | [RULE-05] |