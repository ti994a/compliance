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
All organizational positions must be assigned risk designations based on their potential impact to organizational operations and national security. Screening criteria must be established for each position type and risk designations must be regularly reviewed and updated.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational positions | YES | Including employees, contractors, and temporary staff |
| Federal positions | YES | Must comply with OPM Position Designation System |
| Volunteer positions | CONDITIONAL | Only if accessing organizational systems or sensitive data |
| Board members | YES | Executive level positions require risk assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Security Team | • Assign risk designations to all positions<br>• Establish and maintain screening criteria<br>• Conduct annual reviews of position risk designations |
| Hiring Managers | • Ensure candidates meet screening criteria before hiring<br>• Request position risk assessments for new roles<br>• Report changes in position duties that may affect risk level |
| Security Office | • Validate risk designations align with system access requirements<br>• Provide input on positions with cybersecurity responsibilities |

## 4. RULES
[RULE-01] All organizational positions MUST be assigned a risk designation (Low, Moderate, High, or Critical) within 30 days of position creation.
[VALIDATION] IF position_created_date + 30_days < current_date AND risk_designation = NULL THEN violation

[RULE-02] Screening criteria MUST be documented for each risk designation level and SHALL include background investigation requirements, security clearance needs, and specific role-based qualifications.
[VALIDATION] IF risk_designation EXISTS AND screening_criteria = NULL THEN violation

[RULE-03] Position risk designations MUST be reviewed annually and updated within 60 days when position duties change significantly.
[VALIDATION] IF last_review_date + 365_days < current_date THEN violation
[VALIDATION] IF position_duties_changed = TRUE AND update_date > change_date + 60_days THEN violation

[RULE-04] Individuals filling positions MUST meet the established screening criteria before being granted access to organizational systems or sensitive information.
[VALIDATION] IF screening_completed = FALSE AND (system_access = TRUE OR sensitive_access = TRUE) THEN critical_violation

[RULE-05] High and Critical risk positions MUST require enhanced background investigations and security clearances appropriate to the sensitivity level.
[VALIDATION] IF risk_designation IN ["High", "Critical"] AND background_investigation_level < "Enhanced" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Position Risk Assessment Process - Methodology for evaluating position duties and assigning risk levels
- [PROC-02] Screening Criteria Development - Process for establishing investigation and qualification requirements
- [PROC-03] Annual Position Review Process - Systematic review of all position risk designations
- [PROC-04] Position Change Management - Process for updating risk designations when duties change

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Organizational restructuring, new regulatory requirements, security incidents involving personnel, changes to OPM guidance

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Position Without Risk Designation]
IF position_created = TRUE
AND days_since_creation > 30
AND risk_designation = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Access Before Screening Completion]
IF position_risk_level = "High"
AND background_investigation = "In Progress"
AND system_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Overdue Position Review]
IF last_risk_review_date + 365_days < current_date
AND position_status = "Active"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Position Duties Changed Without Update]
IF position_duties_significantly_changed = TRUE
AND change_date + 60_days < current_date
AND risk_designation_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Adequate Screening for Standard Position]
IF risk_designation = "Low"
AND screening_criteria_met = TRUE
AND background_check_completed = TRUE
AND access_level = "Standard"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Risk designation assigned to all positions | [RULE-01] |
| Screening criteria established for positions | [RULE-02] |
| Position risk designations reviewed and updated | [RULE-03] |
| Enhanced screening for high-risk positions | [RULE-05] |
| Screening completion before access | [RULE-04] |