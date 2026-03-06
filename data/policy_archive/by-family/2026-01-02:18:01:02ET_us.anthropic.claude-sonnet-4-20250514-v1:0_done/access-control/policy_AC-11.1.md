# POLICY: AC-11.1: Pattern-hiding Displays

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-11.1 |
| NIST Control | AC-11.1: Pattern-hiding Displays |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | device lock, screen saver, display concealment, session lock, publicly viewable |

## 1. POLICY STATEMENT
All organizational devices MUST conceal previously visible information on displays through device locks that show only publicly viewable images. This control prevents unauthorized disclosure of sensitive information when devices are locked or unattended.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Corporate workstations | YES | All desktop and laptop computers |
| Mobile devices | YES | Smartphones, tablets with organizational data |
| Kiosks and shared terminals | YES | Public-facing and shared access systems |
| Server consoles | YES | Physical server management interfaces |
| Personal devices (BYOD) | CONDITIONAL | Only when accessing organizational data |
| Display-only devices | NO | Digital signage without sensitive data access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Configure pattern-hiding display policies<br>• Monitor compliance with display concealment requirements<br>• Approve publicly viewable image content |
| System Administrators | • Implement device lock configurations<br>• Deploy approved screen saver and lock screen images<br>• Ensure automatic lock activation settings |
| End Users | • Activate device locks when stepping away<br>• Report malfunctioning lock screen mechanisms<br>• Comply with manual lock requirements |

## 4. RULES
[RULE-01] Device locks MUST conceal all previously visible information by displaying only publicly viewable images such as screen savers, solid colors, clock displays, or blank screens.
[VALIDATION] IF device_locked = TRUE AND sensitive_info_visible = TRUE THEN critical_violation

[RULE-02] Publicly viewable images MUST NOT contain any controlled unclassified information, sensitive data, or proprietary content.
[VALIDATION] IF lock_screen_content CONTAINS sensitive_data THEN violation

[RULE-03] Pattern-hiding displays MUST activate automatically when the device lock engages, with no user intervention required.
[VALIDATION] IF device_locked = TRUE AND pattern_hiding_active = FALSE THEN violation

[RULE-04] Organizations MUST maintain an approved list of publicly viewable images and patterns for use in device locks.
[VALIDATION] IF lock_screen_image NOT IN approved_image_list THEN violation

[RULE-05] Device lock mechanisms MUST prevent bypass of pattern-hiding display functionality through technical controls.
[VALIDATION] IF pattern_hiding_bypassable = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Device Lock Configuration - Standardized setup of automatic lock and pattern-hiding features
- [PROC-02] Approved Image Management - Process for reviewing and approving publicly viewable display content
- [PROC-03] Lock Screen Compliance Testing - Regular verification that sensitive information is properly concealed
- [PROC-04] Exception Handling - Process for devices that cannot support standard pattern-hiding displays

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving display exposure, new device types, technology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Laptop with Visible Email]
IF device_type = "laptop"
AND device_locked = TRUE
AND email_content_visible = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Workstation with Approved Screen Saver]
IF device_locked = TRUE
AND display_shows = "approved_screensaver"
AND previous_content_concealed = TRUE
THEN compliance = TRUE

[SCENARIO-03: Mobile Device with Company Logo]
IF device_type = "mobile"
AND lock_screen_image = "company_logo"
AND logo_contains_sensitive_data = FALSE
AND previous_screen_hidden = TRUE
THEN compliance = TRUE

[SCENARIO-04: Kiosk with Blank Screen Override]
IF device_type = "kiosk"
AND pattern_hiding_disabled = TRUE
AND user_role = "standard_user"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: BYOD Device Accessing Corporate Email]
IF device_ownership = "personal"
AND accessing_corporate_data = TRUE
AND pattern_hiding_configured = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information previously visible on display is concealed via device lock with publicly viewable image | [RULE-01], [RULE-03] |
| Publicly viewable images do not contain controlled information | [RULE-02], [RULE-04] |
| Pattern-hiding mechanism cannot be bypassed | [RULE-05] |