# POLICY: PT-3.1: Data Tagging

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-3.1 |
| NIST Control | PT-3.1: Data Tagging |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | data tagging, PII processing, processing purposes, privacy transparency, data elements |

## 1. POLICY STATEMENT
All personally identifiable information (PII) elements within organizational systems MUST be tagged with data tags that clearly identify their authorized processing purposes. Data tags SHALL accompany PII elements throughout their lifecycle to enable tracking and compatibility assessment of processing activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems processing PII | YES | Including cloud, hybrid, and on-premises systems |
| Third-party systems with PII access | YES | Via contractual requirements |
| Development and testing environments | YES | When containing production PII |
| Archived PII data | YES | Tags must be preserved during archival |
| De-identified data | CONDITIONAL | Only if re-identification risk exists |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define data tagging schema and standards<br>• Approve processing purpose categories<br>• Monitor compliance with tagging requirements |
| Data Stewards | • Implement data tagging for assigned systems<br>• Ensure tag accuracy and completeness<br>• Validate processing purpose compatibility |
| System Owners | • Configure systems to support data tagging<br>• Ensure tags transit with PII elements<br>• Report tagging compliance status |

## 4. RULES
[RULE-01] All PII elements MUST be tagged with data tags containing their authorized processing purposes before initial use or within 30 days of policy implementation.
[VALIDATION] IF pii_element.data_tag IS NULL OR pii_element.processing_purposes IS EMPTY THEN violation

[RULE-02] Data tags SHALL use the organization's approved data tagging schema and contain only pre-defined processing purpose categories.
[VALIDATION] IF data_tag.schema_version != approved_version OR processing_purpose NOT IN approved_purposes THEN violation

[RULE-03] Data tags MUST accompany PII elements during all data transfers, processing operations, and storage activities within organizational systems.
[VALIDATION] IF pii_transfer_event AND (source_tag != destination_tag OR destination_tag IS NULL) THEN violation

[RULE-04] Processing purpose compatibility assessments MUST be performed and documented before any change in PII processing activities.
[VALIDATION] IF processing_change_request AND compatibility_assessment.completed = FALSE THEN violation

[RULE-05] Automated data tagging tools SHALL be implemented for systems processing more than 10,000 PII records to ensure consistent tag application.
[VALIDATION] IF pii_record_count > 10000 AND automated_tagging = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Tagging Schema Management - Define and maintain approved processing purposes and tag formats
- [PROC-02] PII Element Identification and Tagging - Systematic process for identifying and tagging PII elements
- [PROC-03] Processing Purpose Compatibility Assessment - Evaluate whether processing changes align with tagged purposes
- [PROC-04] Tag Validation and Audit - Regular verification of tag accuracy and completeness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, system changes, privacy incidents, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Untagged PII Discovery]
IF pii_element.identified = TRUE
AND data_tag.exists = FALSE
AND discovery_date > policy_effective_date + 30_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Processing Purpose Change]
IF current_processing != original_tagged_purpose
AND compatibility_assessment.completed = TRUE
AND compatibility_assessment.result = "compatible"
AND tag_update.completed = TRUE
THEN compliance = TRUE

[SCENARIO-03: Third-Party Data Transfer]
IF data_transfer.destination = "third_party"
AND pii_elements.tagged = TRUE
AND contractual_tagging_requirements.enforced = TRUE
AND recipient_tag_support.verified = TRUE
THEN compliance = TRUE

[SCENARIO-04: Automated Tagging Failure]
IF system.pii_record_count > 10000
AND automated_tagging.implemented = FALSE
AND manual_tagging.error_rate > 5%
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Legacy System Integration]
IF legacy_system.pii_processing = TRUE
AND data_tagging.supported = FALSE
AND remediation_plan.approved = TRUE
AND implementation_deadline < 90_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data tags containing processing purposes are attached to PII elements | [RULE-01], [RULE-02] |
| Tags accompany PII throughout system processing | [RULE-03] |
| Processing purpose compatibility is maintained | [RULE-04] |
| Automated tools support consistent tagging | [RULE-05] |