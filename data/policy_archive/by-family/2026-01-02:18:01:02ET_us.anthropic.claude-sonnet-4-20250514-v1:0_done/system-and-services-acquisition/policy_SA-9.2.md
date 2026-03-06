# POLICY: SA-9.2: Identification of Functions, Ports, Protocols, and Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9.2 |
| NIST Control | SA-9.2: Identification of Functions, Ports, Protocols, and Services |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external services, ports, protocols, functions, service providers, third-party, network services |

## 1. POLICY STATEMENT
External system service providers MUST identify and document all functions, ports, protocols, and services required for their service delivery. This requirement enables informed security decisions regarding network restrictions and service limitations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External service providers | YES | All providers of system services to the organization |
| Cloud service providers | YES | Including SaaS, PaaS, and IaaS providers |
| Managed service providers | YES | IT operations, security, and infrastructure services |
| Software vendors | CONDITIONAL | Only for hosted or network-dependent services |
| Internal IT services | NO | Covered under separate internal controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Define service identification requirements in contracts<br>• Ensure vendor compliance with documentation standards<br>• Validate completeness of service specifications |
| Security Architect | • Review service specifications for security implications<br>• Assess network exposure and protocol risks<br>• Approve service configurations |
| Vendor Management | • Maintain service documentation repository<br>• Monitor vendor compliance with identification requirements<br>• Coordinate service specification updates |

## 4. RULES
[RULE-01] All external service providers MUST provide complete documentation of functions, ports, protocols, and services within 30 days of contract execution.
[VALIDATION] IF contract_signed = TRUE AND documentation_received = FALSE AND days_elapsed > 30 THEN violation

[RULE-02] Service documentation MUST include specific port numbers, protocol types, data flows, and functional dependencies for all network communications.
[VALIDATION] IF documentation_complete = FALSE OR missing_network_details = TRUE THEN violation

[RULE-03] External service providers MUST notify the organization within 15 business days of any changes to functions, ports, protocols, or services.
[VALIDATION] IF service_change_date < (notification_date - 15_business_days) THEN violation

[RULE-04] Service identification requirements MUST be included in all procurement contracts and service level agreements for external system services.
[VALIDATION] IF contract_type = "external_system_service" AND identification_clause = FALSE THEN violation

[RULE-05] Service specifications MUST be reviewed and validated by Security Architecture team before service activation.
[VALIDATION] IF service_status = "active" AND security_review_completed = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Service Documentation Review - Standardized process for validating service specifications
- [PROC-02] Service Change Notification - Process for handling provider notifications of service modifications
- [PROC-03] Contract Security Requirements - Template clauses for service identification requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: New service categories, significant security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Service Documentation]
IF external_service = TRUE
AND contract_active = TRUE
AND service_documentation = "incomplete"
AND days_since_contract > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Undocumented Service Changes]
IF service_change_implemented = TRUE
AND change_notification_received = FALSE
AND discovery_method = "security_monitoring"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Activated Service Without Review]
IF service_status = "production"
AND security_architecture_review = FALSE
AND service_type = "external_system_service"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Contract Without Requirements]
IF contract_type = "external_system_service"
AND contract_date > policy_effective_date
AND service_identification_clause = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Service Onboarding]
IF external_service = TRUE
AND documentation_complete = TRUE
AND security_review_approved = TRUE
AND contract_includes_requirements = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| External service providers required to identify functions, ports, protocols, and services | [RULE-01], [RULE-02] |
| Service identification requirements defined and implemented | [RULE-04], [RULE-05] |
| Documentation completeness and accuracy | [RULE-02], [RULE-03] |
| Contractual enforcement mechanisms | [RULE-04] |