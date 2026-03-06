```markdown
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
All personally identifiable information (PII) elements within organizational systems MUST be tagged with metadata that defines authorized processing activities. Data tags SHALL support automated tracking and enforcement of privacy controls throughout the PII lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII data elements | YES | Including structured and unstructured data |
| Cloud-based PII storage | YES | Across all deployment models |
| Third-party PII processors | YES | When processing on organization's behalf |
| Archived PII data | YES | Including backup and disaster recovery systems |
| Development/test environments | CONDITIONAL | Only if containing production PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define data tagging taxonomy and standards<br>• Approve authorized processing categories<br>• Monitor tagging compliance across organization |
| Data Owners | • Classify PII elements requiring tags<br>• Define authorized processing for their data<br>• Validate tag accuracy and completeness |
| System Administrators | • Implement automated tagging mechanisms<br>• Maintain tag integrity during data operations<br>• Generate tagging compliance reports |

## 4. RULES
[RULE-01] All PII elements MUST be tagged with metadata defining authorized processing activities before being stored or processed in organizational systems.
[VALIDATION] IF pii_element.exists = TRUE AND pii_element.data_tag.exists = FALSE THEN violation

[RULE-02] Data tags MUST include at minimum: processing purpose, authorized users/roles, retention period, and permissible operations.
[VALIDATION] IF data_tag.missing_required_fields > 0 THEN violation

[RULE-03] Automated tagging mechanisms MUST be implemented for systems processing more than 1000 PII records per day.
[VALIDATION] IF daily_pii_volume > 1000 AND automated_tagging = FALSE THEN violation

[RULE-04] Data tags MUST be updated within 24 hours when authorized processing activities change.
[VALIDATION] IF processing_change_date + 24_hours < current_time AND tag_update_date < processing_change_date THEN violation

[RULE-05] Systems MUST enforce processing restrictions based on data tags before allowing access to PII elements.
[VALIDATION] IF pii_access_request.purpose NOT IN data_tag.authorized_processing THEN access_denied

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Classification and Tagging - Systematic identification and tagging of PII elements
- [PROC-02] Tag Validation and Monitoring - Regular verification of tag accuracy and completeness
- [PROC-03] Automated Tag Management - Implementation and maintenance of automated tagging systems
- [PROC-04] Exception Handling - Process for managing untagged or improperly tagged PII

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy incident, new PII processing activity, regulatory changes, system modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: New PII Collection]
IF new_pii_data = TRUE
AND data_collection_date > policy_effective_date
AND data_tag.exists = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Cloud Migration with PII]
IF pii_migration_to_cloud = TRUE
AND destination_system.tagging_capability = TRUE
AND migrated_data.tagged = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Third-party Processing]
IF third_party_processor = TRUE
AND pii_shared = TRUE
AND shared_data.tags_included = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Automated Processing Validation]
IF processing_request.automated = TRUE
AND requested_operation NOT IN data_tag.authorized_processing
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Tag Update After Policy Change]
IF processing_policy_updated = TRUE
AND policy_change_date + 24_hours < current_time
AND affected_tags.updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data tags containing authorized processing are attached to PII elements | [RULE-01], [RULE-02] |
| Automated tools support data tag enforcement | [RULE-03], [RULE-05] |
| Tag accuracy and currency maintained | [RULE-04] |
| Processing restrictions enforced via tags | [RULE-05] |
```