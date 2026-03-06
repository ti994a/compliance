# POLICY: SA-17.2: Security-relevant Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-17.2 |
| NIST Control | SA-17.2: Security-relevant Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security-relevant, developer, hardware, software, firmware, rationale, completeness |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST define security-relevant hardware, software, and firmware components and provide complete rationale demonstrating the definition's completeness. This ensures trusted components maintaining required security properties are properly identified and justified.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Developers | YES | All internal and external developers |
| Component Vendors | YES | Third-party component providers |
| Service Providers | YES | External service providers |
| Internal Development Teams | YES | All internal software development |
| COTS Products | YES | Commercial off-the-shelf acquisitions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Developers | • Define security-relevant components<br>• Provide completeness rationale<br>• Maintain component documentation |
| Procurement Team | • Enforce requirements in contracts<br>• Validate developer submissions<br>• Review completeness rationale |
| Security Architecture Team | • Review component definitions<br>• Validate security relevance<br>• Approve rationale documentation |

## 4. RULES
[RULE-01] Developers MUST define all security-relevant hardware components that are trusted to maintain required security properties.
[VALIDATION] IF system_has_hardware = TRUE AND security_relevant_hardware_defined = FALSE THEN violation

[RULE-02] Developers MUST define all security-relevant software components that are trusted to maintain required security properties.
[VALIDATION] IF system_has_software = TRUE AND security_relevant_software_defined = FALSE THEN violation

[RULE-03] Developers MUST define all security-relevant firmware components that are trusted to maintain required security properties.
[VALIDATION] IF system_has_firmware = TRUE AND security_relevant_firmware_defined = FALSE THEN violation

[RULE-04] Developers MUST provide written rationale demonstrating that their definition of security-relevant components is complete.
[VALIDATION] IF component_definitions_exist = TRUE AND completeness_rationale_provided = FALSE THEN violation

[RULE-05] Completeness rationale MUST address how the developer determined no additional security-relevant components exist.
[VALIDATION] IF rationale_provided = TRUE AND methodology_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security-Relevant Component Identification - Process for systematically identifying components that maintain security properties
- [PROC-02] Completeness Rationale Development - Methodology for creating and documenting rationale for definition completeness
- [PROC-03] Developer Documentation Review - Process for evaluating submitted component definitions and rationale

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New system acquisitions, major system changes, security incidents involving component failures

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Hardware Definition]
IF system_type = "hybrid_cloud"
AND hardware_components_present = TRUE
AND security_relevant_hardware_list = "undefined"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Software Rationale]
IF software_components_defined = TRUE
AND firmware_components_defined = TRUE
AND completeness_rationale = "generic_statement"
AND methodology_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Third-party Component Gap]
IF vendor_type = "third_party"
AND security_relevant_components_defined = TRUE
AND rationale_addresses_integration = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Complete Implementation]
IF hardware_components_defined = TRUE
AND software_components_defined = TRUE
AND firmware_components_defined = TRUE
AND completeness_rationale_provided = TRUE
AND methodology_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: COTS Product Acquisition]
IF product_type = "COTS"
AND vendor_security_documentation = "incomplete"
AND internal_analysis_performed = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer required to define security-relevant hardware | [RULE-01] |
| Developer required to define security-relevant software | [RULE-02] |
| Developer required to define security-relevant firmware | [RULE-03] |
| Developer required to provide completeness rationale | [RULE-04], [RULE-05] |