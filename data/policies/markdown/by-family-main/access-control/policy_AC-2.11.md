# POLICY: AC-2.11: Usage Conditions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-2.11 |
| NIST Control | AC-2.11: Usage Conditions |
| Version | 1.0 |
| Owner | Identity and Access Management Team |
| Keywords | usage conditions, account restrictions, time-based access, least privilege, account monitoring |

## 1. POLICY STATEMENT
All system accounts SHALL have defined usage conditions that specify circumstances under which the account may be used. These conditions MUST be technically enforced by system controls and monitored for violations to ensure least privilege and increase user accountability.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All system accounts | YES | Includes user, service, and administrative accounts |
| Shared accounts | YES | Require additional usage restrictions |
| Emergency accounts | YES | Temporary conditions with automatic expiration |
| Guest accounts | YES | Strict time and resource limitations |
| External contractor accounts | YES | Project-specific usage conditions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IAM Team | • Define standard usage conditions for account types<br>• Configure technical enforcement mechanisms<br>• Monitor usage condition violations |
| System Administrators | • Implement usage conditions in system configurations<br>• Respond to usage condition violation alerts<br>• Maintain usage condition documentation |
| Security Operations | • Monitor account usage patterns<br>• Investigate usage condition violations<br>• Report compliance metrics |

## 4. RULES
[RULE-01] All system accounts MUST have documented usage conditions that specify at least one restriction parameter (time, location, duration, or resource access).
[VALIDATION] IF account_exists = TRUE AND usage_conditions_documented = FALSE THEN violation

[RULE-02] Usage conditions MUST be technically enforced through system controls and SHALL NOT rely solely on administrative procedures.
[VALIDATION] IF usage_conditions_defined = TRUE AND technical_enforcement = FALSE THEN violation

[RULE-03] Time-based usage conditions MUST restrict access to specific days of week, hours of day, or maximum session duration as appropriate for the account type.
[VALIDATION] IF time_restrictions_required = TRUE AND (day_restrictions = NULL AND hour_restrictions = NULL AND session_duration = NULL) THEN violation

[RULE-04] Usage condition violations MUST generate automated alerts within 15 minutes of detection.
[VALIDATION] IF usage_violation_detected = TRUE AND alert_time > 15_minutes THEN violation

[RULE-05] Privileged accounts MUST have more restrictive usage conditions than standard user accounts, including time limitations and approval requirements.
[VALIDATION] IF account_privilege_level = "high" AND usage_restrictions <= standard_user_restrictions THEN violation

[RULE-06] Usage conditions MUST be reviewed and updated within 30 days of any change in user role, project assignment, or security clearance.
[VALIDATION] IF (role_change_date OR project_change_date OR clearance_change_date) > 0 AND usage_conditions_review_date > 30_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Usage Condition Definition - Establish standard usage conditions for each account type and risk level
- [PROC-02] Technical Implementation - Configure system controls to enforce defined usage conditions
- [PROC-03] Violation Response - Investigate and respond to usage condition violations within defined timeframes
- [PROC-04] Condition Review - Periodic review and update of usage conditions based on risk assessments

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, system changes, regulatory updates, usage pattern anomalies

## 7. SCENARIO PATTERNS
[SCENARIO-01: After-Hours Administrative Access]
IF account_type = "administrative"
AND access_time NOT IN business_hours
AND emergency_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Account Beyond Project End]
IF account_type = "contractor"
AND current_date > project_end_date
AND account_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Shared Account Without Session Limits]
IF account_type = "shared"
AND session_duration_limit = NULL
AND concurrent_session_limit = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Service Account Interactive Login]
IF account_type = "service"
AND login_type = "interactive"
AND usage_conditions_allow_interactive = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Emergency Account Extended Use]
IF account_type = "emergency"
AND account_age > 72_hours
AND justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Usage conditions defined for system accounts | [RULE-01] |
| Usage conditions technically enforced | [RULE-02] |
| Time-based restrictions implemented | [RULE-03] |
| Violation monitoring and alerting | [RULE-04] |
| Privileged account restrictions | [RULE-05] |
| Condition review and updates | [RULE-06] |