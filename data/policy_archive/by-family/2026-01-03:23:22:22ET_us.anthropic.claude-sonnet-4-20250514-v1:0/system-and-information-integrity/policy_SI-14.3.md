# POLICY: SI-14.3: Non-persistent Connectivity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-14.3 |
| NIST Control | SI-14.3: Non-persistent Connectivity |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | non-persistent, connectivity, on-demand, connection termination, lateral movement, adversary |

## 1. POLICY STATEMENT
All system connections MUST be established on-demand only when required and automatically terminated upon completion of each request. Persistent connections that enable lateral movement through organizational systems are prohibited unless explicitly documented and approved through the exception process.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All internet-facing and internal systems |
| Development Systems | YES | Systems containing sensitive data |
| Network Infrastructure | YES | Routers, switches, firewalls |
| Cloud Services | YES | All hybrid and multi-cloud connections |
| Third-party Integrations | YES | API connections and data feeds |
| Administrative Workstations | CONDITIONAL | Only when accessing production systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure connection timeout policies<br>• Monitor connection patterns<br>• Implement automated termination controls |
| System Administrators | • Deploy non-persistent connection mechanisms<br>• Document approved persistent connections<br>• Maintain connection logs |
| Security Operations Center | • Monitor for unauthorized persistent connections<br>• Investigate connection anomalies<br>• Escalate policy violations |

## 4. RULES

[RULE-01] System connections MUST be established only on-demand when a specific request or transaction requires access.
[VALIDATION] IF connection_type = "automatic" OR connection_trigger ≠ "user_request" THEN violation

[RULE-02] All connections MUST be automatically terminated within 15 minutes of request completion or user inactivity.
[VALIDATION] IF connection_duration > 15_minutes AND request_status = "completed" THEN violation

[RULE-03] Persistent connections SHALL NOT be maintained unless documented in the approved exceptions list and reviewed monthly.
[VALIDATION] IF connection_persistent = TRUE AND exception_approved = FALSE THEN critical_violation

[RULE-04] Administrative connections to production systems MUST terminate within 5 minutes of inactivity.
[VALIDATION] IF connection_type = "administrative" AND idle_time > 5_minutes AND connection_active = TRUE THEN violation

[RULE-05] Cross-network zone connections MUST implement automatic session termination and SHALL NOT persist beyond single transaction scope.
[VALIDATION] IF source_zone ≠ destination_zone AND session_scope = "multi-transaction" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Connection Monitoring - Real-time monitoring of all system connections for duration and persistence
- [PROC-02] Exception Management - Process for documenting and approving necessary persistent connections
- [PROC-03] Automated Termination - Implementation of technical controls for automatic connection termination
- [PROC-04] Incident Response - Response procedures for unauthorized persistent connections

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving lateral movement, infrastructure changes, new system deployments

## 7. SCENARIO PATTERNS

[SCENARIO-01: API Connection Timeout]
IF connection_type = "API"
AND last_request_time > 15_minutes_ago
AND connection_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Administrative Session Persistence]
IF user_role = "administrator"
AND target_system = "production"
AND idle_time > 5_minutes
AND session_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Cross-Zone Persistent Connection]
IF source_network_zone = "DMZ"
AND destination_network_zone = "internal"
AND connection_duration > 30_minutes
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Approved Exception Usage]
IF connection_persistent = TRUE
AND exception_approved = TRUE
AND exception_review_date < 30_days_ago
THEN compliance = TRUE

[SCENARIO-05: On-Demand Connection Establishment]
IF connection_trigger = "user_request"
AND connection_established_time = request_time
AND connection_duration < 15_minutes
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Connections established on demand | [RULE-01] |
| Connections terminated after request completion | [RULE-02], [RULE-04] |
| Prevention of persistent connections | [RULE-03], [RULE-05] |
| Administrative access controls | [RULE-04] |
| Cross-network zone restrictions | [RULE-05] |