```markdown
# POLICY: SC-24: Fail in Known State

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-24 |
| NIST Control | SC-24: Fail in Known State |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system failure, known state, fail-safe, state preservation, availability, system recovery |

## 1. POLICY STATEMENT
All information systems and system components must be designed and configured to fail to a predetermined, secure state when system failures occur. System state information must be preserved during failures to enable rapid recovery and minimize disruption to business operations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All mission-critical and business systems |
| Development Systems | CONDITIONAL | Only if processing production data |
| Network Components | YES | Routers, switches, firewalls, load balancers |
| Security Controls | YES | Authentication, authorization, monitoring systems |
| Third-party Services | YES | Cloud services processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Architects | • Define fail-safe states for system designs<br>• Document state preservation requirements<br>• Validate failure mode specifications |
| System Administrators | • Configure systems to fail to known states<br>• Implement state preservation mechanisms<br>• Test failure scenarios regularly |
| Security Engineers | • Review fail-safe configurations for security implications<br>• Monitor failure events and responses<br>• Validate security posture during failures |

## 4. RULES
[RULE-01] All systems MUST be configured to fail to a predetermined secure state that maintains confidentiality, integrity, and availability requirements.
[VALIDATION] IF system_failure_occurs = TRUE AND current_state ≠ defined_secure_state THEN violation

[RULE-02] Critical system state information MUST be preserved during system failures to enable recovery within defined RTO objectives.
[VALIDATION] IF system_failure = TRUE AND state_preservation = FALSE AND system_criticality = "high" THEN critical_violation

[RULE-03] Fail-safe states MUST be documented and approved by system owners and security teams before system deployment.
[VALIDATION] IF system_deployed = TRUE AND fail_safe_documentation = FALSE THEN violation

[RULE-04] Systems MUST NOT fail to states that could cause data exposure, unauthorized access, or safety hazards.
[VALIDATION] IF failure_state = "open" OR failure_state = "bypass" OR failure_state = "undefined" THEN critical_violation

[RULE-05] Failure scenarios and recovery procedures MUST be tested at least annually or after significant system changes.
[VALIDATION] IF last_failure_test > 365_days OR (major_change = TRUE AND post_change_test = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Failure State Definition - Document secure failure states for each system component
- [PROC-02] State Preservation Implementation - Configure mechanisms to preserve critical system state data
- [PROC-03] Failure Testing Protocol - Regular testing of system failure scenarios and recovery procedures
- [PROC-04] Incident Response for System Failures - Response procedures when systems fail outside known states

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, security incidents involving system failures, technology refresh cycles

## 7. SCENARIO PATTERNS
[SCENARIO-01: Database Server Failure]
IF database_server_failure = TRUE
AND current_state = "secure_readonly"
AND data_integrity_maintained = TRUE
THEN compliance = TRUE

[SCENARIO-02: Firewall Failure to Open State]
IF firewall_failure = TRUE
AND failure_state = "allow_all"
AND traffic_blocked = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Authentication System Failure]
IF auth_system_failure = TRUE
AND failure_state = "deny_all"
AND state_data_preserved = TRUE
THEN compliance = TRUE

[SCENARIO-04: Load Balancer Failure Without State Preservation]
IF load_balancer_failure = TRUE
AND session_state_preserved = FALSE
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Untested Failure Configuration]
IF system_deployed = TRUE
AND failure_mode_documented = TRUE
AND last_failure_test > 365_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Types of system failures for which components fail to known state are defined | [RULE-03] |
| Fail to a known system state is defined for system components | [RULE-01] |
| System state information preserved in event of failure is defined | [RULE-02] |
| System components fail to known secure state | [RULE-01], [RULE-04] |
| State information is preserved during failures | [RULE-02] |
| Failure scenarios are tested and validated | [RULE-05] |
```