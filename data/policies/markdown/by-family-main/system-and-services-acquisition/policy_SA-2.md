# POLICY: SA-2: Allocation of Resources

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-2 |
| NIST Control | SA-2: Allocation of Resources |
| Version | 1.0 |
| Owner | Chief Financial Officer |
| Keywords | resource allocation, budgeting, capital planning, security requirements, privacy requirements, funding |

## 1. POLICY STATEMENT
The organization SHALL determine high-level information security and privacy requirements during mission and business process planning, allocate appropriate resources through capital planning and investment control processes, and establish discrete budget line items for security and privacy investments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and hybrid systems |
| System services | YES | Both internal and external services |
| Capital planning processes | YES | All IT investment decisions |
| Budget documentation | YES | Annual and multi-year budgets |
| Mission planning activities | YES | Business process planning included |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Financial Officer | • Oversee capital planning and investment control process<br>• Ensure discrete security/privacy budget line items<br>• Approve resource allocation decisions |
| CISO/Privacy Officer | • Determine high-level security and privacy requirements<br>• Document resource needs for protection measures<br>• Validate adequacy of allocated resources |
| Business Process Owners | • Integrate security/privacy requirements into mission planning<br>• Justify resource requirements for their systems<br>• Participate in capital planning process |

## 4. RULES
[RULE-01] High-level information security requirements MUST be determined and documented during mission and business process planning for all systems and services.
[VALIDATION] IF system_planning_initiated = TRUE AND security_requirements_documented = FALSE THEN violation

[RULE-02] High-level privacy requirements MUST be determined and documented during mission and business process planning for all systems and services that process PII.
[VALIDATION] IF system_processes_pii = TRUE AND privacy_requirements_documented = FALSE THEN violation

[RULE-03] Resources required to protect systems and services MUST be determined, documented, and allocated through the organizational capital planning and investment control process.
[VALIDATION] IF system_approved = TRUE AND (protection_resources_determined = FALSE OR protection_resources_documented = FALSE OR protection_resources_allocated = FALSE) THEN violation

[RULE-04] A discrete line item for information security MUST be established in all organizational programming and budgeting documentation.
[VALIDATION] IF budget_documentation_exists = TRUE AND security_line_item_exists = FALSE THEN violation

[RULE-05] A discrete line item for privacy MUST be established in organizational programming and budgeting documentation for systems processing PII.
[VALIDATION] IF organization_processes_pii = TRUE AND privacy_line_item_exists = FALSE THEN violation

[RULE-06] Resource allocation MUST include funding for system acquisition, sustainment, and supply chain risk management throughout the system development lifecycle.
[VALIDATION] IF system_lifecycle_stage IN ["acquisition", "sustainment", "disposal"] AND supply_chain_funding_allocated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Requirements Determination - Process for identifying and documenting high-level security requirements during planning
- [PROC-02] Privacy Requirements Determination - Process for identifying and documenting privacy requirements for PII-processing systems
- [PROC-03] Capital Planning Integration - Procedure for incorporating security/privacy resource needs into capital planning
- [PROC-04] Budget Line Item Management - Process for establishing and maintaining discrete security/privacy budget categories
- [PROC-05] Resource Adequacy Assessment - Annual review of allocated resources against protection requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major organizational changes, significant budget modifications, new regulatory requirements, security incidents affecting resource planning

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Without Security Requirements]
IF new_system_planning = TRUE
AND security_requirements_documented = FALSE
AND system_approval_pending = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Privacy Budget Line Item]
IF organization_processes_pii = TRUE
AND annual_budget_approved = TRUE
AND privacy_line_item_exists = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Inadequate Supply Chain Funding]
IF system_acquisition_approved = TRUE
AND supply_chain_risks_identified = TRUE
AND supply_chain_funding_allocated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Complete Compliance Example]
IF security_requirements_documented = TRUE
AND privacy_requirements_documented = TRUE
AND resources_allocated_via_capital_planning = TRUE
AND security_line_item_exists = TRUE
AND privacy_line_item_exists = TRUE
THEN compliance = TRUE

[SCENARIO-05: Legacy System Resource Review]
IF system_age > 3_years
AND last_resource_review > 1_year
AND protection_requirements_changed = TRUE
THEN compliance_review_required = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| High-level information security requirements determined in mission planning | [RULE-01] |
| High-level privacy requirements determined in mission planning | [RULE-02] |
| Resources determined and documented via capital planning | [RULE-03] |
| Resources allocated via capital planning | [RULE-03] |
| Discrete security line item in budget documentation | [RULE-04] |
| Discrete privacy line item in budget documentation | [RULE-05] |