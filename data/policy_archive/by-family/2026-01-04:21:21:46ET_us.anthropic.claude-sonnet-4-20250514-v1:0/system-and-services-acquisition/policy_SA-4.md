# POLICY: SA-4: Acquisition Process

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4 |
| NIST Control | SA-4: Acquisition Process |
| Version | 1.0 |
| Owner | Chief Procurement Officer |
| Keywords | acquisition, contracts, security requirements, privacy requirements, vendor management, procurement, supply chain |

## 1. POLICY STATEMENT
All acquisition contracts for systems, system components, or system services MUST include comprehensive security and privacy requirements, assurance criteria, and acceptance standards using standardized contract language. Contracts SHALL explicitly define responsibilities, documentation requirements, and acceptance criteria to ensure acquired solutions meet organizational security and privacy objectives.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| IT Systems | YES | All information systems and components |
| Cloud Services | YES | SaaS, PaaS, IaaS acquisitions |
| Software Licenses | YES | Commercial and custom software |
| Hardware Procurement | YES | Servers, networking, endpoints |
| Professional Services | YES | Development, consulting, managed services |
| Low-value purchases | CONDITIONAL | Purchases >$10K or handling sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Include standardized security language in contracts<br>• Validate contract compliance before execution<br>• Coordinate with security teams on requirements |
| CISO/Privacy Officer | • Define security and privacy functional requirements<br>• Review and approve acquisition security terms<br>• Establish acceptance criteria for security controls |
| Legal Counsel | • Develop standardized contract language<br>• Review liability and responsibility allocations<br>• Ensure regulatory compliance in contracts |

## 4. RULES
[RULE-01] All acquisition contracts MUST include security functional requirements explicitly or by reference using organization-approved standardized contract language.
[VALIDATION] IF contract_type IN ["system", "component", "service"] AND security_requirements_included = FALSE THEN critical_violation

[RULE-02] All acquisition contracts MUST include privacy functional requirements explicitly or by reference using organization-approved standardized contract language.
[VALIDATION] IF contract_handles_pii = TRUE AND privacy_requirements_included = FALSE THEN critical_violation

[RULE-03] Contracts MUST specify strength of mechanism requirements including degree of correctness, completeness, and resistance to tampering.
[VALIDATION] IF security_controls_specified = TRUE AND strength_requirements_defined = FALSE THEN violation

[RULE-04] Security and privacy assurance requirements including development processes and assessment evidence MUST be included in contracts.
[VALIDATION] IF contract_value > 100000 AND assurance_requirements_included = FALSE THEN violation

[RULE-05] Contracts MUST explicitly allocate responsibility for information security, privacy, and supply chain risk management between parties.
[VALIDATION] IF responsibility_allocation_documented = FALSE THEN violation

[RULE-06] All contracts MUST include requirements for protecting security and privacy documentation throughout the system lifecycle.
[VALIDATION] IF documentation_protection_requirements = FALSE THEN violation

[RULE-07] Contracts MUST define measurable acceptance criteria for security and privacy controls before system acceptance.
[VALIDATION] IF acceptance_criteria_defined = FALSE OR acceptance_criteria_measurable = FALSE THEN violation

[RULE-08] System development environment and intended operational environment MUST be described in acquisition contracts.
[VALIDATION] IF environment_description_included = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Contract Security Review Process - Mandatory security review before contract execution
- [PROC-02] Standardized Contract Language Management - Maintenance of approved security clauses
- [PROC-03] Vendor Security Assessment - Pre-award security capability evaluation
- [PROC-04] Acceptance Testing Procedures - Security control validation before acceptance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Regulatory changes, security incidents involving vendors, contract disputes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Service Procurement]
IF service_type = "cloud_service"
AND contract_includes_security_requirements = TRUE
AND privacy_requirements_included = TRUE
AND responsibility_allocation_defined = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Privacy Requirements]
IF contract_processes_pii = TRUE
AND privacy_functional_requirements = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Inadequate Acceptance Criteria]
IF contract_value > 50000
AND acceptance_criteria_defined = TRUE
AND acceptance_criteria_measurable = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Development Service Contract]
IF service_type = "development"
AND assurance_requirements_included = FALSE
AND contract_value > 100000
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Hardware Procurement Compliance]
IF procurement_type = "hardware"
AND security_functional_requirements = TRUE
AND strength_requirements_defined = TRUE
AND documentation_protection_requirements = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security functional requirements included | [RULE-01] |
| Privacy functional requirements included | [RULE-02] |
| Strength of mechanism requirements | [RULE-03] |
| Security assurance requirements | [RULE-04] |
| Privacy assurance requirements | [RULE-04] |
| Security controls specification | [RULE-01], [RULE-03] |
| Privacy controls specification | [RULE-02] |
| Security documentation requirements | [RULE-06] |
| Privacy documentation requirements | [RULE-06] |
| Documentation protection requirements | [RULE-06] |
| Development environment description | [RULE-08] |
| Security responsibility allocation | [RULE-05] |
| Privacy responsibility allocation | [RULE-05] |
| Supply chain risk management allocation | [RULE-05] |
| Acceptance criteria definition | [RULE-07] |