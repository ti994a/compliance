```markdown
# POLICY: PT-2: Authority to Process Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-2 |
| NIST Control | PT-2: Authority to Process Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII processing, authority documentation, privacy controls, data processing, authorized use |

## 1. POLICY STATEMENT
The organization SHALL determine and document legal and organizational authority for processing personally identifiable information (PII) and restrict PII processing to only authorized purposes. All PII processing operations must be explicitly authorized and documented through appropriate legal instruments and organizational policies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems processing, storing, or transmitting PII |
| All Personnel | YES | Staff with access to or responsibility for PII |
| Third-Party Processors | YES | Contractors, vendors processing PII on behalf of organization |
| Cloud Services | YES | All cloud-hosted systems containing PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Establish PII processing authorities<br>• Review and approve processing documentation<br>• Monitor compliance with processing restrictions |
| Data Controllers | • Document specific processing authorities for their systems<br>• Ensure processing stays within authorized scope<br>• Conduct regular processing reviews |
| Legal Counsel | • Validate legal basis for PII processing<br>• Review processing agreements and contracts<br>• Advise on regulatory compliance requirements |

## 4. RULES

[RULE-01] Organizations MUST determine and document the legal or organizational authority that permits each type of PII processing operation before processing begins.
[VALIDATION] IF pii_processing_initiated = TRUE AND authority_documented = FALSE THEN critical_violation

[RULE-02] PII processing operations SHALL be restricted to only those purposes and methods explicitly authorized in documented authorities.
[VALIDATION] IF processing_scope > authorized_scope THEN violation

[RULE-03] Processing authority documentation MUST include specific types of PII, processing operations, purposes, legal basis, and retention periods.
[VALIDATION] IF authority_document_missing_required_elements = TRUE THEN violation

[RULE-04] Personnel involved in PII processing MUST receive training on authorized processing requirements within 30 days of role assignment.
[VALIDATION] IF personnel_pii_access = TRUE AND training_completion_date > (role_start_date + 30_days) THEN violation

[RULE-05] Organizations SHALL conduct quarterly audits to verify PII processing remains within authorized boundaries.
[VALIDATION] IF last_processing_audit_date > (current_date - 90_days) THEN violation

[RULE-06] Any changes to PII processing scope or purpose MUST be reviewed and approved by the Chief Privacy Officer before implementation.
[VALIDATION] IF processing_scope_changed = TRUE AND cpo_approval = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Processing Authority Assessment - Evaluate legal basis and organizational authority for new processing
- [PROC-02] Processing Documentation Review - Annual review of all PII processing authority documents
- [PROC-03] Processing Scope Monitoring - Quarterly verification that processing remains within authorized limits
- [PROC-04] Authority Change Management - Process for modifying existing PII processing authorities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New regulatory requirements, significant processing changes, privacy incidents, legal challenges

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Processing Expansion]
IF system_processes_new_pii_type = TRUE
AND processing_authority_updated = FALSE
AND processing_duration > 24_hours
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Missing Processing Documentation]
IF pii_processing_active = TRUE
AND authority_documentation_exists = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Third-Party Processing Without Authority]
IF third_party_processes_pii = TRUE
AND data_processing_agreement_signed = FALSE
AND processing_authority_delegated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Processing Beyond Authorized Scope]
IF current_processing_purpose NOT IN authorized_purposes
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant New Processing Initiative]
IF new_pii_processing_requested = TRUE
AND legal_basis_documented = TRUE
AND cpo_approval_obtained = TRUE
AND processing_within_scope = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authority to permit processing is determined and documented | RULE-01, RULE-03 |
| Processing types are defined and documented | RULE-03, RULE-06 |
| Processing restricted to authorized purposes only | RULE-02, RULE-04 |
| Processing scope restrictions are enforced | RULE-05, RULE-06 |
```