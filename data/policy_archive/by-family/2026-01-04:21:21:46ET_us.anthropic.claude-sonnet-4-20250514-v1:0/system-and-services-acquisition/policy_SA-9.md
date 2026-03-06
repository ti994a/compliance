```markdown
# POLICY: SA-9: External System Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9 |
| NIST Control | SA-9: External System Services |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external services, third-party, vendor management, service providers, contracts, SLA, oversight, monitoring |

## 1. POLICY STATEMENT
All external system service providers MUST comply with organizational security and privacy requirements and employ defined security controls. The organization SHALL establish documented oversight roles and implement ongoing monitoring processes to ensure continuous compliance by external service providers.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud Service Providers | YES | All IaaS, PaaS, SaaS providers |
| Managed Security Services | YES | SOC, incident response, vulnerability scanning |
| Software Vendors | YES | Applications processing organizational data |
| Outsourced IT Services | YES | Help desk, infrastructure management |
| Data Processing Services | YES | Analytics, backup, archival services |
| Internal Services | NO | Services provided by organizational units |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Vendor Management Office | • Maintain approved vendor list<br>• Coordinate contract security requirements<br>• Track compliance status |
| Information Security Team | • Define security requirements for external services<br>• Review vendor security assessments<br>• Monitor ongoing compliance |
| Privacy Office | • Define privacy requirements<br>• Review data processing agreements<br>• Assess privacy impact |
| Service Owners | • Document service dependencies<br>• Monitor service performance<br>• Report compliance issues |

## 4. RULES
[RULE-01] External service providers MUST demonstrate compliance with all applicable organizational security and privacy requirements before service commencement.
[VALIDATION] IF provider_status = "new" AND security_compliance_verified = FALSE THEN violation

[RULE-02] All external service agreements SHALL include specific security control requirements, performance metrics, and remediation procedures.
[VALIDATION] IF contract_signed = TRUE AND security_requirements_documented = FALSE THEN violation

[RULE-03] External service providers MUST provide security assessment documentation within 90 days of contract execution and annually thereafter.
[VALIDATION] IF days_since_last_assessment > 365 THEN violation

[RULE-04] Organizational oversight roles and responsibilities for each external service SHALL be documented and assigned to specific personnel.
[VALIDATION] IF external_service_active = TRUE AND oversight_role_assigned = FALSE THEN violation

[RULE-05] External service compliance MUST be monitored using defined processes with documented review at least quarterly.
[VALIDATION] IF days_since_last_compliance_review > 90 THEN violation

[RULE-06] Non-compliance incidents by external service providers MUST be documented and remediated according to service level agreement timelines.
[VALIDATION] IF noncompliance_detected = TRUE AND remediation_time > SLA_timeline THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Service Provider Assessment - Security and privacy evaluation before engagement
- [PROC-02] Contract Security Requirements - Standard security clauses and control specifications
- [PROC-03] Ongoing Compliance Monitoring - Quarterly reviews and continuous monitoring processes
- [PROC-04] Incident Response Coordination - Procedures for security incidents involving external services
- [PROC-05] Service Level Agreement Management - Performance monitoring and remediation tracking

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New regulatory requirements, significant security incidents, contract renewals, technology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Cloud Service Onboarding]
IF service_type = "cloud"
AND contract_status = "pending"
AND security_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Expired Vendor Assessment]
IF vendor_assessment_date < (current_date - 365_days)
AND service_status = "active"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Oversight Assignment]
IF external_service_count > 0
AND assigned_oversight_personnel = NULL
AND service_criticality = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: SLA Violation Response]
IF noncompliance_incident = TRUE
AND incident_age > SLA_response_time
AND escalation_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Monitoring Process]
IF compliance_review_frequency <= 90_days
AND oversight_documented = TRUE
AND vendor_assessments_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Providers comply with organizational security requirements | [RULE-01], [RULE-03] |
| Providers comply with organizational privacy requirements | [RULE-01], [RULE-03] |
| Providers employ defined security controls | [RULE-02], [RULE-03] |
| Organizational oversight roles defined and documented | [RULE-04] |
| User roles and responsibilities defined and documented | [RULE-04] |
| Monitoring processes defined and employed | [RULE-05], [RULE-06] |
```