# POLICY: PE-2.1: Access by Position or Role

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-2.1 |
| NIST Control | PE-2.1: Access by Position or Role |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | physical access, role-based access, facility security, position authorization, data center access |

## 1. POLICY STATEMENT
Physical access to facilities containing information systems MUST be authorized based on documented position or role requirements. All facility access authorizations SHALL be tied to specific job functions and business justifications rather than individual requests.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary and backup facilities |
| Server Rooms | YES | All locations with production systems |
| Network Equipment Rooms | YES | Including telecommunications closets |
| Office Areas | CONDITIONAL | Only areas with sensitive system components |
| Third-party Facilities | YES | Cloud provider and colocation facilities |
| Remote Locations | YES | Branch offices with system infrastructure |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facility Security Manager | • Define position-based access requirements<br>• Maintain role-to-access mapping matrix<br>• Approve access authorization changes |
| IT Security Team | • Validate technical justification for access<br>• Review access logs and compliance<br>• Coordinate with HR on role changes |
| Human Resources | • Notify security of position changes<br>• Validate employment status and clearances<br>• Process termination notifications |

## 4. RULES
[RULE-01] Physical access authorizations MUST be based on documented position descriptions or role definitions that specify required facility access levels.
[VALIDATION] IF access_granted = TRUE AND position_documentation = FALSE THEN violation

[RULE-02] Emergency personnel (medical staff, fire safety) SHALL have pre-authorized access documented in emergency response procedures.
[VALIDATION] IF user_type = "emergency_personnel" AND pre_authorization_documented = FALSE THEN violation

[RULE-03] Maintenance personnel access MUST be limited to scheduled maintenance windows and require escort for unscheduled access.
[VALIDATION] IF user_type = "maintenance" AND scheduled = FALSE AND escort_present = FALSE THEN violation

[RULE-04] Duty officers and operations staff MUST have access authorizations that align with shift schedules and operational responsibilities.
[VALIDATION] IF user_type = "duty_officer" AND current_time NOT IN authorized_schedule THEN violation

[RULE-05] Position-based access authorizations MUST be reviewed within 30 days of any role change, promotion, or transfer.
[VALIDATION] IF role_change_date < (current_date - 30_days) AND access_review_completed = FALSE THEN violation

[RULE-06] Temporary or contractor positions MUST have access authorizations with defined expiration dates matching contract or assignment duration.
[VALIDATION] IF user_type = "contractor" AND (access_expiration_date = NULL OR access_expiration_date > contract_end_date) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Position-Based Access Matrix - Maintain mapping of positions to required facility access levels
- [PROC-02] Emergency Personnel Authorization - Pre-authorize and document emergency responder access rights
- [PROC-03] Role Change Access Review - Process for reviewing access when positions change
- [PROC-04] Maintenance Personnel Escort - Procedures for escorted access during unscheduled maintenance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Organizational restructuring, facility changes, security incidents, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee Access]
IF employee_status = "new_hire"
AND position_defined = TRUE
AND access_matches_position = TRUE
THEN compliance = TRUE

[SCENARIO-02: Contractor Overstay]
IF user_type = "contractor"
AND contract_end_date < current_date
AND facility_access_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Emergency Medical Access]
IF user_type = "emergency_medical"
AND emergency_situation = TRUE
AND pre_authorization_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Maintenance Without Escort]
IF user_type = "maintenance"
AND maintenance_scheduled = FALSE
AND escort_present = FALSE
AND facility_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Role Change Without Review]
IF employee_role_changed = TRUE
AND role_change_date < (current_date - 30_days)
AND access_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical access authorized based on position or role | [RULE-01] |
| Emergency personnel access properly documented | [RULE-02] |
| Maintenance personnel access controls | [RULE-03] |
| Operational staff access alignment | [RULE-04] |
| Access review upon role changes | [RULE-05] |
| Temporary access expiration controls | [RULE-06] |