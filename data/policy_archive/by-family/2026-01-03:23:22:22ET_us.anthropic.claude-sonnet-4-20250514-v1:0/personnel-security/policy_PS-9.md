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
All organizational position descriptions MUST incorporate relevant security and privacy roles and responsibilities. Position descriptions SHALL clearly define security and privacy duties to ensure personnel understand their cybersecurity and privacy obligations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employee positions | YES | Including full-time, part-time, temporary |
| Contractor positions | YES | For positions requiring system access |
| Executive positions | YES | Leadership security/privacy responsibilities |
| Intern positions | CONDITIONAL | If granted system access or handling sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Business Partners | • Review and update position descriptions with security/privacy requirements<br>• Ensure job postings include relevant security responsibilities<br>• Coordinate with security teams on role requirements |
| Information Security Team | • Define security responsibilities for technical positions<br>• Review position descriptions for security role accuracy<br>• Provide guidance on security-related duties |
| Privacy Office | • Define privacy responsibilities for data-handling positions<br>• Review position descriptions for privacy role accuracy<br>• Ensure privacy duties align with regulatory requirements |

## 4. RULES

[RULE-01] All position descriptions MUST include applicable security roles and responsibilities based on the position's access to information systems and data.
[VALIDATION] IF position_description EXISTS AND system_access = TRUE AND security_responsibilities = NULL THEN violation

[RULE-02] All position descriptions MUST include applicable privacy roles and responsibilities for positions that handle personally identifiable information (PII) or other regulated data.
[VALIDATION] IF position_description EXISTS AND handles_PII = TRUE AND privacy_responsibilities = NULL THEN violation

[RULE-03] Position descriptions SHALL be reviewed and updated within 90 days when security or privacy requirements change for the role.
[VALIDATION] IF security_requirements_changed = TRUE AND last_updated > 90_days THEN violation

[RULE-04] New position descriptions MUST be approved by both HR and the appropriate security/privacy teams before publication.
[VALIDATION] IF position_description = "new" AND (hr_approval = FALSE OR security_privacy_approval = FALSE) THEN violation

[RULE-05] Position descriptions for privileged access roles MUST include specific security responsibilities and accountability measures.
[VALIDATION] IF privileged_access = TRUE AND specific_security_responsibilities = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Position Description Review Process - Annual review of all position descriptions for security/privacy accuracy
- [PROC-02] New Role Creation Process - Security and privacy team consultation for new positions
- [PROC-03] Role Modification Process - Impact assessment when changing position responsibilities
- [PROC-04] Compliance Verification Process - Quarterly sampling to ensure descriptions meet requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Regulatory changes, organizational restructuring, new compliance requirements, security incidents involving role confusion

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Technical Position]
IF position_type = "technical"
AND system_access = TRUE
AND security_responsibilities = NULL
AND position_status = "published"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: PII Handler Missing Privacy Duties]
IF handles_PII = TRUE
AND privacy_responsibilities = NULL
AND position_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Privileged User Role]
IF privileged_access = TRUE
AND specific_security_responsibilities = TRUE
AND accountability_measures = TRUE
THEN compliance = TRUE

[SCENARIO-04: Outdated Position Description]
IF security_requirements_changed = TRUE
AND days_since_update > 90
AND position_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Contractor Position with System Access]
IF employee_type = "contractor"
AND system_access = TRUE
AND security_responsibilities = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security roles and responsibilities are incorporated into organizational position descriptions | RULE-01, RULE-05 |
| Privacy roles and responsibilities are incorporated into organizational position descriptions | RULE-02 |
| Position descriptions maintain current security and privacy requirements | RULE-03, RULE-04 |