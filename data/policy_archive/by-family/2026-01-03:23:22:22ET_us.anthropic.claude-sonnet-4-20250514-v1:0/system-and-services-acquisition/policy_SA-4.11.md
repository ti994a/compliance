# POLICY: SA-4.11: System of Records

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.11 |
| NIST Control | SA-4.11: System of Records |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy act, system of records, acquisition contracts, PII processing, third-party operations |

## 1. POLICY STATEMENT
All acquisition contracts for third-party operation of systems of records on behalf of the organization MUST include explicit Privacy Act requirements and compliance obligations. Contractors operating systems of records MUST demonstrate adherence to Privacy Act provisions throughout the contract lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Third-party contractors | YES | When operating systems of records |
| Cloud service providers | YES | When processing PII in systems of records |
| Acquisition contracts | YES | All contracts involving PII processing |
| Internal systems | NO | Covered by separate internal policies |
| Public-facing websites | CONDITIONAL | Only if collecting PII for records systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define Privacy Act requirements for contracts<br>• Review and approve contract privacy provisions<br>• Monitor contractor compliance |
| Procurement Officer | • Ensure Privacy Act requirements are included in solicitations<br>• Validate contractor privacy capabilities<br>• Execute compliant acquisition contracts |
| Contract Manager | • Monitor ongoing Privacy Act compliance<br>• Conduct regular contractor assessments<br>• Manage privacy-related contract modifications |

## 4. RULES
[RULE-01] All acquisition contracts for systems of records operation MUST include specific Privacy Act requirements before contract execution.
[VALIDATION] IF contract_type = "system_of_records_operation" AND privacy_act_requirements = "not_included" THEN critical_violation

[RULE-02] Privacy Act requirements MUST be defined and documented before solicitation release for any system of records operation contract.
[VALIDATION] IF solicitation_released = TRUE AND privacy_act_requirements = "undefined" THEN violation

[RULE-03] Contractors operating systems of records MUST demonstrate Privacy Act compliance capabilities during the acquisition evaluation process.
[VALIDATION] IF contractor_selected = TRUE AND privacy_act_compliance_demonstrated = FALSE THEN violation

[RULE-04] Contract modifications affecting PII processing MUST trigger review and update of Privacy Act requirements within 30 days.
[VALIDATION] IF contract_modification = TRUE AND pii_impact = TRUE AND privacy_review_days > 30 THEN violation

[RULE-05] Contractors MUST provide quarterly Privacy Act compliance reports for active systems of records operations.
[VALIDATION] IF contract_active = TRUE AND quarterly_report_overdue = TRUE THEN moderate_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privacy Act Requirements Definition - Establish specific Privacy Act obligations for each system of records contract
- [PROC-02] Contractor Privacy Assessment - Evaluate contractor Privacy Act compliance capabilities
- [PROC-03] Contract Privacy Monitoring - Ongoing oversight of contractor Privacy Act adherence
- [PROC-04] Privacy Incident Response - Handle Privacy Act violations by contractors

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Privacy Act amendments, major privacy incidents, contract performance issues

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Privacy Act Requirements]
IF contract_type = "system_of_records_operation"
AND privacy_act_requirements = "not_specified"
AND contract_status = "executed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Contractor Compliance Failure]
IF contractor_operating_records = TRUE
AND privacy_act_violation_reported = TRUE
AND corrective_action_plan = "not_submitted"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Adequate Contract Provisions]
IF contract_includes_privacy_requirements = TRUE
AND contractor_compliance_verified = TRUE
AND monitoring_active = TRUE
THEN compliance = TRUE

[SCENARIO-04: Contract Modification Impact]
IF contract_modification = TRUE
AND pii_processing_scope_changed = TRUE
AND privacy_requirements_updated = FALSE
AND days_since_modification > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Cloud Provider Records System]
IF service_type = "cloud_hosting"
AND processes_system_of_records = TRUE
AND privacy_act_requirements_included = TRUE
AND sla_includes_privacy_metrics = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privacy Act requirements are defined for system of records operations | [RULE-02] |
| Privacy Act requirements are included in acquisition contracts | [RULE-01] |
| Contractor Privacy Act compliance is verified | [RULE-03] |
| Ongoing compliance monitoring is maintained | [RULE-05] |