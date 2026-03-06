# POLICY: AC-3.5: Security-relevant Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-3.5 |
| NIST Control | AC-3.5: Security-relevant Information |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security-relevant information, access control, secure states, non-operable systems, maintenance |

## 1. POLICY STATEMENT
Access to security-relevant information SHALL be prevented except during secure, non-operable system states when systems are offline for authorized maintenance, troubleshooting, or administrative activities. Security-relevant information includes access control lists, firewall rules, security configuration parameters, and cryptographic key management data that could impact security function operation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing business/mission data |
| Development Systems | YES | When containing production security configurations |
| Test Systems | CONDITIONAL | Only if using production security data |
| Contractor Systems | YES | When accessing organizational security-relevant information |
| Personal Devices | NO | Not authorized to access security-relevant information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement technical controls preventing unauthorized access<br>• Document secure maintenance procedures<br>• Validate system state before accessing security-relevant information |
| Security Operations | • Monitor access to security-relevant information<br>• Define approved secure, non-operable system states<br>• Investigate unauthorized access attempts |
| IT Operations Manager | • Approve maintenance windows requiring security-relevant information access<br>• Ensure proper authorization documentation<br>• Coordinate secure state transitions |

## 4. RULES
[RULE-01] Access to security-relevant information MUST be prevented during normal operational system states through technical access controls.
[VALIDATION] IF system_state = "operational" AND access_attempt = "security_relevant_info" AND technical_control_bypass = TRUE THEN critical_violation

[RULE-02] Security-relevant information access SHALL only be permitted during documented secure, non-operable system states with proper authorization.
[VALIDATION] IF system_state != "secure_non_operable" AND security_info_access = TRUE AND emergency_exception = FALSE THEN violation

[RULE-03] Secure, non-operable system states MUST be formally defined and include offline maintenance, boot-up, troubleshooting, and shutdown phases.
[VALIDATION] IF system_state_definition = "undefined" OR maintenance_procedures = "undocumented" THEN compliance_gap

[RULE-04] All access to security-relevant information during secure states MUST be logged with administrator identity, timestamp, and business justification.
[VALIDATION] IF security_info_access = TRUE AND (log_entry = "missing" OR justification = "missing") THEN violation

[RULE-05] Emergency access to security-relevant information during operational states MUST be pre-approved through break-glass procedures and reviewed within 24 hours.
[VALIDATION] IF emergency_access = TRUE AND (pre_approval = FALSE OR review_time > 24_hours) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Secure State Definition - Document approved non-operable system states and transition procedures
- [PROC-02] Security-Relevant Information Classification - Identify and catalog information requiring protection
- [PROC-03] Maintenance Access Control - Establish authorization and logging requirements for maintenance access
- [PROC-04] Emergency Break-Glass - Define emergency access procedures and review requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized access, system architecture changes, new security-relevant information types

## 7. SCENARIO PATTERNS
[SCENARIO-01: Routine Maintenance Access]
IF system_state = "secure_non_operable"
AND maintenance_window = "approved"
AND administrator_access = "security_relevant_info"
AND logging_enabled = TRUE
THEN compliance = TRUE

[SCENARIO-02: Operational State Access Attempt]
IF system_state = "operational"
AND user_access_attempt = "firewall_rules"
AND emergency_justification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Emergency Access During Incident]
IF security_incident = "active"
AND system_state = "operational"
AND break_glass_approval = TRUE
AND access_type = "cryptographic_keys"
THEN compliance = TRUE
review_required_within = "24_hours"

[SCENARIO-04: Unauthorized Configuration Access]
IF user_role != "system_administrator"
AND access_target = "access_control_lists"
AND system_state = "operational"
AND authorization = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Contractor Maintenance Access]
IF user_type = "contractor"
AND system_state = "secure_non_operable"
AND escort_required = TRUE
AND escort_present = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Access to security-relevant information is prevented except during secure states | [RULE-01], [RULE-02] |
| Secure, non-operable system states are defined | [RULE-03] |
| Access controls are implemented for security-relevant information | [RULE-01], [RULE-04] |
| Emergency access procedures are established | [RULE-05] |