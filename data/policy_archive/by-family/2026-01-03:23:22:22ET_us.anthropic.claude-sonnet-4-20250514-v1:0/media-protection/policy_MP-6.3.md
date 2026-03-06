# POLICY: MP-6.3: Nondestructive Techniques

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-6.3 |
| NIST Control | MP-6.3: Nondestructive Techniques |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | portable storage, sanitization, nondestructive, USB devices, malware prevention |

## 1. POLICY STATEMENT
All portable storage devices MUST undergo nondestructive sanitization using approved techniques before connection to organizational systems under defined circumstances. This policy ensures malicious code cannot be introduced through removable media while preserving device functionality.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External hard drives | YES | SSD, magnetic, all capacities |
| USB flash drives | YES | All flash memory devices |
| Optical media | YES | CDs, DVDs, Blu-ray discs |
| Memory cards | YES | SD, microSD, CF cards |
| Mobile devices | CONDITIONAL | Only when used as storage |
| Internal drives | NO | Covered by other controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Define sanitization circumstances<br>• Maintain approved sanitization tools<br>• Monitor compliance |
| System Administrators | • Execute sanitization procedures<br>• Document sanitization activities<br>• Report sanitization failures |
| End Users | • Submit devices for sanitization<br>• Comply with connection restrictions<br>• Report suspicious device behavior |

## 4. RULES
[RULE-01] Portable storage devices MUST undergo nondestructive sanitization before initial connection when purchased from external vendors or when chain of custody cannot be verified.
[VALIDATION] IF device_source = "external_vendor" OR chain_of_custody = "unverified" AND sanitization_completed = FALSE THEN violation

[RULE-02] Sanitization procedures MUST use organization-approved nondestructive techniques that preserve device functionality while removing potential malicious code.
[VALIDATION] IF sanitization_method NOT IN approved_techniques_list THEN violation

[RULE-03] All sanitization activities MUST be documented with device identifier, sanitization method, date, and responsible personnel within 24 hours.
[VALIDATION] IF sanitization_completed = TRUE AND documentation_time > 24_hours THEN violation

[RULE-04] Devices SHALL NOT be connected to organizational systems until sanitization is completed and documented for circumstances requiring sanitization.
[VALIDATION] IF requires_sanitization = TRUE AND (sanitization_status ≠ "completed" OR documentation_status ≠ "complete") AND system_connection = TRUE THEN critical_violation

[RULE-05] Sanitization failure or detection of malicious code MUST trigger immediate quarantine and incident response procedures.
[VALIDATION] IF sanitization_result = "failed" OR malware_detected = TRUE AND quarantine_initiated = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Device Intake Assessment - Evaluate device source and custody history
- [PROC-02] Nondestructive Sanitization Execution - Apply approved sanitization techniques
- [PROC-03] Sanitization Documentation - Record all sanitization activities and results
- [PROC-04] Device Quarantine - Isolate devices with sanitization failures or malware

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New device types, sanitization tool updates, security incidents involving portable media

## 7. SCENARIO PATTERNS
[SCENARIO-01: New USB Drive from Vendor]
IF device_type = "USB_drive"
AND source = "external_vendor" 
AND sanitization_completed = FALSE
AND connection_attempted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Employee Personal Device]
IF device_ownership = "personal"
AND chain_of_custody = "unverified"
AND sanitization_completed = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-03: Internal Device Transfer]
IF device_source = "internal_transfer"
AND chain_of_custody = "verified"
AND sanitization_required = FALSE
THEN compliance = TRUE

[SCENARIO-04: Sanitization Documentation Delay]
IF sanitization_completed = TRUE
AND documentation_delay > 24_hours
AND system_connection = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Malware Detection During Sanitization]
IF sanitization_status = "in_progress"
AND malware_detected = TRUE
AND quarantine_initiated = TRUE
AND incident_response_triggered = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Nondestructive sanitization applied under defined circumstances | [RULE-01] |
| Use of approved sanitization techniques | [RULE-02] |
| Documentation of sanitization activities | [RULE-03] |
| Prevention of unauthorized device connections | [RULE-04] |
| Response to sanitization failures | [RULE-05] |