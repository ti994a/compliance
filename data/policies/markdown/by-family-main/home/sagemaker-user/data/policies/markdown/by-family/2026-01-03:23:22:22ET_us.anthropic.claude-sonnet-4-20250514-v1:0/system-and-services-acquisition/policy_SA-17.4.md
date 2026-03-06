# POLICY: SA-17.4: Informal Correspondence

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-17.4 |
| NIST Control | SA-17.4: Informal Correspondence |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer requirements, security specifications, interface documentation, formal methods, assurance |

## 1. POLICY STATEMENT
All system developers MUST produce informal descriptive specifications that document security-relevant interfaces and demonstrate consistency with formal security models. These specifications MUST comprehensively cover all security-relevant hardware, software, and firmware interfaces with proper validation and demonstration requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Developers | YES | All contracted and internal developers |
| System Components | YES | Security-relevant components only |
| System Services | YES | Custom developed services |
| COTS Products | NO | Commercial off-the-shelf without customization |
| Third-party Integrators | YES | When developing custom interfaces |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Developer | • Produce informal descriptive specifications<br>• Demonstrate specification consistency<br>• Document internal security mechanisms |
| Security Architect | • Review specification completeness<br>• Validate consistency demonstrations<br>• Approve specification accuracy |
| Procurement Manager | • Include requirements in contracts<br>• Verify deliverable compliance<br>• Manage developer obligations |

## 4. RULES
[RULE-01] Developers MUST produce an informal descriptive top-level specification as an integral part of the development process that specifies interfaces to security-relevant hardware, software, and firmware in terms of exceptions, error messages, and effects.
[VALIDATION] IF development_phase = "active" AND security_interfaces_exist = TRUE AND informal_specification_exists = FALSE THEN violation

[RULE-02] Developers MUST demonstrate via informal demonstration and convincing argument with formal methods that the descriptive specification is consistent with the formal policy model.
[VALIDATION] IF formal_policy_model_exists = TRUE AND consistency_demonstration_provided = FALSE THEN violation

[RULE-03] Developers MUST show via informal demonstration that the descriptive specification completely covers all interfaces to security-relevant hardware, software, and firmware.
[VALIDATION] IF security_interfaces_count > documented_interfaces_count THEN violation

[RULE-04] Developers MUST demonstrate that the descriptive specification accurately describes the interfaces to security-relevant hardware, software, and firmware.
[VALIDATION] IF accuracy_demonstration_provided = FALSE OR specification_accuracy_verified = FALSE THEN violation

[RULE-05] Developers MUST describe security-relevant hardware, software, and firmware mechanisms not addressed in the descriptive specification but strictly internal to security components.
[VALIDATION] IF internal_mechanisms_exist = TRUE AND internal_mechanisms_documented = FALSE THEN violation

[RULE-06] All informal correspondence documentation MUST be delivered before system acceptance and maintained throughout the system lifecycle.
[VALIDATION] IF system_acceptance_date <= current_date AND correspondence_documentation_complete = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Specification Review - Formal review process for informal descriptive specifications
- [PROC-02] Consistency Validation - Process for validating specification consistency with formal models
- [PROC-03] Interface Coverage Assessment - Procedure for verifying complete interface documentation
- [PROC-04] Internal Mechanism Documentation - Process for documenting internal security mechanisms

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New development contracts, security architecture changes, formal model updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Interface Documentation]
IF development_contract = "active"
AND security_relevant_interfaces > 0
AND informal_specification_delivered = FALSE
AND development_phase >= "design_complete"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Coverage Demonstration]
IF informal_specification_exists = TRUE
AND total_security_interfaces = 15
AND documented_interfaces = 12
AND coverage_demonstration_provided = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Consistency Validation]
IF formal_policy_model_exists = TRUE
AND informal_specification_exists = TRUE
AND consistency_demonstration = FALSE
AND system_acceptance_pending = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Undocumented Internal Mechanisms]
IF security_relevant_internals_identified = TRUE
AND internal_mechanism_documentation = FALSE
AND specification_review_complete = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Complete Compliance]
IF informal_specification_exists = TRUE
AND consistency_demonstrated = TRUE
AND coverage_complete = TRUE
AND accuracy_verified = TRUE
AND internal_mechanisms_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Produce informal descriptive specification for exceptions | RULE-01 |
| Produce informal descriptive specification for error messages | RULE-01 |
| Produce informal descriptive specification for effects | RULE-01 |
| Show consistency with formal policy model | RULE-02 |
| Show complete interface coverage | RULE-03 |
| Show specification accuracy | RULE-04 |
| Describe internal security mechanisms | RULE-05 |