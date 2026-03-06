# POLICY: MP-7.2: Prohibit Use of Sanitization-resistant Media

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-7.2 |
| NIST Control | MP-7.2: Prohibit Use of Sanitization-resistant Media |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | sanitization-resistant media, compact flash, embedded flash, solid state drives, USB removable media, media protection |

## 1. POLICY STATEMENT
The organization SHALL prohibit the use of sanitization-resistant media in all organizational systems to ensure complete data sanitization capabilities. All media types that do not support standardized sanitization commands or interfaces are prohibited from use in organizational systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Includes production, development, and test environments |
| Third-party contractor systems | YES | When processing organizational data |
| Personal devices (BYOD) | YES | When connected to organizational networks |
| Backup and archive systems | YES | All data storage components |
| IoT and embedded devices | YES | Devices with storage capabilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve sanitization-resistant media policy exceptions<br>• Oversee policy compliance monitoring<br>• Review and approve alternative media types |
| IT Security Manager | • Maintain approved media inventory<br>• Conduct regular compliance assessments<br>• Coordinate with procurement for media validation |
| System Administrators | • Implement technical controls to prevent prohibited media use<br>• Monitor systems for unauthorized media connections<br>• Report policy violations immediately |
| Procurement Team | • Validate media sanitization capabilities before purchase<br>• Maintain vendor compliance documentation<br>• Reject purchases of sanitization-resistant media |

## 4. RULES
[RULE-01] Organizations MUST prohibit the use of compact flash, embedded flash on boards and devices, solid state drives without standardized sanitization support, and USB removable media that cannot be properly sanitized.
[VALIDATION] IF media_type IN ["compact_flash", "embedded_flash", "non_sanitizable_ssd", "non_sanitizable_usb"] AND system_connection = TRUE THEN violation

[RULE-02] All media devices MUST support standardized sanitization commands and interfaces before being approved for organizational use.
[VALIDATION] IF media_sanitization_support = FALSE AND approval_status = "approved" THEN critical_violation

[RULE-03] Technical controls MUST be implemented to automatically detect and block connection of sanitization-resistant media to organizational systems.
[VALIDATION] IF sanitization_resistant_media_detected = TRUE AND blocking_control_active = FALSE THEN violation

[RULE-04] Media procurement requests MUST include sanitization capability verification before purchase approval.
[VALIDATION] IF procurement_request = TRUE AND sanitization_verification = FALSE THEN violation

[RULE-05] Existing sanitization-resistant media MUST be removed from organizational systems within 30 days of policy implementation.
[VALIDATION] IF policy_effective_date + 30_days < current_date AND sanitization_resistant_media_present = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Sanitization Capability Assessment - Evaluate and document sanitization support for all media types
- [PROC-02] Sanitization-Resistant Media Identification - Maintain inventory of prohibited media types and detection methods
- [PROC-03] Technical Control Implementation - Deploy automated blocking mechanisms for prohibited media
- [PROC-04] Procurement Validation Process - Verify sanitization capabilities before media purchase approval

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New media technology introductions, sanitization standard updates, security incidents involving media sanitization failures

## 7. SCENARIO PATTERNS
[SCENARIO-01: USB Drive Connection]
IF device_type = "USB_removable_media"
AND sanitization_support = FALSE
AND system_connection_attempted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: SSD Procurement]
IF procurement_item = "solid_state_drive"
AND sanitization_verification = "not_performed"
AND purchase_approved = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Embedded Flash System]
IF system_component = "embedded_flash_device"
AND sanitization_capability = "none"
AND deployment_status = "active"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Legacy Media Removal]
IF media_type = "sanitization_resistant"
AND policy_effective_date + 30_days < current_date
AND removal_status = "pending"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Technical Control Bypass]
IF sanitization_resistant_media = "detected"
AND blocking_control = "disabled"
AND connection_successful = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Sanitization-resistant media is identified | [RULE-01], [RULE-02] |
| Use of sanitization-resistant media in organizational systems is prohibited | [RULE-01], [RULE-03], [RULE-05] |