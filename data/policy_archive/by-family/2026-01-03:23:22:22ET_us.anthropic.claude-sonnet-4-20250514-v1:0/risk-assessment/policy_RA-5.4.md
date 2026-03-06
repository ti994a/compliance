# POLICY: RA-5.4: Discoverable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-5.4 |
| NIST Control | RA-5.4: Discoverable Information |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | discoverable information, reconnaissance, information disclosure, corrective actions, vulnerability assessment |

## 1. POLICY STATEMENT
The organization SHALL identify information about systems that is discoverable through public sources or reconnaissance activities and implement corrective actions when such information poses security risks. This policy excludes intentionally exposed information used for deception capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and on-premises |
| Public-facing services | YES | Web applications, APIs, DNS records |
| Internal systems | YES | When discoverable externally |
| Deception technologies | NO | Honeypots and honeynets excluded |
| Third-party services | CONDITIONAL | When containing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center | • Conduct regular reconnaissance assessments<br>• Monitor for discoverable information<br>• Execute corrective actions |
| System Owners | • Report discoverable information findings<br>• Implement approved corrective measures<br>• Maintain system configuration baselines |
| Risk Management Team | • Assess risk impact of discoverable information<br>• Approve corrective action plans<br>• Track remediation efforts |

## 4. RULES
[RULE-01] Organizations MUST conduct discoverable information assessments at least quarterly using automated tools and manual reconnaissance techniques.
[VALIDATION] IF last_assessment_date > 90_days THEN violation

[RULE-02] Corrective actions MUST be initiated within 72 hours for high-risk discoverable information and within 30 days for moderate-risk findings.
[VALIDATION] IF risk_level = "high" AND corrective_action_start > 72_hours THEN critical_violation
[VALIDATION] IF risk_level = "moderate" AND corrective_action_start > 30_days THEN violation

[RULE-03] Discoverable information assessments MUST include DNS enumeration, web application fingerprinting, search engine reconnaissance, and social media monitoring.
[VALIDATION] IF assessment_scope NOT includes ["dns", "web_fingerprint", "search_engine", "social_media"] THEN violation

[RULE-04] High-risk discoverable information SHALL be documented in the risk register within 24 hours of identification.
[VALIDATION] IF risk_level = "high" AND risk_register_entry_time > 24_hours THEN violation

[RULE-05] Corrective actions MUST be validated through follow-up assessments within 7 days of implementation.
[VALIDATION] IF corrective_action_completed = TRUE AND validation_assessment_time > 7_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Discoverable Information Assessment - Quarterly systematic evaluation of externally visible system information
- [PROC-02] Risk Classification - Methodology for categorizing discoverable information risk levels
- [PROC-03] Corrective Action Implementation - Standard response procedures for different risk categories
- [PROC-04] Validation Testing - Post-remediation verification processes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving reconnaissance, new system deployments, significant infrastructure changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Exposed Configuration Files]
IF discoverable_info_type = "configuration_files"
AND contains_credentials = TRUE
AND corrective_action_time > 72_hours
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Detailed Error Messages]
IF discoverable_info_type = "error_messages"
AND reveals_system_details = TRUE
AND risk_assessment_completed = TRUE
AND corrective_action_time <= 30_days
THEN compliance = TRUE

[SCENARIO-03: Employee Information Disclosure]
IF discoverable_info_type = "personnel_data"
AND source = "social_media"
AND risk_level = "moderate"
AND risk_register_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Intentional Honeypot Exposure]
IF discoverable_info_type = "system_details"
AND system_type = "honeypot"
AND deception_capability = TRUE
THEN compliance = TRUE

[SCENARIO-05: Overdue Assessment]
IF last_assessment_date > 90_days
AND system_status = "production"
AND assessment_scheduled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information about the system is discoverable | RULE-01, RULE-03 |
| Corrective actions taken if information is discoverable are defined | RULE-02, PROC-03 |
| Actions are taken when information is confirmed as discoverable | RULE-02, RULE-04, RULE-05 |