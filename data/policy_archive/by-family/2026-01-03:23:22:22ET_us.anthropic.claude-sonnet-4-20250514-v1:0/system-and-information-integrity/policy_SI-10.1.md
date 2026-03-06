# POLICY: SI-10.1: Manual Override Capability

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-10.1 |
| NIST Control | SI-10.1: Manual Override Capability |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | input validation, manual override, authorization, auditing, contingency, emergency access |

## 1. POLICY STATEMENT
The organization SHALL provide manual override capabilities for input validation systems that are restricted to authorized personnel only and fully audited. Manual overrides SHALL be used exclusively during defined contingency situations or emergency events when normal input validation processes cannot function.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems with input validation | YES | Including web applications, APIs, databases |
| Cloud-based applications | YES | Both SaaS and organization-managed |
| Third-party integrated systems | CONDITIONAL | When organization controls override capability |
| Development/test environments | YES | Must mirror production controls |
| Legacy systems | CONDITIONAL | Based on technical feasibility assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement manual override mechanisms<br>• Configure audit logging for override events<br>• Maintain authorized user lists |
| Security Operations | • Monitor override usage patterns<br>• Investigate unauthorized override attempts<br>• Review audit logs for compliance |
| Application Owners | • Define input types requiring override capability<br>• Authorize personnel for override access<br>• Document business justification for overrides |

## 4. RULES
[RULE-01] All systems with input validation MUST implement manual override capability for critical business functions and emergency scenarios.
[VALIDATION] IF system_has_input_validation = TRUE AND manual_override_implemented = FALSE THEN violation

[RULE-02] Manual override access SHALL be restricted to explicitly authorized individuals with documented business justification.
[VALIDATION] IF override_user NOT IN authorized_users_list THEN critical_violation

[RULE-03] All manual override usage MUST be logged with timestamp, user identity, system affected, input bypassed, and business justification.
[VALIDATION] IF override_used = TRUE AND (timestamp = NULL OR user_id = NULL OR justification = NULL) THEN violation

[RULE-04] Manual override capabilities SHALL only be used during declared contingency events or pre-approved emergency situations.
[VALIDATION] IF override_used = TRUE AND (contingency_declared = FALSE AND emergency_approved = FALSE) THEN violation

[RULE-05] Override access permissions MUST be reviewed quarterly and immediately after any personnel changes affecting authorized users.
[VALIDATION] IF last_review_date > 90_days OR personnel_change_date > access_review_date THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Manual Override Authorization - Process for granting and revoking override permissions
- [PROC-02] Override Usage Documentation - Standard for recording business justification and approval
- [PROC-03] Emergency Override Activation - Steps for using overrides during contingency events
- [PROC-04] Override Audit Review - Monthly review of all override usage and patterns

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents involving overrides, system architecture changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Emergency Override During Outage]
IF contingency_event = "declared"
AND user_id IN authorized_emergency_users
AND override_logged = TRUE
AND business_justification = "documented"
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Override Usage]
IF override_used = TRUE
AND user_id NOT IN authorized_users_list
AND audit_log = "generated"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Override Without Proper Logging]
IF override_used = TRUE
AND user_id IN authorized_users_list
AND (audit_log = "incomplete" OR justification = "missing")
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Routine Override Usage]
IF override_used = TRUE
AND contingency_declared = FALSE
AND emergency_approved = FALSE
AND frequency = "daily"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Stale Override Permissions]
IF user_employment_status = "terminated"
AND override_access = "active"
AND termination_date < (current_date - 1_day)
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Manual override capability provided | [RULE-01] |
| Access restricted to authorized individuals | [RULE-02] |
| Override usage audited | [RULE-03] |
| Limited to contingency/emergency use | [RULE-04] |
| Regular access review | [RULE-05] |