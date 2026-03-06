# POLICY: AC-16.6: Maintenance of Attribute Association

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-16.6 |
| NIST Control | AC-16.6: Maintenance of Attribute Association |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | attribute association, security attributes, privacy attributes, subjects, objects, personnel responsibilities |

## 1. POLICY STATEMENT
Personnel must associate and maintain the association of organization-defined security and privacy attributes with designated subjects and objects according to established security and privacy policies. This control ensures that attribute associations are actively managed by users rather than relying solely on automated systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Personnel | YES | Users handling classified or sensitive data |
| Systems Processing PII | YES | Enhanced privacy attribute requirements |
| Cloud Resources | YES | Hybrid cloud infrastructure included |
| Third-party Systems | CONDITIONAL | Only when processing company data |
| Guest Users | YES | Limited attribute association required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owners | • Define required security and privacy attributes for their data<br>• Establish attribute association policies<br>• Monitor compliance with attribute requirements |
| System Users | • Associate appropriate attributes with subjects and objects<br>• Maintain attribute associations during data lifecycle<br>• Report attribute association failures |
| Security Team | • Define organization-wide attribute taxonomy<br>• Monitor attribute association compliance<br>• Provide training on attribute management |

## 4. RULES
[RULE-01] Personnel MUST associate organization-defined security attributes with all subjects and objects they create or modify within 24 hours of creation or modification.
[VALIDATION] IF (subject_created OR object_created OR subject_modified OR object_modified) AND security_attributes_assigned = FALSE AND time_elapsed > 24_hours THEN violation

[RULE-02] Personnel MUST associate organization-defined privacy attributes with all subjects and objects containing PII within 2 hours of creation or modification.
[VALIDATION] IF (contains_pii = TRUE) AND privacy_attributes_assigned = FALSE AND time_elapsed > 2_hours THEN critical_violation

[RULE-03] Personnel SHALL maintain attribute associations throughout the entire lifecycle of subjects and objects, updating attributes within 4 hours when circumstances change.
[VALIDATION] IF attribute_change_required = TRUE AND attribute_update_time > 4_hours THEN violation

[RULE-04] Personnel MUST NOT remove or modify security or privacy attributes without proper authorization from the data owner.
[VALIDATION] IF (attribute_removed OR attribute_modified) AND authorization_documented = FALSE THEN critical_violation

[RULE-05] Personnel SHALL verify attribute associations monthly for all subjects and objects under their responsibility.
[VALIDATION] IF last_verification_date > 30_days AND verification_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Attribute Assignment Procedure - Standardized process for assigning security and privacy attributes
- [PROC-02] Attribute Maintenance Procedure - Process for ongoing maintenance and updates of attribute associations
- [PROC-03] Attribute Verification Procedure - Monthly verification process for attribute accuracy
- [PROC-04] Attribute Exception Handling - Process for handling cases where standard attributes don't apply

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Data breach, regulatory changes, system architecture changes, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Sensitive Document Creation]
IF document_created = TRUE
AND sensitivity_level = "confidential"
AND security_attributes_assigned = FALSE
AND time_elapsed > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: PII Data Without Privacy Attributes]
IF data_contains_pii = TRUE
AND privacy_attributes_assigned = FALSE
AND time_elapsed > 2_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unauthorized Attribute Modification]
IF attribute_modified = TRUE
AND user_role != "data_owner"
AND authorization_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Monthly Verification]
IF last_attribute_verification > 35_days
AND user_has_assigned_objects = TRUE
AND exception_granted = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Proper Attribute Lifecycle Management]
IF object_status_changed = TRUE
AND attributes_updated_within_timeframe = TRUE
AND authorization_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel associate security attributes with subjects | [RULE-01] |
| Personnel associate security attributes with objects | [RULE-01] |
| Personnel associate privacy attributes with subjects | [RULE-02] |
| Personnel associate privacy attributes with objects | [RULE-02] |
| Maintenance of attribute associations | [RULE-03], [RULE-05] |
| Compliance with security policies | [RULE-01], [RULE-04] |
| Compliance with privacy policies | [RULE-02], [RULE-04] |