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
All unclassified, non-national security systems are prohibited from establishing direct connections to external networks without mandatory boundary protection devices. Direct connections to external networks MUST be mediated through approved boundary protection mechanisms to control information flows and communications.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Unclassified Systems | YES | All non-national security systems |
| Classified Systems | NO | Covered by separate controls |
| Development Systems | YES | When connecting to external networks |
| Test Systems | YES | When connecting to external networks |
| Contractor Systems | YES | When integrated with organization network |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Deploy and maintain boundary protection devices<br>• Monitor external network connections<br>• Approve connection architectures |
| System Administrators | • Implement connection controls<br>• Document system connections<br>• Report direct connection attempts |
| CISO | • Define boundary protection requirements<br>• Approve exceptions<br>• Oversee compliance monitoring |

## 4. RULES
[RULE-01] Unclassified, non-national security systems MUST NOT establish direct physical or virtual connections to external networks without boundary protection devices.
[VALIDATION] IF system_classification = "unclassified" AND connection_type = "direct" AND boundary_protection = FALSE THEN critical_violation

[RULE-02] All external network connections MUST be mediated through approved boundary protection devices including firewalls, gateways, or routers.
[VALIDATION] IF external_connection = TRUE AND boundary_device_approved = FALSE THEN violation

[RULE-03] Direct connections SHALL be documented and include justification for the specific boundary protection device selected.
[VALIDATION] IF direct_connection_exists = TRUE AND documentation_complete = FALSE THEN violation

[RULE-04] Boundary protection devices MUST be configured to control and monitor information flows between internal systems and external networks.
[VALIDATION] IF boundary_device_deployed = TRUE AND monitoring_enabled = FALSE THEN violation

[RULE-05] System administrators MUST report any attempts to bypass boundary protection devices within 4 hours of detection.
[VALIDATION] IF bypass_attempt_detected = TRUE AND reporting_time > 4_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Connection Approval - Process for reviewing and approving external network connections
- [PROC-02] Boundary Device Configuration - Standards for configuring firewalls, gateways, and routers
- [PROC-03] Connection Monitoring - Procedures for monitoring and logging external network traffic
- [PROC-04] Violation Response - Process for responding to direct connection violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, architecture changes, new external connections, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Direct Internet Connection]
IF system_type = "unclassified"
AND connection_destination = "internet"
AND firewall_present = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: VPN with Boundary Protection]
IF system_type = "unclassified"
AND connection_type = "VPN"
AND boundary_device = "approved_gateway"
AND monitoring_enabled = TRUE
THEN compliance = TRUE

[SCENARIO-03: Development System Direct Connection]
IF system_purpose = "development"
AND external_connection = TRUE
AND boundary_protection = FALSE
AND business_justification = "testing"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Partner Network Connection]
IF connection_destination = "partner_network"
AND boundary_device = "approved_firewall"
AND traffic_filtering = TRUE
AND connection_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Bypass Attempt]
IF direct_connection_attempted = TRUE
AND boundary_device_bypassed = TRUE
AND incident_reported = FALSE
AND detection_time > 4_hours
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibit direct connections without boundary protection | [RULE-01] |
| Require approved boundary protection devices | [RULE-02] |
| Document connection requirements | [RULE-03] |
| Configure boundary devices for monitoring | [RULE-04] |
| Report bypass attempts | [RULE-05] |