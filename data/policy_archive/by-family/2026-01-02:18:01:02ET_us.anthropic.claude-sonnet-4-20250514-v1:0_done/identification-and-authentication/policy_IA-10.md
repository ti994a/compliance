```markdown
# POLICY: IA-10: Adaptive Authentication

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-10 |
| NIST Control | IA-10: Adaptive Authentication |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | adaptive authentication, supplemental authentication, suspicious behavior, multi-factor authentication, risk-based authentication |

## 1. POLICY STATEMENT
The organization SHALL implement adaptive authentication mechanisms that require supplemental authentication techniques when users access systems under specific high-risk circumstances or exhibit suspicious behavior patterns. Adaptive authentication supplements but does not replace multi-factor authentication requirements and dynamically adjusts authentication strength based on assessed risk levels.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, hybrid, and on-premises systems |
| All user types | YES | Employees, contractors, partners, privileged users |
| Service accounts | CONDITIONAL | When interactive access is possible |
| Emergency access accounts | YES | Enhanced monitoring required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define adaptive authentication policy and risk thresholds<br>• Approve supplemental authentication mechanisms<br>• Review adaptive authentication effectiveness |
| System Administrators | • Implement adaptive authentication controls<br>• Configure risk-based triggers and thresholds<br>• Monitor authentication anomalies |
| Security Operations Center | • Monitor adaptive authentication alerts<br>• Investigate suspicious authentication patterns<br>• Coordinate incident response for authentication anomalies |

## 4. RULES

[RULE-01] Organizations MUST define specific circumstances that trigger supplemental authentication requirements beyond standard multi-factor authentication.
[VALIDATION] IF adaptive_auth_triggers = "undefined" OR adaptive_auth_triggers = "null" THEN violation

[RULE-02] Supplemental authentication MUST be required when users access data volumes exceeding 150% of their 30-day baseline or access data types outside their normal role permissions.
[VALIDATION] IF data_access_volume > (baseline_30day * 1.5) AND supplemental_auth_required = FALSE THEN violation
[VALIDATION] IF data_type NOT IN user_role_permissions AND supplemental_auth_required = FALSE THEN violation

[RULE-03] Users accessing systems from suspicious network locations or unrecognized devices MUST complete supplemental authentication before system access is granted.
[VALIDATION] IF (source_ip IN suspicious_networks OR device_trust_level = "unknown") AND supplemental_auth_completed = FALSE THEN violation

[RULE-04] Adaptive authentication mechanisms MUST log all trigger events, supplemental authentication attempts, and access decisions for audit purposes.
[VALIDATION] IF adaptive_auth_event_occurred = TRUE AND audit_log_created = FALSE THEN violation

[RULE-05] Organizations MUST review and update adaptive authentication triggers and thresholds quarterly based on threat intelligence and user behavior analytics.
[VALIDATION] IF last_trigger_review > 90_days THEN violation

[RULE-06] Failed supplemental authentication attempts exceeding 3 consecutive failures MUST result in account lockout and security team notification.
[VALIDATION] IF consecutive_supplemental_auth_failures > 3 AND account_locked = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Adaptive Authentication Configuration - Define risk triggers, thresholds, and supplemental mechanisms
- [PROC-02] Suspicious Behavior Detection - Establish baseline user patterns and anomaly detection
- [PROC-03] Supplemental Authentication Response - Handle adaptive authentication challenges and failures
- [PROC-04] Adaptive Authentication Monitoring - Review logs and adjust risk parameters

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Quarterly
- Triggering events: Security incidents involving authentication bypass, new threat intelligence, significant changes to user access patterns

## 7. SCENARIO PATTERNS

[SCENARIO-01: Excessive Data Access]
IF user_data_access_volume > (30day_baseline * 2.0)
AND time_period = "single_session"
AND supplemental_auth_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Geographic Anomaly Access]
IF user_location_distance > 500_miles_from_last_login
AND time_between_logins < 4_hours
AND supplemental_auth_required = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Privileged Account After Hours]
IF user_role = "privileged"
AND access_time OUTSIDE business_hours
AND data_sensitivity = "confidential"
AND supplemental_auth_completed = TRUE
THEN compliance = TRUE

[SCENARIO-04: Cross-Departmental Data Access]
IF user_department = "HR"
AND accessed_data_department = "Finance"
AND business_justification = "documented"
AND supplemental_auth_completed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Multiple Failed Supplemental Auth]
IF supplemental_auth_failures = 4
AND account_status = "active"
AND security_team_notified = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Define circumstances requiring supplemental authentication | [RULE-01] |
| Implement risk-based authentication triggers | [RULE-02], [RULE-03] |
| Maintain audit logs for adaptive authentication events | [RULE-04] |
| Regular review of authentication parameters | [RULE-05] |
| Handle supplemental authentication failures | [RULE-06] |
```