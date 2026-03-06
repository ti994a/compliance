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
The organization MUST implement non-persistent system components and services that are initiated in a known, trusted state and automatically terminated upon end of session or use. This approach mitigates advanced persistent threats by reducing the attack surface and time available for adversaries to exploit vulnerabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Virtual machines | YES | All VMs in production and development |
| Container instances | YES | Kubernetes pods, Docker containers |
| Temporary workstations | YES | Kiosk systems, guest access points |
| Critical application services | CONDITIONAL | High-risk or internet-facing services |
| Database servers | NO | Persistent storage required |
| Network infrastructure | NO | Requires continuous availability |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure non-persistent components with automated termination<br>• Monitor component lifecycle and refresh cycles<br>• Maintain known-good baseline images |
| Security Operations | • Define refresh frequencies based on threat assessment<br>• Monitor for APT indicators during component lifecycles<br>• Validate proper termination of sessions |
| Infrastructure Teams | • Implement virtualization platforms supporting non-persistence<br>• Ensure adequate resources for component refresh cycles<br>• Maintain backup and recovery capabilities |

## 4. RULES
[RULE-01] Non-persistent system components MUST be initiated from a known, trusted baseline state that has been security-hardened and approved.
[VALIDATION] IF component_startup = TRUE AND baseline_verified = FALSE THEN violation

[RULE-02] Non-persistent components MUST be automatically terminated upon session end or after maximum session duration of 8 hours for user sessions and 24 hours for service components.
[VALIDATION] IF session_duration > max_allowed_duration AND auto_terminate = FALSE THEN violation

[RULE-03] Critical internet-facing services MUST implement non-persistent instances with refresh cycles not exceeding 72 hours.
[VALIDATION] IF service_criticality = "high" AND internet_facing = TRUE AND refresh_interval > 72_hours THEN violation

[RULE-04] Non-persistent components MUST NOT retain user data, configurations, or logs beyond the session lifecycle without explicit data handling procedures.
[VALIDATION] IF component_terminated = TRUE AND persistent_data_found = TRUE AND data_handling_exception = FALSE THEN violation

[RULE-05] Organizations MUST maintain an inventory of all non-persistent components including refresh frequencies and termination triggers.
[VALIDATION] IF non_persistent_component = TRUE AND inventory_record = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Baseline Image Management - Creation and maintenance of security-hardened baseline images
- [PROC-02] Component Lifecycle Management - Automated provisioning, monitoring, and termination processes
- [PROC-03] Session Termination - Procedures for graceful and forced termination of non-persistent components
- [PROC-04] Refresh Scheduling - Risk-based determination of component refresh frequencies
- [PROC-05] Incident Response for Non-persistent Systems - Modified IR procedures accounting for component volatility

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving APTs, major infrastructure changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: Virtual Desktop Session Timeout]
IF component_type = "virtual_desktop"
AND session_active = TRUE
AND session_duration > 8_hours
AND auto_terminate = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Container Refresh Compliance]
IF component_type = "container"
AND internet_facing = TRUE
AND last_refresh > 72_hours
AND business_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Proper Session Termination]
IF session_ended = TRUE
AND component_terminated = TRUE
AND data_persistence = FALSE
AND termination_time < 5_minutes
THEN compliance = TRUE

[SCENARIO-04: Baseline Image Verification]
IF component_startup = TRUE
AND baseline_hash_verified = TRUE
AND security_hardening_applied = TRUE
THEN compliance = TRUE

[SCENARIO-05: Unauthorized Data Persistence]
IF component_type = "non_persistent"
AND session_terminated = TRUE
AND user_data_retained = TRUE
AND retention_authorized = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Non-persistent components defined and implemented | RULE-05 |
| Components initiated in known state | RULE-01 |
| Components terminated upon session end | RULE-02, RULE-03 |
| Proper lifecycle management | RULE-04, RULE-05 |