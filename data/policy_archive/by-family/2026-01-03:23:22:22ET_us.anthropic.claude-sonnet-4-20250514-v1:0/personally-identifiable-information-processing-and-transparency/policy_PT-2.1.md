# POLICY: PT-2.1: Data Tagging

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-2.1 |
| NIST Control | PT-2.1: Data Tagging |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | data tagging, PII processing, authorized processing, privacy controls, data classification |

## 1. POLICY STATEMENT
All personally identifiable information (PII) elements within organizational systems MUST be tagged with data tags that specify authorized processing activities. Data tags SHALL be maintained throughout the PII lifecycle to enable tracking and enforcement of authorized processing activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII data elements | YES | Includes structured and unstructured PII |
| Cloud-based PII storage | YES | All hybrid cloud infrastructure |
| Third-party PII processors | YES | When processing on organization's behalf |
| Public datasets | NO | Unless containing organizational PII |
| De-identified data | CONDITIONAL | Only if re-identification risk exists |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Define data tagging taxonomy and standards<br>• Oversee data tagging compliance<br>• Approve processing authorizations |
| System Administrators | • Implement data tagging mechanisms<br>• Monitor tag integrity and accuracy<br>• Report tagging violations |
| Data Stewards | • Apply appropriate tags to PII elements<br>• Validate tag accuracy during processing<br>• Update tags when processing changes |

## 4. RULES
[RULE-01] All PII elements MUST be tagged with data tags that specify authorized processing activities before any processing occurs.
[VALIDATION] IF pii_element.processing_initiated = TRUE AND pii_element.data_tag = NULL THEN violation

[RULE-02] Data tags MUST include at minimum: processing purpose, authorized personnel/systems, retention period, and sharing restrictions.
[VALIDATION] IF data_tag.missing_required_fields > 0 THEN violation

[RULE-03] Data tags SHALL be updated within 24 hours when processing authorizations change.
[VALIDATION] IF processing_authorization.change_date + 24_hours < current_time AND data_tag.last_updated < processing_authorization.change_date THEN violation

[RULE-04] Automated tools MUST validate data tag compliance before processing PII elements.
[VALIDATION] IF pii_processing.initiated = TRUE AND automated_validation.completed = FALSE THEN violation

[RULE-05] Data tags MUST NOT be removed or modified without proper authorization from the Data Protection Officer.
[VALIDATION] IF data_tag.modified = TRUE AND authorization.dpo_approved = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Tagging Standards - Define taxonomy and format for PII data tags
- [PROC-02] Tag Application Process - Systematic approach for applying tags to PII elements
- [PROC-03] Tag Monitoring and Validation - Regular verification of tag accuracy and compliance
- [PROC-04] Tag Update Management - Process for updating tags when processing changes
- [PROC-05] Violation Response - Procedures for addressing data tagging violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy incident, regulatory change, new PII processing activity, system architecture changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Untagged PII Processing]
IF pii_data.processing_active = TRUE
AND pii_data.data_tag = NULL
AND processing_duration > 0_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Processing Authorization]
IF data_tag.processing_purpose = "marketing"
AND current_authorization.processing_purpose = "analytics"
AND tag_update_delay > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Required Tag Fields]
IF data_tag.retention_period = NULL
OR data_tag.authorized_personnel = NULL
OR data_tag.sharing_restrictions = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unauthorized Tag Modification]
IF data_tag.last_modified_by != "authorized_personnel"
AND dpo_approval = FALSE
AND tag_modification_time > baseline_time
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Automated Validation Bypass]
IF pii_processing.status = "active"
AND automated_validation.bypassed = TRUE
AND manual_override.documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data tags attached to PII elements | [RULE-01] |
| Tags contain authorized processing definitions | [RULE-02] |
| Tag maintenance and updates | [RULE-03] |
| Automated tool integration | [RULE-04] |
| Tag modification controls | [RULE-05] |