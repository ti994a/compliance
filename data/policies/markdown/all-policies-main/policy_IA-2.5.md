# POLICY: IA-2.5: Individual Authentication with Group Authentication

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-2.5 |
| NIST Control | IA-2.5: Individual Authentication with Group Authentication |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | individual authentication, group authentication, shared accounts, authenticators, user identification |

## 1. POLICY STATEMENT
When shared accounts or authenticators are employed, users MUST be individually authenticated before granting access to the shared accounts or resources. This policy mitigates risks associated with group account usage by ensuring individual accountability and traceability.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Systems with shared accounts or authenticators |
| Cloud services | YES | Including SaaS, PaaS, IaaS platforms |
| Shared service accounts | YES | Administrative, application, and service accounts |
| Individual user accounts | NO | Only applies when shared resources are accessed |
| Guest/temporary accounts | YES | When shared among multiple users |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure systems to enforce individual authentication before shared access<br>• Monitor compliance with authentication requirements<br>• Maintain audit logs of authentication events |
| Identity Access Management Team | • Design and implement authentication workflows<br>• Manage shared account provisioning and access controls<br>• Ensure integration between individual and group authentication systems |
| Security Operations Center | • Monitor for unauthorized shared account access<br>• Investigate authentication bypass attempts<br>• Report compliance violations |

## 4. RULES
[RULE-01] Users MUST complete individual authentication using their unique credentials before accessing any shared account or authenticator.
[VALIDATION] IF shared_account_access = TRUE AND individual_auth_completed = FALSE THEN critical_violation

[RULE-02] Systems with shared accounts MUST implement technical controls that prevent direct access to shared resources without prior individual authentication.
[VALIDATION] IF system_has_shared_accounts = TRUE AND direct_access_possible = TRUE THEN violation

[RULE-03] All individual authentication events preceding shared account access MUST be logged with user identity, timestamp, and target shared resource.
[VALIDATION] IF shared_account_accessed = TRUE AND individual_auth_logged = FALSE THEN violation

[RULE-04] Shared authenticators (tokens, certificates, keys) MUST NOT be accessible until individual user identity is verified and authorized.
[VALIDATION] IF shared_authenticator_access = TRUE AND user_identity_verified = FALSE THEN critical_violation

[RULE-05] Emergency access procedures for shared accounts MUST include individual authentication requirements or documented compensating controls.
[VALIDATION] IF emergency_access = TRUE AND (individual_auth_required = FALSE AND compensating_controls = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Shared Account Access Workflow - Define step-by-step process for individual authentication before shared access
- [PROC-02] Authentication System Integration - Establish technical integration between individual and group authentication systems
- [PROC-03] Audit Log Review - Regular review of authentication logs for compliance verification
- [PROC-04] Emergency Access Authorization - Process for documented exceptions during emergency situations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving shared accounts, system architecture changes, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Shared Account Access]
IF user_requests_shared_account_access = TRUE
AND individual_authentication_completed = TRUE
AND user_authorized_for_shared_resource = TRUE
THEN compliance = TRUE

[SCENARIO-02: Direct Shared Account Login Attempt]
IF user_attempts_direct_shared_login = TRUE
AND individual_authentication_bypassed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Service Account with Individual Auth]
IF service_account_access_required = TRUE
AND individual_user_authenticated = TRUE
AND access_logged_with_user_identity = TRUE
THEN compliance = TRUE

[SCENARIO-04: Emergency Access Without Individual Auth]
IF emergency_situation = TRUE
AND shared_account_accessed = TRUE
AND individual_authentication_completed = FALSE
AND compensating_controls_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Shared Authenticator Usage]
IF shared_token_requested = TRUE
AND requesting_user_individually_authenticated = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Users individually authenticated before shared account access | [RULE-01] |
| Technical controls prevent direct shared access | [RULE-02] |
| Authentication events logged with individual identity | [RULE-03] |
| Shared authenticators protected by individual verification | [RULE-04] |
| Emergency procedures include authentication requirements | [RULE-05] |