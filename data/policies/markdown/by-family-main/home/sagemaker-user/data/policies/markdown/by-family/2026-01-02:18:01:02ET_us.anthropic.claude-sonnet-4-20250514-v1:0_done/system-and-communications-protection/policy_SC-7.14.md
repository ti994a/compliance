# POLICY: SC-7.14: Protect Against Unauthorized Physical Connections

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.14 |
| NIST Control | SC-7.14: Protect Against Unauthorized Physical Connections |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | physical connections, managed interfaces, cable management, wiring closets, unauthorized access |

## 1. POLICY STATEMENT
The organization SHALL protect all managed network interfaces against unauthorized physical connections through clearly identified and physically separated infrastructure components. Physical access controls MUST enforce limited authorized access to connection points, cable trays, and network distribution equipment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and secondary facilities |
| Network Equipment Rooms | YES | Including IDF/MDF closets |
| Cable Distribution Systems | YES | Trays, conduits, patch panels |
| Shared Multi-Classification Areas | YES | Enhanced controls required |
| Remote Offices | CONDITIONAL | If housing critical systems |
| Vendor/Contractor Areas | YES | When accessing managed interfaces |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Operations Manager | • Maintain physical separation of network infrastructure<br>• Implement cable management standards<br>• Coordinate access control implementation |
| Facilities Security Manager | • Enforce physical access controls to network areas<br>• Monitor and audit facility access<br>• Maintain separation between security domains |
| System Administrators | • Document and label all managed interfaces<br>• Report unauthorized connection attempts<br>• Maintain interface inventory |

## 4. RULES
[RULE-01] All managed network interfaces MUST be physically protected against unauthorized connections through clearly identified and separated cable trays, connection frames, and patch panels.
[VALIDATION] IF managed_interface = TRUE AND (separated_infrastructure = FALSE OR clearly_identified = FALSE) THEN violation

[RULE-02] Systems operating at different security categories or classification levels MUST maintain physical separation of network infrastructure when sharing common facilities.
[VALIDATION] IF security_levels_differ = TRUE AND shared_facility = TRUE AND physical_separation = FALSE THEN critical_violation

[RULE-03] Physical access controls MUST enforce limited authorized access to cable distribution paths, equipment rooms, and connection points for managed interfaces.
[VALIDATION] IF managed_interface_area = TRUE AND access_control_enforced = FALSE THEN violation

[RULE-04] Cable trays, patch panels, and connection frames MUST be clearly labeled to identify the security domain and authorized personnel for each managed interface.
[VALIDATION] IF managed_interface_component = TRUE AND (labeled = FALSE OR security_domain_identified = FALSE) THEN violation

[RULE-05] Unauthorized physical connection attempts MUST be detected and reported within 24 hours of discovery.
[VALIDATION] IF unauthorized_connection_detected = TRUE AND reporting_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Interface Protection Assessment - Quarterly evaluation of managed interface protection controls
- [PROC-02] Cable Management Standards - Implementation and maintenance of separated infrastructure
- [PROC-03] Access Control Enforcement - Verification of physical access restrictions to network areas
- [PROC-04] Unauthorized Connection Response - Detection and remediation of unauthorized physical connections

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving physical access, facility modifications, new system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Multi-Classification Shared Facility]
IF security_classification_level_1 != security_classification_level_2
AND shared_equipment_room = TRUE
AND physical_cable_separation = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Unlabeled Network Infrastructure]
IF managed_interface = TRUE
AND cable_tray_labeled = FALSE
AND patch_panel_identified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Inadequate Access Controls]
IF network_equipment_room = TRUE
AND physical_access_control = "badge_only"
AND authorized_personnel_list = "not_maintained"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Contractor Area Network Access]
IF contractor_workspace = TRUE
AND managed_interface_access = TRUE
AND separated_infrastructure = TRUE
AND access_control_enforced = TRUE
THEN compliance = TRUE

[SCENARIO-05: Unauthorized Connection Discovery]
IF unauthorized_physical_connection = "detected"
AND detection_date = "2024-01-15"
AND reporting_date = "2024-01-17"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Managed interfaces protected against unauthorized physical connections are defined | [RULE-01], [RULE-04] |
| Managed interfaces are protected against unauthorized physical connections | [RULE-01], [RULE-02], [RULE-03] |
| Physical separation maintained for different security levels | [RULE-02] |
| Access controls enforce limited authorized access | [RULE-03] |
| Unauthorized connections detected and reported | [RULE-05] |