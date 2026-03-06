```markdown
# POLICY: IA-2.2: Multi-factor Authentication to Non-privileged Accounts

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-2.2 |
| NIST Control | IA-2.2: Multi-factor Authentication to Non-privileged Accounts |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | multi-factor authentication, MFA, non-privileged accounts, authentication factors, biometric, hardware tokens |

## 1. POLICY STATEMENT
All non-privileged user accounts MUST implement multi-factor authentication (MFA) using at least two different authentication factors. MFA requirements apply to all access methods including local, network, and remote access to company systems and applications.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Non-privileged user accounts | YES | All standard employee and contractor accounts |
| Service accounts | NO | Covered under separate privileged access policies |
| Guest accounts | YES | When guest access is permitted |
| Application accounts | YES | User-facing applications requiring authentication |
| System accounts | NO | Technical system-to-system accounts excluded |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Configure and maintain MFA systems<br>• Monitor MFA compliance<br>• Approve MFA exceptions |
| System Administrators | • Implement MFA on all applicable systems<br>• Ensure MFA integration with identity providers<br>• Report MFA failures |
| Account Managers | • Verify MFA enrollment for new accounts<br>• Disable accounts with non-compliant MFA<br>• Process MFA reset requests |

## 4. RULES
[RULE-01] All non-privileged accounts MUST implement multi-factor authentication using at least two different authentication factors from: something you know (password/PIN), something you have (token/smart card), or something you are (biometric).
[VALIDATION] IF account_type = "non-privileged" AND mfa_factors_count < 2 THEN violation

[RULE-02] MFA MUST be required for all access methods including local system access, network access, and remote access.
[VALIDATION] IF access_method IN ["local", "network", "remote"] AND mfa_enabled = FALSE THEN violation

[RULE-03] Hardware authenticators SHALL be preferred for high-risk environments and MAY include time-based tokens, challenge-response devices, or smart cards.
[VALIDATION] IF risk_level = "high" AND authenticator_type != "hardware" AND exception_approved = FALSE THEN violation

[RULE-04] MFA bypass or temporary disabling MUST be approved by IT Security and documented with business justification and expiration date not exceeding 72 hours.
[VALIDATION] IF mfa_bypass = TRUE AND (approval_date = NULL OR expiration_date > current_date + 72_hours) THEN violation

[RULE-05] Users MUST enroll in MFA within 5 business days of account creation and complete MFA setup before gaining system access.
[VALIDATION] IF account_age > 5_business_days AND mfa_enrolled = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] MFA Enrollment Process - Standardized user enrollment and device registration
- [PROC-02] MFA Exception Management - Approval workflow for temporary MFA bypass
- [PROC-03] MFA Incident Response - Response procedures for MFA failures and compromises
- [PROC-04] Authentication Factor Management - Provisioning and lifecycle management of MFA devices

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving authentication, technology changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Employee Login]
IF account_type = "non-privileged"
AND access_method = "remote"
AND mfa_factors_configured >= 2
THEN compliance = TRUE

[SCENARIO-02: Contractor Without MFA]
IF user_type = "contractor"
AND account_type = "non-privileged"
AND mfa_enabled = FALSE
AND account_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Emergency MFA Bypass]
IF mfa_bypass = TRUE
AND emergency_justification = "documented"
AND approval_date = current_date
AND expiration_date <= current_date + 72_hours
THEN compliance = TRUE

[SCENARIO-04: Application Access Without MFA]
IF application_type = "business_application"
AND user_account = "non-privileged"
AND mfa_required = FALSE
AND risk_classification != "low"
THEN compliance = FALSE
violation_severity = "Medium"

[SCENARIO-05: New Account Past Enrollment Deadline]
IF account_creation_date < current_date - 5_business_days
AND mfa_enrolled = FALSE
AND account_status = "active"
THEN compliance = FALSE
violation_severity = "Medium"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Multi-factor authentication for non-privileged accounts implemented | RULE-01, RULE-02 |
| Authentication factors properly configured | RULE-01, RULE-03 |
| MFA bypass controls implemented | RULE-04 |
| Timely MFA enrollment enforced | RULE-05 |
```