# POLICY: SA-4.3: Development Methods, Techniques, and Practices

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-4.3 |
| NIST Control | SA-4.3: Development Methods, Techniques, and Practices |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | SDLC, development lifecycle, systems engineering, software development, quality control, vendor management, acquisition |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services acquired by the organization MUST demonstrate the use of a comprehensive system development life cycle (SDLC) process that includes defined systems engineering methods, approved software development practices, and established quality control processes. This requirement ensures transparency and reduces vulnerabilities through state-of-the-practice development methodologies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External System Developers | YES | All contracted development work |
| System Component Vendors | YES | Components integrated into organizational systems |
| Service Providers | YES | Custom development services |
| Internal Development Teams | YES | When acting as system developers |
| COTS Products | CONDITIONAL | When customization/integration services included |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Procurement Officer | • Ensure SDLC requirements in all development contracts<br>• Validate developer SDLC documentation<br>• Monitor compliance throughout acquisition lifecycle |
| CISO | • Define approved development methodologies<br>• Review and approve SDLC processes<br>• Oversee security engineering method requirements |
| System Owner | • Specify system-specific SDLC requirements<br>• Review developer SDLC demonstrations<br>• Validate integration of security/privacy engineering |

## 4. RULES
[RULE-01] All system developers MUST demonstrate use of a documented SDLC process that includes defined systems engineering methods before contract award.
[VALIDATION] IF developer_sdlc_documented = FALSE OR systems_engineering_methods = "undefined" THEN contract_award_blocked

[RULE-02] Developer SDLC processes MUST include organizationally-approved software development methods and coding standards.
[VALIDATION] IF software_dev_methods NOT IN approved_methods_list THEN compliance_violation

[RULE-03] Quality control processes MUST be integrated throughout the developer's SDLC with documented testing, evaluation, and validation techniques.
[VALIDATION] IF quality_control_processes = "undefined" OR testing_methods = "unspecified" THEN major_violation

[RULE-04] Developers MUST provide transparency documentation detailing their systems security and privacy engineering methods within 30 days of contract execution.
[VALIDATION] IF security_privacy_methods_doc = FALSE AND days_since_contract > 30 THEN compliance_violation

[RULE-05] SDLC process demonstrations MUST be updated and re-validated annually or upon significant methodology changes.
[VALIDATION] IF last_sdlc_validation > 365_days OR methodology_change = TRUE AND revalidation = FALSE THEN review_required

## 5. REQUIRED PROCEDURES
- [PROC-01] SDLC Requirements Definition - Establish minimum SDLC standards for each acquisition type
- [PROC-02] Developer SDLC Assessment - Evaluate and validate developer SDLC processes
- [PROC-03] SDLC Monitoring and Oversight - Ongoing verification of SDLC compliance during development
- [PROC-04] SDLC Documentation Review - Review and approve developer methodology documentation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Major acquisition failures, security incidents related to development practices, changes in organizational development standards

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Development Contract]
IF contract_type = "system_development"
AND developer_sdlc_demonstration = "completed"
AND systems_engineering_methods = "defined"
AND software_dev_methods IN approved_list
THEN compliance = TRUE

[SCENARIO-02: Missing Quality Control Documentation]
IF developer_contract = "active"
AND quality_control_processes = "undocumented"
AND contract_days_active > 30
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-03: COTS with Custom Development]
IF product_type = "COTS"
AND customization_services = TRUE
AND vendor_sdlc_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Annual SDLC Revalidation]
IF developer_relationship = "ongoing"
AND last_sdlc_validation > 365_days
AND revalidation_completed = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Security Engineering Method Changes]
IF security_engineering_methods = "changed"
AND change_notification_provided = TRUE
AND updated_documentation_received = TRUE
AND approval_status = "pending"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer demonstrates SDLC with defined systems engineering methods | [RULE-01] |
| Developer demonstrates approved software development methods | [RULE-02] |
| Developer demonstrates quality control processes | [RULE-03] |
| Transparency in development methodologies provided | [RULE-04] |
| Ongoing validation of SDLC processes | [RULE-05] |