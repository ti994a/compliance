# POLICY: SA-4.1: Functional Properties of Controls

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.1 |
| NIST Control | SA-4.1: Functional Properties of Controls |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer requirements, control properties, functional descriptions, acquisition, system development |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services MUST provide detailed descriptions of the functional properties of security and privacy controls to be implemented. These descriptions MUST focus on externally visible functionality and interfaces, excluding internal implementation details.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Developers | YES | All contracted and internal development teams |
| Component Vendors | YES | Third-party component and service providers |
| Cloud Service Providers | YES | IaaS, PaaS, SaaS providers |
| COTS Software Vendors | YES | Commercial off-the-shelf software acquisitions |
| Internal IT Development | YES | In-house developed systems and components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish functional property requirements<br>• Approve control description standards<br>• Oversee compliance verification |
| Procurement Manager | • Include functional property requirements in contracts<br>• Verify deliverable completeness<br>• Manage vendor compliance |
| System Owner | • Define required control functionality<br>• Review and approve control descriptions<br>• Validate implementation alignment |

## 4. RULES
[RULE-01] Developers MUST provide functional property descriptions for all security and privacy controls before system deployment or service activation.
[VALIDATION] IF system_status = "ready_for_deployment" AND functional_descriptions_provided = FALSE THEN violation

[RULE-02] Control descriptions MUST focus on externally visible functionality, interfaces, and capabilities, excluding internal implementation details.
[VALIDATION] IF description_contains_internal_details = TRUE OR interface_functionality_missing = TRUE THEN violation

[RULE-03] Functional property descriptions MUST be documented in acquisition contracts and service agreements within 30 days of contract execution.
[VALIDATION] IF contract_executed = TRUE AND functional_requirements_documented = FALSE AND days_since_execution > 30 THEN violation

[RULE-04] Control descriptions MUST be updated within 15 days when control functionality changes or new controls are implemented.
[VALIDATION] IF control_functionality_changed = TRUE AND description_update_days > 15 THEN violation

[RULE-05] All functional property descriptions MUST be reviewed and approved by the system owner and CISO before acceptance.
[VALIDATION] IF system_owner_approval = FALSE OR ciso_approval = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Control Description Review - Standardized review process for functional property descriptions
- [PROC-02] Vendor Documentation Requirements - Template and requirements for developer submissions
- [PROC-03] Contract Integration Process - Incorporating functional property requirements into acquisition contracts
- [PROC-04] Change Management for Controls - Process for updating descriptions when functionality changes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system acquisitions, control framework updates, regulatory changes, security incidents involving undocumented functionality

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Control Descriptions]
IF system_deployment_requested = TRUE
AND functional_descriptions_complete = FALSE
AND developer_type = "third_party"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Internal Implementation Details]
IF control_description_provided = TRUE
AND contains_internal_algorithms = TRUE
AND interface_functionality_described = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Contract Without Requirements]
IF acquisition_contract_signed = TRUE
AND functional_property_requirements_included = FALSE
AND system_type = "critical"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated Control Descriptions]
IF control_functionality_modified = TRUE
AND description_last_updated > 15_days_ago
AND system_in_production = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Approved Documentation]
IF functional_descriptions_provided = TRUE
AND system_owner_approved = TRUE
AND ciso_approved = TRUE
AND interface_functionality_complete = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer provides functional property descriptions | [RULE-01] |
| Descriptions focus on external functionality and interfaces | [RULE-02] |
| Requirements documented in acquisition contracts | [RULE-03] |
| Descriptions updated when controls change | [RULE-04] |
| Proper approval process followed | [RULE-05] |