# POLICY: SA-11.5: Penetration Testing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.5 |
| NIST Control | SA-11.5: Penetration Testing |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | penetration testing, developer testing, vulnerability assessment, security testing, system acquisition |

## 1. POLICY STATEMENT
All system, system component, and system service developers MUST perform penetration testing at organization-defined levels of rigor and under specified constraints before deployment. Penetration testing SHALL be conducted to discover vulnerabilities resulting from implementation errors, configuration faults, or operational weaknesses.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All internally developed systems |
| Third-party Vendors | YES | Contract-mandated testing required |
| COTS Products | CONDITIONAL | When customization exceeds 25% |
| Cloud Services | YES | Vendor-provided testing evidence required |
| Legacy Systems | YES | During major updates or annual review |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define penetration testing standards and rigor levels<br>• Approve testing methodologies and constraints<br>• Review and approve testing results |
| Development Manager | • Ensure developer compliance with testing requirements<br>• Coordinate testing activities with security team<br>• Validate remediation of identified vulnerabilities |
| Security Architect | • Define technical testing requirements<br>• Review testing plans and methodologies<br>• Validate testing scope and depth |

## 4. RULES
[RULE-01] Developers MUST perform penetration testing on all systems, system components, and services before production deployment.
[VALIDATION] IF system_type IN ["critical", "high_impact"] AND penetration_test_completed = FALSE THEN critical_violation

[RULE-02] Penetration testing MUST include white-box, gray-box, or black-box methodologies as defined by system criticality and risk level.
[VALIDATION] IF system_criticality = "high" AND testing_methodology NOT IN ["white-box", "gray-box"] THEN violation

[RULE-03] Testing breadth MUST cover all system interfaces, APIs, and user-accessible functions for high-impact systems.
[VALIDATION] IF system_impact = "high" AND interface_coverage < 100% THEN violation

[RULE-04] Testing depth MUST include automated vulnerability scanning AND manual testing by qualified security professionals.
[VALIDATION] IF testing_depth NOT INCLUDES ["automated_scanning", "manual_testing"] THEN violation

[RULE-05] All identified vulnerabilities rated Medium or higher MUST be remediated before production deployment.
[VALIDATION] IF vulnerability_severity IN ["medium", "high", "critical"] AND remediation_status = "open" THEN violation

[RULE-06] Penetration testing constraints MUST protect personally identifiable information and prevent system disruption.
[VALIDATION] IF pii_exposure = TRUE OR system_disruption = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Developer Penetration Testing Standards - Defines methodology, tools, and rigor requirements
- [PROC-02] Vulnerability Remediation Process - Establishes timelines and validation for vulnerability fixes
- [PROC-03] Third-party Testing Validation - Process for reviewing vendor-provided testing evidence
- [PROC-04] PII Protection During Testing - Safeguards for handling sensitive data during assessments

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major security incidents, regulatory changes, significant system modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical System Deployment]
IF system_criticality = "high"
AND penetration_test_completed = TRUE
AND critical_vulnerabilities = 0
AND medium_vulnerabilities ≤ 2
THEN compliance = TRUE

[SCENARIO-02: Vendor Testing Evidence]
IF vendor_type = "third_party"
AND penetration_test_provided = TRUE
AND test_methodology = "inadequate"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Legacy System Exception]
IF system_age > 5_years
AND penetration_test_waiver = TRUE
AND compensating_controls = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: PII Exposure During Testing]
IF penetration_test_active = TRUE
AND pii_data_accessed = TRUE
AND privacy_safeguards = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Incomplete Vulnerability Remediation]
IF penetration_test_completed = TRUE
AND high_severity_vulnerabilities > 0
AND deployment_approved = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer penetration testing requirement | [RULE-01] |
| Testing breadth definition | [RULE-03] |
| Testing depth definition | [RULE-04] |
| Testing constraints definition | [RULE-06] |
| Vulnerability remediation | [RULE-05] |