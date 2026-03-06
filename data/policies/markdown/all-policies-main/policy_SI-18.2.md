# POLICY: SI-18.2: Data Tags

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18.2 |
| NIST Control | SI-18.2: Data Tags |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | data tags, PII, automation, deletion, correction, lifecycle, privacy |

## 1. POLICY STATEMENT
The organization MUST employ automated data tagging mechanisms to enable correction or deletion of personally identifiable information (PII) throughout its entire lifecycle within organizational systems. Data tags SHALL contain sufficient metadata to support automated privacy controls and compliance requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Including cloud, hybrid, and on-premises |
| Third-party systems with PII | YES | When under organizational control |
| Development/test systems | YES | If containing real PII data |
| Archived PII data | YES | Must maintain tag integrity |
| Public information | NO | Unless contains embedded PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Define tagging schema and standards<br>• Monitor tag compliance across systems<br>• Approve automated correction/deletion rules |
| System Administrators | • Implement data tagging mechanisms<br>• Configure automated PII management tools<br>• Maintain tag integrity during system operations |
| Data Owners | • Classify PII sensitivity levels<br>• Define retention and processing requirements<br>• Validate automated tag assignments |

## 4. RULES

[RULE-01] All PII within organizational systems MUST be tagged with metadata including processing permissions, authority to process, de-identification status, impact level, lifecycle stage, and retention dates.
[VALIDATION] IF pii_data_exists = TRUE AND required_tags_complete < 100% THEN violation

[RULE-02] Data tagging mechanisms MUST support automated correction and deletion of PII based on tag metadata without manual intervention.
[VALIDATION] IF automation_capability = FALSE OR manual_intervention_required = TRUE THEN violation

[RULE-03] PII tags MUST be updated within 24 hours when data classification, retention requirements, or processing permissions change.
[VALIDATION] IF tag_update_time > 24_hours AND metadata_changed = TRUE THEN violation

[RULE-04] Systems processing PII MUST maintain tag integrity during data operations including backup, restore, migration, and transformation processes.
[VALIDATION] IF data_operation_completed = TRUE AND tag_integrity_verified = FALSE THEN violation

[RULE-05] Automated PII correction or deletion actions MUST be logged with sufficient detail to support audit and compliance requirements.
[VALIDATION] IF automated_pii_action = TRUE AND audit_log_complete = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Tag Schema Management - Define and maintain standardized PII tagging schemas
- [PROC-02] Automated PII Lifecycle Management - Configure and monitor automated correction/deletion processes
- [PROC-03] Tag Integrity Verification - Regular validation of tag accuracy and completeness
- [PROC-04] Cross-System Tag Synchronization - Maintain consistent tagging across integrated systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, system integrations, regulatory changes, privacy incidents

## 7. SCENARIO PATTERNS

[SCENARIO-01: Untagged PII Discovery]
IF pii_discovered = TRUE
AND data_tags_present = FALSE
AND discovery_date > 7_days_ago
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Retention Period Exceeded]
IF pii_retention_date < current_date
AND automated_deletion_enabled = TRUE
AND pii_still_exists = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Manual PII Deletion Process]
IF pii_deletion_request = TRUE
AND manual_process_used = TRUE
AND automated_capability_available = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Tag Integrity After Migration]
IF system_migration_completed = TRUE
AND pii_tags_verified = TRUE
AND tag_integrity_maintained = TRUE
THEN compliance = TRUE

[SCENARIO-05: Processing Permission Change]
IF processing_permission_revoked = TRUE
AND tag_update_time <= 24_hours
AND automated_action_triggered = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data tags employed for PII automation | RULE-01, RULE-02 |
| Tags support correction/deletion across lifecycle | RULE-02, RULE-04 |
| Tag metadata includes required elements | RULE-01, RULE-03 |
| Automated mechanisms properly configured | RULE-02, RULE-05 |