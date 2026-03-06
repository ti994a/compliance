# POLICY: PE-16: Delivery and Removal

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-16 |
| NIST Control | PE-16: Delivery and Removal |
| Version | 1.0 |
| Owner | Chief Physical Security Officer |
| Keywords | delivery, removal, system components, facility access, authorization, records |

## 1. POLICY STATEMENT
The organization SHALL authorize and control all system components entering and exiting company facilities. Complete records of all system component movements SHALL be maintained to ensure accountability and security.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All physical facilities | YES | Including data centers, offices, warehouses |
| System components | YES | Servers, networking equipment, storage devices, workstations |
| Third-party vendors | YES | When delivering or removing equipment |
| Employees | YES | When transporting system components |
| Contractors | YES | When handling system components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facility Security Manager | • Authorize component entry/exit<br>• Maintain delivery/removal records<br>• Oversee access control to delivery areas |
| IT Asset Manager | • Validate component specifications<br>• Update asset inventory<br>• Coordinate with procurement |
| Security Guards | • Verify authorizations<br>• Escort vendors in restricted areas<br>• Document component movements |

## 4. RULES
[RULE-01] All system components entering facilities MUST have pre-authorization from the Facility Security Manager or designated representative.
[VALIDATION] IF component_entry = TRUE AND pre_authorization = FALSE THEN violation

[RULE-02] System components exiting facilities MUST be authorized by both the IT Asset Manager and Facility Security Manager for components valued over $1,000.
[VALIDATION] IF component_exit = TRUE AND component_value > 1000 AND (it_authorization = FALSE OR facility_authorization = FALSE) THEN violation

[RULE-03] Delivery and removal records MUST be maintained for a minimum of 3 years and include component type, serial number, date/time, authorizing personnel, and purpose.
[VALIDATION] IF record_age > 3_years AND record_retention = TRUE THEN compliant
[VALIDATION] IF missing_required_fields > 0 THEN violation

[RULE-04] Delivery areas MUST be physically separated from system and media libraries with controlled access.
[VALIDATION] IF delivery_area_separation = FALSE OR controlled_access = FALSE THEN violation

[RULE-05] All personnel handling system component delivery/removal MUST be escorted in restricted areas unless they possess appropriate facility clearance.
[VALIDATION] IF restricted_area = TRUE AND facility_clearance = FALSE AND escort = FALSE THEN violation

[RULE-06] Emergency removal of system components MUST be documented within 4 hours with retroactive authorization obtained within 24 hours.
[VALIDATION] IF emergency_removal = TRUE AND documentation_time > 4_hours THEN violation
[VALIDATION] IF emergency_removal = TRUE AND retroactive_auth_time > 24_hours THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Authorization Process - Define approval workflow and required documentation
- [PROC-02] Delivery Area Access Control - Establish physical security measures for delivery zones
- [PROC-03] Record Keeping Standards - Specify required data fields and retention requirements
- [PROC-04] Emergency Procedures - Define process for urgent component removal situations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility changes, regulatory updates, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Component Entry]
IF component_entering_facility = TRUE
AND pre_authorization = FALSE
AND emergency_situation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Delivery Records]
IF component_movement_record = TRUE
AND (serial_number = NULL OR date_time = NULL OR authorizing_personnel = NULL)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: High-Value Component Exit]
IF component_value > 1000
AND component_exiting = TRUE
AND (it_manager_approval = FALSE OR facility_manager_approval = FALSE)
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Unescorted Vendor in Restricted Area]
IF personnel_type = "vendor"
AND area_classification = "restricted"
AND facility_clearance = FALSE
AND escort_present = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Emergency Removal Documentation]
IF removal_type = "emergency"
AND documentation_time <= 4_hours
AND retroactive_authorization_time <= 24_hours
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System components authorized when entering facility | [RULE-01] |
| System components controlled when entering facility | [RULE-01], [RULE-05] |
| System components authorized when exiting facility | [RULE-02] |
| System components controlled when exiting facility | [RULE-02], [RULE-05] |
| Records of system components maintained | [RULE-03] |
| Delivery area access restrictions | [RULE-04] |