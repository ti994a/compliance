# POLICY: SC-7.5: Deny by Default — Allow by Exception

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.5 |
| NIST Control | SC-7.5: Deny by Default — Allow by Exception |
| Version | 1.0 |
| Owner | Network Security Manager |
| Keywords | network traffic, firewall, managed interfaces, deny default, allow exception, boundary protection |

## 1. POLICY STATEMENT
All network communications traffic MUST be denied by default at managed interfaces, with traffic allowed only through documented exceptions. This deny-all, permit-by-exception approach applies to both inbound and outbound communications across all network boundaries and external system connections.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network firewalls | YES | All perimeter and internal firewalls |
| Routers with ACLs | YES | Enterprise and branch routers |
| Network switches | CONDITIONAL | Only Layer 3 switches with filtering |
| Cloud security groups | YES | AWS, Azure, GCP security groups |
| Load balancers | YES | Application and network load balancers |
| VPN gateways | YES | Site-to-site and remote access VPNs |
| Network appliances | YES | IPS, proxy servers, web filters |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Manager | • Approve all traffic exception requests<br>• Review quarterly compliance reports<br>• Maintain deny-by-default policy standards |
| Network Operations Team | • Implement deny-by-default configurations<br>• Monitor traffic blocking events<br>• Execute approved exception changes |
| Security Architecture Team | • Design network segmentation with default-deny<br>• Review exception requests for security impact<br>• Validate managed interface configurations |

## 4. RULES
[RULE-01] All managed interfaces MUST be configured with deny-by-default rules that block all network traffic unless explicitly permitted.
[VALIDATION] IF managed_interface_exists = TRUE AND default_action != "deny" THEN critical_violation

[RULE-02] Traffic exceptions MUST be documented with business justification, approved by Network Security Manager, and implemented with least-privilege access.
[VALIDATION] IF traffic_allowed = TRUE AND (exception_documented = FALSE OR approval_exists = FALSE) THEN major_violation

[RULE-03] Exception rules MUST specify exact source, destination, port, and protocol rather than using wildcard or "any" statements.
[VALIDATION] IF exception_rule_exists = TRUE AND (source = "any" OR destination = "any" OR port = "any") THEN major_violation

[RULE-04] All managed interfaces MUST log denied traffic attempts for security monitoring and compliance validation.
[VALIDATION] IF managed_interface_exists = TRUE AND deny_logging_enabled = FALSE THEN moderate_violation

[RULE-05] Exception rules MUST be reviewed quarterly and removed if no longer required for business operations.
[VALIDATION] IF exception_age > 90_days AND last_review_date < current_date - 90_days THEN moderate_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Exception Request Process - Formal process for requesting and approving traffic exceptions
- [PROC-02] Managed Interface Configuration Standard - Technical requirements for deny-by-default implementation  
- [PROC-03] Quarterly Exception Review Process - Regular review and cleanup of exception rules
- [PROC-04] Traffic Monitoring and Alerting - Monitoring denied traffic for security events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents, network architecture changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Firewall Default Configuration]
IF device_type = "firewall"
AND deployment_status = "new"
AND default_rule_action = "permit"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Overly Permissive Exception Rule]
IF exception_rule_exists = TRUE
AND source_address = "0.0.0.0/0"
AND destination_port = "any"
AND business_justification = "general connectivity"
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-03: Undocumented Traffic Exception]
IF traffic_flow_permitted = TRUE
AND traffic_type = "non-standard"
AND exception_documentation = FALSE
AND approval_record = FALSE
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-04: Missing Deny Logging]
IF managed_interface_type = "border_router"
AND deny_rule_exists = TRUE
AND logging_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Stale Exception Rule]
IF exception_rule_active = TRUE
AND last_traffic_date < current_date - 180_days
AND quarterly_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Network communications traffic is denied by default at managed interfaces | [RULE-01], [RULE-04] |
| Network communications traffic is allowed by exception at managed interfaces | [RULE-02], [RULE-03], [RULE-05] |