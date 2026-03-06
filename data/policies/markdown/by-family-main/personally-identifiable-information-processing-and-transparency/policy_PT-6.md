```markdown
# POLICY: PT-6: System of Records Notice

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-6 |
| NIST Control | PT-6: System of Records Notice |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy act, system of records, federal register, OMB guidance, congressional review |

## 1. POLICY STATEMENT
For systems processing information maintained in Privacy Act systems of records, the organization MUST draft, review, publish, and maintain accurate system of records notices in accordance with OMB guidance and Privacy Act requirements. All notices MUST be published in the Federal Register and kept current with system operations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Information Systems | YES | Systems processing Privacy Act records |
| Contractor Systems | CONDITIONAL | If processing federal Privacy Act records |
| Development/Test Systems | YES | If containing real Privacy Act records |
| Cloud Services | YES | If storing Privacy Act records |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Draft and maintain system of records notices<br>• Submit notices for OMB review<br>• Ensure Federal Register publication |
| System Owners | • Identify systems requiring notices<br>• Provide accurate system information<br>• Report system modifications |
| Legal Counsel | • Review notices for legal compliance<br>• Coordinate congressional submissions<br>• Validate Privacy Act applicability |

## 4. RULES

[RULE-01] System of records notices MUST be drafted in accordance with current OMB guidance and Privacy Act requirements for all systems processing information maintained in Privacy Act systems of records.
[VALIDATION] IF system_processes_privacy_act_records = TRUE AND sorn_drafted_per_omb_guidance = FALSE THEN violation

[RULE-02] New and significantly modified system of records notices MUST be submitted to OMB and appropriate congressional committees for advance review before publication.
[VALIDATION] IF sorn_status IN ["new", "significantly_modified"] AND advance_review_completed = FALSE THEN violation

[RULE-03] System of records notices MUST be published in the Federal Register within 60 days of OMB approval.
[VALIDATION] IF omb_approval_date IS NOT NULL AND federal_register_publication_date > (omb_approval_date + 60_days) THEN violation

[RULE-04] System of records notices MUST be reviewed annually and updated within 30 days when system changes affect notice accuracy or scope.
[VALIDATION] IF last_review_date > (current_date - 365_days) OR (system_change_date IS NOT NULL AND notice_update_date > (system_change_date + 30_days)) THEN violation

[RULE-05] System of records notices MUST accurately reflect current system operations, data categories, routine uses, and retention schedules.
[VALIDATION] IF sorn_accuracy_verified = FALSE OR sorn_reflects_current_operations = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SORN Development Process - Standardized process for drafting notices per OMB A-108
- [PROC-02] OMB Review Coordination - Procedures for submitting notices for advance review
- [PROC-03] Federal Register Publication - Process for publishing approved notices
- [PROC-04] SORN Maintenance - Annual review and update procedures
- [PROC-05] System Change Assessment - Process to evaluate if changes require SORN updates

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New Privacy Act systems, significant system modifications, OMB guidance updates, Privacy Act amendments

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Privacy Act System]
IF system_type = "new"
AND processes_privacy_act_records = TRUE
AND sorn_drafted = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: System Modification Without SORN Update]
IF system_modification_date < current_date - 30_days
AND modification_affects_sorn = TRUE
AND sorn_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing OMB Review]
IF sorn_status = "significantly_modified"
AND federal_register_published = TRUE
AND omb_advance_review = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated SORN Information]
IF sorn_last_review > current_date - 365_days
AND system_operational = TRUE
AND processes_privacy_act_records = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Delayed Federal Register Publication]
IF omb_approval_date IS NOT NULL
AND days_since_approval > 60
AND federal_register_published = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| SORN drafted per OMB guidance | RULE-01 |
| Advance review by OMB and Congress | RULE-02 |
| Federal Register publication | RULE-03 |
| Accurate and up-to-date notices | RULE-04, RULE-05 |
| Proper scoping per policy | RULE-05 |
```