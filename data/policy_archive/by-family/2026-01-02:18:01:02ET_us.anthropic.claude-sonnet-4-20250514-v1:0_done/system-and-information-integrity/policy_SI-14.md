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
The organization SHALL implement non-persistent system components and services that are initiated in a known, trusted state and automatically terminated upon end of session or use. This approach mitigates advanced persistent threat (APT) risks by reducing adversary targeting windows and available attack surfaces.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Virtual machines | YES | All production and development VMs |
| Container instances | YES | All containerized applications and services |
| Temporary compute resources | YES | Cloud instances, sandbox environments |
| Critical system components | CONDITIONAL | Based on risk assessment and business requirements |
| User workstations | CONDITIONAL | High-risk users and privileged access workstations |
| Network appliances | NO | Unless specifically configured for non-persistence |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure non-persistent components<br>• Monitor session termination processes<br>• Maintain known-state baselines |
| Security Operations | • Define non-persistence requirements<br>• Monitor compliance with termination policies<br>• Assess APT risk mitigation effectiveness |
| Cloud Infrastructure Team | • Implement automated provisioning/deprovisioning<br>• Ensure proper state management<br>• Configure session timeout parameters |

## 4. RULES

[RULE-01] Non-persistent system components MUST be initiated from a verified known state baseline that has been security-hardened and approved.
[VALIDATION] IF component_initiated = TRUE AND baseline_verified = FALSE THEN violation

[RULE-02] Non-persistent services SHALL terminate automatically upon session end, user logout, or maximum session timeout (not exceeding 24 hours for standard services, 4 hours for privileged services).
[VALIDATION] IF session_active = TRUE AND session_duration > max_timeout THEN violation
[VALIDATION] IF user_logout = TRUE AND service_terminated = FALSE AND termination_time > 5_minutes THEN violation

[RULE-03] Organizations MUST define and document which system components and services require non-persistent implementation based on risk assessment and threat modeling.
[VALIDATION] IF component_classification = "high_risk" AND non_persistence_required = TRUE AND implementation_status = "not_implemented" THEN violation

[RULE-04] Non-persistent components SHALL NOT retain user data, configurations, or state information beyond the active session unless explicitly required and documented.
[VALIDATION] IF session_ended = TRUE AND persistent_data_found = TRUE AND exception_documented = FALSE THEN violation

[RULE-05] Refresh cycles for non-persistent components MUST occur at frequencies sufficient to prevent APT exploitation but not compromise system stability (minimum weekly, maximum daily for high-risk components).
[VALIDATION] IF component_risk = "high" AND last_refresh > 24_hours THEN violation
[VALIDATION] IF component_risk = "medium" AND last_refresh > 168_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Non-Persistent Component Classification - Risk-based assessment to determine non-persistence requirements
- [PROC-02] Known State Baseline Management - Creation and maintenance of security-hardened baseline images
- [PROC-03] Automated Termination Configuration - Setup of session timeouts and automatic cleanup processes
- [PROC-04] Refresh Cycle Management - Scheduled refresh of non-persistent components based on risk levels

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving persistent threats, changes to threat landscape, new virtualization technologies

## 7. SCENARIO PATTERNS

[SCENARIO-01: Virtual Desktop Session Timeout]
IF user_type = "privileged"
AND session_duration > 4_hours
AND auto_termination = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Container Persistence After Job Completion]
IF container_type = "batch_job"
AND job_status = "completed"
AND container_running = TRUE
AND time_since_completion > 30_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: VM Refresh Cycle Compliance]
IF vm_classification = "high_risk"
AND last_refresh_date > 24_hours
AND business_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Known State Verification]
IF component_startup = TRUE
AND baseline_hash_verified = TRUE
AND security_controls_active = TRUE
THEN compliance = TRUE

[SCENARIO-05: Data Persistence Exception]
IF session_ended = TRUE
AND data_retained = TRUE
AND exception_approved = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Non-persistent components defined | RULE-03 |
| Components initiated in known state | RULE-01 |
| Components terminated upon session end | RULE-02 |
| Proper refresh cycle implementation | RULE-05 |
| Data retention controls | RULE-04 |