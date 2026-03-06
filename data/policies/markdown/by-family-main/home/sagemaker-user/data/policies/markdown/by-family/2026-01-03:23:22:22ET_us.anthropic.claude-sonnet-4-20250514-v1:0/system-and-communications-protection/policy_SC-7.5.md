# POLICY: SC-7.5: Deny by Default — Allow by Exception

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.5 |
| NIST Control | SC-7.5: Deny by Default — Allow by Exception |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network security, firewall, traffic control, boundary protection, managed interfaces, deny default, allow exception |

## 1. POLICY STATEMENT
All network communications traffic SHALL be denied by default at managed interfaces, with explicit exceptions granted only for essential and approved connections. This policy applies to both inbound and outbound traffic across all system boundaries and external system connections.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network firewalls | YES | All managed network interfaces |
| Cloud security groups | YES | AWS, Azure, GCP security configurations |
| Network access control lists | YES | Router and switch ACLs |
| Application firewalls | YES | Web application and API gateways |
| VPN gateways | YES | Remote access and site-to-site connections |
| Development/test systems | YES | Must follow same deny-default principles |
| Legacy systems | CONDITIONAL | Exemptions require CISO approval |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure deny-default rules on all managed interfaces<br>• Review and approve traffic exception requests<br>• Monitor and audit network traffic patterns |
| System Administrators | • Implement deny-default configurations<br>• Document all approved exceptions<br>• Maintain current network access documentation |
| Security Architecture Team | • Design network segmentation with deny-default principles<br>• Review exception requests for security impact<br>• Validate compliance during security assessments |

## 4. RULES
[RULE-01] All managed network interfaces MUST be configured with deny-all default policies that block all inbound and outbound traffic unless explicitly permitted.
[VALIDATION] IF interface_type = "managed" AND default_policy != "deny_all" THEN critical_violation

[RULE-02] Network traffic exceptions MUST be documented with business justification, approved by Network Security Team, and reviewed quarterly.
[VALIDATION] IF traffic_allowed = TRUE AND (justification_documented = FALSE OR approval_status != "approved") THEN violation

[RULE-03] Exception rules MUST specify exact source, destination, port, and protocol combinations with no wildcard entries for external connections.
[VALIDATION] IF rule_scope = "external" AND (source = "any" OR destination = "any" OR port = "any") THEN violation

[RULE-04] All network access rules MUST be reviewed and revalidated at least quarterly, with unused rules removed within 30 days of identification.
[VALIDATION] IF rule_last_reviewed > 90_days OR (rule_usage = "none" AND rule_age > 30_days) THEN violation

[RULE-05] Emergency exception procedures MUST require CISO approval within 24 hours and automatic expiration within 72 hours unless formally extended.
[VALIDATION] IF exception_type = "emergency" AND (ciso_approval_time > 24_hours OR expiration_time > 72_hours) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Exception Request Process - Standardized workflow for requesting, reviewing, and approving traffic exceptions
- [PROC-02] Quarterly Access Rule Review - Systematic review of all network access rules and exception justifications
- [PROC-03] Emergency Access Procedures - Process for temporary exceptions during incidents or urgent business needs
- [PROC-04] Network Configuration Management - Change control procedures for firewall and security group modifications

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, network architecture changes, regulatory updates, failed compliance assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Default Allow Configuration]
IF interface_type = "managed"
AND default_policy = "allow_all"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Undocumented Exception Rule]
IF traffic_rule = "allow"
AND business_justification = "none"
AND approval_status = "pending"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Wildcard External Rule]
IF rule_direction = "inbound"
AND source_address = "any"
AND connection_type = "external"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Expired Emergency Exception]
IF exception_type = "emergency"
AND current_time > expiration_time
AND extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Specific Exception]
IF traffic_rule = "allow"
AND source_specific = TRUE
AND destination_specific = TRUE
AND business_justification = "documented"
AND approval_status = "approved"
AND last_reviewed < 90_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Network communications traffic is denied by default at managed interfaces | [RULE-01] |
| Network communications traffic is allowed by exception at managed interfaces | [RULE-02], [RULE-03] |
| Exception management and documentation | [RULE-02], [RULE-04] |
| Emergency access controls | [RULE-05] |