# POLICY: AC-2.3: Disable Accounts

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-2.3 |
| NIST Control | AC-2.3: Disable Accounts |
| Version | 1.0 |
| Owner | Identity and Access Management Team |
| Keywords | account_disable, expired_accounts, inactive_accounts, policy_violation, user_separation |

## 1. POLICY STATEMENT
All user accounts must be automatically or manually disabled within defined timeframes when they expire, become unassociated with users, violate organizational policy, or remain inactive beyond established thresholds. This policy supports least privilege principles by reducing the attack surface through timely account lifecycle management.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All user accounts | YES | Including employees, contractors, service accounts |
| System accounts | YES | When associated with individuals |
| Shared accounts | YES | Must have designated ownership |
| Emergency accounts | YES | Subject to shorter disable timeframes |
| Guest accounts | YES | Subject to automatic expiration |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity and Access Management Team | • Implement automated account disabling mechanisms<br>• Monitor account status and lifecycle events<br>• Maintain account disable procedures |
| System Administrators | • Execute manual account disabling when required<br>• Verify automated disabling functions<br>• Report account anomalies |
| Human Resources | • Notify IAM team of employee status changes<br>• Provide termination and separation dates<br>• Validate user-account associations |

## 4. RULES
[RULE-01] Expired accounts MUST be disabled within 24 hours of expiration date.
[VALIDATION] IF account_expiration_date < current_date AND account_status = "active" AND hours_since_expiration > 24 THEN violation

[RULE-02] Accounts no longer associated with users MUST be disabled within 24 hours of user separation notification.
[VALIDATION] IF user_separation_date < current_date AND account_status = "active" AND hours_since_separation > 24 THEN violation

[RULE-03] Accounts violating organizational policy MUST be disabled within 4 hours of policy violation detection.
[VALIDATION] IF policy_violation_detected = TRUE AND account_status = "active" AND hours_since_detection > 4 THEN critical_violation

[RULE-04] Inactive accounts MUST be disabled after 90 days of inactivity for standard users and 30 days for privileged users.
[VALIDATION] IF days_since_last_login > 90 AND user_type = "standard" AND account_status = "active" THEN violation
[VALIDATION] IF days_since_last_login > 30 AND user_type = "privileged" AND account_status = "active" THEN violation

[RULE-05] Emergency accounts MUST be disabled within 72 hours of creation unless explicitly renewed.
[VALIDATION] IF account_type = "emergency" AND hours_since_creation > 72 AND renewal_documented = FALSE AND account_status = "active" THEN violation

[RULE-06] Contractor accounts MUST be disabled within 24 hours of contract end date.
[VALIDATION] IF user_type = "contractor" AND contract_end_date < current_date AND account_status = "active" AND hours_since_contract_end > 24 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Automated Account Lifecycle Management - Implement systems to automatically disable accounts based on HR feeds and expiration dates
- [PROC-02] Manual Account Disabling Process - Define escalation procedures when automated disabling fails
- [PROC-03] Policy Violation Response - Establish rapid response for accounts violating security policies
- [PROC-04] Account Status Monitoring - Regular auditing of account status against disable criteria

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving disabled accounts, changes to HR systems, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Terminated Employee Account]
IF user_status = "terminated"
AND termination_date = "2024-01-15"
AND current_date = "2024-01-17"
AND account_status = "active"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inactive Privileged Account]
IF user_type = "privileged"
AND last_login_date = "2024-01-01"
AND current_date = "2024-02-15"
AND account_status = "active"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Policy Violation Response]
IF policy_violation_detected = TRUE
AND detection_time = "2024-01-15 09:00"
AND current_time = "2024-01-15 14:00"
AND account_status = "active"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Expired Emergency Account]
IF account_type = "emergency"
AND creation_date = "2024-01-10"
AND current_date = "2024-01-14"
AND renewal_documented = FALSE
AND account_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Contractor After Project End]
IF user_type = "contractor"
AND contract_end_date = "2024-01-20"
AND current_date = "2024-01-22"
AND account_status = "disabled"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Disable expired accounts within defined timeframe | [RULE-01] |
| Disable accounts no longer associated with users | [RULE-02] |
| Disable accounts violating organizational policy | [RULE-03] |
| Disable inactive accounts within defined timeframe | [RULE-04] |