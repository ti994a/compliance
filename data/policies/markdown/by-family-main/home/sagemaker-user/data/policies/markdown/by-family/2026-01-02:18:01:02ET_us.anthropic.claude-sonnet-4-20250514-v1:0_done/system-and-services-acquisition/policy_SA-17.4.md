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
All system, component, and service developers MUST produce informal descriptive specifications that document security-relevant interfaces and demonstrate consistency with formal policy models. These specifications MUST be created as an integral part of the development process and provide complete coverage of security-relevant hardware, software, and firmware interfaces.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Custom developed systems | YES | All internally developed systems |
| Third-party developed systems | YES | When organization controls development requirements |
| COTS products | NO | Unless customization involves security-relevant interfaces |
| Cloud services | CONDITIONAL | When custom integration affects security interfaces |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Developers | • Produce informal descriptive top-level specifications<br>• Demonstrate consistency with formal policy models<br>• Document internal security mechanisms |
| Security Architects | • Review specifications for completeness<br>• Validate consistency with security requirements<br>• Approve interface documentation |
| Procurement Officers | • Include specification requirements in contracts<br>• Verify deliverable compliance<br>• Manage vendor compliance |

## 4. RULES
[RULE-01] Developers MUST produce an informal descriptive top-level specification as an integral part of the development process that specifies interfaces to security-relevant hardware, software, and firmware in terms of exceptions, error messages, and effects.
[VALIDATION] IF development_project = TRUE AND security_relevant_interfaces = TRUE AND informal_specification_produced = FALSE THEN violation

[RULE-02] Developers MUST demonstrate via informal demonstration that the descriptive top-level specification is consistent with the formal policy model using convincing argument with formal methods where feasible.
[VALIDATION] IF informal_specification_exists = TRUE AND consistency_demonstration_completed = FALSE THEN violation

[RULE-03] Developers MUST demonstrate that the descriptive top-level specification completely covers all interfaces to security-relevant hardware, software, and firmware.
[VALIDATION] IF security_interfaces_identified = TRUE AND specification_coverage < 100% THEN violation

[RULE-04] Developers MUST show that the descriptive top-level specification is an accurate description of the actual interfaces to security-relevant hardware, software, and firmware.
[VALIDATION] IF specification_exists = TRUE AND accuracy_verification_completed = FALSE THEN violation

[RULE-05] Developers MUST describe security-relevant hardware, software, and firmware mechanisms not addressed in the descriptive top-level specification but strictly internal to the security components.
[VALIDATION] IF internal_mechanisms_exist = TRUE AND internal_mechanisms_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Specification Review - Formal review process for all informal specifications
- [PROC-02] Consistency Validation - Process for demonstrating specification consistency with policy models  
- [PROC-03] Interface Coverage Assessment - Verification that all security-relevant interfaces are documented
- [PROC-04] Internal Mechanism Documentation - Process for documenting internal security mechanisms

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Major system changes, new development projects, security architecture updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Complete Development Documentation]
IF development_project = TRUE
AND security_relevant_interfaces = TRUE  
AND informal_specification_produced = TRUE
AND consistency_demonstrated = TRUE
AND coverage_complete = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Specification]
IF development_project = TRUE
AND security_relevant_interfaces = TRUE
AND informal_specification_produced = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Incomplete Interface Coverage]
IF informal_specification_exists = TRUE
AND security_interfaces_count = 10
AND documented_interfaces_count = 7
THEN compliance = FALSE  
violation_severity = "Moderate"

[SCENARIO-04: Undocumented Internal Mechanisms]
IF internal_security_mechanisms = TRUE
AND internal_mechanisms_documented = FALSE
AND specification_approved = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Third-Party Development Contract]
IF vendor_development = TRUE
AND contract_includes_specification_requirements = FALSE
AND security_relevant_interfaces = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Produce informal descriptive specification for exceptions, error messages, and effects | RULE-01 |
| Demonstrate consistency with formal policy model | RULE-02 |
| Show complete coverage of security-relevant interfaces | RULE-03 |
| Show accurate description of interfaces | RULE-04 |
| Describe internal security mechanisms not in specification | RULE-05 |