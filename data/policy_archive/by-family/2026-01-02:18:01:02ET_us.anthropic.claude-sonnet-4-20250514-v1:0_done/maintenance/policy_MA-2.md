# POLICY: MA-2: Controlled Maintenance

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MA-2 |
| NIST Control | MA-2: Controlled Maintenance |
| Version | 1.0 |
| Owner | IT Operations Manager |
| Keywords | maintenance, repair, replacement, sanitization, approval, monitoring, documentation |

## 1. POLICY STATEMENT
All system maintenance, repair, and replacement activities must be scheduled, documented, approved, and monitored in accordance with organizational requirements and vendor specifications. Equipment removed for off-site maintenance must be properly sanitized and explicitly approved by designated personnel.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All production and non-production systems |
| System Components | YES | Servers, network devices, peripherals, storage |
| Cloud Infrastructure | YES | Hybrid cloud components under organizational control |
| Third-party Vendors | YES | When performing maintenance on organizational systems |
| Mobile Devices | YES | Company-owned devices containing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Operations Manager | • Approve maintenance schedules and procedures<br>• Oversee vendor maintenance activities<br>• Ensure compliance with maintenance policies |
| System Administrators | • Execute approved maintenance activities<br>• Document maintenance actions and results<br>• Verify system functionality post-maintenance |
| Information Security Officer | • Approve off-site maintenance requests<br>• Verify sanitization procedures<br>• Monitor security controls post-maintenance |
| Facilities Manager | • Escort external maintenance personnel<br>• Control physical access during maintenance<br>• Approve equipment removal from facilities |

## 4. RULES
[RULE-01] All maintenance activities MUST be scheduled and documented in accordance with manufacturer specifications and organizational requirements.
[VALIDATION] IF maintenance_scheduled = FALSE OR documentation_complete = FALSE THEN violation

[RULE-02] All maintenance activities MUST be approved by IT Operations Manager before execution.
[VALIDATION] IF maintenance_approval = FALSE AND maintenance_started = TRUE THEN violation

[RULE-03] Off-site maintenance or equipment removal MUST receive explicit approval from Information Security Officer and Facilities Manager.
[VALIDATION] IF equipment_location = "off-site" AND (security_approval = FALSE OR facilities_approval = FALSE) THEN critical_violation

[RULE-04] Equipment MUST be sanitized to remove all organizational data before off-site maintenance, repair, or replacement.
[VALIDATION] IF equipment_location = "off-site" AND sanitization_completed = FALSE THEN critical_violation

[RULE-05] All potentially impacted security controls MUST be verified as functioning properly within 24 hours following maintenance completion.
[VALIDATION] IF maintenance_complete = TRUE AND control_verification_time > 24_hours THEN violation

[RULE-06] Maintenance records MUST include date/time, description of work, personnel involved, escort information, and components removed/replaced.
[VALIDATION] IF maintenance_record_complete = FALSE OR required_fields_missing > 0 THEN violation

[RULE-07] External maintenance personnel MUST be escorted at all times when accessing organizational facilities.
[VALIDATION] IF personnel_type = "external" AND escort_present = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Maintenance Scheduling - Coordinate with vendors and internal teams for planned maintenance windows
- [PROC-02] Equipment Sanitization - Remove organizational data from media before off-site maintenance
- [PROC-03] Maintenance Documentation - Record all maintenance activities with required information fields
- [PROC-04] Post-Maintenance Verification - Test and verify security controls after maintenance completion
- [PROC-05] Vendor Escort Management - Provide appropriate supervision for external maintenance personnel

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents during maintenance, vendor changes, regulatory updates, system architecture changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Emergency Server Repair]
IF maintenance_type = "emergency"
AND approval_obtained = FALSE
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Routine Printer Maintenance]
IF equipment_type = "printer"
AND maintenance_scheduled = TRUE
AND documentation_complete = TRUE
AND escort_provided = TRUE
THEN compliance = TRUE

[SCENARIO-03: Off-site Storage Replacement]
IF equipment_type = "storage"
AND location = "off-site"
AND sanitization_verified = TRUE
AND security_approval = TRUE
AND facilities_approval = TRUE
THEN compliance = TRUE

[SCENARIO-04: Unescorted Vendor Access]
IF personnel_type = "vendor"
AND facility_access = TRUE
AND escort_present = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Missing Post-Maintenance Verification]
IF maintenance_complete = TRUE
AND days_since_completion > 1
AND control_verification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Maintenance scheduling and documentation | [RULE-01] |
| Maintenance activity approval | [RULE-02] |
| Off-site maintenance approval | [RULE-03] |
| Equipment sanitization | [RULE-04] |
| Post-maintenance control verification | [RULE-05] |
| Maintenance record completeness | [RULE-06] |
| External personnel escort | [RULE-07] |