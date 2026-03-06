# POLICY: SA-17.3: Formal Correspondence

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-17.3 |
| NIST Control | SA-17.3: Formal Correspondence |
| Version | 1.0 |
| Owner | Chief Technology Officer |
| Keywords | formal specification, developer requirements, security interfaces, formal methods, correspondence |

## 1. POLICY STATEMENT
All system developers MUST produce formal top-level specifications that accurately describe security-relevant interfaces and demonstrate correspondence between formal models and actual implementations. Developers MUST provide formal proof or informal demonstration that specifications are consistent with policy models and completely cover all security-relevant interfaces.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Developers | YES | All contracted and internal developers |
| System Components | YES | Security-relevant hardware, software, firmware |
| Third-party Services | YES | When security-relevant interfaces exist |
| Commercial Off-the-shelf | CONDITIONAL | When customization affects security interfaces |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Developer | • Produce formal top-level specifications<br>• Demonstrate correspondence between models and implementation<br>• Document internal security mechanisms |
| Security Architect | • Review formal specifications for completeness<br>• Validate correspondence demonstrations<br>• Approve specification adequacy |
| Procurement Manager | • Include formal specification requirements in contracts<br>• Verify deliverable compliance<br>• Manage developer performance |

## 4. RULES
[RULE-01] Developers MUST produce formal top-level specifications that specify interfaces to security-relevant components in terms of exceptions, error messages, and effects as an integral part of development.
[VALIDATION] IF security_relevant_component = TRUE AND formal_specification_exists = FALSE THEN violation

[RULE-02] Developers MUST demonstrate via proof (where feasible) or informal demonstration that formal top-level specifications are consistent with formal policy models.
[VALIDATION] IF formal_specification_exists = TRUE AND consistency_demonstration = FALSE THEN violation

[RULE-03] Developers MUST show via informal demonstration that formal top-level specifications completely cover all interfaces to security-relevant hardware, software, and firmware.
[VALIDATION] IF security_interface_count > covered_interface_count THEN violation

[RULE-04] Developers MUST demonstrate that formal top-level specifications accurately describe the implemented security-relevant components.
[VALIDATION] IF specification_accuracy_verified = FALSE AND implementation_complete = TRUE THEN violation

[RULE-05] Developers MUST document security-relevant mechanisms that are internal to components but not addressed in the formal top-level specification.
[VALIDATION] IF internal_mechanisms_exist = TRUE AND internal_documentation = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Formal Specification Review - Multi-phase review process for developer-produced specifications
- [PROC-02] Correspondence Verification - Validation methodology for specification-implementation correspondence
- [PROC-03] Contract Requirements Integration - Process to embed formal specification requirements in acquisition contracts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Major system acquisitions, formal methods standard updates, compliance audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Formal Specification]
IF security_relevant_system = TRUE
AND development_phase = "complete"
AND formal_specification_delivered = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Interface Coverage]
IF formal_specification_exists = TRUE
AND total_security_interfaces = 15
AND documented_interfaces = 12
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: No Correspondence Demonstration]
IF formal_specification_exists = TRUE
AND formal_policy_model_exists = TRUE
AND consistency_proof_provided = FALSE
AND informal_demonstration_provided = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Undocumented Internal Mechanisms]
IF internal_security_mechanisms = TRUE
AND formal_specification_addresses_internal = FALSE
AND separate_internal_documentation = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Commercial Product Exception]
IF product_type = "COTS"
AND security_interface_customization = FALSE
AND formal_specification_waiver_approved = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Formal specification with exceptions, errors, effects | RULE-01 |
| Proof of specification-policy consistency | RULE-02 |
| Complete interface coverage demonstration | RULE-03 |
| Specification accuracy verification | RULE-04 |
| Internal mechanism documentation | RULE-05 |