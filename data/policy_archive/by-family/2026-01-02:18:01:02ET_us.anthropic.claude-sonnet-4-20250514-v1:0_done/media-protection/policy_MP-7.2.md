# POLICY: MP-7.2: Prohibit Use of Sanitization-resistant Media

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-7.2 |
| NIST Control | MP-7.2: Prohibit Use of Sanitization-resistant Media |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | sanitization-resistant, media, USB, flash, solid state drives, data purging, media protection |

## 1. POLICY STATEMENT
The organization prohibits the use of sanitization-resistant media in all organizational systems to ensure complete data sanitization capabilities. All media used within organizational systems must support standardized sanitization commands and interfaces.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including production, development, and test environments |
| Employee workstations | YES | Corporate and remote devices |
| Contractor equipment | YES | When connected to organizational networks |
| Vendor systems | CONDITIONAL | Only when processing organizational data |
| Air-gapped systems | YES | All systems regardless of connectivity |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Asset Manager | • Maintain approved media inventory<br>• Validate sanitization capabilities before procurement<br>• Monitor compliance with media restrictions |
| System Administrators | • Implement technical controls to block prohibited media<br>• Report violations to security team<br>• Configure systems to prevent unauthorized media usage |
| Procurement Team | • Verify media sanitization capabilities before purchase<br>• Reject purchases of sanitization-resistant media<br>• Maintain vendor compliance documentation |

## 4. RULES
[RULE-01] Organizations MUST prohibit the use of compact flash, embedded flash on boards, solid state drives without standardized sanitization support, and USB removable media that cannot be properly sanitized.
[VALIDATION] IF media_type IN ["compact_flash", "embedded_flash", "non_sanitizable_ssd", "non_sanitizable_usb"] THEN violation

[RULE-02] All media used in organizational systems MUST support standardized sanitization commands through documented interfaces.
[VALIDATION] IF media_sanitization_support = FALSE OR sanitization_interface_documented = FALSE THEN violation

[RULE-03] Technical controls MUST be implemented to prevent connection of sanitization-resistant media to organizational systems.
[VALIDATION] IF technical_controls_implemented = FALSE AND sanitization_resistant_media_blocked = FALSE THEN violation

[RULE-04] Media procurement requests MUST include verification of sanitization capabilities before approval.
[VALIDATION] IF procurement_request = TRUE AND sanitization_verification = FALSE THEN violation

[RULE-05] Exceptions to sanitization-resistant media prohibition MUST be documented, approved by CISO, and reviewed annually.
[VALIDATION] IF sanitization_resistant_media_used = TRUE AND (exception_documented = FALSE OR ciso_approval = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Sanitization Verification - Process to validate media sanitization capabilities before deployment
- [PROC-02] Technical Control Implementation - Procedures for blocking sanitization-resistant media at system level
- [PROC-03] Exception Management - Process for documenting and approving sanitization-resistant media exceptions
- [PROC-04] Procurement Validation - Verification process for media sanitization support during purchasing

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New media technology introduction, sanitization standard updates, security incidents involving media

## 7. SCENARIO PATTERNS
[SCENARIO-01: USB Drive Connection]
IF device_type = "USB_removable_media"
AND sanitization_support = FALSE
AND technical_controls_active = TRUE
THEN compliance = TRUE (blocked)
violation_severity = N/A

[SCENARIO-02: SSD Procurement]
IF procurement_item = "solid_state_drive"
AND sanitization_verification = FALSE
AND purchase_approved = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Embedded Flash Usage]
IF media_type = "embedded_flash"
AND sanitization_resistant = TRUE
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Legacy System Exception]
IF system_type = "legacy_critical"
AND sanitization_resistant_media = TRUE
AND ciso_exception_approved = TRUE
AND annual_review_current = TRUE
THEN compliance = TRUE
violation_severity = N/A

[SCENARIO-05: Contractor Equipment]
IF user_type = "contractor"
AND device_contains_sanitization_resistant_media = TRUE
AND organizational_data_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Sanitization-resistant media is identified | [RULE-01], [RULE-02] |
| Use of sanitization-resistant media in organizational systems is prohibited | [RULE-01], [RULE-03], [RULE-05] |