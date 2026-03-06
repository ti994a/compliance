```markdown
# POLICY: PS-9: Position Descriptions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-9 |
| NIST Control | PS-9: Position Descriptions |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | position descriptions, job descriptions, security roles, privacy roles, responsibilities, personnel security |

## 1. POLICY STATEMENT
All organizational position descriptions MUST incorporate relevant security and privacy roles and responsibilities based on the position's access to information systems and data. Position descriptions SHALL clearly define security and privacy expectations to ensure personnel understand their compliance obligations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employee positions | YES | Full-time, part-time, temporary |
| Contractor positions | YES | When accessing company systems/data |
| Board positions | YES | When involving oversight responsibilities |
| Intern positions | YES | When granted system access |
| Vendor personnel | CONDITIONAL | Only if accessing internal systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Business Partners | • Review and update position descriptions<br>• Ensure security/privacy roles are documented<br>• Coordinate with security teams for role definitions |
| Information Security Team | • Define security responsibilities by role type<br>• Review position descriptions for security completeness<br>• Provide guidance on security role requirements |
| Privacy Office | • Define privacy responsibilities by role type<br>• Review position descriptions for privacy completeness<br>• Ensure data handling responsibilities are specified |
| Hiring Managers | • Identify security/privacy requirements for positions<br>• Communicate role expectations during hiring<br>• Validate candidate understanding of responsibilities |

## 4. RULES

[RULE-01] All position descriptions MUST include specific security roles and responsibilities relevant to the position's system access and data handling requirements.
[VALIDATION] IF position_description_exists = TRUE AND security_roles_documented = FALSE THEN violation

[RULE-02] All position descriptions MUST include specific privacy roles and responsibilities for positions that involve personal data processing or privacy program oversight.
[VALIDATION] IF handles_personal_data = TRUE AND privacy_roles_documented = FALSE THEN violation

[RULE-03] Position descriptions SHALL be reviewed and updated within 30 days when security or privacy responsibilities change for the role.
[VALIDATION] IF role_responsibilities_changed = TRUE AND update_time > 30_days THEN violation

[RULE-04] Security and privacy responsibilities in position descriptions MUST align with the organization's security and privacy policies and applicable regulatory requirements.
[VALIDATION] IF responsibilities_documented = TRUE AND policy_alignment_verified = FALSE THEN violation

[RULE-05] Position descriptions for privileged access roles MUST include enhanced security responsibilities including incident reporting, access management, and security awareness requirements.
[VALIDATION] IF privileged_access_role = TRUE AND enhanced_security_responsibilities = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Position Description Development - Standard process for creating position descriptions with security/privacy components
- [PROC-02] Security Role Assessment - Process for determining appropriate security responsibilities by position type
- [PROC-03] Privacy Role Assessment - Process for determining appropriate privacy responsibilities by position type
- [PROC-04] Position Description Review - Annual review and update process for existing position descriptions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Regulatory changes, organizational restructuring, new system implementations, security incidents involving role confusion

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Technical Position]
IF position_type = "technical"
AND system_access_required = TRUE
AND security_responsibilities_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Privacy Officer Role]
IF position_involves_privacy_oversight = TRUE
AND privacy_responsibilities_documented = TRUE
AND responsibilities_align_with_privacy_program = TRUE
THEN compliance = TRUE

[SCENARIO-03: Administrative Role Changes]
IF position_responsibilities_changed = TRUE
AND change_date > 30_days_ago
AND position_description_updated = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Contractor Position]
IF worker_type = "contractor"
AND system_access_granted = TRUE
AND security_responsibilities_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Executive Position]
IF position_level = "executive"
AND security_oversight_responsibilities = TRUE
AND privacy_oversight_responsibilities = TRUE
AND both_roles_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security roles and responsibilities are incorporated into organizational position descriptions | [RULE-01], [RULE-05] |
| Privacy roles and responsibilities are incorporated into organizational position descriptions | [RULE-02] |
| Position descriptions reflect current role requirements | [RULE-03] |
| Security and privacy roles align with organizational policies | [RULE-04] |
```