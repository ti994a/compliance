# POLICY: RA-5.4: Discoverable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-5.4 |
| NIST Control | RA-5.4: Discoverable Information |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | discoverable information, reconnaissance, information exposure, corrective actions, vulnerability assessment |

## 1. POLICY STATEMENT
The organization MUST identify information about systems that could be discovered by adversaries through passive reconnaissance and take immediate corrective actions when such information is confirmed as discoverable. This policy excludes intentionally discoverable information used for authorized deception capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, hybrid, and on-premises systems |
| Third-party hosted systems | YES | Where organization has control over exposed information |
| Deception/honeypot systems | NO | Intentionally discoverable information excluded |
| Development/test systems | YES | Often contain discoverable information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Team | • Conduct regular discovery assessments<br>• Monitor for newly discoverable information<br>• Execute corrective actions |
| System Administrators | • Implement corrective measures<br>• Configure systems to minimize information exposure<br>• Report discoverable information findings |
| Risk Management Team | • Assess risk impact of discoverable information<br>• Prioritize corrective actions<br>• Track remediation efforts |

## 4. RULES
[RULE-01] Organizations MUST conduct discoverable information assessments at least quarterly and after significant system changes.
[VALIDATION] IF last_assessment_date > 90_days OR significant_change = TRUE AND assessment_completed = FALSE THEN violation

[RULE-02] All discoverable information findings MUST be documented with risk ratings within 48 hours of discovery.
[VALIDATION] IF finding_discovered = TRUE AND documentation_time > 48_hours THEN violation

[RULE-03] High-risk discoverable information MUST have corrective actions initiated within 24 hours and completed within 7 days.
[VALIDATION] IF risk_level = "HIGH" AND corrective_action_start > 24_hours THEN critical_violation

[RULE-04] Medium-risk discoverable information MUST have corrective actions completed within 30 days.
[VALIDATION] IF risk_level = "MEDIUM" AND corrective_action_completion > 30_days THEN violation

[RULE-05] All corrective actions MUST be verified for effectiveness within 5 business days of completion.
[VALIDATION] IF corrective_action_completed = TRUE AND verification_time > 5_business_days THEN violation

[RULE-06] Discoverable information findings and corrective actions MUST be reported to senior management monthly.
[VALIDATION] IF monthly_report_submitted = FALSE AND month_end_passed = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Discoverable Information Assessment - Systematic evaluation of publicly accessible system information
- [PROC-02] Risk Classification - Standardized approach to rating discoverable information risk
- [PROC-03] Corrective Action Implementation - Process for removing or mitigating discoverable information
- [PROC-04] Effectiveness Verification - Validation that corrective actions successfully addressed findings

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving reconnaissance, significant architecture changes, new system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Exposed System Information]
IF system_information_publicly_accessible = TRUE
AND information_sensitivity = "HIGH"
AND corrective_action_initiated = FALSE
AND discovery_time > 24_hours
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Delayed Risk Assessment]
IF discoverable_information_found = TRUE
AND risk_assessment_completed = FALSE
AND finding_age > 48_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incomplete Corrective Action]
IF corrective_action_required = TRUE
AND risk_level = "MEDIUM"
AND action_completion_time > 30_days
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Verification]
IF corrective_action_completed = TRUE
AND effectiveness_verification = FALSE
AND completion_date > 5_business_days
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Authorized Deception System]
IF system_type = "honeypot"
AND information_intentionally_discoverable = TRUE
AND proper_authorization = TRUE
THEN compliance = TRUE
violation_severity = "None"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information about the system is discoverable | [RULE-01], [RULE-02] |
| Corrective actions taken if information about the system is discoverable are defined | [RULE-03], [RULE-04] |
| Actions are taken when information about the system is confirmed as discoverable | [RULE-05], [RULE-06] |