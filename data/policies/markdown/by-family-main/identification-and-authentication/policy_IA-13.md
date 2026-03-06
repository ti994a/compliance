# POLICY: IA-13: Identity Providers and Authorization Servers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-13 |
| NIST Control | IA-13: Identity Providers and Authorization Servers |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | identity providers, authorization servers, SSO, authentication, authorization, NPE, access tokens |

## 1. POLICY STATEMENT
The organization SHALL employ identity providers and authorization servers to manage user, device, and non-person entity (NPE) identities, attributes, and access rights. These systems MUST support authentication and authorization decisions in accordance with organizational identification and authentication policies using approved mechanisms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Identity Providers | YES | All organizational IdP systems |
| External Identity Providers | YES | Federated and third-party IdP services |
| Authorization Servers | YES | OAuth, SAML, and similar services |
| Users | YES | All human users requiring system access |
| Devices | YES | All organizational and BYOD devices |
| Non-Person Entities | YES | Service accounts, APIs, automated systems |
| Guest Networks | CONDITIONAL | Only if integrated with organizational IdP |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity and Access Management Team | • Implement and maintain identity providers<br>• Configure authorization servers<br>• Monitor authentication/authorization events |
| System Administrators | • Integrate systems with approved IdP/AuthZ servers<br>• Maintain system-level authentication configurations<br>• Report integration issues |
| Security Operations Center | • Monitor identity provider security events<br>• Investigate authentication anomalies<br>• Respond to identity-related incidents |

## 4. RULES

[RULE-01] All user authentication MUST be processed through approved identity providers that manage user identities, attributes, and access rights.
[VALIDATION] IF authentication_method != "approved_idp" THEN violation

[RULE-02] Device authentication MUST utilize organizational identity providers or approved device identity management systems.
[VALIDATION] IF device_auth = TRUE AND idp_managed = FALSE AND approved_exception = FALSE THEN violation

[RULE-03] Non-person entity (NPE) identities SHALL be managed through designated identity providers with appropriate attribute and access right controls.
[VALIDATION] IF entity_type = "NPE" AND idp_managed = FALSE THEN violation

[RULE-04] Authorization servers MUST issue access tokens only after successful identity verification through approved identity providers.
[VALIDATION] IF access_token_issued = TRUE AND identity_verified = FALSE THEN critical_violation

[RULE-05] Identity providers MUST maintain current user, device, and NPE attributes required for access control decisions.
[VALIDATION] IF attribute_staleness > 24_hours AND access_granted = TRUE THEN violation

[RULE-06] Single Sign-On (SSO) implementations MUST integrate both identity provider and authorization server functions in accordance with organizational security requirements.
[VALIDATION] IF sso_deployed = TRUE AND (idp_compliant = FALSE OR authz_compliant = FALSE) THEN violation

[RULE-07] External identity providers MUST meet organizational security standards and maintain current federation agreements.
[VALIDATION] IF external_idp = TRUE AND (security_assessment_current = FALSE OR federation_agreement_valid = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Identity Provider Configuration - Standardized setup and security hardening of IdP systems
- [PROC-02] Authorization Server Deployment - Implementation and integration of authorization servers
- [PROC-03] External IdP Integration - Vetting and onboarding of external identity providers
- [PROC-04] NPE Identity Management - Lifecycle management for non-person entity identities
- [PROC-05] Access Token Management - Issuance, validation, and revocation of access tokens

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving identity systems, new IdP deployments, federation changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Direct Database Authentication]
IF authentication_method = "direct_database"
AND approved_idp_available = TRUE
AND legacy_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unmanaged Service Account]
IF entity_type = "service_account"
AND idp_managed = FALSE
AND local_account = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Expired External IdP Agreement]
IF external_idp = TRUE
AND federation_agreement_expired = TRUE
AND active_users > 0
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Token Issued Without Verification]
IF access_token_issued = TRUE
AND identity_verification_bypassed = TRUE
AND emergency_access = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Compliant SSO Implementation]
IF sso_enabled = TRUE
AND idp_approved = TRUE
AND authz_server_compliant = TRUE
AND security_controls_active = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Identity providers manage user identities for authentication decisions | RULE-01, RULE-05 |
| Identity providers manage device identities for authentication decisions | RULE-02, RULE-05 |
| Identity providers manage NPE identities for authentication decisions | RULE-03, RULE-05 |
| Identity providers manage user identities for authorization decisions | RULE-01, RULE-05 |
| Identity providers manage device identities for authorization decisions | RULE-02, RULE-05 |
| Identity providers manage NPE identities for authorization decisions | RULE-03, RULE-05 |
| Authorization servers manage user identities for authentication decisions | RULE-04, RULE-06 |
| Authorization servers manage device identities for authentication decisions | RULE-04, RULE-06 |
| Authorization servers manage NPE identities for authentication decisions | RULE-04, RULE-06 |
| Authorization servers manage user identities for authorization decisions | RULE-04, RULE-06 |
| Authorization servers manage device identities for authorization decisions | RULE-04, RULE-06 |
| Authorization servers manage NPE identities for authorization decisions | RULE-04, RULE-06 |