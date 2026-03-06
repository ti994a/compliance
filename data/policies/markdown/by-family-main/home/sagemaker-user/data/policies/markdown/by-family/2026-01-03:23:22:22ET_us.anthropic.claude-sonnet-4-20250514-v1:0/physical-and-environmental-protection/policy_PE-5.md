# POLICY: PE-5: Access Control for Output Devices

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-5 |
| NIST Control | PE-5: Access Control for Output Devices |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | physical access, output devices, printers, monitors, unauthorized access |

## 1. POLICY STATEMENT
The organization SHALL control physical access to output from designated output devices to prevent unauthorized individuals from obtaining sensitive information. All output devices processing confidential, restricted, or regulated data MUST be subject to appropriate physical access controls based on data classification.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Printers (network/local) | YES | All printers processing confidential+ data |
| Monitors/Displays | YES | Public areas and shared workspaces |
| Copiers/Scanners | YES | All multifunction devices |
| Audio Output Devices | CONDITIONAL | When processing sensitive audio data |
| Facsimile Machines | YES | All fax machines in organization |
| Mobile Devices | CONDITIONAL | When used as output devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Implement physical security controls for output device areas<br>• Maintain access control systems for secured printer rooms<br>• Monitor compliance with location requirements |
| IT Security Manager | • Define output devices requiring access controls<br>• Classify data sensitivity levels<br>• Audit output device security configurations |
| Department Managers | • Ensure staff compliance with output device policies<br>• Report security incidents involving output devices<br>• Approve access requests for secured output areas |

## 4. RULES
[RULE-01] Output devices processing confidential, restricted, or regulated data MUST be placed in physically secured areas with access controls (locked rooms, card readers, or keypads).
[VALIDATION] IF device_data_classification IN ["confidential", "restricted", "regulated"] AND physical_security_controls = FALSE THEN violation

[RULE-02] Printers in open areas MUST NOT be used for printing confidential, restricted, or regulated information.
[VALIDATION] IF printer_location = "open_area" AND print_job_classification IN ["confidential", "restricted", "regulated"] THEN violation

[RULE-03] Monitors displaying sensitive information in public or shared areas MUST use privacy screens or be positioned to prevent unauthorized viewing.
[VALIDATION] IF monitor_location IN ["public", "shared"] AND sensitive_data_displayed = TRUE AND privacy_protection = FALSE THEN violation

[RULE-04] Access to secured output device areas SHALL be limited to authorized personnel with documented business need and current access approval.
[VALIDATION] IF area_access_granted = TRUE AND (authorization_current = FALSE OR business_need_documented = FALSE) THEN violation

[RULE-05] Output retrieval from secured devices MUST occur within 30 minutes of job completion, or jobs SHALL be automatically purged.
[VALIDATION] IF output_retrieval_time > 30_minutes AND auto_purge_enabled = FALSE THEN violation

[RULE-06] All access to secured output device areas MUST be logged and retained for minimum 90 days.
[VALIDATION] IF secured_area_access = TRUE AND (access_logged = FALSE OR log_retention < 90_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Output Device Risk Assessment - Annual assessment of all output devices and required controls
- [PROC-02] Secured Printer Room Access Management - Process for granting, reviewing, and revoking access
- [PROC-03] Output Device Incident Response - Procedures for responding to unauthorized access incidents
- [PROC-04] Output Job Monitoring - Process for monitoring and purging abandoned print jobs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents, new output devices, facility changes, data classification updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Confidential Printing in Open Area]
IF print_job_classification = "confidential"
AND printer_location = "open_area"
AND override_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unattended Output in Secured Area]
IF output_completion_time > 30_minutes_ago
AND output_retrieved = FALSE
AND auto_purge_enabled = TRUE
THEN compliance = TRUE

[SCENARIO-03: Unauthorized Access to Printer Room]
IF user_accessed_secured_area = TRUE
AND user_authorization_status = "expired"
AND access_logged = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Public Monitor with Privacy Screen]
IF monitor_location = "public_area"
AND sensitive_data_displayed = TRUE
AND privacy_screen_installed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Contractor Fax Access]
IF user_type = "contractor"
AND device_type = "facsimile"
AND business_need_documented = TRUE
AND access_approval_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical access to output devices is controlled | [RULE-01], [RULE-04] |
| Unauthorized individuals prevented from obtaining output | [RULE-02], [RULE-03], [RULE-05] |
| Output devices requiring controls are defined | [RULE-01] |
| Access monitoring and logging implemented | [RULE-06] |