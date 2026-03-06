# POLICY: MP-4.2: Automated Restricted Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-4.2 |
| NIST Control | MP-4.2: Automated Restricted Access |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media storage, automated access control, biometric, keypad, card reader, access logging, audit trail |

## 1. POLICY STATEMENT
All media storage areas MUST implement automated access control mechanisms to restrict physical entry and log all access attempts and granted access. Automated logging of access events is required to maintain accountability and support audit requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Physical media storage areas | YES | All areas storing digital media, backup tapes, removable storage |
| Data centers | YES | Areas containing storage infrastructure |
| Server rooms | YES | Rooms with storage media or backup systems |
| Archive facilities | YES | Long-term media storage locations |
| Temporary storage areas | CONDITIONAL | If storing media >24 hours |
| Individual workstations | NO | Covered under endpoint security policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Deploy and maintain automated access control systems<br>• Monitor access logs and investigate anomalies<br>• Ensure backup power for access control systems |
| IT Security Team | • Define authorized personnel lists<br>• Review access logs quarterly<br>• Integrate with SIEM systems |
| Media Custodians | • Maintain current access authorization lists<br>• Report access control system failures<br>• Conduct periodic access reviews |

## 4. RULES
[RULE-01] All media storage areas MUST implement automated access control mechanisms including keypads, biometric readers, or card readers.
[VALIDATION] IF media_storage_area = TRUE AND automated_access_control = FALSE THEN critical_violation

[RULE-02] Automated access control systems MUST log all access attempts including successful and failed attempts with timestamp, user identity, and location.
[VALIDATION] IF access_attempt_logged = FALSE OR timestamp_missing = TRUE OR user_identity_missing = TRUE THEN violation

[RULE-03] Access logs MUST be retained for minimum 90 days and integrated with centralized logging systems within 24 hours.
[VALIDATION] IF log_retention_days < 90 OR centralized_integration_time > 24_hours THEN violation

[RULE-04] Automated access control systems MUST have backup power capability to maintain operation during power outages.
[VALIDATION] IF backup_power_available = FALSE OR backup_power_test_failed = TRUE THEN violation

[RULE-05] Access authorization lists MUST be reviewed and updated within 30 days of personnel changes affecting media access privileges.
[VALIDATION] IF personnel_change_date + 30_days < current_date AND authorization_list_updated = FALSE THEN violation

[RULE-06] Failed access attempts exceeding 3 consecutive attempts MUST trigger automated security alerts within 15 minutes.
[VALIDATION] IF consecutive_failed_attempts >= 3 AND alert_triggered = FALSE THEN violation
[VALIDATION] IF consecutive_failed_attempts >= 3 AND alert_time > 15_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Automated Access Control Deployment - Installation and configuration of access control systems
- [PROC-02] Access Log Monitoring - Daily review and analysis of access logs
- [PROC-03] Access Authorization Management - Process for granting, modifying, and revoking access
- [PROC-04] System Maintenance - Regular testing and maintenance of automated systems
- [PROC-05] Incident Response - Response to access control failures or security events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents involving media storage, system failures, regulatory changes, facility modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Media Access]
IF user_type = "contractor"
AND media_storage_access_required = TRUE
AND automated_access_control_bypassed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Failed Access Logging]
IF access_attempt = TRUE
AND logging_system_operational = TRUE
AND access_event_logged = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Emergency Access Override]
IF emergency_declared = TRUE
AND manual_override_used = TRUE
AND override_documented = TRUE
AND security_personnel_notified = TRUE
THEN compliance = TRUE

[SCENARIO-04: System Maintenance Window]
IF maintenance_scheduled = TRUE
AND access_control_disabled = TRUE
AND alternative_security_measures = TRUE
AND duration <= 4_hours
THEN compliance = TRUE

[SCENARIO-05: Terminated Employee Access]
IF employee_status = "terminated"
AND termination_date + 1_day < current_date
AND media_storage_access_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Automated mechanisms restrict access to media storage areas | [RULE-01] |
| Access attempts to media storage areas are logged using automated mechanisms | [RULE-02] |
| Access granted to media storage areas is logged using automated mechanisms | [RULE-02] |
| Automated mechanisms for restricting access are defined | [RULE-01] |
| Automated mechanisms for logging access attempts are defined | [RULE-02] |
| Automated mechanisms for logging access granted are defined | [RULE-02] |