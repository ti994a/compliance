# POLICY: PE-3.1: System Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3.1 |
| NIST Control | PE-3.1: System Access |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | physical access, system components, authorization, facility security, access control |

## 1. POLICY STATEMENT
The organization SHALL enforce physical access authorizations specifically for system components in addition to general facility access controls. Physical spaces containing concentrated system components MUST have enhanced access controls beyond standard facility protections.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary system component locations |
| Server Rooms | YES | Areas with concentrated IT equipment |
| Network Closets | YES | Critical network infrastructure |
| Cloud Provider Facilities | CONDITIONAL | When under organizational control |
| Office Spaces | CONDITIONAL | Only if containing system components |
| Remote Facilities | YES | All locations with system components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Implement system-specific access controls<br>• Define areas requiring enhanced protection<br>• Maintain access authorization records |
| Facility Manager | • Coordinate facility and system access controls<br>• Ensure physical security infrastructure<br>• Monitor access control effectiveness |
| IT Security Officer | • Define system component protection requirements<br>• Review access authorization requests<br>• Validate security control implementation |

## 4. RULES
[RULE-01] Areas containing system components MUST implement physical access controls that are separate from and additional to general facility access controls.
[VALIDATION] IF area_contains_system_components = TRUE AND system_specific_access_controls = FALSE THEN violation

[RULE-02] Physical access authorizations for system areas MUST be explicitly granted and documented separately from facility access permissions.
[VALIDATION] IF system_area_access = TRUE AND explicit_system_authorization = FALSE THEN violation

[RULE-03] Areas with concentrated system components (3+ critical systems) MUST have enhanced physical access controls including biometric or multi-factor authentication.
[VALIDATION] IF critical_system_count >= 3 AND enhanced_access_control = FALSE THEN violation

[RULE-04] System component access authorizations MUST be reviewed and revalidated every 90 days.
[VALIDATION] IF last_authorization_review > 90_days THEN violation

[RULE-05] Physical access to system components MUST be logged with individual identification, timestamp, and purpose.
[VALIDATION] IF system_access_occurred = TRUE AND (user_id = NULL OR timestamp = NULL OR purpose = NULL) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Area Classification - Identify and classify areas containing system components
- [PROC-02] Enhanced Access Control Implementation - Deploy additional controls for system areas
- [PROC-03] System Access Authorization - Process for granting system-specific access
- [PROC-04] Access Log Review - Regular review of system area access logs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility changes, system relocations, compliance findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Data Center Access]
IF location_type = "data_center"
AND system_components_present = TRUE
AND access_control_type = "facility_only"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Server Room Access]
IF user_type = "contractor"
AND area_type = "server_room"
AND system_specific_authorization = TRUE
AND facility_authorization = TRUE
THEN compliance = TRUE

[SCENARIO-03: Unlogged System Access]
IF area_contains_critical_systems = TRUE
AND physical_access_occurred = TRUE
AND access_logged = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Expired System Authorization]
IF system_area_access = "granted"
AND authorization_review_date < (current_date - 90_days)
AND access_still_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Network Closet Multi-Factor]
IF area_type = "network_closet"
AND critical_system_count >= 3
AND access_method = "badge_only"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical access authorizations to the system are enforced | RULE-02, RULE-04 |
| Physical access controls are enforced for facility spaces containing system components | RULE-01, RULE-03 |
| System component areas are properly identified and protected | RULE-01, RULE-03 |
| Access activities are properly documented and monitored | RULE-05 |