# POLICY: SR-3.3: Sub-tier Flow Down

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-3.3 |
| NIST Control | SR-3.3: Sub-tier Flow Down |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | supply chain, subcontractors, flow down, prime contractors, contract controls |

## 1. POLICY STATEMENT
All supply chain risk management controls required in prime contractor agreements MUST be flowed down to subcontractor agreements at all tiers. Organizations SHALL ensure prime contractors implement processes to cascade security controls through the entire supply chain hierarchy.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Prime Contractors | YES | All Tier 1 contractors |
| Subcontractors | YES | All sub-tier contractors |
| Procurement Teams | YES | Contract management responsibilities |
| Third-party Services | YES | When part of supply chain |
| Internal Development | NO | Not applicable to internal teams |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Establish flow down requirements<br>• Approve contract templates<br>• Monitor compliance across tiers |
| Contract Managers | • Verify flow down clauses in contracts<br>• Validate subcontractor compliance<br>• Report flow down violations |
| Supply Chain Risk Manager | • Define controls requiring flow down<br>• Assess sub-tier risk exposure<br>• Monitor supply chain compliance |

## 4. RULES
[RULE-01] Prime contractor agreements MUST include explicit requirements to flow down all SR-3b identified controls to subcontractors.
[VALIDATION] IF contract_type = "prime" AND flowdown_clause = FALSE THEN critical_violation

[RULE-02] Prime contractors MUST provide evidence of subcontractor contract compliance within 30 days of subcontractor engagement.
[VALIDATION] IF subcontractor_engaged = TRUE AND evidence_provided_days > 30 THEN violation

[RULE-03] Subcontractor agreements SHALL include the same security controls as specified in the prime contract without dilution.
[VALIDATION] IF prime_controls != subcontractor_controls THEN violation

[RULE-04] Organizations MUST maintain visibility into sub-tier contractor relationships through prime contractor reporting.
[VALIDATION] IF subtier_contractors > 0 AND visibility_reports = FALSE THEN violation

[RULE-05] Flow down requirements SHALL extend to all tiers of the supply chain without limitation.
[VALIDATION] IF contract_tier > 1 AND flowdown_required = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Contract Template Management - Maintain standardized flow down clauses
- [PROC-02] Subcontractor Verification - Validate control implementation at sub-tiers
- [PROC-03] Supply Chain Mapping - Document multi-tier contractor relationships
- [PROC-04] Compliance Monitoring - Regular assessment of flow down effectiveness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Contract renewals, supply chain incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Flow Down Clause]
IF contract_type = "prime"
AND security_controls_required = TRUE
AND flowdown_clause_present = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Diluted Subcontractor Controls]
IF prime_contract_controls = 15
AND subcontractor_controls = 10
AND justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Undisclosed Sub-tier Contractor]
IF subcontractor_tier > 2
AND organization_visibility = FALSE
AND prime_contractor_reporting = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Compliant Multi-tier Flow Down]
IF prime_contract_flowdown = TRUE
AND subtier_contracts_verified = TRUE
AND control_consistency = TRUE
THEN compliance = TRUE

[SCENARIO-05: Late Compliance Evidence]
IF subcontractor_engagement_date = "2024-01-01"
AND compliance_evidence_date = "2024-02-15"
AND days_difference > 30
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls included in prime contractor contracts are flowed to subcontractors | [RULE-01], [RULE-03] |
| Prime contractor flow down processes implemented | [RULE-02], [RULE-04] |
| Multi-tier supply chain coverage | [RULE-05] |