# POLICY: SC-18.4: Prevent Automatic Execution

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-18.4 |
| NIST Control | SC-18.4: Prevent Automatic Execution |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mobile code, automatic execution, email attachments, web links, portable storage, auto-execute |

## 1. POLICY STATEMENT
The organization SHALL prevent automatic execution of mobile code in designated software applications and SHALL enforce mandatory user approval actions before executing any mobile code. All systems MUST implement controls to disable auto-execute features on portable storage devices and require explicit user consent for code execution.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Email Systems | YES | All email clients and servers |
| Web Browsers | YES | All corporate and BYOD browsers |
| Portable Storage Devices | YES | USB, CD, DVD, external drives |
| Desktop Applications | CONDITIONAL | Applications handling external content |
| Mobile Applications | YES | Corporate-managed mobile apps |
| Virtualized Systems | YES | All virtual desktop infrastructure |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define mobile code execution policies<br>• Approve software application classifications<br>• Review security control effectiveness |
| System Administrators | • Configure auto-execute prevention settings<br>• Implement user prompt mechanisms<br>• Monitor mobile code execution attempts |
| Security Operations | • Monitor mobile code security events<br>• Investigate unauthorized execution attempts<br>• Maintain mobile code security controls |

## 4. RULES
[RULE-01] Software applications designated as high-risk MUST prevent automatic execution of mobile code without explicit user approval.
[VALIDATION] IF application_risk_level = "high" AND mobile_code_auto_execution = TRUE THEN critical_violation

[RULE-02] Email systems MUST prompt users before opening email attachments or executing embedded mobile code.
[VALIDATION] IF email_attachment_opened = TRUE AND user_prompt_displayed = FALSE THEN violation

[RULE-03] Web browsers MUST require user confirmation before executing mobile code from web links or downloads.
[VALIDATION] IF web_mobile_code_executed = TRUE AND user_confirmation = FALSE THEN violation

[RULE-04] Portable storage devices MUST have auto-execute features disabled on all organizational systems.
[VALIDATION] IF portable_device_connected = TRUE AND auto_execute_enabled = TRUE THEN violation

[RULE-05] User approval actions for mobile code execution MUST be logged and retained for audit purposes.
[VALIDATION] IF mobile_code_executed = TRUE AND execution_logged = FALSE THEN violation

[RULE-06] Systems MUST maintain a defined list of software applications where mobile code auto-execution is prohibited.
[VALIDATION] IF prohibited_app_list_exists = FALSE OR prohibited_app_list_age > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Mobile Code Risk Assessment - Classify applications and define execution restrictions
- [PROC-02] Auto-Execute Configuration Management - Disable auto-execute features on systems and devices  
- [PROC-03] User Prompt Implementation - Configure and test user approval mechanisms
- [PROC-04] Mobile Code Monitoring - Log and review mobile code execution events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving mobile code, new application deployments, system configuration changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Email Attachment Auto-Execution]
IF email_attachment_type = "executable"
AND auto_execution_occurred = TRUE
AND user_prompt_bypassed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: USB Auto-Run Disabled]
IF portable_device_type = "USB"
AND device_connected = TRUE
AND auto_run_disabled = TRUE
AND user_prompt_displayed = TRUE
THEN compliance = TRUE

[SCENARIO-03: Web Browser Mobile Code]
IF browser_mobile_code_detected = TRUE
AND user_confirmation_required = TRUE
AND confirmation_received = FALSE
AND code_blocked = TRUE
THEN compliance = TRUE

[SCENARIO-04: Prohibited Application Mobile Code]
IF application_name IN prohibited_applications_list
AND mobile_code_auto_executed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Mobile Code Logging Failure]
IF mobile_code_execution_attempt = TRUE
AND execution_logged = FALSE
AND logging_system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Automatic execution prevention in defined applications | [RULE-01], [RULE-06] |
| User prompt enforcement before mobile code execution | [RULE-02], [RULE-03] |
| Auto-execute feature disabling on portable devices | [RULE-04] |
| Mobile code execution logging and audit trail | [RULE-05] |