# POLICY: PT-5.2: Privacy Act Statements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-5.2 |
| NIST Control | PT-5.2: Privacy Act Statements |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy act, forms, collection, system of records, notice, pii |

## 1. POLICY STATEMENT
All forms that collect information to be maintained in a Privacy Act system of records MUST include Privacy Act statements or provide separate Privacy Act statements that individuals can retain. This ensures individuals receive required legal notice before providing personal information to federal agencies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Collection Forms | YES | All forms collecting PII for Privacy Act systems |
| Web Applications | YES | Online forms and data collection interfaces |
| Mobile Applications | YES | Apps collecting PII for Privacy Act systems |
| Third-Party Vendors | YES | When collecting PII on behalf of the organization |
| Internal Systems | CONDITIONAL | Only if maintaining Privacy Act system of records |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee Privacy Act statement implementation<br>• Review and approve Privacy Act statement content<br>• Coordinate with legal counsel on compliance |
| Form Developers | • Include required Privacy Act statements on forms<br>• Ensure statements are prominently displayed<br>• Validate statement accuracy before deployment |
| Legal Counsel | • Review Privacy Act statement content<br>• Provide guidance on legal requirements<br>• Advise on system of records applicability |

## 4. RULES
[RULE-01] All forms collecting information for Privacy Act systems of records MUST include a Privacy Act statement on the form itself or provide a separate retainable Privacy Act statement.
[VALIDATION] IF form_collects_pii = TRUE AND privacy_act_system = TRUE AND privacy_act_statement_present = FALSE THEN violation

[RULE-02] Privacy Act statements MUST include all six required elements: authority, mandatory/voluntary nature, principal purposes, routine uses, effects of non-disclosure, and system of records citation.
[VALIDATION] IF privacy_act_statement_elements < 6 THEN violation

[RULE-03] Privacy Act statements MUST be provided regardless of collection medium (paper, electronic, web, mobile, telephone).
[VALIDATION] IF collection_medium = ANY AND privacy_act_system = TRUE AND privacy_act_statement_present = FALSE THEN violation

[RULE-04] Form developers MUST consult with the Chief Privacy Officer and legal counsel before finalizing Privacy Act statements.
[VALIDATION] IF privacy_act_statement_created = TRUE AND (cpo_review = FALSE OR legal_review = FALSE) THEN violation

[RULE-05] Privacy Act statements on separate forms MUST be designed to be retainable by individuals.
[VALIDATION] IF separate_privacy_act_form = TRUE AND retainable_design = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privacy Act Statement Creation - Standard process for developing compliant Privacy Act statements
- [PROC-02] Form Review and Approval - Mandatory review process for all data collection forms
- [PROC-03] System of Records Determination - Process to identify when Privacy Act applies
- [PROC-04] Privacy Act Statement Updates - Process for maintaining current statements when systems change

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New Privacy Act system of records, changes to existing systems, legal updates, form modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Web Form Missing Privacy Act Statement]
IF form_type = "web_form"
AND collects_pii = TRUE
AND privacy_act_system = TRUE
AND privacy_act_statement_present = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Privacy Act Statement]
IF privacy_act_statement_present = TRUE
AND required_elements_count < 6
AND missing_elements INCLUDES "authority" OR "routine_uses"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Third-Party Vendor Collection]
IF data_collector = "third_party_vendor"
AND collecting_for_privacy_act_system = TRUE
AND vendor_privacy_act_statement_compliant = TRUE
AND cpo_approved = TRUE
THEN compliance = TRUE

[SCENARIO-04: Mobile App Without Statement]
IF collection_medium = "mobile_application"
AND privacy_act_system = TRUE
AND privacy_act_statement_accessible = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Separate Retainable Form]
IF privacy_act_statement_location = "separate_form"
AND form_retainable = TRUE
AND all_required_elements_present = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privacy Act statements included on forms collecting information for Privacy Act systems | RULE-01, RULE-03 |
| Privacy Act statements provided on separate retainable forms | RULE-05 |
| Complete Privacy Act statement content requirements | RULE-02 |
| Proper consultation with privacy and legal officials | RULE-04 |