# POLICY: SC-18.4: Prevent Automatic Execution

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-18.4 |
| NIST Control | SC-18.4: Prevent Automatic Execution |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mobile code, automatic execution, email attachments, web links, portable storage, USB devices |

## 1. POLICY STATEMENT
The organization SHALL prevent automatic execution of mobile code in designated software applications and enforce specific actions before any mobile code execution. All systems MUST implement controls to prompt users and validate mobile code before execution to prevent unauthorized or malicious code from running automatically.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Email systems | YES | All email clients and servers |
| Web browsers | YES | All corporate and BYOD browsers |
| Portable storage devices | YES | USB, CD, DVD, external drives |
| Software applications | CONDITIONAL | Applications designated by security team |
| Mobile devices | YES | Corporate and BYOD devices accessing corporate resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define software applications requiring mobile code prevention<br>• Approve mobile code execution policies<br>• Review and update prevention controls |
| IT Security Team | • Configure automatic execution prevention controls<br>• Monitor mobile code execution attempts<br>• Maintain list of approved/blocked mobile code types |
| System Administrators | • Implement prevention mechanisms on systems<br>• Configure user prompting for mobile code<br>• Disable auto-execute features on portable storage |
| End Users | • Respond to mobile code execution prompts<br>• Report suspicious mobile code attempts<br>• Comply with mobile code handling procedures |

## 4. RULES
[RULE-01] Automatic execution of mobile code MUST be prevented in all software applications designated by the security team.
[VALIDATION] IF application_in_scope = TRUE AND auto_execution_disabled = FALSE THEN violation

[RULE-02] Systems MUST prompt users before opening email attachments containing mobile code.
[VALIDATION] IF attachment_contains_mobile_code = TRUE AND user_prompted = FALSE THEN violation

[RULE-03] Systems MUST prompt users before executing mobile code from web links or downloads.
[VALIDATION] IF web_content_contains_mobile_code = TRUE AND user_prompted = FALSE THEN violation

[RULE-04] Auto-execute features MUST be disabled on all portable storage devices (USB, CD, DVD).
[VALIDATION] IF portable_device_connected = TRUE AND autorun_enabled = TRUE THEN violation

[RULE-05] Mobile code execution SHALL NOT proceed without explicit user confirmation and validation.
[VALIDATION] IF mobile_code_executed = TRUE AND user_confirmation = FALSE THEN critical_violation

[RULE-06] Systems MUST maintain logs of all mobile code execution attempts and user responses.
[VALIDATION] IF mobile_code_attempt_logged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Mobile Code Risk Assessment - Evaluate and categorize mobile code types by risk level
- [PROC-02] User Prompting Configuration - Implement and maintain user confirmation mechanisms
- [PROC-03] Portable Device Control - Configure and monitor auto-execute prevention on removable media
- [PROC-04] Mobile Code Monitoring - Log and analyze mobile code execution attempts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving mobile code, new software deployments, changes to email/web systems

## 7. SCENARIO PATTERNS
[SCENARIO-01: Email Attachment Auto-Execution]
IF email_attachment_received = TRUE
AND attachment_contains_mobile_code = TRUE
AND auto_execution_prevented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: USB Auto-Run Disabled]
IF usb_device_inserted = TRUE
AND autorun_feature_enabled = FALSE
AND user_prompted_for_action = TRUE
THEN compliance = TRUE

[SCENARIO-03: Web Download Without Prompt]
IF web_download_contains_mobile_code = TRUE
AND user_prompted_before_execution = FALSE
AND code_executed_automatically = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Mobile Code with User Confirmation]
IF mobile_code_execution_requested = TRUE
AND user_prompted = TRUE
AND user_confirmed_execution = TRUE
AND execution_logged = TRUE
THEN compliance = TRUE

[SCENARIO-05: Bypass of Prevention Controls]
IF mobile_code_prevention_bypassed = TRUE
AND bypass_not_authorized = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prevent automatic execution in designated applications | [RULE-01] |
| Enforce actions before mobile code execution | [RULE-02], [RULE-03], [RULE-05] |
| Disable auto-execute on portable storage | [RULE-04] |
| User prompting for email attachments | [RULE-02] |
| User prompting for web-based mobile code | [RULE-03] |
| Logging mobile code attempts | [RULE-06] |