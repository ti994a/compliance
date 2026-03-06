# POLICY: PS-9: Position Descriptions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-9 |
| NIST Control | PS-9: Position Descriptions |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | position descriptions, security roles, privacy roles, job descriptions, responsibilities, personnel security |

## 1. POLICY STATEMENT
All organizational position descriptions MUST incorporate relevant security and privacy roles and responsibilities. Position descriptions SHALL clearly define security and privacy expectations for each role to ensure accountability and appropriate training assignment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employee positions | YES | Including full-time, part-time, temporary |
| Contractor positions | YES | When accessing organizational systems |
| Vendor personnel | CONDITIONAL | When requiring system access |
| Volunteer positions | CONDITIONAL | When handling sensitive data |
| Executive positions | YES | Enhanced security responsibilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Human Resources Officer | • Oversee position description policy implementation<br>• Ensure compliance across all organizational units<br>• Coordinate with security and privacy officers |
| Human Resources Managers | • Review and update position descriptions<br>• Validate security/privacy role incorporation<br>• Maintain position description documentation |
| Information Security Officer | • Define security roles and responsibilities<br>• Review security-related position requirements<br>• Approve security role specifications |
| Privacy Officer | • Define privacy roles and responsibilities<br>• Review privacy-related position requirements<br>• Approve privacy role specifications |

## 4. RULES

[RULE-01] All position descriptions MUST include specific security roles and responsibilities relevant to the position's access level and data handling requirements.
[VALIDATION] IF position_description EXISTS AND security_roles = NULL THEN violation

[RULE-02] All position descriptions MUST include specific privacy roles and responsibilities when the position involves personally identifiable information (PII) or privacy-sensitive activities.
[VALIDATION] IF position_handles_PII = TRUE AND privacy_roles = NULL THEN violation

[RULE-03] Position descriptions SHALL be reviewed and updated within 30 days of any significant change in security or privacy requirements affecting the role.
[VALIDATION] IF security_requirements_change_date > position_update_date + 30_days THEN violation

[RULE-04] Security and privacy responsibilities in position descriptions MUST align with the organization's security and privacy frameworks and policies.
[VALIDATION] IF security_responsibilities NOT IN approved_security_framework THEN violation

[RULE-05] Position descriptions for roles with privileged access MUST include enhanced security responsibilities and accountability measures.
[VALIDATION] IF privileged_access = TRUE AND enhanced_security_responsibilities = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Position Description Development - Standard process for creating new position descriptions with security/privacy roles
- [PROC-02] Position Description Review - Annual review and update process for existing positions
- [PROC-03] Security Role Assignment - Process for determining appropriate security responsibilities by role
- [PROC-04] Privacy Role Assignment - Process for determining appropriate privacy responsibilities by role
- [PROC-05] Position Description Approval - Workflow for security and privacy officer review and approval

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Organizational restructuring, new regulatory requirements, security incidents, privacy breaches, technology changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: New IT Administrator Position]
IF position_type = "IT Administrator"
AND system_access_level = "privileged"
AND security_responsibilities = NULL
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: HR Specialist with PII Access]
IF position_handles_PII = TRUE
AND data_sensitivity = "high"
AND privacy_responsibilities = NULL
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Updated Security Framework]
IF security_framework_updated = TRUE
AND position_descriptions_updated = FALSE
AND days_since_update > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Contractor Position with System Access]
IF employee_type = "contractor"
AND system_access_required = TRUE
AND security_roles_defined = TRUE
AND privacy_roles_defined = TRUE
THEN compliance = TRUE

[SCENARIO-05: Executive Position Missing Enhanced Responsibilities]
IF position_level = "executive"
AND privileged_access = TRUE
AND enhanced_security_responsibilities = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security roles and responsibilities incorporated into position descriptions | [RULE-01], [RULE-04], [RULE-05] |
| Privacy roles and responsibilities incorporated into position descriptions | [RULE-02], [RULE-04] |
| Position descriptions maintain current security requirements | [RULE-03] |
| Privileged positions have appropriate security responsibilities | [RULE-05] |