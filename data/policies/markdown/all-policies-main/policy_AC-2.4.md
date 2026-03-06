# POLICY: AC-2.4: Automated Audit Actions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-2.4 |
| NIST Control | AC-2.4: Automated Audit Actions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | account management, automated auditing, audit records, account lifecycle, access control |

## 1. POLICY STATEMENT
All account creation, modification, enabling, disabling, and removal actions MUST be automatically audited across all systems and applications. These audit records SHALL be generated in real-time without manual intervention and maintained in accordance with organizational retention requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, and hybrid |
| User Accounts | YES | All account types (privileged, standard, service) |
| Service Accounts | YES | Automated and manual service accounts |
| Shared Accounts | YES | Where organizationally approved |
| Guest/Temporary Accounts | YES | All temporary access accounts |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure automated audit mechanisms<br>• Ensure audit functionality is operational<br>• Maintain audit system availability |
| Security Operations Team | • Monitor audit record generation<br>• Investigate audit failures<br>• Review audit configurations |
| Account Managers | • Validate audit records capture all account actions<br>• Report audit discrepancies<br>• Ensure compliance with audit requirements |

## 4. RULES

[RULE-01] All systems MUST automatically generate audit records for account creation actions without manual intervention.
[VALIDATION] IF account_created = TRUE AND audit_record_generated = FALSE THEN critical_violation

[RULE-02] All systems MUST automatically generate audit records for account modification actions including permission changes, attribute updates, and role assignments.
[VALIDATION] IF account_modified = TRUE AND audit_record_generated = FALSE THEN critical_violation

[RULE-03] All systems MUST automatically generate audit records for account enabling actions when dormant or disabled accounts are reactivated.
[VALIDATION] IF account_enabled = TRUE AND previous_status = "disabled" AND audit_record_generated = FALSE THEN critical_violation

[RULE-04] All systems MUST automatically generate audit records for account disabling actions including temporary suspensions and lockouts.
[VALIDATION] IF account_disabled = TRUE AND audit_record_generated = FALSE THEN critical_violation

[RULE-05] All systems MUST automatically generate audit records for account removal actions including deletions and permanent deactivations.
[VALIDATION] IF account_removed = TRUE AND audit_record_generated = FALSE THEN critical_violation

[RULE-06] Automated audit mechanisms MUST capture the timestamp, user identity, action type, target account, and system identifier for all account management actions.
[VALIDATION] IF audit_record_exists = TRUE AND (timestamp = NULL OR user_identity = NULL OR action_type = NULL OR target_account = NULL OR system_id = NULL) THEN major_violation

[RULE-07] Systems MUST generate alerts when automated audit mechanisms fail or become unavailable.
[VALIDATION] IF audit_mechanism_status = "failed" AND alert_generated = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Audit System Configuration - Configure and maintain automated audit mechanisms for account management actions
- [PROC-02] Audit Record Validation - Regularly validate completeness and accuracy of automated audit records
- [PROC-03] Audit Failure Response - Respond to and remediate automated audit mechanism failures
- [PROC-04] Audit Record Review - Review and analyze account management audit records per AU-06 requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: System changes, audit failures, compliance findings, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Successful Account Creation Audit]
IF account_creation_requested = TRUE
AND automated_audit_enabled = TRUE
AND audit_record_generated = TRUE
AND audit_record_complete = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Audit for Account Modification]
IF account_permissions_modified = TRUE
AND automated_audit_enabled = TRUE
AND audit_record_generated = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Audit System Failure During Account Removal]
IF account_removal_action = TRUE
AND audit_mechanism_status = "failed"
AND failure_alert_generated = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Audit Record]
IF account_disabled = TRUE
AND audit_record_generated = TRUE
AND (timestamp = NULL OR user_identity = NULL)
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-05: Service Account Management Audit]
IF service_account_created = TRUE
AND account_type = "service"
AND automated_audit_enabled = TRUE
AND audit_record_generated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Account creation is automatically audited | [RULE-01] |
| Account modification is automatically audited | [RULE-02] |
| Account enabling is automatically audited | [RULE-03] |
| Account disabling is automatically audited | [RULE-04] |
| Account removal actions are automatically audited | [RULE-05] |