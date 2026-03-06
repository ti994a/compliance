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
All developers of systems, system components, or system services for organizational use MUST identify and document the specific functions, ports, protocols, and services intended for organizational use during the early stages of system development. This identification enables risk assessment and security design decisions before implementation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal system developers | YES | All internal development teams |
| External contractors/vendors | YES | All contracted development services |
| COTS/SaaS providers | YES | Must provide documentation during procurement |
| System integrators | YES | For custom integrations and configurations |
| Cloud service providers | CONDITIONAL | When developing custom solutions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Developers | • Document all functions, ports, protocols, and services<br>• Provide documentation during requirements and design phases<br>• Update documentation when changes occur |
| Procurement Manager | • Include identification requirements in contracts<br>• Verify compliance before acceptance<br>• Maintain vendor documentation |
| Security Architect | • Review identified functions, ports, protocols, and services<br>• Assess security risks and recommend mitigations<br>• Approve or reject based on risk assessment |

## 4. RULES
[RULE-01] Developers MUST identify and document all functions intended for organizational use during the requirements definition phase.
[VALIDATION] IF development_phase = "requirements" AND functions_documented = FALSE THEN violation

[RULE-02] Developers MUST identify and document all ports intended for organizational use during the design phase.
[VALIDATION] IF development_phase IN ["requirements", "design"] AND ports_documented = FALSE THEN violation

[RULE-03] Developers MUST identify and document all protocols intended for organizational use during the design phase.
[VALIDATION] IF development_phase IN ["requirements", "design"] AND protocols_documented = FALSE THEN violation

[RULE-04] Developers MUST identify and document all services intended for organizational use during the design phase.
[VALIDATION] IF development_phase IN ["requirements", "design"] AND services_documented = FALSE THEN violation

[RULE-05] All acquisition contracts MUST include requirements for developers to provide functions, ports, protocols, and services documentation.
[VALIDATION] IF contract_type = "development" AND identification_requirements = FALSE THEN violation

[RULE-06] Documentation updates MUST be provided within 15 business days when functions, ports, protocols, or services change.
[VALIDATION] IF change_date + 15_business_days < current_date AND documentation_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Documentation Requirements - Standard template and submission process for identification documentation
- [PROC-02] Security Review Process - Review and approval workflow for identified functions, ports, protocols, and services
- [PROC-03] Contract Language Standards - Standard contractual requirements for developer identification obligations
- [PROC-04] Change Management Process - Process for handling updates to identified components

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system acquisitions, significant security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Port Documentation]
IF system_type = "custom_development"
AND development_phase = "design"
AND ports_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Vendor Documentation]
IF vendor_type = "external"
AND contract_signed = TRUE
AND functions_documentation = "partial"
AND acceptance_date < current_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Late Documentation Update]
IF service_change_date = "2024-01-15"
AND current_date = "2024-02-10"
AND documentation_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Compliant Early Identification]
IF development_phase = "requirements"
AND functions_documented = TRUE
AND ports_documented = TRUE
AND protocols_documented = TRUE
AND services_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: COTS Provider Compliance]
IF provider_type = "COTS"
AND procurement_phase = "evaluation"
AND vendor_documentation_complete = TRUE
AND security_review_completed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer required to identify functions intended for organizational use | [RULE-01] |
| Developer required to identify ports intended for organizational use | [RULE-02] |
| Developer required to identify protocols intended for organizational use | [RULE-03] |
| Developer required to identify services intended for organizational use | [RULE-04] |