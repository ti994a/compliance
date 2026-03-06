# POLICY: SA-4.9: Functions, Ports, Protocols, and Services in Use

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.9 |
| NIST Control | SA-4.9: Functions, Ports, Protocols, and Services in Use |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | developer requirements, functions, ports, protocols, services, acquisition, system development |

## 1. POLICY STATEMENT
Developers of systems, system components, or system services SHALL identify all functions, ports, protocols, and services intended for organizational use during the system development lifecycle. This identification MUST occur early in development to enable security-informed design decisions and avoid costly retrofitting.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal development teams | YES | All systems developed internally |
| External vendors/contractors | YES | Systems, components, or services acquired |
| Cloud service providers | YES | When providing system services |
| COTS software vendors | YES | During procurement and integration |
| System integrators | YES | For integration projects |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Manager | • Ensure contracts include SA-4.9 requirements<br>• Validate developer compliance documentation<br>• Coordinate with security team on requirements |
| System Developer | • Identify and document all functions, ports, protocols, services<br>• Provide documentation during design phase<br>• Update documentation when changes occur |
| Security Architect | • Review developer-provided documentation<br>• Assess security implications of identified items<br>• Recommend security controls and configurations |
| System Owner | • Approve functions, ports, protocols, and services for use<br>• Ensure ongoing compliance monitoring<br>• Coordinate security reviews |

## 4. RULES
[RULE-01] Developers MUST identify all functions, ports, protocols, and services intended for organizational use before system design finalization.
[VALIDATION] IF system_design_finalized = TRUE AND developer_identification_complete = FALSE THEN violation

[RULE-02] Developer identification documentation MUST include business justification for each function, port, protocol, and service.
[VALIDATION] IF identification_documented = TRUE AND business_justification_missing = TRUE THEN violation

[RULE-03] Security team MUST review and approve all developer-identified functions, ports, protocols, and services before implementation.
[VALIDATION] IF implementation_started = TRUE AND security_approval = FALSE THEN violation

[RULE-04] Changes to functions, ports, protocols, or services MUST be re-identified and approved through the same process within 5 business days.
[VALIDATION] IF change_implemented = TRUE AND reidentification_time > 5_business_days THEN violation

[RULE-05] External service providers MUST clearly distinguish between internally provided and externally sourced functions, ports, protocols, and services.
[VALIDATION] IF external_services_used = TRUE AND source_distinction_missing = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Requirements Documentation - Standard template and process for identifying functions, ports, protocols, and services
- [PROC-02] Security Review Process - Procedures for security team assessment of developer-provided documentation
- [PROC-03] Change Management Integration - Process for handling modifications to identified items
- [PROC-04] Contract Language Standards - Required contractual language for external developers

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major system acquisitions, security incidents related to undocumented services, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Developer Documentation]
IF system_in_development = TRUE
AND developer_identification_provided = FALSE
AND design_phase_complete = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Undocumented External Services]
IF external_services_used = TRUE
AND service_source_documented = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unapproved Protocol Usage]
IF new_protocol_implemented = TRUE
AND security_approval_received = FALSE
AND protocol_in_production = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Compliant Early Identification]
IF development_phase = "requirements"
AND developer_identification_complete = TRUE
AND security_review_scheduled = TRUE
THEN compliance = TRUE

[SCENARIO-05: Late Change Documentation]
IF service_modification_date = "2024-01-15"
AND reidentification_date = "2024-01-23"
AND business_days_elapsed = 6
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer identifies functions intended for organizational use | [RULE-01], [RULE-02] |
| Developer identifies ports intended for organizational use | [RULE-01], [RULE-02] |
| Developer identifies protocols intended for organizational use | [RULE-01], [RULE-02] |
| Developer identifies services intended for organizational use | [RULE-01], [RULE-02] |
| External service source identification | [RULE-05] |
| Change management compliance | [RULE-04] |
| Security review requirements | [RULE-03] |