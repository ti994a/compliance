# POLICY: SR-3.3: Sub-tier Flow Down

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-3.3 |
| NIST Control | SR-3.3: Sub-tier Flow Down |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | supply chain, subcontractor, flow down, prime contractor, contract controls |

## 1. POLICY STATEMENT
All supply chain risk management controls required in prime contractor agreements MUST be flowed down to subcontractor agreements at all tiers. Organizations SHALL ensure prime contractors implement processes to facilitate control flow down to sub-tier contractors.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Prime contractors | YES | All Tier 1 contractors with subcontractors |
| Subcontractors | YES | All sub-tier contractors (Tier 2+) |
| Internal procurement teams | YES | Contract oversight responsibility |
| System integrators | YES | When acting as prime or subcontractor |
| Cloud service providers | CONDITIONAL | When using sub-processors |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Establish flow down requirements in procurement policies<br>• Approve contract templates with flow down clauses<br>• Oversee compliance monitoring |
| Contract Managers | • Verify flow down clauses in all prime contracts<br>• Monitor subcontractor compliance reporting<br>• Escalate non-compliance issues |
| Prime Contractors | • Flow down specified controls to all subcontractors<br>• Monitor subcontractor compliance<br>• Report compliance status to organization |

## 4. RULES
[RULE-01] Prime contractor agreements MUST include explicit requirements to flow down all SR-3b identified controls to subcontractors.
[VALIDATION] IF contract_type = "prime" AND flowdown_clause_present = FALSE THEN violation

[RULE-02] Prime contractors MUST provide evidence of control flow down to subcontractors within 30 days of subcontract execution.
[VALIDATION] IF subcontract_executed = TRUE AND evidence_provided = FALSE AND days_elapsed > 30 THEN violation

[RULE-03] Subcontractor agreements MUST contain the same security controls as specified in the prime contract.
[VALIDATION] IF prime_controls NOT subset_of subcontractor_controls THEN violation

[RULE-04] Prime contractors SHALL establish processes to monitor subcontractor compliance with flowed-down controls.
[VALIDATION] IF monitoring_process_documented = FALSE OR monitoring_frequency = NULL THEN violation

[RULE-05] Organizations MUST verify flow down implementation before accepting deliverables from prime contractors with subcontractors.
[VALIDATION] IF deliverable_acceptance = TRUE AND flowdown_verification = FALSE AND subcontractors_present = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Contract Flow Down Verification - Process to verify controls are included in subcontractor agreements
- [PROC-02] Subcontractor Compliance Monitoring - Ongoing monitoring of sub-tier compliance
- [PROC-03] Flow Down Exception Management - Process for handling flow down exceptions or waivers
- [PROC-04] Prime Contractor Reporting - Regular reporting requirements for subcontractor compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New major contracts, supply chain incidents, regulatory changes, failed compliance audits

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Flow Down Clause]
IF contract_type = "prime"
AND subcontractors_involved = TRUE
AND flowdown_clause_present = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Control Flow Down]
IF prime_contract_controls = 15
AND subcontractor_contract_controls = 12
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Cloud Provider Sub-processors]
IF service_type = "cloud"
AND sub_processors_used = TRUE
AND sub_processor_agreements_compliant = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Delayed Flow Down Evidence]
IF subcontract_execution_date < (current_date - 30_days)
AND flowdown_evidence_provided = FALSE
AND prime_contractor_responsive = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Verified Flow Down Implementation]
IF flowdown_clause_present = TRUE
AND subcontractor_controls_verified = TRUE
AND monitoring_process_active = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls included in prime contracts are flowed to subcontractors | [RULE-01], [RULE-03] |
| Prime contractor flow down processes established | [RULE-04] |
| Flow down implementation verification | [RULE-02], [RULE-05] |
| Sub-tier contractor compliance monitoring | [RULE-04] |