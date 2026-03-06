# POLICY: MA-5.5: Non-system Maintenance

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MA-5.5 |
| NIST Control | MA-5.5: Non-system Maintenance |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | maintenance, access authorization, physical proximity, non-escorted personnel, custodial, facility |

## 1. POLICY STATEMENT
All non-escorted personnel performing maintenance activities not directly associated with information systems but working in physical proximity to systems must possess valid access authorizations. This includes facility maintenance, custodial, and physical plant personnel who may gain incidental access to system areas during their duties.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Facility maintenance personnel | YES | All contractors and employees |
| Custodial staff | YES | Internal and outsourced staff |
| Physical plant personnel | YES | HVAC, electrical, plumbing technicians |
| Delivery personnel | YES | When working in system areas |
| Construction workers | YES | During facility modifications |
| Direct system maintenance staff | NO | Covered under MA-5 base control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facility Security Manager | • Maintain registry of authorized non-system maintenance personnel<br>• Coordinate access authorization processes<br>• Conduct periodic access reviews |
| Physical Access Control Administrator | • Issue and manage access credentials<br>• Monitor proximity-based access events<br>• Maintain access control records |
| Information System Security Officer | • Define system proximity boundaries<br>• Approve access authorization requirements<br>• Review maintenance activity logs |

## 4. RULES
[RULE-01] Non-escorted personnel performing maintenance activities within the defined physical proximity of information systems MUST possess current access authorizations before beginning work.
[VALIDATION] IF personnel_type = "non_system_maintenance" AND escort_status = "unescorted" AND system_proximity = TRUE AND access_authorization = "invalid" THEN violation

[RULE-02] Access authorizations for non-system maintenance personnel MUST include background verification appropriate to the sensitivity level of systems in proximity.
[VALIDATION] IF system_sensitivity_level = "high" AND background_check_level < "moderate" THEN violation

[RULE-03] Physical proximity boundaries for systems MUST be documented and clearly marked to identify areas requiring access authorization.
[VALIDATION] IF proximity_boundary_documented = FALSE OR boundary_markings = "absent" THEN violation

[RULE-04] Access authorizations for non-system maintenance personnel MUST be reviewed and revalidated at least annually or upon change in system sensitivity.
[VALIDATION] IF last_authorization_review > 365_days OR (system_sensitivity_changed = TRUE AND authorization_updated = FALSE) THEN violation

[RULE-05] All non-system maintenance activities in system proximity areas MUST be logged with personnel identification, time, and purpose.
[VALIDATION] IF maintenance_activity = TRUE AND system_proximity = TRUE AND activity_logged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Non-System Maintenance Personnel Authorization - Process for vetting and authorizing facility maintenance staff
- [PROC-02] Proximity Boundary Definition - Method for determining and marking system proximity areas
- [PROC-03] Access Authorization Review - Annual review and revalidation of maintenance personnel access
- [PROC-04] Maintenance Activity Logging - Documentation requirements for proximity maintenance work

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Security incidents involving maintenance personnel, facility modifications, system relocations, changes in system sensitivity levels

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Custodial Access]
IF personnel_type = "custodial"
AND system_proximity = TRUE
AND access_authorization = "expired"
AND escort_present = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Emergency Facility Repair]
IF maintenance_type = "emergency_repair"
AND system_proximity = TRUE
AND access_authorization = "pending"
AND temporary_escort_assigned = TRUE
THEN compliance = TRUE

[SCENARIO-03: Contractor Background Check Gap]
IF personnel_type = "contractor"
AND system_sensitivity_level = "high"
AND background_check_level = "basic"
AND proximity_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Undocumented Proximity Boundaries]
IF system_location = "data_center"
AND proximity_boundaries_defined = FALSE
AND non_system_maintenance_occurring = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Authorization and Logging]
IF personnel_type = "HVAC_technician"
AND access_authorization = "current"
AND system_proximity = TRUE
AND activity_logged = TRUE
AND background_check_appropriate = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Non-escorted personnel have required access authorizations | [RULE-01] |
| Background verification appropriate to system sensitivity | [RULE-02] |
| Physical proximity boundaries documented and marked | [RULE-03] |
| Regular review of access authorizations | [RULE-04] |
| Maintenance activity documentation | [RULE-05] |