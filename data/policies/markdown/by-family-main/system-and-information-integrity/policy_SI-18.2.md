# POLICY: SI-18.2: Data Tags

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18.2 |
| NIST Control | SI-18.2: Data Tags |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | data tags, PII, automation, correction, deletion, information lifecycle |

## 1. POLICY STATEMENT
The organization SHALL employ data tags to automate the correction or deletion of personally identifiable information (PII) across the information lifecycle within organizational systems. Data tags MUST enable automated tools to identify, process, and manage PII according to established processing permissions and retention requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Including cloud, hybrid, and on-premises |
| Third-party systems | YES | When processing organizational PII |
| Development/test systems | YES | When containing production PII |
| Archived data | YES | Throughout entire lifecycle |
| Public-facing systems | YES | Customer and employee PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define data tagging schema and requirements<br>• Approve automated correction/deletion procedures<br>• Monitor compliance with lifecycle management |
| Data Owners | • Classify PII and assign appropriate tags<br>• Define processing permissions and retention periods<br>• Validate automated correction/deletion results |
| System Administrators | • Implement data tagging mechanisms<br>• Configure automated correction/deletion tools<br>• Maintain audit logs of automated actions |

## 4. RULES
[RULE-01] All PII within organizational systems MUST be tagged with processing permissions, authority to process, de-identification status, impact level, lifecycle stage, and retention dates.
[VALIDATION] IF pii_detected = TRUE AND (processing_permission_tag = NULL OR authority_tag = NULL OR impact_level_tag = NULL OR retention_date_tag = NULL) THEN violation

[RULE-02] Data tags MUST be automatically applied at the point of PII creation or ingestion into organizational systems.
[VALIDATION] IF pii_created = TRUE AND tag_application_time > pii_creation_time + 1_hour THEN violation

[RULE-03] Automated correction tools MUST use data tags to identify and process PII correction requests within 72 hours of request submission.
[VALIDATION] IF correction_request = TRUE AND processing_time > 72_hours AND automation_available = TRUE THEN violation

[RULE-04] Automated deletion tools MUST use data tags to identify and delete PII upon retention period expiration or deletion request.
[VALIDATION] IF (retention_date < current_date OR deletion_request = TRUE) AND pii_exists = TRUE AND deletion_time > 30_days THEN violation

[RULE-05] Data tags MUST be updated automatically when PII processing permissions, authority, or lifecycle stage changes.
[VALIDATION] IF pii_status_change = TRUE AND tag_update_time > status_change_time + 24_hours THEN violation

[RULE-06] All automated correction and deletion actions MUST be logged with reference to the data tags that triggered the action.
[VALIDATION] IF (automated_correction = TRUE OR automated_deletion = TRUE) AND audit_log_entry = NULL THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Tag Schema Management - Define and maintain standardized tagging schema for PII
- [PROC-02] Automated Tool Configuration - Configure and test automated correction/deletion tools
- [PROC-03] Tag Validation and Quality Assurance - Regular validation of tag accuracy and completeness
- [PROC-04] Exception Handling - Process cases where automated actions cannot be completed
- [PROC-05] Audit Log Review - Regular review of automated correction/deletion activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy regulation changes, system architecture changes, data breach incidents, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Required Tags]
IF pii_identified = TRUE
AND processing_permission_tag = NULL
AND system_production = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Automated Deletion Failure]
IF retention_date < current_date
AND pii_still_exists = TRUE
AND deletion_automation_enabled = TRUE
AND days_overdue > 30
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Correction Request Processing]
IF correction_request_submitted = TRUE
AND automation_tools_available = TRUE
AND processing_time <= 72_hours
AND audit_log_exists = TRUE
THEN compliance = TRUE

[SCENARIO-04: Tag Update Lag]
IF pii_processing_authority_changed = TRUE
AND tag_update_time <= 24_hours
AND automated_update = TRUE
THEN compliance = TRUE

[SCENARIO-05: Third-party System Integration]
IF third_party_system = TRUE
AND processes_org_pii = TRUE
AND data_tags_implemented = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data tags employed to automate PII correction/deletion across lifecycle | RULE-01, RULE-02, RULE-03, RULE-04 |
| Tags include processing permissions and authority | RULE-01, RULE-05 |
| Tags support automated tool functionality | RULE-03, RULE-04, RULE-06 |
| Lifecycle management automation | RULE-04, RULE-05 |