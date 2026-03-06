# POLICY: CA-8: Penetration Testing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CA-8 |
| NIST Control | CA-8: Penetration Testing |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | penetration testing, vulnerability assessment, security testing, adversary simulation, rules of engagement |

## 1. POLICY STATEMENT
The organization SHALL conduct penetration testing at defined frequencies on specified systems and system components to identify exploitable vulnerabilities and validate security controls. Penetration testing MUST be performed by qualified personnel using approved methodologies with established rules of engagement.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All internet-facing and critical internal systems |
| Development Systems | CONDITIONAL | When containing production-like data or configurations |
| Third-party Hosted Systems | YES | Where contractually permitted |
| Network Infrastructure | YES | Firewalls, routers, switches, wireless networks |
| Applications | YES | Web applications, APIs, mobile applications |
| Physical Security Controls | CONDITIONAL | When integrated with technical systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve penetration testing schedule and scope<br>• Review and act on critical findings<br>• Ensure adequate budget and resources |
| Security Architecture Team | • Define systems requiring penetration testing<br>• Establish rules of engagement<br>• Coordinate testing activities with operations |
| Penetration Testing Team | • Execute penetration tests per approved methodology<br>• Document findings and provide remediation guidance<br>• Maintain testing tools and techniques |
| System Owners | • Participate in rules of engagement development<br>• Provide system access and documentation<br>• Implement remediation actions |

## 4. RULES

[RULE-01] Penetration testing MUST be conducted annually for all internet-facing systems and every two years for critical internal systems.
[VALIDATION] IF system_classification = "internet-facing" AND last_pentest_date > 365_days THEN violation
[VALIDATION] IF system_classification = "critical_internal" AND last_pentest_date > 730_days THEN violation

[RULE-02] Penetration testing SHALL be performed by personnel with demonstrable skills and current security certifications (OSCP, GPEN, or equivalent).
[VALIDATION] IF penetration_tester_certified = FALSE OR certification_current = FALSE THEN violation

[RULE-03] Rules of engagement MUST be documented and approved by system owners and security leadership before testing begins.
[VALIDATION] IF rules_of_engagement_approved = FALSE OR system_owner_signoff = FALSE THEN critical_violation

[RULE-04] Penetration testing MUST include both automated vulnerability scanning and manual exploitation attempts.
[VALIDATION] IF automated_scanning = FALSE OR manual_testing = FALSE THEN violation

[RULE-05] Critical and high-severity findings MUST be remediated within 30 days and 90 days respectively.
[VALIDATION] IF finding_severity = "critical" AND remediation_time > 30_days THEN critical_violation
[VALIDATION] IF finding_severity = "high" AND remediation_time > 90_days THEN violation

[RULE-06] Penetration testing reports MUST be classified as confidential and distributed only to authorized personnel.
[VALIDATION] IF report_classification != "confidential" OR unauthorized_distribution = TRUE THEN violation

[RULE-07] Additional penetration testing MUST be conducted when transitioning to new technologies or after significant system changes.
[VALIDATION] IF technology_transition = TRUE OR major_system_change = TRUE AND additional_pentest_conducted = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Penetration Testing Methodology - Standardized approach including reconnaissance, vulnerability identification, exploitation, and reporting phases
- [PROC-02] Rules of Engagement Development - Process for defining scope, constraints, communication protocols, and emergency procedures
- [PROC-03] Finding Classification and Remediation - Severity rating system and remediation timelines
- [PROC-04] Penetration Tester Qualification - Requirements for internal and external testing personnel
- [PROC-05] Report Distribution and Handling - Secure distribution and storage of sensitive testing results

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Major security incidents, significant technology changes, regulatory updates, failed penetration tests

## 7. SCENARIO PATTERNS

[SCENARIO-01: Overdue External System Testing]
IF system_type = "internet-facing"
AND last_penetration_test > 365_days
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unqualified Testing Personnel]
IF penetration_test_conducted = TRUE
AND tester_certification = "none"
AND internal_tester = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Rules of Engagement]
IF penetration_test_scheduled = TRUE
AND rules_of_engagement_documented = FALSE
AND testing_start_date < 7_days
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Delayed Critical Finding Remediation]
IF finding_severity = "critical"
AND discovery_date > 35_days_ago
AND remediation_status = "open"
AND no_approved_extension = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Technology Transition Without Testing]
IF ipv6_deployment = TRUE
AND deployment_date > 90_days_ago
AND post_deployment_pentest = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Conduct penetration testing at defined frequency | RULE-01, RULE-07 |
| Use qualified personnel for testing | RULE-02 |
| Establish rules of engagement | RULE-03 |
| Include comprehensive testing methodology | RULE-04 |
| Remediate identified vulnerabilities | RULE-05 |
| Protect sensitive testing information | RULE-06 |
| Test during technology transitions | RULE-07 |