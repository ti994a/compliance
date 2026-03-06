# POLICY: MP-4.2: Automated Restricted Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-4.2 |
| NIST Control | MP-4.2: Automated Restricted Access |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | media storage, automated access control, biometric, keypad, card reader, access logging, storage areas |

## 1. POLICY STATEMENT
Access to media storage areas MUST be restricted using automated mechanisms and all access attempts and granted access MUST be logged. The organization SHALL implement keypads, biometric readers, card readers, or equivalent automated systems to control and monitor physical access to areas containing digital media storage.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Physical media storage areas | YES | All areas containing backup tapes, removable media, archives |
| Data center storage facilities | YES | Server rooms with removable storage devices |
| Offsite storage locations | YES | Third-party and company-owned remote facilities |
| Individual workstation storage | NO | Covered under separate endpoint controls |
| Cloud storage services | NO | Covered under logical access controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Define automated access control requirements<br>• Approve access control mechanisms<br>• Review access logs quarterly |
| Facilities Manager | • Install and maintain automated access systems<br>• Ensure proper functioning of logging mechanisms<br>• Coordinate access provisioning |
| IT Security Team | • Monitor access logs for anomalies<br>• Integrate access logs with SIEM systems<br>• Conduct access reviews |

## 4. RULES
[RULE-01] All media storage areas MUST be protected by automated access control mechanisms such as keypads, biometric readers, or card readers.
[VALIDATION] IF storage_area_type = "media_storage" AND automated_access_control = FALSE THEN critical_violation

[RULE-02] Automated access control systems MUST log all access attempts including successful and failed attempts with timestamp, user identity, and access method.
[VALIDATION] IF access_attempt_logged = FALSE OR timestamp_missing = TRUE OR user_identity_missing = TRUE THEN violation

[RULE-03] Access logs MUST be retained for minimum 90 days and protected from unauthorized modification.
[VALIDATION] IF log_retention_days < 90 OR log_integrity_protection = FALSE THEN violation

[RULE-04] Failed access attempts exceeding 3 consecutive attempts MUST trigger automated alerts to security personnel within 15 minutes.
[VALIDATION] IF failed_attempts >= 3 AND alert_sent = FALSE AND time_elapsed > 15_minutes THEN violation

[RULE-05] Automated access control systems MUST have backup power and fail-secure mechanisms to maintain security during power outages.
[VALIDATION] IF backup_power = FALSE OR fail_secure_mode = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Access Control System Installation - Standard deployment of automated mechanisms
- [PROC-02] Access Provisioning - Process for granting and revoking media storage access
- [PROC-03] Log Review and Analysis - Regular examination of access logs for anomalies
- [PROC-04] System Maintenance - Preventive maintenance of automated access systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, system failures, regulatory changes, facility modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unprotected Media Storage Area]
IF storage_area_contains_media = TRUE
AND automated_access_control = FALSE
AND manual_access_only = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Missing Access Logs]
IF access_granted = TRUE
AND access_logged = FALSE
AND automated_system_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Excessive Failed Access Attempts]
IF failed_access_attempts = 5
AND alert_generated = FALSE
AND time_since_first_attempt > 15_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Proper Automated Access Control]
IF automated_mechanism_type IN ["keypad", "biometric", "card_reader"]
AND access_attempts_logged = TRUE
AND access_granted_logged = TRUE
AND log_retention >= 90_days
THEN compliance = TRUE

[SCENARIO-05: System Failure Without Fail-Safe]
IF power_outage = TRUE
AND automated_system_failed = TRUE
AND fail_secure_activated = FALSE
AND unauthorized_access_possible = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Automated mechanisms restrict access to media storage areas | [RULE-01] |
| Access attempts to media storage areas are logged | [RULE-02] |
| Access granted to media storage areas is logged | [RULE-02] |
| Log retention and integrity | [RULE-03] |
| Automated alerting for security events | [RULE-04] |
| System reliability and fail-safe operation | [RULE-05] |