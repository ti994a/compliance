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
All acquisition contracts involving organizational data MUST include explicit data ownership requirements and mandatory data removal/return provisions. Contractors SHALL remove all organizational data from their systems and return it to the organization within contractually defined timeframes upon contract termination or expiration.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All acquisition contracts | YES | When contractor handles organizational data |
| Cloud service providers | YES | Including SaaS, PaaS, IaaS arrangements |
| Software development contractors | YES | When accessing or processing organizational data |
| Consulting services | YES | When data access is required |
| Hardware maintenance contracts | CONDITIONAL | Only if data access is involved |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Ensure all contracts include data ownership clauses<br>• Define standard data removal timeframes<br>• Approve contract data ownership terms |
| Contract Manager | • Monitor contractor compliance with data removal requirements<br>• Verify data return completion<br>• Document data removal validation |
| Data Owner | • Classify data sensitivity levels<br>• Define data handling requirements<br>• Validate completeness of returned data |

## 4. RULES
[RULE-01] All acquisition contracts involving organizational data MUST include explicit data ownership clauses stating the organization retains full ownership of all data.
[VALIDATION] IF contract_involves_org_data = TRUE AND data_ownership_clause = FALSE THEN critical_violation

[RULE-02] Contracts MUST specify data removal timeframes: 30 days for standard contracts, 7 days for sensitive data contracts, and 24 hours for classified data contracts.
[VALIDATION] IF data_classification = "classified" AND removal_timeframe > 24_hours THEN critical_violation

[RULE-03] Contractors MUST provide written certification of complete data removal and return within the specified timeframe.
[VALIDATION] IF contract_end_date + removal_timeframe < current_date AND removal_certification = FALSE THEN violation

[RULE-04] Data return MUST include all organizational data, metadata, backups, and copies in the original or agreed-upon format.
[VALIDATION] IF data_returned = TRUE AND (backups_removed = FALSE OR metadata_removed = FALSE) THEN violation

[RULE-05] Contracts MUST include penalties for non-compliance with data ownership and removal requirements.
[VALIDATION] IF contract_includes_data_clauses = TRUE AND penalty_clauses = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Contract Data Ownership Review - Standard review process for all contracts involving organizational data
- [PROC-02] Data Removal Verification - Process to validate contractor compliance with data removal requirements
- [PROC-03] Data Return Validation - Procedure to verify completeness and integrity of returned organizational data

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Contract breaches, regulatory changes, data incidents involving contractors

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Contract Expiration]
IF contract_status = "expired"
AND contract_involves_org_data = TRUE
AND days_since_expiration > 30
AND data_removal_certified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Sensitive Data Contract Termination]
IF contract_terminated = TRUE
AND data_classification = "sensitive"
AND days_since_termination > 7
AND data_return_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Incomplete Data Return]
IF data_return_completed = TRUE
AND (backups_confirmed_removed = FALSE OR metadata_returned = FALSE)
AND contractor_certification = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Contract Clauses]
IF new_contract = TRUE
AND contractor_data_access = TRUE
AND data_ownership_clauses = FALSE
AND contract_signed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compliant Data Handling]
IF contract_includes_data_ownership = TRUE
AND removal_timeframe_defined = TRUE
AND penalty_clauses_included = TRUE
AND contractor_acknowledged = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Organizational data ownership requirements included in acquisition contract | [RULE-01], [RULE-05] |
| All data removed from contractor system and returned within defined timeframe | [RULE-02], [RULE-03], [RULE-04] |