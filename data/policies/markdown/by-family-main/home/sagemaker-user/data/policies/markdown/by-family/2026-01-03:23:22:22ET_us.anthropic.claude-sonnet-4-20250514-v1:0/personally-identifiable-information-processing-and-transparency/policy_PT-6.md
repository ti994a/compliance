```markdown
POLICY: PT-6: System of Records Notice

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-6 |
| NIST Control | PT-6: System of Records Notice |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy act, system of records, federal register, OMB guidance, congressional review |

1. POLICY STATEMENT
Systems processing information maintained in Privacy Act systems of records MUST draft, review, publish, and maintain accurate system of records notices in accordance with OMB guidance and Privacy Act requirements. All notices MUST be submitted for advance review and published in the Federal Register.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Information Systems | YES | Only systems processing Privacy Act records |
| Contractor Systems | CONDITIONAL | If processing federal Privacy Act records |
| State/Local Systems | NO | Unless processing federal records |
| Development/Test Systems | CONDITIONAL | If containing real Privacy Act records |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee SORN development and accuracy<br>• Submit SORNs to OMB and Congress<br>• Ensure Federal Register publication |
| System Owners | • Identify Privacy Act applicability<br>• Provide system details for SORN drafting<br>• Report system modifications |
| Legal Counsel | • Review SORN compliance with Privacy Act<br>• Validate OMB guidance adherence |

4. RULES
[RULE-01] Systems processing Privacy Act records MUST have a system of records notice (SORN) drafted in accordance with OMB A-108 guidance.
[VALIDATION] IF system_processes_privacy_act_records = TRUE AND sorn_exists = FALSE THEN violation

[RULE-02] New and significantly modified SORNs MUST be submitted to OMB and appropriate congressional committees for advance review before publication.
[VALIDATION] IF sorn_status IN ["new", "significantly_modified"] AND advance_review_submitted = FALSE THEN violation

[RULE-03] All SORNs MUST be published in the Federal Register within 60 days of OMB approval.
[VALIDATION] IF omb_approval_date IS NOT NULL AND federal_register_publication = FALSE AND days_since_approval > 60 THEN violation

[RULE-04] SORNs MUST be reviewed annually and updated within 30 days when system changes affect notice accuracy.
[VALIDATION] IF last_sorn_review > 365_days OR (system_modification_date > last_sorn_update AND days_since_modification > 30) THEN violation

[RULE-05] SORNs MUST include all required elements per OMB A-108: system name, authority, purpose, categories of records, categories of individuals, routine uses, and disclosure procedures.
[VALIDATION] IF sorn_required_elements_complete = FALSE THEN violation

5. REQUIRED PROCEDURES
- [PROC-01] SORN Development Process - Standardized process for drafting SORNs with all required elements
- [PROC-02] OMB and Congressional Submission - Process for advance review submission and tracking
- [PROC-03] Federal Register Publication - Coordination with Federal Register for timely publication
- [PROC-04] SORN Maintenance and Updates - Regular review and update procedures for accuracy

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Privacy Act amendments, OMB guidance updates, system modifications, audit findings

7. SCENARIO PATTERNS
[SCENARIO-01: New System with Privacy Act Records]
IF system_status = "new"
AND processes_privacy_act_records = TRUE
AND sorn_drafted = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: System Modification Without SORN Update]
IF system_modification_date < current_date - 45_days
AND modification_affects_privacy_act_records = TRUE
AND sorn_last_updated < system_modification_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Federal Register Publication]
IF omb_approval_received = TRUE
AND approval_date < current_date - 70_days
AND federal_register_published = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Incomplete SORN Elements]
IF sorn_exists = TRUE
AND required_elements_count < 7
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Annual Review Overdue]
IF sorn_last_review_date < current_date - 400_days
AND system_active = TRUE
AND processes_privacy_act_records = TRUE
THEN compliance = FALSE
violation_severity = "Low"

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| SORNs drafted per OMB guidance | RULE-01, RULE-05 |
| Advance review submission | RULE-02 |
| Federal Register publication | RULE-03 |
| SORN accuracy and currency | RULE-04 |
```