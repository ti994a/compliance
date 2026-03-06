# POLICY: SC-7.27: Unclassified Non-national Security System Connections

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.27 |
| NIST Control | SC-7.27: Unclassified Non-national Security System Connections |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | boundary protection, external networks, firewalls, direct connections, unclassified systems |

## 1. POLICY STATEMENT
All unclassified, non-national security systems are prohibited from establishing direct connections to external networks without mandatory boundary protection devices. Direct connections to external networks must be mediated through approved boundary protection mechanisms such as firewalls, gateways, or routers.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Unclassified information systems | YES | All systems processing unclassified data |
| Non-national security systems | YES | Business systems, development environments |
| Network infrastructure | YES | Routers, switches, gateways |
| Cloud services | YES | Hybrid cloud connections to external networks |
| IoT devices | YES | All connected devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Deploy and maintain boundary protection devices<br>• Monitor external network connections<br>• Approve network architecture changes |
| System Administrators | • Ensure systems comply with connection requirements<br>• Report unauthorized direct connections<br>• Implement approved network configurations |
| Security Architecture Team | • Define approved boundary protection devices<br>• Review network connection requests<br>• Maintain network security standards |

## 4. RULES
[RULE-01] Unclassified, non-national security systems MUST NOT establish direct connections to external networks without approved boundary protection devices.
[VALIDATION] IF system_classification = "unclassified" AND connection_type = "direct" AND boundary_protection = FALSE THEN critical_violation

[RULE-02] All external network connections MUST be mediated through approved boundary protection devices including firewalls, gateways, or routers.
[VALIDATION] IF external_connection = TRUE AND (firewall_present = FALSE AND gateway_present = FALSE AND router_present = FALSE) THEN violation

[RULE-03] Boundary protection devices MUST be configured according to organizational security standards and maintained with current security patches.
[VALIDATION] IF boundary_device_configured = FALSE OR patch_status = "outdated" THEN violation

[RULE-04] Network administrators MUST document and approve all external network connection architectures before implementation.
[VALIDATION] IF external_connection = TRUE AND (documentation_complete = FALSE OR approval_status = "pending") THEN violation

[RULE-05] Direct physical or virtual connections bypassing boundary protection devices SHALL NOT be permitted for any unclassified system.
[VALIDATION] IF connection_bypasses_protection = TRUE AND system_classification = "unclassified" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Connection Approval Process - Review and approval workflow for external connections
- [PROC-02] Boundary Device Configuration Management - Standards for configuring and maintaining protection devices
- [PROC-03] Connection Monitoring and Auditing - Continuous monitoring of network connections and traffic flows
- [PROC-04] Incident Response for Unauthorized Connections - Process for detecting and remediating policy violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized connections, major network architecture changes, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Direct Internet Connection]
IF system_type = "unclassified_business_system"
AND connection_destination = "internet"
AND firewall_protection = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Cloud Service Direct Connection]
IF system_classification = "unclassified"
AND connection_type = "direct_vpn"
AND boundary_protection_bypass = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Approved Gateway Connection]
IF system_type = "unclassified"
AND external_connection = TRUE
AND approved_gateway = TRUE
AND gateway_configured_properly = TRUE
THEN compliance = TRUE

[SCENARIO-04: IoT Device Direct Connection]
IF device_type = "IoT"
AND system_classification = "unclassified"
AND internet_connection = "direct"
AND firewall_present = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Emergency Bypass]
IF connection_type = "emergency_bypass"
AND boundary_protection = FALSE
AND emergency_authorization = FALSE
AND duration > 4_hours
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibit direct connections without boundary protection | [RULE-01], [RULE-05] |
| Require mediation through boundary devices | [RULE-02] |
| Maintain boundary protection device security | [RULE-03] |
| Document and approve connection architectures | [RULE-04] |