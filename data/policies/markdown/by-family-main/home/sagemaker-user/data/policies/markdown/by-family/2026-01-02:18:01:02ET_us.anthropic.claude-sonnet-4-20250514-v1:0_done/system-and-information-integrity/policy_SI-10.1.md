# POLICY: SI-10.1: Manual Override Capability

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-10.1 |
| NIST Control | SI-10.1: Manual Override Capability |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | input validation, manual override, authorization, audit, contingency, emergency access |

## 1. POLICY STATEMENT
The organization SHALL provide manual override capabilities for input validation systems that are restricted to authorized personnel and fully audited. Manual overrides are permitted only during defined contingency situations or emergency circumstances when normal input validation would prevent critical business operations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Systems with input validation controls |
| Cloud applications | YES | Including SaaS, PaaS, IaaS platforms |
| Third-party systems | YES | When organization controls override capability |
| Development/test systems | CONDITIONAL | Only if processing production data |
| Emergency response systems | YES | Critical for contingency operations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement manual override mechanisms<br>• Configure authorization controls<br>• Monitor override usage |
| Security Operations | • Review override audit logs<br>• Investigate unauthorized usage<br>• Maintain authorized user lists |
| Application Owners | • Define override requirements<br>• Justify business need<br>• Approve authorized users |

## 4. RULES
[RULE-01] Systems with input validation controls MUST provide manual override capability for organization-defined information inputs during contingency situations.
[VALIDATION] IF system_has_input_validation = TRUE AND manual_override_capability = FALSE THEN violation

[RULE-02] Manual override capability MUST be restricted to only pre-authorized individuals with documented business justification.
[VALIDATION] IF override_used = TRUE AND user_authorized = FALSE THEN critical_violation

[RULE-03] All use of manual override capability MUST be logged with timestamp, user identity, justification, and system affected.
[VALIDATION] IF override_used = TRUE AND audit_log_created = FALSE THEN violation

[RULE-04] Authorized override users MUST be reviewed and reauthorized at least quarterly.
[VALIDATION] IF last_authorization_review > 90_days THEN violation

[RULE-05] Manual override usage MUST be reported to security operations within 24 hours of activation.
[VALIDATION] IF override_used = TRUE AND security_notification_time > 24_hours THEN violation

[RULE-06] Override capability SHALL only be used during declared contingency events or pre-approved emergency circumstances.
[VALIDATION] IF override_used = TRUE AND (contingency_declared = FALSE AND emergency_approved = FALSE) THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Manual Override Authorization - Process for designating and approving authorized override users
- [PROC-02] Override Activation Protocol - Steps for properly invoking manual override during emergencies
- [PROC-03] Override Audit Review - Regular review of override usage and compliance validation
- [PROC-04] Contingency Override Planning - Integration with business continuity and disaster recovery plans

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving override misuse, system changes affecting input validation, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Authorized Emergency Override]
IF contingency_event = "declared"
AND user_authorized = TRUE
AND override_logged = TRUE
AND security_notified = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Override Usage]
IF override_used = TRUE
AND user_authorized = FALSE
AND system_type = "production"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Audit Trail]
IF override_used = TRUE
AND user_authorized = TRUE
AND audit_log_complete = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Stale Authorization]
IF user_authorized = TRUE
AND last_authorization_review > 90_days
AND override_capability_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Delayed Security Notification]
IF override_used = TRUE
AND security_notification_time > 24_hours
AND contingency_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Manual override capability provided for defined inputs | [RULE-01] |
| Override use restricted to authorized individuals | [RULE-02] |
| Override usage is audited | [RULE-03] |
| Authorization management and review | [RULE-04] |
| Proper contingency usage controls | [RULE-06] |