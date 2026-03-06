# POLICY: PE-2: Physical Access Authorizations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-2 |
| NIST Control | PE-2: Physical Access Authorizations |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | physical access, authorization, credentials, facility access, access list, badge management |

## 1. POLICY STATEMENT
The organization SHALL develop, approve, and maintain authorized access lists for all facilities containing information systems, issue appropriate authorization credentials, and conduct regular reviews to ensure access remains current and justified. Physical access authorizations apply to both employees and visitors requiring access to controlled facility areas.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All facilities housing information systems | YES | Includes data centers, server rooms, network closets |
| Publicly accessible areas | NO | Lobbies, cafeterias, general office spaces |
| Employees requiring facility access | YES | Permanent and temporary staff |
| Visitors and contractors | YES | Temporary access with escort requirements |
| Cloud provider facilities | CONDITIONAL | Where organization has physical presence |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Maintain master facility access lists<br>• Approve access authorization requests<br>• Conduct quarterly access reviews<br>• Coordinate access terminations |
| Facility Security Officer | • Issue and manage physical credentials<br>• Monitor daily access activities<br>• Process visitor access requests<br>• Maintain access control systems |
| System Owners | • Identify personnel requiring facility access<br>• Justify business need for access requests<br>• Report access changes and terminations |

## 4. RULES
[RULE-01] The organization MUST maintain an approved list of individuals authorized to access each facility containing information systems.
[VALIDATION] IF facility_contains_systems = TRUE AND authorized_access_list_exists = FALSE THEN violation

[RULE-02] Authorization credentials MUST be issued only to individuals on the approved access list and SHALL include photo identification.
[VALIDATION] IF credential_issued = TRUE AND individual_on_approved_list = FALSE THEN critical_violation

[RULE-03] Facility access lists MUST be reviewed at least quarterly and whenever personnel changes occur.
[VALIDATION] IF last_access_review > 90_days THEN violation

[RULE-04] Individuals MUST be removed from facility access lists within 24 hours of access no longer being required.
[VALIDATION] IF access_termination_required = TRUE AND removal_time > 24_hours THEN violation

[RULE-05] Visitor access MUST be documented, sponsored by an authorized employee, and limited to specific areas and timeframes.
[VALIDATION] IF visitor_access = TRUE AND (sponsor_authorized = FALSE OR documentation_complete = FALSE) THEN violation

[RULE-06] Authorization credentials MUST be returned or deactivated immediately upon access termination.
[VALIDATION] IF access_terminated = TRUE AND credential_active = TRUE AND time_elapsed > 4_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Access Authorization - Process for requesting, approving, and documenting facility access
- [PROC-02] Credential Management - Procedures for issuing, tracking, and recovering physical access credentials  
- [PROC-03] Access List Review - Quarterly review process for validating continued access requirements
- [PROC-04] Visitor Management - Process for authorizing, escorting, and monitoring temporary facility access
- [PROC-05] Access Termination - Immediate revocation procedures for departing personnel

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after security incidents
- Triggering events: Security breaches, facility changes, regulatory updates, personnel turnover in security roles

## 7. SCENARIO PATTERNS
[SCENARIO-01: Terminated Employee Access]
IF employee_status = "terminated"
AND termination_date < current_date
AND facility_access_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Contractor Project Completion]
IF user_type = "contractor"
AND project_end_date < current_date - 7_days
AND facility_access_active = TRUE
AND extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Quarterly Access Review Overdue]
IF facility_type = "controlled_area"
AND last_access_review > current_date - 90_days
AND review_extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Visitor Without Proper Authorization]
IF access_type = "visitor"
AND sponsor_on_approved_list = FALSE
AND unescorted_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Photo Identification]
IF credential_issued = TRUE
AND photo_id_attached = FALSE
AND access_to_controlled_area = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authorized access list developed, approved, and maintained | [RULE-01] |
| Authorization credentials issued for facility access | [RULE-02] |
| Access list reviewed at defined frequency | [RULE-03] |
| Individuals removed when access no longer required | [RULE-04], [RULE-06] |
| Visitor access properly controlled and documented | [RULE-05] |
| Credential management and recovery processes | [RULE-06] |