# POLICY: PE-2: Physical Access Authorizations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-2 |
| NIST Control | PE-2: Physical Access Authorizations |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | physical access, facility security, authorization credentials, access lists, badge management |

## 1. POLICY STATEMENT
The organization SHALL develop, approve, and maintain authorized facility access lists for all system facilities. Authorization credentials MUST be issued for facility access and access lists SHALL be regularly reviewed with individuals removed when access is no longer required.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All facilities housing information systems | YES | Includes data centers, server rooms, network closets |
| Publicly accessible areas | NO | Lobbies, cafeterias, general office spaces |
| Employees and contractors | YES | Requires formal authorization process |
| Visitors | YES | Temporary access with escort requirements |
| Vendor/maintenance personnel | YES | Limited access with supervision |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facility Security Manager | • Maintain authorized access lists<br>• Issue and revoke authorization credentials<br>• Conduct quarterly access reviews |
| System Owners | • Identify personnel requiring facility access<br>• Approve access requests for their systems<br>• Notify of personnel changes |
| Physical Security Team | • Implement access controls<br>• Monitor facility access<br>• Maintain visitor logs |

## 4. RULES
[RULE-01] All facilities housing information systems MUST maintain an approved list of individuals authorized for physical access.
[VALIDATION] IF facility_houses_systems = TRUE AND authorized_access_list_exists = FALSE THEN violation

[RULE-02] Authorization credentials SHALL be issued only to individuals on the approved access list and MUST include photo identification.
[VALIDATION] IF individual_has_credentials = TRUE AND individual_on_approved_list = FALSE THEN violation

[RULE-03] Facility access lists MUST be reviewed at least quarterly and updated within 5 business days of personnel changes.
[VALIDATION] IF last_access_review > 90_days THEN violation
[VALIDATION] IF personnel_change_date + 5_business_days < current_date AND access_list_updated = FALSE THEN violation

[RULE-04] Individuals MUST be removed from facility access lists within 24 hours of termination or role change eliminating access need.
[VALIDATION] IF employee_terminated = TRUE AND removal_time > 24_hours THEN critical_violation

[RULE-05] Visitor access MUST be documented, time-limited, and require continuous escort by authorized personnel.
[VALIDATION] IF visitor_access = TRUE AND (documentation = FALSE OR escort = FALSE) THEN violation

[RULE-06] Authorization credentials MUST be deactivated immediately upon loss, theft, or suspected compromise.
[VALIDATION] IF credential_compromised = TRUE AND deactivation_time > 1_hour THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Access Request Process - Formal approval workflow for facility access
- [PROC-02] Credential Issuance and Management - Badge creation, distribution, and lifecycle management
- [PROC-03] Quarterly Access Review Process - Systematic review of all authorized personnel
- [PROC-04] Emergency Access Revocation - Immediate credential deactivation procedures
- [PROC-05] Visitor Management Process - Registration, escort, and monitoring procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents, organizational changes, facility modifications, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Terminated Employee Access]
IF employee_status = "terminated"
AND termination_date < current_date - 24_hours
AND facility_access_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Contractor Project Completion]
IF user_type = "contractor"
AND project_end_date < current_date
AND facility_access_active = TRUE
AND access_extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Overdue Access Review]
IF last_quarterly_review_date < current_date - 90_days
AND facility_houses_critical_systems = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unescorted Visitor]
IF visitor_in_facility = TRUE
AND escort_present = FALSE
AND visitor_clearance_level < "authorized_unescorted"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Lost Badge Incident]
IF credential_reported_lost = TRUE
AND time_since_report > 1_hour
AND credential_deactivated = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authorized access list developed | RULE-01 |
| Authorized access list approved | RULE-01 |
| Authorized access list maintained | RULE-03 |
| Authorization credentials issued | RULE-02 |
| Access list reviewed quarterly | RULE-03 |
| Individuals removed when access no longer required | RULE-04 |