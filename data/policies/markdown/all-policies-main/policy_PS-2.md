# POLICY: PS-2: Position Risk Designation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-2 |
| NIST Control | PS-2: Position Risk Designation |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | position risk, screening criteria, personnel security, risk designation, background investigation |

## 1. POLICY STATEMENT
All organizational positions must be assigned risk designations based on their duties and potential impact to organizational operations. Screening criteria must be established for each position type and risk designations must be regularly reviewed and updated.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational positions | YES | Including employees, contractors, and temporary staff |
| Volunteer positions | YES | If accessing organizational systems or facilities |
| Board members | YES | Based on access requirements |
| Intern positions | YES | Regardless of duration |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Security Team | • Assign initial risk designations<br>• Establish screening criteria<br>• Conduct periodic reviews<br>• Maintain position risk registry |
| Hiring Managers | • Identify position duties and responsibilities<br>• Request appropriate risk designations<br>• Ensure screening requirements are met |
| Security Office | • Validate risk designations align with access requirements<br>• Review high-risk position designations<br>• Approve exceptions to standard criteria |

## 4. RULES

[RULE-01] All organizational positions MUST be assigned a risk designation (Low, Moderate, High, or Critical) based on potential impact to organizational operations, assets, or individuals.
[VALIDATION] IF position_exists = TRUE AND risk_designation = NULL THEN violation

[RULE-02] Position risk designations MUST be based on duties involving access to sensitive information, critical systems, financial authority, or public trust responsibilities.
[VALIDATION] IF high_risk_duties = TRUE AND risk_designation != ("High" OR "Critical") THEN violation

[RULE-03] Screening criteria MUST be established for each risk designation level and documented in the position risk registry.
[VALIDATION] IF risk_designation_exists = TRUE AND screening_criteria = NULL THEN violation

[RULE-04] Position risk designations MUST be reviewed and updated at least annually or when position duties significantly change.
[VALIDATION] IF last_review_date > 365_days AND position_active = TRUE THEN violation

[RULE-05] High and Critical risk positions MUST require background investigations appropriate to the sensitivity level before personnel placement.
[VALIDATION] IF risk_designation = ("High" OR "Critical") AND background_investigation_complete = FALSE AND placement_date != NULL THEN critical_violation

[RULE-06] Position risk designations MUST align with required system access levels and clearance requirements.
[VALIDATION] IF system_access_level > position_risk_level THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Position Risk Assessment - Systematic evaluation of position duties and impact potential
- [PROC-02] Screening Criteria Development - Establishment of investigation and qualification requirements
- [PROC-03] Risk Designation Review - Annual review and update process for all positions
- [PROC-04] Exception Management - Process for handling special circumstances or temporary assignments

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Organizational restructure, new regulatory requirements, security incidents involving personnel

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Position Creation]
IF new_position_created = TRUE
AND risk_designation = NULL
AND position_active_days > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: System Administrator Role]
IF position_duties CONTAINS "system_administration"
AND system_criticality = "High"
AND risk_designation = "Low"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Contractor High-Risk Access]
IF employee_type = "contractor"
AND risk_designation = "Critical"
AND background_investigation = "None"
AND system_access = "Granted"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Annual Review Overdue]
IF position_active = TRUE
AND last_review_date > 400_days
AND risk_designation = ("High" OR "Critical")
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Financial Authority Mismatch]
IF financial_authority > 100000
AND risk_designation = "Low"
AND fiduciary_duties = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Risk designation assigned to all positions | [RULE-01] |
| Screening criteria established for positions | [RULE-03] |
| Position risk designations reviewed and updated | [RULE-04] |
| Risk designation reflects position duties | [RULE-02] |
| Background investigations for high-risk positions | [RULE-05] |
| Access alignment with risk designation | [RULE-06] |