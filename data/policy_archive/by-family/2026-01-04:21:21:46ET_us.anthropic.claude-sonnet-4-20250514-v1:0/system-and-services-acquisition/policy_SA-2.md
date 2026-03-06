```markdown
# POLICY: SA-2: Allocation of Resources

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-2 |
| NIST Control | SA-2: Allocation of Resources |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | resource allocation, budgeting, capital planning, security requirements, privacy requirements, funding |

## 1. POLICY STATEMENT
The organization must determine high-level information security and privacy requirements during mission and business process planning, allocate appropriate resources through capital planning processes, and establish discrete budget line items for information security and privacy investments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Systems | YES | Including cloud, on-premises, and hybrid |
| System Services | YES | Internal and external services |
| Capital Planning Process | YES | All technology investments >$100K |
| Budget Documentation | YES | Annual and multi-year budgets |
| Supply Chain Activities | YES | Security-related procurement |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve security resource allocation strategies<br>• Review budget adequacy for security requirements<br>• Validate security line item justifications |
| Privacy Officer | • Determine privacy resource requirements<br>• Approve privacy budget allocations<br>• Validate privacy line item justifications |
| Capital Planning Board | • Review and approve security/privacy resource requests<br>• Ensure adequate funding allocation<br>• Document resource allocation decisions |
| System Owners | • Identify system-specific security/privacy requirements<br>• Justify resource needs during planning<br>• Submit accurate budget requests |

## 4. RULES

[RULE-01] High-level information security requirements MUST be determined and documented during mission and business process planning for all systems and services.
[VALIDATION] IF system_planning_initiated = TRUE AND security_requirements_documented = FALSE THEN violation

[RULE-02] High-level privacy requirements MUST be determined and documented during mission and business process planning for all systems processing PII.
[VALIDATION] IF system_processes_pii = TRUE AND privacy_requirements_documented = FALSE THEN violation

[RULE-03] Required security and privacy resources MUST be determined, documented, and allocated through the organizational capital planning and investment control process.
[VALIDATION] IF system_investment > 100000 AND (security_resources_documented = FALSE OR privacy_resources_documented = FALSE) THEN violation

[RULE-04] Discrete line items for information security MUST be established in all organizational programming and budgeting documentation.
[VALIDATION] IF budget_document_exists = TRUE AND security_line_item_exists = FALSE THEN violation

[RULE-05] Discrete line items for privacy MUST be established in organizational programming and budgeting documentation for systems processing PII.
[VALIDATION] IF budget_document_exists = TRUE AND processes_pii = TRUE AND privacy_line_item_exists = FALSE THEN violation

[RULE-06] Security and privacy resource allocation MUST include funding for acquisition, sustainment, and supply chain risk management throughout the system development lifecycle.
[VALIDATION] IF resource_allocation_complete = TRUE AND (acquisition_funding = FALSE OR sustainment_funding = FALSE OR supply_chain_funding = FALSE) THEN violation

[RULE-07] Resource allocation decisions MUST be reviewed and approved by the Capital Planning Board within 30 days of submission.
[VALIDATION] IF resource_request_submitted = TRUE AND approval_time > 30_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Requirements Determination - Process for identifying security requirements during planning
- [PROC-02] Privacy Requirements Assessment - Process for determining privacy resource needs
- [PROC-03] Capital Planning Integration - Procedure for incorporating security/privacy into capital planning
- [PROC-04] Budget Line Item Creation - Process for establishing discrete security/privacy budget items
- [PROC-05] Resource Allocation Review - Procedure for reviewing and approving resource requests

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system acquisitions, budget cycle changes, regulatory updates, significant security incidents

## 7. SCENARIO PATTERNS

[SCENARIO-01: New System Without Security Requirements]
IF new_system_planning = TRUE
AND security_requirements_documented = FALSE
AND planning_phase_complete = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Budget Without Security Line Items]
IF annual_budget_submitted = TRUE
AND security_line_item_exists = FALSE
AND organization_has_systems = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: PII System Without Privacy Resources]
IF system_processes_pii = TRUE
AND privacy_resources_allocated = FALSE
AND system_in_production = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Adequate Resource Allocation]
IF security_requirements_documented = TRUE
AND privacy_requirements_documented = TRUE
AND resources_allocated = TRUE
AND budget_line_items_exist = TRUE
THEN compliance = TRUE

[SCENARIO-05: Supply Chain Funding Gap]
IF system_acquisition_planned = TRUE
AND supply_chain_risks_identified = TRUE
AND supply_chain_funding_allocated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| High-level security requirements determined in planning | [RULE-01] |
| High-level privacy requirements determined in planning | [RULE-02] |
| Resources determined and documented in capital planning | [RULE-03] |
| Resources allocated through capital planning process | [RULE-03] |
| Discrete security line item in budget documentation | [RULE-04] |
| Discrete privacy line item in budget documentation | [RULE-05] |
```