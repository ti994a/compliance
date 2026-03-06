# POLICY: SC-7.19: Block Communication from Non-organizationally Configured Hosts

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.19 |
| NIST Control | SC-7.19: Block Communication from Non-organizationally Configured Hosts |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | communication blocking, boundary protection, unauthorized clients, traffic filtering, network security |

## 1. POLICY STATEMENT
The organization SHALL block inbound and outbound communications traffic from communication clients that are independently configured by end users and external service providers. Only organizationally-approved and configured communication clients are permitted to traverse network boundaries.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All network boundaries | YES | Including perimeter firewalls, internal segments |
| Employee workstations | YES | Corporate and BYOD devices |
| Communication applications | YES | IM clients, video conferencing, file sharing |
| Mobile devices | YES | Company-owned and personal devices on network |
| Guest networks | CONDITIONAL | Must maintain separation from corporate resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Implement traffic blocking mechanisms<br>• Monitor for unauthorized communication clients<br>• Maintain approved application whitelist |
| IT Operations | • Deploy and configure network filtering controls<br>• Maintain network boundary documentation<br>• Respond to blocking rule exceptions |
| Security Operations Center | • Monitor communication traffic violations<br>• Investigate unauthorized application usage<br>• Escalate policy violations |

## 4. RULES
[RULE-01] All inbound communication traffic from independently configured communication clients MUST be blocked at network boundaries.
[VALIDATION] IF traffic_direction = "inbound" AND client_configuration = "user_configured" AND traffic_blocked = FALSE THEN violation

[RULE-02] All outbound communication traffic to independently configured communication clients MUST be blocked at network boundaries.
[VALIDATION] IF traffic_direction = "outbound" AND client_configuration = "user_configured" AND traffic_blocked = FALSE THEN violation

[RULE-03] Communication clients MUST be organizationally approved and configured to be permitted through network boundaries.
[VALIDATION] IF application_approved = FALSE OR application_org_configured = FALSE THEN traffic_blocked = TRUE

[RULE-04] Network filtering mechanisms MUST maintain a whitelist of approved communication applications and block all others by default.
[VALIDATION] IF application NOT IN approved_whitelist AND traffic_allowed = TRUE THEN violation

[RULE-05] Blocking mechanisms MUST log all blocked communication attempts for security monitoring and compliance verification.
[VALIDATION] IF communication_blocked = TRUE AND log_generated = FALSE THEN configuration_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Communication Application Approval Process - Evaluation and approval workflow for new communication tools
- [PROC-02] Network Boundary Traffic Filtering - Implementation and maintenance of blocking controls
- [PROC-03] Violation Monitoring and Response - Detection and remediation of unauthorized communication attempts
- [PROC-04] Approved Application Whitelist Management - Regular review and updates to permitted applications

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New communication technologies, security incidents, regulatory changes, network architecture modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Personal Messaging App Usage]
IF application_type = "instant_messaging"
AND configuration_source = "end_user"
AND network_boundary_crossed = TRUE
AND traffic_blocked = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unauthorized Video Conferencing]
IF application_category = "video_conferencing"
AND approval_status = "not_approved"
AND traffic_direction = "outbound"
AND blocking_active = TRUE
THEN compliance = TRUE

[SCENARIO-03: Approved Corporate Communication Tool]
IF application_name IN approved_whitelist
AND configuration_managed = "organization"
AND traffic_allowed = TRUE
THEN compliance = TRUE

[SCENARIO-04: File Sharing Service Bypass]
IF application_function = "file_sharing"
AND configuration_source = "external_provider"
AND boundary_protection_bypassed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Mobile App Communication Blocking]
IF device_type = "mobile"
AND application_installed = "user_initiated"
AND communication_blocked = TRUE
AND exception_documented = FALSE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Block inbound communications from user-configured clients | [RULE-01] |
| Block outbound communications to user-configured clients | [RULE-02] |
| Allow only organizationally configured communication clients | [RULE-03] |
| Implement default-deny filtering for communication applications | [RULE-04] |
| Log blocked communication attempts for monitoring | [RULE-05] |