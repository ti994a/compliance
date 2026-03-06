# POLICY: PT-6.1: Routine Uses

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-6.1 |
| NIST Control | PT-6.1: Routine Uses |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | routine uses, Privacy Act, system of records notice, SORN, disclosure, compatibility |

## 1. POLICY STATEMENT
The organization SHALL regularly review all routine uses published in system of records notices to ensure continued accuracy and compatibility with the original collection purpose. All routine use disclosures MUST be explicitly authorized through published system of records notices and remain compatible with the purpose for which information was originally collected.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Systems of Records | YES | All systems subject to Privacy Act |
| Contractor-Operated Systems | YES | When processing federal records |
| Third-Party Recipients | YES | All entities receiving routine use disclosures |
| Cloud Service Providers | CONDITIONAL | When processing Privacy Act records |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Establish routine use review frequency<br>• Approve routine use determinations<br>• Oversee SORN maintenance |
| Privacy Officers | • Conduct routine use reviews<br>• Assess compatibility determinations<br>• Document review findings |
| System Owners | • Identify routine use requirements<br>• Coordinate with privacy office<br>• Implement disclosure controls |

## 4. RULES
[RULE-01] All routine uses MUST be explicitly published in the relevant system of records notice before any disclosure occurs.
[VALIDATION] IF disclosure_occurs = TRUE AND routine_use_published = FALSE THEN critical_violation

[RULE-02] Routine uses SHALL be reviewed at least annually to ensure continued accuracy and compatibility with collection purpose.
[VALIDATION] IF last_review_date > 365_days AND system_active = TRUE THEN violation

[RULE-03] Each routine use disclosure MUST be compatible with the purpose for which the information was originally collected.
[VALIDATION] IF disclosure_purpose != compatible_with_collection_purpose THEN critical_violation

[RULE-04] Routine use reviews MUST document the assessment of continued compatibility and accuracy.
[VALIDATION] IF review_completed = TRUE AND documentation_exists = FALSE THEN violation

[RULE-05] Any changes to routine uses MUST be reflected through formal SORN amendment processes.
[VALIDATION] IF routine_use_changed = TRUE AND sorn_amended = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Routine Use Review Process - Annual assessment of all published routine uses
- [PROC-02] Compatibility Assessment - Evaluation of routine use alignment with collection purpose
- [PROC-03] SORN Amendment Process - Formal update procedures for routine use changes
- [PROC-04] Disclosure Authorization - Pre-disclosure verification of routine use authority

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: SORN updates, new routine uses, compatibility concerns, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Expired Routine Use Review]
IF last_routine_use_review > 365_days
AND system_of_records_active = TRUE
AND no_documented_extension = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Undocumented Routine Use Disclosure]
IF disclosure_occurred = TRUE
AND routine_use_published_in_sorn = FALSE
AND emergency_exception = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Incompatible Purpose Disclosure]
IF routine_use_purpose = "law_enforcement"
AND original_collection_purpose = "benefits_administration"
AND compatibility_assessment = "incompatible"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Undocumented Review Process]
IF routine_use_review_conducted = TRUE
AND review_documentation_exists = FALSE
AND findings_recorded = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Valid Routine Use with Documentation]
IF routine_use_published_in_sorn = TRUE
AND last_review_date <= 365_days
AND compatibility_documented = TRUE
AND disclosure_authorized = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Review routine uses at defined frequency | RULE-02 |
| Ensure continued accuracy of routine uses | RULE-04 |
| Ensure compatibility with collection purpose | RULE-03 |
| Maintain published routine use authorities | RULE-01, RULE-05 |