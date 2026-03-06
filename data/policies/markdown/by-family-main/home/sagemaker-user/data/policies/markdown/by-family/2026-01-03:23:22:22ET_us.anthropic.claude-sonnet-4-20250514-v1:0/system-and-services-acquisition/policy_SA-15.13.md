# POLICY: SA-15.13: Logging Syntax

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-15.13 |
| NIST Control | SA-15.13: Logging Syntax |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | secure logging, developer requirements, audit events, incident response, logging format |

## 1. POLICY STATEMENT
All system and component developers MUST implement secure logging formats with defined event types and detail levels to support incident response and security reconstruction. Logging requirements MUST be specified in acquisition contracts and validated during development phases.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All custom software development |
| External Vendors/Contractors | YES | Systems, components, and services under contract |
| COTS Software | CONDITIONAL | When customization or integration involves logging |
| Cloud Service Providers | YES | When logging configuration is controllable |
| Legacy Systems | CONDITIONAL | During major updates or security reviews |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define secure logging standards<br>• Approve logging format specifications<br>• Oversee compliance validation |
| Procurement Manager | • Include logging requirements in contracts<br>• Validate vendor compliance documentation<br>• Manage acquisition documentation |
| Development Manager | • Ensure developer adherence to logging standards<br>• Review logging implementations<br>• Coordinate with security teams on requirements |
| Security Architect | • Define technical logging specifications<br>• Review logging format compliance<br>• Validate event type coverage |

## 4. RULES
[RULE-01] Developers MUST implement secure logging formats that align with organizational audit event standards defined in AU-02.
[VALIDATION] IF logging_format_documented = FALSE OR logging_format_compliant = FALSE THEN violation

[RULE-02] All acquisition contracts for systems, components, or services MUST specify required logging formats, event types, and detail levels.
[VALIDATION] IF contract_type IN ["system", "component", "service"] AND logging_requirements_specified = FALSE THEN violation

[RULE-03] Developers MUST log security-relevant events at the detail level specified in organizational requirements with structured, parseable formats.
[VALIDATION] IF security_events_logged = FALSE OR detail_level < required_minimum OR format_structured = FALSE THEN violation

[RULE-04] Logging implementations MUST support incident response and forensic reconstruction capabilities as defined in IR-04 and IR-08.
[VALIDATION] IF incident_response_support = FALSE OR forensic_capability = FALSE THEN violation

[RULE-05] All logging format specifications MUST be documented and validated during development milestones and acceptance testing.
[VALIDATION] IF milestone_validation = FALSE OR acceptance_testing_passed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Secure Logging Standards Definition - Establish organizational logging format and event type requirements
- [PROC-02] Contract Logging Requirements - Include specific logging clauses in acquisition documents
- [PROC-03] Developer Logging Validation - Verify compliance during development phases
- [PROC-04] Logging Format Assessment - Evaluate logging implementations against security requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Major system acquisitions, security incidents involving logging gaps, technology architecture changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Contract Requirements]
IF contract_type = "system_development"
AND logging_requirements_specified = FALSE
AND contract_executed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Non-Compliant Logging Format]
IF developer_logging_implemented = TRUE
AND logging_format_structured = FALSE
AND security_events_captured = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Adequate Logging Implementation]
IF logging_format_compliant = TRUE
AND required_events_logged = TRUE
AND incident_response_supported = TRUE
AND contract_requirements_met = TRUE
THEN compliance = TRUE

[SCENARIO-04: Legacy System Exemption]
IF system_type = "legacy"
AND major_update_planned = FALSE
AND compensating_controls = TRUE
AND risk_accepted = TRUE
THEN compliance = TRUE

[SCENARIO-05: Vendor Non-Compliance]
IF vendor_type = "external"
AND logging_requirements_contractual = TRUE
AND vendor_compliance_validated = FALSE
AND delivery_date_passed = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Secure logging format(s) are defined | [RULE-01] |
| Event types to log are defined | [RULE-01], [RULE-03] |
| Level of detail to log is defined | [RULE-03] |
| Developer uses secure logging formats | [RULE-01], [RULE-05] |
| Contract requirements specified | [RULE-02] |
| Incident response capability supported | [RULE-04] |