# POLICY: SA-17.4: Informal Correspondence

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-17.4 |
| NIST Control | SA-17.4: Informal Correspondence |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer requirements, security interfaces, top-level specification, formal policy model, security-relevant hardware |

## 1. POLICY STATEMENT
All system, component, and service developers MUST produce informal descriptive top-level specifications that accurately document security-relevant interfaces and demonstrate consistency with formal policy models. These specifications MUST be created as an integral part of the development process and cover all security-relevant hardware, software, and firmware interfaces.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Custom developed systems | YES | All internally developed systems |
| Third-party developers | YES | When contracted for custom development |
| COTS products | NO | Unless customization involves security interfaces |
| Cloud service providers | CONDITIONAL | Only for custom integrations |
| System integrators | YES | When modifying security-relevant interfaces |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Developers | • Create informal descriptive top-level specifications<br>• Demonstrate consistency with formal policy models<br>• Document all security-relevant interfaces |
| Security Architects | • Review specifications for completeness<br>• Validate consistency with security requirements<br>• Approve interface documentation |
| Procurement Officers | • Include specification requirements in contracts<br>• Verify deliverable compliance<br>• Enforce contract terms |

## 4. RULES

[RULE-01] Developers MUST produce an informal descriptive top-level specification as an integral part of the development process that specifies interfaces to security-relevant hardware, software, and firmware in terms of exceptions, error messages, and effects.
[VALIDATION] IF development_project = TRUE AND security_interfaces_exist = TRUE AND top_level_specification_exists = FALSE THEN violation

[RULE-02] Developers MUST demonstrate via informal demonstration and convincing argument with formal methods that the descriptive top-level specification is consistent with the formal policy model.
[VALIDATION] IF top_level_specification_exists = TRUE AND consistency_demonstration_completed = FALSE THEN violation

[RULE-03] Developers MUST show that the descriptive top-level specification completely covers all interfaces to security-relevant hardware, software, and firmware.
[VALIDATION] IF security_interfaces_count > documented_interfaces_count THEN violation

[RULE-04] Developers MUST demonstrate that the descriptive top-level specification accurately describes the interfaces to security-relevant hardware, software, and firmware.
[VALIDATION] IF specification_accuracy_validated = FALSE AND development_phase >= "testing" THEN violation

[RULE-05] Developers MUST describe security-relevant hardware, software, and firmware mechanisms not addressed in the descriptive top-level specification but strictly internal to security components.
[VALIDATION] IF internal_mechanisms_exist = TRUE AND internal_mechanisms_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Specification Review - Formal review process for all informal descriptive specifications
- [PROC-02] Consistency Validation - Process for demonstrating specification-model consistency
- [PROC-03] Interface Coverage Assessment - Verification that all security interfaces are documented
- [PROC-04] Contract Compliance Verification - Validation of developer deliverable completeness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New development projects, security architecture changes, contract modifications

## 7. SCENARIO PATTERNS

[SCENARIO-01: Missing Interface Documentation]
IF development_project = "active"
AND security_relevant_interfaces > 0
AND top_level_specification_exists = FALSE
AND development_phase >= "design"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Coverage Demonstration]
IF top_level_specification_exists = TRUE
AND total_security_interfaces = 15
AND documented_interfaces = 12
AND coverage_demonstration = "incomplete"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Internal Mechanism Documentation]
IF security_relevant_internal_mechanisms = TRUE
AND internal_mechanism_documentation = FALSE
AND specification_phase = "complete"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Third-Party Developer Compliance]
IF developer_type = "third_party"
AND contract_includes_SA174_requirements = TRUE
AND specification_deliverable_received = TRUE
AND consistency_demonstration_provided = TRUE
THEN compliance = TRUE

[SCENARIO-05: Formal Methods Integration]
IF formal_policy_model_exists = TRUE
AND informal_specification_exists = TRUE
AND consistency_demonstration_method = "formal_methods"
AND demonstration_completed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Produce informal descriptive top-level specification for exceptions | RULE-01 |
| Produce informal descriptive top-level specification for error messages | RULE-01 |
| Produce informal descriptive top-level specification for effects | RULE-01 |
| Show consistency with formal policy model | RULE-02 |
| Show complete coverage of security interfaces | RULE-03 |
| Show accurate description of interfaces | RULE-04 |
| Describe internal security mechanisms | RULE-05 |