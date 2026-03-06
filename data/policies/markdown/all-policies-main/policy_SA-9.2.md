```markdown
# POLICY: SA-9.2: Identification of Functions, Ports, Protocols, and Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9.2 |
| NIST Control | SA-9.2: Identification of Functions, Ports, Protocols, and Services |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external services, ports, protocols, functions, service providers, acquisition, network services |

## 1. POLICY STATEMENT
External system service providers MUST identify and document all functions, ports, protocols, and services required for their service delivery. This requirement enables informed security decisions regarding network restrictions and service trade-offs.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External service providers | YES | All contracted external system services |
| Cloud service providers | YES | IaaS, PaaS, SaaS providers |
| Managed service providers | YES | IT operations, security services |
| Software vendors | CONDITIONAL | Only for hosted/managed services |
| Internal IT services | NO | Covered under separate controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Team | • Include identification requirements in contracts<br>• Validate provider compliance before contract execution<br>• Maintain service documentation repository |
| Security Architecture Team | • Review identified functions, ports, protocols<br>• Assess security implications of required services<br>• Approve or reject service configurations |
| Vendor Management Office | • Monitor ongoing compliance with identification requirements<br>• Coordinate service documentation updates<br>• Escalate non-compliance issues |

## 4. RULES
[RULE-01] All external service providers MUST provide complete documentation of functions, ports, protocols, and services before service activation.
[VALIDATION] IF external_service_active = TRUE AND documentation_complete = FALSE THEN critical_violation

[RULE-02] Service identification documentation MUST include specific port numbers, protocol types, data flows, and functional dependencies.
[VALIDATION] IF documentation_provided = TRUE AND (ports_specified = FALSE OR protocols_specified = FALSE OR functions_specified = FALSE) THEN violation

[RULE-03] Providers MUST notify the organization within 30 days of any changes to identified functions, ports, protocols, or services.
[VALIDATION] IF service_change_date < (current_date - 30_days) AND notification_received = FALSE THEN violation

[RULE-04] Identification requirements MUST be included in all external service contracts and service level agreements.
[VALIDATION] IF contract_executed = TRUE AND identification_clause_included = FALSE THEN violation

[RULE-05] Security team MUST review and approve all identified functions, ports, protocols, and services before service implementation.
[VALIDATION] IF service_implemented = TRUE AND security_approval = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Service Documentation Review - Standardized process for evaluating provider-submitted service specifications
- [PROC-02] Service Change Notification - Process for handling provider notifications of service modifications
- [PROC-03] Contract Requirements Integration - Procedure for including identification requirements in procurement documents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New service categories, regulatory changes, security incidents involving external services

## 7. SCENARIO PATTERNS
[SCENARIO-01: Complete Documentation Provided]
IF external_service_provider = TRUE
AND functions_documented = TRUE
AND ports_documented = TRUE
AND protocols_documented = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Protocol Information]
IF external_service_provider = TRUE
AND functions_documented = TRUE
AND ports_documented = TRUE
AND protocols_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Service Change Without Notification]
IF service_configuration_changed = TRUE
AND change_date > (current_date - 45_days)
AND provider_notification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Unapproved Service Implementation]
IF external_service_active = TRUE
AND documentation_provided = TRUE
AND security_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Contract Missing Requirements]
IF external_service_contract = TRUE
AND identification_requirements_clause = FALSE
AND service_start_date > policy_effective_date
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| External service providers that require identification are defined | [RULE-01], [RULE-04] |
| Providers required to identify functions, ports, protocols, and services | [RULE-01], [RULE-02], [RULE-05] |
```