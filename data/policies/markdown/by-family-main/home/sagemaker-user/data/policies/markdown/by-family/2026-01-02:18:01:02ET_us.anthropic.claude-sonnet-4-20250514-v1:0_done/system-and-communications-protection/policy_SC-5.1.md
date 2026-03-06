# POLICY: SC-5.1: Restrict Ability to Attack Other Systems

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-5.1 |
| NIST Control | SC-5.1: Restrict Ability to Attack Other Systems |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | denial-of-service, DoS attacks, network restrictions, egress filtering, resource limits |

## 1. POLICY STATEMENT
The organization SHALL restrict the ability of individuals to launch denial-of-service attacks against other systems by implementing technical controls that limit network connectivity and system resource usage. These restrictions apply to all users including potential hostile insiders and compromised accounts.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All network endpoints | YES | Includes workstations, servers, mobile devices |
| Cloud instances | YES | AWS, Azure, GCP resources |
| Network infrastructure | YES | Routers, switches, firewalls |
| Third-party connections | YES | Vendor and partner network access |
| Guest networks | YES | Visitor and temporary access networks |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure egress filtering rules<br>• Monitor for DoS attack patterns<br>• Implement bandwidth restrictions |
| System Administrators | • Configure resource limits on systems<br>• Monitor system resource utilization<br>• Implement user connection limits |
| Security Operations Center | • Monitor for suspicious network activity<br>• Investigate potential DoS attempts<br>• Coordinate incident response |

## 4. RULES

[RULE-01] All systems MUST implement egress filtering to prevent connection to known malicious destinations and restrict outbound connections to only business-justified services and ports.
[VALIDATION] IF egress_filtering = FALSE OR allowed_destinations = "unrestricted" THEN violation

[RULE-02] Network devices MUST enforce bandwidth limitations per user session not exceeding 100 Mbps for standard users and 1 Gbps for privileged users unless explicitly approved.
[VALIDATION] IF user_bandwidth > 100_Mbps AND user_type = "standard" AND exception_approved = FALSE THEN violation

[RULE-03] Systems MUST limit concurrent network connections per user to maximum 1000 connections for standard users and 5000 for service accounts.
[VALIDATION] IF concurrent_connections > 1000 AND user_type = "standard" THEN violation
[VALIDATION] IF concurrent_connections > 5000 AND user_type = "service" THEN violation

[RULE-04] All systems MUST implement resource quotas limiting CPU usage to 80% and memory usage to 90% per user process to prevent resource exhaustion attacks.
[VALIDATION] IF cpu_usage_per_process > 80% OR memory_usage_per_process > 90% THEN resource_violation

[RULE-05] Boundary devices MUST block traffic to RFC 1918 private address spaces from internal networks unless explicitly required for business operations.
[VALIDATION] IF destination_ip IN rfc1918_ranges AND source = "internal" AND business_justification = FALSE THEN violation

[RULE-06] Systems MUST log all denied connection attempts and resource limit violations for security monitoring and analysis.
[VALIDATION] IF logging_enabled = FALSE OR log_retention < 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DoS Attack Prevention Configuration - Standard configurations for network and system DoS prevention controls
- [PROC-02] Resource Limit Monitoring - Procedures for monitoring and alerting on resource usage violations
- [PROC-03] Egress Traffic Analysis - Regular review of outbound traffic patterns for anomalies
- [PROC-04] Exception Request Process - Approval workflow for bandwidth or connection limit exceptions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving DoS attacks, major network architecture changes, new threat intelligence

## 7. SCENARIO PATTERNS

[SCENARIO-01: Excessive Outbound Connections]
IF user_connection_count > 1000
AND user_type = "standard"
AND time_period = "concurrent"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unrestricted Egress Traffic]
IF egress_filtering = "disabled"
AND system_type = "endpoint"
AND network_zone = "internal"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Resource Exhaustion Attempt]
IF cpu_usage > 80%
AND process_owner = "user_account"
AND duration > 300_seconds
AND resource_limits_enforced = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Approved High-Bandwidth User]
IF user_bandwidth > 100_Mbps
AND user_type = "standard"
AND exception_approved = TRUE
AND approval_date > (current_date - 365_days)
THEN compliance = TRUE

[SCENARIO-05: Service Account Connection Limits]
IF concurrent_connections = 3000
AND user_type = "service"
AND connections < 5000
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Restrict ability to launch DoS attacks against other systems | [RULE-01], [RULE-02], [RULE-03] |
| Limit transport medium connectivity | [RULE-01], [RULE-05] |
| Prevent excessive system resource usage | [RULE-04] |
| Implement boundary device protections | [RULE-05] |
| Maintain audit trail of restrictions | [RULE-06] |