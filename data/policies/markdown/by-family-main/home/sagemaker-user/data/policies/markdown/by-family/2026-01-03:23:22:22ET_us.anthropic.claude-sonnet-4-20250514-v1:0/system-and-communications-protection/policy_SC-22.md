# POLICY: SC-22: Architecture and Provisioning for Name/Address Resolution Service

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-22 |
| NIST Control | SC-22: Architecture and Provisioning for Name/Address Resolution Service |
| Version | 1.0 |
| Owner | Infrastructure Security Manager |
| Keywords | DNS, name resolution, fault tolerance, role separation, redundancy |

## 1. POLICY STATEMENT
The organization SHALL ensure all name/address resolution services are fault-tolerant through redundant systems and implement strict internal and external role separation. DNS infrastructure MUST eliminate single points of failure and maintain clear separation between internal and external resolution services.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| DNS Servers | YES | All authoritative and recursive DNS servers |
| Name Resolution Services | YES | All systems providing name/address resolution |
| Network Infrastructure | CONDITIONAL | Only components supporting DNS services |
| Third-party DNS Providers | YES | When used for organizational domains |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Infrastructure Security Manager | • Oversee DNS architecture compliance<br>• Approve DNS configuration changes<br>• Monitor fault tolerance implementation |
| Network Operations Team | • Configure and maintain DNS servers<br>• Implement role separation controls<br>• Monitor DNS service availability |
| System Administrators | • Deploy redundant DNS infrastructure<br>• Maintain geographic separation<br>• Document DNS configurations |

## 4. RULES
[RULE-01] Organizations MUST deploy at least two authoritative DNS servers with one configured as primary and one as secondary.
[VALIDATION] IF authoritative_dns_count < 2 OR primary_server_configured = FALSE OR secondary_server_configured = FALSE THEN violation

[RULE-02] DNS servers MUST be deployed in geographically separated network subnetworks and SHALL NOT be located in the same physical facility.
[VALIDATION] IF dns_server_locations = same_facility OR geographic_separation = FALSE THEN violation

[RULE-03] Internal DNS servers MUST only process name resolution requests from internal organizational clients and SHALL NOT respond to external queries.
[VALIDATION] IF internal_dns_server = TRUE AND external_queries_allowed = TRUE THEN violation

[RULE-04] External DNS servers MUST only process requests from external clients and SHALL NOT handle internal organizational queries.
[VALIDATION] IF external_dns_server = TRUE AND internal_queries_processed = TRUE THEN violation

[RULE-05] Organizations MUST specify and document authorized clients for DNS servers by address ranges and explicit lists.
[VALIDATION] IF dns_client_authorization = undefined OR client_access_lists = empty THEN violation

[RULE-06] DNS infrastructure MUST implement fault-tolerant mechanisms to eliminate single points of failure.
[VALIDATION] IF single_point_failure_exists = TRUE OR fault_tolerance_implemented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNS Architecture Review - Annual assessment of DNS fault tolerance and role separation
- [PROC-02] DNS Configuration Management - Standardized process for DNS server deployment and configuration
- [PROC-03] Geographic Separation Validation - Quarterly verification of physical separation requirements
- [PROC-04] Role Separation Testing - Semi-annual testing of internal/external DNS role enforcement

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: DNS infrastructure changes, security incidents, merger/acquisition, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Single DNS Server Deployment]
IF authoritative_dns_count = 1
AND backup_dns_configured = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Co-located DNS Servers]
IF primary_dns_location = secondary_dns_location
AND physical_facility = same_building
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Internal DNS Responding to External Queries]
IF dns_server_role = "internal"
AND external_query_responses > 0
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Undefined Client Access Controls]
IF dns_server_deployed = TRUE
AND client_access_lists = undefined
AND address_range_restrictions = none
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Role Separation Implementation]
IF internal_dns_external_access = FALSE
AND external_dns_internal_access = FALSE
AND geographic_separation = TRUE
AND fault_tolerance_verified = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Fault-tolerant name/address resolution systems | [RULE-01], [RULE-02], [RULE-06] |
| Internal role separation implementation | [RULE-03], [RULE-05] |
| External role separation implementation | [RULE-04], [RULE-05] |