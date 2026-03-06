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
All Privacy Act exemptions claimed for systems of records must be reviewed at defined intervals to ensure they remain legally appropriate, necessary, properly promulgated as regulations, and accurately described in system of records notices. Organizations must maintain current justification for all claimed exemptions and remove those no longer required.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Systems of Records | YES | All systems claiming Privacy Act exemptions |
| Contractor-Operated Systems | YES | When processing federal records under Privacy Act |
| Commercial Systems | NO | Unless processing federal records |
| Development/Test Systems | CONDITIONAL | If containing real PII covered by Privacy Act |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee exemption review process<br>• Approve exemption continuations or removals<br>• Ensure regulatory compliance |
| System Owners | • Maintain exemption documentation<br>• Conduct periodic reviews<br>• Update system of records notices |
| Legal Counsel | • Validate legal appropriateness<br>• Review regulatory requirements<br>• Approve exemption language |

## 4. RULES

**[RULE-01]** Organizations MUST review all Privacy Act exemptions for each system of records at least annually to ensure continued appropriateness and necessity.
**[VALIDATION]** IF exemption_last_review_date > 365_days_ago THEN violation

**[RULE-02]** All Privacy Act exemptions MUST be promulgated as formal regulations through the Federal Register rulemaking process.
**[VALIDATION]** IF exemption_claimed = TRUE AND regulation_published = FALSE THEN critical_violation

**[RULE-03]** System of records notices (SORNs) MUST accurately describe all claimed exemptions including specific Privacy Act provisions exempted and justification.
**[VALIDATION]** IF exemption_in_regulation != exemption_in_SORN THEN violation

**[RULE-04]** Exemption documentation MUST include system name, specific Privacy Act provisions exempted, reasons for exemption, and explanation of necessity and appropriateness.
**[VALIDATION]** IF exemption_documentation_complete = FALSE THEN violation

**[RULE-05]** Organizations MUST remove exemptions that are no longer appropriate, necessary, or legally justified within 90 days of determination.
**[VALIDATION]** IF exemption_removal_required = TRUE AND removal_date > determination_date + 90_days THEN violation

## 5. REQUIRED PROCEDURES
- **[PROC-01]** Annual Exemption Review - Systematic review of all claimed exemptions for continued validity
- **[PROC-02]** Exemption Documentation Maintenance - Ongoing maintenance of exemption justifications and regulatory status
- **[PROC-03]** SORN Update Process - Process for updating system of records notices when exemptions change

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Changes in Privacy Act regulations, new exemption claims, system modifications affecting PII processing

## 7. SCENARIO PATTERNS

**[SCENARIO-01: Outdated Exemption Review]**
IF exemption_claimed = TRUE
AND last_review_date > 18_months_ago
AND no_documented_review_scheduled = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

**[SCENARIO-02: Unpromulgated Exemption]**
IF exemption_applied_to_records = TRUE
AND federal_register_regulation = FALSE
AND exemption_age > 6_months
THEN compliance = FALSE
violation_severity = "Critical"

**[SCENARIO-03: SORN Mismatch]**
IF regulation_exempts_provision_X = TRUE
AND SORN_lists_provision_Y = TRUE
AND provision_X != provision_Y
THEN compliance = FALSE
violation_severity = "High"

**[SCENARIO-04: Incomplete Documentation]**
IF exemption_claimed = TRUE
AND (justification_missing = TRUE OR necessity_explanation_missing = TRUE)
THEN compliance = FALSE
violation_severity = "Moderate"

**[SCENARIO-05: Overdue Exemption Removal]**
IF exemption_determination = "no_longer_appropriate"
AND determination_date < current_date - 90_days
AND exemption_still_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Regular exemption review at defined frequency | RULE-01 |
| Exemptions promulgated as regulations | RULE-02 |
| Accurate SORN descriptions of exemptions | RULE-03 |
| Complete exemption documentation | RULE-04 |
| Timely removal of inappropriate exemptions | RULE-05 |