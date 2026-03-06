# POLICY: AC-3.8: Revocation of Access Authorizations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-3.8 |
| NIST Control | AC-3.8: Revocation of Access Authorizations |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | access revocation, security attributes, authorization timing, subject access, object access |

## 1. POLICY STATEMENT
The organization SHALL enforce immediate revocation of access authorizations when security attributes of subjects or objects change according to predefined timing rules. Access revocation timing rules MUST be documented and consistently applied across all systems and resources.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and hybrid environments |
| All user accounts | YES | Employees, contractors, service accounts |
| All system processes | YES | Automated processes acting on behalf of users |
| All data objects | YES | Files, databases, applications, network resources |
| Third-party systems | CONDITIONAL | When integrated with organization systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure automated revocation mechanisms<br>• Monitor revocation effectiveness<br>• Maintain revocation timing rules |
| Security Operations Center | • Monitor access revocation events<br>• Investigate revocation failures<br>• Escalate immediate revocation needs |
| Data Owners | • Define security attribute change triggers<br>• Approve revocation timing requirements<br>• Validate revocation completeness |

## 4. RULES
[RULE-01] Access revocation rules MUST be documented for each system, specifying timing requirements based on security attribute changes.
[VALIDATION] IF system_documented = TRUE AND revocation_rules_defined = TRUE THEN compliant

[RULE-02] Group membership changes MUST trigger access revocation within 15 minutes for high-impact systems and within 4 hours for moderate-impact systems.
[VALIDATION] IF group_membership_changed = TRUE AND system_impact = "high" AND revocation_time > 15_minutes THEN violation

[RULE-03] Security clearance or classification level changes MUST trigger immediate access revocation to resources requiring higher authorization.
[VALIDATION] IF clearance_level_decreased = TRUE AND higher_resource_access = TRUE AND revocation_time > 0_minutes THEN critical_violation

[RULE-04] Role-based access changes MUST be revoked before the next authentication attempt or within 1 hour, whichever occurs first.
[VALIDATION] IF role_changed = TRUE AND (next_auth_attempt = TRUE OR time_elapsed > 1_hour) AND access_active = TRUE THEN violation

[RULE-05] Systems unable to provide immediate revocation MUST implement compensating controls approved by the CISO.
[VALIDATION] IF immediate_revocation_capable = FALSE AND compensating_controls_approved = FALSE THEN violation

[RULE-06] Object security label changes MUST trigger immediate reevaluation of all active access sessions to that object.
[VALIDATION] IF object_label_changed = TRUE AND active_sessions_reevaluated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Access Revocation Configuration - Define and implement system-specific revocation timing rules
- [PROC-02] Security Attribute Monitoring - Continuously monitor for changes requiring access revocation
- [PROC-03] Compensating Controls Assessment - Evaluate and approve alternative revocation methods
- [PROC-04] Revocation Effectiveness Testing - Regularly validate revocation mechanisms function as intended

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving access revocation failures, system architecture changes, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Group Membership Removal]
IF user_removed_from_group = TRUE
AND system_impact_level = "high"
AND revocation_completed_time > 15_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Clearance Downgrade]
IF user_clearance_level = "decreased"
AND access_to_higher_classified_data = TRUE
AND revocation_time > 0_minutes
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Object Reclassification]
IF object_security_label = "increased"
AND active_user_sessions_exist = TRUE
AND session_reevaluation_performed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: System Without Immediate Capability]
IF system_immediate_revocation = FALSE
AND ciso_approved_compensating_controls = TRUE
AND compensating_controls_implemented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Role Change Delay]
IF user_role_changed = TRUE
AND next_authentication_attempt = FALSE
AND time_since_change > 1_hour
AND access_still_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Revocation enforcement for subject security attribute changes | [RULE-02], [RULE-03], [RULE-04] |
| Revocation enforcement for object security attribute changes | [RULE-06] |
| Defined timing rules for access revocations | [RULE-01] |
| Alternative approaches for immediate revocation | [RULE-05] |