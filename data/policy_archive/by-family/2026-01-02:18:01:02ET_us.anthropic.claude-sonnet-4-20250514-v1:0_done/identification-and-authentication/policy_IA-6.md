# POLICY: IA-6: Authentication Feedback

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-6 |
| NIST Control | IA-6: Authentication Feedback |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authentication, feedback, obscure, shoulder surfing, password display, security |

## 1. POLICY STATEMENT
All systems MUST obscure authentication feedback during the authentication process to prevent unauthorized individuals from observing and exploiting authentication information. The level of obscuring SHALL be appropriate to the system type and threat environment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including desktops, servers, mobile devices, web applications |
| Authentication interfaces | YES | Login screens, password prompts, biometric readers |
| Third-party applications | YES | When integrated with organizational authentication |
| Guest networks | YES | All authentication points require feedback obscuring |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure authentication feedback obscuring on all systems<br>• Verify proper implementation during system updates<br>• Monitor compliance through regular audits |
| Application Developers | • Implement appropriate feedback obscuring in custom applications<br>• Follow secure coding standards for authentication interfaces<br>• Test obscuring functionality before deployment |
| Security Team | • Define obscuring requirements based on threat assessment<br>• Review and approve authentication interface designs<br>• Conduct periodic compliance assessments |

## 4. RULES
[RULE-01] All password input fields MUST display asterisks, dots, or similar obscuring characters instead of plaintext passwords.
[VALIDATION] IF password_field_type = "text" AND display_mode = "plaintext" THEN critical_violation

[RULE-02] Temporary display of authentication characters SHALL NOT exceed 2 seconds on any system type.
[VALIDATION] IF character_display_time > 2_seconds THEN violation

[RULE-03] Systems with large displays (>10 inches) MUST implement complete character obscuring with no temporary plaintext display.
[VALIDATION] IF screen_size > 10_inches AND temporary_display = TRUE THEN violation

[RULE-04] Mobile devices with small displays (<6 inches) MAY show individual characters for maximum 1 second before obscuring.
[VALIDATION] IF screen_size < 6_inches AND character_display_time > 1_second THEN violation

[RULE-05] Biometric authentication feedback MUST NOT display detailed matching information or templates to users.
[VALIDATION] IF authentication_type = "biometric" AND detailed_feedback = TRUE THEN violation

[RULE-06] Authentication error messages MUST NOT reveal whether username or password was incorrect.
[VALIDATION] IF error_message CONTAINS "invalid username" OR error_message CONTAINS "invalid password" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Authentication Interface Assessment - Annual review of all authentication interfaces for proper feedback obscuring
- [PROC-02] System Configuration Verification - Quarterly validation of obscuring settings on all systems
- [PROC-03] Application Security Testing - Security testing of authentication feedback during development lifecycle
- [PROC-04] Incident Response for Authentication Exposure - Process for handling reported authentication information exposure

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving authentication exposure, new system deployments, major system updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Desktop Password Entry]
IF system_type = "desktop"
AND screen_size > 10_inches
AND password_obscuring = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Mobile App Authentication]
IF system_type = "mobile_device"
AND screen_size < 6_inches
AND character_display_time = 0.5_seconds
AND subsequent_obscuring = TRUE
THEN compliance = TRUE

[SCENARIO-03: Web Application Login]
IF application_type = "web"
AND password_field_shows_asterisks = TRUE
AND error_message = "Invalid credentials"
THEN compliance = TRUE

[SCENARIO-04: Biometric Reader Feedback]
IF authentication_method = "fingerprint"
AND display_shows_match_details = TRUE
AND template_information_visible = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Kiosk Authentication]
IF system_type = "public_kiosk"
AND password_characters_visible = TRUE
AND temporary_display_time > 0_seconds
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authentication information feedback is obscured during authentication process | RULE-01, RULE-02, RULE-03 |
| Protection from exploitation by unauthorized individuals | RULE-04, RULE-05, RULE-06 |
| Appropriate obscuring method selection based on system type | RULE-03, RULE-04 |