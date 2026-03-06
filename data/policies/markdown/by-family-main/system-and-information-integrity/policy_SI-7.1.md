# POLICY: SI-7.1: Integrity Checks

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.1 |
| NIST Control | SI-7.1: Integrity Checks |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | integrity checks, startup verification, software integrity, firmware integrity, system boot, hash verification |

## 1. POLICY STATEMENT
All organization-defined software, firmware, and information SHALL undergo automated integrity verification during system startup to detect unauthorized modifications. Systems MUST NOT proceed with normal operations if integrity checks fail without explicit security approval.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All production servers and workstations |
| Development Systems | YES | Systems processing sensitive data |
| Network Infrastructure | YES | Routers, switches, firewalls |
| IoT/Embedded Devices | CONDITIONAL | If they support integrity checking |
| Test/Sandbox Systems | NO | Unless containing production data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure integrity checking mechanisms<br>• Monitor integrity check results<br>• Respond to integrity failures |
| Security Operations | • Define integrity check requirements<br>• Investigate integrity violations<br>• Maintain baseline integrity measurements |
| IT Operations | • Ensure integrity checks complete before system availability<br>• Document integrity check failures<br>• Coordinate system recovery procedures |

## 4. RULES
[RULE-01] All critical system software components MUST have integrity checks performed during system startup using cryptographic hash verification.
[VALIDATION] IF system_type = "critical" AND startup_integrity_check = FALSE THEN violation

[RULE-02] Firmware integrity checks SHALL be performed on all network infrastructure devices and security appliances at boot time.
[VALIDATION] IF device_type IN ["firewall", "router", "switch", "security_appliance"] AND firmware_integrity_check = FALSE THEN violation

[RULE-03] Systems MUST NOT enter operational state if integrity checks fail unless documented emergency override is approved by CISO or designated security authority.
[VALIDATION] IF integrity_check_status = "failed" AND operational_state = "active" AND emergency_override = FALSE THEN critical_violation

[RULE-04] Integrity check failures MUST be logged and reported to Security Operations Center within 15 minutes of detection.
[VALIDATION] IF integrity_failure_detected = TRUE AND soc_notification_time > 15_minutes THEN violation

[RULE-05] Baseline integrity measurements SHALL be updated within 24 hours after authorized software or firmware changes.
[VALIDATION] IF authorized_change_date + 24_hours < current_date AND baseline_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Integrity Baseline Management - Establish and maintain cryptographic baselines for software and firmware
- [PROC-02] Startup Integrity Verification - Automated integrity checking during system boot processes  
- [PROC-03] Integrity Failure Response - Investigation and remediation of integrity check failures
- [PROC-04] Emergency Override Process - Documented process for bypassing failed integrity checks

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system changes, security incidents involving integrity, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production Server Boot Failure]
IF system_type = "production"
AND integrity_check_status = "failed"
AND system_operational = TRUE
AND override_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Network Device Firmware Check]
IF device_type = "firewall"
AND firmware_integrity_check = "enabled"
AND check_performed_at_boot = TRUE
AND baseline_current = TRUE
THEN compliance = TRUE

[SCENARIO-03: Development System Exception]
IF system_type = "development"
AND contains_production_data = FALSE
AND integrity_check_disabled = TRUE
THEN compliance = TRUE

[SCENARIO-04: Delayed Failure Notification]
IF integrity_check_failed = TRUE
AND failure_detection_time = "09:00"
AND soc_notification_time = "09:20"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Outdated Baseline After Change]
IF authorized_software_change = "completed"
AND change_completion_date = "3_days_ago"
AND integrity_baseline_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Software integrity check defined and performed at startup | [RULE-01] |
| Firmware integrity check defined and performed at startup | [RULE-02] |
| Information integrity check defined and performed at startup | [RULE-01], [RULE-05] |
| Integrity verification controls operational | [RULE-03], [RULE-04] |