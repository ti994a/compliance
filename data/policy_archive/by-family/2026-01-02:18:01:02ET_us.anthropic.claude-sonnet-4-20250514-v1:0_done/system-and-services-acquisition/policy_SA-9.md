# POLICY: SA-9: External System Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9 |
| NIST Control | SA-9: External System Services |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external services, third-party providers, service level agreements, vendor management, supply chain security |

## 1. POLICY STATEMENT
All external system service providers MUST comply with organizational security and privacy requirements and employ organization-defined controls. The organization SHALL establish documented oversight responsibilities and implement ongoing monitoring processes to ensure continuous compliance by external service providers.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud Service Providers | YES | All IaaS, PaaS, SaaS providers |
| Managed Service Providers | YES | IT operations, security services |
| Software Vendors | YES | Commercial and custom software |
| Business Partners | YES | Systems integration, data sharing |
| Contractors | YES | System development, maintenance |
| Government Agencies | CONDITIONAL | When providing system services |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve security requirements for external services<br>• Review compliance monitoring reports<br>• Authorize external service relationships |
| Procurement Officer | • Include security requirements in contracts<br>• Validate provider compliance documentation<br>• Manage service level agreements |
| System Owner | • Define technical security controls for external services<br>• Monitor ongoing compliance<br>• Report security incidents involving external providers |

## 4. RULES
[RULE-01] External system service providers MUST comply with all organizational security and privacy requirements as defined in approved contracts and service level agreements.
[VALIDATION] IF provider_type = "external" AND security_compliance_status != "compliant" THEN violation

[RULE-02] All external service contracts SHALL include organization-defined security controls that providers must implement and maintain.
[VALIDATION] IF contract_type = "external_service" AND required_controls_defined = FALSE THEN violation

[RULE-03] Organizational oversight roles and responsibilities for external system services MUST be documented and assigned to qualified personnel.
[VALIDATION] IF external_service_active = TRUE AND oversight_roles_documented = FALSE THEN violation

[RULE-04] User roles and responsibilities regarding external system services SHALL be defined, documented, and communicated to all relevant personnel.
[VALIDATION] IF user_access_to_external_service = TRUE AND user_responsibilities_documented = FALSE THEN violation

[RULE-05] Organizations MUST employ defined processes, methods, and techniques to monitor control compliance by external service providers on an ongoing basis.
[VALIDATION] IF external_provider_active = TRUE AND monitoring_process_implemented = FALSE THEN violation

[RULE-06] Service level agreements with external providers SHALL define measurable security outcomes, performance expectations, and remediation requirements for noncompliance.
[VALIDATION] IF sla_exists = TRUE AND measurable_security_outcomes_defined = FALSE THEN violation

[RULE-07] External service provider compliance assessments MUST be reviewed at least annually or upon significant service changes.
[VALIDATION] IF last_compliance_review_date > 365_days OR service_change_impact = "significant" AND compliance_review_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Service Provider Evaluation - Security and privacy assessment before engagement
- [PROC-02] Contract Security Requirements - Standard security clauses and control requirements
- [PROC-03] Ongoing Compliance Monitoring - Regular assessment of provider security posture
- [PROC-04] Incident Response Coordination - Joint incident handling with external providers
- [PROC-05] Service Level Agreement Management - Performance monitoring and remediation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon significant regulatory changes
- Triggering events: New external service engagements, security incidents involving external providers, regulatory changes, failed compliance assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Cloud Provider Onboarding]
IF service_type = "cloud_provider"
AND contract_signed = TRUE
AND security_requirements_included = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing SLA Security Metrics]
IF external_service_active = TRUE
AND sla_exists = TRUE
AND security_metrics_defined = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Overdue Compliance Assessment]
IF external_provider_relationship = "active"
AND last_compliance_assessment > 365_days
AND assessment_waiver_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Undefined User Responsibilities]
IF users_accessing_external_service = TRUE
AND user_responsibility_documentation = "missing"
AND security_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Provider Security Incident]
IF external_provider_incident_reported = TRUE
AND organizational_oversight_notified = TRUE
AND incident_response_coordinated = TRUE
THEN compliance = TRUE
violation_severity = "None"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Providers comply with organizational security requirements | [RULE-01] |
| Providers comply with organizational privacy requirements | [RULE-01] |
| Providers employ organization-defined controls | [RULE-02] |
| Organizational oversight roles defined and documented | [RULE-03] |
| User roles and responsibilities defined and documented | [RULE-04] |
| Monitoring processes defined and employed | [RULE-05] |
| Ongoing compliance monitoring implemented | [RULE-07] |