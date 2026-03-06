# POLICY: SC-5: Denial-of-service Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-5 |
| NIST Control | SC-5: Denial-of-service Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | denial-of-service, DoS, DDoS, availability, network protection, bandwidth, capacity |

## 1. POLICY STATEMENT
The organization SHALL protect information systems against denial-of-service (DoS) attacks by implementing appropriate safeguards and controls. Systems MUST maintain availability during and after DoS events through defined protection mechanisms and capacity planning.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, hybrid, and on-premises |
| Network infrastructure | YES | Routers, switches, firewalls, load balancers |
| External-facing services | YES | Web applications, APIs, email systems |
| Internal-only systems | CONDITIONAL | Based on criticality assessment |
| Third-party services | YES | Where contractually controllable |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve DoS protection strategy<br>• Ensure adequate budget for protection mechanisms<br>• Review effectiveness quarterly |
| Network Security Team | • Implement and maintain DoS protection controls<br>• Monitor for DoS attacks<br>• Tune protection mechanisms |
| System Administrators | • Configure system-level DoS protections<br>• Monitor system capacity and performance<br>• Implement rate limiting and throttling |
| Incident Response Team | • Respond to active DoS attacks<br>• Coordinate mitigation efforts<br>• Document lessons learned |

## 4. RULES
[RULE-01] All external-facing systems MUST implement at least two different types of DoS protection mechanisms.
[VALIDATION] IF system_external_facing = TRUE AND dos_protection_count < 2 THEN violation

[RULE-02] DoS protection mechanisms MUST be tested quarterly through simulated attacks or penetration testing.
[VALIDATION] IF last_dos_test_date > 90_days AND system_criticality >= "High" THEN violation

[RULE-03] Network capacity MUST be monitored continuously with alerts triggered at 80% utilization.
[VALIDATION] IF network_monitoring = FALSE OR alert_threshold > 80 THEN violation

[RULE-04] Rate limiting MUST be implemented on all public APIs with maximum requests per minute defined based on service capacity.
[VALIDATION] IF api_public = TRUE AND rate_limiting = FALSE THEN violation

[RULE-05] DoS incident response procedures MUST be activated within 15 minutes of attack detection for critical systems.
[VALIDATION] IF system_criticality = "Critical" AND response_time > 15_minutes THEN critical_violation

[RULE-06] Bandwidth capacity MUST exceed normal usage by at least 50% to absorb volumetric attacks.
[VALIDATION] IF available_bandwidth < (normal_usage * 1.5) THEN violation

[RULE-07] All DoS protection mechanisms MUST log attack attempts and mitigation actions for forensic analysis.
[VALIDATION] IF dos_logging = FALSE OR log_retention < 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DoS Risk Assessment - Annual assessment of DoS threats and vulnerabilities
- [PROC-02] Protection Mechanism Testing - Quarterly testing of all DoS protections
- [PROC-03] Capacity Planning - Semi-annual review of bandwidth and system capacity
- [PROC-04] Incident Response - Procedures for detecting and responding to DoS attacks
- [PROC-05] Vendor Coordination - Coordination with ISP and cloud providers during attacks

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major DoS attacks, infrastructure changes, new threat intelligence, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical System Without Protection]
IF system_criticality = "Critical"
AND external_facing = TRUE
AND dos_protection_mechanisms = 0
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Untested Protection Mechanisms]
IF dos_protection_implemented = TRUE
AND last_test_date > 90_days
AND system_criticality >= "High"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: API Without Rate Limiting]
IF service_type = "Public API"
AND rate_limiting = FALSE
AND traffic_volume = "High"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Adequate Multi-Layer Protection]
IF dos_protection_count >= 2
AND testing_current = TRUE
AND monitoring_enabled = TRUE
AND capacity_adequate = TRUE
THEN compliance = TRUE

[SCENARIO-05: Slow Incident Response]
IF dos_attack_detected = TRUE
AND system_criticality = "Critical"
AND response_time > 15_minutes
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| DoS protection mechanisms implemented | RULE-01, RULE-04 |
| Protection effectiveness verified | RULE-02 |
| Capacity management implemented | RULE-03, RULE-06 |
| Incident response capabilities | RULE-05 |
| Audit and monitoring controls | RULE-07 |