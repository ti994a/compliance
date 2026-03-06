# POLICY: PE-2.1: Access by Position or Role

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-2.1 |
| NIST Control | PE-2.1: Access by Position or Role |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | physical access, facility access, role-based access, position authorization, data center security |

## 1. POLICY STATEMENT
Physical access to facilities housing information systems SHALL be authorized based on documented position requirements or assigned organizational roles. All facility access decisions MUST align with job responsibilities and business need-to-know principles for physical security zones.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All company-operated facilities |
| Co-location Facilities | YES | Where company systems reside |
| Cloud Provider Facilities | CONDITIONAL | When direct access agreements exist |
| Office Buildings with IT Infrastructure | YES | Server rooms, network closets |
| Remote Offices | CONDITIONAL | If housing critical systems |
| Vendor Facilities | CONDITIONAL | If housing company-owned systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Define position-based access requirements<br>• Approve facility access authorizations<br>• Maintain access control matrices<br>• Conduct quarterly access reviews |
| Facility Access Coordinators | • Process access requests against role requirements<br>• Validate position documentation<br>• Update access control systems<br>• Document access decisions |
| HR Business Partners | • Provide position descriptions and requirements<br>• Notify of role changes affecting facility access<br>• Validate employment status for access requests |

## 4. RULES
[RULE-01] Physical access authorizations MUST be based on documented position descriptions that specify facility access requirements and business justification.
[VALIDATION] IF access_request = TRUE AND position_documentation = FALSE THEN violation

[RULE-02] Role-based access matrices MUST define specific facility zones accessible by each organizational position or role classification.
[VALIDATION] IF facility_zone_access = granted AND role_matrix_authorization = FALSE THEN violation

[RULE-03] Emergency personnel access (medical, fire safety, security) MUST be pre-authorized based on emergency response roles with appropriate escort requirements.
[VALIDATION] IF personnel_type = "emergency" AND pre_authorization = FALSE AND escort_present = FALSE THEN violation

[RULE-04] Maintenance personnel facility access MUST be authorized based on specific maintenance roles and SHALL require escort for non-employee maintenance staff.
[VALIDATION] IF personnel_type = "maintenance" AND employee_status = FALSE AND escort_assigned = FALSE THEN violation

[RULE-05] Temporary access for non-standard roles MUST be approved by Physical Security Manager and SHALL NOT exceed 30 days without re-authorization.
[VALIDATION] IF access_type = "temporary" AND duration > 30_days AND reauthorization = FALSE THEN violation

[RULE-06] Position-based access authorizations MUST be reviewed quarterly and updated within 5 business days of role changes.
[VALIDATION] IF last_review_date > 90_days OR role_change_date > 5_business_days AND access_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Position-Based Access Authorization - Defines process for mapping positions to facility access requirements
- [PROC-02] Role Change Access Update - Procedures for updating access when employee roles change
- [PROC-03] Emergency Personnel Access Management - Pre-authorization and escort procedures for emergency responders
- [PROC-04] Quarterly Access Review - Systematic review of position-based access authorizations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Organizational restructuring, new facility acquisition, security incidents involving unauthorized access, changes to regulatory requirements

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee Data Center Access]
IF employee_status = "new_hire"
AND position = "database_administrator"
AND facility_type = "data_center"
AND position_access_matrix = "data_center_authorized"
THEN compliance = TRUE

[SCENARIO-02: Contractor Maintenance Access]
IF personnel_type = "contractor"
AND role = "HVAC_maintenance"
AND facility_zone = "server_room"
AND escort_assigned = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Role Change Access Update]
IF employee_role_change = TRUE
AND role_change_date = "15_days_ago"
AND facility_access_updated = FALSE
AND new_role_requires_different_access = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Emergency Medical Access]
IF personnel_type = "emergency_medical"
AND emergency_situation = TRUE
AND pre_authorization = TRUE
AND facility_zone = "data_center"
THEN compliance = TRUE

[SCENARIO-05: Temporary Project Access]
IF access_type = "temporary"
AND project_duration = "45_days"
AND initial_authorization_date = "50_days_ago"
AND reauthorization_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical access authorized based on position or role | [RULE-01], [RULE-02] |
| Role-based facility access for permanent personnel | [RULE-02], [RULE-06] |
| Access authorization for maintenance personnel | [RULE-04] |
| Access authorization for emergency personnel | [RULE-03] |
| Position-based access control implementation | [RULE-01], [RULE-05] |