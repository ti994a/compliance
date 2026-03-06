# POLICY: PT-5.2: Privacy Act Statements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-5.2 |
| NIST Control | PT-5.2: Privacy Act Statements |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy act, statements, forms, collection, system of records, PII, notice |

## 1. POLICY STATEMENT
All forms that collect information to be maintained in a Privacy Act system of records MUST include Privacy Act statements either on the collection form or on separate retainable forms. Privacy Act statements SHALL provide individuals with sufficient information to make informed decisions about providing requested information.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal information systems | YES | All systems subject to Privacy Act |
| Paper forms | YES | Physical forms collecting PII |
| Electronic forms | YES | Web forms, mobile apps, online collection |
| Third-party contractors | YES | When collecting data on agency behalf |
| Non-federal systems | NO | Unless processing federal agency data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee Privacy Act statement implementation<br>• Review and approve statement content<br>• Ensure compliance monitoring |
| System Owners | • Implement Privacy Act statements on collection forms<br>• Coordinate with privacy office for statement content<br>• Maintain current statements |
| Legal Counsel | • Review Privacy Act statement language<br>• Provide guidance on legal requirements<br>• Advise on compliance issues |

## 4. RULES
[RULE-01] All forms collecting information for Privacy Act system of records MUST include Privacy Act statements either directly on the form or on separate retainable forms.
[VALIDATION] IF form_collects_PII = TRUE AND privacy_act_system = TRUE AND privacy_act_statement = FALSE THEN violation

[RULE-02] Privacy Act statements SHALL include authority for collection, mandatory/voluntary nature, principal purposes, routine uses, effects of non-disclosure, and system of records notice citation.
[VALIDATION] IF privacy_act_statement = TRUE AND (authority_citation = FALSE OR purpose_statement = FALSE OR routine_uses = FALSE OR disclosure_effects = FALSE OR sorn_citation = FALSE) THEN violation

[RULE-03] Privacy Act statements MUST be provided regardless of collection medium including paper forms, electronic forms, websites, mobile applications, or telephone collection.
[VALIDATION] IF collection_medium IN ["paper", "electronic", "web", "mobile", "telephone"] AND privacy_act_system = TRUE AND privacy_act_statement = FALSE THEN violation

[RULE-04] System owners SHALL consult with the Chief Privacy Officer and legal counsel when developing Privacy Act statements.
[VALIDATION] IF privacy_act_statement_created = TRUE AND (cpo_consultation = FALSE OR legal_review = FALSE) THEN violation

[RULE-05] Privacy Act statements MUST be updated within 30 days when system of records notices are modified or routine uses change.
[VALIDATION] IF sorn_modified = TRUE AND privacy_act_statement_updated = FALSE AND days_elapsed > 30 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privacy Act Statement Development - Standard process for creating compliant statements
- [PROC-02] Form Review and Approval - Workflow for reviewing collection forms
- [PROC-03] Statement Update Management - Process for maintaining current statements
- [PROC-04] Compliance Monitoring - Regular assessment of statement implementation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: SORN modifications, new collection systems, regulatory changes, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Web Form Without Statement]
IF collection_method = "web_form"
AND privacy_act_system = TRUE
AND privacy_act_statement_present = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Statement Elements]
IF privacy_act_statement_present = TRUE
AND authority_citation = TRUE
AND purpose_statement = FALSE
AND routine_uses = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Separate Retainable Form]
IF collection_form_has_statement = FALSE
AND separate_retainable_form = TRUE
AND statement_complete = TRUE
THEN compliance = TRUE

[SCENARIO-04: Third-Party Collection]
IF collector = "third_party_contractor"
AND collecting_for_agency = TRUE
AND privacy_act_system = TRUE
AND privacy_act_statement = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Outdated Statement After SORN Change]
IF sorn_last_modified = "2024-01-15"
AND privacy_act_statement_last_updated = "2023-12-01"
AND current_date = "2024-02-20"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privacy Act statements included on forms collecting information for system of records | RULE-01, RULE-03 |
| Privacy Act statements provided on separate retainable forms | RULE-01 |
| Complete statement content requirements | RULE-02 |
| Consultation with privacy and legal officials | RULE-04 |
| Statement currency and updates | RULE-05 |