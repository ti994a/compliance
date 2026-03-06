# POLICY: PS-4: Personnel Termination

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-4 |
| NIST Control | PS-4: Personnel Termination |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | termination, access revocation, exit interviews, property retrieval, authenticators |

## 1. POLICY STATEMENT
Upon termination of individual employment, the organization must immediately disable system access, revoke credentials, conduct exit interviews, and retrieve organizational property. Access to information and systems formerly controlled by terminated individuals must be retained by the organization.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full-time, part-time, temporary |
| Contractors | YES | When system access provided |
| Volunteers | YES | When system access provided |
| Third-party users | YES | When organizational accounts exist |
| Service accounts | NO | Covered under technical controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Manager | • Initiate termination workflow<br>• Conduct exit interviews<br>• Coordinate property retrieval<br>• Maintain termination records |
| IT Security Administrator | • Disable system accounts<br>• Revoke authenticators and credentials<br>• Document access revocation<br>• Retain access to terminated user data |
| Direct Supervisor | • Retrieve organizational property<br>• Participate in exit interview<br>• Confirm completion of termination checklist |

## 4. RULES
[RULE-01] System access MUST be disabled within 4 hours for voluntary terminations and within 1 hour for involuntary terminations.
[VALIDATION] IF termination_type = "voluntary" AND access_disabled_time > 4_hours THEN violation
[VALIDATION] IF termination_type = "involuntary" AND access_disabled_time > 1_hour THEN critical_violation

[RULE-02] All authenticators and credentials associated with terminated individuals MUST be terminated or revoked within 24 hours of termination notification.
[VALIDATION] IF credential_revocation_time > 24_hours THEN violation

[RULE-03] Exit interviews MUST be conducted for all terminated employees and SHALL include discussion of nondisclosure agreements, security obligations, and return of property.
[VALIDATION] IF exit_interview_completed = FALSE AND termination_reason != "job_abandonment" THEN violation

[RULE-04] All security-related organizational property MUST be retrieved before final termination processing, including hardware tokens, ID cards, keys, and technical documentation.
[VALIDATION] IF property_retrieval_complete = FALSE AND termination_status = "final" THEN violation

[RULE-05] Organizations MUST retain access to information and systems formerly controlled by terminated individuals for a minimum of 90 days.
[VALIDATION] IF data_retention_period < 90_days THEN violation

[RULE-06] For cause terminations, account disabling SHOULD occur prior to employee notification when security risk is assessed as high.
[VALIDATION] IF termination_cause = "security_violation" AND pre_notification_disable = FALSE THEN advisory_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Personnel Termination Workflow - Automated process triggered by HR system
- [PROC-02] Emergency Account Disabling - Immediate access revocation for high-risk terminations  
- [PROC-03] Exit Interview Protocol - Standardized security topics and documentation
- [PROC-04] Property Recovery Checklist - Comprehensive inventory and return process
- [PROC-05] Data Retention and Transfer - Secure handling of terminated user information

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving terminated users, audit findings, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Voluntary Termination]
IF termination_type = "voluntary"
AND notice_period >= 2_weeks
AND access_disabled_time <= 4_hours
AND exit_interview_completed = TRUE
THEN compliance = TRUE

[SCENARIO-02: Emergency Involuntary Termination]
IF termination_type = "involuntary"
AND termination_cause = "policy_violation"
AND access_disabled_time > 1_hour
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Contractor Project Completion]
IF user_type = "contractor"
AND project_end_date = current_date
AND access_disabled_time <= 4_hours
AND property_returned = TRUE
THEN compliance = TRUE

[SCENARIO-04: Job Abandonment Case]
IF termination_reason = "job_abandonment"
AND access_disabled_time <= 24_hours
AND exit_interview_completed = FALSE
AND property_retrieval_attempted = TRUE
THEN compliance = TRUE

[SCENARIO-05: Incomplete Property Return]
IF termination_status = "final"
AND property_retrieval_complete = FALSE
AND outstanding_items > 0
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System access disabled within defined timeframe | [RULE-01] |
| Authenticators and credentials terminated/revoked | [RULE-02] |
| Exit interviews conducted with security topics | [RULE-03] |
| Security-related property retrieved | [RULE-04] |
| Access to former employee information retained | [RULE-05] |