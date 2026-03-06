# POLICY: CA-8.3: Facility Penetration Testing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CA-8.3 |
| NIST Control | CA-8.3: Facility Penetration Testing |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | penetration testing, physical security, facility access, vulnerability assessment, physical controls |

## 1. POLICY STATEMENT
The organization SHALL conduct regular penetration testing of physical access points to identify vulnerabilities in facility security controls. All penetration tests MUST follow a defined process with established frequency and include both announced and unannounced testing scenarios to validate the effectiveness of physical security measures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Primary facilities | YES | Data centers, corporate offices, secure areas |
| Remote offices | YES | If housing critical systems or data |
| Third-party facilities | CONDITIONAL | Only facilities under organizational control |
| Temporary locations | NO | Unless specified by risk assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Define penetration testing frequency<br>• Coordinate testing activities<br>• Review and approve test plans |
| Security Assessment Team | • Execute penetration tests<br>• Document vulnerabilities<br>• Provide remediation recommendations |
| Facility Operations | • Support testing activities<br>• Implement corrective actions<br>• Maintain physical security controls |

## 4. RULES
[RULE-01] Organizations MUST define and document the frequency for conducting facility penetration testing, with testing occurring at least annually for high-risk facilities and biennially for standard facilities.
[VALIDATION] IF facility_risk_level = "high" AND last_test_date > 365_days THEN violation
[VALIDATION] IF facility_risk_level = "standard" AND last_test_date > 730_days THEN violation

[RULE-02] Penetration testing MUST include both announced and unannounced attempts to bypass or circumvent physical access controls at facility entry points.
[VALIDATION] IF test_type NOT IN ["announced", "unannounced"] THEN violation
[VALIDATION] IF annual_tests_completed AND (announced_tests = 0 OR unannounced_tests = 0) THEN violation

[RULE-03] All facility penetration tests MUST target physical access points including perimeter controls, entry doors, visitor management systems, and secure area access controls.
[VALIDATION] IF test_scope NOT INCLUDES ["perimeter", "entry_points", "visitor_management", "secure_areas"] THEN incomplete_coverage

[RULE-04] Penetration test results MUST be documented within 30 days of test completion and include identified vulnerabilities, risk ratings, and remediation recommendations.
[VALIDATION] IF test_completion_date + 30_days < current_date AND report_status != "completed" THEN violation

[RULE-05] Critical and high-risk vulnerabilities identified during facility penetration testing MUST be remediated within 90 days of discovery.
[VALIDATION] IF vulnerability_risk IN ["critical", "high"] AND discovery_date + 90_days < current_date AND status != "remediated" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Facility Penetration Test Planning - Define scope, methodology, and rules of engagement
- [PROC-02] Physical Access Point Assessment - Execute testing against entry controls and barriers  
- [PROC-03] Vulnerability Reporting and Tracking - Document findings and monitor remediation progress
- [PROC-04] Test Results Review and Approval - Validate findings and approve remediation plans

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after significant facility changes
- Triggering events: Security incidents, facility modifications, regulatory changes, failed assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Overdue High-Risk Facility Testing]
IF facility_classification = "high_risk"
AND last_penetration_test > 365_days_ago
AND no_approved_extension = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Test Coverage]
IF penetration_test_completed = TRUE
AND test_scope_missing = ["visitor_management"]
AND facility_has_visitors = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unaddressed Critical Vulnerability]
IF vulnerability_severity = "critical"
AND days_since_discovery > 90
AND remediation_status != "completed"
AND approved_exception = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Test Documentation]
IF penetration_test_completed = TRUE
AND test_completion_date + 30_days < current_date
AND formal_report_exists = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Annual Testing Cycle]
IF facility_risk_level = "standard"
AND last_test_date <= 730_days_ago
AND test_included_announced = TRUE
AND test_included_unannounced = TRUE
AND report_completed_timely = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Define penetration testing frequency | RULE-01 |
| Include announced and unannounced testing | RULE-02 |
| Test physical access points comprehensively | RULE-03 |
| Document test results timely | RULE-04 |
| Remediate identified vulnerabilities | RULE-05 |