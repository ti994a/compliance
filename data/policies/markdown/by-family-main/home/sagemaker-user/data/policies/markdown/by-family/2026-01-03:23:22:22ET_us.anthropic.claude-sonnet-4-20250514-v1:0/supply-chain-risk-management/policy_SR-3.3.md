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
All security and supply chain risk management controls required in prime contractor agreements MUST be flowed down to subcontractor agreements at all supply chain tiers. Organizations SHALL ensure prime contractors implement processes to enforce control flow down to sub-tier contractors.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Prime contractors | YES | All Tier 1 contractors with system/service agreements |
| Subcontractors | YES | All sub-tier contractors in supply chain |
| Procurement teams | YES | Contract development and management |
| Internal IT services | NO | Covered under separate internal controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Establish flow down requirements in master contract templates<br>• Review and approve contract flow down procedures<br>• Monitor compliance across supply chain tiers |
| Contract Managers | • Verify flow down clauses in all contractor agreements<br>• Validate subcontractor compliance documentation<br>• Escalate flow down violations |
| Supply Chain Risk Manager | • Define controls subject to flow down requirements<br>• Assess sub-tier risk management effectiveness<br>• Review flow down compliance reports |

## 4. RULES
[RULE-01] Prime contractor agreements MUST include explicit requirements for flowing down all SR-3b identified controls to subcontractor agreements.
[VALIDATION] IF contract_type = "prime" AND flowdown_clause_present = FALSE THEN violation

[RULE-02] Prime contractors MUST provide documented evidence that required controls have been included in all subcontractor agreements within 30 days of subcontractor engagement.
[VALIDATION] IF subcontractor_engaged = TRUE AND evidence_provided = FALSE AND days_elapsed > 30 THEN violation

[RULE-03] Subcontractor agreements SHALL include the same security controls specified in the prime contractor agreement without modification or reduction in scope.
[VALIDATION] IF subcontractor_controls != prime_contractor_controls THEN critical_violation

[RULE-04] Prime contractors MUST maintain current documentation of all sub-tier contractors and their applicable control requirements.
[VALIDATION] IF subtier_documentation_age > 90_days OR subtier_list_incomplete = TRUE THEN violation

[RULE-05] Organizations SHALL conduct annual reviews to verify control flow down compliance across all supply chain tiers.
[VALIDATION] IF annual_flowdown_review_completed = FALSE AND review_due_date < current_date THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Contract Template Management - Maintain standardized flow down clauses for all contract types
- [PROC-02] Subcontractor Verification - Process for validating sub-tier control implementation
- [PROC-03] Flow Down Compliance Monitoring - Quarterly assessment of contractor flow down effectiveness
- [PROC-04] Non-Compliance Remediation - Escalation and correction procedures for flow down failures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: New regulatory requirements, supply chain incidents, contract template changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Flow Down Clause]
IF contract_type = "prime_contractor"
AND security_controls_specified = TRUE
AND flowdown_clause_present = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Subcontractor Controls]
IF subcontractor_agreement_exists = TRUE
AND prime_contract_controls = 15
AND subcontractor_contract_controls = 12
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Undocumented Sub-tier Contractors]
IF prime_contractor_has_subcontractors = TRUE
AND subtier_documentation_provided = FALSE
AND contract_execution_date > 30_days_ago
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Compliant Flow Down Implementation]
IF prime_contract_controls = subcontractor_controls
AND flowdown_documentation_current = TRUE
AND annual_review_completed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Delayed Evidence Submission]
IF subcontractor_engaged_date + 30_days < current_date
AND flowdown_evidence_submitted = FALSE
AND no_approved_extension = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls included in prime contractor contracts are flowed down to subcontractors | [RULE-01], [RULE-03] |
| Prime contractors implement flow down processes | [RULE-02], [RULE-04] |
| Sub-tier control implementation verification | [RULE-02], [RULE-05] |
| Documentation of sub-tier contractor relationships | [RULE-04] |