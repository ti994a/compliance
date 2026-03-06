```markdown
# POLICY: SA-17.2: Security-relevant Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-17.2 |
| NIST Control | SA-17.2: Security-relevant Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security-relevant, developer requirements, hardware, software, firmware, rationale, completeness |

## 1. POLICY STATEMENT
All system developers MUST define security-relevant hardware, software, and firmware components and provide complete rationale demonstrating the definitions are comprehensive. This requirement applies to all system development, component acquisition, and service procurement activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All custom system development |
| External Vendors/Contractors | YES | All contracted development work |
| COTS Software Vendors | YES | When security-relevant components exist |
| Cloud Service Providers | YES | For custom configurations and integrations |
| Third-party Integrators | YES | When modifying security-relevant components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve security-relevant component definitions<br>• Validate completeness rationale<br>• Enforce policy compliance |
| Procurement Manager | • Ensure contracts include security-relevant component requirements<br>• Verify vendor deliverable compliance<br>• Maintain vendor documentation |
| System Architect | • Review and validate security-relevant component definitions<br>• Assess completeness of developer rationale<br>• Approve architectural security decisions |
| Developer/Vendor | • Define all security-relevant hardware, software, firmware<br>• Provide comprehensive completeness rationale<br>• Maintain current documentation |

## 4. RULES
[RULE-01] Developers MUST define all security-relevant hardware components that maintain required security properties for confidentiality, integrity, or availability.
[VALIDATION] IF system_component = "hardware" AND security_function = TRUE AND definition_provided = FALSE THEN violation

[RULE-02] Developers MUST define all security-relevant software components that perform security functions or enforce security policies.
[VALIDATION] IF system_component = "software" AND security_function = TRUE AND definition_provided = FALSE THEN violation

[RULE-03] Developers MUST define all security-relevant firmware components that control system security behavior or maintain security properties.
[VALIDATION] IF system_component = "firmware" AND security_function = TRUE AND definition_provided = FALSE THEN violation

[RULE-04] Developers MUST provide written rationale demonstrating that security-relevant component definitions are complete and comprehensive.
[VALIDATION] IF component_definitions_provided = TRUE AND completeness_rationale = FALSE THEN violation

[RULE-05] Security-relevant component definitions and rationale MUST be delivered before system acceptance or deployment authorization.
[VALIDATION] IF system_status = "ready_for_deployment" AND (component_definitions = FALSE OR rationale_provided = FALSE) THEN critical_violation

[RULE-06] All procurement contracts MUST include requirements for security-relevant component definition and completeness rationale deliverables.
[VALIDATION] IF contract_type = "system_development" AND security_component_requirements = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security-Relevant Component Identification - Process for systematically identifying components with security functions
- [PROC-02] Completeness Rationale Review - Procedure for evaluating developer rationale adequacy
- [PROC-03] Contract Security Requirements - Standard language for procurement contracts
- [PROC-04] Vendor Deliverable Validation - Process for reviewing and accepting vendor documentation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Major system changes, new procurement types, security incidents involving undefined components

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Firmware Definition]
IF system_component = "firmware"
AND security_function = TRUE
AND component_definition = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Rationale]
IF component_definitions = "provided"
AND completeness_rationale = "partial"
AND security_gaps_identified = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Contract Missing Requirements]
IF procurement_contract = TRUE
AND system_type = "security_relevant"
AND component_definition_requirement = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: COTS Vendor Compliance]
IF vendor_type = "COTS"
AND security_relevant_components = TRUE
AND vendor_definitions_provided = TRUE
AND completeness_rationale = TRUE
THEN compliance = TRUE

[SCENARIO-05: Pre-deployment Validation]
IF system_status = "pre_deployment"
AND component_definitions = TRUE
AND rationale_reviewed = TRUE
AND architect_approved = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer defines security-relevant hardware | [RULE-01] |
| Developer defines security-relevant software | [RULE-02] |
| Developer defines security-relevant firmware | [RULE-03] |
| Developer provides completeness rationale | [RULE-04] |
| Deliverables completed before deployment | [RULE-05] |
| Contract requirements inclusion | [RULE-06] |
```