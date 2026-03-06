# POLICY: PM-32: Purposing

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-32 |
| NIST Control | PM-32: Purposing |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | purposing, mission-essential, resource analysis, intended use, threat exposure |

## 1. POLICY STATEMENT
The organization SHALL analyze systems and system components supporting mission-essential services to ensure information resources are used consistent with their intended purpose. Systems MUST NOT be used for services or functions outside the scope of their intended mission or business functions without proper authorization and risk assessment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Mission-essential systems | YES | Primary focus of analysis |
| Supporting system components | YES | Components that enable mission-essential functions |
| Business applications | CONDITIONAL | Only if supporting mission-essential services |
| Development/test systems | CONDITIONAL | If processing mission-essential data |
| Third-party hosted systems | YES | If supporting mission-essential functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Define intended system purpose and scope<br>• Monitor system usage patterns<br>• Report unauthorized usage |
| Security Operations | • Conduct quarterly purposing analysis<br>• Identify usage anomalies<br>• Document findings and recommendations |
| Risk Management | • Assess risk of purpose drift<br>• Approve exceptions to intended use<br>• Update risk assessments based on findings |

## 4. RULES
[RULE-01] Mission-essential systems and components MUST have documented intended purposes that clearly define authorized services and functions.
[VALIDATION] IF system_classification = "mission-essential" AND intended_purpose_documented = FALSE THEN violation

[RULE-02] Organizations SHALL conduct purposing analysis of mission-essential systems at least quarterly to identify usage inconsistent with intended purpose.
[VALIDATION] IF last_purposing_analysis > 90_days AND system_type = "mission-essential" THEN violation

[RULE-03] Systems MUST NOT be used for services or functions outside their documented intended purpose without written authorization and updated risk assessment.
[VALIDATION] IF unauthorized_usage_detected = TRUE AND written_authorization = FALSE THEN violation

[RULE-04] Purpose drift findings SHALL be documented and remediated within 30 days for high-risk exposures and 90 days for moderate-risk exposures.
[VALIDATION] IF finding_risk_level = "high" AND remediation_time > 30_days THEN critical_violation
[VALIDATION] IF finding_risk_level = "moderate" AND remediation_time > 90_days THEN violation

[RULE-05] Mission-essential system inventory MUST be maintained and updated within 30 days of any changes to system purpose or scope.
[VALIDATION] IF system_purpose_change_date < (current_date - 30_days) AND inventory_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Mission-Essential System Identification - Process for defining and documenting systems supporting mission-essential functions
- [PROC-02] Quarterly Purposing Analysis - Systematic review of system usage against intended purpose
- [PROC-03] Purpose Drift Investigation - Process for investigating and documenting unauthorized system usage
- [PROC-04] Exception Management - Process for authorizing and managing approved deviations from intended purpose

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, security incidents involving purpose drift, organizational mission changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Service Addition]
IF system_classification = "mission-essential"
AND new_service_added = TRUE
AND service_authorization_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Overdue Purposing Analysis]
IF system_type = "mission-essential"
AND last_analysis_date > 90_days_ago
AND analysis_exemption = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Approved Purpose Expansion]
IF system_usage_change = TRUE
AND written_authorization = TRUE
AND risk_assessment_updated = TRUE
AND inventory_updated = TRUE
THEN compliance = TRUE

[SCENARIO-04: High-Risk Purpose Drift]
IF unauthorized_usage_detected = TRUE
AND risk_level = "high"
AND remediation_completed = FALSE
AND days_since_detection > 30
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Missing System Documentation]
IF system_classification = "mission-essential"
AND intended_purpose_documented = FALSE
AND system_age > 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Systems supporting mission-essential services are defined | [RULE-01], [RULE-05] |
| Analysis ensures resources used consistent with intended purpose | [RULE-02], [RULE-03] |
| Purpose drift is identified and remediated | [RULE-04] |
| System inventory is maintained | [RULE-05] |