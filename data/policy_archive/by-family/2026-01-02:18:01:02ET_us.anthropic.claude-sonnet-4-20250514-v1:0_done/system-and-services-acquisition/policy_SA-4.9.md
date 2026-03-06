# POLICY: SA-4.9: Functions, Ports, Protocols, and Services in Use

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.9 |
| NIST Control | SA-4.9: Functions, Ports, Protocols, and Services in Use |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer requirements, system acquisition, ports, protocols, services, functions, SDLC |

## 1. POLICY STATEMENT
All system developers, component suppliers, and service providers MUST identify and document the specific functions, ports, protocols, and services intended for organizational use during the early stages of system development. This identification MUST occur before system implementation to enable security risk assessment and design influence.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All custom applications and systems |
| External Vendors/Contractors | YES | All contracted development work |
| COTS Software Vendors | YES | Must provide documentation |
| Cloud Service Providers | YES | SaaS, PaaS, IaaS implementations |
| System Integrators | YES | Integration and customization work |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Ensure contracts include SA-4.9 requirements<br>• Verify developer compliance before acceptance<br>• Maintain vendor compliance documentation |
| System Owner | • Define organizational use requirements<br>• Review and approve developer-provided documentation<br>• Ensure ongoing compliance monitoring |
| Developer/Vendor | • Identify all functions, ports, protocols, services<br>• Document intended organizational use<br>• Provide updates when changes occur |

## 4. RULES
[RULE-01] Developers MUST identify and document all functions intended for organizational use during requirements definition phase.
[VALIDATION] IF development_phase = "requirements" AND functions_documented = FALSE THEN violation

[RULE-02] Developers MUST identify and document all network ports intended for organizational use before design completion.
[VALIDATION] IF development_phase <= "design" AND ports_documented = FALSE THEN violation

[RULE-03] Developers MUST identify and document all protocols intended for organizational use before design completion.
[VALIDATION] IF development_phase <= "design" AND protocols_documented = FALSE THEN violation

[RULE-04] Developers MUST identify and document all services intended for organizational use before design completion.
[VALIDATION] IF development_phase <= "design" AND services_documented = FALSE THEN violation

[RULE-05] All acquisition contracts MUST include explicit requirements for SA-4.9 compliance and deliverables.
[VALIDATION] IF contract_type = "development" AND sa49_requirements = FALSE THEN violation

[RULE-06] Developer documentation MUST be reviewed and approved by system owner before system implementation.
[VALIDATION] IF system_status = "pre-implementation" AND documentation_approved = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Documentation Review - Standardized process for evaluating completeness and accuracy
- [PROC-02] Contract Language Templates - Pre-approved SA-4.9 requirements for procurement
- [PROC-03] Change Management Process - Handling updates to functions, ports, protocols, services
- [PROC-04] Vendor Compliance Verification - Methods for validating developer submissions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Contract modifications, security incidents, regulatory changes, failed compliance assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Port Documentation]
IF development_contract = TRUE
AND system_phase = "design_complete"
AND ports_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Late Stage Identification]
IF system_phase = "implementation"
AND functions_identification_phase = "implementation"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incomplete Service Documentation]
IF vendor_type = "cloud_provider"
AND services_documented = "partial"
AND system_owner_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Contract Without Requirements]
IF contract_type = "system_development"
AND sa49_clause_included = FALSE
AND contract_status = "executed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Compliant Early Identification]
IF development_phase = "requirements"
AND functions_documented = TRUE
AND ports_documented = TRUE
AND protocols_documented = TRUE
AND services_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer identifies functions for organizational use | [RULE-01] |
| Developer identifies ports for organizational use | [RULE-02] |
| Developer identifies protocols for organizational use | [RULE-03] |
| Developer identifies services for organizational use | [RULE-04] |