# POLICY: SC-5.1: Restrict Ability to Attack Other Systems

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-5.1 |
| NIST Control | SC-5.1: Restrict Ability to Attack Other Systems |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | denial-of-service, DoS attacks, network protection, egress filtering, resource limits |

## 1. POLICY STATEMENT
The organization SHALL restrict the ability of individuals to launch denial-of-service (DoS) attacks against other systems from organizational networks and computing resources. This includes implementing technical controls to prevent both internal and compromised accounts from conducting outbound attacks that could impact external systems or services.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All network endpoints | YES | Includes workstations, servers, IoT devices |
| Cloud infrastructure | YES | AWS, Azure, hybrid environments |
| Remote access connections | YES | VPN, remote desktop sessions |
| Guest networks | YES | Visitor and contractor access |
| Development/test systems | YES | Including sandbox environments |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure egress filtering rules<br>• Monitor for DoS attack patterns<br>• Implement bandwidth limitations |
| System Administrators | • Configure host-based resource limits<br>• Deploy endpoint protection controls<br>• Monitor system resource usage |
| SOC Analysts | • Detect outbound attack traffic<br>• Investigate DoS-related incidents<br>• Coordinate incident response |

## 4. RULES
[RULE-01] Network egress filtering MUST be implemented to block traffic patterns commonly associated with denial-of-service attacks, including SYN floods, UDP floods, and ICMP floods.
[VALIDATION] IF egress_filtering_enabled = FALSE OR blocked_attack_patterns < required_patterns THEN violation

[RULE-02] Per-user and per-system bandwidth limitations MUST be enforced to prevent excessive resource consumption that could be used for DoS attacks.
[VALIDATION] IF bandwidth_limits_configured = FALSE OR max_bandwidth > approved_threshold THEN violation

[RULE-03] Systems MUST implement rate limiting for outbound connections to prevent connection flooding attacks against external targets.
[VALIDATION] IF rate_limiting_enabled = FALSE OR connection_rate > max_allowed_rate THEN violation

[RULE-04] Network monitoring MUST detect and alert on traffic patterns indicative of outbound DoS attacks within 5 minutes of detection.
[VALIDATION] IF monitoring_enabled = FALSE OR alert_delay > 5_minutes THEN violation

[RULE-05] Compromised or suspicious accounts MUST have network access restricted within 15 minutes of identification to prevent DoS attack launches.
[VALIDATION] IF account_status = "compromised" AND network_restriction_time > 15_minutes THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DoS Attack Prevention Configuration - Standard configurations for network and host-based DoS prevention controls
- [PROC-02] Outbound Traffic Monitoring - Procedures for detecting and responding to suspicious egress traffic
- [PROC-03] Incident Response for DoS Events - Response procedures when DoS attacks are detected or suspected
- [PROC-04] Resource Limit Management - Process for setting and maintaining appropriate system resource limits

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving DoS attacks, major network architecture changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: Employee Workstation Compromise]
IF user_account = "compromised"
AND outbound_traffic_volume > normal_baseline * 10
AND egress_filtering = "bypassed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Development System Attack Launch]
IF system_type = "development"
AND connection_rate > 1000_per_second
AND rate_limiting = "disabled"
AND target_systems = "external"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Proper DoS Prevention]
IF egress_filtering = "enabled"
AND bandwidth_limits = "configured"
AND monitoring_alerts = "active"
AND rate_limiting = "enforced"
THEN compliance = TRUE

[SCENARIO-04: Guest Network Attack Attempt]
IF network_segment = "guest"
AND attack_pattern_detected = TRUE
AND blocking_action_time > 5_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Cloud Instance Misconfiguration]
IF cloud_instance = "production"
AND security_groups = "unrestricted_egress"
AND DoS_prevention_controls = "not_implemented"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Restrict ability to launch DoS attacks against other systems | [RULE-01], [RULE-02], [RULE-03] |
| Monitor for DoS attack patterns | [RULE-04] |
| Respond to compromised accounts used for attacks | [RULE-05] |