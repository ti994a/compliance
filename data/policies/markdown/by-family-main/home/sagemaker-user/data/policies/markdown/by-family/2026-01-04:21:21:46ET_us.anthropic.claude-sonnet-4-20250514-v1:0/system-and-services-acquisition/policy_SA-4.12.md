# POLICY: SA-4.12: Data Ownership

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.12 |
| NIST Control | SA-4.12: Data Ownership |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | data ownership, contractor data, acquisition contracts, data removal, data return |

## 1. POLICY STATEMENT
All acquisition contracts involving contractor access to organizational data MUST include explicit data ownership requirements and mandatory data removal/return provisions. Contractors SHALL remove all organizational data from their systems and return it to the organization within contractually defined timeframes upon contract termination or expiration.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All acquisition contracts | YES | When contractor accesses organizational data |
| Software-as-a-Service contracts | YES | Including cloud service providers |
| Professional services contracts | YES | When data processing is involved |
| Hardware maintenance contracts | CONDITIONAL | Only if data access required |
| Public domain data contracts | NO | No organizational data ownership |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Define standard data ownership contract clauses<br>• Approve all acquisition contracts with data provisions<br>• Ensure contract compliance monitoring |
| Contract Manager | • Include data ownership requirements in all applicable contracts<br>• Define specific data removal timeframes<br>• Monitor contractor compliance with data return requirements |
| Data Protection Officer | • Review data ownership clauses for adequacy<br>• Validate data removal and return procedures<br>• Oversee data destruction verification |
| Legal Counsel | • Draft enforceable data ownership language<br>• Review contract terms for legal compliance<br>• Handle data ownership disputes |

## 4. RULES
[RULE-01] All acquisition contracts where contractors access organizational data MUST include explicit data ownership clauses stating the organization retains full ownership of all data.
[VALIDATION] IF contract_involves_data_access = TRUE AND data_ownership_clause = FALSE THEN critical_violation

[RULE-02] Contracts MUST specify data removal timeframes not exceeding 30 days for standard contracts and 7 days for contracts involving sensitive data (PII, PHI, classified).
[VALIDATION] IF data_sensitivity = "sensitive" AND removal_timeframe > 7_days THEN violation
[VALIDATION] IF data_sensitivity = "standard" AND removal_timeframe > 30_days THEN violation

[RULE-03] Contractors MUST provide written certification of data removal and return within the contractually specified timeframe.
[VALIDATION] IF contract_end_date + removal_timeframe < current_date AND certification_received = FALSE THEN violation

[RULE-04] Contracts MUST require contractors to maintain data removal and return procedures that are auditable by the organization.
[VALIDATION] IF contract_data_access = TRUE AND auditable_procedures_required = FALSE THEN violation

[RULE-05] Data return requirements MUST specify acceptable formats and secure transmission methods for returning organizational data.
[VALIDATION] IF data_return_format_specified = FALSE OR secure_transmission_method_specified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Contract Data Ownership Review - Mandatory review of all contracts for data ownership provisions before execution
- [PROC-02] Data Removal Verification - Process to verify contractor compliance with data removal requirements
- [PROC-03] Data Return Validation - Procedure to validate completeness and integrity of returned organizational data
- [PROC-04] Contractor Data Audit - Regular auditing of contractor data handling and removal capabilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Contract disputes, data breaches, regulatory changes, failed data return certifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Service Contract Expiration]
IF contract_type = "cloud_service"
AND contract_status = "expired"
AND data_removal_timeframe = 30_days
AND days_since_expiration > 30
AND removal_certification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Sensitive Data Processing Contract]
IF contract_involves_pii = TRUE
AND data_removal_timeframe > 7_days
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Data Ownership Clause]
IF contractor_data_access = TRUE
AND data_ownership_clause_present = FALSE
AND contract_executed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Compliant Professional Services Contract]
IF contract_type = "professional_services"
AND data_ownership_clause_present = TRUE
AND data_removal_timeframe <= 30_days
AND auditable_procedures_required = TRUE
AND secure_return_method_specified = TRUE
THEN compliance = TRUE

[SCENARIO-05: Late Data Return Certification]
IF contract_end_date + removal_timeframe < current_date - 5_days
AND removal_certification_received = FALSE
AND contractor_notified = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Organizational data ownership requirements included in acquisition contract | [RULE-01] |
| All data removed from contractor system within defined timeframe | [RULE-02], [RULE-03] |
| Data returned to organization within defined timeframe | [RULE-03], [RULE-05] |
| Contractor procedures for data removal are auditable | [RULE-04] |