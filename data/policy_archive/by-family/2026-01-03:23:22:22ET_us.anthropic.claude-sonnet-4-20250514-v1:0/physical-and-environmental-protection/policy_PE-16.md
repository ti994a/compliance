# POLICY: PE-16: Delivery and Removal

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-16 |
| NIST Control | PE-16: Delivery and Removal |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | delivery, removal, system components, facility access, authorization, records |

## 1. POLICY STATEMENT
All system components entering and exiting company facilities must be authorized and controlled through documented procedures. The organization maintains comprehensive records of all system component movements to ensure security and accountability.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All facilities housing IT systems | YES | Primary and backup data centers, offices |
| System components | YES | Servers, networking equipment, storage devices, laptops |
| Third-party vendors | YES | When delivering or removing equipment |
| Employees | YES | When transporting company equipment |
| Contractors | YES | When handling system components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facility Security Manager | • Authorize component entry/exit<br>• Maintain delivery/removal records<br>• Oversee access control to delivery areas |
| IT Asset Manager | • Validate component specifications<br>• Update asset inventory<br>• Coordinate with procurement |
| Security Operations | • Monitor facility access<br>• Investigate unauthorized movements<br>• Enforce isolation procedures |

## 4. RULES
[RULE-01] All system components MUST receive written authorization before entering or exiting any facility housing information systems.
[VALIDATION] IF component_movement = TRUE AND written_authorization = FALSE THEN violation

[RULE-02] Delivery and removal areas MUST be physically isolated from system and media libraries during component transfers.
[VALIDATION] IF component_transfer_active = TRUE AND isolation_controls = FALSE THEN violation

[RULE-03] Records of all system component movements MUST be maintained for a minimum of 3 years and include component type, serial number, date/time, authorization reference, and responsible personnel.
[VALIDATION] IF movement_record_missing = TRUE OR record_retention < 3_years THEN violation

[RULE-04] Access to delivery areas MUST be restricted to authorized personnel only during component entry/exit operations.
[VALIDATION] IF delivery_area_access = TRUE AND personnel_authorized = FALSE THEN violation

[RULE-05] All incoming system components MUST be inspected and verified against purchase orders or service requests before facility entry.
[VALIDATION] IF component_entry = TRUE AND (inspection_complete = FALSE OR verification_complete = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Authorization Process - Formal approval workflow for equipment entry/exit
- [PROC-02] Delivery Area Management - Procedures for isolating and controlling delivery zones
- [PROC-03] Movement Documentation - Standardized recording of all component transfers
- [PROC-04] Vendor Escort Protocol - Requirements for supervising third-party deliveries/removals

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized equipment, facility modifications, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Equipment Entry]
IF system_component_entering = TRUE
AND written_authorization = FALSE
AND facility_security_notified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Delivery Records]
IF component_delivery_occurred = TRUE
AND movement_record_created = FALSE
AND 24_hours_elapsed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unescorted Vendor Access]
IF vendor_present = TRUE
AND delivery_area_access = TRUE
AND authorized_escort = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Proper Equipment Removal]
IF system_component_exiting = TRUE
AND written_authorization = TRUE
AND movement_record_complete = TRUE
AND delivery_area_isolated = TRUE
THEN compliance = TRUE

[SCENARIO-05: Inadequate Area Isolation]
IF component_transfer_active = TRUE
AND delivery_area_isolated = FALSE
AND system_library_accessible = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System components authorized when entering facility | [RULE-01] |
| System components controlled when entering facility | [RULE-02], [RULE-04] |
| System components authorized when exiting facility | [RULE-01] |
| System components controlled when exiting facility | [RULE-02], [RULE-04] |
| Records of system components maintained | [RULE-03] |