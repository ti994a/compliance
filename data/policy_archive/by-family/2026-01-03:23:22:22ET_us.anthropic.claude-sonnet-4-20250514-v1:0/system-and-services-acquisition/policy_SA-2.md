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
The organization SHALL determine high-level information security and privacy requirements during mission and business process planning, allocate adequate resources through capital planning processes, and establish discrete budget line items for security and privacy investments throughout the system development lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| System Services | YES | Third-party and internal services |
| Capital Planning Process | YES | All IT investments and acquisitions |
| Mission Planning Activities | YES | Business process and mission planning |
| Budget Documentation | YES | Programming and budgeting processes |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Financial Officer | • Ensure discrete security/privacy budget line items<br>• Oversee capital planning integration<br>• Approve resource allocation decisions |
| CISO/Privacy Officer | • Define high-level security/privacy requirements<br>• Validate resource adequacy<br>• Review budget allocations |
| Business Process Owners | • Identify mission-critical security/privacy needs<br>• Participate in requirements determination<br>• Justify resource requests |

## 4. RULES
[RULE-01] High-level information security requirements MUST be determined and documented during mission and business process planning for all systems and services.
[VALIDATION] IF system_planning_initiated = TRUE AND security_requirements_documented = FALSE THEN violation

[RULE-02] High-level privacy requirements MUST be determined and documented during mission and business process planning for all systems and services that process PII.
[VALIDATION] IF system_processes_pii = TRUE AND privacy_requirements_documented = FALSE THEN violation

[RULE-03] Required security and privacy protection resources MUST be determined, documented, and allocated through the organizational capital planning and investment control process.
[VALIDATION] IF capital_planning_process = TRUE AND security_privacy_resources_allocated = FALSE THEN violation

[RULE-04] A discrete line item for information security MUST be established in organizational programming and budgeting documentation for each system or service.
[VALIDATION] IF budget_documentation_exists = TRUE AND security_line_item = FALSE THEN violation

[RULE-05] A discrete line item for privacy MUST be established in organizational programming and budgeting documentation for systems processing PII.
[VALIDATION] IF system_processes_pii = TRUE AND privacy_line_item = FALSE THEN violation

[RULE-06] Resource allocation MUST include funding for acquisition, sustainment, and supply chain risk management throughout the system development lifecycle.
[VALIDATION] IF lifecycle_phase IN ["acquisition", "sustainment", "supply_chain"] AND funding_allocated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Requirements Determination - Process for identifying high-level security needs during planning
- [PROC-02] Privacy Requirements Assessment - Methodology for determining privacy resource needs
- [PROC-03] Capital Planning Integration - Procedure for incorporating security/privacy into investment control
- [PROC-04] Budget Line Item Creation - Process for establishing discrete security/privacy budget items
- [PROC-05] Resource Adequacy Review - Annual assessment of allocated resources vs. requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when capital planning process changes
- Triggering events: Major system acquisitions, budget cycle changes, regulatory updates, significant security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Without Security Budget]
IF new_system_planned = TRUE
AND security_requirements_identified = TRUE
AND discrete_security_budget = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: PII System Missing Privacy Resources]
IF system_processes_pii = TRUE
AND privacy_requirements_documented = TRUE
AND privacy_budget_line_item = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Capital Planning Without Security Integration]
IF capital_planning_cycle = "active"
AND security_privacy_resources = "not_integrated"
AND investment_control_process = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Lifecycle Funding Gap]
IF system_lifecycle_phase = "sustainment"
AND security_funding_allocated = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compliant Resource Allocation]
IF security_requirements_documented = TRUE
AND privacy_requirements_documented = TRUE
AND capital_planning_integrated = TRUE
AND discrete_budget_items = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| High-level security requirements determined in planning | RULE-01 |
| High-level privacy requirements determined in planning | RULE-02 |
| Resources determined and documented in capital planning | RULE-03 |
| Resources allocated through capital planning process | RULE-03 |
| Discrete security line item in budget documentation | RULE-04 |
| Discrete privacy line item in budget documentation | RULE-05 |