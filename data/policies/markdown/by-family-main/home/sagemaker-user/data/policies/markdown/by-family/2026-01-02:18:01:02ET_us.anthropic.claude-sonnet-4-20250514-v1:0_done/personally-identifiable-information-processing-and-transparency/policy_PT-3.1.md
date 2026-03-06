# POLICY: PT-3.1: Data Tagging

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-3.1 |
| NIST Control | PT-3.1: Data Tagging |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | data tagging, PII processing, privacy purposes, automated tracking, data elements |

## 1. POLICY STATEMENT
All personally identifiable information (PII) elements MUST be tagged with data tags containing their authorized processing purposes as they transit through organizational systems. Data tags MUST remain attached to PII elements throughout their lifecycle to enable purpose tracking and compatibility assessment for any processing changes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII data elements | YES | Includes structured and unstructured data |
| Cloud systems processing PII | YES | Hybrid cloud infrastructure included |
| Third-party data processors | YES | When processing organizational PII |
| Development/test environments | YES | When containing production PII |
| Archived PII data | YES | Tags must persist through archival |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Define data tagging schema and purposes<br>• Approve processing purpose changes<br>• Monitor tag compliance across systems |
| System Administrators | • Implement data tagging mechanisms<br>• Ensure tag persistence during data transfers<br>• Maintain automated tagging tools |
| Data Owners | • Define authorized processing purposes for their data<br>• Validate tag accuracy during data reviews<br>• Report tag compliance issues |

## 4. RULES
[RULE-01] All PII elements MUST be tagged with data tags containing at least one authorized processing purpose before initial processing.
[VALIDATION] IF pii_element.data_tag IS NULL OR pii_element.data_tag.purposes IS EMPTY THEN violation

[RULE-02] Data tags MUST persist with PII elements during all system transfers, transformations, and storage operations.
[VALIDATION] IF data_transfer_occurred = TRUE AND destination_pii.data_tag != source_pii.data_tag THEN violation

[RULE-03] Processing purpose changes MUST be validated against existing data tags before implementation to ensure compatibility.
[VALIDATION] IF new_processing_purpose NOT IN existing_data_tag.authorized_purposes AND compatibility_assessment = FALSE THEN violation

[RULE-04] Data tagging schema MUST include processing purpose, data classification, retention period, and authorized user roles.
[VALIDATION] IF data_tag_schema MISSING (purpose OR classification OR retention OR authorized_roles) THEN violation

[RULE-05] Automated data tagging tools MUST be implemented for systems processing more than 1000 PII records daily.
[VALIDATION] IF daily_pii_volume > 1000 AND automated_tagging = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Tag Schema Management - Define and maintain standardized tagging formats and purpose categories
- [PROC-02] PII Element Identification - Systematic discovery and classification of PII data elements
- [PROC-03] Tag Compliance Monitoring - Regular verification of tag presence and accuracy
- [PROC-04] Purpose Compatibility Assessment - Evaluation process for processing changes against existing tags

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployments, data breach incidents, regulatory changes, processing purpose modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Untagged PII Processing]
IF pii_element.identified = TRUE
AND pii_element.data_tag IS NULL
AND processing_initiated = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Tag Loss During Transfer]
IF data_transfer.source_tagged = TRUE
AND data_transfer.destination_tagged = FALSE
AND transfer_completed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incompatible Purpose Change]
IF processing_purpose_change = TRUE
AND new_purpose NOT IN data_tag.authorized_purposes
AND compatibility_assessment.approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Compliant Tagged Processing]
IF pii_element.data_tag.present = TRUE
AND processing_purpose IN data_tag.authorized_purposes
AND tag_schema.complete = TRUE
THEN compliance = TRUE

[SCENARIO-05: Missing Automated Tagging]
IF system.daily_pii_volume > 1000
AND automated_tagging.implemented = FALSE
AND manual_tagging.error_rate > 5%
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data tags containing processing purposes are attached to PII elements | [RULE-01], [RULE-04] |
| Tags persist throughout PII lifecycle | [RULE-02] |
| Processing purpose compatibility validation | [RULE-03] |
| Automated tagging implementation for high-volume systems | [RULE-05] |