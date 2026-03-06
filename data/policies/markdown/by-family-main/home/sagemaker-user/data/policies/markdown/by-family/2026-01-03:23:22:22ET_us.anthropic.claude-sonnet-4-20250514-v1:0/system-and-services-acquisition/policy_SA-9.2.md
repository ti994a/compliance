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
External system service providers MUST identify and document all functions, ports, protocols, and services required for their service delivery. This requirement applies to all external services that pose potential security risks to organizational systems or data.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External service providers | YES | All contracted external system services |
| Cloud service providers | YES | IaaS, PaaS, SaaS providers |
| Managed service providers | YES | Network, security, IT operations |
| Software vendors | CONDITIONAL | Only for services requiring network access |
| Internal IT services | NO | Covered under separate internal controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Manager | • Define service identification requirements in contracts<br>• Validate provider compliance before contract execution<br>• Maintain vendor compliance documentation |
| Security Architect | • Review identified functions, ports, and protocols<br>• Assess security implications of required services<br>• Approve or reject service configurations |
| Vendor Manager | • Collect and maintain service identification documentation<br>• Monitor ongoing compliance with identification requirements<br>• Coordinate updates when services change |

## 4. RULES
[RULE-01] External service providers MUST provide complete documentation of all functions, ports, protocols, and services required for service delivery before contract execution.
[VALIDATION] IF contract_signed = TRUE AND service_documentation_complete = FALSE THEN violation

[RULE-02] Service identification documentation MUST include specific port numbers, protocol types (TCP/UDP), service functions, and data flow directions.
[VALIDATION] IF documentation_provided = TRUE AND (ports_specified = FALSE OR protocols_specified = FALSE OR functions_specified = FALSE) THEN violation

[RULE-03] Providers MUST notify the organization within 30 days of any changes to required functions, ports, protocols, or services.
[VALIDATION] IF service_change_date + 30_days < notification_date THEN violation

[RULE-04] High-risk external services MUST undergo security review of identified functions, ports, and protocols before service activation.
[VALIDATION] IF risk_level = "HIGH" AND security_review_completed = FALSE AND service_active = TRUE THEN critical_violation

[RULE-05] Service identification documentation MUST be updated annually or when services are modified.
[VALIDATION] IF last_update_date + 365_days < current_date AND service_active = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Service Documentation Review - Process for validating completeness of provider service identification
- [PROC-02] Service Change Notification - Process for providers to report changes to required functions, ports, protocols, and services
- [PROC-03] Security Assessment of External Services - Process for reviewing security implications of identified service requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New external service contracts, significant service modifications, security incidents involving external services

## 7. SCENARIO PATTERNS
[SCENARIO-01: Incomplete Service Documentation]
IF external_service_contracted = TRUE
AND functions_documented = FALSE
AND contract_execution_date > current_date - 30_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Undocumented Service Changes]
IF service_modification_detected = TRUE
AND provider_notification_received = FALSE
AND change_date + 30_days < current_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: High-Risk Service Without Review]
IF risk_assessment_score >= 7
AND security_review_completed = FALSE
AND service_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Outdated Documentation]
IF service_documentation_age > 365_days
AND service_status = "active"
AND update_request_sent = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Complete Compliant Documentation]
IF functions_documented = TRUE
AND ports_documented = TRUE
AND protocols_documented = TRUE
AND documentation_current = TRUE
AND security_review_completed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| External service providers required to identify functions, ports, protocols, and services | [RULE-01], [RULE-02] |
| Documentation completeness and accuracy | [RULE-02] |
| Change management for service modifications | [RULE-03] |
| Security review of high-risk services | [RULE-04] |
| Documentation currency requirements | [RULE-05] |