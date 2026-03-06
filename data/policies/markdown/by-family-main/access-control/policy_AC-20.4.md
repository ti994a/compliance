# POLICY: AC-20.4: Network Accessible Storage Devices — Prohibited Use

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-20.4 |
| NIST Control | AC-20.4: Network Accessible Storage Devices — Prohibited Use |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network storage, external systems, cloud storage, prohibited devices, access control |

## 1. POLICY STATEMENT
The organization SHALL prohibit the use of specified network-accessible storage devices in external systems to prevent unauthorized data exposure and maintain control over organizational information. All network-accessible storage devices prohibited from use in external systems must be clearly defined and enforced through technical and administrative controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, contractors |
| External systems | YES | Public, hybrid, community cloud systems |
| Network storage devices | YES | Online storage, cloud storage services |
| Mobile devices | YES | When accessing external systems |
| Third-party vendors | YES | When processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define prohibited storage devices<br>• Approve policy exceptions<br>• Oversee compliance monitoring |
| IT Security Team | • Implement technical controls<br>• Monitor usage violations<br>• Maintain prohibited device inventory |
| System Administrators | • Configure blocking mechanisms<br>• Report compliance status<br>• Maintain system documentation |
| End Users | • Comply with usage restrictions<br>• Report suspected violations<br>• Use approved alternatives only |

## 4. RULES
[RULE-01] The organization MUST maintain a documented list of network-accessible storage devices prohibited from use in external systems.
[VALIDATION] IF prohibited_device_list = NULL OR last_updated > 365_days THEN violation

[RULE-02] Technical controls MUST be implemented to prevent access to prohibited network-accessible storage devices from external systems.
[VALIDATION] IF technical_controls_implemented = FALSE OR bypass_possible = TRUE THEN critical_violation

[RULE-03] Users SHALL NOT utilize any prohibited network-accessible storage devices when operating in external systems.
[VALIDATION] IF user_accessed_prohibited_storage = TRUE AND system_type = "external" THEN violation

[RULE-04] All external system connections MUST be configured to block access to prohibited network-accessible storage devices.
[VALIDATION] IF external_connection_configured = TRUE AND prohibited_storage_blocked = FALSE THEN violation

[RULE-05] Violations of prohibited storage device usage MUST be logged and reported within 24 hours of detection.
[VALIDATION] IF violation_detected = TRUE AND reporting_time > 24_hours THEN process_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Prohibited Storage Device Inventory Management - Quarterly review and update of prohibited device list
- [PROC-02] Technical Control Implementation - Deploy and maintain blocking mechanisms for prohibited devices
- [PROC-03] Violation Response - Investigate and remediate prohibited storage device usage incidents
- [PROC-04] External System Assessment - Evaluate external systems for prohibited storage device access capabilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New external system deployments, security incidents involving storage devices, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Employee Using Personal Cloud Storage]
IF user_type = "employee"
AND storage_service = "personal_cloud_storage"
AND system_environment = "external"
AND service_on_prohibited_list = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Accessing Approved Storage]
IF user_type = "contractor"
AND storage_service = "approved_enterprise_storage"
AND system_environment = "external"
AND technical_controls_active = TRUE
THEN compliance = TRUE

[SCENARIO-03: Blocked Prohibited Service Access]
IF access_attempt = "prohibited_storage_service"
AND technical_controls_implemented = TRUE
AND access_blocked = TRUE
AND incident_logged = TRUE
THEN compliance = TRUE

[SCENARIO-04: Unmonitored External System]
IF system_type = "external"
AND prohibited_storage_monitoring = FALSE
AND connection_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Emergency Exception Usage]
IF storage_service_prohibited = TRUE
AND emergency_exception_approved = TRUE
AND usage_time_limited = TRUE
AND security_review_scheduled = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Network-accessible storage devices prohibited from use in external systems are defined | [RULE-01] |
| Use of prohibited network-accessible storage devices is prevented in external systems | [RULE-02], [RULE-03], [RULE-04] |
| Violations are detected and reported | [RULE-05] |
| Technical controls enforce prohibition | [RULE-02], [RULE-04] |