# POLICY: SA-9: External System Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9 |
| NIST Control | SA-9: External System Services |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external services, third-party providers, vendor management, service agreements, oversight, monitoring |

## 1. POLICY STATEMENT
All external system service providers MUST comply with organizational security and privacy requirements and employ organization-defined controls. The organization SHALL establish documented oversight roles and responsibilities for external services and implement ongoing monitoring processes to verify provider compliance with security and privacy controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud Service Providers | YES | All IaaS, PaaS, SaaS providers |
| Managed Security Services | YES | SOC, SIEM, incident response providers |
| Software Vendors | YES | Applications processing organizational data |
| Business Partners | YES | Systems with data sharing agreements |
| Contractors | YES | Remote access to organizational systems |
| Internal IT Services | NO | Covered under separate controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Vendor Management Office | • Maintain vendor risk assessments<br>• Negotiate security requirements in contracts<br>• Monitor SLA compliance |
| CISO | • Define security requirements for external providers<br>• Approve high-risk vendor relationships<br>• Oversee compliance monitoring program |
| Data Protection Officer | • Define privacy requirements for external providers<br>• Review data processing agreements<br>• Monitor privacy compliance |
| Business Unit Owners | • Identify external service needs<br>• Ensure business requirements align with security controls<br>• Report compliance issues |

## 4. RULES
[RULE-01] External service providers MUST comply with all organizational security and privacy requirements as defined in approved vendor security standards and contractual agreements.
[VALIDATION] IF provider_compliance_status ≠ "compliant" AND contract_active = TRUE THEN violation

[RULE-02] All external service contracts MUST include organization-defined security controls, measurable performance outcomes, and remediation requirements for non-compliance instances.
[VALIDATION] IF contract_security_controls = "undefined" OR sla_measurable_outcomes = FALSE THEN violation

[RULE-03] Organizational oversight roles and user responsibilities for external system services MUST be documented and maintained in the vendor management system.
[VALIDATION] IF oversight_roles_documented = FALSE OR user_responsibilities_documented = FALSE THEN violation

[RULE-04] External service provider control compliance MUST be monitored on an ongoing basis using organization-defined processes, methods, and techniques with quarterly formal reviews.
[VALIDATION] IF last_compliance_review > 90_days AND provider_risk_level ≥ "medium" THEN violation

[RULE-05] External providers MUST provide evidence of control implementation through third-party assessments, certifications, or audit reports updated within the past 12 months.
[VALIDATION] IF assessment_evidence_age > 365_days OR assessment_evidence = "none" THEN violation

[RULE-06] Chain of trust documentation MUST be established and maintained for all external service relationships, including sub-processor arrangements.
[VALIDATION] IF trust_relationship_documented = FALSE OR subprocessor_chain_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Vendor Security Assessment - Risk evaluation before contract execution
- [PROC-02] Contract Security Review - Legal and security review of service agreements
- [PROC-03] Ongoing Compliance Monitoring - Quarterly compliance verification process
- [PROC-04] Incident Response Coordination - Joint incident handling with external providers
- [PROC-05] Chain of Trust Validation - Sub-processor security verification process

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New regulatory requirements, significant security incidents involving external providers, changes to organizational risk tolerance

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Provider Compliance Gap]
IF provider_type = "cloud_service"
AND soc2_report_age > 365_days
AND data_classification ≥ "confidential"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unmonitored High-Risk Vendor]
IF provider_risk_level = "high"
AND last_compliance_review > 90_days
AND contract_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Subprocessor Documentation]
IF subprocessors_exist = TRUE
AND subprocessor_security_documentation = "incomplete"
AND data_processing_scope = "personal_data"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Adequate Low-Risk Vendor Management]
IF provider_risk_level = "low"
AND contract_security_requirements = "defined"
AND last_compliance_review ≤ 180_days
AND sla_compliance = "meeting_targets"
THEN compliance = TRUE

[SCENARIO-05: Emergency Service Activation]
IF service_activation_type = "emergency"
AND temporary_approval_duration ≤ 30_days
AND security_assessment_scheduled = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Providers comply with organizational security requirements | [RULE-01] |
| Providers comply with organizational privacy requirements | [RULE-01] |
| Providers employ organization-defined controls | [RULE-02] |
| Organizational oversight roles defined and documented | [RULE-03] |
| User roles and responsibilities defined and documented | [RULE-03] |
| Monitoring processes defined and employed | [RULE-04] |
| Ongoing compliance monitoring implemented | [RULE-04], [RULE-05] |