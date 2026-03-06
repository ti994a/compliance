# POLICY: AC-16.10: Attribute Configuration by Authorized Individuals

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-16.10 |
| NIST Control | AC-16.10: Attribute Configuration by Authorized Individuals |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | attribute configuration, access control, security attributes, privacy attributes, authorized individuals |

## 1. POLICY STATEMENT
Only authorized individuals SHALL have the capability to define or change the type and value of security and privacy attributes available for association with subjects and objects. The organization MUST implement controls to restrict attribute configuration capabilities to prevent unauthorized modification of access control mechanisms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing organizational data |
| Cloud Services | YES | Including hybrid and multi-cloud environments |
| Applications | YES | Custom and COTS applications with attribute-based access |
| Databases | YES | Systems storing security/privacy attributes |
| Identity Management Systems | YES | Primary systems for attribute management |
| Contractors | YES | When managing organizational systems |
| End Users | NO | Unless specifically authorized for attribute management |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement attribute configuration restrictions<br>• Maintain authorized user lists<br>• Monitor attribute modification activities |
| Security Officers | • Define security attribute types and allowable values<br>• Approve attribute configuration permissions<br>• Review attribute modification logs |
| Privacy Officers | • Define privacy attribute types and allowable values<br>• Ensure privacy attribute compliance<br>• Validate privacy impact assessments |
| Identity Administrators | • Manage authorized individual access<br>• Configure role-based attribute permissions<br>• Maintain attribute schema integrity |

## 4. RULES
[RULE-01] Systems MUST restrict the capability to define or change security attribute types and values to explicitly authorized individuals only.
[VALIDATION] IF user_attempts_attribute_modification = TRUE AND user_authorized_for_security_attributes = FALSE THEN violation

[RULE-02] Systems MUST restrict the capability to define or change privacy attribute types and values to explicitly authorized individuals only.
[VALIDATION] IF user_attempts_privacy_attribute_modification = TRUE AND user_authorized_for_privacy_attributes = FALSE THEN violation

[RULE-03] All security and privacy attribute modifications MUST be logged with user identification, timestamp, attribute type, old value, and new value.
[VALIDATION] IF attribute_modified = TRUE AND (user_id = NULL OR timestamp = NULL OR old_value = NULL OR new_value = NULL) THEN violation

[RULE-04] Authorized individuals MUST be formally designated through documented approval process by system owner and security officer.
[VALIDATION] IF user_has_attribute_permissions = TRUE AND formal_authorization_documented = FALSE THEN violation

[RULE-05] Attribute configuration permissions MUST be reviewed and revalidated at least annually or upon role change.
[VALIDATION] IF last_permission_review > 365_days OR user_role_changed = TRUE AND permission_revalidation = FALSE THEN violation

[RULE-06] Emergency attribute modifications MUST be pre-approved through documented emergency procedures and reviewed within 24 hours.
[VALIDATION] IF emergency_attribute_change = TRUE AND (emergency_approval = FALSE OR post_review_time > 24_hours) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Attribute Authorization Process - Formal designation and approval of individuals authorized for attribute configuration
- [PROC-02] Attribute Change Management - Controlled process for modifying attribute types and values
- [PROC-03] Attribute Audit Review - Regular review of attribute modification logs and access patterns
- [PROC-04] Emergency Attribute Procedures - Process for urgent attribute changes with proper oversight

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving attribute manipulation, system architecture changes, regulatory requirement updates, unauthorized access events

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Security Attribute Modification]
IF user_type = "standard_user"
AND attempts_security_attribute_change = TRUE
AND authorized_for_security_attributes = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Privacy Attribute Access]
IF user_type = "contractor"
AND attempts_privacy_attribute_modification = TRUE
AND formal_authorization_documented = TRUE
AND authorization_current = TRUE
THEN compliance = TRUE

[SCENARIO-03: Unlogged Attribute Change]
IF attribute_value_changed = TRUE
AND modification_logged = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Expired Authorization Usage]
IF user_has_attribute_permissions = TRUE
AND last_authorization_review > 365_days
AND user_performs_attribute_change = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Change Without Review]
IF emergency_attribute_change = TRUE
AND emergency_approval_documented = TRUE
AND hours_since_change > 24
AND post_change_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authorized individuals provided capability to define/change security attributes | [RULE-01], [RULE-04] |
| Authorized individuals provided capability to define/change privacy attributes | [RULE-02], [RULE-04] |
| Restriction of attribute configuration to authorized personnel only | [RULE-01], [RULE-02] |
| Audit trail of attribute modifications | [RULE-03] |
| Formal authorization process | [RULE-04] |
| Periodic review of permissions | [RULE-05] |