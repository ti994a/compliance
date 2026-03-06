# POLICY: IA-5.13: Expiration of Cached Authenticators

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5.13 |
| NIST Control | IA-5.13: Expiration of Cached Authenticators |
| Version | 1.0 |
| Owner | Identity and Access Management Team |
| Keywords | cached authenticators, authentication, expiration, offline access, credential management |

## 1. POLICY STATEMENT
The organization SHALL prohibit the use of cached authenticators after a defined time period to ensure authentication validity when network connectivity is restored. Cached authentication information MUST be automatically expired to prevent the use of potentially compromised or outdated credentials for local machine access.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All workstations and laptops | YES | Including domain-joined and hybrid devices |
| Mobile devices with cached credentials | YES | Corporate-managed devices only |
| Servers with cached authentication | YES | Including terminal servers and jump hosts |
| Kiosks and shared workstations | YES | Public-facing and shared access points |
| Personal devices (BYOD) | CONDITIONAL | Only if accessing corporate cached credentials |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity and Access Management Team | • Define cached authenticator expiration policies<br>• Configure domain and system-level cache settings<br>• Monitor compliance with expiration requirements |
| System Administrators | • Implement cache expiration settings on managed systems<br>• Validate proper configuration of authentication caching<br>• Report cache-related authentication issues |
| Security Operations Center | • Monitor for expired cache usage attempts<br>• Investigate authentication anomalies related to cached credentials<br>• Escalate policy violations |

## 4. RULES
[RULE-01] Cached authenticators on domain-joined Windows systems MUST expire after 10 days of no network connectivity to the domain controller.
[VALIDATION] IF system_type = "windows_domain" AND last_domain_contact > 10_days AND cached_auth_used = TRUE THEN violation

[RULE-02] Cached authenticators on macOS systems bound to Active Directory MUST expire after 14 days of no network connectivity.
[VALIDATION] IF system_type = "macos_ad_bound" AND last_ad_contact > 14_days AND cached_auth_used = TRUE THEN violation

[RULE-03] Linux systems with cached LDAP credentials MUST expire cached authenticators after 7 days of no LDAP server connectivity.
[VALIDATION] IF system_type = "linux_ldap" AND last_ldap_contact > 7_days AND cached_auth_used = TRUE THEN violation

[RULE-04] Mobile device management systems MUST enforce cached credential expiration within 24 hours for high-privilege accounts.
[VALIDATION] IF account_privilege = "high" AND device_type = "mobile" AND cached_credential_age > 24_hours THEN critical_violation

[RULE-05] Systems MUST NOT allow cached authenticator usage if the cached credential was created more than 30 days ago, regardless of network connectivity status.
[VALIDATION] IF cached_credential_creation_date < (current_date - 30_days) AND cached_auth_used = TRUE THEN violation

[RULE-06] Privileged service accounts MUST NOT use cached authenticators under any circumstances.
[VALIDATION] IF account_type = "service" AND account_privilege = "privileged" AND cached_auth_used = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cache Expiration Configuration - Configure operating system and directory service cache expiration settings
- [PROC-02] Cache Monitoring and Alerting - Monitor systems for cached authenticator usage and expiration compliance
- [PROC-03] Emergency Cache Override - Document process for temporary cache extension during planned network outages
- [PROC-04] Cache Audit and Reporting - Regular assessment of cache configuration and usage patterns

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving cached credentials, major infrastructure changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Laptop Offline Extended Period]
IF device_type = "laptop"
AND last_network_contact > 10_days
AND user_attempts_cached_login = TRUE
AND cached_credential_age > 10_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Privileged Account Cache Usage]
IF account_privilege = "administrative"
AND authentication_method = "cached_credential"
AND network_available = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Mobile Device Cache Expiration]
IF device_type = "mobile"
AND cached_credential_age > 24_hours
AND account_privilege = "high"
AND cache_usage_attempted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Planned Network Maintenance]
IF network_outage = "planned"
AND cache_extension_documented = TRUE
AND extension_duration <= 72_hours
AND security_approval = TRUE
THEN compliance = TRUE

[SCENARIO-05: Stale Cache Beyond Maximum Age]
IF cached_credential_creation_date < (current_date - 30_days)
AND authentication_attempt = TRUE
AND cache_used = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cached authenticators prohibited after defined time period | RULE-01, RULE-02, RULE-03 |
| High-privilege account cache restrictions | RULE-04, RULE-06 |
| Maximum cache age enforcement | RULE-05 |
| Service account cache prohibition | RULE-06 |