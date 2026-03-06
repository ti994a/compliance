# POLICY: SC-24: Fail in Known State

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-24 |
| NIST Control | SC-24: Fail in Known State |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system failure, known state, fail-safe, state preservation, system recovery, availability |

## 1. POLICY STATEMENT
All information systems and components must be configured to fail to a predetermined, secure state when system failures occur. System state information must be preserved during failures to enable rapid recovery and minimize disruption to business operations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All mission-critical and business systems |
| Development Systems | YES | Systems processing sensitive data |
| Test Systems | CONDITIONAL | Only if processing production data |
| Network Components | YES | Routers, switches, firewalls, load balancers |
| Security Controls | YES | Authentication, authorization, monitoring systems |
| Third-party Systems | YES | Vendor systems processing company data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Architects | • Define fail-safe states for system designs<br>• Document state preservation requirements<br>• Review failure scenarios during design |
| System Administrators | • Configure systems to fail to known states<br>• Implement state preservation mechanisms<br>• Test failure recovery procedures |
| Security Engineers | • Validate fail-safe configurations maintain security<br>• Monitor failure events and responses<br>• Assess security implications of failure states |

## 4. RULES

[RULE-01] All information systems MUST be configured to fail to a predetermined secure state that maintains confidentiality, integrity, and availability requirements.
[VALIDATION] IF system_failure_occurs = TRUE AND fail_state ≠ "predetermined_secure_state" THEN violation

[RULE-02] System components MUST preserve critical state information during failure events to enable recovery within defined RTO/RPO objectives.
[VALIDATION] IF system_failure = TRUE AND state_information_preserved = FALSE THEN violation

[RULE-03] Fail-safe configurations MUST be documented and include specific failure types, resulting safe states, and recovery procedures.
[VALIDATION] IF fail_safe_documentation = "incomplete" OR fail_safe_documentation = "missing" THEN violation

[RULE-04] Systems MUST NOT fail to states that could cause unauthorized access, data exposure, or compromise security controls.
[VALIDATION] IF failure_state = "open" OR failure_state = "bypass_security" THEN critical_violation

[RULE-05] Fail-safe mechanisms MUST be tested quarterly and after any significant system changes.
[VALIDATION] IF last_fail_safe_test > 90_days OR system_change_without_test = TRUE THEN violation

[RULE-06] Critical systems MUST implement redundant fail-safe mechanisms to prevent single points of failure.
[VALIDATION] IF system_criticality = "high" AND fail_safe_redundancy = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Fail-Safe State Definition - Document predetermined secure states for each system type
- [PROC-02] State Preservation Implementation - Configure and test state information backup mechanisms  
- [PROC-03] Failure Response Testing - Quarterly validation of fail-safe mechanisms and recovery procedures
- [PROC-04] Failure Event Analysis - Post-incident review of failure responses and improvements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Major system failures, security incidents, significant architecture changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Network Security Device Failure]
IF device_type = "firewall" 
AND device_failure = TRUE
AND fail_state = "fail_open"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Authentication System Failure]
IF system_type = "authentication"
AND system_failure = TRUE  
AND fail_state = "allow_all_access"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Database System Failure with State Preservation]
IF system_type = "database"
AND system_failure = TRUE
AND state_information_preserved = TRUE
AND fail_state = "read_only_secure"
THEN compliance = TRUE

[SCENARIO-04: Load Balancer Failure]
IF component_type = "load_balancer"
AND failure_occurred = TRUE
AND traffic_routing = "secure_backend_only"
AND state_preserved = TRUE
THEN compliance = TRUE

[SCENARIO-05: Untested Fail-Safe Configuration]
IF fail_safe_configured = TRUE
AND last_test_date > 90_days
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Types of system failures for which components fail to known state are defined | [RULE-03] |
| System components fail to known secure state during failures | [RULE-01] |
| System state information is preserved during failures | [RULE-02] |
| Fail-safe mechanisms prevent insecure failure states | [RULE-04] |