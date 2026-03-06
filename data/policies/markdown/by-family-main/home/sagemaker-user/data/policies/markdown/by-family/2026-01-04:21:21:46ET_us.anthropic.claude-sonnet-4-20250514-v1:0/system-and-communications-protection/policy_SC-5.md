```markdown
# POLICY: SC-5: Denial-of-Service Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-5 |
| NIST Control | SC-5: Denial-of-Service Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | denial-of-service, DoS, DDoS, availability, network protection, boundary protection, capacity planning |

## 1. POLICY STATEMENT
The organization SHALL protect information systems against denial-of-service (DoS) attacks by implementing appropriate safeguards and controls. Systems MUST maintain availability during DoS events through defined protection mechanisms and capacity management.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and on-premises |
| Network infrastructure | YES | Routers, switches, firewalls, load balancers |
| Internet-facing services | YES | Web applications, APIs, email systems |
| Internal networks | YES | Protection from internal DoS sources |
| Third-party services | CONDITIONAL | Where organization has control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Implement DoS protection controls<br>• Monitor network traffic patterns<br>• Configure boundary protection devices |
| System Administrators | • Maintain system capacity and performance<br>• Implement system-level DoS protections<br>• Monitor resource utilization |
| Incident Response Team | • Respond to active DoS attacks<br>• Coordinate DoS mitigation efforts<br>• Document DoS incidents |

## 4. RULES
[RULE-01] Organizations MUST define specific types of denial-of-service events that systems are protected against, including volumetric, protocol, and application-layer attacks.
[VALIDATION] IF dos_event_types_documented = FALSE THEN violation

[RULE-02] Organizations MUST implement boundary protection devices that filter malicious packets to prevent DoS attacks from reaching internal systems.
[VALIDATION] IF boundary_protection_deployed = FALSE OR packet_filtering_enabled = FALSE THEN violation

[RULE-03] Systems MUST employ network capacity and bandwidth management controls sufficient to handle expected traffic loads plus a minimum 50% overhead for DoS resilience.
[VALIDATION] IF current_capacity < (expected_load * 1.5) THEN violation

[RULE-04] Internet-facing systems MUST implement rate limiting controls to prevent resource exhaustion from excessive requests.
[VALIDATION] IF internet_facing = TRUE AND rate_limiting_enabled = FALSE THEN violation

[RULE-05] Organizations MUST maintain service redundancy for critical systems to ensure availability during DoS events.
[VALIDATION] IF system_criticality = "high" AND redundancy_implemented = FALSE THEN violation

[RULE-06] DoS protection mechanisms MUST be tested quarterly through simulated attacks or load testing.
[VALIDATION] IF last_dos_test_date > 90_days THEN violation

[RULE-07] Systems MUST log and monitor for indicators of DoS attacks including traffic volume anomalies and connection patterns.
[VALIDATION] IF dos_monitoring_enabled = FALSE OR logging_configured = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DoS Event Type Assessment - Annual review and documentation of DoS threats
- [PROC-02] Capacity Planning - Quarterly assessment of network and system capacity
- [PROC-03] DoS Response Procedures - Incident response plan for active DoS attacks
- [PROC-04] Protection Control Testing - Quarterly validation of DoS protection mechanisms

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major DoS incidents, infrastructure changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: Volumetric Attack Protection]
IF attack_type = "volumetric"
AND traffic_volume > baseline_threshold * 10
AND mitigation_activated = TRUE
AND service_availability > 95%
THEN compliance = TRUE

[SCENARIO-02: Unprotected Internet Service]
IF system_internet_facing = TRUE
AND rate_limiting_enabled = FALSE
AND boundary_protection = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Insufficient Capacity Planning]
IF system_criticality = "high"
AND current_capacity < expected_load * 1.5
AND capacity_review_date > 90_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing DoS Testing]
IF last_dos_test_date > 90_days
AND system_internet_facing = TRUE
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Internal DoS Source]
IF dos_source = "internal"
AND internal_rate_limiting = FALSE
AND network_segmentation = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| DoS event types are defined | RULE-01 |
| Effects of DoS events are protected against | RULE-02, RULE-04, RULE-05 |
| Controls achieve DoS protection objective | RULE-03, RULE-06, RULE-07 |
| Boundary protection implementation | RULE-02 |
| Service availability maintenance | RULE-03, RULE-05 |
```