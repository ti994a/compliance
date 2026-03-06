# POLICY: PT-2.1: Data Tagging

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-2.1 |
| NIST Control | PT-2.1: Data Tagging |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | data tagging, PII processing, authorized processing, privacy controls, data tracking |

## 1. POLICY STATEMENT
All personally identifiable information (PII) elements must be tagged with data labels that specify authorized processing activities and usage restrictions. Data tags must accompany PII throughout its lifecycle to enable tracking, enforcement of processing limitations, and automated privacy controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII data elements | YES | Includes structured and unstructured data |
| System databases containing PII | YES | Production, development, and test environments |
| Data processing applications | YES | Must support tag preservation and enforcement |
| Third-party data processors | YES | Must maintain tagging requirements |
| Public information | NO | Unless derived from PII sources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Define data tag taxonomies and processing categories<br>• Approve tag definitions and usage policies<br>• Monitor tag compliance and effectiveness |
| System Administrators | • Implement tagging mechanisms in systems<br>• Ensure tag preservation during data operations<br>• Configure automated tag enforcement |
| Data Stewards | • Apply appropriate tags to PII elements<br>• Validate tag accuracy and completeness<br>• Report tagging violations or gaps |

## 4. RULES
[RULE-01] All PII elements MUST be tagged with authorized processing categories before initial use or storage.
[VALIDATION] IF pii_element_exists = TRUE AND data_tag_present = FALSE THEN critical_violation

[RULE-02] Data tags MUST specify at minimum: processing purpose, retention period, sharing restrictions, and sensitivity classification.
[VALIDATION] IF data_tag_missing_required_fields > 0 THEN violation

[RULE-03] Tagged PII MUST NOT be processed for purposes not explicitly authorized in the data tag.
[VALIDATION] IF processing_purpose NOT IN authorized_purposes THEN violation

[RULE-04] Data tags MUST be preserved and updated during all data transformation, migration, and integration operations.
[VALIDATION] IF data_operation_completed = TRUE AND tag_preservation_verified = FALSE THEN violation

[RULE-05] Systems processing tagged PII MUST enforce tag-based access controls and usage restrictions automatically where technically feasible.
[VALIDATION] IF automated_tag_enforcement = FALSE AND technical_feasibility = TRUE THEN violation

[RULE-06] Data tag definitions and taxonomies MUST be reviewed and updated at least annually or when processing purposes change.
[VALIDATION] IF tag_taxonomy_last_review > 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Data Tagging Standards - Define tag formats, required fields, and application procedures
- [PROC-02] Tag Enforcement Monitoring - Regular verification of tag presence and accuracy
- [PROC-03] System Integration Tagging - Ensure tag preservation during system integrations
- [PROC-04] Third-Party Tag Requirements - Contractual requirements for external processors

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, system integrations, privacy incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Untagged PII Discovery]
IF pii_data_discovered = TRUE
AND data_tags_present = FALSE
AND data_age > 30_days
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Cross-System Data Transfer]
IF pii_transfer_initiated = TRUE
AND source_system_tagged = TRUE
AND destination_system_preserves_tags = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Processing Beyond Authorization]
IF data_processing_request = TRUE
AND requested_purpose NOT IN tag_authorized_purposes
AND purpose_expansion_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Development Environment Tagging]
IF environment_type = "development"
AND production_pii_copied = TRUE
AND development_tags_applied = TRUE
AND tag_restrictions_enforced = TRUE
THEN compliance = TRUE

[SCENARIO-05: Automated Tag Enforcement Failure]
IF system_supports_automation = TRUE
AND tag_enforcement_automated = FALSE
AND manual_controls_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data tags attached to PII elements | [RULE-01] |
| Tags contain authorized processing definitions | [RULE-02] |
| Processing restricted to authorized purposes | [RULE-03] |
| Tag preservation during data operations | [RULE-04] |
| Automated enforcement where feasible | [RULE-05] |
| Regular tag definition reviews | [RULE-06] |