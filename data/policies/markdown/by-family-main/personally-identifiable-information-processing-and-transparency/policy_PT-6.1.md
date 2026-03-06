# POLICY: PT-6.1: Routine Uses

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-6.1 |
| NIST Control | PT-6.1: Routine Uses |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | routine uses, system of records notice, Privacy Act, PII disclosure, compatibility review |

## 1. POLICY STATEMENT
The organization SHALL regularly review all routine uses published in system of records notices to ensure continued accuracy and compatibility with original collection purposes. All routine use disclosures MUST comply with Privacy Act requirements and be explicitly documented in published system of records notices.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Systems | YES | All systems subject to Privacy Act |
| Contractor Systems | CONDITIONAL | When processing federal records |
| Cloud Services | YES | When containing federal PII records |
| Legacy Systems | YES | All systems with published SORNs |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Establish routine use review frequency<br>• Approve routine use modifications<br>• Ensure SORN compliance |
| System Owners | • Conduct periodic routine use reviews<br>• Document compatibility assessments<br>• Report changes to privacy office |
| Privacy Officers | • Validate routine use accuracy<br>• Assess purpose compatibility<br>• Coordinate SORN updates |

## 4. RULES

[RULE-01] All routine uses published in system of records notices MUST be reviewed at least annually to ensure continued accuracy.
[VALIDATION] IF last_routine_use_review > 365_days THEN violation

[RULE-02] Routine use reviews MUST assess compatibility between disclosure purposes and original collection purposes.
[VALIDATION] IF routine_use_review_conducted = TRUE AND compatibility_assessment_documented = FALSE THEN violation

[RULE-03] Organizations MUST NOT disclose PII under routine uses that are not explicitly published in the applicable system of records notice.
[VALIDATION] IF disclosure_made = TRUE AND routine_use_published_in_SORN = FALSE THEN critical_violation

[RULE-04] Routine use reviews MUST be documented with findings and any recommended changes to system of records notices.
[VALIDATION] IF routine_use_review_conducted = TRUE AND documentation_complete = FALSE THEN violation

[RULE-05] Modified or discontinued routine uses MUST trigger updates to the published system of records notice within 60 days.
[VALIDATION] IF routine_use_changed = TRUE AND SORN_update_days > 60 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Routine Use Review Process - Annual assessment of all published routine uses for accuracy and compatibility
- [PROC-02] Compatibility Assessment - Evaluation methodology for determining purpose compatibility
- [PROC-03] SORN Update Process - Procedures for modifying system of records notices when routine uses change
- [PROC-04] Disclosure Tracking - Documentation requirements for all routine use disclosures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: New routine uses, Privacy Act updates, system changes, audit findings

## 7. SCENARIO PATTERNS

[SCENARIO-01: Annual Routine Use Review]
IF system_has_published_SORN = TRUE
AND last_routine_use_review > 365_days
AND no_documented_review_exists = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Undocumented Routine Use Disclosure]
IF PII_disclosure_made = TRUE
AND routine_use_published_in_SORN = FALSE
AND disclosure_purpose = "sharing_with_contractor"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Incompatible Purpose Assessment]
IF routine_use_review_conducted = TRUE
AND original_collection_purpose = "tax_administration"
AND routine_use_purpose = "marketing_research"
AND compatibility_finding = "incompatible"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Delayed SORN Update]
IF routine_use_discontinued = TRUE
AND discontinuation_date = 90_days_ago
AND SORN_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Routine Use Management]
IF routine_use_review_current = TRUE
AND compatibility_documented = TRUE
AND SORN_reflects_current_uses = TRUE
AND disclosure_tracking_complete = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Review routine uses at defined frequency | [RULE-01] |
| Ensure continued accuracy of routine uses | [RULE-01], [RULE-04] |
| Ensure compatibility with collection purpose | [RULE-02] |
| Only disclose under published routine uses | [RULE-03] |
| Document routine use reviews | [RULE-04] |
| Update SORNs when routine uses change | [RULE-05] |