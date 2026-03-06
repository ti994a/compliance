# POLICY: AC-18: Wireless Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-18 |
| NIST Control | AC-18: Wireless Access |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | wireless, access, configuration, authorization, 802.11, bluetooth, authentication |

## 1. POLICY STATEMENT
All wireless access technologies must be properly configured, documented, and authorized before connecting to organizational systems. Each type of wireless access requires specific configuration requirements, connection requirements, and implementation guidance to ensure secure connectivity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Corporate Networks | YES | All wired/wireless infrastructure |
| Cloud Systems | YES | Hybrid cloud wireless connections |
| Mobile Devices | YES | Company and BYOD devices |
| IoT Devices | YES | All wireless-enabled IoT systems |
| Guest Networks | YES | Visitor and temporary access |
| Contractor Systems | CONDITIONAL | Must meet same requirements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Establish wireless configuration standards<br>• Review and approve wireless access requests<br>• Monitor wireless network security |
| IT Operations | • Implement approved wireless configurations<br>• Maintain wireless access documentation<br>• Perform regular wireless security assessments |
| System Owners | • Request wireless access authorization<br>• Ensure compliance with wireless policies<br>• Report wireless security incidents |

## 4. RULES
[RULE-01] Configuration requirements MUST be established and documented for each type of wireless access technology before deployment.
[VALIDATION] IF wireless_technology_deployed = TRUE AND configuration_requirements_documented = FALSE THEN violation

[RULE-02] Connection requirements MUST be defined and enforced for each wireless access type, including authentication protocols and encryption standards.
[VALIDATION] IF wireless_connection_active = TRUE AND connection_requirements_defined = FALSE THEN violation

[RULE-03] Implementation guidance MUST be created and maintained for each wireless technology, including security controls and monitoring procedures.
[VALIDATION] IF wireless_technology_type EXISTS AND implementation_guidance_exists = FALSE THEN violation

[RULE-04] Each type of wireless access MUST be formally authorized by the Network Security Team prior to allowing system connections.
[VALIDATION] IF wireless_access_enabled = TRUE AND formal_authorization = FALSE THEN critical_violation

[RULE-05] Wireless networks MUST use WPA3 or equivalent encryption, with WPA2 as minimum acceptable standard for legacy systems.
[VALIDATION] IF wireless_encryption IN ["WEP", "Open", "WPS"] THEN critical_violation

[RULE-06] Wireless access points MUST be configured with unique, complex administrative credentials and disable default settings.
[VALIDATION] IF access_point_config = "default" OR admin_password = "default" THEN critical_violation

[RULE-07] Guest wireless networks MUST be isolated from corporate networks and require separate authorization processes.
[VALIDATION] IF guest_network_isolation = FALSE OR guest_access_unauthorized = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Wireless Technology Assessment - Evaluate security requirements for new wireless technologies
- [PROC-02] Wireless Access Authorization - Formal approval process for wireless system connections
- [PROC-03] Wireless Configuration Management - Standardized configuration and deployment procedures
- [PROC-04] Wireless Security Monitoring - Continuous monitoring of wireless network security

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New wireless technology deployment, security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Wireless Access Point]
IF wireless_access_point_detected = TRUE
AND formal_authorization = FALSE
AND network_connection_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Weak Wireless Encryption]
IF wireless_network_active = TRUE
AND encryption_standard IN ["WEP", "Open"]
AND corporate_data_accessible = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Configuration Documentation]
IF wireless_technology_deployed = TRUE
AND deployment_date > 30_days_ago
AND configuration_requirements_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Guest Network Isolation Failure]
IF guest_network_active = TRUE
AND corporate_network_accessible = TRUE
AND network_segmentation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Properly Authorized Wireless Deployment]
IF wireless_access_request_approved = TRUE
AND configuration_requirements_met = TRUE
AND implementation_guidance_followed = TRUE
AND security_monitoring_enabled = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Configuration requirements established for each wireless type | [RULE-01] |
| Connection requirements established for each wireless type | [RULE-02] |
| Implementation guidance established for each wireless type | [RULE-03] |
| Each wireless access type authorized prior to connections | [RULE-04] |