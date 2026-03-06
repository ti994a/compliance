# POLICY: SC-22: Architecture and Provisioning for Name/Address Resolution Service

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-22 |
| NIST Control | SC-22: Architecture and Provisioning for Name/Address Resolution Service |
| Version | 1.0 |
| Owner | Infrastructure Security Manager |
| Keywords | DNS, name resolution, fault tolerance, role separation, redundancy, authoritative servers |

## 1. POLICY STATEMENT
The organization SHALL ensure all name/address resolution services are fault-tolerant through redundant systems and implement strict internal and external role separation. DNS infrastructure MUST eliminate single points of failure and enforce role-based access controls to prevent unauthorized resolution requests.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| DNS Servers | YES | All authoritative and recursive DNS servers |
| Network Infrastructure | YES | Supporting network components for DNS services |
| Third-party DNS Services | YES | External DNS providers under contract |
| Development/Test DNS | CONDITIONAL | If processing production data or accessible externally |
| IoT Device DNS | YES | All connected devices using organizational DNS |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Infrastructure Security Manager | • Policy oversight and compliance monitoring<br>• DNS security architecture approval<br>• Risk assessment coordination |
| DNS Administrators | • DNS server configuration and maintenance<br>• Role separation implementation<br>• Redundancy monitoring and testing |
| Network Operations Center | • DNS service availability monitoring<br>• Incident response for DNS failures<br>• Performance baseline maintenance |

## 4. RULES
[RULE-01] Organizations MUST deploy at least two authoritative DNS servers with one configured as primary and one as secondary server.
[VALIDATION] IF authoritative_dns_count < 2 OR primary_server_count != 1 OR secondary_server_count < 1 THEN critical_violation

[RULE-02] DNS servers MUST be deployed in geographically separated network subnetworks and SHALL NOT be located in the same physical facility.
[VALIDATION] IF dns_servers_same_facility = TRUE OR geographic_separation < 50_miles THEN violation

[RULE-03] Internal DNS servers MUST only process name resolution requests from internal organizational clients and SHALL NOT respond to external requests.
[VALIDATION] IF internal_dns_external_response = TRUE OR external_client_access = TRUE THEN violation

[RULE-04] External DNS servers MUST only process requests from external clients and SHALL NOT handle internal organizational resolution requests.
[VALIDATION] IF external_dns_internal_response = TRUE OR internal_client_access = TRUE THEN violation

[RULE-05] Organizations MUST specify authorized clients for DNS servers through address ranges, explicit allow lists, or equivalent access controls.
[VALIDATION] IF client_access_controls = FALSE OR authorization_method = "undefined" THEN violation

[RULE-06] DNS infrastructure MUST maintain 99.9% availability measured monthly with automated failover capabilities.
[VALIDATION] IF monthly_availability < 99.9 OR automated_failover = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DNS Server Deployment - Geographic separation validation and redundancy testing
- [PROC-02] Role Separation Configuration - Internal/external DNS role enforcement and validation
- [PROC-03] Client Authorization Management - Access control list maintenance and review
- [PROC-04] Fault Tolerance Testing - Regular failover testing and recovery procedures
- [PROC-05] DNS Security Monitoring - Continuous monitoring for unauthorized access attempts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: DNS infrastructure changes, security incidents, regulatory updates, geographic relocations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Single DNS Server Deployment]
IF authoritative_dns_count = 1
AND backup_dns_available = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Co-located DNS Servers]
IF primary_dns_facility = secondary_dns_facility
AND geographic_separation = 0
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Internal DNS Serving External Clients]
IF dns_role = "internal"
AND external_requests_processed = TRUE
AND role_separation_bypass = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Undefined Client Access Controls]
IF client_authorization_method = "none"
AND access_control_lists = "undefined"
AND open_dns_resolver = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Fault-Tolerant Configuration]
IF authoritative_dns_count >= 2
AND geographic_separation >= 50_miles
AND role_separation_implemented = TRUE
AND client_access_controls = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Systems providing name/address resolution are fault-tolerant | [RULE-01], [RULE-02], [RULE-06] |
| Systems implement internal role separation | [RULE-03], [RULE-05] |
| Systems implement external role separation | [RULE-04], [RULE-05] |