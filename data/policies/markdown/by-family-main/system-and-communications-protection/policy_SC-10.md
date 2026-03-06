# POLICY: SC-10: Network Disconnect

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-10 |
| NIST Control | SC-10: Network Disconnect |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network disconnect, session termination, inactivity timeout, communications session |

## 1. POLICY STATEMENT
All network connections associated with communications sessions MUST be automatically terminated either at the end of the session or after a defined period of inactivity. This applies to both internal and external network connections to prevent unauthorized access through abandoned sessions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All network-connected systems | YES | Including servers, workstations, mobile devices |
| Internal network connections | YES | LAN, WLAN, VPN connections |
| External network connections | YES | Internet-facing services, partner connections |
| Application-level sessions | YES | Web apps, databases, APIs |
| Operating system connections | YES | TCP/IP, socket connections |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Administrators | • Configure timeout settings on network infrastructure<br>• Monitor session termination logs<br>• Implement connection pooling controls |
| System Administrators | • Set OS-level timeout parameters<br>• Configure application session timeouts<br>• Validate automatic disconnect functionality |
| Security Operations | • Monitor for orphaned sessions<br>• Review timeout compliance reports<br>• Investigate session anomalies |

## 4. RULES
[RULE-01] All interactive user sessions MUST automatically terminate after 30 minutes of inactivity for standard users and 15 minutes for privileged users.
[VALIDATION] IF session_type = "interactive" AND user_privilege = "standard" AND inactivity_time > 30_minutes THEN violation
[VALIDATION] IF session_type = "interactive" AND user_privilege = "privileged" AND inactivity_time > 15_minutes THEN critical_violation

[RULE-02] Administrative and privileged access sessions MUST terminate immediately upon completion of the administrative task or after 15 minutes of inactivity, whichever occurs first.
[VALIDATION] IF session_type = "administrative" AND inactivity_time > 15_minutes THEN critical_violation

[RULE-03] External network connections MUST terminate after 8 hours of continuous connection or 10 minutes of inactivity for non-authenticated sessions.
[VALIDATION] IF connection_type = "external" AND authenticated = FALSE AND inactivity_time > 10_minutes THEN violation
[VALIDATION] IF connection_type = "external" AND session_duration > 8_hours THEN violation

[RULE-04] Application sessions MUST properly deallocate TCP/IP address and port pairs at the operating system level upon termination.
[VALIDATION] IF session_terminated = TRUE AND tcp_resources_deallocated = FALSE THEN violation

[RULE-05] Database connections MUST be returned to connection pools or terminated within 5 minutes of application session end.
[VALIDATION] IF application_session_ended = TRUE AND db_connection_active = TRUE AND time_elapsed > 5_minutes THEN violation

[RULE-06] VPN connections MUST terminate after 12 hours of continuous connection or 60 minutes of inactivity.
[VALIDATION] IF connection_type = "VPN" AND (session_duration > 12_hours OR inactivity_time > 60_minutes) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Session Timeout Configuration - Standardized timeout settings for all system types
- [PROC-02] Connection Monitoring - Automated monitoring of active sessions and connections
- [PROC-03] Resource Deallocation - Proper cleanup of network resources upon session termination
- [PROC-04] Timeout Exception Process - Documented process for systems requiring extended sessions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving session hijacking, changes to network architecture, new application deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Abandoned Administrative Session]
IF session_type = "administrative"
AND last_activity > 15_minutes_ago
AND session_status = "active"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Long-Running Database Connection]
IF connection_type = "database"
AND application_session_status = "terminated"
AND connection_active_time > 5_minutes_post_termination
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: External Unauthenticated Session]
IF connection_source = "external"
AND authentication_status = "unauthenticated"
AND inactivity_time = 12_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Proper VPN Termination]
IF connection_type = "VPN"
AND session_duration = 8_hours
AND inactivity_time = 30_minutes
AND auto_disconnect = TRUE
THEN compliance = TRUE

[SCENARIO-05: Resource Cleanup Failure]
IF session_terminated = TRUE
AND tcp_port_released = FALSE
AND ip_address_deallocated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Network connection termination at session end | [RULE-04] |
| Automatic termination after inactivity period | [RULE-01], [RULE-02], [RULE-03], [RULE-06] |
| Proper resource deallocation | [RULE-04], [RULE-05] |
| Defined inactivity timeouts | [RULE-01], [RULE-02], [RULE-03], [RULE-06] |