```markdown
# POLICY: AC-16.2: Attribute Value Changes by Authorized Individuals

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-16.2 |
| NIST Control | AC-16.2: Attribute Value Changes by Authorized Individuals |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | attribute management, access control, authorization, security attributes, privacy attributes |

## 1. POLICY STATEMENT
Only authorized individuals or automated processes acting on their behalf may define or modify security and privacy attribute values that control access to organizational information. All attribute changes must be logged and subject to approval workflows based on the sensitivity of the attributes being modified.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid |
| Security attributes | YES | Classification, clearance, role-based attributes |
| Privacy attributes | YES | PII handling, consent status, retention |
| Automated processes | YES | When acting on behalf of authorized users |
| Third-party contractors | CONDITIONAL | Only when explicitly authorized |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Approve high-impact attribute changes<br>• Define attribute modification policies<br>• Review attribute change reports |
| System Administrator | • Implement technical controls for attribute management<br>• Configure approval workflows<br>• Monitor attribute change logs |
| Security Administrator | • Manage authorization lists<br>• Conduct periodic access reviews<br>• Investigate unauthorized changes |

## 4. RULES
[RULE-01] Only individuals explicitly listed in the authorized attribute managers list SHALL be permitted to modify security or privacy attributes.
[VALIDATION] IF user_id NOT IN authorized_managers_list AND attribute_change_attempted = TRUE THEN violation

[RULE-02] All attribute value changes MUST be logged with timestamp, user identity, old value, new value, and justification.
[VALIDATION] IF attribute_changed = TRUE AND (timestamp = NULL OR user_id = NULL OR old_value = NULL OR new_value = NULL) THEN violation

[RULE-03] High-impact attribute changes MUST require dual approval before implementation.
[VALIDATION] IF attribute_impact_level = "high" AND approval_count < 2 THEN violation

[RULE-04] Automated processes modifying attributes MUST be associated with a specific authorized individual's credentials and approval.
[VALIDATION] IF process_type = "automated" AND (associated_user_id = NULL OR user_authorization = FALSE) THEN violation

[RULE-05] Attribute modification capabilities MUST be removed within 4 hours of authorization revocation.
[VALIDATION] IF user_authorization_status = "revoked" AND modification_access_removed_time > 4_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Attribute Manager Authorization - Process for granting and revoking attribute modification rights
- [PROC-02] Attribute Change Approval Workflow - Standardized approval process based on attribute sensitivity
- [PROC-03] Audit Log Review - Monthly review of all attribute changes for unauthorized modifications
- [PROC-04] Emergency Attribute Changes - Expedited process for security incidents with post-change validation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving attribute manipulation, system architecture changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Attribute Modification]
IF user_role = "standard_user"
AND security_attribute_change = TRUE
AND user_id NOT IN authorized_managers_list
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Audit Trail]
IF privacy_attribute_modified = TRUE
AND change_log_entry = NULL
AND system_type = "production"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: High-Impact Change Without Dual Approval]
IF attribute_type = "security_clearance"
AND attribute_change_impact = "high"
AND approver_count = 1
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Automated Process with Valid Authorization]
IF process_type = "automated"
AND associated_user_authorized = TRUE
AND change_logged = TRUE
AND attribute_impact_level = "low"
THEN compliance = TRUE

[SCENARIO-05: Delayed Access Revocation]
IF user_authorization_revoked = TRUE
AND attribute_modification_access = "active"
AND hours_since_revocation > 4
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authorized individuals can define security attribute values | RULE-01, RULE-04 |
| Authorized individuals can change security attribute values | RULE-01, RULE-03 |
| Authorized individuals can define privacy attribute values | RULE-01, RULE-04 |
| Authorized individuals can change privacy attribute values | RULE-01, RULE-03 |
| Process authorization verification | RULE-04 |
| Audit trail maintenance | RULE-02 |
```