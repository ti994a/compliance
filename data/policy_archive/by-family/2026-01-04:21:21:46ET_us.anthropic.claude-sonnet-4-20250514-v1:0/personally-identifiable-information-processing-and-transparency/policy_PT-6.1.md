```markdown
# POLICY: PT-6(1): Routine Uses

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-6(1) |
| NIST Control | PT-6(1): Routine Uses |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | routine uses, system of records notice, Privacy Act, PII disclosure, compatibility review |

## 1. POLICY STATEMENT
The organization must regularly review all routine uses published in system of records notices to ensure continued accuracy and compatibility with the original collection purpose. Reviews must verify that routine use disclosures remain justified and properly documented.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Systems of Records | YES | Systems containing PII subject to Privacy Act |
| Published Routine Uses | YES | All routine uses in active SORNs |
| Federal Agencies | YES | Agencies maintaining systems of records |
| Third-party Recipients | CONDITIONAL | When receiving routine use disclosures |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Establish routine use review frequency<br>• Oversee compliance with review requirements<br>• Approve routine use modifications |
| System Owners | • Conduct periodic routine use reviews<br>• Document review findings<br>• Recommend routine use updates |
| Privacy Officers | • Validate compatibility assessments<br>• Ensure SORN accuracy<br>• Coordinate with legal counsel |

## 4. RULES
[RULE-01] All routine uses published in system of records notices MUST be reviewed at least annually to ensure continued accuracy and purpose compatibility.
[VALIDATION] IF last_review_date > 365_days AND system_status = "active" THEN violation

[RULE-02] Routine use reviews MUST verify that each disclosed use remains compatible with the original purpose for which the information was collected.
[VALIDATION] IF compatibility_assessment = "incompatible" AND routine_use_status = "active" THEN critical_violation

[RULE-03] Organizations MUST document all routine use review activities including findings, recommendations, and corrective actions taken.
[VALIDATION] IF review_conducted = TRUE AND documentation_complete = FALSE THEN violation

[RULE-04] Routine uses found to be inaccurate or incompatible MUST be updated in the system of records notice within 90 days of discovery.
[VALIDATION] IF issue_identified_date + 90_days < current_date AND sorn_updated = FALSE THEN violation

[RULE-05] New routine uses SHALL NOT be established without explicit publication in the relevant system of records notice.
[VALIDATION] IF routine_use_active = TRUE AND sorn_published = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Routine Use Review Process - Annual assessment of all published routine uses for accuracy and compatibility
- [PROC-02] Compatibility Assessment - Evaluation methodology for determining purpose compatibility
- [PROC-03] SORN Update Process - Procedures for modifying system of records notices
- [PROC-04] Documentation Standards - Requirements for maintaining review records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: New routine uses, system modifications, privacy incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Overdue Routine Use Review]
IF last_routine_use_review > 365_days
AND system_of_records_status = "active"
AND review_exemption = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Incompatible Routine Use]
IF compatibility_assessment = "incompatible"
AND routine_use_disclosure = "active"
AND corrective_action_taken = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Undocumented Review Activity]
IF routine_use_review_conducted = TRUE
AND review_documentation_exists = FALSE
AND review_date < 30_days_ago
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Delayed SORN Update]
IF routine_use_issue_identified = TRUE
AND days_since_identification > 90
AND sorn_update_published = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unauthorized Routine Use]
IF routine_use_disclosure = "active"
AND sorn_publication_status = "not_published"
AND disclosure_date > routine_use_start_date
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Review routine uses at defined frequency | [RULE-01] |
| Ensure continued accuracy of routine uses | [RULE-01], [RULE-04] |
| Verify purpose compatibility | [RULE-02] |
| Document review activities | [RULE-03] |
| Update SORNs when changes needed | [RULE-04] |
| Publish routine uses before establishment | [RULE-05] |
```