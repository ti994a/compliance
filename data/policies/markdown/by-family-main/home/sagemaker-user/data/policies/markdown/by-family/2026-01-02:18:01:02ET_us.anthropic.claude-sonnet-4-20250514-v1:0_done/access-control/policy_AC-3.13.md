# POLICY: AC-3.13: Attribute-based Access Control

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-3.13 |
| NIST Control | AC-3.13: Attribute-based Access Control |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | attribute-based, access control, ABAC, subjects, objects, authorization, privileges |

## 1. POLICY STATEMENT
The organization SHALL enforce attribute-based access control (ABAC) policies over all defined subjects and objects within information systems. Access permissions SHALL be dynamically determined based on organizational, action, environmental, and resource attributes according to predefined authorization rules.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, hybrid, and on-premises |
| External contractors | YES | When accessing organizational systems |
| Service accounts | YES | Must have defined attributes |
| Emergency access accounts | CONDITIONAL | Subject to emergency procedures |
| Public-facing resources | CONDITIONAL | Based on data classification |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owners | • Define resource attributes and classification<br>• Approve access rules for their data<br>• Review attribute assignments quarterly |
| System Administrators | • Implement ABAC mechanisms<br>• Configure attribute mappings<br>• Monitor access control enforcement |
| Identity Management Team | • Maintain subject attributes<br>• Provision users with appropriate attributes<br>• Validate attribute accuracy |

## 4. RULES
[RULE-01] All subjects (users, processes, devices) accessing organizational systems MUST have defined organizational attributes including role, clearance level, department, and employment status.
[VALIDATION] IF subject_access_attempt = TRUE AND (role = NULL OR clearance_level = NULL OR department = NULL) THEN access_denied

[RULE-02] All protected objects (files, databases, applications) MUST be assigned resource attributes including data classification, owner, and access requirements.
[VALIDATION] IF object_classification = NULL OR object_owner = NULL THEN access_control_incomplete

[RULE-03] Access decisions MUST be evaluated in real-time based on current attribute values and SHALL NOT rely on cached permissions older than 15 minutes.
[VALIDATION] IF permission_cache_age > 15_minutes THEN force_attribute_reevaluation

[RULE-04] Environmental attributes including time of access, location, and network context MUST be considered for access to systems containing sensitive data (Confidential or above).
[VALIDATION] IF data_classification >= "Confidential" AND (time_attribute = NULL OR location_attribute = NULL) THEN access_denied

[RULE-05] Attribute-based access rules MUST be documented, approved by data owners, and reviewed annually or when organizational structure changes occur.
[VALIDATION] IF rule_last_review > 365_days OR org_structure_changed = TRUE THEN rule_review_required

## 5. REQUIRED PROCEDURES
- [PROC-01] Attribute Definition and Management - Process for defining, assigning, and maintaining subject and object attributes
- [PROC-02] ABAC Rule Creation and Approval - Workflow for creating and approving attribute-based access rules
- [PROC-03] Access Decision Logging and Monitoring - Procedures for logging and reviewing ABAC access decisions
- [PROC-04] Attribute Validation and Cleanup - Regular validation of attribute accuracy and removal of obsolete attributes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Organizational restructuring, system changes, security incidents, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard User Access]
IF subject_role = "employee"
AND object_classification = "internal"
AND location_attribute = "corporate_network"
AND time_attribute = "business_hours"
THEN compliance = TRUE

[SCENARIO-02: Contractor Restricted Access]
IF subject_role = "contractor"
AND object_classification = "confidential"
AND project_assignment != object_owner
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: After-Hours Sensitive Access]
IF subject_role = "standard_user"
AND object_classification = "confidential"
AND time_attribute = "after_hours"
AND manager_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Terminated Employee Access]
IF subject_employment_status = "terminated"
AND access_granted = TRUE
AND termination_date < current_date
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Cross-Department Data Access]
IF subject_department != object_owner_department
AND data_sharing_agreement = FALSE
AND business_justification = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Attribute-based access control policy is enforced over defined subjects | [RULE-01] |
| Attribute-based access control policy is enforced over defined objects | [RULE-02] |
| Access is controlled based on attributes to assume access permissions are defined | [RULE-03], [RULE-04] |