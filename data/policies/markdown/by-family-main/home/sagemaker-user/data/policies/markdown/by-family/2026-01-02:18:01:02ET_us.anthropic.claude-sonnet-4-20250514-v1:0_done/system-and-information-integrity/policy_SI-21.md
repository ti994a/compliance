# POLICY: SI-21: Information Refresh

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-21 |
| NIST Control | SI-21: Information Refresh |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | information refresh, data retention, on-demand generation, data deletion, information lifecycle |

## 1. POLICY STATEMENT
The organization SHALL refresh information at defined frequencies or generate information on demand and delete it when no longer needed to minimize exposure to adversaries. Information MUST NOT be retained longer than necessary to support organizational missions or business functions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and hybrid environments |
| Temporary data files | YES | Generated during processing operations |
| Cached information | YES | Application and system caches |
| Log files | YES | Security, audit, and application logs |
| Backup data | YES | Subject to retention schedules |
| PII/sensitive data | YES | Enhanced requirements apply |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Define information refresh frequencies<br>• Approve retention schedules<br>• Validate business requirements for data retention |
| System Administrator | • Implement automated refresh mechanisms<br>• Configure on-demand generation systems<br>• Execute deletion procedures |
| Security Team | • Monitor compliance with refresh schedules<br>• Validate secure deletion methods<br>• Assess risks of extended retention |

## 4. RULES

[RULE-01] Organizations MUST define specific information types requiring refresh and establish maximum retention periods for each type.
[VALIDATION] IF information_type_defined = FALSE OR retention_period_undefined = TRUE THEN violation

[RULE-02] Information refresh MUST occur at frequencies not exceeding the defined maximum retention periods for each information type.
[VALIDATION] IF current_date - last_refresh_date > max_retention_period THEN violation

[RULE-03] On-demand information generation systems MUST automatically delete generated information within 24 hours of creation unless actively in use.
[VALIDATION] IF generation_type = "on-demand" AND creation_date + 24_hours < current_date AND active_use = FALSE THEN violation

[RULE-04] PII and sensitive information MUST be refreshed at frequencies not exceeding 90 days unless specific business justification exists.
[VALIDATION] IF data_classification IN ["PII", "sensitive"] AND last_refresh > 90_days AND business_justification = FALSE THEN violation

[RULE-05] Automated refresh mechanisms MUST be implemented for all defined information types with retention periods less than 365 days.
[VALIDATION] IF retention_period < 365_days AND automation_implemented = FALSE THEN violation

[RULE-06] Information deletion MUST use approved secure deletion methods that prevent data recovery.
[VALIDATION] IF deletion_method NOT IN approved_methods THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Information Classification and Retention Schedule - Define information types and refresh frequencies
- [PROC-02] Automated Refresh Implementation - Configure and maintain automated refresh systems
- [PROC-03] On-Demand Generation Management - Implement and monitor on-demand data generation
- [PROC-04] Secure Deletion Verification - Validate proper deletion of refreshed information

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Data breach incidents, regulatory changes, system architecture changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Expired Temporary Files]
IF file_type = "temporary"
AND creation_date + retention_period < current_date
AND file_exists = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: On-Demand Data Cleanup]
IF generation_method = "on-demand"
AND creation_timestamp + 24_hours < current_timestamp
AND active_sessions = 0
AND data_deleted = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-03: PII Refresh Overdue]
IF data_contains_pii = TRUE
AND last_refresh_date + 90_days < current_date
AND business_justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Automated Refresh Failure]
IF retention_period < 365_days
AND automated_refresh_configured = FALSE
AND manual_refresh_frequency > retention_period
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant On-Demand Processing]
IF generation_method = "on-demand"
AND data_deleted_when_not_needed = TRUE
AND secure_deletion_method_used = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information types for refresh are defined | [RULE-01] |
| Information is refreshed at defined frequencies | [RULE-02] |
| On-demand information is properly managed | [RULE-03] |
| Sensitive data refresh requirements | [RULE-04] |
| Automated refresh implementation | [RULE-05] |
| Secure deletion methods | [RULE-06] |