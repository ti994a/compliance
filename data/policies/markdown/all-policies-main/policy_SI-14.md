# POLICY: SI-14: Non-persistence

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-14 |
| NIST Control | SI-14: Non-persistence |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | non-persistence, APT, virtualization, session termination, known state, system components |

## 1. POLICY STATEMENT
The organization SHALL implement non-persistent system components and services that are initiated in a known, trusted state and automatically terminated upon end of session or use. This approach mitigates advanced persistent threats by reducing the attack surface and time window available to adversaries.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Virtual machines | YES | All virtualized workloads |
| Container instances | YES | Ephemeral containers and services |
| User workstations | CONDITIONAL | High-risk roles and privileged users |
| Database servers | CONDITIONAL | Non-production and test environments |
| Network appliances | NO | Core infrastructure components |
| Mobile devices | CONDITIONAL | BYOD and contractor devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Infrastructure Team | • Configure non-persistent components<br>• Implement automated refresh mechanisms<br>• Monitor component lifecycle |
| Security Operations | • Define refresh frequency requirements<br>• Monitor for persistence violations<br>• Validate known state baselines |
| System Administrators | • Execute refresh procedures<br>• Maintain configuration baselines<br>• Document exceptions and approvals |

## 4. RULES
[RULE-01] Non-persistent system components MUST be initiated from a known, trusted baseline state that has been security-approved and documented.
[VALIDATION] IF component_initialization = TRUE AND baseline_state != "approved_baseline" THEN violation

[RULE-02] Non-persistent components MUST be automatically terminated upon session end or after maximum session duration of 8 hours for standard users and 4 hours for privileged users.
[VALIDATION] IF session_active = TRUE AND user_type = "standard" AND session_duration > 8_hours THEN violation
[VALIDATION] IF session_active = TRUE AND user_type = "privileged" AND session_duration > 4_hours THEN violation

[RULE-03] Critical system components designated as non-persistent MUST be refreshed at least every 24 hours or upon detection of suspicious activity.
[VALIDATION] IF component_type = "critical" AND last_refresh_time > 24_hours AND suspicious_activity = FALSE THEN violation
[VALIDATION] IF component_type = "critical" AND suspicious_activity = TRUE AND refresh_initiated = FALSE THEN critical_violation

[RULE-04] Organizations MUST maintain an inventory of all non-persistent components including refresh frequency, baseline versions, and termination triggers.
[VALIDATION] IF component_non_persistent = TRUE AND inventory_documented = FALSE THEN violation

[RULE-05] Non-persistent services MUST NOT retain user data, configurations, or logs beyond session termination unless explicitly approved and documented.
[VALIDATION] IF session_terminated = TRUE AND data_persisted = TRUE AND approval_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Baseline Management - Establish and maintain approved baseline images
- [PROC-02] Automated Refresh Implementation - Configure automatic termination and refresh cycles
- [PROC-03] Exception Approval Process - Document and approve persistence requirements
- [PROC-04] Incident Response Integration - Trigger immediate refresh upon security events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, technology changes, regulatory updates, APT intelligence updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Privileged User Session Timeout]
IF user_type = "privileged"
AND session_duration > 4_hours
AND auto_termination = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Virtual Machine Persistence]
IF component_type = "virtual_machine"
AND designated_non_persistent = TRUE
AND last_refresh > 24_hours
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Container Data Retention]
IF service_type = "container"
AND session_terminated = TRUE
AND user_data_retained = TRUE
AND retention_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Suspicious Activity Response]
IF suspicious_activity_detected = TRUE
AND component_type = "critical"
AND immediate_refresh_triggered = TRUE
AND refresh_completed_within_1_hour = TRUE
THEN compliance = TRUE

[SCENARIO-05: Baseline Integrity]
IF component_initialization = TRUE
AND baseline_verification = "passed"
AND known_state_confirmed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Non-persistent components defined and implemented | [RULE-04] |
| Components initiated in known state | [RULE-01] |
| Components terminated upon session end | [RULE-02], [RULE-03] |
| Refresh frequency established | [RULE-03] |
| Data retention controls | [RULE-05] |