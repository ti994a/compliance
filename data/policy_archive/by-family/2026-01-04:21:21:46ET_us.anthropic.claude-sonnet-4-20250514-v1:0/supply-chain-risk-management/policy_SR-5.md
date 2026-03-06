```markdown
# POLICY: SR-5: Acquisition Strategies, Tools, and Methods

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-5 |
| NIST Control | SR-5: Acquisition Strategies, Tools, and Methods |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | supply chain, acquisition, procurement, contracts, vendor management, risk mitigation |

## 1. POLICY STATEMENT
The organization SHALL employ defined acquisition strategies, contract tools, and procurement methods to protect against, identify, and mitigate supply chain risks throughout the procurement lifecycle. All acquisitions of systems, components, and services MUST incorporate supply chain risk management controls appropriate to the classification and criticality of the asset.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All procurement activities | YES | Hardware, software, services |
| Third-party vendors | YES | All tiers of suppliers |
| Internal development | CONDITIONAL | When using external components |
| Emergency purchases | YES | Expedited risk assessment required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Procurement Officer | • Define acquisition strategies and contract requirements<br>• Approve high-risk procurements<br>• Maintain approved vendor lists |
| Supply Chain Risk Manager | • Conduct supply chain risk assessments<br>• Define risk mitigation strategies<br>• Monitor vendor compliance |
| Procurement Teams | • Implement acquisition controls<br>• Execute contract requirements<br>• Document procurement decisions |

## 4. RULES

[RULE-01] All procurements above $50,000 or involving critical systems MUST undergo supply chain risk assessment before contract award.
[VALIDATION] IF procurement_value > 50000 OR system_criticality = "high" AND risk_assessment_completed = FALSE THEN violation

[RULE-02] Contracts MUST include clauses prohibiting counterfeit components, requiring tamper-evident packaging, and mandating supply chain transparency for critical acquisitions.
[VALIDATION] IF system_criticality IN ["high", "critical"] AND contract_clauses_complete = FALSE THEN violation

[RULE-03] Organizations SHALL maintain an approved vendor list based on supply chain risk assessments and vendor security posture evaluations.
[VALIDATION] IF vendor_approval_status = "unapproved" AND procurement_initiated = TRUE THEN violation

[RULE-04] Procurement methods MUST employ risk mitigation strategies including blind buys, trusted distribution, or end-use obfuscation for high-risk acquisitions.
[VALIDATION] IF supply_chain_risk_level = "high" AND mitigation_strategy_implemented = FALSE THEN violation

[RULE-05] All procurement personnel MUST complete annual supply chain risk management training and awareness programs.
[VALIDATION] IF personnel_role = "procurement" AND training_completion_date < (current_date - 365_days) THEN violation

[RULE-06] Development plans, documentation, and evidence MUST be protected commensurate with the security requirements of the system being acquired.
[VALIDATION] IF documentation_protection_level < system_security_level THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment - Evaluate vendor and component risks before procurement
- [PROC-02] Vendor Approval Process - Establish and maintain approved vendor listings
- [PROC-03] Contract Security Requirements - Define mandatory security clauses for contracts
- [PROC-04] Procurement Risk Mitigation - Implement appropriate risk reduction strategies
- [PROC-05] Personnel Training Program - Deliver supply chain awareness training

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major supply chain incidents, regulatory changes, significant vendor changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Critical System Procurement]
IF system_criticality = "critical"
AND procurement_value > 100000
AND supply_chain_assessment = "completed"
AND contract_security_clauses = "included"
THEN compliance = TRUE

[SCENARIO-02: Unapproved Vendor Usage]
IF vendor_approval_status = "unapproved"
AND procurement_initiated = TRUE
AND emergency_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Risk Assessment]
IF procurement_value > 50000
AND risk_assessment_completed = FALSE
AND contract_signed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Inadequate Contract Protections]
IF system_criticality IN ["high", "critical"]
AND counterfeit_protection_clause = FALSE
AND tamper_evident_requirement = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Training Compliance]
IF personnel_role = "procurement"
AND training_completion_date < (current_date - 365_days)
AND active_procurement_activities = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Acquisition strategies defined and employed to protect against supply chain risks | RULE-01, RULE-04 |
| Acquisition strategies defined and employed to identify supply chain risks | RULE-01, RULE-03 |
| Acquisition strategies defined and employed to mitigate supply chain risks | RULE-02, RULE-04, RULE-06 |
```