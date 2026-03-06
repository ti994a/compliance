# POLICY: SC-10: Network Disconnect

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-10 |
| NIST Control | SC-10: Network Disconnect |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network disconnect, session termination, inactivity timeout, communications session, TCP/IP |

## 1. POLICY STATEMENT
All network connections associated with communications sessions MUST be automatically terminated either at the end of the session or after defined periods of inactivity. This applies to both internal and external network connections to prevent unauthorized access through abandoned sessions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All network infrastructure | YES | Routers, switches, firewalls |
| Application servers | YES | Web, database, API servers |
| Workstations and laptops | YES | Corporate and BYOD devices |
| Mobile devices | YES | Smartphones, tablets |
| Cloud services | YES | SaaS, PaaS, IaaS connections |
| Guest networks | YES | Visitor and contractor access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Operations Center | • Configure timeout settings on network infrastructure<br>• Monitor session termination compliance<br>• Maintain network disconnect logs |
| System Administrators | • Implement application-level session timeouts<br>• Configure OS-level connection termination<br>• Test disconnect mechanisms regularly |
| Security Operations | • Define inactivity timeout periods by access type<br>• Monitor for policy violations<br>• Review disconnect audit logs |

## 4. RULES
[RULE-01] Network connections MUST be automatically terminated at the end of each communications session through proper session cleanup procedures.
[VALIDATION] IF session_status = "ended" AND network_connection_active = TRUE AND cleanup_time > 30_seconds THEN violation

[RULE-02] Network connections MUST be terminated after defined periods of inactivity based on connection type and risk level.
[VALIDATION] IF inactivity_duration > defined_timeout_period AND connection_active = TRUE THEN violation

[RULE-03] TCP/IP address and port pairs MUST be de-allocated at the operating system level when sessions terminate.
[VALIDATION] IF session_terminated = TRUE AND tcp_resources_deallocated = FALSE THEN violation

[RULE-04] Application-level networking assignments MUST be de-allocated when multiple application sessions share a single OS-level connection.
[VALIDATION] IF application_session_ended = TRUE AND shared_connection = TRUE AND app_resources_deallocated = FALSE THEN violation

[RULE-05] Inactivity timeout periods SHALL be established based on network access type and documented in security procedures.
[VALIDATION] IF access_type_defined = TRUE AND timeout_period_documented = FALSE THEN violation

[RULE-06] Administrative and privileged access connections MUST have inactivity timeouts not exceeding 15 minutes.
[VALIDATION] IF access_level = "administrative" AND timeout_period > 15_minutes THEN violation

[RULE-07] Standard user connections MUST have inactivity timeouts not exceeding 30 minutes for internal networks and 15 minutes for external access.
[VALIDATION] IF access_level = "standard" AND network_type = "internal" AND timeout_period > 30_minutes THEN violation
[VALIDATION] IF access_level = "standard" AND network_type = "external" AND timeout_period > 15_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Session Timeout Configuration - Define and implement timeout periods for different access types
- [PROC-02] Network Connection Monitoring - Continuous monitoring of active connections and termination events
- [PROC-03] Resource Deallocation - Procedures for proper cleanup of network resources upon session termination
- [PROC-04] Timeout Exception Management - Process for requesting and approving timeout extensions for specific use cases

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving session hijacking, changes to network architecture, new application deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Web Application Session Timeout]
IF user_activity = "inactive"
AND session_type = "web_application"
AND inactivity_duration > 30_minutes
AND connection_terminated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Administrative SSH Session]
IF access_type = "administrative"
AND protocol = "SSH"
AND inactivity_duration > 15_minutes
AND session_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Proper Session Cleanup]
IF session_ended = TRUE
AND tcp_resources_deallocated = TRUE
AND application_resources_cleaned = TRUE
AND cleanup_time <= 30_seconds
THEN compliance = TRUE

[SCENARIO-04: VPN Connection Timeout]
IF connection_type = "VPN"
AND network_access = "external"
AND user_type = "standard"
AND inactivity_duration > 15_minutes
AND connection_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Database Connection Pool]
IF connection_type = "database"
AND shared_connection = TRUE
AND application_session_ended = TRUE
AND app_level_cleanup = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Network connection terminated at session end | [RULE-01], [RULE-03] |
| Network connection terminated after inactivity period | [RULE-02], [RULE-06], [RULE-07] |
| Proper resource deallocation at OS level | [RULE-03] |
| Application-level resource cleanup | [RULE-04] |
| Defined inactivity periods by access type | [RULE-05] |