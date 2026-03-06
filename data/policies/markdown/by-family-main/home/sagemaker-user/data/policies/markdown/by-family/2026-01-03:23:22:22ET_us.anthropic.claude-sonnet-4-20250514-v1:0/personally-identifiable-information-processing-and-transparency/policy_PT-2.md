# POLICY: PT-2: Authority to Process Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-2 |
| NIST Control | PT-2: Authority to Process Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, processing, authority, documentation, privacy, legal basis, authorized processing |

## 1. POLICY STATEMENT
The organization SHALL determine, document, and maintain legal or organizational authority for all processing of personally identifiable information (PII). PII processing SHALL be restricted to only authorized purposes with documented legal basis and appropriate controls to manage privacy risks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems that collect, store, process, or transmit PII |
| All Personnel | YES | Staff handling PII in any capacity |
| Third-Party Processors | YES | Contractors, vendors processing PII on behalf of organization |
| Business Applications | YES | Applications that process PII data |
| Data Sharing Agreements | YES | All agreements involving PII exchange |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Establish PII processing authorities<br>• Review and approve processing documentation<br>• Oversee privacy risk assessments |
| Data Owners | • Document processing purposes for their data<br>• Ensure processing aligns with authorized purposes<br>• Maintain current processing documentation |
| Legal Counsel | • Validate legal basis for PII processing<br>• Review processing authorities and documentation<br>• Advise on regulatory compliance requirements |
| System Administrators | • Implement technical controls to restrict unauthorized processing<br>• Monitor PII processing activities<br>• Report unauthorized processing incidents |

## 4. RULES
[RULE-01] All PII processing activities MUST have documented legal or organizational authority before commencement.
[VALIDATION] IF pii_processing = TRUE AND documented_authority = FALSE THEN violation

[RULE-02] Processing authority documentation MUST specify the type of processing permitted, data categories, and legal basis.
[VALIDATION] IF authority_doc EXISTS AND (processing_type = NULL OR data_categories = NULL OR legal_basis = NULL) THEN violation

[RULE-03] PII processing SHALL be restricted to only the purposes and methods specified in the documented authority.
[VALIDATION] IF actual_processing NOT IN authorized_processing_types THEN violation

[RULE-04] Processing authority documentation MUST be reviewed and updated within 30 days of any change to processing activities or legal requirements.
[VALIDATION] IF processing_change_date > (last_authority_review + 30_days) THEN violation

[RULE-05] Organizations MUST conduct privacy risk assessments for all authorized PII processing activities annually.
[VALIDATION] IF pii_processing = TRUE AND (privacy_risk_assessment = NULL OR assessment_age > 365_days) THEN violation

[RULE-06] Personnel involved in PII processing MUST receive training on authorized processing requirements within 30 days of role assignment.
[VALIDATION] IF pii_access = TRUE AND (training_completion = NULL OR role_start_date > (training_date + 30_days)) THEN violation

[RULE-07] Technical controls MUST be implemented to prevent unauthorized PII processing operations.
[VALIDATION] IF pii_system = TRUE AND technical_controls_implemented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Processing Authority Assessment - Evaluate and document legal basis for new processing activities
- [PROC-02] Processing Documentation Review - Annual review of all processing authority documentation
- [PROC-03] Privacy Risk Assessment - Assess privacy risks for authorized processing activities
- [PROC-04] Unauthorized Processing Response - Incident response for unauthorized PII processing
- [PROC-05] Third-Party Processing Validation - Verify contractor/vendor processing authorities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New PII processing activities, regulatory changes, privacy incidents, system changes, legal requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Marketing Campaign Processing]
IF new_processing_activity = "marketing_campaign"
AND pii_categories = ["email", "demographics"]
AND documented_authority = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Third-Party Analytics Processing]
IF processor_type = "third_party"
AND processing_purpose = "analytics"
AND data_sharing_agreement_current = TRUE
AND processing_within_scope = TRUE
THEN compliance = TRUE

[SCENARIO-03: Employee Data for Unauthorized Purpose]
IF data_subject_type = "employee"
AND processing_purpose = "performance_monitoring"
AND authorized_purposes = ["payroll", "benefits"]
AND "performance_monitoring" NOT IN authorized_purposes
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Expired Processing Authority]
IF processing_authority_expiration < current_date
AND processing_status = "active"
AND renewal_documentation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Privacy Risk Assessment Overdue]
IF pii_processing = TRUE
AND last_privacy_assessment > 365_days_ago
AND processing_risk_level = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authority to process PII is determined and documented | [RULE-01], [RULE-02] |
| Processing types are defined and documented | [RULE-02] |
| PII processing restricted to authorized purposes only | [RULE-03] |
| Documentation maintained current | [RULE-04] |
| Privacy risks assessed for authorized processing | [RULE-05] |
| Personnel training on authorized processing | [RULE-06] |
| Technical controls prevent unauthorized processing | [RULE-07] |