# POLICY: PT-6.2: Exemption Rules

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-6.2 |
| NIST Control | PT-6.2: Exemption Rules |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy act, exemptions, system of records, regulations, SORN, review |

## 1. POLICY STATEMENT
All Privacy Act exemptions claimed for systems of records MUST be reviewed at defined intervals to ensure they remain appropriate, necessary, legally compliant, properly promulgated as regulations, and accurately described in system of records notices.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Systems of Records | YES | All systems subject to Privacy Act |
| Privacy Act Exemptions | YES | Both (j) and (k) exemptions |
| Contractor Systems | CONDITIONAL | If processing federal records |
| Commercial Systems | NO | Unless processing federal PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define exemption review frequency<br>• Approve exemption determinations<br>• Ensure regulatory compliance |
| Privacy Officers | • Conduct periodic exemption reviews<br>• Validate SORN accuracy<br>• Document review findings |
| Legal Counsel | • Verify regulatory promulgation<br>• Assess legal appropriateness<br>• Review exemption justifications |
| System Owners | • Provide system information<br>• Implement exemption requirements<br>• Report changes affecting exemptions |

## 4. RULES
[RULE-01] Organizations MUST define and document the frequency for reviewing Privacy Act exemptions for each system of records.
[VALIDATION] IF exemption_review_frequency = "undefined" OR exemption_review_frequency = "null" THEN violation

[RULE-02] Privacy Act exemption reviews MUST be conducted at the defined frequency for each system of records.
[VALIDATION] IF current_date > (last_review_date + review_frequency_days) THEN violation

[RULE-03] Exemption reviews MUST verify that claimed exemptions remain appropriate and necessary in accordance with law.
[VALIDATION] IF exemption_appropriateness_assessed = FALSE OR exemption_necessity_assessed = FALSE THEN violation

[RULE-04] Exemption reviews MUST confirm that all claimed exemptions have been properly promulgated as regulations.
[VALIDATION] IF exemption_claimed = TRUE AND regulatory_promulgation_verified = FALSE THEN critical_violation

[RULE-05] Exemption reviews MUST ensure that all claimed exemptions are accurately described in the system of records notice.
[VALIDATION] IF exemption_in_regulation = TRUE AND exemption_in_sorn = FALSE THEN violation

[RULE-06] Organizations MUST maintain documentation of exemption reviews including findings, justifications, and any corrective actions.
[VALIDATION] IF exemption_review_conducted = TRUE AND review_documentation = "incomplete" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Exemption Review Process - Systematic review of claimed exemptions against legal requirements
- [PROC-02] SORN Accuracy Validation - Verification that exemptions are correctly described in notices
- [PROC-03] Regulatory Compliance Check - Confirmation of proper regulatory promulgation
- [PROC-04] Exemption Documentation - Maintenance of review records and justifications

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New exemptions claimed, regulatory changes, system modifications, legal updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Overdue Exemption Review]
IF exemption_claimed = TRUE
AND last_review_date + review_frequency < current_date
AND extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Unpromulgated Exemption]
IF exemption_claimed = TRUE
AND regulatory_status = "not_promulgated"
AND exemption_applied = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: SORN Mismatch]
IF exemption_in_regulation = TRUE
AND exemption_description_sorn ≠ exemption_description_regulation
AND discrepancy_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unnecessary Exemption]
IF exemption_review_completed = TRUE
AND exemption_necessity_finding = "not_necessary"
AND exemption_removal_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Missing Review Documentation]
IF exemption_review_due = TRUE
AND review_conducted = TRUE
AND review_documentation_complete = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Review exemptions at defined frequency | [RULE-01], [RULE-02] |
| Ensure exemptions remain appropriate and necessary | [RULE-03] |
| Verify exemptions promulgated as regulations | [RULE-04] |
| Ensure accurate description in SORN | [RULE-05] |
| Maintain review documentation | [RULE-06] |