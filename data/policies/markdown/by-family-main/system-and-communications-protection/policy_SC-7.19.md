# POLICY: SC-7.19: Block Communication from Non-organizationally Configured Hosts

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.19 |
| NIST Control | SC-7.19: Block Communication from Non-organizationally Configured Hosts |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network security, communication blocking, unauthorized clients, boundary protection, traffic filtering |

## 1. POLICY STATEMENT
The organization SHALL block inbound and outbound communications traffic from communication clients that are independently configured by end users and external service providers. Only organization-authorized and organization-configured communication tools are permitted for business communications.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All network endpoints | YES | Corporate and BYOD devices |
| Network infrastructure | YES | Firewalls, proxies, gateways |
| Cloud services | YES | SaaS applications and platforms |
| Guest networks | CONDITIONAL | Limited scope with documented exceptions |
| Air-gapped systems | NO | Isolated from external communications |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure traffic blocking mechanisms<br>• Monitor unauthorized communication attempts<br>• Maintain approved communication client lists |
| IT Operations | • Deploy and maintain network filtering tools<br>• Implement configuration management<br>• Report blocking violations |
| Security Operations Center | • Monitor security events and alerts<br>• Investigate communication policy violations<br>• Coordinate incident response activities |

## 4. RULES

[RULE-01] Network security controls MUST block all inbound traffic from communication clients that are independently configured by end users and not approved by the organization.
[VALIDATION] IF traffic_source = "independent_client" AND organization_approved = FALSE AND direction = "inbound" THEN block_traffic = TRUE

[RULE-02] Network security controls MUST block all outbound traffic to communication clients that are independently configured by end users and not approved by the organization.
[VALIDATION] IF traffic_destination = "independent_client" AND organization_approved = FALSE AND direction = "outbound" THEN block_traffic = TRUE

[RULE-03] Organizations MUST maintain a documented list of approved communication clients and external service providers that are exempt from blocking rules.
[VALIDATION] IF communication_client EXISTS AND approved_list_documented = FALSE THEN violation

[RULE-04] Communication clients configured by the organization for authorized business functions SHALL NOT be subject to traffic blocking controls.
[VALIDATION] IF client_configured_by = "organization" AND business_authorized = TRUE THEN blocking_exempt = TRUE

[RULE-05] Network monitoring systems MUST log all blocked communication attempts from unauthorized clients within 5 minutes of detection.
[VALIDATION] IF blocked_communication_detected = TRUE AND log_time > detection_time + 5_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Communication Client Assessment - Evaluate and approve business communication tools
- [PROC-02] Traffic Blocking Configuration - Configure network devices to block unauthorized communications
- [PROC-03] Exception Management - Document and approve temporary communication exceptions
- [PROC-04] Monitoring and Alerting - Monitor for unauthorized communication attempts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, new communication technologies, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Instant Messaging]
IF application_type = "instant_messaging"
AND configured_by = "end_user"
AND organization_approved = FALSE
AND traffic_blocked = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved Video Conferencing]
IF application_type = "video_conferencing"
AND configured_by = "organization"
AND approved_list = TRUE
AND traffic_blocked = FALSE
THEN compliance = TRUE

[SCENARIO-03: Personal Cloud Storage Access]
IF application_type = "cloud_storage"
AND configured_by = "end_user"
AND business_approved = FALSE
AND blocking_bypassed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Guest Network Exception]
IF network_segment = "guest"
AND documented_exception = TRUE
AND limited_scope = TRUE
AND time_limited = TRUE
THEN compliance = TRUE

[SCENARIO-05: Unmonitored Communication Blocking]
IF unauthorized_traffic_detected = TRUE
AND blocking_occurred = TRUE
AND logged_within_5min = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Block inbound communications from unauthorized clients | [RULE-01] |
| Block outbound communications to unauthorized clients | [RULE-02] |
| Maintain approved communication client documentation | [RULE-03] |
| Exempt organization-configured authorized tools | [RULE-04] |
| Log blocked communication attempts | [RULE-05] |