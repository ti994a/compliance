# POLICY: AC-2: Account Management

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-2 |
| NIST Control | AC-2: Account Management |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | account management, access control, user accounts, privileged access, account lifecycle, authentication |

## 1. POLICY STATEMENT
All system accounts must be properly managed throughout their lifecycle with defined types, assigned managers, and appropriate approvals. Account creation, modification, monitoring, and removal must follow established procedures with timely notifications for personnel changes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All system accounts | YES | Individual, shared, group, system, service accounts |
| Cloud infrastructure accounts | YES | AWS, Azure, GCP user and service accounts |
| Application accounts | YES | Business applications and databases |
| Guest/contractor accounts | YES | Temporary and external user access |
| Emergency accounts | YES | Crisis response accounts with special procedures |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Account Managers | • Approve account creation/modification requests<br>• Monitor assigned accounts for compliance<br>• Coordinate with HR for personnel changes |
| System Administrators | • Implement account lifecycle procedures<br>• Configure account attributes and privileges<br>• Maintain account inventory and documentation |
| Security Team | • Review account compliance<br>• Monitor account usage patterns<br>• Investigate anomalous account activity |

## 4. RULES

[RULE-01] Account types allowed (individual, system, service) and prohibited (shared, anonymous, guest) MUST be documented and enforced per system classification.
[VALIDATION] IF account_type IN prohibited_list AND account_status = "active" THEN violation

[RULE-02] All account creation requests MUST receive approval from designated account manager before provisioning.
[VALIDATION] IF account_created = TRUE AND manager_approval = FALSE THEN critical_violation

[RULE-03] Account managers MUST be notified within 24 hours when users are terminated and within 8 hours for involuntary terminations.
[VALIDATION] IF termination_type = "voluntary" AND notification_time > 24_hours THEN violation
[VALIDATION] IF termination_type = "involuntary" AND notification_time > 8_hours THEN critical_violation

[RULE-04] Accounts MUST be disabled within 24 hours of user termination and removed within 30 days unless retention is required for legal/audit purposes.
[VALIDATION] IF user_terminated = TRUE AND account_active = TRUE AND hours_since_termination > 24 THEN violation

[RULE-05] Privileged accounts MUST receive additional approval from system owner and CISO before activation.
[VALIDATION] IF account_privileges = "administrative" AND (system_owner_approval = FALSE OR ciso_approval = FALSE) THEN critical_violation

[RULE-06] Account reviews MUST be conducted quarterly for privileged accounts and annually for standard accounts.
[VALIDATION] IF account_type = "privileged" AND days_since_review > 90 THEN violation
[VALIDATION] IF account_type = "standard" AND days_since_review > 365 THEN violation

[RULE-07] Shared or group account authenticators MUST be changed within 24 hours when any member is removed from the group.
[VALIDATION] IF group_member_removed = TRUE AND authenticator_changed = FALSE AND hours_since_removal > 24 THEN violation

[RULE-08] Account usage MUST be monitored and anomalous activity reported to security team within 4 hours of detection.
[VALIDATION] IF anomalous_activity_detected = TRUE AND security_notification_time > 4_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Account Provisioning Process - Standardized workflow for account creation with approval gates
- [PROC-02] Account Review Process - Quarterly/annual reviews with attestation requirements  
- [PROC-03] Personnel Change Integration - Automated HR system integration for terminations/transfers
- [PROC-04] Emergency Account Management - Crisis response procedures for rapid account activation
- [PROC-05] Privileged Account Oversight - Enhanced controls and monitoring for administrative access

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Quarterly  
- Triggering events: Security incidents, regulatory changes, system architecture changes, audit findings

## 7. SCENARIO PATTERNS

[SCENARIO-01: Terminated Employee Access]
IF employee_status = "terminated"
AND account_status = "active" 
AND hours_since_termination > 24
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unapproved Privileged Account]
IF account_privileges = "administrative"
AND system_owner_approval = FALSE
AND account_status = "active"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Overdue Account Review]
IF account_type = "privileged"
AND days_since_last_review > 90
AND review_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Shared Account Credential Change]
IF account_type = "shared"
AND group_member_departed = TRUE
AND credential_rotated = FALSE
AND hours_since_departure > 24
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Prohibited Account Type]
IF account_type = "anonymous"
AND system_classification = "confidential"
AND account_status = "active"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Account types defined and documented | [RULE-01] |
| Account managers assigned | [RULE-02], [RULE-05] |
| Prerequisites for group membership | [RULE-07] |
| Approval required for account creation | [RULE-02], [RULE-05] |
| Account lifecycle management | [RULE-04] |
| Account usage monitoring | [RULE-08] |
| Notification requirements | [RULE-03] |
| Access authorization validation | [RULE-02], [RULE-05] |
| Account compliance reviews | [RULE-06] |
| Shared account authenticator management | [RULE-07] |
| Personnel termination alignment | [RULE-03], [RULE-04] |