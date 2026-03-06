# POLICY: SA-17.7: Structure for Least Privilege

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-17.7 |
| NIST Control | SA-17.7: Structure for Least Privilege |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | least privilege, developer requirements, system architecture, access control, privilege decomposition |

## 1. POLICY STATEMENT
The organization requires all system developers to structure security-relevant hardware, software, and firmware components to facilitate controlling access with least privilege principles. All system components must be designed with minimal necessary privileges and fine-grained access controls to limit security impact from failures or misuse.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All systems developed internally |
| Third-Party Developers | YES | All contracted system development |
| COTS Software | CONDITIONAL | When customizable or configurable |
| System Integrators | YES | All system integration projects |
| Cloud Service Providers | CONDITIONAL | When providing custom development |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve least privilege architecture requirements<br>• Review developer compliance assessments<br>• Define privilege decomposition standards |
| System Architect | • Design least privilege system structures<br>• Review developer architecture documentation<br>• Validate privilege separation implementations |
| Procurement Manager | • Include least privilege requirements in contracts<br>• Validate developer capability assessments<br>• Manage contract compliance monitoring |
| Development Manager | • Ensure internal teams follow least privilege design<br>• Conduct code reviews for privilege implementation<br>• Coordinate with security architecture team |

## 4. RULES

[RULE-01] All system developers MUST structure security-relevant components to implement least privilege with role-based access interfaces that provide only necessary privileges for each function.
[VALIDATION] IF component_privileges > minimum_required_privileges THEN violation

[RULE-02] Developer documentation MUST demonstrate privilege decomposition with granular access controls and justify all assigned privileges for each system component.
[VALIDATION] IF privilege_justification = "missing" OR granularity_level = "coarse" THEN violation

[RULE-03] System modules MUST be designed so internal elements are only accessible through the module's defined interfaces, with no direct external access to encapsulated components.
[VALIDATION] IF direct_external_access = TRUE AND encapsulated_component = TRUE THEN violation

[RULE-04] All acquisition contracts MUST include specific least privilege architecture requirements and deliverable documentation proving compliance with privilege separation principles.
[VALIDATION] IF contract_least_privilege_clause = "absent" OR deliverable_requirements = "undefined" THEN violation

[RULE-05] Developer architecture reviews MUST occur before final acceptance and SHALL verify that access modes (read/write/execute) are minimized for each component's required functionality.
[VALIDATION] IF architecture_review = "incomplete" OR access_modes > minimum_required THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Security Architecture Review - Formal assessment of least privilege implementation
- [PROC-02] Privilege Decomposition Validation - Testing and verification of granular access controls
- [PROC-03] Contract Compliance Monitoring - Ongoing verification of developer adherence to requirements
- [PROC-04] Internal Development Standards - Guidelines for internal teams on least privilege design

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system acquisitions, security incidents involving privilege escalation, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Third-Party Developer Compliance]
IF developer_type = "third_party"
AND least_privilege_documentation = "provided"
AND privilege_granularity = "fine"
AND access_justification = "complete"
THEN compliance = TRUE

[SCENARIO-02: Excessive Component Privileges]
IF component_privileges > minimum_required
AND justification_documented = FALSE
AND architecture_review = "passed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Contract Requirements]
IF contract_type = "development"
AND least_privilege_clause = "absent"
AND project_value > 100000
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Internal Module Design]
IF module_type = "internal"
AND direct_external_access = TRUE
AND security_relevant = TRUE
AND encapsulation_bypass = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: COTS Configuration Assessment]
IF system_type = "COTS"
AND customization_level = "high"
AND privilege_configuration = "default"
AND least_privilege_assessment = "not_performed"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer structures security-relevant components for least privilege | [RULE-01], [RULE-02] |
| Internal module privilege separation | [RULE-03] |
| Contract requirements for least privilege architecture | [RULE-04] |
| Architecture review and validation processes | [RULE-05] |