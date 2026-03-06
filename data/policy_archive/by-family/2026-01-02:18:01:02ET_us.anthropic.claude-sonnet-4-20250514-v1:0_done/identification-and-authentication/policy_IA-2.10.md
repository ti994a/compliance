# POLICY: IA-2.10: Single Sign-on

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-2.10 |
| NIST Control | IA-2.10: Single Sign-on |
| Version | 1.0 |
| Owner | Identity and Access Management Team |
| Keywords | single sign-on, SSO, authentication, system accounts, services, multi-factor authentication |

## 1. POLICY STATEMENT
The organization SHALL implement single sign-on (SSO) capability for designated system accounts and services to enable users to authenticate once and access multiple authorized resources. SSO implementation MUST maintain security controls while providing operational efficiency and SHALL support multi-factor authentication integration where technically feasible.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Enterprise Applications | YES | All applications supporting SSO protocols |
| System Service Accounts | YES | Automated service-to-service authentication |
| Cloud Services | YES | SaaS, PaaS, IaaS platforms |
| Legacy Systems | CONDITIONAL | If SSO integration is technically feasible |
| Privileged Admin Accounts | YES | Administrative access to multiple systems |
| Contractor/Vendor Access | YES | External users requiring multi-system access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IAM Team | • Define SSO requirements and standards<br>• Implement and maintain SSO infrastructure<br>• Monitor SSO authentication events |
| System Owners | • Identify systems requiring SSO capability<br>• Integrate applications with SSO infrastructure<br>• Validate SSO functionality during testing |
| Security Team | • Review SSO security configurations<br>• Assess SSO-related risks<br>• Monitor for SSO authentication anomalies |

## 4. RULES
[RULE-01] Organizations MUST define and document which system accounts and services require single sign-on capability based on operational efficiency and security requirements.
[VALIDATION] IF system_requires_sso = TRUE AND sso_requirement_documented = FALSE THEN violation

[RULE-02] SSO solutions MUST support integration with multi-factor authentication (MFA) for enhanced security across connected systems.
[VALIDATION] IF sso_deployed = TRUE AND mfa_integration_supported = FALSE THEN violation

[RULE-03] SSO authentication events MUST be logged and monitored across all integrated systems and services.
[VALIDATION] IF sso_enabled = TRUE AND authentication_logging = FALSE THEN violation

[RULE-04] SSO session management MUST enforce appropriate timeout policies and session termination across all connected systems.
[VALIDATION] IF sso_session_active = TRUE AND session_timeout_configured = FALSE THEN violation

[RULE-05] SSO implementations MUST use industry-standard protocols (SAML 2.0, OAuth 2.0, OpenID Connect) and maintain secure configurations.
[VALIDATION] IF sso_protocol NOT IN ["SAML2.0", "OAuth2.0", "OpenIDConnect"] THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SSO Requirements Assessment - Evaluate systems and services for SSO capability requirements
- [PROC-02] SSO Implementation Standards - Technical standards for SSO deployment and configuration
- [PROC-03] SSO Monitoring and Incident Response - Procedures for monitoring SSO events and responding to anomalies
- [PROC-04] SSO Integration Testing - Validation procedures for new system SSO integrations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployments, SSO technology changes, security incidents involving authentication

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Application SSO Integration]
IF application_type = "enterprise"
AND user_count > 50
AND sso_integration_available = TRUE
AND sso_not_implemented = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Service Account SSO Usage]
IF account_type = "service"
AND multi_system_access = TRUE
AND sso_capability_available = TRUE
AND individual_credentials_used = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: SSO Without MFA Integration]
IF sso_implemented = TRUE
AND mfa_integration_possible = TRUE
AND mfa_not_configured = TRUE
AND system_sensitivity = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Legacy System SSO Exemption]
IF system_type = "legacy"
AND sso_technical_feasibility = FALSE
AND exemption_documented = TRUE
AND compensating_controls = TRUE
THEN compliance = TRUE

[SCENARIO-05: SSO Session Management Failure]
IF sso_session_active = TRUE
AND user_inactive_time > max_session_timeout
AND session_not_terminated = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Single sign-on capability provided for defined accounts and services | [RULE-01] |
| SSO implementation maintains security controls | [RULE-02], [RULE-05] |
| SSO events are properly monitored and logged | [RULE-03] |
| SSO sessions are properly managed | [RULE-04] |