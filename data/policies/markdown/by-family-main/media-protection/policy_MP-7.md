# POLICY: MP-7: Media Use

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-7 |
| NIST Control | MP-7: Media Use |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media protection, portable storage, removable devices, USB, external drives, media restrictions |

## 1. POLICY STATEMENT
This policy restricts and controls the use of system media types on organizational systems and components to prevent unauthorized data transfer and malware introduction. All portable storage devices must have identifiable owners and approved usage, with technical controls enforcing media restrictions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including workstations, servers, mobile devices |
| Contractor systems | YES | When processing organizational data |
| Personal devices (BYOD) | YES | When connected to organizational networks |
| Air-gapped systems | YES | Enhanced restrictions apply |
| Guest networks | CONDITIONAL | If media transfer capabilities exist |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve media restriction policies<br>• Define prohibited media types<br>• Oversee technical control implementation |
| IT Security Team | • Configure technical media controls<br>• Monitor media usage violations<br>• Maintain approved device registry |
| System Administrators | • Implement endpoint media restrictions<br>• Deploy device control software<br>• Report unauthorized media usage |
| End Users | • Comply with media usage restrictions<br>• Use only approved portable devices<br>• Report lost or stolen media devices |

## 4. RULES

[RULE-01] Organizations MUST define and document specific types of system media that are restricted or prohibited on organizational systems and components.
[VALIDATION] IF media_types_defined = FALSE OR documentation_exists = FALSE THEN violation

[RULE-02] Technical controls MUST be implemented to enforce media restrictions, including disabling USB ports, optical drives, or other removable media interfaces where prohibited.
[VALIDATION] IF technical_controls_implemented = FALSE AND media_restrictions_defined = TRUE THEN violation

[RULE-03] Portable storage devices SHALL NOT be used on organizational systems unless they have an identifiable owner documented in the approved device registry.
[VALIDATION] IF portable_device_used = TRUE AND (owner_identified = FALSE OR registry_entry = FALSE) THEN critical_violation

[RULE-04] Write capabilities to removable media MUST be disabled on systems processing sensitive data unless explicitly approved through exception process.
[VALIDATION] IF system_sensitivity_level >= "MODERATE" AND removable_write_enabled = TRUE AND exception_approved = FALSE THEN violation

[RULE-05] Media usage restrictions MUST be technically enforced through endpoint protection software, Group Policy, or hardware controls rather than relying solely on administrative controls.
[VALIDATION] IF enforcement_method = "administrative_only" AND technical_controls_available = TRUE THEN violation

[RULE-06] All approved portable storage devices MUST be encrypted and scanned for malware before use on organizational systems.
[VALIDATION] IF device_approved = TRUE AND (encryption_status = FALSE OR malware_scan_current = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Type Classification - Document and classify all media types as approved, restricted, or prohibited
- [PROC-02] Technical Control Implementation - Deploy and configure endpoint media restriction technologies
- [PROC-03] Device Registration Process - Register and approve portable storage devices with identifiable owners
- [PROC-04] Exception Management - Process requests for media usage exceptions with risk assessment
- [PROC-05] Violation Response - Investigate and respond to unauthorized media usage incidents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving removable media, new media technologies, changes to data classification

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unregistered USB Device]
IF device_type = "USB_storage"
AND owner_registered = FALSE
AND system_connection_attempted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Personal Device on Sensitive System]
IF device_ownership = "personal"
AND system_classification >= "MODERATE"
AND device_usage = TRUE
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Disabled Technical Controls]
IF media_restrictions_policy = "ACTIVE"
AND technical_enforcement = "DISABLED"
AND administrative_justification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Approved Encrypted Device]
IF device_registered = TRUE
AND owner_identified = TRUE
AND encryption_enabled = TRUE
AND malware_scan_current = TRUE
THEN compliance = TRUE

[SCENARIO-05: Write-Enabled Media on Sensitive System]
IF system_data_classification = "CONFIDENTIAL"
AND removable_media_write = "ENABLED"
AND business_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Define restricted media types | RULE-01 |
| Implement technical controls for media restrictions | RULE-02 |
| Prohibit unidentified portable storage devices | RULE-03 |
| Control write capabilities to removable media | RULE-04 |
| Enforce restrictions through technical means | RULE-05 |
| Ensure approved devices are secured | RULE-06 |