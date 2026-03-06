# POLICY: SC-7.5: Deny by Default — Allow by Exception

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.5 |
| NIST Control | SC-7.5: Deny by Default — Allow by Exception |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network traffic, firewall, deny default, allow exception, managed interfaces, boundary protection |

## 1. POLICY STATEMENT
All network communications traffic MUST be denied by default at managed interfaces, with network communications allowed only through explicit, documented exceptions. This policy applies to both inbound and outbound traffic across all system boundaries and external system connections.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network firewalls | YES | All perimeter and internal firewalls |
| Routers with ACLs | YES | Enterprise and branch routers |
| Load balancers | YES | Application and network load balancers |
| Cloud security groups | YES | AWS, Azure, GCP security groups |
| Network switches | CONDITIONAL | Only Layer 3 switches with filtering |
| Workstation firewalls | YES | Host-based firewalls on endpoints |
| External connections | YES | Partner, vendor, and internet connections |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Configure deny-by-default rules on all managed interfaces<br>• Review and approve traffic exception requests<br>• Monitor compliance with traffic policies |
| System Administrators | • Implement host-based deny-by-default configurations<br>• Document business justification for traffic exceptions<br>• Maintain current network documentation |
| Security Operations Center | • Monitor for unauthorized traffic patterns<br>• Investigate policy violations<br>• Generate compliance reports |

## 4. RULES
[RULE-01] All managed network interfaces MUST implement a default-deny policy that blocks all network communications traffic unless explicitly permitted.
[VALIDATION] IF interface_type = "managed" AND default_policy != "deny" THEN critical_violation

[RULE-02] Traffic exceptions MUST be documented with business justification, approved by network security team, and implemented using least-privilege principles.
[VALIDATION] IF traffic_allowed = TRUE AND (justification_documented = FALSE OR security_approved = FALSE) THEN violation

[RULE-03] Exception rules MUST specify source, destination, port, protocol, and business purpose with no wildcard (*) entries for production systems.
[VALIDATION] IF rule_contains_wildcard = TRUE AND environment = "production" THEN violation

[RULE-04] All traffic exception rules MUST be reviewed quarterly and removed if no longer required for business operations.
[VALIDATION] IF rule_last_reviewed > 90_days OR rule_business_need = FALSE THEN violation

[RULE-05] Deny-by-default policies MUST be applied to both inbound and outbound traffic at all managed interfaces.
[VALIDATION] IF (inbound_default_policy != "deny" OR outbound_default_policy != "deny") AND interface_managed = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Exception Request Process - Standardized workflow for requesting and approving traffic exceptions
- [PROC-02] Quarterly Rule Review - Systematic review of all exception rules for continued business necessity
- [PROC-03] Interface Configuration Standard - Technical requirements for implementing deny-by-default on various device types
- [PROC-04] Violation Response - Incident response procedures for unauthorized traffic detection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized traffic, major network architecture changes, regulatory audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Firewall Default Allow]
IF device_type = "firewall"
AND default_policy = "allow"
AND interface_status = "managed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Undocumented Exception Rule]
IF traffic_rule = "allow"
AND business_justification = "missing"
AND rule_age > 30_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Wildcard Production Rule]
IF rule_contains = "any/any"
AND environment = "production"
AND exception_approved = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Stale Exception Rule]
IF rule_last_reviewed > 90_days
AND business_need_validated = FALSE
AND rule_type = "exception"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Compliant Exception]
IF default_policy = "deny"
AND exception_documented = TRUE
AND security_approved = TRUE
AND rule_specific = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Network communications traffic is denied by default at managed interfaces | [RULE-01], [RULE-05] |
| Network communications traffic is allowed by exception at managed interfaces | [RULE-02], [RULE-03], [RULE-04] |