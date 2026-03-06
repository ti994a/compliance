# POLICY: SC-5: Denial-of-Service Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-5 |
| NIST Control | SC-5: Denial-of-Service Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | denial-of-service, DoS, DDoS, availability, network protection, boundary protection, bandwidth, capacity planning |

## 1. POLICY STATEMENT
The organization SHALL protect information systems against denial-of-service (DoS) attacks by implementing appropriate safeguards and controls. Systems MUST maintain availability and performance during DoS events through proactive protection measures and capacity planning.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and on-premises |
| Network infrastructure | YES | Routers, switches, firewalls, load balancers |
| Internet-facing services | YES | Web applications, APIs, email servers |
| Internal applications | YES | Business-critical and high-impact systems |
| Third-party services | CONDITIONAL | When organization controls configuration |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve DoS protection strategy<br>• Oversee policy compliance<br>• Coordinate with incident response |
| Network Security Team | • Implement boundary protection controls<br>• Monitor for DoS attacks<br>• Maintain DDoS mitigation tools |
| System Administrators | • Configure system-level protections<br>• Monitor system performance<br>• Implement capacity planning |
| Security Operations Center | • Monitor for DoS indicators<br>• Initiate incident response procedures<br>• Coordinate attack mitigation |

## 4. RULES
[RULE-01] Organizations MUST define and document specific types of denial-of-service events against which systems will be protected.
[VALIDATION] IF dos_events_documented = FALSE THEN violation

[RULE-02] Boundary protection devices MUST be configured to filter malicious traffic and limit DoS attack effects on internal networks.
[VALIDATION] IF boundary_device_dos_filtering = FALSE AND system_internet_facing = TRUE THEN violation

[RULE-03] Systems MUST implement rate limiting controls to prevent resource exhaustion from excessive requests.
[VALIDATION] IF rate_limiting_enabled = FALSE AND system_criticality IN ["HIGH", "MODERATE"] THEN violation

[RULE-04] Network capacity and bandwidth MUST be planned to accommodate expected traffic loads plus 25% overhead for high-impact systems.
[VALIDATION] IF capacity_planning_overhead < 0.25 AND system_impact = "HIGH" THEN violation

[RULE-05] DoS protection controls MUST be tested annually and after significant infrastructure changes.
[VALIDATION] IF dos_testing_date > 365_days_ago OR infrastructure_change_date > dos_testing_date THEN violation

[RULE-06] Redundant services MUST be implemented for business-critical applications to maintain availability during DoS events.
[VALIDATION] IF service_redundancy = FALSE AND business_criticality = "CRITICAL" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DoS Event Classification - Categorize and prioritize different types of DoS attacks
- [PROC-02] Capacity Planning Assessment - Regular evaluation of system capacity requirements
- [PROC-03] DoS Protection Testing - Annual testing of DoS mitigation controls
- [PROC-04] Incident Response Coordination - Integration with IR procedures for DoS events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major DoS incidents, infrastructure changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unprotected Internet-Facing System]
IF system_internet_facing = TRUE
AND boundary_protection_configured = FALSE
AND dos_controls_implemented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Insufficient Capacity Planning]
IF system_impact = "HIGH"
AND current_utilization > 0.80
AND capacity_planning_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Rate Limiting on API]
IF service_type = "API"
AND public_access = TRUE
AND rate_limiting_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Untested DoS Controls]
IF dos_controls_implemented = TRUE
AND last_test_date > 365_days_ago
AND infrastructure_changes = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Critical Service Without Redundancy]
IF business_criticality = "CRITICAL"
AND service_redundancy = FALSE
AND dos_protection_level = "BASIC"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| DoS event types are defined | [RULE-01] |
| Protection controls are employed | [RULE-02], [RULE-03], [RULE-06] |
| Capacity planning implemented | [RULE-04] |
| Controls are tested and validated | [RULE-05] |