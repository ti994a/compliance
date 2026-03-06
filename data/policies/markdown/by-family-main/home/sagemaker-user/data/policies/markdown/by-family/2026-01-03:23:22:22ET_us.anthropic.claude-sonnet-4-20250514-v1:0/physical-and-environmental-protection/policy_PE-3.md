# POLICY: PE-3: Physical Access Control

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3 |
| NIST Control | PE-3: Physical Access Control |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | physical access, facility security, visitor control, access logs, biometric, card readers |

## 1. POLICY STATEMENT
The organization SHALL enforce physical access authorizations at all facility entry and exit points where information systems reside, maintain comprehensive audit logs of physical access events, and implement controls for publicly accessible areas. All physical access devices, visitor activities, and access credentials MUST be properly managed and regularly reviewed.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary facilities housing critical systems |
| Office Buildings | YES | Areas containing information systems |
| Server Rooms | YES | All dedicated IT equipment areas |
| Publicly Accessible Areas | CONDITIONAL | Only areas adjacent to controlled spaces |
| Remote Work Locations | NO | Covered under separate telework policy |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Oversee physical access control implementation<br>• Maintain access authorization records<br>• Conduct regular access device inventories |
| Facility Security Officers | • Verify individual access authorizations<br>• Escort visitors as required<br>• Monitor physical access control systems |
| IT Security Team | • Review physical access audit logs<br>• Coordinate with physical security on system-related access<br>• Validate access controls for IT equipment areas |

## 4. RULES
[RULE-01] Individual access authorizations MUST be verified before granting physical access to any facility containing information systems.
[VALIDATION] IF access_granted = TRUE AND authorization_verified = FALSE THEN violation

[RULE-02] Physical access audit logs MUST be maintained for all controlled entry and exit points with retention period of minimum 90 days.
[VALIDATION] IF controlled_access_point = TRUE AND audit_log_maintained = FALSE THEN violation

[RULE-03] Visitors MUST be escorted at all times in areas containing sensitive information systems or when accessing non-public areas.
[VALIDATION] IF visitor = TRUE AND sensitive_area = TRUE AND escort_present = FALSE THEN violation

[RULE-04] Physical access devices (keys, cards, biometric data) MUST be inventoried every 90 days and secured when not in use.
[VALIDATION] IF last_inventory_date > 90_days AND access_device_type IN ["keys", "cards", "biometric"] THEN violation

[RULE-05] Access credentials MUST be changed within 24 hours when personnel are terminated or transferred, or when compromise is suspected.
[VALIDATION] IF (employee_status = "terminated" OR employee_status = "transferred") AND credential_change_time > 24_hours THEN critical_violation

[RULE-06] Publicly accessible areas adjacent to controlled spaces MUST implement physical barriers and monitoring to prevent unauthorized access to non-public areas.
[VALIDATION] IF public_area_adjacent = TRUE AND (barriers_present = FALSE OR monitoring_active = FALSE) THEN violation

[RULE-07] Lost keys or compromised combinations MUST be reported immediately and replaced within 4 hours of discovery.
[VALIDATION] IF (key_status = "lost" OR combination_status = "compromised") AND replacement_time > 4_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Access Authorization - Process for granting, modifying, and revoking facility access
- [PROC-02] Visitor Management - Procedures for visitor registration, escort assignment, and activity monitoring
- [PROC-03] Access Device Inventory - Quarterly inventory and accountability procedures for physical access devices
- [PROC-04] Emergency Access - Procedures for emergency facility access and post-incident credential changes
- [PROC-05] Audit Log Review - Monthly review procedures for physical access logs and anomaly investigation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility changes, technology upgrades, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor After-Hours Access]
IF user_type = "contractor"
AND access_time = "after_hours"
AND authorization_verified = TRUE
AND escort_present = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Visitor in Server Room]
IF user_type = "visitor"
AND location = "server_room"
AND escort_present = TRUE
AND visitor_logged = TRUE
THEN compliance = TRUE

[SCENARIO-03: Terminated Employee Badge Access]
IF employee_status = "terminated"
AND termination_date < current_date
AND badge_access_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Access Log]
IF controlled_entry_point = TRUE
AND access_occurred = TRUE
AND audit_log_entry = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Public Area Tailgating]
IF area_type = "public_adjacent"
AND unauthorized_access_attempt = TRUE
AND physical_barrier_bypassed = TRUE
AND monitoring_alert_generated = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Verify individual access authorizations before granting facility access | [RULE-01] |
| Maintain physical access audit logs for entry/exit points | [RULE-02] |
| Escort visitors and control visitor activity | [RULE-03] |
| Inventory physical access devices at defined frequency | [RULE-04] |
| Change combinations/keys when personnel transferred or terminated | [RULE-05] |
| Control access to publicly accessible areas | [RULE-06] |
| Secure keys, combinations, and other physical access devices | [RULE-07] |