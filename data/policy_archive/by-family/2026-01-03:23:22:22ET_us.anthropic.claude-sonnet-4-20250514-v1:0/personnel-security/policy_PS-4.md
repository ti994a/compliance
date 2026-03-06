# POLICY: PS-4: Personnel Termination

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-4 |
| NIST Control | PS-4: Personnel Termination |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | termination, access revocation, exit interview, property retrieval, credentials, authenticators |

## 1. POLICY STATEMENT
Upon employee termination, organizations MUST disable system access within defined timeframes, revoke all authenticators and credentials, conduct security-focused exit interviews, retrieve organizational property, and retain access to systems formerly controlled by the terminated individual. Termination procedures MUST be executed promptly to prevent unauthorized access and ensure proper accountability.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full-time, part-time, temporary |
| Contractors | YES | Long-term contractors with system access |
| Vendors | YES | Third-party personnel with privileged access |
| Interns | YES | All intern classifications |
| Volunteers | CONDITIONAL | Only those with system access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Manager | • Initiate termination workflow within 1 hour of decision<br>• Schedule and conduct exit interviews<br>• Coordinate property retrieval<br>• Maintain termination records |
| IT Security Manager | • Disable system access per defined timeframes<br>• Revoke authenticators and credentials<br>• Document access retention requirements<br>• Verify complete access removal |
| Direct Supervisor | • Retrieve organizational property<br>• Participate in exit interview process<br>• Confirm completion of knowledge transfer |

## 4. RULES
[RULE-01] System access MUST be disabled within 4 hours for standard terminations and within 1 hour for involuntary terminations or terminations for cause.
[VALIDATION] IF termination_type = "standard" AND access_disabled_time > 4_hours THEN violation
[VALIDATION] IF termination_type IN ["involuntary", "for_cause"] AND access_disabled_time > 1_hour THEN critical_violation

[RULE-02] All authenticators and credentials associated with terminated individuals MUST be revoked or terminated within 24 hours of termination notification.
[VALIDATION] IF termination_date + 24_hours < current_time AND active_credentials > 0 THEN violation

[RULE-03] Exit interviews MUST be conducted for all terminated employees and SHALL include discussion of nondisclosure agreements, security obligations, and future employment limitations.
[VALIDATION] IF exit_interview_completed = FALSE AND termination_reason != "job_abandonment" THEN violation

[RULE-04] All security-related organizational property MUST be retrieved before final departure or within 48 hours for remote employees.
[VALIDATION] IF property_retrieved = FALSE AND hours_since_termination > 48 THEN violation

[RULE-05] Organizations MUST retain administrative access to information and systems formerly controlled by terminated individuals for minimum 90 days.
[VALIDATION] IF admin_access_retained = FALSE OR retention_period < 90_days THEN violation

[RULE-06] Termination actions for individuals with security clearances MUST be completed within 2 hours and reported to security office within 4 hours.
[VALIDATION] IF security_clearance = TRUE AND termination_actions_time > 2_hours THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Employee Termination Workflow - Automated process triggering all termination actions
- [PROC-02] Access Revocation Checklist - Systematic verification of all access removal
- [PROC-03] Exit Interview Protocol - Standardized security topics and documentation
- [PROC-04] Property Recovery Process - Tracking and verification of returned items
- [PROC-05] System Access Retention - Procedures for maintaining access to former employee data

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving terminated employees, changes to termination processes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Employee Termination]
IF termination_type = "standard"
AND access_disabled_time <= 4_hours
AND credentials_revoked_time <= 24_hours
AND exit_interview_completed = TRUE
THEN compliance = TRUE

[SCENARIO-02: Involuntary Termination Delay]
IF termination_type = "involuntary"
AND access_disabled_time > 1_hour
AND system_access_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Remote Employee Property Issues]
IF employee_location = "remote"
AND termination_date + 48_hours < current_date
AND property_retrieved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Security Clearance Termination]
IF security_clearance = TRUE
AND termination_actions_time <= 2_hours
AND security_office_notified_time <= 4_hours
AND exit_interview_completed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Job Abandonment Case]
IF termination_reason = "job_abandonment"
AND access_disabled_time <= 1_hour
AND exit_interview_completed = FALSE
AND property_recovery_initiated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System access disabled within defined timeframe | [RULE-01] |
| Authenticators and credentials terminated/revoked | [RULE-02] |
| Exit interviews conducted with security discussion | [RULE-03] |
| Security-related property retrieved | [RULE-04] |
| Access to former employee systems retained | [RULE-05] |
| Special handling for security clearance holders | [RULE-06] |