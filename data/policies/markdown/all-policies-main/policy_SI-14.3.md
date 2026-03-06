# POLICY: SI-14.3: Non-persistent Connectivity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-14.3 |
| NIST Control | SI-14.3: Non-persistent Connectivity |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | non-persistent, connectivity, on-demand, connection termination, lateral movement, adversary prevention |

## 1. POLICY STATEMENT
All system connections MUST be established only on demand and automatically terminated upon completion of each request. Persistent connections are prohibited unless explicitly authorized and documented as business-critical exceptions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid |
| Network connections | YES | Internal and external connections |
| Administrative connections | YES | Privileged access sessions included |
| Application connections | YES | Database, API, and service connections |
| Vendor/partner connections | YES | Third-party system integrations |
| Development/test systems | CONDITIONAL | Must follow same rules unless isolated |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure systems for non-persistent connectivity<br>• Monitor connection patterns and duration<br>• Implement automatic termination mechanisms |
| Network Security Team | • Design network architecture supporting on-demand connections<br>• Monitor for unauthorized persistent connections<br>• Validate connection termination procedures |
| Application Owners | • Ensure applications establish connections only when needed<br>• Implement proper connection pooling and cleanup<br>• Document any business-critical persistent connection requirements |

## 4. RULES
[RULE-01] System connections MUST be established only when a specific request or transaction requires access.
[VALIDATION] IF connection_established = TRUE AND active_request = FALSE THEN violation

[RULE-02] All connections MUST be automatically terminated within 5 minutes of request completion or session inactivity.
[VALIDATION] IF connection_duration > 5_minutes AND request_status = "completed" THEN violation

[RULE-03] Persistent connections SHALL NOT be maintained unless documented as business-critical exceptions with CISO approval.
[VALIDATION] IF connection_type = "persistent" AND exception_approved = FALSE THEN critical_violation

[RULE-04] Connection establishment mechanisms MUST include automated monitoring and logging of connection duration and purpose.
[VALIDATION] IF connection_logged = FALSE OR duration_monitored = FALSE THEN violation

[RULE-05] Systems MUST implement connection pooling with automatic cleanup rather than maintaining individual persistent connections.
[VALIDATION] IF connection_pooling = FALSE AND connection_count > threshold THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Connection Monitoring - Continuous monitoring of connection establishment and termination
- [PROC-02] Exception Management - Process for requesting and approving persistent connection exceptions
- [PROC-03] Automated Termination - Implementation of automatic connection cleanup mechanisms
- [PROC-04] Connection Auditing - Regular review of connection patterns and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving lateral movement, new system deployments, architecture changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Database Connection Pool]
IF connection_type = "database"
AND pooling_enabled = TRUE
AND idle_timeout <= 300_seconds
THEN compliance = TRUE

[SCENARIO-02: Administrative SSH Session]
IF connection_type = "SSH"
AND session_purpose = "administrative"
AND auto_logout > 300_seconds
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: API Integration]
IF connection_type = "API"
AND connection_persistent = TRUE
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Approved Exception]
IF connection_persistent = TRUE
AND ciso_approval = TRUE
AND business_justification = "documented"
AND review_date <= current_date
THEN compliance = TRUE

[SCENARIO-05: Vendor Connection]
IF connection_source = "external_vendor"
AND connection_duration > 600_seconds
AND active_transaction = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Connections established on demand | [RULE-01] |
| Connections terminated after completion | [RULE-02] |
| Persistent connection controls | [RULE-03] |
| Connection monitoring and logging | [RULE-04] |
| Automated connection management | [RULE-05] |