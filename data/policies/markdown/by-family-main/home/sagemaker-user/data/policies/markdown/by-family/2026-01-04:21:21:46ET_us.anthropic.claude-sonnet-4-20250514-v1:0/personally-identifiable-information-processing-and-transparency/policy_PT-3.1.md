```markdown
# POLICY: PT-3.1: Data Tagging

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-3.1 |
| NIST Control | PT-3.1: Data Tagging |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | data tagging, PII processing, privacy controls, data classification, processing purposes |

## 1. POLICY STATEMENT
All personally identifiable information (PII) elements SHALL be tagged with data tags containing defined processing purposes. Data tags MUST accompany PII throughout the system lifecycle to enable purpose tracking and compatibility assessment for processing changes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII data elements | YES | Regardless of format or location |
| Third-party systems processing PII | YES | When under organizational control |
| Archived/backup PII | YES | Tags must be preserved |
| De-identified data | CONDITIONAL | If re-identification possible |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owners | • Define processing purposes for PII elements<br>• Approve data tag schemas<br>• Validate tag accuracy |
| System Administrators | • Implement data tagging mechanisms<br>• Ensure tags transit with PII<br>• Maintain tag integrity |
| Privacy Officers | • Define organizational tagging standards<br>• Monitor tag compliance<br>• Assess processing purpose compatibility |

## 4. RULES
[RULE-01] All PII elements MUST be tagged with data tags containing defined processing purposes before initial processing.
[VALIDATION] IF pii_element.processing_initiated = TRUE AND pii_element.data_tag = NULL THEN violation

[RULE-02] Data tags MUST contain explicitly defined processing purposes using the organization's standardized purpose taxonomy.
[VALIDATION] IF data_tag.processing_purpose NOT IN approved_purpose_taxonomy THEN violation

[RULE-03] Data tags SHALL transit with PII elements throughout all system operations including storage, transmission, and processing.
[VALIDATION] IF pii_element.location_changed = TRUE AND data_tag.location ≠ pii_element.location THEN violation

[RULE-04] Processing purpose changes MUST be evaluated for compatibility with existing data tags before implementation.
[VALIDATION] IF processing_purpose.changed = TRUE AND compatibility_assessment.completed = FALSE THEN violation

[RULE-05] Data tag schemas MUST be documented and approved by the Chief Privacy Officer before deployment.
[VALIDATION] IF data_tag_schema.deployed = TRUE AND cpo_approval.exists = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Tag Schema Development - Define standardized tagging formats and purpose taxonomies
- [PROC-02] PII Element Identification - Systematic discovery and classification of PII elements
- [PROC-03] Tag Implementation - Technical deployment of tagging mechanisms
- [PROC-04] Purpose Compatibility Assessment - Evaluation process for processing changes
- [PROC-05] Tag Integrity Monitoring - Ongoing verification of tag-PII association

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, system changes, privacy incidents, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Untagged PII Processing]
IF pii_element.identified = TRUE
AND data_processing.initiated = TRUE
AND data_tag.attached = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Invalid Processing Purpose]
IF data_tag.processing_purpose = "marketing"
AND approved_purpose_taxonomy.contains("marketing") = FALSE
AND pii_processing.active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Tag-Data Separation]
IF pii_element.location = "database_server_2"
AND data_tag.location = "database_server_1"
AND data_transmission.completed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Purpose Change Without Assessment]
IF processing_purpose.original = "account_management"
AND processing_purpose.new = "fraud_detection"
AND compatibility_assessment.performed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Tagged Processing]
IF pii_element.tagged = TRUE
AND data_tag.purpose IN approved_taxonomy
AND tag_location = pii_location
AND cpo_approval.exists = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data tags containing defined processing purposes are attached to PII elements | RULE-01, RULE-02 |
| Processing purposes are properly defined and documented | RULE-02, RULE-05 |
| Tags accompany PII throughout system operations | RULE-03 |
| Processing changes are assessed for purpose compatibility | RULE-04 |
```