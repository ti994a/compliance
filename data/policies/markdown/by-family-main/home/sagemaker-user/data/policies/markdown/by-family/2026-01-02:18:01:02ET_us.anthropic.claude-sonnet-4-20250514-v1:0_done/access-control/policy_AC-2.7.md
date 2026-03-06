# POLICY: AC-2.7: Privileged User Accounts

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-2.7 |
| NIST Control | AC-2.7: Privileged User Accounts |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | privileged access, role-based access, account management, access revocation, monitoring |

## 1. POLICY STATEMENT
The organization SHALL establish and administer privileged user accounts using a role-based access control scheme with continuous monitoring of role assignments and changes. Access MUST be revoked immediately when privileged roles are no longer appropriate for the user's responsibilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All privileged user accounts | YES | Includes system, network, database, application admins |
| Service accounts with elevated privileges | YES | Must follow same role-based principles |
| Temporary privileged access | YES | Including break-glass and emergency access |
| Third-party contractor privileged accounts | YES | Additional approval requirements apply |
| Standard user accounts | NO | Covered under base AC-2 control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity and Access Management Team | • Define privileged roles and access schemes<br>• Monitor role assignments and changes<br>• Execute access revocation procedures |
| System Owners | • Request privileged access for authorized personnel<br>• Notify IAM of role changes within 24 hours<br>• Conduct quarterly access reviews |
| Privileged Users | • Use privileged access only for authorized functions<br>• Report role changes or transfers immediately |

## 4. RULES
[RULE-01] All privileged user accounts MUST be established and administered according to a documented role-based access control scheme that defines specific roles, responsibilities, and associated system privileges.
[VALIDATION] IF privileged_account_exists = TRUE AND role_based_scheme_documented = FALSE THEN violation

[RULE-02] Privileged role assignments and attribute changes MUST be monitored in real-time with automated alerts generated for any modifications.
[VALIDATION] IF privileged_role_change = TRUE AND monitoring_alert_generated = FALSE THEN violation

[RULE-03] Access revocation for privileged accounts MUST occur within 1 hour of notification that role assignments are no longer appropriate.
[VALIDATION] IF role_no_longer_appropriate = TRUE AND revocation_time > 1_hour THEN critical_violation

[RULE-04] Privileged role assignments MUST be reviewed and revalidated quarterly by system owners and annually by senior management.
[VALIDATION] IF last_quarterly_review > 90_days OR last_annual_review > 365_days THEN violation

[RULE-05] Emergency or break-glass privileged access MUST be automatically revoked within 24 hours unless explicitly extended through documented approval process.
[VALIDATION] IF emergency_access_granted = TRUE AND access_duration > 24_hours AND extension_approved = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privileged Role Definition - Document all privileged roles with specific access rights and responsibilities
- [PROC-02] Privileged Account Provisioning - Standardized process for granting role-based privileged access
- [PROC-03] Continuous Monitoring - Real-time monitoring and alerting for privileged account activities
- [PROC-04] Access Revocation - Immediate removal of privileged access when no longer needed
- [PROC-05] Periodic Access Review - Quarterly validation of privileged role appropriateness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving privileged accounts, organizational restructuring, technology platform changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Employee Role Change]
IF employee_role_changed = TRUE
AND privileged_access_still_active = TRUE
AND new_role_requires_privileges = FALSE
AND notification_sent > 24_hours_ago
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Project Completion]
IF user_type = "contractor"
AND project_status = "completed"
AND privileged_access_active = TRUE
AND revocation_time > 1_hour
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Emergency Access Extension]
IF access_type = "emergency"
AND access_duration > 24_hours
AND extension_request_submitted = TRUE
AND management_approval = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-04: Unmonitored Privilege Escalation]
IF privilege_level_increased = TRUE
AND monitoring_system_alert = FALSE
AND change_detection_time > 15_minutes
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Overdue Access Review]
IF privileged_account_active = TRUE
AND last_access_review > 90_days
AND business_justification_current = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privileged accounts established per role-based scheme | [RULE-01] |
| Privileged role assignments monitored | [RULE-02] |
| Changes to roles or attributes monitored | [RULE-02] |
| Access revoked when assignments inappropriate | [RULE-03] |
| Periodic validation of role appropriateness | [RULE-04] |
| Emergency access controls | [RULE-05] |