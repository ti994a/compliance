```markdown
# POLICY: MA-3.2: Inspect Media

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MA-3.2 |
| NIST Control | MA-3.2: Inspect Media |
| Version | 1.0 |
| Owner | IT Security Manager |
| Keywords | media inspection, malicious code, diagnostic programs, test programs, maintenance media |

## 1. POLICY STATEMENT
All media containing diagnostic and test programs MUST be inspected for malicious code before use in organizational systems. Any malicious code detected SHALL be handled according to incident response procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Diagnostic media | YES | All media with diagnostic programs |
| Test program media | YES | All media with test programs |
| Maintenance media | YES | All media used for system maintenance |
| Production systems | YES | Systems where media will be used |
| Cloud environments | YES | Including hybrid cloud infrastructure |
| Third-party media | YES | Media from vendors and contractors |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Perform malicious code scanning<br>• Maintain inspection tools<br>• Document inspection results |
| System Administrators | • Submit media for inspection<br>• Ensure no uninspected media is used<br>• Report suspected malicious code |
| Maintenance Personnel | • Request media inspection before use<br>• Follow approved media handling procedures |

## 4. RULES
[RULE-01] All media containing diagnostic and test programs MUST be scanned for malicious code using approved security tools before system use.
[VALIDATION] IF media_type IN ["diagnostic", "test", "maintenance"] AND malware_scan_status != "completed" AND system_use = TRUE THEN violation

[RULE-02] Media inspection MUST be completed within 4 hours of submission for routine maintenance and within 1 hour for emergency maintenance.
[VALIDATION] IF maintenance_priority = "routine" AND inspection_time > 4_hours THEN violation
[VALIDATION] IF maintenance_priority = "emergency" AND inspection_time > 1_hour THEN violation

[RULE-03] Media found to contain malicious code MUST be quarantined immediately and reported as a security incident within 2 hours.
[VALIDATION] IF malicious_code_detected = TRUE AND quarantine_status != "active" THEN critical_violation
[VALIDATION] IF malicious_code_detected = TRUE AND incident_reported_time > 2_hours THEN violation

[RULE-04] Only approved anti-malware tools with current signatures SHALL be used for media inspection.
[VALIDATION] IF scanning_tool NOT IN approved_tools_list OR signature_age > 24_hours THEN violation

[RULE-05] All media inspection activities MUST be logged with timestamp, inspector ID, scan results, and approval status.
[VALIDATION] IF media_inspection_log.required_fields.missing > 0 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Inspection Process - Standard procedure for scanning diagnostic and test media
- [PROC-02] Malicious Code Response - Incident handling for infected media detection
- [PROC-03] Emergency Media Approval - Expedited process for critical maintenance scenarios
- [PROC-04] Third-party Media Validation - Additional requirements for vendor-provided media

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving media, new malware detection tools, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Media Inspection]
IF media_contains = "diagnostic_programs"
AND malware_scan_completed = TRUE
AND scan_results = "clean"
AND approval_documented = TRUE
THEN compliance = TRUE

[SCENARIO-02: Uninspected Media Usage]
IF media_type = "test_programs"
AND system_usage = TRUE
AND inspection_status = "pending"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Infected Media Detection]
IF malicious_code_detected = TRUE
AND quarantine_time <= 15_minutes
AND incident_reported = TRUE
AND incident_report_time <= 2_hours
THEN compliance = TRUE

[SCENARIO-04: Emergency Maintenance Delay]
IF maintenance_priority = "emergency"
AND inspection_completion_time > 1_hour
AND system_downtime_impact = "critical"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Outdated Scanning Tools]
IF antimalware_signature_age > 24_hours
AND media_scan_performed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Media containing diagnostic and test programs are checked for malicious code before system use | [RULE-01] |
| Inspection process uses current malware detection capabilities | [RULE-04] |
| Infected media handling follows incident response procedures | [RULE-03] |
| Inspection activities are properly documented | [RULE-05] |
| Timely completion of media inspection process | [RULE-02] |
```