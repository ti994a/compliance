# POLICY: SC-7.11: Restrict Incoming Communications Traffic

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.11 |
| NIST Control | SC-7.11: Restrict Incoming Communications Traffic |
| Version | 1.0 |
| Owner | Network Security Manager |
| Keywords | incoming communications, authorized sources, traffic restriction, firewall rules, access control lists, network security |

## 1. POLICY STATEMENT
The organization SHALL only allow incoming communications from pre-authorized sources to be routed to pre-authorized destinations within the network infrastructure. All unauthorized source-destination communication pairs MUST be blocked at network boundary protection devices.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network firewalls | YES | All perimeter and internal firewalls |
| Router access control lists | YES | Edge and core routers |
| Load balancers | YES | External-facing load balancers |
| VPN gateways | YES | Remote access and site-to-site VPNs |
| Cloud security groups | YES | AWS, Azure, GCP security groups |
| Internal workstations | NO | Covered by endpoint security policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Manager | • Approve authorized source-destination pairs<br>• Review traffic restriction policies quarterly<br>• Oversee firewall rule management |
| Network Operations Team | • Implement firewall rules and ACLs<br>• Monitor blocked traffic alerts<br>• Maintain authorized communications inventory |
| Security Operations Center | • Monitor unauthorized communication attempts<br>• Investigate traffic anomalies<br>• Escalate policy violations |

## 4. RULES
[RULE-01] Network boundary devices MUST maintain an approved list of authorized source-destination address pairs for incoming communications.
[VALIDATION] IF authorized_pairs_list = "not_maintained" OR list_approval_status = "unapproved" THEN violation

[RULE-02] Incoming communications from unauthorized sources SHALL be blocked and logged at the network perimeter.
[VALIDATION] IF source_address NOT IN authorized_sources AND traffic_allowed = TRUE THEN critical_violation

[RULE-03] Communications to unauthorized destinations from any source MUST be blocked even if the source is authorized.
[VALIDATION] IF destination_address NOT IN authorized_destinations AND traffic_allowed = TRUE THEN violation

[RULE-04] Source address validation techniques MUST be implemented to prevent spoofing and use of illegal/unallocated addresses.
[VALIDATION] IF source_validation = "disabled" OR spoofing_protection = FALSE THEN violation

[RULE-05] All blocked incoming communications attempts MUST be logged with source, destination, timestamp, and reason for blocking.
[VALIDATION] IF blocked_traffic_logged = FALSE OR log_retention < 90_days THEN violation

[RULE-06] Authorized source-destination pairs list MUST be reviewed and updated at least quarterly or when network changes occur.
[VALIDATION] IF last_review_date > 90_days_ago AND no_network_changes = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Authorized Communications Management - Process for defining and maintaining authorized source-destination pairs
- [PROC-02] Firewall Rule Implementation - Standardized process for implementing traffic restrictions
- [PROC-03] Traffic Monitoring and Alerting - Continuous monitoring of blocked and allowed communications
- [PROC-04] Exception Request Process - Formal process for temporary communication exceptions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Network architecture changes, security incidents involving unauthorized communications, regulatory audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: External Web Traffic]
IF source_address = "external_internet"
AND destination_port IN [80, 443]
AND destination_address IN authorized_web_servers
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Database Access]
IF source_address = "external_internet"
AND destination_port IN [1433, 3306, 5432]
AND traffic_blocked = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Internal Communications Restriction]
IF source_address IN internal_network
AND destination_address IN restricted_admin_network
AND source_authorized_for_destination = FALSE
AND traffic_allowed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Spoofed Source Address]
IF source_address IN internal_ip_ranges
AND traffic_origin = "external_interface"
AND spoofing_protection_triggered = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Approved Business Partner Access]
IF source_address IN authorized_partner_ranges
AND destination_address IN authorized_partner_services
AND current_time WITHIN business_hours
AND partnership_agreement = "active"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Only allow incoming communications from authorized sources | [RULE-01], [RULE-02] |
| Route to authorized destinations only | [RULE-03] |
| Implement source address validation | [RULE-04] |
| Log blocked communications | [RULE-05] |
| Maintain current authorization lists | [RULE-06] |