# POLICY: SA-4.12: Data Ownership

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.12 |
| NIST Control | SA-4.12: Data Ownership |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | data ownership, contractor data, acquisition contracts, data return, data removal |

## 1. POLICY STATEMENT
All acquisition contracts involving organizational data MUST include explicit data ownership requirements and mandatory data return/removal provisions. Contractors SHALL remove all organizational data from their systems and return it to the organization within contractually defined timeframes upon contract termination or expiration.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All acquisition contracts | YES | Where contractor processes organizational data |
| Software-as-a-Service contracts | YES | Including cloud service providers |
| Professional services contracts | YES | Where contractor accesses organizational systems |
| Hardware procurement | CONDITIONAL | Only if data storage/processing involved |
| Internal IT services | NO | Covered under separate policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Ensure all contracts include data ownership clauses<br>• Approve data return timeframes<br>• Monitor contractor compliance |
| Contract Manager | • Include required data ownership language in contracts<br>• Verify contractor data handling procedures<br>• Execute data return processes |
| Data Owner | • Define data classification and handling requirements<br>• Validate completeness of returned data<br>• Approve data destruction certification |

## 4. RULES
[RULE-01] All acquisition contracts involving organizational data MUST include explicit data ownership clauses stating the organization retains full ownership of all data.
[VALIDATION] IF contract_involves_org_data = TRUE AND data_ownership_clause = FALSE THEN violation

[RULE-02] Contracts MUST specify data return timeframes not exceeding 30 days for standard terminations and 72 hours for emergency terminations.
[VALIDATION] IF data_return_timeframe > 30_days AND termination_type = "standard" THEN violation
[VALIDATION] IF data_return_timeframe > 72_hours AND termination_type = "emergency" THEN critical_violation

[RULE-03] Contractors MUST provide written certification of complete data removal within 5 business days of data return completion.
[VALIDATION] IF data_returned = TRUE AND removal_certification_received = FALSE AND days_elapsed > 5 THEN violation

[RULE-04] Contracts MUST require contractors to maintain detailed data inventory logs throughout the contract period.
[VALIDATION] IF contract_involves_org_data = TRUE AND data_inventory_requirement = FALSE THEN violation

[RULE-05] Data return procedures MUST include verification mechanisms to ensure completeness and integrity of returned data.
[VALIDATION] IF data_return_completed = TRUE AND verification_performed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Contract Data Ownership Review - Mandatory review of all contracts for data ownership compliance
- [PROC-02] Contractor Data Inventory Management - Process for maintaining and auditing contractor data inventories
- [PROC-03] Data Return Verification - Procedures for validating completeness of returned organizational data
- [PROC-04] Emergency Data Recovery - Expedited processes for critical data return situations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Contract breaches, data incidents, regulatory changes, failed audits

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Contract Termination]
IF contract_status = "terminated"
AND termination_type = "standard"
AND data_return_timeframe <= 30_days
AND removal_certification_received = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Data Ownership Clause]
IF contract_involves_org_data = TRUE
AND data_ownership_clause = FALSE
AND contract_signed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Data Return]
IF contract_terminated = TRUE
AND days_since_termination > contractual_timeframe
AND data_returned = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Return Verification]
IF data_return_completed = TRUE
AND verification_performed = FALSE
AND days_elapsed > 5
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Termination Compliance]
IF termination_type = "emergency"
AND data_return_timeframe <= 72_hours
AND removal_certification_received = TRUE
AND verification_completed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Organizational data ownership requirements included in acquisition contract | [RULE-01] |
| All data removed from contractor system and returned within defined timeframe | [RULE-02], [RULE-03] |
| Data inventory and tracking requirements | [RULE-04] |
| Verification of data return completeness | [RULE-05] |