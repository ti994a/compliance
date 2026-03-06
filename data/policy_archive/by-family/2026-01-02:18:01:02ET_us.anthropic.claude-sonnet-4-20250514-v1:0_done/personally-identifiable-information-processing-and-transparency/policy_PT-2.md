# POLICY: PT-2: Authority to Process Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-2 |
| NIST Control | PT-2: Authority to Process Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII processing, legal authority, data processing, privacy compliance, authorized use |

## 1. POLICY STATEMENT
The organization SHALL determine and document legal authority for all personally identifiable information (PII) processing activities and restrict PII processing to only authorized purposes. All PII processing operations must be explicitly authorized through documented legal basis and organizational policies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Including cloud, hybrid, and on-premises |
| Third-party processors | YES | Via contracts and agreements |
| Employees handling PII | YES | All roles with PII access |
| Data sharing activities | YES | Internal and external sharing |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Document processing authorities<br>• Review legal basis determinations<br>• Approve PII processing activities |
| Data Controllers | • Identify PII processing needs<br>• Ensure lawful basis exists<br>• Implement processing restrictions |
| Legal Counsel | • Validate legal authorities<br>• Review compliance requirements<br>• Advise on jurisdictional issues |

## 4. RULES
[RULE-01] All PII processing activities MUST have documented legal authority before processing begins.
[VALIDATION] IF pii_processing_activity = TRUE AND documented_authority = FALSE THEN critical_violation

[RULE-02] Processing authority documentation MUST specify the types of PII, processing operations, and legal basis.
[VALIDATION] IF authority_document EXISTS AND (pii_types = NULL OR processing_operations = NULL OR legal_basis = NULL) THEN violation

[RULE-03] PII processing SHALL be restricted to only those operations explicitly authorized in the documented authority.
[VALIDATION] IF actual_processing NOT IN authorized_processing_list THEN violation

[RULE-04] Processing authority documentation MUST be reviewed and updated within 30 days of any change in legal requirements or organizational policies.
[VALIDATION] IF legal_change_date < (current_date - 30_days) AND authority_review_date < legal_change_date THEN violation

[RULE-05] All personnel with PII access MUST receive training on authorized processing limitations within 30 days of access grant.
[VALIDATION] IF pii_access_granted = TRUE AND training_completion_date > (access_grant_date + 30_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Processing Authority Assessment - Evaluate and document legal basis for processing
- [PROC-02] Processing Restriction Implementation - Technical and administrative controls to limit processing
- [PROC-03] Authority Documentation Review - Periodic review of processing authorities
- [PROC-04] Unauthorized Processing Detection - Monitoring and auditing of PII use

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Legal/regulatory changes, new processing activities, privacy incidents, system changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Marketing Campaign]
IF new_processing_purpose = "marketing"
AND documented_authority = FALSE
AND pii_processing_initiated = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Data Analytics Beyond Scope]
IF processing_type = "data_mining"
AND authorized_operations NOT CONTAINS "analytics"
AND pii_accessed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Third-Party Data Sharing]
IF data_recipient = "external_party"
AND sharing_authority_documented = TRUE
AND contract_includes_restrictions = TRUE
THEN compliance = TRUE

[SCENARIO-04: Employee Training Delay]
IF employee_pii_access = TRUE
AND access_grant_date < (current_date - 45_days)
AND training_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Legacy System Processing]
IF system_age > 2_years
AND processing_authority_review_date < (current_date - 1_year)
AND active_pii_processing = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authority determination and documentation | RULE-01, RULE-02 |
| Processing restriction to authorized purposes | RULE-03 |
| Authority documentation maintenance | RULE-04 |
| Personnel training on authorized processing | RULE-05 |