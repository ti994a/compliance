# POLICY: SA-17.2: Security-relevant Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-17.2 |
| NIST Control | SA-17.2: Security-relevant Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security-relevant, developer requirements, hardware definition, software definition, firmware definition, completeness rationale |

## 1. POLICY STATEMENT
All system developers MUST define security-relevant hardware, software, and firmware components and provide complete rationale demonstrating the definitions encompass all trusted components required to maintain security properties. This policy ensures critical security components are properly identified and documented during system acquisition and development.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Developers | YES | All contracted and internal developers |
| System Components | YES | Hardware, software, firmware requiring security properties |
| System Services | YES | External services integrated with company systems |
| Legacy Systems | CONDITIONAL | During major updates or security reviews |
| Development Tools | CONDITIONAL | When they affect production security properties |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Developer | • Define all security-relevant components<br>• Provide completeness rationale<br>• Document component security properties<br>• Update definitions when components change |
| Security Architect | • Review component definitions for completeness<br>• Validate security property requirements<br>• Approve completeness rationale |
| Procurement Manager | • Include requirements in acquisition contracts<br>• Verify deliverable compliance<br>• Manage developer obligations |

## 4. RULES
[RULE-01] Developers MUST define all security-relevant hardware components that are trusted to maintain confidentiality, integrity, or availability properties.
[VALIDATION] IF security_relevant_hardware_defined = FALSE THEN violation

[RULE-02] Developers MUST define all security-relevant software components that perform security functions or handle sensitive data.
[VALIDATION] IF security_relevant_software_defined = FALSE THEN violation

[RULE-03] Developers MUST define all security-relevant firmware components that control system security behavior or protect system resources.
[VALIDATION] IF security_relevant_firmware_defined = FALSE THEN violation

[RULE-04] Developers MUST provide written rationale demonstrating their component definitions are complete and include all security-relevant elements.
[VALIDATION] IF completeness_rationale_provided = FALSE THEN violation

[RULE-05] Component definitions MUST be updated within 30 days when security-relevant components are added, modified, or removed.
[VALIDATION] IF component_change_date > (definition_update_date + 30_days) THEN violation

[RULE-06] All acquisition contracts MUST include requirements for security-relevant component definition and completeness rationale as mandatory deliverables.
[VALIDATION] IF contract_type = "system_development" AND sa_17_2_requirements = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security-Relevant Component Identification - Process for systematically identifying components requiring security properties
- [PROC-02] Completeness Rationale Development - Methodology for demonstrating definition completeness
- [PROC-03] Component Definition Review - Security architect review and approval process
- [PROC-04] Contract Requirements Integration - Including SA-17.2 requirements in procurement documents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system acquisitions, security incidents involving undefined components, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Complete Component Definition]
IF hardware_components_defined = TRUE
AND software_components_defined = TRUE
AND firmware_components_defined = TRUE
AND completeness_rationale_provided = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Firmware Definition]
IF hardware_components_defined = TRUE
AND software_components_defined = TRUE
AND firmware_components_defined = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Incomplete Rationale]
IF all_components_defined = TRUE
AND completeness_rationale_provided = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Contract Missing Requirements]
IF contract_type = "system_development"
AND sa_17_2_deliverables_required = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Outdated Component Definitions]
IF component_last_changed < (current_date - 30_days)
AND definition_last_updated < component_last_changed
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer required to define security-relevant hardware | [RULE-01] |
| Developer required to define security-relevant software | [RULE-02] |
| Developer required to define security-relevant firmware | [RULE-03] |
| Developer required to provide completeness rationale | [RULE-04] |