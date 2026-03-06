# POLICY: PS-2: Position Risk Designation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-2 |
| NIST Control | PS-2: Position Risk Designation |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | position risk, screening criteria, personnel security, background investigation, position designation |

## 1. POLICY STATEMENT
All organizational positions must be assigned risk designations based on their duties and potential impact to organizational operations and national security. Screening criteria must be established for each position type and risk designations must be regularly reviewed and updated.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational positions | YES | Including employees, contractors, and temporary staff |
| Federal positions | YES | Must comply with OPM Position Designation System |
| Volunteer positions | CONDITIONAL | Only if accessing organizational systems or facilities |
| Board members | YES | Executive-level positions require risk designation |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Human Resources Officer | • Oversee position risk designation program<br>• Ensure compliance with OPM guidelines<br>• Approve risk designation assignments |
| Security Office | • Develop screening criteria based on risk levels<br>• Coordinate background investigations<br>• Review position access requirements |
| Hiring Managers | • Identify position duties and responsibilities<br>• Recommend appropriate risk designations<br>• Ensure screening criteria are met before hiring |

## 4. RULES
[RULE-01] All organizational positions MUST be assigned a risk designation (Low, Moderate, High, or Critical) based on potential impact to organizational operations, assets, and individuals.
[VALIDATION] IF position_exists = TRUE AND risk_designation = NULL THEN violation

[RULE-02] Position risk designations MUST be based on Office of Personnel Management Position Designation System criteria and organizational security requirements.
[VALIDATION] IF risk_designation NOT IN ["Low", "Moderate", "High", "Critical"] THEN violation

[RULE-03] Screening criteria MUST be established for each risk designation level and documented in position descriptions.
[VALIDATION] IF risk_designation_exists = TRUE AND screening_criteria = NULL THEN violation

[RULE-04] Position risk designations MUST be reviewed and updated at least annually or when position duties significantly change.
[VALIDATION] IF last_review_date > 365_days OR duties_changed = TRUE AND review_completed = FALSE THEN violation

[RULE-05] Individuals MUST complete required background investigations and meet screening criteria before being granted access commensurate with their position risk level.
[VALIDATION] IF position_filled = TRUE AND (background_check_complete = FALSE OR screening_criteria_met = FALSE) THEN violation

[RULE-06] Critical and High risk positions MUST require enhanced screening including credit checks, reference verification, and continuous monitoring where applicable.
[VALIDATION] IF risk_designation IN ["Critical", "High"] AND enhanced_screening_complete = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Position Risk Assessment - Systematic evaluation of position duties to determine risk designation
- [PROC-02] Screening Criteria Development - Establishment of investigation and qualification requirements by risk level
- [PROC-03] Annual Position Review - Regular reassessment of position risk designations and screening criteria
- [PROC-04] Position Change Management - Process for updating risk designations when duties change significantly

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Organizational restructuring, new regulatory requirements, security incidents involving personnel, changes in OPM guidance

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Position Without Risk Designation]
IF position_created = TRUE
AND risk_designation = NULL
AND position_active_days > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Overdue Position Review]
IF position_exists = TRUE
AND last_review_date > 365_days
AND duties_unchanged = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-03: High Risk Position Inadequate Screening]
IF risk_designation = "High"
AND background_investigation_level < "Secret"
AND system_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Position Duties Changed Without Review]
IF position_duties_modified = TRUE
AND modification_date > 90_days
AND risk_designation_reviewed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Contractor Position Missing Screening]
IF employee_type = "contractor"
AND system_access_required = TRUE
AND screening_criteria_met = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Risk designation assigned to all positions | [RULE-01] |
| Screening criteria established for positions | [RULE-03] |
| Position risk designations reviewed and updated | [RULE-04] |
| Background investigations completed | [RULE-05] |
| Enhanced screening for high-risk positions | [RULE-06] |