# POLICY: PT-5.2: Privacy Act Statements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-5.2 |
| NIST Control | PT-5.2: Privacy Act Statements |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy act, forms, collection, statements, notices, PII, system of records |

## 1. POLICY STATEMENT
All forms that collect information to be maintained in a Privacy Act system of records MUST include Privacy Act statements either directly on the collection form or on separate retainable forms. Privacy Act statements MUST provide individuals with sufficient information to make informed decisions about providing requested information.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal information collection forms | YES | All forms collecting PII for Privacy Act systems |
| Electronic forms and websites | YES | Including mobile applications and online portals |
| Third-party contractors | YES | When collecting information on behalf of the organization |
| Internal administrative forms | CONDITIONAL | Only if maintained in Privacy Act system of records |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee Privacy Act statement compliance<br>• Review and approve Privacy Act statements<br>• Coordinate with legal counsel on notice requirements |
| Form Owners | • Ensure Privacy Act statements are included on collection forms<br>• Maintain current Privacy Act statements<br>• Coordinate with privacy office for statement content |
| Legal Counsel | • Review Privacy Act statement legal requirements<br>• Provide guidance on notice provisions<br>• Ensure compliance with Privacy Act obligations |

## 4. RULES
[RULE-01] All forms collecting information for Privacy Act systems of records MUST include Privacy Act statements either directly on the form or as separate retainable documents.
[VALIDATION] IF form_collects_PII = TRUE AND privacy_act_system = TRUE AND privacy_act_statement_present = FALSE THEN violation

[RULE-02] Privacy Act statements MUST include authority for collection, mandatory/voluntary nature, principal purposes, routine uses, effects of non-disclosure, and system of records notice citation.
[VALIDATION] IF privacy_act_statement_present = TRUE AND required_elements_count < 6 THEN violation

[RULE-03] Privacy Act statements MUST be provided regardless of collection medium including paper forms, electronic forms, websites, mobile applications, or telephone collection.
[VALIDATION] IF collection_medium = ANY AND privacy_act_system = TRUE AND privacy_act_statement_present = FALSE THEN violation

[RULE-04] Form owners MUST consult with the Chief Privacy Officer and legal counsel when developing or modifying Privacy Act statements.
[VALIDATION] IF privacy_act_statement_modified = TRUE AND (CPO_consultation = FALSE OR legal_consultation = FALSE) THEN violation

[RULE-05] Privacy Act statements on separate forms MUST be designed to be retainable by individuals providing information.
[VALIDATION] IF separate_privacy_statement = TRUE AND retainable_format = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privacy Act Statement Development - Standard process for creating compliant Privacy Act statements
- [PROC-02] Form Review and Approval - Mandatory review process for all information collection forms
- [PROC-03] Privacy Act Statement Updates - Process for maintaining current Privacy Act statements when systems change

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New information collection, system of records changes, legal requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Online Form Without Statement]
IF form_type = "electronic"
AND collects_PII = TRUE
AND privacy_act_system = TRUE
AND privacy_act_statement_present = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Privacy Statement]
IF privacy_act_statement_present = TRUE
AND required_elements_count < 6
AND form_deployed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Third-Party Collection Form]
IF collector = "third_party_contractor"
AND collects_for_privacy_act_system = TRUE
AND privacy_act_statement_provided = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Telephone Collection Process]
IF collection_method = "telephone"
AND privacy_act_system = TRUE
AND verbal_privacy_notice = FALSE
AND written_statement_available = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Updated System Without Statement Update]
IF system_of_records_modified = TRUE
AND privacy_act_statement_updated = FALSE
AND days_since_modification > 30
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privacy Act statements included on forms collecting information for Privacy Act systems | RULE-01 |
| Privacy Act statements provided on separate retainable forms | RULE-01, RULE-05 |
| Required Privacy Act statement elements included | RULE-02 |
| Privacy Act statements provided across all collection mediums | RULE-03 |