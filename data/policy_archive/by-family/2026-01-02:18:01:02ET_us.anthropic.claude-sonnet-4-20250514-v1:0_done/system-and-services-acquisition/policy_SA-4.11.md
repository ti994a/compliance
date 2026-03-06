# POLICY: SA-4.11: System of Records

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.11 |
| NIST Control | SA-4.11: System of Records |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy act, system of records, acquisition contracts, external operations, PII processing |

## 1. POLICY STATEMENT
All acquisition contracts for external operation of systems of records on behalf of the organization MUST include Privacy Act requirements. Contractors operating systems of records MUST comply with all applicable Privacy Act provisions as if they were federal agencies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External contractors | YES | When operating systems of records |
| Cloud service providers | YES | When processing PII in systems of records |
| Managed service providers | YES | When managing systems containing records |
| Internal IT operations | NO | Covered by separate internal policies |
| Non-PII processing systems | NO | Privacy Act not applicable |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define Privacy Act requirements for contracts<br>• Review and approve contract privacy provisions<br>• Monitor contractor compliance |
| Procurement Officer | • Include Privacy Act clauses in acquisition contracts<br>• Ensure contractor acknowledgment of requirements<br>• Validate contractor privacy capabilities |
| Contract Manager | • Monitor ongoing Privacy Act compliance<br>• Conduct contractor privacy assessments<br>• Manage privacy-related contract modifications |

## 4. RULES
[RULE-01] All acquisition contracts for systems of records operation MUST include specific Privacy Act requirements and compliance obligations.
[VALIDATION] IF contract_type = "system_of_records_operation" AND privacy_act_clauses = FALSE THEN critical_violation

[RULE-02] Privacy Act requirements MUST be defined and documented before contract award for any system of records operation.
[VALIDATION] IF contract_award_date <= privacy_requirements_defined_date THEN violation

[RULE-03] Contractors operating systems of records MUST demonstrate Privacy Act compliance capabilities during the acquisition process.
[VALIDATION] IF contractor_privacy_capability_verified = FALSE AND system_of_records = TRUE THEN violation

[RULE-04] Contract modifications affecting Privacy Act compliance MUST be reviewed and approved by the Chief Privacy Officer within 10 business days.
[VALIDATION] IF contract_modification_affects_privacy = TRUE AND cpo_approval_time > 10_business_days THEN violation

[RULE-05] Contractors MUST provide annual Privacy Act compliance attestation and supporting evidence.
[VALIDATION] IF last_compliance_attestation_date > 365_days AND contract_active = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privacy Act Contract Requirements Definition - Process for identifying and documenting Privacy Act obligations
- [PROC-02] Contractor Privacy Capability Assessment - Evaluation of contractor's Privacy Act compliance capabilities
- [PROC-03] Privacy Contract Clause Integration - Standard clauses and customization process
- [PROC-04] Ongoing Privacy Compliance Monitoring - Regular assessment of contractor Privacy Act adherence

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Privacy Act updates, major contract awards, privacy incidents involving contractors

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Provider System of Records]
IF service_type = "cloud_hosting"
AND processes_system_of_records = TRUE
AND privacy_act_clauses_included = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Managed Service Privacy Compliance]
IF contractor_role = "managed_services"
AND manages_PII_systems = TRUE
AND privacy_capability_assessment = "not_conducted"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Contract Modification Impact]
IF contract_change_type = "scope_expansion"
AND new_scope_includes_PII = TRUE
AND privacy_officer_review = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Annual Compliance Verification]
IF contractor_type = "system_operator"
AND operates_system_of_records = TRUE
AND last_attestation_date > 12_months
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Pre-Award Requirements]
IF procurement_phase = "pre_award"
AND system_of_records_operation = TRUE
AND privacy_requirements_documented = TRUE
AND contractor_capability_verified = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privacy Act requirements are defined in acquisition contracts | [RULE-01], [RULE-02] |
| Contractors demonstrate Privacy Act compliance capabilities | [RULE-03] |
| Ongoing Privacy Act compliance monitoring | [RULE-05] |
| Contract modification privacy review | [RULE-04] |