# POLICY: SC-22: Architecture and Provisioning for Name/Address Resolution Service

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-22 |
| NIST Control | SC-22: Architecture and Provisioning for Name/Address Resolution Service |
| Version | 1.0 |
| Owner | Infrastructure Security Manager |
| Keywords | DNS, name resolution, fault tolerance, role separation, redundancy, availability |

## 1. POLICY STATEMENT
The organization SHALL ensure all name/address resolution services are fault-tolerant through redundant infrastructure and implement strict internal and external role separation. DNS and other name resolution systems MUST be architected to eliminate single points of failure and enforce access controls based on client location and authorization.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| DNS Servers | YES | All authoritative and recursive DNS servers |
| Name Resolution Services | YES | All systems providing name/address translation |
| Network Infrastructure | CONDITIONAL | Only components supporting DNS services |
| Third-party DNS Providers | YES | External DNS services under contract |
| Development/Test DNS | YES | Non-production systems handling real domains |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Infrastructure Security Manager | • Policy enforcement and compliance monitoring<br>• DNS architecture approval<br>• Security assessment coordination |
| DNS Administrators | • DNS server configuration and maintenance<br>• Role separation implementation<br>• Monitoring and incident response |
| Network Security Team | • Access control implementation<br>• Geographic separation validation<br>• Security testing and assessment |

## 4. RULES

[RULE-01] Organizations MUST deploy at least two authoritative DNS servers with one configured as primary and one as secondary.
[VALIDATION] IF dns_server_count < 2 OR primary_server_count != 1 OR secondary_server_count < 1 THEN critical_violation

[RULE-02] DNS servers MUST be deployed in geographically separated network subnetworks and SHALL NOT be located in the same physical facility.
[VALIDATION] IF primary_location = secondary_location OR geographic_separation < 50_miles THEN violation

[RULE-03] Internal DNS servers MUST only process name resolution requests from internal organizational clients and SHALL NOT respond to external requests.
[VALIDATION] IF internal_dns_server = TRUE AND external_request_processed = TRUE THEN violation

[RULE-04] External DNS servers MUST only process requests from external clients and SHALL NOT process internal organizational requests.
[VALIDATION] IF external_dns_server = TRUE AND internal_request_processed = TRUE THEN violation

[RULE-05] Organizations MUST specify and document authorized clients for each DNS server role using address ranges and explicit access lists.
[VALIDATION] IF dns_server_deployed = TRUE AND (client_access_list = NULL OR address_ranges = NULL) THEN violation

[RULE-06] DNS infrastructure MUST implement fault-tolerance mechanisms to ensure service availability during component failures.
[VALIDATION] IF single_point_of_failure = TRUE OR failover_capability = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNS Architecture Review - Annual assessment of DNS infrastructure design and fault tolerance
- [PROC-02] Role Separation Validation - Quarterly testing of internal/external DNS role enforcement
- [PROC-03] Geographic Separation Audit - Semi-annual verification of physical facility separation
- [PROC-04] DNS Access Control Review - Monthly review of client authorization lists and address ranges

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Infrastructure changes, security incidents, merger/acquisition, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Single DNS Server Deployment]
IF dns_server_count = 1
AND authoritative_service = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Co-located DNS Servers]
IF primary_dns_facility = secondary_dns_facility
AND geographic_separation < 50_miles
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Internal DNS Processing External Requests]
IF dns_server_role = "internal"
AND external_requests_allowed = TRUE
AND request_source = "internet"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Client Access Controls]
IF dns_server_deployed = TRUE
AND client_access_list = "undefined"
AND address_range_restrictions = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Role Separation Implementation]
IF internal_dns_servers >= 1
AND external_dns_servers >= 1
AND role_separation_enforced = TRUE
AND geographic_separation >= 50_miles
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Systems providing name/address resolution are fault-tolerant | [RULE-01], [RULE-06] |
| Systems implement internal role separation | [RULE-03], [RULE-05] |
| Systems implement external role separation | [RULE-04], [RULE-05] |
| Geographic separation requirements | [RULE-02] |
| Client authorization specification | [RULE-05] |