# POLICY: SC-10: Network Disconnect

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-10 |
| NIST Control | SC-10: Network Disconnect |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network disconnect, session termination, timeout, inactivity, communications session |

## 1. POLICY STATEMENT
All network connections associated with communications sessions MUST be automatically terminated either at the end of the session or after a defined period of inactivity. This applies to both internal and external network connections to prevent unauthorized access through abandoned sessions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All network systems | YES | Including servers, workstations, network devices |
| Internal networks | YES | Corporate LAN, VPN, wireless networks |
| External networks | YES | Internet-facing services, partner connections |
| Application sessions | YES | Web applications, databases, APIs |
| Administrative sessions | YES | Enhanced timeout requirements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure network timeout settings<br>• Monitor session termination compliance<br>• Maintain timeout policy exceptions |
| System Administrators | • Implement session timeouts on managed systems<br>• Configure operating system level disconnects<br>• Document timeout configurations |
| Application Owners | • Configure application-level session timeouts<br>• Ensure proper session cleanup<br>• Test timeout functionality |

## 4. RULES

[RULE-01] All interactive user sessions MUST terminate automatically after 30 minutes of inactivity for standard users and 15 minutes for privileged users.
[VALIDATION] IF session_type = "interactive" AND user_privilege = "standard" AND inactivity_time > 30_minutes THEN violation
[VALIDATION] IF session_type = "interactive" AND user_privilege = "privileged" AND inactivity_time > 15_minutes THEN critical_violation

[RULE-02] Network connections MUST be terminated at both the operating system level (TCP/IP) and application level when sessions end.
[VALIDATION] IF session_ended = TRUE AND (os_connection_active = TRUE OR app_connection_active = TRUE) THEN violation

[RULE-03] Administrative and privileged access sessions MUST NOT exceed 4 hours maximum duration regardless of activity level.
[VALIDATION] IF session_type = "administrative" AND session_duration > 4_hours THEN violation

[RULE-04] External network connections MUST terminate after 60 minutes of inactivity unless explicitly documented business justification exists.
[VALIDATION] IF connection_type = "external" AND inactivity_time > 60_minutes AND business_exception = FALSE THEN violation

[RULE-05] Systems MUST deallocate all networking resources including TCP/IP address pairs and port assignments upon session termination.
[VALIDATION] IF session_terminated = TRUE AND (tcp_resources_allocated = TRUE OR port_assignments_active = TRUE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Session Timeout Configuration - Standard procedures for configuring timeout values across different system types
- [PROC-02] Network Resource Deallocation - Process for ensuring complete cleanup of network resources
- [PROC-03] Timeout Exception Management - Process for documenting and approving timeout exceptions
- [PROC-04] Session Monitoring and Alerting - Procedures for monitoring session compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents involving session hijacking, new system deployments, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard User Web Session]
IF user_type = "standard_user"
AND session_type = "web_application" 
AND inactivity_time = 45_minutes
AND auto_logout = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Privileged Database Session]
IF user_privilege = "database_admin"
AND session_type = "database_connection"
AND inactivity_time = 20_minutes
AND session_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: External API Connection]
IF connection_type = "external_api"
AND inactivity_time = 90_minutes
AND business_exception = TRUE
AND exception_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Administrative Session Duration]
IF session_type = "administrative"
AND session_duration = 5_hours
AND user_activity = "continuous"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Resource Cleanup After Termination]
IF session_status = "terminated"
AND tcp_connections = 0
AND allocated_ports = 0
AND application_cleanup = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Network connections terminated at session end | [RULE-02], [RULE-05] |
| Connections terminated after inactivity period | [RULE-01], [RULE-04] |
| Operating system level deallocation | [RULE-02], [RULE-05] |
| Application level session cleanup | [RULE-02], [RULE-05] |
| Defined inactivity periods by access type | [RULE-01], [RULE-03], [RULE-04] |