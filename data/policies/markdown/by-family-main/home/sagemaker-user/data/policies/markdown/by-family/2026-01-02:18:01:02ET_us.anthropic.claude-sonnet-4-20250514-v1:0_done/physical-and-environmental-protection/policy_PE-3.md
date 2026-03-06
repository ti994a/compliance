# POLICY: PE-3: Physical Access Control

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3 |
| NIST Control | PE-3: Physical Access Control |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | physical access, facility security, visitor control, access logs, biometrics, keys |

## 1. POLICY STATEMENT
The organization SHALL enforce physical access controls at all facility entry and exit points where information systems reside, maintain audit logs of physical access events, and implement additional controls for publicly accessible areas. All physical access devices, visitor activities, and access authorizations must be properly managed and monitored.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary facilities housing critical systems |
| Office Buildings | YES | Areas containing IT equipment or sensitive data |
| Remote Facilities | YES | Satellite offices with system components |
| Third-party Colocation | YES | Must meet equivalent standards |
| Public Areas | CONDITIONAL | Only areas with system components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Implement and maintain physical access control systems<br>• Manage visitor escort procedures<br>• Conduct regular access device inventories |
| Security Operations Center | • Monitor physical access logs and alerts<br>• Investigate access anomalies<br>• Coordinate incident response for physical breaches |
| HR Department | • Notify facilities team of personnel changes within 4 hours<br>• Maintain current employee authorization lists<br>• Process visitor access requests |

## 4. RULES
[RULE-01] Individual access authorizations MUST be verified before granting physical access to any facility containing information systems.
[VALIDATION] IF access_granted = TRUE AND authorization_verified = FALSE THEN violation

[RULE-02] Physical access audit logs MUST be maintained for all designated entry and exit points with retention period of minimum 90 days.
[VALIDATION] IF entry_point_designated = TRUE AND audit_log_exists = FALSE THEN violation
[VALIDATION] IF audit_log_retention < 90_days THEN violation

[RULE-03] Visitors MUST be escorted at all times in non-public areas and visitor activity MUST be logged and monitored.
[VALIDATION] IF visitor_in_restricted_area = TRUE AND escort_present = FALSE THEN critical_violation

[RULE-04] Physical access devices (keys, cards, combinations) MUST be inventoried quarterly and secured when not in use.
[VALIDATION] IF last_inventory_date > 90_days THEN violation
[VALIDATION] IF access_device_unsecured = TRUE THEN violation

[RULE-05] Access combinations and keys MUST be changed within 24 hours when compromised, lost, or when personnel possessing them are terminated or transferred.
[VALIDATION] IF (key_lost = TRUE OR combination_compromised = TRUE OR personnel_terminated = TRUE) AND change_time > 24_hours THEN critical_violation

[RULE-06] Multi-factor authentication MUST be implemented for access to critical facility areas housing production systems.
[VALIDATION] IF facility_area_criticality = "high" AND authentication_factors < 2 THEN violation

[RULE-07] Physical access control systems MUST generate real-time alerts for unauthorized access attempts and system failures.
[VALIDATION] IF unauthorized_attempt = TRUE AND alert_generated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Access Authorization - Process for granting, modifying, and revoking facility access
- [PROC-02] Visitor Management - Registration, escort assignment, and activity monitoring procedures  
- [PROC-03] Access Device Management - Inventory, distribution, and lifecycle management of physical access devices
- [PROC-04] Emergency Access - Procedures for facility access during emergencies or system failures
- [PROC-05] Access Log Review - Regular analysis and investigation of physical access audit logs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents, facility changes, regulatory updates, personnel changes in key roles

## 7. SCENARIO PATTERNS
[SCENARIO-01: Terminated Employee Badge Access]
IF employee_status = "terminated"
AND badge_deactivated = FALSE  
AND termination_notification_time > 4_hours
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Unescorted Visitor in Server Room]
IF visitor_type = "external"
AND current_location = "server_room"
AND escort_present = FALSE
AND area_classification = "restricted"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Access Log Data]
IF facility_entry_point = "main_datacenter" 
AND designated_for_logging = TRUE
AND log_data_available = FALSE
AND time_period = "last_30_days"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Overdue Key Inventory]
IF last_inventory_date > 90_days
AND access_device_type = "physical_keys"
AND facility_classification = "restricted"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Compromised Access Code Not Changed]
IF access_code_compromised = TRUE
AND incident_reported_time = 8_hours_ago
AND access_code_changed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Verify individual access authorizations before granting facility access | [RULE-01] |
| Maintain physical access audit logs for designated entry/exit points | [RULE-02] |
| Escort visitors and control visitor activity in restricted areas | [RULE-03] |
| Inventory physical access devices quarterly | [RULE-04] |
| Change combinations/keys when compromised or personnel changes | [RULE-05] |
| Control ingress and egress using approved mechanisms | [RULE-06] |
| Generate alerts for unauthorized access attempts | [RULE-07] |