# POLICY: SA-17: Developer Security and Privacy Architecture and Design

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-17 |
| NIST Control | SA-17: Developer Security and Privacy Architecture and Design |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer, security architecture, privacy architecture, design specification, enterprise architecture, external development |

## 1. POLICY STATEMENT
All external developers contracted to build systems, system components, or system services MUST produce design specifications and security/privacy architectures that align with the organization's enterprise architecture. These specifications MUST accurately describe required security and privacy functionality and demonstrate how individual functions work together to provide unified protection.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External system developers | YES | All contracted development work |
| System component vendors | YES | Custom or modified components |
| System service providers | YES | Custom service development |
| Internal development teams | CONDITIONAL | When demonstrating enterprise alignment required |
| COTS software purchases | NO | Standard commercial products without customization |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Enterprise Architect | • Define organizational security and privacy architecture standards<br>• Review developer submissions for enterprise alignment<br>• Approve architecture consistency determinations |
| Procurement Manager | • Include SA-17 requirements in all development contracts<br>• Ensure contract deliverables specify required documentation<br>• Validate developer submissions before acceptance |
| Security Architect | • Review developer security architecture specifications<br>• Validate security control allocation and integration<br>• Assess unified security approach adequacy |

## 4. RULES
[RULE-01] All development contracts MUST include requirements for developers to produce design specifications and security/privacy architectures consistent with organizational enterprise architecture.
[VALIDATION] IF contract_type = "development" AND sa17_requirements = FALSE THEN violation

[RULE-02] Developer-produced security architectures MUST accurately describe required security functionality and allocation of controls among physical and logical components.
[VALIDATION] IF security_architecture_submitted = TRUE AND (functionality_description = "incomplete" OR control_allocation = "undefined") THEN violation

[RULE-03] Developer-produced privacy architectures MUST accurately describe required privacy functionality and allocation of controls among physical and logical components.
[VALIDATION] IF privacy_architecture_submitted = TRUE AND (privacy_functionality_description = "incomplete" OR privacy_control_allocation = "undefined") THEN violation

[RULE-04] Developer architectures MUST demonstrate how individual security and privacy functions work together to provide unified protection capabilities.
[VALIDATION] IF architecture_submitted = TRUE AND unified_approach_documented = FALSE THEN violation

[RULE-05] Enterprise Architecture team MUST review and approve all developer architecture submissions for consistency with organizational enterprise architecture before system acceptance.
[VALIDATION] IF developer_architecture_submitted = TRUE AND enterprise_architecture_approval = FALSE AND system_accepted = TRUE THEN critical_violation

[RULE-06] Developer design specifications MUST be updated and resubmitted for approval when significant changes are made to security or privacy functionality during development.
[VALIDATION] IF security_changes = "significant" AND updated_specification_submitted = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Architecture Review Process - Standardized review workflow for evaluating developer submissions
- [PROC-02] Enterprise Architecture Consistency Assessment - Methodology for determining alignment with organizational architecture
- [PROC-03] Contract Requirements Integration - Process for including SA-17 requirements in procurement documents
- [PROC-04] Architecture Change Management - Procedures for handling architecture modifications during development

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Enterprise architecture updates, significant contract failures, regulatory changes, security incidents involving developer-built systems

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Architecture Requirements in Contract]
IF contract_type = "system_development"
AND sa17_requirements_included = FALSE
AND contract_signed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Security Architecture Submission]
IF developer_security_architecture = "submitted"
AND functionality_description = "incomplete"
AND enterprise_architect_review = "pending"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: System Accepted Without Architecture Approval]
IF system_acceptance = "completed"
AND developer_architecture_submitted = TRUE
AND enterprise_architecture_approval = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Architecture Changes Without Updated Documentation]
IF development_phase = "active"
AND security_functionality_changes = "significant"
AND updated_architecture_submitted = FALSE
AND days_since_change > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Architecture Review Process]
IF developer_architecture_submitted = TRUE
AND enterprise_architecture_review = "completed"
AND consistency_determination = "approved"
AND unified_approach_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer produces design specification consistent with enterprise architecture | RULE-01, RULE-05 |
| Security architecture accurately describes functionality and control allocation | RULE-02 |
| Privacy architecture accurately describes functionality and control allocation | RULE-03 |
| Architecture expresses unified approach to security protection | RULE-04 |
| Architecture expresses unified approach to privacy protection | RULE-04 |
| Organizational review and approval of developer submissions | RULE-05 |