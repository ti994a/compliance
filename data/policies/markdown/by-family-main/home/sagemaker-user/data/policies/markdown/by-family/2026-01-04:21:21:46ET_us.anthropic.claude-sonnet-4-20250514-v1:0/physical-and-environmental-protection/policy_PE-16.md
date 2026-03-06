# POLICY: PE-16: Delivery and Removal

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-16 |
| NIST Control | PE-16: Delivery and Removal |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | delivery, removal, system components, facility access, authorization, records |

## 1. POLICY STATEMENT
The organization SHALL authorize and control designated types of system components entering and exiting facilities. Complete records of all system component movements SHALL be maintained to ensure accountability and security.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All primary and secondary facilities |
| Office Buildings | YES | Buildings housing IT infrastructure |
| Warehouses | YES | IT storage and staging facilities |
| Remote Sites | CONDITIONAL | Sites with critical system components |
| Vendor Facilities | NO | Covered under vendor agreements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Define authorized system component types<br>• Oversee delivery/removal procedures<br>• Maintain component movement records |
| Facility Security Officers | • Verify authorizations for component entry/exit<br>• Inspect and log all system components<br>• Coordinate with IT asset management |
| IT Asset Managers | • Provide component specifications<br>• Validate component authenticity<br>• Update asset inventory systems |

## 4. RULES
[RULE-01] All system components entering facilities MUST be pre-authorized through the IT procurement or maintenance request system before delivery.
[VALIDATION] IF component_entering = TRUE AND pre_authorization = FALSE THEN violation

[RULE-02] System components exiting facilities MUST have documented authorization from IT Asset Management or authorized maintenance personnel.
[VALIDATION] IF component_exiting = TRUE AND exit_authorization = FALSE THEN violation

[RULE-03] Facility Security Officers MUST inspect and verify the identity of all system components against authorization documentation before allowing entry or exit.
[VALIDATION] IF component_movement = TRUE AND verification_completed = FALSE THEN violation

[RULE-04] Complete records of system component deliveries and removals MUST be maintained for a minimum of 3 years including date, time, component details, and responsible personnel.
[VALIDATION] IF record_retention_period < 3_years THEN violation

[RULE-05] Delivery and removal areas MUST be physically separated from production system areas and media libraries.
[VALIDATION] IF delivery_area_separated = FALSE OR media_library_access = TRUE THEN violation

[RULE-06] Emergency removal of system components MUST be documented within 24 hours with retroactive authorization from IT Asset Management.
[VALIDATION] IF emergency_removal = TRUE AND documentation_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Component Authorization Process - Pre-approval workflow for component entry/exit
- [PROC-02] Component Inspection and Verification - Physical verification against authorization
- [PROC-03] Movement Record Maintenance - Documentation and retention requirements
- [PROC-04] Emergency Component Removal - Procedures for urgent situations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Server Delivery]
IF component_type = "server"
AND delivery_attempted = TRUE
AND pre_authorization = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Emergency Equipment Removal]
IF component_removal = "emergency"
AND documentation_completed = TRUE
AND documentation_time <= 24_hours
AND retroactive_authorization = TRUE
THEN compliance = TRUE

[SCENARIO-03: Missing Exit Documentation]
IF component_exiting = TRUE
AND exit_authorization = FALSE
AND component_value > $1000
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Inadequate Record Retention]
IF movement_records_exist = TRUE
AND record_age > 3_years
AND records_archived = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Unseparated Delivery Area]
IF delivery_area_location = "production_floor"
AND system_access_possible = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System components authorized when entering facility | [RULE-01], [RULE-03] |
| System components controlled when entering facility | [RULE-03], [RULE-05] |
| System components authorized when exiting facility | [RULE-02], [RULE-06] |
| System components controlled when exiting facility | [RULE-03], [RULE-05] |
| Records of system components maintained | [RULE-04] |