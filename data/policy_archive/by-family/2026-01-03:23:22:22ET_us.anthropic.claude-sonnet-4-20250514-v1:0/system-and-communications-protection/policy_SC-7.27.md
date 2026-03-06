# POLICY: SC-7.27: Unclassified Non-national Security System Connections

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.27 |
| NIST Control | SC-7.27: Unclassified Non-national Security System Connections |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | boundary protection, external networks, firewalls, network connections, unclassified systems |

## 1. POLICY STATEMENT
All unclassified, non-national security systems are prohibited from directly connecting to external networks without approved boundary protection devices. Direct connections to external networks MUST be mediated through organizational boundary protection mechanisms to control information flows and communications.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Unclassified Systems | YES | All non-national security systems |
| Classified Systems | NO | Covered by separate controls |
| Network Infrastructure | YES | Routers, switches, gateways |
| Cloud Services | YES | When connecting to external networks |
| IoT Devices | YES | All internet-connected devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Deploy and maintain boundary protection devices<br>• Monitor external network connections<br>• Approve connection architectures |
| System Administrators | • Ensure systems comply with connection requirements<br>• Implement approved network configurations<br>• Report direct connection attempts |
| Security Architecture | • Define boundary protection requirements<br>• Review and approve network designs<br>• Maintain approved device inventory |

## 4. RULES
[RULE-01] Unclassified, non-national security systems MUST NOT establish direct connections to external networks without boundary protection devices.
[VALIDATION] IF system_classification = "unclassified" AND external_connection = TRUE AND boundary_protection = FALSE THEN critical_violation

[RULE-02] All external network connections MUST utilize approved boundary protection devices including firewalls, gateways, or security routers.
[VALIDATION] IF external_connection = TRUE AND protection_device NOT IN approved_devices_list THEN violation

[RULE-03] Direct physical or virtual connections to external networks MUST be documented and approved by the Network Security Team prior to implementation.
[VALIDATION] IF connection_type IN ["direct_physical", "direct_virtual"] AND approval_status = "pending" AND days_since_request > 5 THEN violation

[RULE-04] Boundary protection devices MUST be configured to mediate and control all communications between internal systems and external networks.
[VALIDATION] IF boundary_device_configured = FALSE OR traffic_mediation = "bypass" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Network Connection Request - Process for requesting and approving external connections
- [PROC-02] Boundary Device Configuration - Standards for configuring protection devices
- [PROC-03] Connection Monitoring - Continuous monitoring of external network connections
- [PROC-04] Violation Response - Process for addressing unauthorized direct connections

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Network architecture changes, security incidents, new external connections

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Direct Connection]
IF system_type = "unclassified"
AND connection_method = "direct"
AND external_network = TRUE
AND boundary_protection = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Approved Mediated Connection]
IF system_type = "unclassified"
AND external_network = TRUE
AND boundary_device = "approved_firewall"
AND traffic_mediation = "active"
THEN compliance = TRUE

[SCENARIO-03: Cloud Service Direct Connection]
IF service_type = "cloud"
AND connection_type = "direct_internet"
AND boundary_protection = FALSE
AND system_classification = "unclassified"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: IoT Device Bypass]
IF device_type = "IoT"
AND internet_connection = TRUE
AND firewall_bypass = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Emergency Connection Exception]
IF connection_type = "emergency"
AND business_justification = "documented"
AND temporary_approval = TRUE
AND duration < 72_hours
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibit direct connections without boundary protection | [RULE-01] |
| Use approved boundary protection devices | [RULE-02] |
| Document and approve external connections | [RULE-03] |
| Configure devices to mediate communications | [RULE-04] |