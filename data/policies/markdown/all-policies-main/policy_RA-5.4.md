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
The organization SHALL identify information about systems that is discoverable through external reconnaissance and take defined corrective actions when such information poses security risks. This policy excludes intentionally discoverable information used for authorized deception capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid |
| Development/test systems | YES | Often overlooked but critical |
| Third-party hosted systems | YES | Where organization has control |
| Deception technologies | NO | Honeypots, honeynets excluded |
| Public-facing services | YES | High priority for assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Team | • Conduct regular reconnaissance assessments<br>• Monitor for exposed information<br>• Execute corrective actions |
| System Administrators | • Implement corrective measures<br>• Configure systems to minimize exposure<br>• Report discoverable information findings |
| Risk Management Team | • Define risk thresholds for discoverable information<br>• Approve corrective action plans<br>• Track remediation efforts |

## 4. RULES
[RULE-01] Organizations MUST conduct systematic assessments to identify discoverable information about systems at least quarterly and after significant system changes.
[VALIDATION] IF last_assessment_date > 90_days OR system_change_occurred = TRUE AND assessment_completed = FALSE THEN violation

[RULE-02] Corrective actions MUST be defined for each category of discoverable information that could aid adversaries in system reconnaissance or attack planning.
[VALIDATION] IF discoverable_info_category_identified = TRUE AND corrective_action_defined = FALSE THEN violation

[RULE-03] High-risk discoverable information MUST be remediated within 72 hours of confirmation, medium-risk within 30 days, and low-risk within 90 days.
[VALIDATION] IF risk_level = "high" AND remediation_time > 72_hours THEN critical_violation
[VALIDATION] IF risk_level = "medium" AND remediation_time > 30_days THEN violation
[VALIDATION] IF risk_level = "low" AND remediation_time > 90_days THEN violation

[RULE-04] Discoverable information assessments MUST include automated scanning, manual reconnaissance techniques, and open source intelligence gathering.
[VALIDATION] IF assessment_methods NOT CONTAINS ["automated_scanning", "manual_reconnaissance", "osint"] THEN violation

[RULE-05] All discoverable information findings and corrective actions MUST be documented and tracked through resolution.
[VALIDATION] IF finding_documented = FALSE OR corrective_action_tracked = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Discoverable Information Assessment - Systematic process for identifying exposed system information
- [PROC-02] Risk Classification - Categorizing discoverable information by potential impact
- [PROC-03] Corrective Action Response - Standardized remediation procedures by risk level
- [PROC-04] Reconnaissance Monitoring - Ongoing surveillance for newly exposed information

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving reconnaissance, major system deployments, significant infrastructure changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Exposed System Information]
IF system_information_discoverable = TRUE
AND risk_assessment_completed = TRUE
AND corrective_action_defined = TRUE
AND remediation_within_timeframe = TRUE
THEN compliance = TRUE

[SCENARIO-02: Delayed Remediation]
IF discoverable_info_risk = "high"
AND discovery_date + 72_hours < current_date
AND remediation_status = "incomplete"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Assessment]
IF last_discovery_assessment > 90_days
AND system_changes_occurred = TRUE
AND assessment_scheduled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Undocumented Findings]
IF discoverable_information_found = TRUE
AND finding_documented = FALSE
AND corrective_action_tracked = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Authorized Deception Technology]
IF system_type = "honeypot"
AND discoverable_information_intentional = TRUE
AND deception_capability_authorized = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information about the system is discoverable | RULE-01, RULE-04 |
| Corrective actions taken if information about the system is discoverable are defined | RULE-02, RULE-03 |
| Corrective actions are taken when information about the system is confirmed as discoverable | RULE-03, RULE-05 |