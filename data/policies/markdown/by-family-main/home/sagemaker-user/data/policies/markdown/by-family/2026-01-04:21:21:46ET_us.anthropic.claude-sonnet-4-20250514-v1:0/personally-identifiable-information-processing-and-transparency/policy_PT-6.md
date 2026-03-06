# POLICY: PT-6: System of Records Notice

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-6 |
| NIST Control | PT-6: System of Records Notice |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy act, system of records, federal register, OMB guidance, SORN, congressional review |

## 1. POLICY STATEMENT
Systems that process information maintained in a Privacy Act system of records MUST publish accurate system of records notices (SORNs) in the Federal Register following OMB guidance and advance review requirements. SORNs MUST be kept current and properly scoped to ensure transparency and legal compliance with Privacy Act obligations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Systems | YES | Systems processing Privacy Act records |
| Contractor Systems | CONDITIONAL | If processing federal Privacy Act records |
| Commercial Systems | NO | Unless under federal contract |
| Development Systems | CONDITIONAL | If containing Privacy Act records |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Draft and maintain SORNs<br>• Submit SORNs for OMB review<br>• Ensure Federal Register publication<br>• Monitor SORN accuracy and scope |
| System Owners | • Identify Privacy Act systems<br>• Provide system details for SORN drafting<br>• Notify CPO of system modifications<br>• Ensure system compliance with published SORN |
| Legal Counsel | • Review SORN legal compliance<br>• Coordinate congressional submissions<br>• Advise on Privacy Act requirements |

## 4. RULES
[RULE-01] Systems processing Privacy Act records MUST have SORNs drafted in accordance with current OMB A-108 guidance and Privacy Act requirements.
[VALIDATION] IF system_processes_privacy_act_records = TRUE AND sorn_follows_omb_guidance = FALSE THEN violation

[RULE-02] New SORNs and significantly modified SORNs MUST be submitted to OMB and appropriate congressional committees for advance review before publication.
[VALIDATION] IF sorn_status = "new" OR modification_significance = "major" AND advance_review_completed = FALSE THEN violation

[RULE-03] All SORNs MUST be published in the Federal Register within 30 days of completing advance review requirements.
[VALIDATION] IF advance_review_complete_date + 30_days < current_date AND federal_register_published = FALSE THEN violation

[RULE-04] SORNs MUST be reviewed annually and updated within 60 days when system changes affect SORN accuracy or scope.
[VALIDATION] IF last_sorn_review + 365_days < current_date THEN violation
[VALIDATION] IF system_change_date + 60_days < current_date AND sorn_updated = FALSE AND change_affects_sorn = TRUE THEN violation

[RULE-05] SORNs MUST accurately reflect current system operations, data categories, routine uses, and retention schedules.
[VALIDATION] IF sorn_accuracy_verified = FALSE OR sorn_scope_current = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SORN Development Process - Standardized process for drafting SORNs using OMB templates and guidance
- [PROC-02] OMB and Congressional Review - Submission and tracking procedures for advance review requirements
- [PROC-03] Federal Register Publication - Process for publishing SORNs and managing publication timelines
- [PROC-04] SORN Maintenance - Annual review and update procedures for existing SORNs
- [PROC-05] System Change Impact Assessment - Process to evaluate when system changes require SORN modifications

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when OMB guidance changes
- Triggering events: New Privacy Act systems, major system modifications, OMB guidance updates, Privacy Act amendments

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Launch]
IF system_type = "new"
AND processes_privacy_act_records = TRUE
AND sorn_published = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: System Modification]
IF system_modification_date = "2024-01-15"
AND modification_affects_data_categories = TRUE
AND sorn_last_updated < "2024-01-15"
AND current_date > "2024-03-15"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Congressional Review]
IF sorn_type = "new"
AND omb_review_completed = TRUE
AND congressional_review_completed = FALSE
AND federal_register_published = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated SORN Content]
IF sorn_last_review + 365_days < current_date
AND annual_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Routine Use Expansion]
IF new_routine_use_added = TRUE
AND routine_use_date + 60_days < current_date
AND sorn_updated_for_routine_use = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| SORNs drafted per OMB guidance | [RULE-01] |
| Advance review submission | [RULE-02] |
| Federal Register publication | [RULE-03] |
| SORN accuracy and currency | [RULE-04], [RULE-05] |
| Proper system scoping | [RULE-05] |