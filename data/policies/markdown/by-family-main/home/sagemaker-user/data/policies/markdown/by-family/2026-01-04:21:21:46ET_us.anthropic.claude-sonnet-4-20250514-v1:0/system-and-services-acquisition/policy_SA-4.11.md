# POLICY: SA-4.11: System of Records

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.11 |
| NIST Control | SA-4.11: System of Records |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy act, system of records, acquisition contracts, third party operations, PII processing |

## 1. POLICY STATEMENT
All acquisition contracts for third-party operation of systems of records on behalf of the organization MUST include explicit Privacy Act requirements and compliance obligations. Contractors operating systems of records SHALL be subject to the same Privacy Act requirements as the organization itself.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External contractors | YES | When operating systems of records |
| Cloud service providers | YES | When processing PII in systems of records |
| Software-as-a-Service vendors | YES | When maintaining organizational records with PII |
| Internal IT operations | NO | Covered under separate internal policies |
| Data processors (non-records) | CONDITIONAL | Only if creating/maintaining systems of records |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define Privacy Act requirements for contracts<br>• Review and approve system of records contracts<br>• Monitor contractor compliance with Privacy Act |
| Procurement Officer | • Ensure Privacy Act clauses in acquisition contracts<br>• Coordinate with CPO on contract requirements<br>• Validate contractor acknowledgment of obligations |
| Contract Manager | • Monitor ongoing contractor Privacy Act compliance<br>• Document compliance verification activities<br>• Escalate non-compliance issues |

## 4. RULES
[RULE-01] All acquisition contracts for system of records operations MUST include specific Privacy Act requirements and compliance obligations before contract execution.
[VALIDATION] IF contract_type = "system_of_records_operation" AND privacy_act_clauses = FALSE THEN critical_violation

[RULE-02] Privacy Act requirements in contracts SHALL be defined and documented prior to solicitation release.
[VALIDATION] IF solicitation_released = TRUE AND privacy_act_requirements_defined = FALSE THEN violation

[RULE-03] Contractors operating systems of records MUST acknowledge in writing their understanding and acceptance of Privacy Act obligations.
[VALIDATION] IF contractor_operates_records = TRUE AND written_acknowledgment = FALSE THEN violation

[RULE-04] Contract performance monitoring SHALL include verification of Privacy Act compliance at least quarterly.
[VALIDATION] IF system_of_records_contract = TRUE AND last_privacy_verification > 90_days THEN violation

[RULE-05] Privacy Act requirement definitions MUST be reviewed and updated during contract modifications that affect PII processing scope.
[VALIDATION] IF contract_modification = TRUE AND pii_scope_change = TRUE AND privacy_requirements_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privacy Act Contract Requirements Definition - Establish specific Privacy Act clauses for each system of records contract
- [PROC-02] Contractor Privacy Act Compliance Verification - Quarterly assessment of contractor adherence to Privacy Act requirements
- [PROC-03] System of Records Contract Review - Pre-execution review ensuring Privacy Act requirement inclusion

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New Privacy Act guidance, contract performance issues, privacy incidents involving contractors

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Provider PII Processing]
IF vendor_type = "cloud_service_provider"
AND processes_organizational_pii = TRUE
AND creates_system_of_records = TRUE
AND contract_includes_privacy_act_clauses = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Contractor Acknowledgment Missing]
IF contract_executed = TRUE
AND contractor_operates_records = TRUE
AND written_privacy_act_acknowledgment = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Quarterly Compliance Verification Overdue]
IF active_system_of_records_contract = TRUE
AND last_compliance_verification_date > 90_days
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Contract Modification Without Privacy Update]
IF contract_modification_executed = TRUE
AND pii_processing_scope_expanded = TRUE
AND privacy_act_requirements_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Proper Implementation]
IF system_of_records_contract = TRUE
AND privacy_act_clauses_included = TRUE
AND contractor_acknowledgment_documented = TRUE
AND quarterly_verification_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privacy Act requirements for system of records operation are defined | [RULE-02] |
| Privacy Act requirements are included in acquisition contracts | [RULE-01] |
| Contractor compliance with Privacy Act obligations is verified | [RULE-04] |
| Contract modifications address Privacy Act requirement changes | [RULE-05] |