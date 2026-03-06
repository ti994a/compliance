```markdown
# POLICY: PS-4: Personnel Termination

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-4 |
| NIST Control | PS-4: Personnel Termination |
| Version | 1.0 |
| Owner | CISO/HR Director |
| Keywords | termination, access revocation, exit interviews, credentials, property retrieval |

## 1. POLICY STATEMENT
Upon employee termination, the organization must immediately disable system access, revoke credentials, conduct exit interviews covering security topics, retrieve organizational property, and retain access to systems formerly controlled by the terminated individual. All termination actions must be executed within defined timeframes to maintain security posture.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full-time, part-time, temporary |
| Contractors | YES | When granted system access |
| Vendors | YES | When granted system access |
| Volunteers | YES | When granted system access |
| Board members | CONDITIONAL | When granted system access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Manager | • Initiate termination process<br>• Conduct exit interviews<br>• Coordinate with IT for access revocation<br>• Retrieve physical property |
| IT Security Administrator | • Disable system accounts<br>• Revoke authenticators and credentials<br>• Transfer data ownership<br>• Document access changes |
| Direct Supervisor | • Retrieve work materials<br>• Escort terminated employee<br>• Provide handover documentation |

## 4. RULES

**[RULE-01]** System access MUST be disabled within 4 hours for standard terminations and within 1 hour for involuntary terminations.
**[VALIDATION]** IF termination_type = "standard" AND access_disabled_time > 4_hours THEN violation
**[VALIDATION]** IF termination_type = "involuntary" AND access_disabled_time > 1_hour THEN critical_violation

**[RULE-02]** All authenticators and credentials associated with terminated individuals MUST be revoked or terminated within the same timeframe as system access disabling.
**[VALIDATION]** IF credentials_revoked = FALSE AND termination_date <= current_date THEN violation

**[RULE-03]** Exit interviews MUST be conducted for all terminated employees and SHALL include discussion of nondisclosure agreements, security obligations, and property return requirements.
**[VALIDATION]** IF exit_interview_completed = FALSE AND termination_reason != "job_abandonment" THEN violation

**[RULE-04]** All security-related organizational property including badges, tokens, keys, devices, and documentation MUST be retrieved before final departure.
**[VALIDATION]** IF property_retrieved = "incomplete" AND employee_departed = TRUE THEN violation

**[RULE-05]** Organizations MUST retain access to information and systems formerly controlled by terminated individuals for business continuity purposes.
**[VALIDATION]** IF data_transfer_completed = FALSE AND system_access_disabled = TRUE THEN operational_risk

**[RULE-06]** For cause terminations, system accounts MAY be disabled prior to employee notification at management discretion.
**[VALIDATION]** IF termination_cause = "security_violation" AND preemptive_disable = TRUE THEN compliant

## 5. REQUIRED PROCEDURES
- **[PROC-01]** Termination Notification Process - HR initiates termination workflow within 2 hours of decision
- **[PROC-02]** Access Revocation Procedure - IT systematically disables all system access and documents changes  
- **[PROC-03]** Exit Interview Protocol - Structured interview covering security topics and documentation requirements
- **[PROC-04]** Property Recovery Process - Systematic retrieval and inventory of organizational assets
- **[PROC-05]** Data Retention and Transfer - Secure transfer of work products and system ownership

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents involving terminated employees, audit findings, regulatory changes

## 7. SCENARIO PATTERNS

**[SCENARIO-01: Standard Employee Termination]**
IF termination_type = "voluntary"
AND access_disabled_time <= 4_hours
AND credentials_revoked = TRUE
AND exit_interview_completed = TRUE
AND property_retrieved = "complete"
THEN compliance = TRUE

**[SCENARIO-02: Emergency Termination]**
IF termination_type = "involuntary"
AND access_disabled_time > 1_hour
THEN compliance = FALSE
violation_severity = "Critical"

**[SCENARIO-03: Contractor Project End]**
IF user_type = "contractor"
AND project_end_date < current_date
AND system_access_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

**[SCENARIO-04: Job Abandonment Case]**
IF termination_reason = "job_abandonment"
AND access_disabled_time <= 24_hours
AND exit_interview_completed = FALSE
AND property_recovery_initiated = TRUE
THEN compliance = TRUE

**[SCENARIO-05: Incomplete Property Return]**
IF employee_departed = TRUE
AND property_retrieved = "partial"
AND follow_up_documented = TRUE
AND recovery_timeline <= 30_days
THEN compliance = CONDITIONAL
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Assessment Objective | Rule Reference |
|---------------------|----------------|
| System access disabled within defined timeframe | RULE-01 |
| Authenticators and credentials terminated/revoked | RULE-02 |
| Exit interviews conducted with security topics | RULE-03 |
| Security-related organizational property retrieved | RULE-04 |
| Access to former employee systems retained | RULE-05 |
```