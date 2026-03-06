# POLICY: AC-17.9: Disconnect or Disable Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-17.9 |
| NIST Control | AC-17.9: Disconnect or Disable Access |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | remote access, disconnect, disable, emergency response, incident response, privileged access |

## 1. POLICY STATEMENT
The organization SHALL maintain the capability to immediately disconnect or disable remote access to information systems within defined time periods based on system criticality and security requirements. This capability MUST be available 24/7 and executable without requiring physical access to systems or cooperation from remote users.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All remote access connections | YES | VPN, RDP, SSH, web portals, API access |
| Cloud-based systems | YES | Including SaaS, PaaS, IaaS platforms |
| Third-party vendor access | YES | Contractor and partner remote connections |
| Emergency access accounts | YES | Including break-glass accounts |
| Mobile device connections | YES | Corporate and BYOD devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Monitor remote access sessions<br>• Execute emergency disconnection procedures<br>• Maintain 24/7 disconnect capability |
| Network Operations Center (NOC) | • Implement technical disconnect mechanisms<br>• Maintain network-level access controls<br>• Support emergency response procedures |
| System Administrators | • Configure system-level disconnect capabilities<br>• Test disconnect mechanisms quarterly<br>• Document disconnect procedures |

## 4. RULES
[RULE-01] Critical systems MUST provide the capability to disconnect remote access within 5 minutes of authorization.
[VALIDATION] IF system_criticality = "critical" AND disconnect_time > 5_minutes THEN violation

[RULE-02] High-impact systems MUST provide the capability to disconnect remote access within 15 minutes of authorization.
[VALIDATION] IF system_impact = "high" AND disconnect_time > 15_minutes THEN violation

[RULE-03] Moderate and low-impact systems MUST provide the capability to disconnect remote access within 60 minutes of authorization.
[VALIDATION] IF system_impact IN ["moderate", "low"] AND disconnect_time > 60_minutes THEN violation

[RULE-04] Emergency disconnect procedures MUST be executable without requiring cooperation from the remote user or physical access to systems.
[VALIDATION] IF disconnect_requires_user_cooperation = TRUE OR disconnect_requires_physical_access = TRUE THEN critical_violation

[RULE-05] Disconnect capabilities MUST be tested quarterly for all remote access methods and documented.
[VALIDATION] IF last_disconnect_test > 90_days THEN violation

[RULE-06] Privileged remote access sessions MUST be capable of immediate termination (within 60 seconds) regardless of system criticality.
[VALIDATION] IF access_level = "privileged" AND disconnect_capability > 60_seconds THEN violation

[RULE-07] All remote access disconnect events MUST be logged with timestamp, user identity, system accessed, and reason for disconnection.
[VALIDATION] IF disconnect_event_logged = FALSE OR log_missing_required_fields = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Emergency Remote Access Disconnection - Step-by-step procedures for SOC to disconnect remote access during security incidents
- [PROC-02] Quarterly Disconnect Testing - Procedures for testing and validating disconnect capabilities across all remote access methods
- [PROC-03] Remote Access Monitoring - Continuous monitoring procedures for detecting suspicious remote access activity
- [PROC-04] Incident Response Integration - Procedures for integrating disconnect capabilities with incident response workflows

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving remote access, system architecture changes, new remote access technologies

## 7. SCENARIO PATTERNS
[SCENARIO-01: Security Incident Response]
IF security_incident = TRUE
AND remote_access_sessions_active = TRUE
AND incident_severity = "high"
AND disconnect_time <= defined_timeframe
THEN compliance = TRUE

[SCENARIO-02: Failed Emergency Disconnect]
IF emergency_disconnect_initiated = TRUE
AND disconnect_time > maximum_allowed_time
AND system_criticality = "critical"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Privileged Access Compromise]
IF user_access_level = "privileged"
AND compromise_suspected = TRUE
AND disconnect_capability > 60_seconds
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Untested Disconnect Mechanism]
IF remote_access_method = "active"
AND last_disconnect_test > 90_days
AND production_system = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Missing Disconnect Logging]
IF disconnect_event_occurred = TRUE
AND event_logged = FALSE
AND audit_trail_required = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Capability to disconnect remote access within defined time periods | RULE-01, RULE-02, RULE-03 |
| Emergency disconnect without user cooperation | RULE-04 |
| Regular testing of disconnect capabilities | RULE-05 |
| Privileged access immediate termination | RULE-06 |
| Audit trail for disconnect events | RULE-07 |