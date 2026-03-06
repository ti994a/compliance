# POLICY: AU-12.3: Changes by Authorized Individuals

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-12.3 |
| NIST Control | AU-12.3: Changes by Authorized Individuals |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit logging, authorized changes, logging configuration, event criteria, time thresholds |

## 1. POLICY STATEMENT
Organizations must provide and implement capabilities for authorized individuals to dynamically change system logging configurations based on defined event criteria and within established time thresholds. All logging configuration changes must be performed only by pre-authorized roles with appropriate justification and documentation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid systems |
| System administrators | YES | Must have defined authorization for logging changes |
| Security operations teams | YES | Authorized for threat-based logging adjustments |
| Application systems | YES | Custom applications with configurable logging |
| Network infrastructure | YES | Routers, switches, firewalls with logging capabilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement logging configuration changes within authorized scope<br>• Document all logging modifications<br>• Ensure changes meet defined time thresholds |
| Security Operations Center | • Monitor for unauthorized logging changes<br>• Authorize temporary logging extensions for threat response<br>• Validate logging changes comply with event criteria |
| Audit Manager | • Define authorized individuals and roles for logging changes<br>• Establish event criteria and time thresholds<br>• Review logging configuration change reports |

## 4. RULES
[RULE-01] Organizations MUST define and document specific individuals or roles authorized to change logging configurations on each system component.
[VALIDATION] IF logging_change_attempted = TRUE AND user_role NOT IN authorized_logging_roles THEN violation

[RULE-02] Logging configuration changes MUST be based on pre-defined, selectable event criteria that specify when modifications are permitted.
[VALIDATION] IF logging_change_made = TRUE AND event_criteria_documented = FALSE THEN violation

[RULE-03] All logging configuration changes MUST be completed within established time thresholds: emergency threat response within 15 minutes, planned changes within 4 hours, routine adjustments within 24 hours.
[VALIDATION] IF change_type = "emergency" AND completion_time > 15_minutes THEN critical_violation
[VALIDATION] IF change_type = "planned" AND completion_time > 4_hours THEN violation
[VALIDATION] IF change_type = "routine" AND completion_time > 24_hours THEN violation

[RULE-04] System components MUST provide technical capability to modify logging configurations without requiring system restart or service interruption.
[VALIDATION] IF logging_change_capability = FALSE OR requires_restart = TRUE THEN violation

[RULE-05] All logging configuration changes MUST be documented with justification, authorized approver, timestamp, and rollback procedures.
[VALIDATION] IF logging_change_made = TRUE AND (justification = NULL OR approver = NULL OR timestamp = NULL) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Logging Authorization Matrix - Define and maintain roles authorized for logging changes
- [PROC-02] Event Criteria Documentation - Establish selectable criteria for logging modifications
- [PROC-03] Emergency Logging Response - Rapid logging configuration for security incidents
- [PROC-04] Logging Change Documentation - Record all configuration modifications and approvals

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents requiring logging changes, system architecture changes, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Emergency Threat Response Logging]
IF security_incident = "active"
AND logging_extension_required = TRUE
AND authorized_role = "SOC_analyst"
AND change_completion_time <= 15_minutes
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Logging Modification]
IF logging_configuration_changed = TRUE
AND user_role NOT IN authorized_logging_roles
AND change_documentation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Planned Logging Reduction]
IF system_resources = "constrained"
AND logging_reduction_planned = TRUE
AND event_criteria_met = TRUE
AND completion_time <= 4_hours
THEN compliance = TRUE

[SCENARIO-04: Missing Change Documentation]
IF logging_change_made = TRUE
AND authorized_user = TRUE
AND (justification = NULL OR timestamp = NULL)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: System Restart Required for Logging]
IF logging_change_requested = TRUE
AND system_capability_requires_restart = TRUE
AND service_interruption = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Authorized individuals/roles defined for logging changes | [RULE-01] |
| Selectable event criteria established for logging modifications | [RULE-02] |
| Time thresholds defined and implemented for logging changes | [RULE-03] |
| Technical capability provided for dynamic logging configuration | [RULE-04] |
| Logging change implementation documented and tracked | [RULE-05] |