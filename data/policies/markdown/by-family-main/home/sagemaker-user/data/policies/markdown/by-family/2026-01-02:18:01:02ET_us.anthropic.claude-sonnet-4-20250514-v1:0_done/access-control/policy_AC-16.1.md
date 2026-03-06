# POLICY: AC-16.1: Dynamic Attribute Association

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-16.1 |
| NIST Control | AC-16.1: Dynamic Attribute Association |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | dynamic attributes, security labels, privacy attributes, access control, data classification |

## 1. POLICY STATEMENT
The organization SHALL dynamically associate security and privacy attributes with subjects and objects as information is created, modified, or combined. These dynamic associations MUST align with organizational security and privacy policies to ensure appropriate access controls are maintained throughout information lifecycle changes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing classified or sensitive data |
| Cloud Services | YES | Hybrid cloud infrastructure components |
| Applications | YES | Applications handling PII or regulated data |
| Data Repositories | YES | All structured and unstructured data stores |
| Network Resources | CONDITIONAL | When processing attributed information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owners | • Define attribute association policies for their data domains<br>• Approve dynamic attribute changes<br>• Monitor attribute integrity |
| System Administrators | • Implement dynamic attribute mechanisms<br>• Configure automated attribute association rules<br>• Monitor system compliance with attribute policies |
| Security Engineers | • Design attribute association architectures<br>• Validate dynamic attribute implementations<br>• Assess attribute security controls |

## 4. RULES
[RULE-01] Systems MUST automatically associate security attributes with subjects and objects when information is created, modified, or combined based on predefined organizational policies.
[VALIDATION] IF information_event IN ["create", "modify", "combine"] AND auto_attribute_assignment = FALSE THEN violation

[RULE-02] Privacy attributes MUST be dynamically updated when personally identifiable information (PII) characteristics change due to data aggregation or processing.
[VALIDATION] IF pii_characteristics_changed = TRUE AND privacy_attributes_updated = FALSE AND time_elapsed > 15_minutes THEN violation

[RULE-03] Security attributes SHALL be reassigned when information security categorization changes due to aggregation or combination with other data elements.
[VALIDATION] IF security_category_changed = TRUE AND attributes_reassigned = FALSE THEN violation

[RULE-04] Dynamic attribute changes MUST be logged with timestamp, user context, and justification for audit purposes.
[VALIDATION] IF attribute_change = TRUE AND (log_entry = FALSE OR timestamp = NULL OR user_context = NULL) THEN violation

[RULE-05] Attribute association policies MUST be reviewed and updated within 30 days when organizational security or privacy policies change.
[VALIDATION] IF policy_change_date > 30_days_ago AND attribute_policies_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Dynamic Attribute Configuration - Establish automated rules for attribute association based on information characteristics
- [PROC-02] Attribute Policy Mapping - Map organizational security/privacy policies to system attribute requirements  
- [PROC-03] Attribute Validation Testing - Verify dynamic attribute assignments function correctly across information lifecycle events
- [PROC-04] Attribute Audit Review - Regular review of attribute assignment logs and policy compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security policy changes, privacy regulation updates, system architecture changes, data breach incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Data Aggregation Classification Change]
IF data_aggregation_event = TRUE
AND original_classification = "Internal"  
AND aggregated_classification = "Confidential"
AND attributes_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: PII Processing Privacy Attributes]
IF pii_processing_initiated = TRUE
AND privacy_attributes_assigned = TRUE
AND assignment_timestamp <= processing_timestamp + 60_seconds
THEN compliance = TRUE

[SCENARIO-03: User Privilege Change Impact]
IF user_privilege_changed = TRUE
AND affected_objects_count > 0
AND object_attributes_updated = FALSE
AND time_elapsed > 5_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Cross-Domain Information Sharing]
IF information_shared_across_domains = TRUE
AND target_domain_attributes_applied = TRUE
AND source_domain_attributes_retained = TRUE
AND audit_log_created = TRUE
THEN compliance = TRUE

[SCENARIO-05: Automated Attribute Assignment Failure]
IF attribute_assignment_mechanism = "automated"
AND assignment_failure = TRUE
AND manual_override_applied = FALSE
AND failure_time > 1_hour_ago
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security attributes dynamically associated with subjects | [RULE-01] |
| Security attributes dynamically associated with objects | [RULE-01], [RULE-03] |
| Privacy attributes dynamically associated with subjects | [RULE-02] |
| Privacy attributes dynamically associated with objects | [RULE-02] |
| Security policies for dynamic association defined | [RULE-01], [RULE-05] |
| Privacy policies for dynamic association defined | [RULE-02], [RULE-05] |